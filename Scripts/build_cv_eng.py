
# =============================================================================
# CV - Roman Ariel Ripari (English)
# Requires: pip install reportlab pypdf
# Fonts:    sudo apt install fonts-dejavu  (Linux)
#           On Windows/Mac: update FONT_REGULAR and FONT_BOLD with local paths
# =============================================================================

from reportlab.pdfgen import canvas as pdf_canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph, Frame, Spacer
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus.flowables import HRFlowable

# =============================================================================
# CONFIGURATION — edit these variables to customize the CV
# =============================================================================

OUTPUT_FILE = "CV_RomanRipari_Eng.pdf"

FONT_REGULAR = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONT_BOLD    = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

# Colors
COLOR_BLACK       = colors.HexColor("#1a1a1a")   # name and job titles
COLOR_DARK        = colors.HexColor("#333333")   # main body text
COLOR_MEDIUM      = colors.HexColor("#555555")   # company / header subtitle
COLOR_GREY        = colors.HexColor("#888888")   # dates
COLOR_LIGHT_GREY  = colors.HexColor("#bbbbbb")   # section headers
COLOR_RULE        = colors.HexColor("#cccccc")   # divider lines
COLOR_WHITE       = colors.white

# Margins and columns
MARGIN_LEFT_RIGHT = 11 * mm
MARGIN_TOP_BOTTOM = 8  * mm
PAGE_WIDTH, PAGE_HEIGHT = A4
USABLE_WIDTH = PAGE_WIDTH - 2 * MARGIN_LEFT_RIGHT

LEFT_COL_WIDTH   = 42 * mm   # left column: contact / skills / certs
CENTER_COL_WIDTH = 93 * mm   # center column: experience
RIGHT_COL_WIDTH  = USABLE_WIDTH - LEFT_COL_WIDTH - CENTER_COL_WIDTH - 6 * mm  # education
COL_GAP          = 3 * mm    # gap between columns

LEFT_COL_X   = MARGIN_LEFT_RIGHT
CENTER_COL_X = LEFT_COL_X + LEFT_COL_WIDTH + COL_GAP
RIGHT_COL_X  = CENTER_COL_X + CENTER_COL_WIDTH + COL_GAP

HEADER_HEIGHT = 22 * mm
BODY_TOP_Y    = PAGE_HEIGHT - MARGIN_TOP_BOTTOM - HEADER_HEIGHT - 2 * mm
BODY_HEIGHT   = BODY_TOP_Y - MARGIN_TOP_BOTTOM

# =============================================================================
# FONT REGISTRATION
# =============================================================================

pdfmetrics.registerFont(TTFont("Regular", FONT_REGULAR))
pdfmetrics.registerFont(TTFont("Bold",    FONT_BOLD))

# =============================================================================
# PARAGRAPH STYLES
# Helper: make_style(name, font, size, line_height, color, space_before, space_after, alignment)
# =============================================================================

def make_style(name, font="Regular", size=7.5, line_height=11, color=COLOR_DARK,
               space_before=0, space_after=2, alignment=0):
    return ParagraphStyle(
        name,
        fontName=font,
        fontSize=size,
        leading=line_height,
        textColor=color,
        spaceBefore=space_before,
        spaceAfter=space_after,
        alignment=alignment,
    )

style_section_header  = make_style("section_header", "Regular", 6.5, 9,    COLOR_LIGHT_GREY, space_after=3)
style_job_title       = make_style("job_title",       "Bold",    8,   11,   COLOR_BLACK,      space_before=6)
style_company         = make_style("company",         "Bold",    7,   10,   COLOR_MEDIUM)
style_date            = make_style("date",            "Regular", 6.5, 9,    COLOR_GREY,       space_after=3)
style_bullet          = make_style("bullet",          "Regular", 6.8, 10.2, COLOR_DARK,       space_after=2.2)
style_left_body       = make_style("left_body",       "Regular", 7,   10.5, COLOR_DARK,       space_after=2)
style_skill           = make_style("skill",           "Regular", 7,   10,   COLOR_DARK,       space_after=2.5)
style_edu_title       = make_style("edu_title",       "Bold",    7.5, 11,   COLOR_BLACK,      space_before=5)
style_edu_institution = make_style("edu_institution", "Regular", 7,   10,   COLOR_MEDIUM)
style_edu_date        = make_style("edu_date",        "Regular", 6.5, 9,    COLOR_GREY,       space_after=4)
style_cert_regular    = make_style("cert_regular",    "Regular", 6.5, 9.5,  COLOR_DARK,       space_after=2)
style_cert_bold       = make_style("cert_bold",       "Bold",    6.5, 9.5,  COLOR_DARK,       space_before=4)

# =============================================================================
# HELPER FUNCTIONS
# =============================================================================

