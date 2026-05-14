"""Build Praxia_Atelier_Servicios.pdf — editorial, accionable, casos protagonistas.

Usa reportlab. Salida: deploy_netlify/Praxia_Atelier_Servicios.pdf
También copia a /raíz/Praxia_Atelier_Servicios.pdf para tener fuente.
"""
from pathlib import Path
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor, white, black
from reportlab.pdfgen import canvas as canvas_module
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import simpleSplit
import os

# === Paleta Praxia ===
INK         = HexColor("#1a1f2e")
INK_SOFT    = HexColor("#44485a")
PAPER       = HexColor("#faf8f3")
LINE        = HexColor("#e6e1d6")
ACCENT      = HexColor("#b9522e")
ACCENT_SOFT = HexColor("#f3ddd0")
MOSS        = HexColor("#4a5d3a")
MOSS_SOFT   = HexColor("#d8dfcd")
GOLD        = HexColor("#b08d3a")
SLATE       = HexColor("#4b5d6e")
SLATE_SOFT  = HexColor("#d2dce4")

# === URLs ===
CAL_URL    = "https://cal.com/marta-escobar-rojas-teatxg/30min"
WEB_URL    = "https://praxia-atelier.net"
EMAIL      = "info@praxia-atelier.net"
EMAIL_HREF = f"mailto:{EMAIL}"

CASES_REAL = [
    {
        "tag": "Cliente real · 2025",
        "name": "Casavera",
        "tagline": "Inmobiliaria boutique · Madrid",
        "needed": "Dejar de gestionar alquileres, ventas e inversión con la operativa repartida en cuatro Excels y el correo.",
        "delivered": "Ecosistema digital con dos caras: web pública con 4 puertas + back office con vista panorámica de los 10 procesos del negocio.",
        "links": [
            ("Sistema operativo · back office (interno)",
             "https://resilient-arithmetic-182add.netlify.app/"),
            ("Web pública · 4 puertas de entrada (cliente)",
             "https://rococo-sawine-40e557.netlify.app/"),
        ],
        "color": ACCENT,
    },
]

CASES_DEMO = [
    {
        "name": "Bodega Valdescuro",
        "sector": "Family business · vino",
        "blurb": "Tres generaciones haciendo vino. La cuarta abre un club privado y vehículo de coinversión.",
        "url": f"{WEB_URL}/Praxia_Atelier_Caso_Bodega_Valdescuro.html",
        "color": HexColor("#6b1d23"),
    },
    {
        "name": "Clínica Lumen",
        "sector": "Health-tech · longevidad",
        "blurb": "Medicina integrativa de longevidad con membresía Plus, avatar Sofia y SaaS para practitioners.",
        "url": f"{WEB_URL}/Praxia_Atelier_Caso_Clinica_Lumen.html",
        "color": HexColor("#0e2a26"),
    },
    {
        "name": "Casa Vento",
        "sector": "Real estate · residencial",
        "blurb": "Operadora de pisos reformados con vehículo privado de coinversión y club de inquilinos.",
        "url": f"{WEB_URL}/Praxia_Atelier_Caso_Casa_Vento.html",
        "color": HexColor("#1a2733"),
    },
    {
        "name": "Mesa de Trabajo",
        "sector": "Founder-cliente · método aplicado",
        "blurb": "El método del estudio aplicado al propio estudio. 8 departamentos de Praxia diseñados con su misma lógica.",
        "url": f"{WEB_URL}/Praxia_Atelier_Caso_Mesa_de_Trabajo.html",
        "color": HexColor("#2a1f15"),
    },
]

CAPSULAS = [
    ("00", "Strategy Sprint",       "1 sem",        "990 – 2.500 €"),
    ("01", "Ecosystem Blueprint",   "10–15 días",   "12.000 – 18.000 €"),
    ("02", "Ecosystem Build",       "3–5 meses",    "60.000 – 120.000 €"),
    ("03", "Ecosystem Operate",     "recurrente",   "5.500 – 8.000 €/mes"),
    ("04/05/06", "Marketing · Ops · Comercial", "2–3 sem", "6.500 – 9.500 €"),
    ("PACK", "GTM (04+05+06 integradas)", "5 sem",  "18.000 € · ahorro 4.500 €"),
]

