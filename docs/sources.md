# Sources

Every figure used in this repo traces to one of the documents below. Pulled
2026-10-20/21. Unlike the Toys "R" Us project, Red Lobster was **never
itself an SEC filer** — it was a segment of public Darden Restaurants until
2014, then fully private (no public debt, no SEC reporting obligation) until
its 2024 Chapter 11 filing. This means the data trail here is **not a
continuous annual panel** the way Toys "R" Us's was — it's a strong
primary-sourced snapshot before the 2014 sale, one well-corroborated
mid-period anchor point (2016), and an unusually rich narrative for the
final crisis year (2023-2024), with a real gap in between. That gap is
stated plainly below, not papered over.

## 1. Pre-2014: Red Lobster as a Darden segment

**Source**: Darden Restaurants' own investor presentation, ["Sale of Red
Lobster, Spring 2014"](https://www.sec.gov/Archives/edgar/data/940944/000094094414000032/finalfinalinvestorpresentati.pdf),
filed with the SEC (Darden CIK 0000940944) in connection with the April 2014
special shareholder meeting process. Saved verbatim at
`data/raw/darden_rl_sale_investor_presentation.pdf` (text extract:
`data/raw/darden_rl_sale_investor_presentation.txt`).

Red Lobster segment financials, as disclosed by Darden (page 10 of the
presentation):

| Fiscal Year | Revenue ($B) | Revenue growth | EBITDA ($M) | EBITDA margin |
|---|---|---|---|---|
| FY2010 | $2.5 | +1% | $313 | 13% |
| FY2011 | $2.5 | -5%* | $350 | 14% |
| FY2012 | $2.7 | +6% | $334 | 13% |
| FY2013 | $2.6 | -2% | $307 | 12% |
| Q3 LTM (Feb 2014) | $2.5 | -4% | $243 | 10% |
| LTM (Apr 27, 2014) | $2.5 | -6% | $229 | 9% |

*The presentation's growth-rate row and revenue row don't align perfectly
year-to-year in the raw extract (a PDF table-parsing artifact); the dollar
figures themselves are transcribed exactly as shown and are internally
consistent (EBITDA margin = EBITDA / revenue checks out for every row).

Note the trend: EBITDA fell from $350M (FY2011) to $229M (LTM pre-sale) —
Darden was selling a segment with **visibly declining profitability**, not
a stable cash cow. Red Lobster also persistently trailed the "Knapp
Track" casual-dining industry benchmark on same-restaurant sales for the
two years of monthly data shown (almost every month negative, often -5% to
-10%).

## 2. The 2014 sale to Golden Gate Capital

**Primary source**: same Darden investor presentation as above, page 4-6.

- **Total consideration: $2.113 billion**, cash, debt- and cash-free basis.
- **Purchase multiple: ~9x** Red Lobster's LTM EBITDA (for the twelve months
  ended April 27, 2014) — ties almost exactly to 9 × $229M ≈ $2.06B.
- Buyer: **Golden Gate Capital**, paired by Darden's advisors with real
  estate buyer **American Realty Capital Properties (ARCP)** to submit a
  joint final proposal — the sale-leaseback was baked into the deal process
  from the start, not bolted on afterward.
- Darden's use of proceeds: ~$1.6B net cash after tax/fees, of which ~$1B
  went to debt repayment and ~$500-600M to a ~$700M FY2015 share buyback
  program.

