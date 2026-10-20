"""
Builds RedLobster_LBO_Model.xlsx. Same honesty discipline as the Toys R Us
model: blue = cited input, black = formula, red = explicitly flagged
assumption. This model's shape differs from the Toys R Us one because the
underlying data differs -- there's no continuous annual panel to run a
multi-year debt schedule against, so instead this model focuses on: (1) the
2014 deal mechanics, (2) lease-adjusted leverage at the 2024 filing, and
(3) the 2023 liquidity collapse walk.
"""
import csv
import os

import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.comments import Comment

HERE = os.path.dirname(__file__)
DATA = os.path.join(HERE, "..", "data", "processed")

FONT = "Calibri"
TITLE_FONT = Font(name=FONT, size=16, bold=True, color="FFFFFF")
HEADER_FONT = Font(name=FONT, size=10, bold=True, color="FFFFFF")
SECTION_FONT = Font(name=FONT, size=11, bold=True)
LABEL_FONT = Font(name=FONT, size=10)
INPUT_FONT = Font(name=FONT, size=10, color="0000FF")
CALC_FONT = Font(name=FONT, size=10, color="000000")
NOTE_FONT = Font(name=FONT, size=9, italic=True, color="808080")
ASSUMPTION_FONT = Font(name=FONT, size=10, color="C00000", bold=True)

DARK_FILL = PatternFill(start_color="1F3864", end_color="1F3864", fill_type="solid")
LIGHT_FILL = PatternFill(start_color="D9E2F3", end_color="D9E2F3", fill_type="solid")
ASSUMPTION_FILL = PatternFill(start_color="FFF2CC", end_color="FFF2CC", fill_type="solid")

THIN = Side(style="thin", color="BFBFBF")
BORDER = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)

MONEY = '#,##0.0;(#,##0.0)'
MONEY0 = '#,##0;(#,##0)'
PCT0 = '0%'
MULT = '0.00"x"'


def read_csv(name):
    with open(os.path.join(DATA, name), newline="") as f:
        return list(csv.DictReader(f))


def title_bar(ws, text, span, row=1):
    ws.merge_cells(start_row=row, start_column=1, end_row=row, end_column=span)
    c = ws.cell(row=row, column=1, value=text)
    c.font = TITLE_FONT
    c.fill = DARK_FILL
    c.alignment = Alignment(vertical="center", indent=1)
    ws.row_dimensions[row].height = 28


def section(ws, row, col, text, span=1):
    ws.merge_cells(start_row=row, start_column=col, end_row=row, end_column=col + span - 1)
    c = ws.cell(row=row, column=col, value=text)
    c.font = SECTION_FONT
    c.fill = LIGHT_FILL
    return row + 1


def kv(ws, row, label, value, col=1, number_format=None, font=CALC_FONT, note=None):
    lc = ws.cell(row=row, column=col, value=label)
    lc.font = LABEL_FONT
    vc = ws.cell(row=row, column=col + 1, value=value)
    vc.font = font
    if number_format:
        vc.number_format = number_format
    if note:
        vc.comment = Comment(note, "model")
    return row + 1


wb = openpyxl.Workbook()
wb.remove(wb.active)

# ======================================================================
# TAB 1: Cover
# ======================================================================
ws = wb.create_sheet("Cover")
ws.column_dimensions["A"].width = 100
title_bar(ws, "Red Lobster -- LBO Case Study Model", span=1)
r = 3
intro = ('A reconstruction of the 2014 Golden Gate Capital acquisition of Red Lobster from Darden '
         'Restaurants (with a simultaneous real-estate sale-leaseback) through the May 2024 Chapter 11 '
         'filing. See docs/sources.md for every citation.')
ws.cell(row=r, column=1, value=intro).font = LABEL_FONT
ws.cell(row=r, column=1).alignment = Alignment(wrap_text=True, vertical="top")
ws.row_dimensions[r].height = 30
r += 2

r = section(ws, r, 1, "HOW THIS DIFFERS FROM A CONVENTIONAL LBO MODEL")
diffs = [
    "Golden Gate Capital put up only $600M of equity for a $2.1B deal -- a $1.5B real-estate sale-leaseback funded the rest.",
    "The sponsor (Golden Gate) fully exited in 2020, four years before the 2024 bankruptcy -- it did not hold through the collapse.",
    "Funded debt at the 2024 filing was a modest $294M. The real fixed-cost burden was $190.5M/year of above-market rent.",
    "No continuous annual financial panel exists -- Red Lobster was private with no SEC reporting obligation from 2014-2024.",
    "The equity wiped out in 2024 belonged to Thai Union / Seafood Alliance / former management, not Golden Gate.",
]
for d in diffs:
    ws.cell(row=r, column=1, value="• " + d).font = LABEL_FONT
    ws.cell(row=r, column=1).alignment = Alignment(wrap_text=True)
    r += 1
