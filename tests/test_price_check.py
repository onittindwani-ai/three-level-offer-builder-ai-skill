import os
import subprocess
import sys
import unittest

ROOT = os.path.join(os.path.dirname(__file__), "..")
sys.path.insert(0, os.path.join(ROOT, "scripts"))
import price_check as pc  # noqa: E402

SCRIPT = os.path.join(ROOT, "scripts", "price_check.py")
CLEANING = [("Tidy", 918, 1699), ("Spotless", 1938, 3599), ("Move in ready", 5151, 9499)]


class Math(unittest.TestCase):
    def test_minimum_price(self):
        self.assertAlmostEqual(pc.minimum_price(1000, 0.5), 2000)
        self.assertAlmostEqual(pc.minimum_price(1000, 0.3), 1000 / 0.7)

    def test_bad_margin(self):
        with self.assertRaises(ValueError):
            pc.minimum_price(100, 1.2)

    def test_clean_price_never_below(self):
        for v in [12, 449.2, 999, 1000.01, 1669, 3523.6, 9365.5, 15020, 99999, 123456]:
            self.assertGreaterEqual(pc.clean_price(v), v, v)

    def test_clean_price_shapes(self):
        self.assertEqual(pc.clean_price(1669), 1699)
        self.assertEqual(pc.clean_price(3523.6), 3599)
        self.assertEqual(pc.clean_price(9365.5), 9399)
        self.assertEqual(pc.clean_price(15020), 15500)

    def test_suggest(self):
        s = pc.suggest(1938, 0.45)
        self.assertGreaterEqual(s["suggested_price"], s["minimum_price"])


class Checks(unittest.TestCase):
    def test_worked_example_passes(self):
        r = pc.check(CLEANING, 0.45)
        self.assertTrue(r["ok"], r)
        self.assertEqual(r["warnings"], [])

    def test_loss_is_a_problem(self):
        r = pc.check([("A", 1000, 900), ("B", 1500, 3000), ("C", 3000, 9000)])
        self.assertTrue(any("loses money" in p for p in r["problems"]))

    def test_low_margin_warns(self):
        r = pc.check([("A", 900, 1000), ("B", 1500, 3000), ("C", 3000, 9000)], 0.4)
        self.assertTrue(any("below your target" in w for w in r["warnings"]))

    def test_generic_names_warn(self):
        r = pc.check([("Basic", 100, 300), ("Standard", 200, 900), ("Premium", 400, 2700)])
        self.assertEqual(sum("generic name" in w for w in r["warnings"]), 3)

    def test_prices_must_rise(self):
        self.assertFalse(pc.check([("A", 100, 500), ("B", 100, 400), ("C", 100, 2000)])["ok"])

    def test_small_gap_warns(self):
        r = pc.check([("A", 100, 1000), ("B", 100, 1200), ("C", 100, 5000)])
        self.assertTrue(any("level 1 may take" in w for w in r["warnings"]))

    def test_big_gap_warns(self):
        r = pc.check([("A", 100, 1000), ("B", 100, 2000), ("C", 100, 20000)])
        self.assertTrue(any("truly limited" in w for w in r["warnings"]))

    def test_two_levels_warn(self):
        r = pc.check([("A", 100, 500), ("B", 100, 1500)])
        self.assertTrue(any("exactly 3" in w for w in r["warnings"]))


class CommandLine(unittest.TestCase):
    def run_cli(self, *args):
        return subprocess.run([sys.executable, SCRIPT, *args], capture_output=True, text=True)

    def test_self_test(self):
        self.assertEqual(self.run_cli("--self-test").returncode, 0)

    def test_pass(self):
        r = self.run_cli("--level", "Tidy", "918", "1699", "--level", "Spotless", "1938", "3599",
                         "--level", "Move in ready", "5151", "9499", "--margin", "0.45")
        self.assertEqual(r.returncode, 0, r.stdout)
        self.assertIn("PASS", r.stdout)

    def test_fail(self):
        r = self.run_cli("--level", "A", "1000", "900", "--level", "B", "1", "3000", "--level", "C", "1", "9000")
        self.assertEqual(r.returncode, 1)

    def test_suggest_needs_margin(self):
        self.assertEqual(self.run_cli("--suggest", "1000").returncode, 2)

    def test_suggest_json(self):
        r = self.run_cli("--suggest", "1000", "--margin", "0.5", "--json")
        self.assertIn('"suggested_price"', r.stdout)

    def test_bad_number(self):
        self.assertEqual(self.run_cli("--level", "A", "x", "1", "--level", "B", "1", "2", "--level", "C", "1", "3").returncode, 2)

    def test_no_args(self):
        self.assertEqual(self.run_cli().returncode, 2)


if __name__ == "__main__":
    unittest.main()
