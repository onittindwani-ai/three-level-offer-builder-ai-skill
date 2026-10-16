---
name: three-level-offer-builder
description: Design a business's pricing as 3 clear levels (an easy yes, the main offer, and an honest premium or invite only level), with names based on the customer's result, what goes in each level, prices worked out from real costs and margins, and the wording for a pricing page, WhatsApp price message or proposal. Use when someone asks how to price, package or bundle their product or service, wants tiers or packages, says customers always pick the cheapest option, wants to raise prices, add a premium offer, take deposits, or rename "Basic, Standard, Premium". Never invents costs, prices, demand or scarcity.
license: MIT
metadata:
  version: "1.0.0"
  works-with: "ChatGPT, Claude, Claude Code, Codex, Gemini"
---

# 3-Level Offer Builder

## Why this skill exists

Most businesses price in one of two broken ways:

1. **One price for everything.** Every customer gets the same thing at the same price. Customers who would happily pay more for more can't, and customers who want less go elsewhere.
2. **Basic, Standard, Premium.** 3 levels that differ by features, named by size, priced by guesswork. Everyone compares features, gets confused, and picks the cheapest.

When Tesla revealed its new Roadster in October 2026, it did something different. It offered 3 versions: one at a 50,000 dollar reservation, one at 250,000, and a third that was invite only, with 1 seat, not even approved for public roads. And it named them **road ready, race ready, air ready**: not by engine size, but by who the buyer becomes.

The top version isn't really there to be bought by many people. It makes the middle one feel reasonable, and it gives the whole range a story.

This skill helps any business do the same thing, honestly:

- **Level 1, the easy yes:** a small, low risk way to start with you.
- **Level 2, the main offer:** what you want most customers to buy. Your best value.
- **Level 3, the premium:** the fullest version, limited for a real reason, priced high, which makes Level 2 the smart choice.

Each level is named after the customer's result. Each price comes from real costs and the margin the owner wants. Every limit is real.

## The 7 rules (never break these)

### Rule 1. Never invent numbers
Use only the costs, prices, hours, capacity and demand the person gives you. If something is missing, ask, or mark it `[NEEDS: what]`. Never make up what competitors charge, what customers will pay, or how many will buy. If you suggest a price, show exactly how you got it from their numbers.

### Rule 2. Every level must make money
Every level's price must cover its full cost (materials, time at a fair hourly cost, tools, delivery, payment fees) plus a margin. A cheap entry level that loses money on every sale is a mistake, not a strategy, unless the owner deliberately chooses it as a short term test and knows the cost. Use `scripts/price_check.py` or the math in [references/PRICING-MATH.md](references/PRICING-MATH.md).

### Rule 3. Level 2 is the hero
Design Level 2 first. It's the best value and the one most customers should choose. Level 1 removes the risk of starting. Level 3 makes Level 2 look smart. If Level 2 isn't clearly the best deal, the structure fails.

### Rule 4. Levels differ by result, not by feature count
Each level should get the customer a different outcome, speed, level of support or certainty, not just "more stuff". "Done in 5 days with 2 rounds of changes" against "done for you in 48 hours, unlimited changes, with the owner personally" is a real difference. "10 pages" against "15 pages" usually isn't.

### Rule 5. Names come from the customer's result
Name each level after who the customer becomes or what they get: "Road ready, Race ready, Air ready". "Filed, Organised, Growing". Never "Basic, Standard, Premium", "Silver, Gold, Platinum" or "Starter, Pro, Enterprise" unless the owner insists. See [references/NAMING.md](references/NAMING.md).

### Rule 6. Scarcity and premium must be real
Only say "limited", "invite only", "few spots" or "by application" if it is true, with a real reason the owner can explain (their own time, a physical limit, a quality limit, a real deadline). Fake scarcity is a lie, it breaks consumer protection rules in many countries, and customers notice. See [references/HONEST-SCARCITY.md](references/HONEST-SCARCITY.md).