def horizontal_line(width=99999, color=COLOR_RULE, thickness=0.5, space_after=3):
    """Horizontal divider line."""
    return HRFlowable(width=width, color=color, thickness=thickness, spaceAfter=space_after)

def section_header(label):
    """Section header with divider line below (e.g. 'S k i l l s')."""
    return [Paragraph(label, style_section_header), horizontal_line()]

def render_column(canvas, x_position, width, content_list):
    """Renders a list of flowables into a column and returns any overflow."""
    frame = Frame(
        x_position, MARGIN_TOP_BOTTOM,
        width, BODY_HEIGHT,
        leftPadding=0, rightPadding=0,
        topPadding=0, bottomPadding=0,
        showBoundary=0,
    )
    overflow = list(content_list)
    frame.addFromList(overflow, canvas)
    return overflow

# =============================================================================
# LEFT COLUMN — Contact, Skills, Languages, Certifications
# =============================================================================

def build_left_column():
    content = []

    content += section_header("C o n t a c t")
    content += [
        Paragraph("romanripari@gmail.com",       style_left_body),
        Paragraph("linkedin.com/in/romanripari", style_left_body),
        Paragraph("https://romanripari.ar",      style_left_body),
        Paragraph("Buenos Aires, Argentina",     style_left_body),
    ]

    content += section_header("S k i l l s")
    skills = [
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
    ]
    for skill in skills:
        content.append(Paragraph(f"• {skill}", style_skill))

    content += section_header("L a n g u a g e s")
    content += [
        Paragraph("English — Advanced", style_left_body),
        Paragraph("Spanish — Native",   style_left_body),
    ]

    content += section_header("C e r t i f i c a t i o n s")
    content += [
        Paragraph("EF Standard English Test",  style_cert_regular),
        Paragraph("(EF SET)",                  style_cert_regular),
        Spacer(1, 2 * mm),
        Paragraph("[PCEP-30-02] PCEP –",       style_cert_bold),
        Paragraph("Certified Entry-Level",     style_cert_regular),
        Paragraph("Python Programmer",         style_cert_regular),
    ]

    return content

# =============================================================================
# CENTER COLUMN — Experience
# =============================================================================

def build_center_column():
    content = []
    content += section_header("E x p e r i e n c e")

    # ── PGD ──────────────────────────────────────────────────────────────────
    content.append(Paragraph("Senior Data Analyst",                   style_job_title))
    content.append(Paragraph("Publicis Global Delivery (PGD)",        style_company))
    content.append(Paragraph("Jul. 2021 – Present  ·  United States", style_date))
    pgd_bullets = [
        "Lead the analysis, production, and delivery of monthly and ad-hoc Competitive Intelligence reports for top-tier global accounts including The Coca-Cola Company (CPG / FMCG).",
        "Process and transform large-scale datasets (100K+ records) covering ad spend, impressions, creative performance, and share of voice across brands, categories, and channels (video, social, OTT, display).",
        "Develop custom automated reporting and data analysis tools in Excel (VBA / Macros), significantly optimizing processing times for international teams.",
        "Integrate generative AI tools and LLMs into analytical workflows to increase delivery speed and insight quality.",
        "Translate internal business requirements from stakeholders into actionable data solutions; provide ongoing technical support for implemented tools.",
        "Manage the full data project lifecycle in Azure DevOps: planning, sprint tracking, quality control, and deadline management.",
        "Act as Performance Manager: mentor team members in technical skills development, productivity, and career growth.",
    ]
    for bullet in pgd_bullets:
        content.append(Paragraph(f"◦ {bullet}", style_bullet))

    # ── EY ───────────────────────────────────────────────────────────────────
    content.append(Paragraph("Senior Analyst VBA + Alteryx", style_job_title))
    content.append(Paragraph("EY International",             style_company))
    content.append(Paragraph("Jun. 2019 – Jul. 2021",        style_date))
    ey_bullets = [
        "Business Intelligence (BI) team lead: people management, task allocation, and deliverable quality control.",
        "Developed interactive dashboards and automation tools in Excel-VBA and Power BI for multiple business units.",
        "ETL and data wrangling: cleaning, transformation, and integration of data from heterogeneous sources using Alteryx.",
        "Structured data analysis and reporting from multiple sources; daily creation and maintenance of SQL (SSMS) databases.",
        "End-to-end project management from planning to execution using Azure DevOps.",
        "Delivered technical training in Excel, VBA, and Alteryx to internal teams.",
    ]
    for bullet in ey_bullets:
        content.append(Paragraph(f"◦ {bullet}", style_bullet))

    # ── IPG ──────────────────────────────────────────────────────────────────
    content.append(Paragraph("Data Projects Analyst", style_job_title))
    content.append(Paragraph("IPG Mediabrands",       style_company))
    content.append(Paragraph("Sep. 2018 – Jun. 2019", style_date))
    ipg_bullets = [
        "Multi-dimensional business analysis: sales, brand equity, search interest, competitiveness, web traffic, social media, and advertising activity.",
        "Built and maintained Power BI dashboards to surface commercial and media insights; identified performance drivers and gaps.",
        "End-to-end data process oversight and cross-functional stakeholder coordination (clients, agencies, internal teams, vendors).",
    ]
    for bullet in ipg_bullets:
        content.append(Paragraph(f"◦ {bullet}", style_bullet))

    # ── NIELSEN ──────────────────────────────────────────────────────────────
    content.append(Paragraph("Senior Analyst",        style_job_title))
    content.append(Paragraph("Nielsen",               style_company))
    content.append(Paragraph("Dec. 2011 – Apr. 2018", style_date))
    nielsen_bullets = [
        "Data Analysis and Business Intelligence (BI) for internal and external clients across Argentina and Latin America.",
        "Generated KPI reports for multiple management levels; queried and analyzed structured databases using specialized software.",
        "Served global clients directly: Danone, The Coca-Cola Company, Unilever, PepsiCo, Clorox, Genomma, Procter &amp; Gamble, Mead Johnson, Peñaflor, Mondelez, and others.",
        "Developed custom reports tailored to each client's specific business needs and market dynamics.",
        "Internal reporting tasks: category management, economic performance tracking via custom \"baskets\", and wholesale market reporting.",
    ]
    for bullet in nielsen_bullets:
        content.append(Paragraph(f"◦ {bullet}", style_bullet))

    return content

