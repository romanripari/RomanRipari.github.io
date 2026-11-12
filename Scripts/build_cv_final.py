
# =============================================================================
# CV - Román Ariel Ripari (Español)
# Requiere: pip install reportlab pypdf
# Fuentes:  sudo apt install fonts-dejavu  (Linux)
#           En Windows/Mac: cambiar FONT_REGULAR y FONT_BOLD por las rutas locales
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
# CONFIGURACIÓN — editá estas variables para personalizar el CV
# =============================================================================

OUTPUT_FILE = "CV_RomanRipari_Esp.pdf"

FONT_REGULAR = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONT_BOLD    = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

# Colores
COLOR_BLACK       = colors.HexColor("#1a1a1a")   # nombre y títulos de puestos
COLOR_DARK        = colors.HexColor("#333333")   # texto principal
COLOR_MEDIUM      = colors.HexColor("#555555")   # empresa / subtítulo header
COLOR_GREY        = colors.HexColor("#888888")   # fechas
COLOR_LIGHT_GREY  = colors.HexColor("#bbbbbb")   # headers de sección
COLOR_RULE        = colors.HexColor("#cccccc")   # líneas separadoras
COLOR_WHITE       = colors.white

# Márgenes y columnas
MARGIN_LEFT_RIGHT = 11 * mm
MARGIN_TOP_BOTTOM = 8  * mm
PAGE_WIDTH, PAGE_HEIGHT = A4
USABLE_WIDTH = PAGE_WIDTH - 2 * MARGIN_LEFT_RIGHT

LEFT_COL_WIDTH   = 42 * mm   # columna izquierda: contacto / habilidades / certs
CENTER_COL_WIDTH = 93 * mm   # columna central: experiencia
RIGHT_COL_WIDTH  = USABLE_WIDTH - LEFT_COL_WIDTH - CENTER_COL_WIDTH - 6 * mm  # educación
COL_GAP          = 3 * mm    # separación entre columnas

LEFT_COL_X   = MARGIN_LEFT_RIGHT
CENTER_COL_X = LEFT_COL_X + LEFT_COL_WIDTH + COL_GAP
RIGHT_COL_X  = CENTER_COL_X + CENTER_COL_WIDTH + COL_GAP

HEADER_HEIGHT = 22 * mm
BODY_TOP_Y    = PAGE_HEIGHT - MARGIN_TOP_BOTTOM - HEADER_HEIGHT - 2 * mm
BODY_HEIGHT   = BODY_TOP_Y - MARGIN_TOP_BOTTOM

# =============================================================================
# REGISTRO DE FUENTES
# =============================================================================

pdfmetrics.registerFont(TTFont("Regular", FONT_REGULAR))
pdfmetrics.registerFont(TTFont("Bold",    FONT_BOLD))

# =============================================================================
# ESTILOS DE PÁRRAFO
# Helper: make_style(nombre, fuente, tamaño, interlineado, color, espacio_antes, espacio_despues, alineacion)
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

style_section_header  = make_style("section_header", "Regular", 6.5, 9,    COLOR_LIGHT_GREY, space_after=2)
style_job_title       = make_style("job_title",       "Bold",    8,   11,   COLOR_BLACK,      space_before=3)
style_company         = make_style("company",         "Bold",    7,   10,   COLOR_MEDIUM)
style_date            = make_style("date",            "Regular", 6.5, 9,    COLOR_GREY,       space_after=2)
style_bullet          = make_style("bullet",          "Regular", 6.8, 10.2, COLOR_DARK,       space_after=1.2)
style_left_body       = make_style("left_body",       "Regular", 7,   10.5, COLOR_DARK,       space_after=1.5)
style_skill           = make_style("skill",           "Regular", 7,   10,   COLOR_DARK,       space_after=2)
style_edu_title       = make_style("edu_title",       "Bold",    7.5, 11,   COLOR_BLACK,      space_before=4)
style_edu_institution = make_style("edu_institution", "Regular", 7,   10,   COLOR_MEDIUM)
style_edu_date        = make_style("edu_date",        "Regular", 6.5, 9,    COLOR_GREY,       space_after=3)
style_cert_regular    = make_style("cert_regular",    "Regular", 6.5, 9.5,  COLOR_DARK,       space_after=2)
style_cert_bold       = make_style("cert_bold",       "Bold",    6.5, 9.5,  COLOR_DARK,       space_before=3)

# =============================================================================
# FUNCIONES AUXILIARES
# =============================================================================

def horizontal_line(width=99999, color=COLOR_RULE, thickness=0.5, space_after=3):
    """Línea separadora horizontal."""
    return HRFlowable(width=width, color=color, thickness=thickness, spaceAfter=space_after)

def section_header(label):
    """Header de sección con línea debajo (ej: 'C o n t a c t o')."""
    return [Paragraph(label, style_section_header), horizontal_line()]

