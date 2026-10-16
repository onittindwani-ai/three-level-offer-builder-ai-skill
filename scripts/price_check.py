#!/usr/bin/env python3
"""Check a 3 level offer: does every level make money, are the gaps sensible, are the names clear?

No dependencies (Python 3.9 or newer). It only does arithmetic on the numbers you give it.

Usage:
  python scripts/price_check.py --level "Tidy" 918 1699 --level "Spotless" 1938 3599 --level "Move in ready" 5151 9499 --margin 0.45
      Each --level is: NAME FULL_COST PRICE (in order: easy yes, hero, premium).
  python scripts/price_check.py --suggest 1938 --margin 0.45
      Suggest a clean price for a full cost and a target margin.
  python scripts/price_check.py ... --json
  python scripts/price_check.py --self-test

Exit code: 0 when there are no problems, 1 when a problem is found, 2 for a usage error.
"""
import argparse
import json
import math
import sys

GENERIC_NAMES = {"basic", "standard", "premium", "pro", "plus", "lite", "silver", "gold", "platinum", "bronze",
                 "starter", "advanced", "elite", "deluxe", "economy", "regular", "max"}


def minimum_price(cost, margin):
    """The lowest price that gives the target margin: cost / (1 - margin)."""
    if not 0 <= margin < 1:
        raise ValueError("margin must be between 0 and 1, for example 0.45 for 45%")
    return cost / (1 - margin)


def clean_price(value):
    """Round UP to a clean, easy to say price."""
    if value <= 0:
        return 0
    if value < 1000:
        step = 50
        rounded = math.ceil(value / step) * step - 1
        return rounded if rounded >= value else rounded + step
    if value < 10000:
        return int(math.ceil(value / 100.0) * 100 - 1)
    if value < 100000:
        return int(math.ceil(value / 500.0) * 500)
    return int(math.ceil(value / 5000.0) * 5000)


def suggest(cost, margin):
    low = minimum_price(cost, margin)
    return {"full_cost": cost, "target_margin": margin, "minimum_price": round(low, 2), "suggested_price": clean_price(low)}


def check(levels, margin=None):
    """levels: list of (name, full_cost, price) in order easy yes, hero, premium."""
    problems, warnings, rows = [], [], []
    if len(levels) != 3:
        warnings.append("this works best with exactly 3 levels (you gave %d)" % len(levels))
    for name, cost, price in levels:
        profit = price - cost
        m = profit / price if price > 0 else 0.0
        rows.append({"name": name, "full_cost": cost, "price": price, "profit": round(profit, 2), "margin": round(m, 4)})
        if price <= 0 or cost < 0:
            problems.append("%s: cost and price must be positive numbers" % name)
        elif price <= cost:
            problems.append("%s loses money: price %s is not above full cost %s" % (name, price, cost))
        elif margin is not None and m < margin:
            warnings.append("%s margin is %.0f%%, below your target %.0f%% (minimum price %.0f)"
                            % (name, m * 100, margin * 100, minimum_price(cost, margin)))
        if name.strip().lower() in GENERIC_NAMES:
            warnings.append("'%s' is a generic name: name it after the customer's result" % name)
    prices = [r["price"] for r in rows]
    if len(prices) >= 2 and any(b <= a for a, b in zip(prices, prices[1:])):
        problems.append("prices must go up from level to level")
    if len(rows) == 3 and not problems:
        g1 = prices[1] / prices[0]
        g2 = prices[2] / prices[1]
        if g1 < 1.5:
            warnings.append("level 2 is only %.1fx level 1: level 1 may take most sales" % g1)
        elif g1 > 4:
            warnings.append("level 2 is %.1fx level 1: the jump may scare people" % g1)
        if g2 < 1.5:
            warnings.append("level 3 is only %.1fx level 2: it may look pointless" % g2)
        elif g2 > 5:
            warnings.append("level 3 is %.1fx level 2: fine only if it is truly limited and personal" % g2)
    return {"ok": not problems, "problems": problems, "warnings": warnings, "levels": rows}


def report(result):
    out = ["PASS" if result["ok"] else "FIX NEEDED"]
    out.append("  %-22s %12s %12s %12s %8s" % ("level", "full cost", "price", "profit", "margin"))
    for r in result["levels"]:
        out.append("  %-22s %12s %12s %12s %7.0f%%" % (r["name"][:22], r["full_cost"], r["price"], r["profit"], r["margin"] * 100))
    for p in result["problems"]:
        out.append("  problem: " + p)
    for w in result["warnings"]:
        out.append("  warning: " + w)
    return "\n".join(out)


SELF_TESTS = [
    ("healthy ladder passes", [("Tidy", 918, 1699), ("Spotless", 1938, 3599), ("Move in ready", 5151, 9499)], 0.45, True),
    ("losing level fails", [("A", 1000, 900), ("B", 1500, 3000), ("C", 3000, 9000)], None, False),
    ("prices not rising fails", [("A", 100, 500), ("B", 100, 400), ("C", 100, 2000)], None, False),
]


def self_test():
    failed = 0
    for name, levels, margin, want in SELF_TESTS:
        got = check(levels, margin)["ok"]
        if got != want:
            failed += 1
        print("%s  %s" % ("ok  " if got == want else "FAIL", name))
    s = suggest(1938, 0.45)
    ok = s["suggested_price"] >= s["minimum_price"]
    failed += 0 if ok else 1
    print("%s  suggested price is never below the minimum" % ("ok  " if ok else "FAIL"))
    total = len(SELF_TESTS) + 1
    print("%d of %d self tests passed" % (total - failed, total))
    return 1 if failed else 0


def main(argv=None):
    ap = argparse.ArgumentParser(description="Check a 3 level offer.")
    ap.add_argument("--level", nargs=3, action="append", metavar=("NAME", "FULL_COST", "PRICE"),
                    help="a level: name, full cost of one sale, price (repeat 3 times, cheapest first)")
    ap.add_argument("--margin", type=float, help="your target margin, for example 0.45 for 45%%")
    ap.add_argument("--suggest", type=float, metavar="FULL_COST", help="suggest a clean price for this full cost")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args(argv)
    if a.self_test:
        return self_test()
    try:
        if a.suggest is not None:
            if a.margin is None:
                print("--suggest needs --margin, for example --margin 0.45", file=sys.stderr)
                return 2
            s = suggest(a.suggest, a.margin)
            print(json.dumps(s, indent=2) if a.json else
                  "full cost %s, target margin %.0f%%: minimum price %.2f, suggested clean price %s"
                  % (s["full_cost"], a.margin * 100, s["minimum_price"], s["suggested_price"]))
            return 0
        if not a.level:
            ap.print_usage(sys.stderr)
            return 2
        levels = [(n, float(c), float(p)) for n, c, p in a.level]
    except ValueError as exc:
        print("could not read the numbers: %s" % exc, file=sys.stderr)
        return 2
    result = check(levels, a.margin)
    print(json.dumps(result, indent=2) if a.json else report(result))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