# === Page geometry ===
PAGE_W, PAGE_H = A4
MARGIN_X = 18 * mm
MARGIN_Y = 18 * mm

# === Fuentes (intentamos fuentes reales si están disponibles, sino fallback) ===
HAS_FRAUNCES = False
HAS_PLEX = False
HAS_MONO = False
font_dirs = ["/System/Library/Fonts", "/Library/Fonts", "/System/Library/Fonts/Supplemental"]
def try_register(name, file_candidates):
    for d in font_dirs:
        for f in file_candidates:
            p = os.path.join(d, f)
            if os.path.exists(p):
                try:
                    pdfmetrics.registerFont(TTFont(name, p))
                    return True
                except Exception:
                    continue
    return False

# Mac-friendly fallbacks
if try_register("Editorial", ["Georgia.ttf", "Times.ttc", "Times New Roman.ttf"]): HAS_FRAUNCES = True
if try_register("Sans",      ["Helvetica.ttc", "Arial.ttf", "HelveticaNeue.ttc"]): HAS_PLEX = True
if try_register("Mono",      ["Menlo.ttc", "Courier New.ttf", "Courier.ttc"]):    HAS_MONO = True

FONT_SERIF = "Editorial" if HAS_FRAUNCES else "Times-Bold"
FONT_SERIF_REG = "Editorial" if HAS_FRAUNCES else "Times-Roman"
FONT_SANS = "Sans" if HAS_PLEX else "Helvetica"
FONT_SANS_BOLD = "Sans" if HAS_PLEX else "Helvetica-Bold"
FONT_MONO = "Mono" if HAS_MONO else "Courier"


def draw_text_block(c, text, x, y, w, font, size, color, leading=None, max_lines=None):
    """Draws wrapped text and returns the y position after the block."""
    if leading is None: leading = size * 1.35
    c.setFillColor(color)
    c.setFont(font, size)
    lines = simpleSplit(text, font, size, w)
    if max_lines:
        lines = lines[:max_lines]
    cur_y = y
    for line in lines:
        c.drawString(x, cur_y, line)
        cur_y -= leading
    return cur_y


def draw_link_button(c, label, url, x, y, w, h, fill_color=None, text_color=None, border_color=None, font_size=10):
    """Draws a clickable button with a label and registers a link annotation."""
    if fill_color is not None:
        c.setFillColor(fill_color)
        c.rect(x, y, w, h, stroke=0, fill=1)
    if border_color is not None:
        c.setStrokeColor(border_color)
        c.setLineWidth(0.6)
        c.rect(x, y, w, h, stroke=1, fill=0)
    c.setFillColor(text_color or white)
    c.setFont(FONT_SANS_BOLD, font_size)
    # center vertically by font ascender approximation
    text_y = y + (h - font_size) / 2 + 1
    text_w = c.stringWidth(label, FONT_SANS_BOLD, font_size)
    c.drawString(x + (w - text_w) / 2, text_y, label)
    # link annotation
    c.linkURL(url, (x, y, x + w, y + h), relative=0, thickness=0)


def draw_text_link(c, label, url, x, y, font, size, color):
    """Draws underlined link text and registers the link annotation."""
    c.setFillColor(color)
    c.setFont(font, size)
    c.drawString(x, y, label)
    text_w = c.stringWidth(label, font, size)
    # underline
    c.setStrokeColor(color)
    c.setLineWidth(0.5)
    c.line(x, y - 1.5, x + text_w, y - 1.5)
    c.linkURL(url, (x, y - 2, x + text_w, y + size), relative=0, thickness=0)
    return text_w