r += 1

r = section(ws, r, 1, "TABS IN THIS WORKBOOK")
tabs = [
    ("2014 Deal", "How the $2.1B purchase was actually funded, and what Darden did with the proceeds."),
    ("Pre-2014 Operating History", "Red Lobster's declining EBITDA as a Darden segment, FY2010 through the sale."),
    ("2016 Anchor Point", "Thai Union's $575M investment and the financials disclosed around it."),
    ("Capital Structure 2024", "Funded debt and lease obligations at the Chapter 11 filing."),
    ("Lease-Adjusted Leverage", "The illustrative capitalized-lease analysis -- the one flagged assumption in this workbook."),
    ("2023 Liquidity Collapse", "The cash walk from $100M to <$30M, as laid out in the first-day declaration."),
    ("Ownership & Outcome", "Who held equity when, and what happened to it in 2024."),
]
for name, desc in tabs:
    ws.cell(row=r, column=1, value=f"{name}:  {desc}").font = LABEL_FONT
    r += 1
r += 1
r = section(ws, r, 1, "KEY DISCLAIMER")
disclaimer = ("Blue font = pulled directly from a cited source. Black font = formula computed from those "
              "inputs. The ONE red-font figure in this workbook (the lease capitalization multiple, on the "
              "Lease-Adjusted Leverage tab) is an explicit, labeled illustrative assumption -- a standard "
              "credit-analysis rule of thumb, not a disclosed or audited figure. Several cells are explicitly "
              "left blank rather than estimated (e.g. Golden Gate Capital's 2020 exit terms) -- see "
              "docs/sources.md for exactly what is and isn't known.")
ws.cell(row=r, column=1, value=disclaimer).font = NOTE_FONT
ws.cell(row=r, column=1).alignment = Alignment(wrap_text=True, vertical="top")
ws.row_dimensions[r].height = 60

# ======================================================================
# TAB 2: 2014 Deal
# ======================================================================
deal = read_csv("deal_2014.csv")
ws = wb.create_sheet("2014 Deal")
ws.column_dimensions["A"].width = 48
ws.column_dimensions["B"].width = 14
ws.column_dimensions["C"].width = 30
ws.column_dimensions["D"].width = 60
title_bar(ws, "2014 Sale: Darden → Golden Gate Capital", span=4)
r = 3
ws.cell(row=r, column=1, value="See docs/sources.md §1-2.").font = NOTE_FONT
r += 2
hdr = r
for i, h in enumerate(["Item", "$M", "Source", "Notes"]):
    c = ws.cell(row=hdr, column=1 + i, value=h)
    c.font = HEADER_FONT
    c.fill = DARK_FILL
r += 1
deal_start = r
for row in deal:
    ws.cell(row=r, column=1, value=row["item"]).font = INPUT_FONT
    c = ws.cell(row=r, column=2, value=float(row["value_musd"]))
    c.font = INPUT_FONT
    c.number_format = MONEY0
    ws.cell(row=r, column=3, value=row["source"]).font = NOTE_FONT
    ws.cell(row=r, column=4, value=row["notes"]).font = NOTE_FONT
    r += 1
deal_end = r - 1
r += 1
r = section(ws, r, 1, "RECONCILIATION", span=4)
ggc_row = [i for i in range(deal_start, deal_end + 1) if ws.cell(row=i, column=1).value == "Golden Gate Capital equity contributed"][0]
re_row = [i for i in range(deal_start, deal_end + 1) if ws.cell(row=i, column=1).value == "Real estate sale-leaseback proceeds (American Realty Capital)"][0]
r = kv(ws, r, "Golden Gate equity + real estate proceeds", f"=B{ggc_row}+B{re_row}", font=Font(name=FONT, bold=True), number_format=MONEY0)
check_row = r - 1
r = kv(ws, r, "vs. disclosed total consideration", 2113, font=INPUT_FONT, number_format=MONEY0)
disclosed_row = r - 1
r = kv(ws, r, "Difference", f"=B{check_row}-B{disclosed_row}", font=CALC_FONT, number_format=MONEY0,
       note="Small gap ($13M on $2.1B) likely reflects rounding in the press-reported $600M/$1.5B split vs. the precise $2,113M disclosed consideration.")