def render_column(canvas, x_position, width, content_list):
    """Renderiza una lista de flowables en una columna y devuelve el overflow."""
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
# COLUMNA IZQUIERDA — Contacto, Habilidades, Idiomas, Certificaciones
# =============================================================================

def build_left_column():
    content = []

    content += section_header("C o n t a c t o")
    content += [
        Paragraph("romanripari@gmail.com",        style_left_body),
        Paragraph("linkedin.com/in/romanripari",  style_left_body),
        Paragraph("https://romanripari.ar",       style_left_body),
        Paragraph("Buenos Aires, Argentina",      style_left_body),
    ]

    content += section_header("H a b i l i d a d e s")
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
    for skill in skills:
        content.append(Paragraph(f"• {skill}", style_skill))

    content += section_header("I d i o m a s")
    content += [
        Paragraph("Inglés — Avanzado", style_left_body),
        Paragraph("Español — Nativo",  style_left_body),
    ]

    content += section_header("C e r t i f i c a c i o n e s")
    content += [
        Paragraph("EF Standard English Test",    style_cert_regular),
        Paragraph("(EF SET)",                    style_cert_regular),
        Spacer(1, 2 * mm),
        Paragraph("[PCEP-30-02] PCEP –",         style_cert_bold),
        Paragraph("Certified Entry-Level",       style_cert_regular),
        Paragraph("Python Programmer",           style_cert_regular),
    ]

    return content

# =============================================================================
# COLUMNA CENTRAL — Experiencia
# =============================================================================

def build_center_column():
    content = []
    content += section_header("E x p e r i e n c i a")

    # ── PGD ──────────────────────────────────────────────────────────────────
    content.append(Paragraph("Analista de Datos Senior",           style_job_title))
    content.append(Paragraph("Publicis Global Delivery (PGD)",     style_company))
    content.append(Paragraph("Jul. 2021 – Actualidad  ·  Estados Unidos", style_date))
    pgd_bullets = [
        "Liderazgo del análisis, producción y entrega de reportes de inteligencia competitiva (Competitive Intelligence) mensuales y ad-hoc para cuentas globales de primer nivel como The Coca-Cola Company (CPG / FMCG).",
        "Procesamiento y transformación de datasets de gran volumen (+100K registros) con métricas de ad spend, impresiones, rendimiento creativo y share of voice a nivel de marca, categoría y canal (video, social, OTT, display).",
        "Desarrollo de herramientas de automated reporting y data analysis en Excel (VBA / Macros), optimizando drásticamente los tiempos de procesamiento de equipos internacionales.",
        "Integración de herramientas de IA generativa y LLMs en flujos de trabajo de análisis para aumentar la velocidad de entrega y la calidad de los insights.",
        "Traducción de requerimientos comerciales (business requirements) de stakeholders internos en soluciones de datos accionables; soporte técnico continuo sobre herramientas implementadas.",
        "Gestión del ciclo de vida de proyectos de datos con Azure DevOps: planificación, sprint tracking, control de calidad y cumplimiento de plazos (deadline management).",
        "Performance Manager: mentoring y desarrollo profesional de miembros del equipo en habilidades técnicas, productividad y crecimiento de carrera.",
    ]
    for bullet in pgd_bullets:
        content.append(Paragraph(f"◦ {bullet}", style_bullet))

    # ── EY ───────────────────────────────────────────────────────────────────
    content.append(Paragraph("Analista Senior VBA + Alteryx",   style_job_title))
    content.append(Paragraph("EY Internacional",                style_company))
    content.append(Paragraph("Jun. 2019 – Jul. 2021",           style_date))
    ey_bullets = [
        "Líder de equipo de Business Intelligence (BI): gestión de personas, distribución de tareas y control de calidad de entregables.",
        "Desarrollo de dashboards interactivos y herramientas de automatización en Excel-VBA y Power BI para múltiples unidades de negocio.",
        "ETL y data wrangling: limpieza, transformación y combinación de datos de múltiples fuentes heterogéneas usando Alteryx.",
        "Análisis y reporting con datos estructurados de múltiples fuentes; creación y mantenimiento diario de bases de datos con SQL (SSMS).",
        "Gestión de proyectos de desarrollo desde la planificación hasta la ejecución con Azure DevOps.",
        "Capacitación (technical training) en Excel, VBA y Alteryx para equipos internos.",
    ]
    for bullet in ey_bullets:
        content.append(Paragraph(f"◦ {bullet}", style_bullet))

    # ── IPG ──────────────────────────────────────────────────────────────────
    content.append(Paragraph("Analista de Proyectos de Datos",  style_job_title))
    content.append(Paragraph("IPG Mediabrands",                 style_company))
    content.append(Paragraph("Sep. 2018 – Jun. 2019",           style_date))
    ipg_bullets = [
        "Análisis multidimensional del negocio: ventas, brand equity, search interest, competitividad, visitas web, redes sociales y actividad publicitaria (advertising activity).",
        "Uso de herramientas de data visualization (Power BI) para actualizar dashboards y descubrir insights comerciales y de medios (media insights).",
        "Supervisión integral del proceso de datos y coordinación con stakeholders: clientes, agencias, equipos internos y proveedores.",
    ]
    for bullet in ipg_bullets:
        content.append(Paragraph(f"◦ {bullet}", style_bullet))

    # ── NIELSEN ──────────────────────────────────────────────────────────────
    content.append(Paragraph("Senior Analyst",       style_job_title))
    content.append(Paragraph("Nielsen",              style_company))
    content.append(Paragraph("Dic. 2011 – Abr. 2018", style_date))
    nielsen_bullets = [
        "Análisis de datos y Business Intelligence (BI) para clientes internos y externos en Argentina y Latinoamérica.",
        "Generación de reportes KPI para diferentes niveles de gestión; uso de software especializado para lectura y análisis de bases de datos.",
        "Clientes directos: Danone, The Coca-Cola Company, Unilever, PepsiCo, Clorox, Genomma, Procter & Gamble, Mead Johnson, Peñaflor, Mondelez, entre otros.",
        "Desarrollo de reportes personalizados (custom reporting) adaptados a las necesidades específicas de cada cliente.",
        "Tareas de reporting interno: consolidación de categorías (category management), creación de \"canastas\" para medir desempeño económico y generación de reportes para mercados específicos (ventas mayoristas).",
    ]
    for bullet in nielsen_bullets:
        content.append(Paragraph(f"◦ {bullet}", style_bullet))

    return content