### Rule 7. Plain words and clear terms
Prices include what tax or fees apply. What's included and what's not is written plainly. Deposits and refunds are explained in one sentence each, right next to the price. No hidden fees, no fine print tricks.

## How to work, step by step

### Step 1. Get the facts (ask once, in one message)

If the person hasn't given these, ask in one short message, numbered, and tell them they can skip what they don't know:

```
To design your 3 levels properly, tell me what you can:
1. What do you sell, and who usually buys it?
2. What's your current price (or prices)?
3. What does one sale cost you? (materials, delivery, tools, fees) And roughly how many hours of work?
4. What's your time worth per hour? (or what you pay staff per hour)
5. How many customers can you handle per month, at most?
6. What do customers ask for most, and what do they complain about?
7. What would you love to sell more of, and what do you hate doing?
8. Anything you're not willing to do (a minimum price, no discounts, no weekends)?
Skip anything you don't know. I'll mark it and work with what you give me.
```

If they give little, continue with what you have and mark gaps `[NEEDS: ...]`. Never stall.

### Step 2. Find the core result
Use the "so what?" ladder: ask "so what?" about the product until you reach the outcome the customer actually pays for (time saved, money made, risk removed, status, peace, a specific moment). All 3 levels deliver that same core result at different speeds, depths or certainties.

### Step 3. Design Level 2 (the hero) first
Use [references/LEVEL-DESIGN.md](references/LEVEL-DESIGN.md). Level 2 should:
- Deliver the full core result for a typical customer.
- Be what you'd recommend to a friend.
- Include the 1 or 2 things customers ask for most.
- Have a healthy margin (see Pricing math).

### Step 4. Design Level 1 (the easy yes)
Smaller, faster, lower risk. Something a hesitant customer says yes to without a long decision. It must still make money and deliver a real, smaller result. Good Level 1s often lead naturally into Level 2 (an audit, a first session, a starter pack, a trial month).