for row in ws.iter_rows(min_row=hdr, max_row=r - 1, min_col=1, max_col=4):
    for cell in row:
        cell.border = BORDER

# ======================================================================
# TAB 3: Pre-2014 Operating History
# ======================================================================
darden = read_csv("pre_2014_darden_segment.csv")
ws = wb.create_sheet("Pre-2014 Operating History")
ws.column_dimensions["A"].width = 30
for i in range(len(darden)):
    ws.column_dimensions[get_column_letter(2 + i)].width = 14
title_bar(ws, "Red Lobster as a Darden Segment (docs/sources.md §1)", span=1 + len(darden))
r = 3
ws.cell(row=r, column=1, value="Source: Darden's own 2014 investor presentation re: the Red Lobster sale.").font = NOTE_FONT
r += 2
hdr = r
ws.cell(row=hdr, column=1, value="Period").font = HEADER_FONT
ws.cell(row=hdr, column=1).fill = DARK_FILL
for i, row in enumerate(darden):
    c = ws.cell(row=hdr, column=2 + i, value=row["period"])
    c.font = HEADER_FONT
    c.fill = DARK_FILL
    c.alignment = Alignment(horizontal="center")
r += 1
fields = [("Revenue ($B)", "revenue_busd", MONEY), ("Revenue growth", "revenue_growth_pct", PCT0),
          ("EBITDA ($M)", "ebitda_musd", MONEY0), ("EBITDA margin", "ebitda_margin_pct", PCT0)]
for label, key, fmt in fields:
    ws.cell(row=r, column=1, value=label).font = LABEL_FONT
    for i, row in enumerate(darden):
        val = float(row[key])
        if "pct" in key:
            val = val / 100
        c = ws.cell(row=r, column=2 + i, value=val)
        c.font = INPUT_FONT
        c.number_format = fmt
    r += 1
for row in ws.iter_rows(min_row=hdr, max_row=r - 1, min_col=1, max_col=1 + len(darden)):
    for cell in row:
        cell.border = BORDER

# ======================================================================
# TAB 4: 2016 Anchor Point
# ======================================================================
anchor = read_csv("anchor_2016_thai_union.csv")
ws = wb.create_sheet("2016 Anchor Point")
ws.column_dimensions["A"].width = 48
ws.column_dimensions["B"].width = 14
ws.column_dimensions["C"].width = 10
ws.column_dimensions["D"].width = 60
title_bar(ws, "2016: Thai Union's Investment (docs/sources.md §3)", span=4)
r = 3
ws.cell(row=r, column=1, value="The only solid financial anchor point between the 2014 sale and the 2024 filing.").font = NOTE_FONT
r += 2
hdr = r
for i, h in enumerate(["Metric", "Value", "Unit", "Source"]):
    c = ws.cell(row=hdr, column=1 + i, value=h)
    c.font = HEADER_FONT
    c.fill = DARK_FILL
r += 1
for row in anchor:
    ws.cell(row=r, column=1, value=row["metric"]).font = INPUT_FONT
    c = ws.cell(row=r, column=2, value=float(row["value"]))
    c.font = INPUT_FONT
    c.number_format = MONEY0 if row["unit"] == "musd" else PCT0 if row["unit"] == "pct" else "General"
    if row["unit"] == "pct":
        ws.cell(row=r, column=2).value = float(row["value"]) / 100
    ws.cell(row=r, column=3, value=row["unit"]).font = NOTE_FONT
    ws.cell(row=r, column=4, value=row["source"]).font = NOTE_FONT
    r += 1
for row in ws.iter_rows(min_row=hdr, max_row=r - 1, min_col=1, max_col=4):
    for cell in row:
        cell.border = BORDER

# ======================================================================
# TAB 5: Capital Structure 2024
# ======================================================================
capstruct = read_csv("capital_structure_at_filing_2024.csv")
ws = wb.create_sheet("Capital Structure 2024")
ws.column_dimensions["A"].width = 54
ws.column_dimensions["B"].width = 14
ws.column_dimensions["C"].width = 44
ws.column_dimensions["D"].width = 40
title_bar(ws, "Capital Structure at the May 2024 Filing (docs/sources.md §5)", span=4)
r = 3
hdr = r + 1
for i, h in enumerate(["Item", "$M", "Detail", "Source"]):
    c = ws.cell(row=hdr, column=1 + i, value=h)
    c.font = HEADER_FONT
    c.fill = DARK_FILL
