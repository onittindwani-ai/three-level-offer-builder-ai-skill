# Pricing Math (Simple and Safe)

No guessing. Every price starts from what one sale really costs you.

## Step 1. Full cost of one sale, per level

Add up everything one sale of this level costs you:

| Cost | How to work it out |
| --- | --- |
| **Materials and products** | What you buy for this one sale |
| **Your time** | Hours × your hourly cost (what you'd pay someone to do it, or a fair wage for yourself) |
| **Staff time** | Hours × what you pay staff per hour, including taxes and benefits |
| **Tools and software** | Monthly tool costs ÷ sales per month |
| **Delivery and travel** | Fuel, courier, parking |
| **Payment and platform fees** | Usually 2% to 3% for cards, more for marketplaces |
| **A share of fixed costs** | Rent, internet, insurance per month ÷ sales per month |

**Cost checklist if you don't know your costs (5 minutes):**
1. Look at last month's bank statement and list every business expense.
2. Count last month's sales.
3. Fixed costs ÷ sales = fixed cost per sale.
4. Add the direct cost of one sale (materials, delivery, fees).
5. Add your hours × an hourly figure you're happy with.
That's your full cost per sale. Not perfect, but far better than a guess.

## Step 2. Price from cost and target margin

```
Price = Full cost ÷ (1 − target margin)
```

| Target margin | Divide the cost by | Example: cost 1,000 |
| --- | --- | --- |
| 30% | 0.70 | 1,429 |
| 40% | 0.60 | 1,667 |
| 50% | 0.50 | 2,000 |
| 60% | 0.40 | 2,500 |
| 70% | 0.30 | 3,333 |

**Margin is not the same as markup.** A 50% margin means half the price is profit. That's a 100% markup on cost. Mixing them up is the most common pricing mistake.

Typical target margins (rough guides, check your own industry): product businesses 30% to 60%, services 50% to 70%, digital products and software higher. Your own costs and goals decide.

## Step 3. Round to a clean price

Round up to a price that's easy to say and read:
- Under 1,000: round to the nearest 49 or 99 (for example 449, 799), or a round number.
- 1,000 to 10,000: round to the nearest 100 or 500.
- Above 10,000: round to the nearest 1,000 or 5,000.
Always round up, never below your minimum price.

## Step 4. Check the gaps between levels

These are rough starting points, not laws. Your own customers decide.

| Gap | Healthy range | If it's off |
| --- | --- | --- |
| Level 2 ÷ Level 1 | About 1.5 to 4 times | Too small: Level 1 eats Level 2 sales. Too big: the jump scares people |
| Level 3 ÷ Level 2 | About 1.5 to 5 times | Too small: Level 3 looks pointless. Larger is fine if Level 3 is genuinely limited and personal |
| Value per rupee | Highest at Level 2 | If Level 1 or 3 is better value, people pick them instead |

## Step 5. Check each level makes money

| Level | Full cost | Price | Profit | Margin |
| --- | --- | --- | --- | --- |
| 1 | | | Price − cost | Profit ÷ price |
| 2 | | | | |
| 3 | | | | |

If any level's margin is below your target, either raise the price, take something out, or make it faster to deliver.

## Worked example: a home cleaning business

Facts given by the owner: cleaner cost 250 per hour (including travel), supplies 150 per visit, payment fees 2%, fixed costs 30,000 a month across 120 visits (250 per visit), target margin 45%.

| Level | Hours | Full cost | Price at 45% margin | Rounded price |
| --- | --- | --- | --- | --- |
| Tidy (2 hours, 1 cleaner) | 2 | 500 + 150 + 250 = 900 (+2% fees) ≈ 918 | 918 ÷ 0.55 ≈ 1,669 | 1,699 |
| Spotless (3 hours, 2 cleaners) | 6 | 1,500 + 150 + 250 = 1,900 (+2%) ≈ 1,938 | ≈ 3,524 | 3,499 is below the minimum, so 3,599 |
| Move in ready (6 hours, 3 cleaners, same day) | 18 | 4,500 + 300 + 250 = 5,050 (+2%) ≈ 5,151 | ≈ 9,365 | 9,499 |

Gaps: 3,599 ÷ 1,699 ≈ 2.1 times, 9,499 ÷ 3,599 ≈ 2.6 times. Both healthy. Every level covers its full cost.

## Use the calculator

```
python scripts/price_check.py --level "Tidy" 918 1699 --level "Spotless" 1938 3599 --level "Move in ready" 5151 9499 --margin 0.45
```

It shows each level's profit and margin, checks the gaps, and warns about generic names, losses and margins below your target. Or suggest a price from a cost:

```
python scripts/price_check.py --suggest 1938 --margin 0.45
```
