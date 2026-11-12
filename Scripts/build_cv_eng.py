
from reportlab.pdfgen import canvas as rl_canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph, Frame, Spacer
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus.flowables import HRFlowable

# ── Fonts ──────────────────────────────────────────────────────────────────
pdfmetrics.registerFont(TTFont("DV",   "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("DV-B", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"))

W, H = A4

# ── Colors ─────────────────────────────────────────────────────────────────
BLACK   = colors.HexColor("#1a1a1a")
DARK    = colors.HexColor("#333333")
MID     = colors.HexColor("#555555")
GREY    = colors.HexColor("#888888")
LGREY   = colors.HexColor("#bbbbbb")
RULE    = colors.HexColor("#cccccc")
WHITE   = colors.white

# ── Layout — 3 columns ────────────────────────────────────────────────────
MARGIN_X = 11 * mm
MARGIN_Y = 8 * mm
TOTAL_W  = W - 2 * MARGIN_X

COL_L_W  = 42 * mm
COL_M_W  = 93 * mm
COL_R_W  = TOTAL_W - COL_L_W - COL_M_W - 6 * mm
GAP      = 3 * mm

COL_L_X  = MARGIN_X
COL_M_X  = COL_L_X + COL_L_W + GAP
COL_R_X  = COL_M_X + COL_M_W + GAP

HEADER_H = 22 * mm
BODY_Y   = H - MARGIN_Y - HEADER_H - 2 * mm
BODY_H   = BODY_Y - MARGIN_Y

# ── Style helper ───────────────────────────────────────────────────────────
def S(name, font="DV", size=7.5, leading=11, color=DARK, sb=0, sa=2, align=0):
    return ParagraphStyle(name, fontName=font, fontSize=size, leading=leading,
                          textColor=color, spaceBefore=sb, spaceAfter=sa, alignment=align)

sSecHdr  = S("sSecHdr",  "DV",    6.5, 9,    LGREY, sb=0,  sa=3,   align=0)
sJobT    = S("sJobT",    "DV-B",  8,   11,   BLACK, sb=6,  sa=0)
sJobC    = S("sJobC",    "DV-B",  7,   10,   MID,   sb=0,  sa=0)
sJobD    = S("sJobD",    "DV",    6.5, 9,    GREY,  sb=0,  sa=3)
sBul     = S("sBul",     "DV",    6.8, 10.2, DARK,  sb=0,  sa=2.2)
sLabel   = S("sLabel",   "DV-B",  7,   10,   BLACK, sb=4,  sa=1)
sLBody   = S("sLBody",   "DV",    7,   10.5, DARK,  sb=0,  sa=2)
sSkill   = S("sSkill",   "DV",    7,   10,   DARK,  sb=0,  sa=2.5)
sEduT    = S("sEduT",    "DV-B",  7.5, 11,   BLACK, sb=5,  sa=0)
sEduI    = S("sEduI",    "DV",    7,   10,   MID,   sb=0,  sa=0)
sEduD    = S("sEduD",    "DV",    6.5, 9,    GREY,  sb=0,  sa=4)
sCert    = S("sCert",    "DV",    6.5, 9.5,  DARK,  sb=0,  sa=2)
sCertB   = S("sCertB",   "DV-B",  6.5, 9.5,  DARK,  sb=4,  sa=0)

def rule(w, color=RULE, t=0.5, sa=3):
    return HRFlowable(width=w, color=color, thickness=t, spaceAfter=sa)

def sec(label):
    return [Paragraph(label, sSecHdr), rule(99999)]

# ── LEFT COLUMN ────────────────────────────────────────────────────────────
def left_col():
    s = []

    s += sec("C o n t a c t")
    s += [Paragraph("romanripari@gmail.com", sLBody),
          Paragraph("linkedin.com/in/romanripari", sLBody),
          Paragraph("https://romanripari.ar", sLBody),
          Paragraph("Buenos Aires, Argentina", sLBody)]

    s += sec("S k i l l s")
    for sk in [
        "Excel / VBA",
        "Python",
        "SQL (SSMS)",
        "Alteryx",
        "Power BI",
        "Azure DevOps",
        "Big Data",
        "Git",
        "AI / LLMs",
        "ETL / Data Pipelines",
        "Data Visualization",
        "Database Management",
        "Competitive Intelligence",
        "Data Storytelling",
    ]:
        s.append(Paragraph(f"• {sk}", sSkill))

    s += sec("L a n g u a g e s")
    s += [Paragraph("English — Advanced", sLBody),
          Paragraph("Spanish — Native", sLBody)]

    s += sec("C e r t i f i c a t i o n s")
    s += [Paragraph("EF Standard English Test", sCert),
          Paragraph("(EF SET)", sCert),
          Spacer(1, 2*mm),
          Paragraph("[PCEP-30-02] PCEP –", sCertB),
          Paragraph("Certified Entry-Level", sCert),
          Paragraph("Python Programmer", sCert)]

    return s