r = hdr + 1
cap_start = r
cap_rows = {}
for row in capstruct:
    ws.cell(row=r, column=1, value=row["item"]).font = INPUT_FONT
    c = ws.cell(row=r, column=2, value=float(row["value_musd"]))
    c.font = INPUT_FONT
    c.number_format = MONEY
    ws.cell(row=r, column=3, value=row["detail"]).font = NOTE_FONT
    ws.cell(row=r, column=4, value=row["source"]).font = NOTE_FONT
    cap_rows[row["item"]] = r
    r += 1
for row in ws.iter_rows(min_row=hdr, max_row=r - 1, min_col=1, max_col=4):
    for cell in row:
        cell.border = BORDER

# ======================================================================
# TAB 6: Lease-Adjusted Leverage
# ======================================================================
ws = wb.create_sheet("Lease-Adjusted Leverage")
ws.column_dimensions["A"].width = 44
ws.column_dimensions["B"].width = 16
title_bar(ws, "Lease-Adjusted Leverage (Illustrative)", span=2)
r = 3
note = ("Funded debt alone looks modest. This tab capitalizes the 2023 annual rent at an illustrative "
        "multiple to show the real fixed-obligation load -- a standard credit-analysis technique, not a "
        "disclosed or audited figure. Change the red cell to test sensitivity.")
ws.cell(row=r, column=1, value=note).font = NOTE_FONT
ws.cell(row=r, column=1).alignment = Alignment(wrap_text=True)
ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=2)
ws.row_dimensions[r].height = 45
r += 2

r = kv(ws, r, "Funded debt at filing ($M)", f"='Capital Structure 2024'!B{cap_rows['Total funded debt at filing']}",
       font=CALC_FONT, number_format=MONEY)
funded_debt_row = r - 1
r = kv(ws, r, "2023 annual lease obligations ($M)", f"='Capital Structure 2024'!B{cap_rows['2023 total lease obligations']}",
       font=CALC_FONT, number_format=MONEY)
rent_row = r - 1
r += 1
mult_row = r
mc = ws.cell(row=r, column=1, value="Illustrative lease capitalization multiple")
mc.font = LABEL_FONT
vc = ws.cell(row=r, column=2, value=8.0)
vc.font = ASSUMPTION_FONT
vc.fill = ASSUMPTION_FILL
vc.number_format = MULT
vc.comment = Comment(
    "THE ONE FULLY ASSUMED NUMBER IN THIS WORKBOOK. 8x annual rent is a commonly used rule of thumb for "
    "capitalizing operating leases into a debt-equivalent balance (~12.5% implied cap rate). Not a figure "
    "from any Red Lobster filing -- change this cell to test sensitivity.",
    "model",
)
r += 1
r = kv(ws, r, "Implied 'lease debt' ($M)", f"=B{rent_row}*B{mult_row}", font=Font(name=FONT, bold=True), number_format=MONEY)
lease_debt_row = r - 1
r = kv(ws, r, "Total effective fixed obligations ($M)", f"=B{funded_debt_row}+B{lease_debt_row}", font=Font(name=FONT, bold=True), number_format=MONEY)
total_row = r - 1
r = kv(ws, r, "Lease debt as a multiple of funded debt", f"=B{lease_debt_row}/B{funded_debt_row}", font=Font(name=FONT, bold=True), number_format=MULT)
r += 1
ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=2)
ws.cell(row=r, column=1, value="Takeaway: looking only at funded debt (~$294M) materially understates how "
        "little margin for error this business had. The sale-leaseback moved the real financial risk off "
        "the balance sheet's debt line and into a rent line that shows up as an operating expense instead.").font = NOTE_FONT
ws.cell(row=r, column=1).alignment = Alignment(wrap_text=True)
ws.row_dimensions[r].height = 45

for row in ws.iter_rows(min_row=3, max_row=r, min_col=1, max_col=2):
    for cell in row:
        if cell.row >= 6:
            cell.border = BORDER

# ======================================================================
# TAB 7: 2023 Liquidity Collapse
# ======================================================================
liq = read_csv("liquidity_collapse_2023.csv")
ws = wb.create_sheet("2023 Liquidity Collapse")
ws.column_dimensions["A"].width = 60
ws.column_dimensions["B"].width = 14
ws.column_dimensions["C"].width = 30
ws.column_dimensions["D"].width = 40
title_bar(ws, "The 2023 Cash Collapse (docs/sources.md §5)", span=4)
r = 3
hdr = r + 1
for i, h in enumerate(["Event", "$M", "Period", "Source"]):
    c = ws.cell(row=hdr, column=1 + i, value=h)
    c.font = HEADER_FONT
    c.fill = DARK_FILL