# =============================================================================
# RIGHT COLUMN — Education
# =============================================================================

def build_right_column():
    content = []
    content += section_header("E d u c a t i o n")

    education = [
        ("B.S. in Data Science\n(in progress)", "Universidad de\nBuenos Aires",     "2020 – Present"),
        ("Android App\nDevelopment",             "Educación IT",                    "2018 – 2019"),
        ("B.A. in Literature",                   "Universidad de\nBuenos Aires",    "2011 – 2014"),
        ("B.S. in Commerce",                     "Universidad Nacional\nde Quilmes","2011 – 2014"),
    ]
    for degree_title, institution, years in education:
        content.append(Paragraph(degree_title.replace("\n", "<br/>"), style_edu_title))
        content.append(Paragraph(institution.replace("\n", "<br/>"), style_edu_institution))
        content.append(Paragraph(years, style_edu_date))

    return content

# =============================================================================
# BUILD THE PDF
# =============================================================================

canvas = pdf_canvas.Canvas(OUTPUT_FILE, pagesize=A4)

# White background
canvas.setFillColor(COLOR_WHITE)
canvas.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=1, stroke=0)

# ── Header: Name and subtitle centered ───────────────────────────────────
name_y = PAGE_HEIGHT - MARGIN_TOP_BOTTOM - 10 * mm

canvas.setFillColor(COLOR_BLACK)
canvas.setFont("Bold", 22)
canvas.drawCentredString(PAGE_WIDTH / 2, name_y, "Roman Ariel Ripari")

canvas.setFont("Regular", 10)
canvas.setFillColor(COLOR_MEDIUM)
canvas.drawCentredString(PAGE_WIDTH / 2, name_y - 7 * mm,
                         "Senior Data Analyst  |  Business Intelligence  |  Competitive Intelligence")

# Divider line below header
canvas.setStrokeColor(COLOR_RULE)
canvas.setLineWidth(0.5)
canvas.line(MARGIN_LEFT_RIGHT, PAGE_HEIGHT - MARGIN_TOP_BOTTOM - HEADER_HEIGHT,
            PAGE_WIDTH - MARGIN_LEFT_RIGHT, PAGE_HEIGHT - MARGIN_TOP_BOTTOM - HEADER_HEIGHT)

# ── Render the three columns ──────────────────────────────────────────────
left_content   = build_left_column()
center_content = build_center_column()
right_content  = build_right_column()

left_overflow   = render_column(canvas, LEFT_COL_X,   LEFT_COL_WIDTH,   left_content)
center_overflow = render_column(canvas, CENTER_COL_X, CENTER_COL_WIDTH, center_content)
right_overflow  = render_column(canvas, RIGHT_COL_X,  RIGHT_COL_WIDTH,  right_content)

for col_name, overflow in [("Left", left_overflow), ("Center", center_overflow), ("Right", right_overflow)]:
    if overflow:
        print(f"⚠ Column {col_name}: {len(overflow)} items did not fit", flush=True)
    else:
        print(f"✓ Column {col_name}: OK", flush=True)

canvas.showPage()
canvas.save()
print(f"✓ PDF saved: {OUTPUT_FILE}", flush=True)
