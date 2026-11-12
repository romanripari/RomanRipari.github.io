
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

W, H = A4  # 595.27 x 841.89 pts

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
TOTAL_W  = W - 2 * MARGIN_X          # usable width

COL_L_W  = 42 * mm   # left: contact / skills / certs
COL_M_W  = 93 * mm   # center: experience (widest)
COL_R_W  = TOTAL_W - COL_L_W - COL_M_W - 6 * mm  # right: education
GAP      = 3 * mm

COL_L_X  = MARGIN_X
COL_M_X  = COL_L_X + COL_L_W + GAP
COL_R_X  = COL_M_X + COL_M_W + GAP

# Header block height
HEADER_H = 22 * mm
BODY_Y   = H - MARGIN_Y - HEADER_H - 2 * mm   # top of body columns
BODY_H   = BODY_Y - MARGIN_Y

# ── Style helper ───────────────────────────────────────────────────────────
def S(name, font="DV", size=7.5, leading=11, color=DARK, sb=0, sa=2, align=0):
    return ParagraphStyle(name, fontName=font, fontSize=size, leading=leading,
                          textColor=color, spaceBefore=sb, spaceAfter=sa, alignment=align)

# Section headers — spaced caps, grey, small
sSecHdr  = S("sSecHdr",  "DV",    6.5, 9,  LGREY,  sb=0, sa=2, align=0)
# Job title
sJobT    = S("sJobT",    "DV-B",  8,   11, BLACK,  sb=3, sa=0)
# Company
sJobC    = S("sJobC",    "DV-B",  7,   10, MID,    sb=0, sa=0)
# Date
sJobD    = S("sJobD",    "DV",    6.5, 9,  GREY,   sb=0, sa=2)
# Bullet
sBul     = S("sBul",     "DV",    6.8, 10.2, DARK, sb=0, sa=1.2)
# Left col label
sLabel   = S("sLabel",   "DV-B",  7,   10, BLACK,  sb=4, sa=1)
# Left col body
sLBody   = S("sLBody",   "DV",    7,   10.5, DARK, sb=0, sa=1.5)
# Skills — small
sSkill   = S("sSkill",   "DV",    7,   10, DARK,   sb=0, sa=2)
# Education
sEduT    = S("sEduT",    "DV-B",  7.5, 11, BLACK,  sb=4, sa=0)
sEduI    = S("sEduI",    "DV",    7,   10, MID,    sb=0, sa=0)
sEduD    = S("sEduD",    "DV",    6.5, 9,  GREY,   sb=0, sa=3)
# Name / title styles — drawn directly on canvas
# Cert
sCert    = S("sCert",    "DV",    6.5, 9.5, DARK,  sb=0, sa=2)
sCertB   = S("sCertB",   "DV-B",  6.5, 9.5, DARK,  sb=3, sa=0)

def rule(w, color=RULE, t=0.5, sa=3):
    return HRFlowable(width=w, color=color, thickness=t, spaceAfter=sa)

def sec(label):
    return [Paragraph(label, sSecHdr), rule(99999)]   # 99999 → fills frame width