r = hdr + 1
start_cash_row = None
for row in liq:
    ws.cell(row=r, column=1, value=row["event"]).font = INPUT_FONT
    c = ws.cell(row=r, column=2, value=float(row["value_musd"]))
    c.font = INPUT_FONT
    c.number_format = MONEY
    ws.cell(row=r, column=3, value=row["period"]).font = NOTE_FONT
    ws.cell(row=r, column=4, value=row["source"]).font = NOTE_FONT
    if row["event"] == "Cash on hand" and start_cash_row is None:
        start_cash_row = r
    r += 1
for row in ws.iter_rows(min_row=hdr, max_row=r - 1, min_col=1, max_col=4):
    for cell in row:
        cell.border = BORDER
r += 1
ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=4)
ws.cell(row=r, column=1, value="The three itemized outflows (operating losses, forced ABL paydown, interest) "
        "sum to -$90M against the $100M starting balance, implying ~$10M -- the declaration states the actual "
        "floor was 'less than $30 million,' meaning smaller unitemized inflows partially offset these three "
        "drivers. That gap is shown, not reconciled away.").font = NOTE_FONT
ws.cell(row=r, column=1).alignment = Alignment(wrap_text=True)
ws.row_dimensions[r].height = 45

# ======================================================================
# TAB 8: Ownership & Outcome
# ======================================================================
outcome = read_csv("bankruptcy_outcome_2024.csv")
ws = wb.create_sheet("Ownership & Outcome")
ws.column_dimensions["A"].width = 20
ws.column_dimensions["B"].width = 85
title_bar(ws, "Ownership Timeline & the 2024 Outcome", span=2)
r = 3
timeline = [
    ("2014", "Golden Gate Capital buys Red Lobster from Darden ($2.1B; $600M own equity + $1.5B real estate monetization)."),
    ("2016", "Thai Union invests $575M for a 49% stake (25% common + 24% convertible preferred)."),
    ("2020", "Golden Gate Capital FULLY EXITS -- sells remaining stake to Thai Union, management, and 'Seafood Alliance.' Exit terms not disclosed in sources reviewed."),
    ("2021", "New $264.7M Term Loan arranged with Fortress Credit Corp."),
    ("2023", "Liquidity crisis: cash falls from $100M to <$30M in ~6 months; $76M net loss for the year."),
    ("May 2024", "Chapter 11 filed. Ownership at filing: Thai Union ~47% common + 100% preferred; Seafood Alliance ~38% common; former management, remainder."),
    ("Sep 2024", "Fortress (the secured lender) credit-bids $376M and takes ownership. Thai Union / Seafood Alliance / management equity -> $0."),
]
hdr = r
ws.cell(row=hdr, column=1, value="Year").font = HEADER_FONT
ws.cell(row=hdr, column=1).fill = DARK_FILL
ws.cell(row=hdr, column=2, value="Event").font = HEADER_FONT
ws.cell(row=hdr, column=2).fill = DARK_FILL
r += 1
for year, event in timeline:
    ws.cell(row=r, column=1, value=year).font = INPUT_FONT
    c = ws.cell(row=r, column=2, value=event)
    c.font = INPUT_FONT
    c.alignment = Alignment(wrap_text=True, vertical="top")
    ws.row_dimensions[r].height = 30
    r += 1
for row in ws.iter_rows(min_row=hdr, max_row=r - 1, min_col=1, max_col=2):
    for cell in row:
        cell.border = BORDER
r += 1

r = section(ws, r, 1, "FINAL OUTCOME DETAIL", span=2)
for row in outcome:
    ws.cell(row=r, column=1, value=row["item"]).font = LABEL_FONT
    v = ws.cell(row=r, column=2, value=row["value"])
    if "NOT DISCLOSED" in str(row["value"]):
        v.font = ASSUMPTION_FONT
        v.fill = ASSUMPTION_FILL
    else:
        v.font = INPUT_FONT
    v.alignment = Alignment(wrap_text=True)
    r += 1

out_path = os.path.join(HERE, "RedLobster_LBO_Model.xlsx")
wb.save(out_path)
print("wrote", out_path)