### Step 5. Design Level 3 (the honest premium)
The fullest version: faster, more personal, more certain, more exclusive. Limited for a real reason (the owner's own time, physical capacity, a quality limit). Priced clearly higher (often 2 to 4 times Level 2; see Pricing math), so that:
- The few who want the best can have it, at a price that's worth the owner's time.
- Level 2 looks like the smart choice next to it.
Options for Level 3: "by application", "invite only", "only X per month", "with the founder personally". Use only what's true.

### Step 6. Price the levels
For each level, calculate: full cost, minimum price (cost plus target margin), and a suggested price rounded to a clean number. Check the gaps between levels. Run `python scripts/price_check.py` if you can run code, or follow [references/PRICING-MATH.md](references/PRICING-MATH.md) by hand. Show your working in a small table.

### Step 7. Name the levels
Write 3 naming sets using [references/NAMING.md](references/NAMING.md) (for example, "who you become", "the result", "the speed"). Recommend one.

### Step 8. Write the customer facing version
Using the matching template:
- A pricing page or price list: [templates/PRICING-PAGE.md](templates/PRICING-PAGE.md)
- A WhatsApp or DM reply to "how much?": [templates/PRICE-MESSAGE.md](templates/PRICE-MESSAGE.md)
- Options inside a proposal: [templates/PROPOSAL-OPTIONS.md](templates/PROPOSAL-OPTIONS.md)
- Deposit and refund terms: [templates/DEPOSIT-AND-REFUND.md](templates/DEPOSIT-AND-REFUND.md)
- Telling existing customers about new prices: [templates/PRICE-CHANGE-MESSAGE.md](templates/PRICE-CHANGE-MESSAGE.md)
- The internal one page offer sheet: [templates/OFFER-SHEET.md](templates/OFFER-SHEET.md)

### Step 9. Check yourself
Use the checklist below.

### Step 10. Reply in this exact order
1. **Your 3 levels at a glance:** a table with name, who it's for, what's included, price, and the result.
2. **The math:** cost, margin and price per level, in a small table, with any `[NEEDS]` gaps.
3. **2 more naming options.**
4. **The customer facing text,** ready to paste (pricing page or price message, whichever fits).
5. **Your honest premium:** why Level 3 is limited, in one sentence they can say out loud.
6. **One test** to try for 2 to 4 weeks (see [references/PRICE-TESTING.md](references/PRICE-TESTING.md)).

## Check before you send

- [ ] No number was invented. Every cost and price came from the person, or is clearly marked `[NEEDS]` or shown as a calculation from their numbers.
- [ ] Every level's price covers its full cost plus a margin.
- [ ] Level 2 is clearly the best value.
- [ ] The levels differ by result, speed, support or certainty, not just quantity.
- [ ] Names describe the customer's result, not size.
- [ ] Any limit or "invite only" is real, with a reason the owner can say out loud.
- [ ] Deposits, refunds, tax and what's not included are clear.
- [ ] The text is in plain words, with one clear next step.

## Special situations

- **They only sell one product at one price.** Build levels around it: Level 1 a smaller version or a first step, Level 2 the current product (often repriced), Level 3 the product plus speed, personal attention or a guarantee.
- **Products, not services (a shop, a cafe, an online store).** Levels become sizes, bundles or memberships: a single item, a bundle that's the best value, a premium gift set or subscription. The same rules apply.
- **They want to raise prices.** Use the levels to do it: the old price often becomes Level 1, the new main offer becomes Level 2. Use [templates/PRICE-CHANGE-MESSAGE.md](templates/PRICE-CHANGE-MESSAGE.md) and give existing customers fair notice.
- **They want deposits or a waitlist.** Use [templates/DEPOSIT-AND-REFUND.md](templates/DEPOSIT-AND-REFUND.md). Refunds must be as easy as paying, stated in one sentence next to the price.
- **They want fake urgency ("only 2 left" when there are 20).** Refuse that part in one sentence and offer a real alternative: a real capacity limit, a real price increase date, a bonus for a real deadline.
- **Regulated businesses** (health, legal, finance, education): never promise outcomes in any level. Levels can differ by access, speed, support and scope, not by guaranteed results. Remind them to check local rules on pricing displays.
- **B2B and large deals.** Levels can be "Assess, Implement, Partner" with scope, response times and outcomes tracked. Price can be "from" with a clear range.
- **Marketplaces with fixed prices or commissions.** Include the platform fee in the cost before pricing.
- **They don't know their costs.** Help them estimate in 5 minutes with the cost checklist in [references/PRICING-MATH.md](references/PRICING-MATH.md). Never guess for them.

## Files in this skill

| File | Use it for |
| --- | --- |
| [references/LEVEL-DESIGN.md](references/LEVEL-DESIGN.md) | How to design each of the 3 levels, with 8 ways levels can differ |
| [references/NAMING.md](references/NAMING.md) | 6 naming styles with 40+ examples |
| [references/PRICING-MATH.md](references/PRICING-MATH.md) | Full cost, margin, price, gaps between levels, rounding, worked examples |
| [references/HONEST-SCARCITY.md](references/HONEST-SCARCITY.md) | Real limits you can use, and what never to do |
| [references/ANCHORING.md](references/ANCHORING.md) | Why a premium level makes the middle look smart, used honestly |
| [references/INDUSTRY-PLAYBOOKS.md](references/INDUSTRY-PLAYBOOKS.md) | 3 level designs for 16 industries |
| [references/OBJECTIONS.md](references/OBJECTIONS.md) | Answers to "too expensive", "can I get a discount" and more |
| [references/PRICE-TESTING.md](references/PRICE-TESTING.md) | Safe, fair ways to test new prices |
| [references/EXAMPLES.md](references/EXAMPLES.md) | 10 full before and after offers |
| [templates/](templates/) | 6 templates for pages, messages, proposals, deposits and price changes |
| [scripts/price_check.py](scripts/price_check.py) | Optional calculator and checker for your 3 levels |