# ── LEFT COLUMN ────────────────────────────────────────────────────────────
def left_col():
    s = []

    s += sec("C o n t a c t o")
    s += [Paragraph("romanripari@gmail.com", sLBody),
          Paragraph("linkedin.com/in/romanripari", sLBody),
          Paragraph("https://romanripari.ar", sLBody),
          Paragraph("Buenos Aires, Argentina", sLBody)]

    s += sec("H a b i l i d a d e s")

    # Skills in a 2-col table-like layout using tab spacing
    # We render each pair on one line separated by spaces, or stacked
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
        "Competitive Intel.",
        "Data Storytelling",
    ]
    for sk in skills:
        s.append(Paragraph(f"• {sk}", sSkill))

    s += sec("I d i o m a s")
    s += [Paragraph("Inglés — Avanzado", sLBody),
          Paragraph("Español — Nativo", sLBody)]

    s += sec("C e r t i f i c a c i o n e s")
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
    s += sec("E x p e r i e n c i a")

    # PGD ───────────────────────────────────────────────────────────────────
    s.append(Paragraph("Analista de Datos Senior", sJobT))
    s.append(Paragraph("Publicis Global Delivery (PGD)", sJobC))
    s.append(Paragraph("Jul. 2021 – Actualidad  ·  Estados Unidos", sJobD))
    for b in [
        "Liderazgo del análisis, producción y entrega de reportes de inteligencia competitiva (Competitive Intelligence) mensuales y ad-hoc para cuentas globales de primer nivel como The Coca-Cola Company (CPG / FMCG).",
        "Procesamiento y transformación de datasets de gran volumen (+100K registros) con métricas de ad spend, impresiones, rendimiento creativo y share of voice a nivel de marca, categoría y canal (video, social, OTT, display).",
        "Desarrollo de herramientas de automated reporting y data analysis en Excel (VBA / Macros), optimizando drásticamente los tiempos de procesamiento de equipos internacionales.",
        "Integración de herramientas de IA generativa y LLMs en flujos de trabajo de análisis para aumentar la velocidad de entrega y la calidad de los insights.",
        "Traducción de requerimientos comerciales (business requirements) de stakeholders internos en soluciones de datos accionables; soporte técnico continuo sobre herramientas implementadas.",
        "Gestión del ciclo de vida de proyectos de datos con Azure DevOps: planificación, sprint tracking, control de calidad y cumplimiento de plazos (deadline management).",
        "Performance Manager: mentoring y desarrollo profesional de miembros del equipo en habilidades técnicas, productividad y crecimiento de carrera.",
    ]:
        s.append(Paragraph(f"◦ {b}", sBul))

    # EY ────────────────────────────────────────────────────────────────────
    s.append(Paragraph("Analista Senior VBA + Alteryx", sJobT))
    s.append(Paragraph("EY Internacional", sJobC))
    s.append(Paragraph("Jun. 2019 – Jul. 2021", sJobD))
    for b in [
        "Líder de equipo de Business Intelligence (BI): gestión de personas, distribución de tareas y control de calidad de entregables.",
        "Desarrollo de dashboards interactivos y herramientas de automatización en Excel-VBA y Power BI para múltiples unidades de negocio.",
        "ETL y data wrangling: limpieza, transformación y combinación de datos de múltiples fuentes heterogéneas usando Alteryx.",
        "Análisis y reporting con datos estructurados de múltiples fuentes; creación y mantenimiento diario de bases de datos con SQL (SSMS).",
        "Gestión de proyectos de desarrollo desde la planificación hasta la ejecución con Azure DevOps.",
        "Capacitación (technical training) en Excel, VBA y Alteryx para equipos internos.",
    ]:
        s.append(Paragraph(f"◦ {b}", sBul))

    # IPG ───────────────────────────────────────────────────────────────────
    s.append(Paragraph("Analista de Proyectos de Datos", sJobT))
    s.append(Paragraph("IPG Mediabrands", sJobC))
    s.append(Paragraph("Sep. 2018 – Jun. 2019", sJobD))
    for b in [
        "Análisis multidimensional del negocio: ventas, brand equity, search interest, competitividad, visitas web, redes sociales y actividad publicitaria (advertising activity).",
        "Uso de herramientas de data visualization (Power BI) para actualizar dashboards y descubrir insights comerciales y de medios (media insights).",
        "Supervisión integral del proceso de datos y coordinación con stakeholders: clientes, agencias, equipos internos y proveedores.",
    ]:
        s.append(Paragraph(f"◦ {b}", sBul))

    # Nielsen ───────────────────────────────────────────────────────────────
    s.append(Paragraph("Senior Analyst", sJobT))
    s.append(Paragraph("Nielsen", sJobC))
    s.append(Paragraph("Dic. 2011 – Abr. 2018", sJobD))
    for b in [
        "Análisis de datos y Business Intelligence (BI) para clientes internos y externos en Argentina y Latinoamérica.",
        "Generación de reportes KPI para diferentes niveles de gestión; uso de software especializado para lectura y análisis de bases de datos.",
        "Clientes directos: Danone, The Coca-Cola Company, Unilever, PepsiCo, Clorox, Genomma, Procter & Gamble, Mead Johnson, Peñaflor, Mondelez, entre otros.",
        "Desarrollo de reportes personalizados (custom reporting) adaptados a las necesidades específicas de cada cliente.",
        "Tareas de reporting interno: consolidación de categorías (category management), creación de \"canastas\" para medir desempeño económico y generación de reportes para mercados específicos (ventas mayoristas).",
    ]:
        s.append(Paragraph(f"◦ {b}", sBul))

    return s

# ── RIGHT COLUMN — Education ───────────────────────────────────────────────
def right_col():
    s = []
    s += sec("E d u c a c i ó n")

    for title, inst, date in [
        ("Licenciatura en\nCiencias de Datos", "Universidad de\nBuenos Aires", "2020 – Actualidad"),
        ("Desarrollo de\naplicaciones Android", "Educación IT", "2018 – 2019"),
        ("Licenciatura\nen Letras", "Universidad de\nBuenos Aires", "2011 – 2014"),
        ("Licenciatura\nen Comercio", "Universidad Nacional\nde Quilmes", "2011 – 2014"),
    ]:
        s.append(Paragraph(title.replace("\n", "<br/>"), sEduT))
        s.append(Paragraph(inst.replace("\n", "<br/>"), sEduI))
        s.append(Paragraph(date, sEduD))

    return s

# ── BUILD PDF ──────────────────────────────────────────────────────────────
OUT = "/tmp/CV_RomanRipari_Final.pdf"
c = rl_canvas.Canvas(OUT, pagesize=A4)

# White background (default)
c.setFillColor(WHITE)
c.rect(0, 0, W, H, fill=1, stroke=0)

# ── Header block ───────────────────────────────────────────────────────────
# Name — large, centered
c.setFillColor(BLACK)
c.setFont("DV-B", 22)
name_y = H - MARGIN_Y - 10 * mm
c.drawCentredString(W / 2, name_y, "Román Ariel Ripari")

# Subtitle
c.setFont("DV", 10)
c.setFillColor(MID)
c.drawCentredString(W / 2, name_y - 7 * mm, "Analista de Datos  |  Data Analyst")

# Thin rule under header
c.setStrokeColor(RULE)
c.setLineWidth(0.5)
c.line(MARGIN_X, H - MARGIN_Y - HEADER_H, W - MARGIN_X, H - MARGIN_Y - HEADER_H)

# ── Three frames ───────────────────────────────────────────────────────────
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
