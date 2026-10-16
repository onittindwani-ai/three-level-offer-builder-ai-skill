# 3-Level Offer Builder

A free AI skill that turns what you sell into **3 clear levels**: an easy yes, a main offer most people choose, and an honest premium level. Each gets a result based name, a price worked out from your real costs, and the exact wording for your price list, WhatsApp replies and proposals.

**Download:** [latest release (zip)](https://github.com/onittindwani-ai/three-level-offer-builder-ai-skill/releases/latest) · **Source:** [github.com/onittindwani-ai/three-level-offer-builder-ai-skill](https://github.com/onittindwani-ai/three-level-offer-builder-ai-skill)

Works for any business: cleaning, clinics, cafes, accountants, agencies, coaches, shops, software. No spreadsheets or pricing experience needed.

## The idea, from Tesla

When Tesla revealed its new Roadster in October 2026, it came in 3 versions:

| Version | Seats | Access |
| --- | --- | --- |
| **Road ready** (Performance) | 2 | 50,000 dollar reservation |
| **Race ready** (Thrust) | 2 | 250,000 dollar reservation, limited |
| **Air ready** (Rocket) | 1 | Invite only, not approved for public roads |

(As reported at the reveal. Final prices were not announced.)

Two lessons any business can use:

1. **The top level makes the middle look smart.** Next to a car you can't have, 250,000 feels like a real option.
2. **Name levels after who the customer becomes,** not by size. "Road ready, race ready, air ready" beats "Basic, Standard, Premium".

This skill applies both, honestly: real costs, real limits, no fake urgency.

## Before and after

**Before:** "Cleaning service: 1,500 per visit." (Below the real cost of a proper clean.)

**After:**
| Level | What you get | Price |
| --- | --- | --- |
| **Tidy** | 2 hours, 1 cleaner | 1,699 |
| **Spotless** (recommended) | 3 hours, 2 cleaners, supplies included | 3,599 |
| **Move in ready** | Full deep clean, team of 3, same day. Only 2 slots a week | 9,499 |

Every level now covers its full cost with a 46% margin, the middle is the clear best value, and the premium's limit is real. (Example business. In real use, only your own numbers are used.)

## What it does

1. **Asks for your real numbers** (costs, hours, capacity) and never invents any.
2. **Designs 3 levels** that differ by result, speed, support or certainty, not just "more stuff".
3. **Prices each level** from full cost and your target margin, rounds to clean prices, and checks the gaps.
4. **Names them** after your customer's result, with 3 naming options.
5. **Writes the words:** price list, pricing page, WhatsApp "how much?" reply, proposal options, deposit and refund terms, price change message.
6. **Keeps it honest:** real limits only, clear refund rules, no fake countdowns.
7. **Gives you a test** to try for 2 to 4 weeks, and what to measure.

## 3 ways to use it

### 1. Easiest: paste a prompt (ChatGPT, Claude, Gemini, any AI chat)
Open [PASTE-INTO-CHATGPT-OR-CLAUDE.md](PASTE-INTO-CHATGPT-OR-CLAUDE.md), copy the box into a new chat, and describe your business under it.

### 2. Claude (claude.ai or the desktop app)
1. Download the zip from the [latest release](https://github.com/onittindwani-ai/three-level-offer-builder-ai-skill/releases/latest).
2. In Claude, open **Settings, Capabilities, Skills**, and upload the zip. (On plans without Skills: create a Project and paste the prompt file into its instructions.)
3. Say: "Use the 3-level offer builder for my business", and describe it.

### 3. Claude Code or Codex
```
git clone https://github.com/onittindwani-ai/three-level-offer-builder-ai-skill.git ~/.claude/skills/three-level-offer-builder
```
For Codex, clone into `~/.agents/skills/three-level-offer-builder` instead.

## What's in the folder

| File | What it's for |
| --- | --- |
| `SKILL.md` | The skill: 7 rules, a 10 step method, a self check and 9 special situations |
| `PASTE-INTO-CHATGPT-OR-CLAUDE.md` | The no install version: one full prompt, plus follow up commands |
| `templates/OFFER-SHEET.md` | Your internal 1 page offer sheet: the single source for every price conversation |
| `templates/PRICING-PAGE.md` | A 3 column pricing page that makes the middle the obvious choice |
| `templates/PRICE-MESSAGE.md` | The WhatsApp or DM reply to "how much?" |
| `templates/PROPOSAL-OPTIONS.md` | Options A, B, C inside a proposal |
| `templates/DEPOSIT-AND-REFUND.md` | Deposits, waitlists and refund rules people trust |
| `templates/PRICE-CHANGE-MESSAGE.md` | Telling existing customers about new prices without losing them |
| `references/LEVEL-DESIGN.md` | The job of each level and 8 ways levels can honestly differ |
| `references/NAMING.md` | 6 naming styles with 40+ examples, and names to avoid |
| `references/PRICING-MATH.md` | Full cost, margin, rounding, gaps, and a worked example |
| `references/HONEST-SCARCITY.md` | Real limits you can use, and what never to do |
| `references/ANCHORING.md` | Why a premium level makes the middle look smart, used honestly |
| `references/INDUSTRY-PLAYBOOKS.md` | 3 level designs for 16 industries |
| `references/OBJECTIONS.md` | Answers to "too expensive" and "discount?" without cutting your price |
| `references/PRICE-TESTING.md` | 4 safe ways to test new prices |
| `references/EXAMPLES.md` | 10 full before and after offers |
| `scripts/price_check.py` | An optional calculator: profit and margin per level, gaps, warnings |
| `tests/` | Automatic tests, run on GitHub for every change |

## The calculator (optional)

If you have Python 3.9 or newer:

```
python scripts/price_check.py --level "Tidy" 918 1699 --level "Spotless" 1938 3599 --level "Move in ready" 5151 9499 --margin 0.45
python scripts/price_check.py --suggest 1938 --margin 0.45
```

It only does arithmetic on the numbers you type. Nothing is sent anywhere.

## Honest limits

- It can't know your costs or your customers. The better your numbers, the better the result.
- The gap ranges (for example Level 2 at 1.5 to 4 times Level 1) are starting points, not laws. Test with real customers.
- Check local rules on price displays, deposits and refunds before publishing.
- This is not financial or legal advice.

## Privacy

Everything runs inside the AI tool you already use. This skill has no server, no tracking and no account. Don't paste passwords, bank details or customer personal data into any AI chat.

## Found a problem?

Open an issue on [GitHub](https://github.com/onittindwani-ai/three-level-offer-builder-ai-skill/issues). Please don't paste private financial details into an issue.

## License

MIT. Free to use, change and share.