# =============================================================================
# COLUMNA DERECHA — Educación
# =============================================================================

def build_right_column():
    content = []
    content += section_header("E d u c a c i ó n")

    education = [
        ("Licenciatura en\nCiencias de Datos",    "Universidad de\nBuenos Aires",        "2020 – Actualidad"),
        ("Desarrollo de\naplicaciones Android",   "Educación IT",                        "2018 – 2019"),
        ("Licenciatura\nen Letras",                "Universidad de\nBuenos Aires",        "2011 – 2014"),
        ("Licenciatura\nen Comercio",              "Universidad Nacional\nde Quilmes",    "2011 – 2014"),
    ]
    for degree_title, institution, years in education:
        content.append(Paragraph(degree_title.replace("\n", "<br/>"), style_edu_title))
        content.append(Paragraph(institution.replace("\n", "<br/>"), style_edu_institution))
        content.append(Paragraph(years, style_edu_date))

    return content

# =============================================================================
# CONSTRUCCIÓN DEL PDF
# =============================================================================

canvas = pdf_canvas.Canvas(OUTPUT_FILE, pagesize=A4)

# Fondo blanco
canvas.setFillColor(COLOR_WHITE)
canvas.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=1, stroke=0)

# ── Header: Nombre y subtítulo centrados ──────────────────────────────────
name_y = PAGE_HEIGHT - MARGIN_TOP_BOTTOM - 10 * mm

canvas.setFillColor(COLOR_BLACK)
canvas.setFont("Bold", 22)
canvas.drawCentredString(PAGE_WIDTH / 2, name_y, "Román Ariel Ripari")

canvas.setFont("Regular", 10)
canvas.setFillColor(COLOR_MEDIUM)
canvas.drawCentredString(PAGE_WIDTH / 2, name_y - 7 * mm, "Analista de Datos  |  Data Analyst")

# Línea bajo el header
canvas.setStrokeColor(COLOR_RULE)
canvas.setLineWidth(0.5)
canvas.line(MARGIN_LEFT_RIGHT, PAGE_HEIGHT - MARGIN_TOP_BOTTOM - HEADER_HEIGHT,
            PAGE_WIDTH - MARGIN_LEFT_RIGHT, PAGE_HEIGHT - MARGIN_TOP_BOTTOM - HEADER_HEIGHT)

# ── Renderizar las tres columnas ──────────────────────────────────────────
left_content   = build_left_column()
center_content = build_center_column()
right_content  = build_right_column()

left_overflow   = render_column(canvas, LEFT_COL_X,   LEFT_COL_WIDTH,   left_content)
center_overflow = render_column(canvas, CENTER_COL_X, CENTER_COL_WIDTH, center_content)
right_overflow  = render_column(canvas, RIGHT_COL_X,  RIGHT_COL_WIDTH,  right_content)

for col_name, overflow in [("Izquierda", left_overflow), ("Centro", center_overflow), ("Derecha", right_overflow)]:
    if overflow:
        print(f"⚠ Columna {col_name}: {len(overflow)} elementos no entraron", flush=True)
    else:
        print(f"✓ Columna {col_name}: OK", flush=True)

canvas.showPage()
canvas.save()
print(f"✓ PDF guardado: {OUTPUT_FILE}", flush=True)