# ── CENTER COLUMN — Experience ─────────────────────────────────────────────
def center_col():
    s = []
    s += sec("E x p e r i e n c e")

    # PGD
    s.append(Paragraph("Senior Data Analyst", sJobT))
    s.append(Paragraph("Publicis Global Delivery (PGD)", sJobC))
    s.append(Paragraph("Jul. 2021 – Present  ·  United States", sJobD))
    for b in [
        "Lead the analysis, production, and delivery of monthly and ad-hoc Competitive Intelligence reports for top-tier global accounts including The Coca-Cola Company (CPG / FMCG).",
        "Process and transform large-scale datasets (100K+ records) covering ad spend, impressions, creative performance, and share of voice across brands, categories, and channels (video, social, OTT, display).",
        "Develop custom automated reporting and data analysis tools in Excel (VBA / Macros), significantly optimizing processing times for international teams.",
        "Integrate generative AI tools and LLMs into analytical workflows to increase delivery speed and insight quality.",
        "Translate internal business requirements from stakeholders into actionable data solutions; provide ongoing technical support for implemented tools.",
        "Manage the full data project lifecycle in Azure DevOps: planning, sprint tracking, quality control, and deadline management.",
        "Act as Performance Manager: mentor team members in technical skills development, productivity, and career growth.",
    ]:
        s.append(Paragraph(f"◦ {b}", sBul))

    # EY
    s.append(Paragraph("Senior Analyst VBA + Alteryx", sJobT))
    s.append(Paragraph("EY International", sJobC))
    s.append(Paragraph("Jun. 2019 – Jul. 2021", sJobD))
    for b in [
        "Business Intelligence (BI) team lead: people management, task allocation, and deliverable quality control.",
        "Developed interactive dashboards and automation tools in Excel-VBA and Power BI for multiple business units.",
        "ETL and data wrangling: cleaning, transformation, and integration of data from heterogeneous sources using Alteryx.",
        "Structured data analysis and reporting from multiple sources; daily creation and maintenance of SQL (SSMS) databases.",
        "End-to-end project management from planning to execution using Azure DevOps.",
        "Delivered technical training in Excel, VBA, and Alteryx to internal teams.",
    ]:
        s.append(Paragraph(f"◦ {b}", sBul))

    # IPG
    s.append(Paragraph("Data Projects Analyst", sJobT))
    s.append(Paragraph("IPG Mediabrands", sJobC))
    s.append(Paragraph("Sep. 2018 – Jun. 2019", sJobD))
    for b in [
        "Multi-dimensional business analysis: sales, brand equity, search interest, competitiveness, web traffic, social media, and advertising activity.",
        "Built and maintained Power BI dashboards to surface commercial and media insights; identified performance drivers and gaps.",
        "End-to-end data process oversight and cross-functional stakeholder coordination (clients, agencies, internal teams, vendors).",
    ]:
        s.append(Paragraph(f"◦ {b}", sBul))

    # Nielsen
    s.append(Paragraph("Senior Analyst", sJobT))
    s.append(Paragraph("Nielsen", sJobC))
    s.append(Paragraph("Dec. 2011 – Apr. 2018", sJobD))
    for b in [
        "Data Analysis and Business Intelligence (BI) for internal and external clients across Argentina and Latin America.",
        "Generated KPI reports for multiple management levels; queried and analyzed structured databases using specialized software.",
        "Served global clients directly: Danone, The Coca-Cola Company, Unilever, PepsiCo, Clorox, Genomma, Procter &amp; Gamble, Mead Johnson, Peñaflor, Mondelez, and others.",
        "Developed custom reports tailored to each client's specific business needs and market dynamics.",
        "Internal reporting tasks: category management, economic performance tracking via custom \"baskets\", and wholesale market reporting.",
    ]:
        s.append(Paragraph(f"◦ {b}", sBul))

    return s

# ── RIGHT COLUMN — Education ───────────────────────────────────────────────
def right_col():
    s = []
    s += sec("E d u c a t i o n")

    for title, inst, date in [
        ("B.S. in Data Science\n(in progress)", "Universidad de\nBuenos Aires", "2020 – Present"),
        ("Android App\nDevelopment", "Educación IT", "2018 – 2019"),
        ("B.A. in Literature", "Universidad de\nBuenos Aires", "2011 – 2014"),
        ("B.S. in Commerce", "Universidad Nacional\nde Quilmes", "2011 – 2014"),
    ]:
        s.append(Paragraph(title.replace("\n", "<br/>"), sEduT))
        s.append(Paragraph(inst.replace("\n", "<br/>"), sEduI))
        s.append(Paragraph(date, sEduD))

    return s

# ── BUILD PDF ──────────────────────────────────────────────────────────────
OUT = "/tmp/CV_RomanRipari_Eng.pdf"
c = rl_canvas.Canvas(OUT, pagesize=A4)

c.setFillColor(WHITE)
c.rect(0, 0, W, H, fill=1, stroke=0)

# Header
c.setFillColor(BLACK)
c.setFont("DV-B", 22)
name_y = H - MARGIN_Y - 10 * mm
c.drawCentredString(W / 2, name_y, "Roman Ariel Ripari")

c.setFont("DV", 10)
c.setFillColor(MID)
c.drawCentredString(W / 2, name_y - 7 * mm, "Senior Data Analyst  |  Business Intelligence  |  Competitive Intelligence")

c.setStrokeColor(RULE)
c.setLineWidth(0.5)
c.line(MARGIN_X, H - MARGIN_Y - HEADER_H, W - MARGIN_X, H - MARGIN_Y - HEADER_H)

# Frames
def make_frame(x, w, story):
    fr = Frame(x, MARGIN_Y, w, BODY_H,
               leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0,
               showBoundary=0)
    overflow = list(story)
    fr.addFromList(overflow, c)
    return overflow

ls = left_col()
ms = center_col()
rs = right_col()

lo = make_frame(COL_L_X, COL_L_W, ls)
mo = make_frame(COL_M_X, COL_M_W, ms)
ro = make_frame(COL_R_X, COL_R_W, rs)

for col_name, overflow in [("Left", lo), ("Center", mo), ("Right", ro)]:
    if overflow:
        print(f"⚠ {col_name} col overflow: {len(overflow)} items", flush=True)
    else:
        print(f"✓ {col_name} col fits", flush=True)

c.showPage()
c.save()
print(f"✓ Saved: {OUT}", flush=True)
print("DONE", flush=True)
