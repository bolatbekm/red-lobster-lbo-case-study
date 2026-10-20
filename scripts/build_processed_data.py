"""
Assembles data/processed/*.csv from the figures cited in docs/sources.md.
Every number here is transcribed from a specific cited source -- nothing is
interpolated or estimated in this project (unlike the Toys R Us project's
one flagged FY2008 interpolation), because the gaps here are too large to
responsibly interpolate across (2017-2022 is a 6-year blank with no
reliable anchor in between) -- the gap is left as a visible gap instead.
"""
import csv
import os

OUT_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "processed")
os.makedirs(OUT_DIR, exist_ok=True)


def write_csv(name, header, rows):
    path = os.path.join(OUT_DIR, name)
    with open(path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(header)
        for r in rows:
            w.writerow(r)
    print("wrote", path, len(rows), "rows")


# --- 1. Pre-2014 Darden segment financials (docs/sources.md §1) ---
write_csv(
    "pre_2014_darden_segment.csv",
    ["period", "period_end", "revenue_busd", "revenue_growth_pct", "ebitda_musd", "ebitda_margin_pct", "source"],
    [
        ("FY2010", "2010-05", 2.5, 1, 313, 13, "Darden investor presentation, Spring 2014"),
        ("FY2011", "2011-05", 2.5, -5, 350, 14, "Darden investor presentation, Spring 2014"),
        ("FY2012", "2012-05", 2.7, 6, 334, 13, "Darden investor presentation, Spring 2014 (incl. Yard House acquisition at Darden level, not RL-specific)"),
        ("FY2013", "2013-05", 2.6, -2, 307, 12, "Darden investor presentation, Spring 2014"),
        ("Q3 LTM FY2014", "2014-02", 2.5, -4, 243, 10, "Darden investor presentation, Spring 2014"),
        ("LTM pre-sale", "2014-04-27", 2.5, -6, 229, 9, "Darden investor presentation, Spring 2014 -- the EBITDA figure the 9x purchase multiple was based on"),
    ],
)

# --- 2. The 2014 deal (docs/sources.md §2) ---
write_csv(
    "deal_2014.csv",
    ["item", "value_musd", "source", "notes"],
    [
        ("Total consideration (debt- and cash-free)", 2113, "Darden investor presentation", "9x LTM EBITDA of $229M ~= $2,061M, close to the $2,113M actual price"),
        ("Purchase multiple (x LTM EBITDA)", 9, "Darden investor presentation", ""),
        ("Golden Gate Capital equity contributed", 600, "Press (Yahoo Finance/Fast Company)", "Not in the Darden presentation -- this is the buy-side financing, which Darden (the seller) would not disclose"),
        ("Real estate sale-leaseback proceeds (American Realty Capital)", 1500, "Press (Yahoo Finance/Fast Company)", "Funded ~71% of the $2,113M purchase price. Ties: 600+1500=2100, ~matches 2113 total consideration."),
        ("Darden net cash proceeds after tax/fees", 1600, "Darden investor presentation", ""),
        ("Of which used for Darden debt repayment", 1000, "Darden investor presentation", ""),
        ("Of which used for Darden share buybacks", 600, "Darden investor presentation", "~$700M total FY2015 buyback program, partly funded from other sources too"),
    ],
)

# --- 3. 2016 Thai Union anchor point (docs/sources.md §3) ---
write_csv(
    "anchor_2016_thai_union.csv",
    ["metric", "value", "unit", "source"],
    [
        ("Thai Union investment", 575, "musd", "Press (Spokesman-Review, Oct 2016)"),
        ("Stake acquired (common, outright)", 25, "pct", "Press"),
        ("Stake acquired (preferred, convertible over 10yr)", 24, "pct", "Press"),
        ("Total stake", 49, "pct", "Press, and confirmed in 2024 first-day declaration as '~47% common + 100% preferred' at a later date"),
        ("Revenue, LTM Aug 2016", 2479, "musd", "Press, citing Thai Union's own disclosed deal rationale"),
        ("Operating profit, LTM Aug 2016", 144, "musd", "Press, citing Thai Union's own disclosed deal rationale"),
        ("Implied Red Lobster equity valuation", 920, "musd", "Press, per Thai Union's own deal math"),
    ],
)

# --- 4. Capital structure & lease burden at the 2024 filing (docs/sources.md §5) ---
write_csv(
    "capital_structure_at_filing_2024.csv",
    ["item", "value_musd", "detail", "source"],
    [
        ("Prepetition Term Loan (Fortress Credit Corp, dated Jan 22 2021)", 264.72, "secured by substantially all assets", "First-day declaration ¶27-28"),
        ("ABL Facility outstanding letters of credit (Wells Fargo)", 29.28, "of a $100M facility, $0 cash drawn", "First-day declaration ¶29"),
        ("Total funded debt at filing", 293.996, "sum of the two rows above", "First-day declaration ¶27"),
        ("2023 total lease obligations", 190.5, "687 leased locations: 247 Master Leases + 440 individual", "First-day declaration ¶38"),
        ("...of which tied to underperforming stores", 64, "lower bound, 'over $64 million'", "First-day declaration ¶38"),
        ("Press-reported alternative 2023 rent figure", 200, "~10% of revenue, slightly different measurement window", "Press (Fast Company)"),
    ],
)

# --- 5. The 2023 liquidity collapse, as a timeline (docs/sources.md §5) ---
write_csv(
    "liquidity_collapse_2023.csv",
    ["event", "value_musd", "period", "source"],
    [
        ("Cash on hand", 100, "May 2023", "First-day declaration ¶34"),
        ("Operating cash losses", -31, "Jun-Sep 2023", "First-day declaration ¶34"),
        ("Forced ABL paydown (vendor-managed inventory program shrank borrowing base)", -27, "~2023", "First-day declaration ¶34"),
        ("FY2023 interest payments", -32, "FY2023", "First-day declaration ¶33"),
        ("Cash on hand", 30, "~Nov 2023 (approx. 6 months after May 2023)", "First-day declaration ¶34 ('less than $30 million')"),
        ("FY2023 net loss", -76, "FY2023", "First-day declaration ¶33"),
        ("Guest count change since 2019", -30, "pct, 2019 to ~2023/24", "First-day declaration ¶33"),
        ("Net sales change, 2021 to 2023", 25, "pct, pandemic recovery", "First-day declaration ¶33"),
        ("Adjusted EBITDA change, trailing twelve months before filing", -60, "pct, LTM pre-filing (~2023-2024)", "First-day declaration ¶33"),
        ("'Ultimate Endless Shrimp' permanent-menu decision cost", -11, "from May 2023 decision", "First-day declaration ¶39"),
    ],
)

# --- 6. Bankruptcy outcome (docs/sources.md §6) ---
write_csv(
    "bankruptcy_outcome_2024.csv",
    ["item", "value", "source"],
    [
        ("Filing date", "2024-05-19", "First-day declaration"),
        ("Court", "US Bankruptcy Court, Middle District of Florida, Orlando Division, Case 6:24-bk-02486-GER", "First-day declaration"),
        ("Fortress credit bid for the business", "$376 million", "Bloomberg Law / Restaurant Business Online"),
        ("Sale closed", "2024-09-16", "Press"),
        ("New owner", "RL Investor Holdings LLC (Fortress-managed funds + TCW Private Credit + Blue Torch Capital)", "Press"),
        ("Thai Union equity outcome", "Wiped out ($0)", "Press"),
        ("Seafood Alliance equity outcome", "Wiped out ($0)", "Press"),
        ("Former management equity outcome", "Wiped out ($0)", "Press"),
        ("General unsecured creditor recovery", "Litigation trust interests only, no stated cash recovery", "Press"),
        ("Golden Gate Capital's 2020 exit terms", "NOT DISCLOSED in sources reviewed -- not estimated here", "n/a"),
    ],
)