**How Golden Gate actually financed its $2.1B purchase** (secondary
source, reported by multiple outlets incl.
[Yahoo Finance/Fast Company, "How private equity rolled Red Lobster"](https://finance.yahoo.com/news/private-equity-rolled-red-lobster-180041614.html)):
**$1.5 billion of the $2.1B came from selling Red Lobster's real estate**
to American Realty Capital, with Red Lobster signing long-term leases to
lease it back. **Golden Gate itself only put up ~$600 million** to close
the deal — the real estate monetization funded ~71% of the purchase price.
Debt commitments for the transaction were arranged by Deutsche Bank
Securities, GE Capital, and Jefferies Finance (named in the same reporting);
the exact amount and terms of that acquisition debt were not found in the
sources reviewed for this project and are not used as a model input — only
the $600M equity and $1.5B real estate monetization figures are, since
those are the figures consistently corroborated across sources.

## 3. 2016: Thai Union's investment (a mid-period anchor point)

**Source**: press reporting on Thai Union Group's required disclosure to
the Stock Exchange of Thailand (Thai Union is Thai-listed, not SEC-listed,
so this is a secondary source, not a primary filing pulled directly) — see
[Spokesman-Review, Oct 2016](https://www.spokesman.com/stories/2016/oct/11/controversial-seafood-supplier-buys-575-million-st/)
and corroborating coverage.

- Thai Union paid **$575 million** for a **49% stake** (25% of common
  units outright, plus 24% of preferred units convertible over 10 years).
- At the time of the investment, Red Lobster's disclosed financials for the
  **12 months ended August 2016**: **$2.479 billion revenue**, **$144
  million operating profit** (5.8% margin — notably thinner than the
  9-14% EBITDA margins Darden reported in 2010-2014, though "operating
  profit" and "EBITDA" aren't necessarily the same measure, so this is not
  a precise apples-to-apples comparison, just the closest available
  mid-period anchor).
- Implied valuation of Red Lobster at the time: ~$920 million (per Thai
  Union's own disclosed deal math) — notably **below** the $2.1B Golden
  Gate paid just over two years earlier, though this reflects an equity
  valuation (after Golden Gate's acquisition debt and the sale-leaseback)
  not a comparable enterprise-value figure, so it is not a clean indicator
  of value destruction on its own.
- [Moody's gave Red Lobster a negative outlook in 2017](https://finance.yahoo.com/news/private-equity-rolled-red-lobster-180041614.html),
  citing "persistently high leverage."

## 4. 2020: Golden Gate Capital's full exit

**Source**: the company's own 2024 bankruptcy first-day declaration (see
§5 below), ¶14: "In 2020, Thai Union, former members of the Red Lobster
management team, and certain investors operating under the name Seafood
Alliance, acquired Golden Gate's remaining equity stake in Red Lobster."

**What is NOT known from sources reviewed**: Golden Gate's realized
return on this exit (price received, gain or loss versus its ~$600M
initial equity) was not found in any source used for this project. This
repo does **not** estimate or guess that figure — it is left explicitly
blank. This matters: whatever happened to Red Lobster after 2020 did not
happen on Golden Gate's balance sheet.

## 5. 2023-2024: the crisis, and the Chapter 11 filing

**Primary source**: *Declaration of Jonathan Tibus in Support of Debtors'
Chapter 11 Petitions and First Day Relief*, filed May 19, 2024, Case No.
6:24-bk-02486-GER (lead case), U.S. Bankruptcy Court for the Middle
District of Florida, Orlando Division — ECF No. 6, 124 pages. Saved
verbatim at `data/raw/tibus_first_day_declaration.pdf` (text extract:
`data/raw/tibus_first_day_declaration.txt`). Jonathan Tibus was CEO at the
time of filing (Alvarez & Marsal, retained January 11, 2024).

Key figures, all from this declaration unless noted:

- **Ownership at filing**: Thai Union ~47% of common equity + 100% of
  preferred units; Seafood Alliance ~38% of common; remaining common held
  by former management via two entities (¶24).
- **Funded debt at filing, ~$294 million total**: Prepetition Term Loan
  (Fortress Credit Corp as agent, dated Jan 22, 2021) **$264.72M**
  outstanding, plus **$29.28M** of outstanding letters of credit under a
  $100M ABL facility (Wells Fargo) — no cash loans drawn under the ABL
  itself at filing (¶27-29).
- **Guest traffic down ~30% since 2019** (¶33).
- **Net sales rose ~25% from 2021 to 2023** (pandemic recovery), but
  **declined materially in the twelve months before filing**; over that
  same trailing-twelve-month window, **consolidated adjusted EBITDA fell
  more than 60%** (¶33).
- **FY2023 net loss: $76 million** (¶33).
- **Cash collapse**: ~$100M cash (May 2023) → less than $30M (~November
  2023), over roughly six months, driven by (¶34): ~$31M of operating cash
  losses (Jun-Sep 2023), a $27M forced ABL paydown (triggered by a
  vendor-managed-inventory program shrinking the ABL borrowing base), and
  $32M of FY2023 interest payments.
- **Lease burden**: 687 leased locations (247 under Master Leases, 440
  individual property leases); **$190.5 million** spent on lease
  obligations in 2023, of which **more than $64 million** tied specifically
  to underperforming stores (¶38). Separate press coverage (Fast Company)
  cites a slightly higher **~$200 million/year, ~10% of revenue** figure
  for the same period — the two are close and likely reflect slightly
  different measurement windows or lease-accounting scopes; both are shown
  rather than silently picking one.
- **The "Ultimate Endless Shrimp" decision**: in May 2023, then-CEO Paul
  Kenny made the limited-time Endless Shrimp promotion a permanent $20
  menu item, against internal management pushback — this single decision
  is specifically identified in the declaration as costing the company
  **$11 million** (¶39, text cuts off mid-sentence in the extracted copy
  listing further consequences; the $11M figure itself is clearly stated).
- **Filing**: Chapter 11 petitions filed **May 19, 2024** (ECF docket
  date), Middle District of Florida, Orlando Division, jointly administered
  under Case No. 6:24-bk-02486-GER.

## 6. The bankruptcy outcome

**Source**: press reporting, notably
[Bloomberg Law, "Red Lobster Cleared to Exit Bankruptcy Under New Owner
Fortress"](https://news.bloomberglaw.com/bankruptcy-law/red-lobster-cleared-to-exit-bankruptcy-under-new-owner-fortress)
and [Restaurant Business Online](https://www.restaurantbusinessonline.com/financing/red-lobster-set-exit-bankruptcy-after-court-approval)
coverage of the September 2024 confirmation.

- The Bankruptcy Court approved a sale to a group led by **Fortress
  Investment Group** (the same Fortress that was the prepetition secured
  term loan lender) via a **credit bid of $376 million** — meaning Fortress
  paid by cancelling debt it was already owed, rather than with new cash.
  The sale closed **September 16, 2024**.
- The reorganized company, **RL Investor Holdings LLC**, is owned by
  Fortress-managed funds together with co-investors **TCW Private Credit**
  and **Blue Torch Capital**.
- **All prior equity — Thai Union, Seafood Alliance, and former
  management — was wiped out.** General unsecured creditors did not
  receive cash recovery; they receive interests in a litigation trust
  instead, whose eventual value is not known from sources reviewed.
- **This is the equity-loss event that matches what the user originally
  asked for** ("investors lost everything") — but it is Thai Union /
  Seafood Alliance / management's 2024 loss, not Golden Gate Capital's.
  Golden Gate had already exited in 2020 (see §4) on terms not disclosed
  in any source used here.

## What this repo does NOT claim

- No continuous year-by-year financial panel exists for Red Lobster the
  way it did for Toys "R" Us — the company was private with no reporting
  obligation for a full decade (2014-2024). The data here is a strong
  pre-sale panel, one solid mid-period anchor (2016), and a very rich
  final-year narrative, with a real, stated gap in between (2017-2022).
- Golden Gate Capital's realized return on its 2014-2020 ownership is not
  estimated anywhere in this repo.
- The exact acquisition-debt amount and terms Golden Gate used alongside
  its $600M equity are not used as a model input, since no source reviewed
  disclosed them precisely.
- The "lease-adjusted leverage" analysis in the notebook/model is this
  repo's own illustrative method for making the sale-leaseback's economic
  effect comparable to conventional debt — it is clearly labeled as a
  modeling choice, not a figure from any filing.