def header(c, page_num, total_pages):
    """Top header on every page: brand + page indicator."""
    # background paper color
    c.setFillColor(PAPER)
    c.rect(0, 0, PAGE_W, PAGE_H, stroke=0, fill=1)

    # Brand top-left
    c.setStrokeColor(INK)
    c.setLineWidth(0.7)
    mark_size = 9 * mm
    c.rect(MARGIN_X, PAGE_H - MARGIN_Y - mark_size, mark_size, mark_size, stroke=1, fill=0)
    c.setFillColor(INK)
    c.setFont(FONT_SERIF, 16)
    c.drawString(MARGIN_X + 2.4*mm, PAGE_H - MARGIN_Y - mark_size + 2.3*mm, "P")

    c.setFont(FONT_SERIF, 13)
    c.drawString(MARGIN_X + mark_size + 3*mm, PAGE_H - MARGIN_Y - 4*mm, "Praxia Atelier")
    c.setFont(FONT_MONO, 7)
    c.setFillColor(INK_SOFT)
    c.drawString(MARGIN_X + mark_size + 3*mm, PAGE_H - MARGIN_Y - 7*mm, "ECOSYSTEM ARCHITECTURE")

    # Page number top-right
    c.setFont(FONT_MONO, 8)
    c.setFillColor(INK_SOFT)
    label = f"{page_num:02d} / {total_pages:02d}"
    tw = c.stringWidth(label, FONT_MONO, 8)
    c.drawString(PAGE_W - MARGIN_X - tw, PAGE_H - MARGIN_Y - 4*mm, label)

    # Hairline separator
    c.setStrokeColor(LINE)
    c.setLineWidth(0.5)
    c.line(MARGIN_X, PAGE_H - MARGIN_Y - 11*mm, PAGE_W - MARGIN_X, PAGE_H - MARGIN_Y - 11*mm)


def footer(c):
    """Footer on every page: web + email links."""
    y = MARGIN_Y - 4*mm
    c.setStrokeColor(LINE)
    c.setLineWidth(0.5)
    c.line(MARGIN_X, MARGIN_Y, PAGE_W - MARGIN_X, MARGIN_Y)

    c.setFont(FONT_MONO, 8)
    c.setFillColor(INK_SOFT)
    c.drawString(MARGIN_X, y, "ESTUDIO · MADRID · 2026")

    # Web link (centered-ish)
    web_label = WEB_URL.replace("https://", "").upper()
    web_w = c.stringWidth(web_label, FONT_MONO, 8)
    web_x = (PAGE_W - web_w) / 2
    c.setFillColor(INK)
    c.drawString(web_x, y, web_label)
    c.linkURL(WEB_URL, (web_x, y - 1, web_x + web_w, y + 8), relative=0, thickness=0)

    # Email link right
    em_label = EMAIL.upper()
    em_w = c.stringWidth(em_label, FONT_MONO, 8)
    em_x = PAGE_W - MARGIN_X - em_w
    c.drawString(em_x, y, em_label)
    c.linkURL(EMAIL_HREF, (em_x, y - 1, em_x + em_w, y + 8), relative=0, thickness=0)


# ============================================================
# PDF generation
# ============================================================
def build(out_path):
    c = canvas_module.Canvas(out_path, pagesize=A4)
    c.setTitle("Praxia Atelier · Servicios")
    c.setAuthor("Marta Escobar Rojas")
    c.setSubject("Estudio de arquitectura de ecosistemas digitales · Servicios y casos")
    c.setCreator("Praxia Atelier")

    TOTAL_PAGES = 4

    # ============================================================
    # PÁGINA 1 · MANIFIESTO + PROPUESTA
    # ============================================================
    header(c, 1, TOTAL_PAGES)

    y = PAGE_H - MARGIN_Y - 22*mm
    content_w = PAGE_W - 2*MARGIN_X

    # Pill
    c.setFillColor(ACCENT_SOFT)
    pill_label = "ESTUDIO · MADRID · 2026"
    pill_w = c.stringWidth(pill_label, FONT_MONO, 8) + 6*mm
    c.roundRect(MARGIN_X, y, pill_w, 6*mm, 3*mm, stroke=0, fill=1)
    c.setFillColor(ACCENT)
    c.setFont(FONT_MONO, 8)
    c.drawString(MARGIN_X + 3*mm, y + 1.8*mm, pill_label)
    y -= 12*mm

    # Big H1 (line by line for control)
    c.setFillColor(INK)
    c.setFont(FONT_SERIF, 28)
    c.drawString(MARGIN_X, y, "Diseñamos ecosistemas digitales")
    y -= 11*mm
    c.setFillColor(ACCENT)
    c.drawString(MARGIN_X, y, "listos para captar capital")
    c.setFillColor(INK)
    suffix = "  o multiplicar el ROI."
    base_w = c.stringWidth("listos para captar capital", FONT_SERIF, 28)
    c.drawString(MARGIN_X + base_w, y, suffix)
    y -= 14*mm

    # Body
    body = ("Si sólo tienes la idea, empezamos por ahí. Si ya tienes empresa, te diseñamos "
            "la capa siguiente. Estructura jurídico-fiscal, software, avatar con IA, modelo "
            "económico y materiales para inversores — un único estudio, una única voz.")
    y = draw_text_block(c, body, MARGIN_X, y, content_w, FONT_SANS, 11, INK_SOFT, leading=15)
    y -= 6*mm

    # Botón principal · Reservar
    btn_w = 65*mm
    btn_h = 11*mm
    draw_link_button(c, "Reservar 30 min con Marta · gratis", CAL_URL,
                     MARGIN_X, y - btn_h, btn_w, btn_h,
                     fill_color=INK, text_color=PAPER, font_size=11)
    # Botón secundario · Ver casos
    draw_link_button(c, "Ver casos navegables", f"{WEB_URL}/#casos",
                     MARGIN_X + btn_w + 4*mm, y - btn_h, 45*mm, btn_h,
                     fill_color=None, text_color=INK, border_color=INK, font_size=10)
    y -= btn_h + 3*mm
    c.setFont(FONT_MONO, 8)
    c.setFillColor(INK_SOFT)
    c.drawString(MARGIN_X, y, "· SIN COSTE · SIN COMPROMISO ·")
    y -= 14*mm

    # Promesa one-pager (left bar)
    c.setFillColor(ACCENT)
    c.rect(MARGIN_X, y - 22*mm, 0.8*mm, 22*mm, stroke=0, fill=1)
    promesa = ("Reserva 30 min y en las 48 h siguientes recibes un one-pager gratis con "
               "tres movimientos accionables específicos para tu proyecto. Sin contratar "
               "nada — el valor es tuyo aunque no sigamos juntos.")
    draw_text_block(c, promesa, MARGIN_X + 4*mm, y - 4*mm, content_w - 4*mm, FONT_SANS, 10, INK, leading=14)
    y -= 30*mm

    # Stat band
    stats = [("10–15", "DÍAS PARA EL BLUEPRINT"),
             ("7", "ENTIDADES COORDINADAS"),
             ("8", "DISCIPLINAS · UNA VOZ"),
             ("100%", "PROTOTIPO NAVEGABLE")]
    cell_w = content_w / 4
    for i, (big, small) in enumerate(stats):
        cx = MARGIN_X + i * cell_w
        c.setFillColor(INK)
        c.setFont(FONT_SERIF, 22)
        c.drawString(cx, y - 8*mm, big)
        c.setFont(FONT_MONO, 6.5)
        c.setFillColor(INK_SOFT)
        c.drawString(cx, y - 13*mm, small)
        if i < 3:
            c.setStrokeColor(LINE)
            c.setLineWidth(0.5)
            c.line(cx + cell_w - 2*mm, y - 14*mm, cx + cell_w - 2*mm, y)
    y -= 22*mm

    # Cómo es el proceso
    c.setFont(FONT_MONO, 8)
    c.setFillColor(ACCENT)
    c.drawString(MARGIN_X, y, "CÓMO ES EL PROCESO")
    y -= 6*mm
    c.setFont(FONT_SERIF, 16)
    c.setFillColor(INK)
    c.drawString(MARGIN_X, y, "Mismo método, dos puntos de entrada.")
    y -= 8*mm

    process = [("Día 0", "Brainstorm para entender tu negocio."),
               ("Día 1", "Te proponemos opciones."),
               ("Día 2–10", "Diseñamos el ecosistema."),
               ("Día 15", "Sales con los planos listos.")]
    pcell_w = content_w / 4
    for i, (when, what) in enumerate(process):
        cx = MARGIN_X + i * pcell_w
        c.setFont(FONT_MONO, 7)
        c.setFillColor(ACCENT)
        c.drawString(cx, y - 5*mm, when.upper())
        c.setFont(FONT_SERIF, 11)
        c.setFillColor(INK)
        # wrap
        for j, line in enumerate(simpleSplit(what, FONT_SERIF, 11, pcell_w - 3*mm)):
            c.drawString(cx, y - 10*mm - j * 4*mm, line)

    footer(c)
    c.showPage()

    # ============================================================
    # PÁGINA 2 · CASOS · PROYECTO REAL DESTACADO
    # ============================================================
    header(c, 2, TOTAL_PAGES)
    y = PAGE_H - MARGIN_Y - 22*mm

    c.setFont(FONT_MONO, 8)
    c.setFillColor(ACCENT)
    c.drawString(MARGIN_X, y, "CASOS · BLOQUE 1 · TRAYECTORIA")
    y -= 7*mm
    c.setFont(FONT_SERIF, 22)
    c.setFillColor(INK)
    c.drawString(MARGIN_X, y, "Proyectos reales con clientes reales.")
    y -= 8*mm
    intro = ("Praxia Atelier abre en 2026, pero el método se ha construido diseñando y operando "
             "proyectos reales. Los que tienen prototipo público están enteramente navegables.")
    y = draw_text_block(c, intro, MARGIN_X, y, content_w, FONT_SANS, 10, INK_SOFT, leading=14)
    y -= 5*mm

    # Casavera · destacado (caja con borde acento grueso)
    box_h = 110*mm
    box_y = y - box_h
    # banner top
    c.setFillColor(ACCENT)
    c.rect(MARGIN_X, y - 6*mm, content_w, 6*mm, stroke=0, fill=1)
    c.setFillColor(white)
    c.setFont(FONT_MONO, 7.5)
    c.drawString(MARGIN_X + 3*mm, y - 4.4*mm, "DESTACADO · PROYECTO REAL · 2025")
    # box
    c.setFillColor(white)
    c.rect(MARGIN_X, box_y, content_w, box_h - 6*mm, stroke=0, fill=1)
    c.setStrokeColor(LINE)
    c.setLineWidth(0.5)
    c.rect(MARGIN_X, box_y, content_w, box_h - 6*mm, stroke=1, fill=0)

    inner_x = MARGIN_X + 6*mm
    inner_y = y - 12*mm
    inner_w = content_w - 12*mm

    case = CASES_REAL[0]
    c.setFont(FONT_MONO, 7)
    c.setFillColor(INK_SOFT)
    c.drawString(inner_x, inner_y, case["tagline"].upper())
    inner_y -= 7*mm

    c.setFont(FONT_SERIF, 19)
    c.setFillColor(INK)
    c.drawString(inner_x, inner_y, case["name"])
    c.setFont(FONT_SERIF, 19)
    c.setFillColor(INK_SOFT)
    name_w = c.stringWidth(case["name"], FONT_SERIF, 19)
    c.drawString(inner_x + name_w + 3*mm, inner_y, "· inmobiliaria boutique")
    inner_y -= 9*mm

    # Lo que necesitaba
    c.setFont(FONT_MONO, 7)
    c.setFillColor(ACCENT)
    c.drawString(inner_x, inner_y, "LO QUE NECESITABA CASAVERA")
    inner_y -= 5*mm
    inner_y = draw_text_block(c, case["needed"], inner_x, inner_y, inner_w, FONT_SANS, 10, INK, leading=14)
    inner_y -= 4*mm

    # Lo que entregó Praxia
    c.setFont(FONT_MONO, 7)
    c.setFillColor(ACCENT)
    c.drawString(inner_x, inner_y, "LO QUE ENTREGÓ PRAXIA")
    inner_y -= 5*mm
    inner_y = draw_text_block(c, case["delivered"], inner_x, inner_y, inner_w, FONT_SANS, 10, INK, leading=14)
    inner_y -= 6*mm

    # Dos botones de prototipo
    c.setFont(FONT_MONO, 7)
    c.setFillColor(INK_SOFT)
    c.drawString(inner_x, inner_y, "DOS PROTOTIPOS NAVEGABLES")
    inner_y -= 6*mm
    btn_h = 9*mm
    btn_w = (inner_w - 4*mm) / 2
    for i, (label, url) in enumerate(case["links"]):
        bx = inner_x + i * (btn_w + 4*mm)
        draw_link_button(c, label, url, bx, inner_y - btn_h, btn_w, btn_h,
                         fill_color=INK, text_color=PAPER, font_size=8.5)
        # add small "→" arrow on right side
    inner_y -= btn_h + 4*mm
    c.setFont(FONT_MONO, 6.5)
    c.setFillColor(ACCENT)
    c.drawString(inner_x, inner_y, "CAPAS · PRODUCTO + IA + MODELO + MARKETING + OPERACIONES + COMERCIAL")

    y = box_y - 8*mm

    # Otros proyectos sin prototipo público
    c.setFont(FONT_MONO, 7.5)
    c.setFillColor(INK_SOFT)
    c.drawString(MARGIN_X, y, "OTROS PROYECTOS · SIN PROTOTIPO PÚBLICO")
    y -= 6*mm

    others = [
        ("EdTech · educación emocional", "Ecosistema de AIE con plataforma de educación emocional · 8 capas · diseño y aterrizaje"),
        ("Proyecto propio · activo",     "Ecosistema emocional propio con IA en producción · 3 líneas (B2C / marketplace / enterprise)"),
    ]
    for title, desc in others:
        c.setFont(FONT_SANS_BOLD, 9)
        c.setFillColor(INK)
        c.drawString(MARGIN_X, y, title)
        y -= 4.5*mm
        y = draw_text_block(c, desc, MARGIN_X, y, content_w, FONT_SANS, 9, INK_SOFT, leading=13, max_lines=2)
        y -= 2*mm

    footer(c)
    c.showPage()

    # ============================================================
    # PÁGINA 3 · PROTOTIPOS FICTICIOS NAVEGABLES
    # ============================================================
    header(c, 3, TOTAL_PAGES)
    y = PAGE_H - MARGIN_Y - 22*mm

    c.setFont(FONT_MONO, 8)
    c.setFillColor(ACCENT)
    c.drawString(MARGIN_X, y, "CASOS · BLOQUE 2 · PARA ENTENDER EL MÉTODO")
    y -= 7*mm
    c.setFont(FONT_SERIF, 22)
    c.setFillColor(INK)
    c.drawString(MARGIN_X, y, "Prototipos ficticios navegables.")
    y -= 8*mm
    intro = ("Construidos con el mismo rigor que un encargo real. Web, back office, simulador "
             "interactivo y modelo económico — todo tocable. Cuando trabajamos contigo, esto "
             "se construye con tu marca, tus números y tus protocolos.")
    y = draw_text_block(c, intro, MARGIN_X, y, content_w, FONT_SANS, 10, INK_SOFT, leading=14)
    y -= 6*mm

    # 4 casos en 2x2
    case_w = (content_w - 6*mm) / 2
    case_h = 60*mm
    for i, dc in enumerate(CASES_DEMO):
        col = i % 2
        row = i // 2
        cx = MARGIN_X + col * (case_w + 6*mm)
        cy = y - row * (case_h + 6*mm) - case_h
        # color band on top
        c.setFillColor(dc["color"])
        c.rect(cx, cy + case_h - 14*mm, case_w, 14*mm, stroke=0, fill=1)
        # text on band
        c.setFillColor(white)
        c.setFont(FONT_MONO, 6.5)
        c.drawString(cx + 4*mm, cy + case_h - 5*mm, dc["sector"].upper())
        c.setFont(FONT_SERIF, 14)
        c.drawString(cx + 4*mm, cy + case_h - 11*mm, dc["name"])
        # white body
        c.setFillColor(white)
        c.rect(cx, cy, case_w, case_h - 14*mm, stroke=0, fill=1)
        c.setStrokeColor(LINE)
        c.setLineWidth(0.5)
        c.rect(cx, cy, case_w, case_h, stroke=1, fill=0)
        # blurb
        draw_text_block(c, dc["blurb"], cx + 4*mm, cy + case_h - 19*mm, case_w - 8*mm,
                        FONT_SANS, 9, INK_SOFT, leading=12, max_lines=4)
        # link button at bottom
        draw_link_button(c, "Abrir caso navegable →", dc["url"],
                         cx + 4*mm, cy + 4*mm, case_w - 8*mm, 7*mm,
                         fill_color=None, text_color=ACCENT, border_color=ACCENT, font_size=8.5)

    y -= 2 * (case_h + 6*mm) + 6*mm

    # Note
    note = ("Estos cuatro casos son ficticios. Sirven para que veas exactamente cómo se ve el "
            "entregable de Praxia: estructura jurídica, software, mockups navegables, modelo "
            "económico y simulador interactivo — antes de contratar nada.")
    y = draw_text_block(c, note, MARGIN_X, y, content_w, FONT_SANS, 9, INK_SOFT, leading=13)

    footer(c)
    c.showPage()

    # ============================================================
    # PÁGINA 4 · CÁPSULAS + BIO + CTA
    # ============================================================
    header(c, 4, TOTAL_PAGES)
    y = PAGE_H - MARGIN_Y - 22*mm

    c.setFont(FONT_MONO, 8)
    c.setFillColor(ACCENT)
    c.drawString(MARGIN_X, y, "QUÉ CONSTRUIMOS · TECNOLOGÍA HECHA A MEDIDA")
    y -= 7*mm
    c.setFont(FONT_SERIF, 22)
    c.setFillColor(INK)
    c.drawString(MARGIN_X, y, "Siete cápsulas. Precio cerrado.")
    y -= 8*mm
    intro = ("No vendemos horas. Cada cápsula tiene alcance, plazo y entregables fijos. "
             "Si no encajan, no hay propuesta.")
    y = draw_text_block(c, intro, MARGIN_X, y, content_w, FONT_SANS, 10, INK_SOFT, leading=14)
    y -= 4*mm

    # Tabla de cápsulas (filas)
    row_h = 12*mm
    for num, name, when, price in CAPSULAS:
        # Fondo alternado
        if num == "PACK":
            c.setFillColor(ACCENT_SOFT)
            c.rect(MARGIN_X, y - row_h, content_w, row_h, stroke=0, fill=1)
        else:
            c.setStrokeColor(LINE)
            c.setLineWidth(0.5)
            c.line(MARGIN_X, y, PAGE_W - MARGIN_X, y)
        # Numero
        c.setFont(FONT_MONO, 9)
        c.setFillColor(ACCENT)
        c.drawString(MARGIN_X + 2*mm, y - 7*mm, num)
        # Nombre
        c.setFont(FONT_SERIF, 12)
        c.setFillColor(INK)
        c.drawString(MARGIN_X + 22*mm, y - 7*mm, name)
        # Plazo
        c.setFont(FONT_MONO, 8)
        c.setFillColor(INK_SOFT)
        c.drawString(MARGIN_X + 95*mm, y - 7*mm, when.upper())
        # Precio (right align)
        c.setFont(FONT_SANS_BOLD, 10)
        c.setFillColor(INK)
        pw = c.stringWidth(price, FONT_SANS_BOLD, 10)
        c.drawString(PAGE_W - MARGIN_X - pw - 2*mm, y - 7*mm, price)
        y -= row_h
    # Línea final
    c.setStrokeColor(LINE)
    c.line(MARGIN_X, y, PAGE_W - MARGIN_X, y)
    y -= 12*mm

    # Truco honesto
    c.setFillColor(ACCENT)
    c.rect(MARGIN_X, y - 16*mm, 0.8*mm, 16*mm, stroke=0, fill=1)
    c.setFont(FONT_MONO, 7)
    c.setFillColor(ACCENT)
    c.drawString(MARGIN_X + 4*mm, y - 4*mm, "TRUCO HONESTO")
    truco = ("Si después del Sprint contratas la Cápsula 01 en los siguientes 30 días, los "
             "honorarios del sprint se descuentan íntegramente de la factura del Blueprint. "
             "En la práctica, el sprint sale gratis si avanzamos.")
    draw_text_block(c, truco, MARGIN_X + 4*mm, y - 9*mm, content_w - 4*mm, FONT_SANS, 9, INK, leading=13)
    y -= 24*mm

    # Bio + CTA
    c.setFont(FONT_MONO, 7.5)
    c.setFillColor(INK_SOFT)
    c.drawString(MARGIN_X, y, "FUNDADORA")
    y -= 5*mm
    c.setFont(FONT_SERIF, 18)
    c.setFillColor(INK)
    c.drawString(MARGIN_X, y, "Marta Escobar Rojas")
    y -= 6*mm
    c.setFont(FONT_SANS, 9.5)
    c.setFillColor(INK_SOFT)
    c.drawString(MARGIN_X, y, "MBA · Founder con IA en producción · Madrid")
    y -= 14*mm

    # Call to action box
    c.setFillColor(INK)
    c.rect(MARGIN_X, y - 28*mm, content_w, 28*mm, stroke=0, fill=1)
    c.setFillColor(PAPER)
    c.setFont(FONT_SERIF, 16)
    c.drawString(MARGIN_X + 6*mm, y - 9*mm, "Reserva 30 minutos sin compromiso.")
    c.setFont(FONT_SANS, 9.5)
    c.drawString(MARGIN_X + 6*mm, y - 14*mm, "Una conversación clara — no una llamada de venta.")
    # Botón terracota
    btn_w = 60*mm
    btn_h = 10*mm
    draw_link_button(c, "Reservar diagnóstico · 30 min", CAL_URL,
                     MARGIN_X + 6*mm, y - 25*mm, btn_w, btn_h,
                     fill_color=ACCENT, text_color=white, font_size=10)
    # Email link
    c.setFillColor(PAPER)
    c.setFont(FONT_MONO, 8)
    c.drawString(MARGIN_X + 6*mm + btn_w + 6*mm, y - 22*mm, "O ESCRIBE A:")
    em_x = MARGIN_X + 6*mm + btn_w + 6*mm
    em_y = y - 25.5*mm
    c.setFont(FONT_SANS_BOLD, 9.5)
    c.drawString(em_x, em_y, EMAIL)
    em_w = c.stringWidth(EMAIL, FONT_SANS_BOLD, 9.5)
    c.linkURL(EMAIL_HREF, (em_x, em_y - 1, em_x + em_w, em_y + 9), relative=0, thickness=0)

    footer(c)
    c.showPage()

    c.save()
    print(f"PDF generated: {out_path}")


if __name__ == "__main__":
    out_root = Path("Praxia_Atelier_Servicios.pdf")
    out_deploy = Path("deploy_netlify/Praxia_Atelier_Servicios.pdf")
    build(str(out_root))
    # copy to deploy
    import shutil
    shutil.copy(out_root, out_deploy)
    print(f"Copied to {out_deploy}")
