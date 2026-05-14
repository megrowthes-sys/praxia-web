"""Build Praxia_Atelier_Servicios.pdf (and .en) — EDITORIAL PREMIUM v2.

Diseño editorial estilo revista:
- Tipografía Fraunces (serif editorial) + IBM Plex Sans + IBM Plex Mono.
- Márgenes generosos (28mm), aire abundante, blanco generoso.
- Números editoriales gigantes (200pt) en marca de página estilo índice.
- Pull quotes en serif italic.
- Casavera ocupa una página entera con jerarquía clara.
- Reglas finas como elemento decorativo, no cajas pesadas.

Generates:
  - Praxia_Atelier_Servicios.pdf  (ES)
  - Praxia_Atelier_Services.pdf   (EN)
"""
from pathlib import Path
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor, white, Color
from reportlab.pdfgen import canvas as canvas_module
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import simpleSplit

# ---------- Palette ----------
INK         = HexColor("#1a1f2e")
INK_SOFT    = HexColor("#44485a")
INK_FAINT   = HexColor("#8b8e98")
PAPER       = HexColor("#faf8f3")
PAPER_DEEP  = HexColor("#f3f0e6")
LINE        = HexColor("#e6e1d6")
LINE_STRONG = HexColor("#c5beae")
ACCENT      = HexColor("#b9522e")
ACCENT_SOFT = HexColor("#f3ddd0")
ACCENT_DEEP = HexColor("#8a3d22")
MOSS        = HexColor("#4a5d3a")
GOLD        = HexColor("#b08d3a")
SLATE       = HexColor("#4b5d6e")

# ---------- URLs ----------
CAL_URL = "https://cal.com/marta-escobar-rojas-teatxg/30min"
WEB_URL = "https://praxia-atelier.net"
EMAIL = "info@praxia-atelier.net"
EMAIL_HREF = f"mailto:{EMAIL}"

# ---------- Fonts ----------
FONT_DIR = Path("_fonts")
def register_fonts():
    fonts = [
        ("Fraunces",        FONT_DIR/"Fraunces-400.ttf"),
        ("Fraunces-Bold",   FONT_DIR/"Fraunces-600.ttf"),
        ("Plex",            FONT_DIR/"Plex-400.ttf"),
        ("Plex-Med",        FONT_DIR/"Plex-500.ttf"),
        ("PlexMono",        FONT_DIR/"PlexMono-400.ttf"),
    ]
    for name, path in fonts:
        if path.exists():
            try:
                pdfmetrics.registerFont(TTFont(name, str(path)))
            except Exception as e:
                print(f"WARN registering {name}: {e}")
register_fonts()

# Use names directly (with fallback)
F_SERIF      = "Fraunces"
F_SERIF_BOLD = "Fraunces-Bold"
F_SANS       = "Plex"
F_SANS_MED   = "Plex-Med"
F_MONO       = "PlexMono"

# ---------- Page geometry ----------
PAGE_W, PAGE_H = A4              # 210mm x 297mm
MARGIN_X       = 22 * mm          # generous
MARGIN_TOP     = 22 * mm
MARGIN_BOT     = 22 * mm
CONTENT_W      = PAGE_W - 2 * MARGIN_X


# ============================================================
# Drawing helpers
# ============================================================
def text_lines(c, text, font, size, w, leading=None, max_lines=None):
    if leading is None: leading = size * 1.42
    lines = simpleSplit(text, font, size, w)
    if max_lines: lines = lines[:max_lines]
    return lines, leading


def draw_text(c, text, x, y, w, font, size, color, leading=None, max_lines=None, indent=0):
    """Draw wrapped text. Returns Y after the last line."""
    lines, leading = text_lines(c, text, font, size, w, leading, max_lines)
    c.setFillColor(color)
    c.setFont(font, size)
    for i, line in enumerate(lines):
        c.drawString(x + (indent if i > 0 else 0), y, line)
        y -= leading
    return y


def draw_link_button(c, label, url, x, y, w, h,
                     fill=None, text=None, border=None, font_size=10,
                     font=None, radius=0):
    if font is None: font = F_SANS_MED
    if fill is not None:
        c.setFillColor(fill)
        if radius > 0:
            c.roundRect(x, y, w, h, radius, stroke=0, fill=1)
        else:
            c.rect(x, y, w, h, stroke=0, fill=1)
    if border is not None:
        c.setStrokeColor(border)
        c.setLineWidth(0.7)
        if radius > 0:
            c.roundRect(x, y, w, h, radius, stroke=1, fill=0)
        else:
            c.rect(x, y, w, h, stroke=1, fill=0)
    c.setFillColor(text or white)
    c.setFont(font, font_size)
    text_y = y + (h - font_size * 0.7) / 2
    text_w = c.stringWidth(label, font, font_size)
    c.drawString(x + (w - text_w) / 2, text_y, label)
    c.linkURL(url, (x, y, x + w, y + h), relative=0, thickness=0)


def hr(c, x1, y, x2, color=LINE, width=0.5):
    c.setStrokeColor(color); c.setLineWidth(width)
    c.line(x1, y, x2, y)


def header_band(c, page_num, total_pages):
    """Top band with brand left + page indicator right + hairline below."""
    # Background
    c.setFillColor(PAPER)
    c.rect(0, 0, PAGE_W, PAGE_H, stroke=0, fill=1)

    # Brand
    mark_size = 9 * mm
    by = PAGE_H - MARGIN_TOP - mark_size
    c.setStrokeColor(INK); c.setLineWidth(0.8)
    c.rect(MARGIN_X, by, mark_size, mark_size, stroke=1, fill=0)
    c.setFillColor(INK)
    c.setFont(F_SERIF_BOLD, 14.5)
    c.drawString(MARGIN_X + 2.6 * mm, by + 2.3 * mm, "P")

    c.setFont(F_SERIF, 12)
    c.drawString(MARGIN_X + mark_size + 3 * mm, PAGE_H - MARGIN_TOP - 3.6 * mm, "Praxia Atelier")
    c.setFont(F_MONO, 6.5)
    c.setFillColor(INK_FAINT)
    c.drawString(MARGIN_X + mark_size + 3 * mm, PAGE_H - MARGIN_TOP - 7 * mm, "ECOSYSTEM ARCHITECTURE")

    # Page indicator (large, editorial style)
    c.setFont(F_MONO, 8)
    c.setFillColor(INK_FAINT)
    label = f"{page_num:02d}/{total_pages:02d}"
    tw = c.stringWidth(label, F_MONO, 8)
    c.drawString(PAGE_W - MARGIN_X - tw, PAGE_H - MARGIN_TOP - 3.6 * mm, label)

    # Hairline
    hr(c, MARGIN_X, PAGE_H - MARGIN_TOP - 11 * mm, PAGE_W - MARGIN_X)


def footer_band(c, lang="es"):
    """Footer with web + email links + tag."""
    y_base = MARGIN_BOT
    y = y_base - 4.5 * mm
    hr(c, MARGIN_X, y_base, PAGE_W - MARGIN_X, LINE)

    c.setFont(F_MONO, 6.5)
    c.setFillColor(INK_FAINT)
    tag = "ESTUDIO · MADRID · 2026" if lang == "es" else "STUDIO · MADRID · 2026"
    c.drawString(MARGIN_X, y, tag)

    web_label = WEB_URL.replace("https://", "").upper()
    web_w = c.stringWidth(web_label, F_MONO, 6.5)
    web_x = (PAGE_W - web_w) / 2
    c.setFillColor(INK)
    c.drawString(web_x, y, web_label)
    c.linkURL(WEB_URL, (web_x, y - 1, web_x + web_w, y + 8), relative=0, thickness=0)

    em_label = EMAIL.upper()
    em_w = c.stringWidth(em_label, F_MONO, 6.5)
    em_x = PAGE_W - MARGIN_X - em_w
    c.drawString(em_x, y, em_label)
    c.linkURL(EMAIL_HREF, (em_x, y - 1, em_x + em_w, y + 8), relative=0, thickness=0)


def big_section_number(c, num, label_below=None, x=None, y=None, color=ACCENT):
    """Draws a giant editorial section number, like a magazine table of contents."""
    if x is None: x = MARGIN_X
    if y is None: y = PAGE_H - MARGIN_TOP - 30 * mm
    c.setFillColor(color)
    c.setFont(F_SERIF, 110)  # huge
    c.drawString(x, y - 30 * mm, num)
    if label_below:
        c.setFont(F_MONO, 7)
        c.setFillColor(INK_SOFT)
        c.drawString(x, y - 36 * mm, label_below.upper())


# ============================================================
# COPY (ES / EN)
# ============================================================
COPY_ES = {
    # Page 1
    "kicker": "ESTUDIO · MADRID · 2026 · 01/04",
    "h1_l1": "Diseñamos",
    "h1_l2": "ecosistemas digitales.",
    "lead": ("Para captar capital, multiplicar el ROI o, simplemente, "
             "saber qué hacer la próxima semana."),
    "two_col_l_label": "IDEA SIN ATERRIZAR",
    "two_col_l_body":  ("Tienes una intuición de negocio pero no sabes "
                        "por dónde empezar a estructurarla. Empezamos "
                        "por ahí — en un brainstorm te devolvemos opciones reales."),
    "two_col_r_label": "EMPRESA CON NUEVA VÍA",
    "two_col_r_body":  ("Tu empresa funciona pero quieres abrir una nueva "
                        "vía de monetización sin canibalizar el core. "
                        "Diseñamos la capa siguiente — completa, lista para operar."),
    "btn_primary": "Reservar 30 min con Marta",
    "btn_secondary": "Ver casos navegables",
    "promise_kicker": "LA PROMESA",
    "promise_quote": ("Reserva 30 minutos y en las 48 horas siguientes "
                      "recibes un one-pager gratis con tres movimientos "
                      "accionables específicos para tu proyecto."),
    "promise_caption": "Sin contratar nada. El valor es tuyo aunque no sigamos juntos.",

    "stats": [
        ("10–15", "DÍAS PARA EL BLUEPRINT"),
        ("7",     "ENTIDADES COORDINADAS"),
        ("8",     "DISCIPLINAS · UNA VOZ"),
        ("100%",  "PROTOTIPO NAVEGABLE"),
    ],

    # Page 2 · Casavera
    "p2_section_num": "02",
    "p2_section_label": "CASOS · TRAYECTORIA",
    "p2_kicker": "PROYECTO REAL · 2025",
    "p2_h1": "Casavera",
    "p2_h1_sub": "Inmobiliaria boutique · Madrid",

    "p2_block1_kicker": "LO QUE NECESITABA CASAVERA",
    "p2_block1_body": ("Inmobiliaria Casavera quería dejar de gestionar alquileres, "
                       "ventas e inversión en Madrid con la operativa repartida en "
                       "cuatro Excels y el correo. Tenía clientes recurrentes y "
                       "reputación, pero ningún sistema que conectara captación con "
                       "visita, visita con reserva, reserva con firma — y nada de eso "
                       "con el plan financiero del año."),

    "p2_block2_kicker": "LO QUE ENTREGÓ PRAXIA",
    "p2_block2_body": ("Un ecosistema digital con dos caras. La web pública, "
                       "con cuatro puertas de entrada — invertir, vender, alquilar, "
                       "buscar piso — pensada para que cada visitante encaje su intención "
                       "en menos de cinco segundos. El back office propio, con vista "
                       "panorámica de los diez procesos del negocio: desde el catálogo "
                       "hasta el cash flow proyectado mes a mes."),

    "p2_link1_kicker": "PROTOTIPO A · INTERNO",
    "p2_link1_label": "Sistema operativo · back office",
    "p2_link2_kicker": "PROTOTIPO B · PÚBLICO",
    "p2_link2_label": "Web pública · 4 puertas de entrada",
    "p2_layers": "PRODUCTO · IA · MODELO · MARKETING · OPERACIONES · COMERCIAL",
    "p2_pull_quote": ("«Una sola fuente de verdad — no cuatro Excels.»"),

    "p2_others_kicker": "OTROS PROYECTOS · SIN PROTOTIPO PÚBLICO",
    "p2_others_1_t": "EdTech · educación emocional",
    "p2_others_1_d": ("Ecosistema de AIE con plataforma de educación emocional. "
                      "Caso real, anonimizado por confidencialidad."),
    "p2_others_2_t": "Proyecto propio · activo",
    "p2_others_2_d": ("Ecosistema emocional propio con IA en producción. Tres líneas "
                      "(B2C · marketplace · enterprise). El laboratorio donde se prueban "
                      "las técnicas de Cápsula 01 y 02."),

    # Page 3 · prototipos ficticios
    "p3_section_num": "03",
    "p3_section_label": "CASOS · MÉTODO",
    "p3_kicker": "PROTOTIPOS NAVEGABLES",
    "p3_h1": "Cuatro casos.",
    "p3_h1_sub": "Para entender cómo se ve un ecosistema de Praxia.",
    "p3_intro": ("Construidos con el mismo rigor que un encargo real. Web, back office, "
                 "simulador interactivo y modelo económico — todo tocable. Cuando "
                 "trabajamos contigo, esto se construye con tu marca, tus números y "
                 "tus protocolos."),
    "p3_cards": [
        ("BODEGA VALDESCURO", "FAMILY BUSINESS · VINO",
         "Tres generaciones haciendo vino. La cuarta abre un club privado y vehículo de coinversión.",
         f"{WEB_URL}/Praxia_Atelier_Caso_Bodega_Valdescuro.html"),
        ("CLÍNICA LUMEN", "HEALTH-TECH · LONGEVIDAD",
         "Medicina integrativa de longevidad con membresía Plus, avatar Sofia y SaaS para practitioners.",
         f"{WEB_URL}/Praxia_Atelier_Caso_Clinica_Lumen.html"),
        ("CASA VENTO", "REAL ESTATE · RESIDENCIAL",
         "Operadora de pisos reformados con vehículo privado de coinversión y club de inquilinos.",
         f"{WEB_URL}/Praxia_Atelier_Caso_Casa_Vento.html"),
        ("MESA DE TRABAJO", "FOUNDER-CLIENTE · MÉTODO",
         "El método del estudio aplicado al propio estudio. Ocho departamentos diseñados con su misma lógica.",
         f"{WEB_URL}/Praxia_Atelier_Caso_Mesa_de_Trabajo.html"),
    ],
    "p3_btn_label": "Abrir caso",

    # Page 4 · cápsulas + cierre
    "p4_section_num": "04",
    "p4_section_label": "QUÉ CONSTRUIMOS",
    "p4_kicker": "SIETE CÁPSULAS · PRECIO CERRADO",
    "p4_h1": "No vendemos horas.",
    "p4_h1_sub": ("Cada cápsula tiene alcance, plazo y entregables fijos. "
                  "Si no encajan, no hay propuesta."),
    "capsules": [
        ("00", "Strategy Sprint", "1 sem", "990 – 2.500 €"),
        ("01", "Ecosystem Blueprint", "10–15 días", "12.000 – 18.000 €"),
        ("02", "Ecosystem Build", "3–5 meses", "60.000 – 120.000 €"),
        ("03", "Ecosystem Operate", "recurrente", "5.500 – 8.000 €/mes"),
        ("04/05/06", "Marketing · Ops · Comercial", "2–3 sem", "6.500 – 9.500 €"),
        ("PACK", "GTM (04+05+06 integradas)", "5 sem", "18.000 € · ahorro 4.500 €"),
    ],
    "trick_kicker": "TRUCO HONESTO",
    "trick_body": ("Si después del Sprint contratas la Cápsula 01 en los siguientes "
                   "30 días, los honorarios del sprint se descuentan íntegramente "
                   "de la factura del Blueprint. En la práctica, el sprint sale "
                   "gratis si avanzamos."),
    "founder_kicker": "FUNDADORA",
    "founder_name": "Marta Escobar Rojas",
    "founder_sub": "MBA · Founder con IA en producción · Madrid",
    "cta_h1": "Treinta minutos.",
    "cta_h2": "Sin compromiso.",
    "cta_caption": "Una conversación clara — no una llamada de venta.",
    "cta_btn": "Reservar diagnóstico",
    "cta_or": "O ESCRIBE A:",
}


COPY_EN = dict(COPY_ES)  # start from ES; override the strings that change
COPY_EN.update({
    "kicker": "STUDIO · MADRID · 2026 · 01/04",
    "h1_l1": "We design",
    "h1_l2": "digital ecosystems.",
    "lead": ("To raise capital, multiply ROI or, simply, "
             "to know exactly what to do next week."),
    "two_col_l_label": "IDEA WITHOUT GROUNDING",
    "two_col_l_body": ("You have a business intuition but you don't know "
                       "where to start structuring it. We start there — in "
                       "a brainstorm we hand you real options."),
    "two_col_r_label": "COMPANY · NEW LINE",
    "two_col_r_body": ("Your company works but you want to open a new "
                       "revenue line without cannibalising the core. "
                       "We design the next layer — complete, ready to operate."),
    "btn_primary": "Book 30 min with Marta",
    "btn_secondary": "See navigable cases",
    "promise_kicker": "THE PROMISE",
    "promise_quote": ("Book thirty minutes and within 48 hours you receive "
                      "a free one-pager with three actionable moves "
                      "specific to your project."),
    "promise_caption": "No contract required. The value is yours even if we don't continue together.",
    "stats": [
        ("10–15", "DAYS TO BLUEPRINT"),
        ("7",     "ENTITIES COORDINATED"),
        ("8",     "DISCIPLINES · ONE VOICE"),
        ("100%",  "NAVIGABLE PROTOTYPE"),
    ],
    "p2_section_label": "CASES · TRACK RECORD",
    "p2_kicker": "REAL PROJECT · 2025",
    "p2_h1_sub": "Boutique real estate · Madrid",
    "p2_block1_kicker": "WHAT CASAVERA NEEDED",
    "p2_block1_body": ("Casavera real estate wanted to stop running rentals, sales "
                       "and investment in Madrid with operations scattered across "
                       "four spreadsheets and email. It had recurring clients and "
                       "reputation, but no system connecting acquisition to visit, "
                       "visit to booking, booking to signing — and none of that to "
                       "the year's financial plan."),
    "p2_block2_kicker": "WHAT PRAXIA DELIVERED",
    "p2_block2_body": ("A digital ecosystem with two faces. The public website, "
                       "with four entry doors — invest, sell, rent, search — "
                       "designed so every visitor fits their intent in under five "
                       "seconds. The custom back office, with a panoramic view of "
                       "the ten business processes: from the catalogue to monthly "
                       "projected cash flow."),
    "p2_link1_kicker": "PROTOTYPE A · INTERNAL",
    "p2_link1_label": "Operating system · back office",
    "p2_link2_kicker": "PROTOTYPE B · PUBLIC",
    "p2_link2_label": "Public website · 4 entry doors",
    "p2_layers": "PRODUCT · AI · MODEL · MARKETING · OPERATIONS · SALES",
    "p2_pull_quote": "“A single source of truth — not four spreadsheets.”",
    "p2_others_kicker": "OTHER PROJECTS · NO PUBLIC PROTOTYPE",
    "p2_others_1_t": "EdTech · emotional education",
    "p2_others_1_d": ("AIE ecosystem with emotional education platform. Real case, "
                      "anonymised for confidentiality."),
    "p2_others_2_t": "Own project · active",
    "p2_others_2_d": ("Own emotional ecosystem with AI in production. Three lines "
                      "(B2C · marketplace · enterprise). The lab where the techniques "
                      "of Capsule 01 and 02 are tested."),
    "p3_section_label": "CASES · METHOD",
    "p3_kicker": "NAVIGABLE PROTOTYPES",
    "p3_h1": "Four cases.",
    "p3_h1_sub": "To understand what a Praxia ecosystem looks like.",
    "p3_intro": ("Built with the same rigour as a real engagement. Website, back "
                 "office, interactive simulator and economic model — all tactile. "
                 "When we work with you, this is built with your brand, your "
                 "numbers and your protocols."),
    "p3_cards": [
        ("BODEGA VALDESCURO", "FAMILY BUSINESS · WINE",
         "Three generations making wine. The fourth opens a private members club and co-investment vehicle.",
         f"{WEB_URL}/Praxia_Atelier_Caso_Bodega_Valdescuro.html"),
        ("CLÍNICA LUMEN", "HEALTH-TECH · LONGEVITY",
         "Integrative longevity medicine with Plus membership, Sofia avatar and SaaS for practitioners.",
         f"{WEB_URL}/Praxia_Atelier_Caso_Clinica_Lumen.html"),
        ("CASA VENTO", "REAL ESTATE · RESIDENTIAL",
         "Operator of refurbished apartments with private co-investment vehicle and tenants' club.",
         f"{WEB_URL}/Praxia_Atelier_Caso_Casa_Vento.html"),
        ("MESA DE TRABAJO", "FOUNDER-CLIENT · METHOD",
         "The studio's method applied to the studio itself. Eight departments designed with the same logic.",
         f"{WEB_URL}/Praxia_Atelier_Caso_Mesa_de_Trabajo.html"),
    ],
    "p3_btn_label": "Open case",
    "p4_section_label": "WHAT WE BUILD",
    "p4_kicker": "SEVEN CAPSULES · CLOSED PRICE",
    "p4_h1": "We don't sell hours.",
    "p4_h1_sub": ("Each capsule has a defined scope, timeline and deliverables. "
                  "If they don't fit, there's no proposal."),
    "capsules": [
        ("00", "Strategy Sprint", "1 wk", "990 – 2,500 €"),
        ("01", "Ecosystem Blueprint", "10–15 days", "12,000 – 18,000 €"),
        ("02", "Ecosystem Build", "3–5 months", "60,000 – 120,000 €"),
        ("03", "Ecosystem Operate", "recurring", "5,500 – 8,000 €/month"),
        ("04/05/06", "Marketing · Ops · Sales", "2–3 wk", "6,500 – 9,500 €"),
        ("PACK", "GTM (04+05+06 integrated)", "5 wk", "18,000 € · save 4,500 €"),
    ],
    "trick_kicker": "HONEST TRICK",
    "trick_body": ("If after the Sprint you book Capsule 01 within 30 days, the "
                   "Sprint fee is deducted in full from the Blueprint invoice. "
                   "In practice, the Sprint is free if we move forward."),
    "founder_kicker": "FOUNDER",
    "founder_sub": "MBA · Founder with AI in production · Madrid",
    "cta_h1": "Thirty minutes.",
    "cta_h2": "No commitment.",
    "cta_caption": "A clear conversation — not a sales call.",
    "cta_btn": "Book diagnostic",
    "cta_or": "OR WRITE TO:",
})


# ============================================================
# Page builders
# ============================================================
def page1(c, t):
    header_band(c, 1, 4)

    # Top kicker
    y = PAGE_H - MARGIN_TOP - 20 * mm
    c.setFont(F_MONO, 7)
    c.setFillColor(ACCENT)
    c.drawString(MARGIN_X, y, t["kicker"])
    y -= 14 * mm

    # H1 — two huge serif lines
    c.setFillColor(INK)
    c.setFont(F_SERIF_BOLD, 46)
    c.drawString(MARGIN_X, y, t["h1_l1"])
    y -= 14 * mm
    c.setFont(F_SERIF_BOLD, 46)
    c.drawString(MARGIN_X, y, t["h1_l2"])
    y -= 16 * mm

    # Lead
    y = draw_text(c, t["lead"], MARGIN_X, y, CONTENT_W * 0.85, F_SERIF, 16, INK_SOFT, leading=22)
    y -= 6 * mm

    # Hairline
    hr(c, MARGIN_X, y, MARGIN_X + 28 * mm, INK, 1.2)
    y -= 14 * mm

    # Two columns
    col_w = (CONTENT_W - 14 * mm) / 2
    col_top = y
    # Left
    c.setFont(F_MONO, 6.5); c.setFillColor(ACCENT)
    c.drawString(MARGIN_X, col_top, t["two_col_l_label"])
    yy = col_top - 6 * mm
    yy = draw_text(c, t["two_col_l_body"], MARGIN_X, yy, col_w, F_SANS, 9.5, INK, leading=14)
    # Right
    rx = MARGIN_X + col_w + 14 * mm
    c.setFont(F_MONO, 6.5); c.setFillColor(MOSS)
    c.drawString(rx, col_top, t["two_col_r_label"])
    yy2 = col_top - 6 * mm
    yy2 = draw_text(c, t["two_col_r_body"], rx, yy2, col_w, F_SANS, 9.5, INK, leading=14)
    y = min(yy, yy2) - 12 * mm

    # CTAs
    btn_h = 11 * mm
    bw1 = 56 * mm; bw2 = 44 * mm
    draw_link_button(c, t["btn_primary"], CAL_URL,
                     MARGIN_X, y - btn_h, bw1, btn_h,
                     fill=INK, text=PAPER, font_size=10.5)
    draw_link_button(c, t["btn_secondary"], f"{WEB_URL}/#casos",
                     MARGIN_X + bw1 + 4 * mm, y - btn_h, bw2, btn_h,
                     fill=None, text=INK, border=INK, font_size=10)
    y -= btn_h + 16 * mm

    # Promise · pull quote box (terracota soft)
    pq_h = 38 * mm
    c.setFillColor(ACCENT_SOFT)
    c.rect(MARGIN_X, y - pq_h, CONTENT_W, pq_h, stroke=0, fill=1)
    # accent bar left
    c.setFillColor(ACCENT)
    c.rect(MARGIN_X, y - pq_h, 1.2 * mm, pq_h, stroke=0, fill=1)
    # Kicker
    c.setFont(F_MONO, 6.5); c.setFillColor(ACCENT_DEEP)
    c.drawString(MARGIN_X + 8 * mm, y - 6 * mm, t["promise_kicker"])
    # Quote in serif italic
    c.setFont(F_SERIF, 14); c.setFillColor(INK)
    yy = y - 13 * mm
    yy = draw_text(c, t["promise_quote"], MARGIN_X + 8 * mm, yy, CONTENT_W - 16 * mm,
                   F_SERIF, 13, INK, leading=18)
    # Caption mono
    c.setFont(F_MONO, 7); c.setFillColor(INK_SOFT)
    c.drawString(MARGIN_X + 8 * mm, y - pq_h + 6 * mm, t["promise_caption"])
    y -= pq_h + 14 * mm

    # Stats (4 cells, no border, big numbers)
    cell_w = CONTENT_W / 4
    for i, (big, small) in enumerate(t["stats"]):
        cx = MARGIN_X + i * cell_w
        c.setFillColor(INK); c.setFont(F_SERIF_BOLD, 28)
        c.drawString(cx, y - 10 * mm, big)
        c.setFont(F_MONO, 6)
        c.setFillColor(INK_SOFT)
        c.drawString(cx, y - 14 * mm, small)
        # Vertical hairline between cells
        if i < 3:
            c.setStrokeColor(LINE); c.setLineWidth(0.4)
            c.line(cx + cell_w - 3 * mm, y - 16 * mm, cx + cell_w - 3 * mm, y + 1 * mm)

    footer_band(c, lang="es" if t is COPY_ES else "en")


def page2_casavera(c, t):
    """Casavera takes a full page."""
    header_band(c, 2, 4)

    # Editorial number 02
    big_section_number(c, t["p2_section_num"], t["p2_section_label"], color=ACCENT)

    # Title block right of the giant number
    title_x = MARGIN_X + 80 * mm
    title_y = PAGE_H - MARGIN_TOP - 24 * mm
    c.setFont(F_MONO, 6.5); c.setFillColor(ACCENT)
    c.drawString(title_x, title_y, t["p2_kicker"])
    c.setFont(F_SERIF_BOLD, 38); c.setFillColor(INK)
    c.drawString(title_x, title_y - 13 * mm, t["p2_h1"])
    c.setFont(F_SERIF, 13); c.setFillColor(INK_SOFT)
    c.drawString(title_x, title_y - 19 * mm, t["p2_h1_sub"])

    # Two columns: needed / delivered
    y = PAGE_H - MARGIN_TOP - 76 * mm
    col_w = (CONTENT_W - 14 * mm) / 2

    # Hairline above
    hr(c, MARGIN_X, y + 6 * mm, PAGE_W - MARGIN_X, LINE)

    # Left col — Needed
    c.setFont(F_MONO, 6.5); c.setFillColor(ACCENT)
    c.drawString(MARGIN_X, y, t["p2_block1_kicker"])
    y_needed = draw_text(c, t["p2_block1_body"], MARGIN_X, y - 6 * mm,
                         col_w, F_SERIF, 11, INK, leading=16)

    # Right col — Delivered
    rx = MARGIN_X + col_w + 14 * mm
    c.setFont(F_MONO, 6.5); c.setFillColor(ACCENT)
    c.drawString(rx, y, t["p2_block2_kicker"])
    y_delivered = draw_text(c, t["p2_block2_body"], rx, y - 6 * mm,
                            col_w, F_SERIF, 11, INK, leading=16)

    y = min(y_needed, y_delivered) - 14 * mm

    # Pull quote (italic, large, centered-ish)
    c.setFont(F_SERIF, 18)
    c.setFillColor(ACCENT)
    pq = t["p2_pull_quote"]
    pq_w = c.stringWidth(pq, F_SERIF, 18)
    c.drawString((PAGE_W - pq_w) / 2, y, pq)
    y -= 16 * mm

    # Two large action buttons
    btn_h = 14 * mm
    bw = (CONTENT_W - 8 * mm) / 2
    # Left
    c.setFont(F_MONO, 6.5); c.setFillColor(ACCENT)
    c.drawString(MARGIN_X, y, t["p2_link1_kicker"])
    draw_link_button(c, t["p2_link1_label"], "https://resilient-arithmetic-182add.netlify.app/",
                     MARGIN_X, y - btn_h - 6 * mm, bw, btn_h,
                     fill=INK, text=PAPER, font_size=10.5)
    # Right
    c.setFont(F_MONO, 6.5); c.setFillColor(ACCENT)
    c.drawString(MARGIN_X + bw + 8 * mm, y, t["p2_link2_kicker"])
    draw_link_button(c, t["p2_link2_label"], "https://rococo-sawine-40e557.netlify.app/",
                     MARGIN_X + bw + 8 * mm, y - btn_h - 6 * mm, bw, btn_h,
                     fill=INK, text=PAPER, font_size=10.5)
    y -= btn_h + 14 * mm

    # Layers tag
    c.setFont(F_MONO, 6.5); c.setFillColor(INK_FAINT)
    c.drawString(MARGIN_X, y, "CAPAS · " + t["p2_layers"])
    y -= 12 * mm

    # Hairline
    hr(c, MARGIN_X, y, PAGE_W - MARGIN_X, LINE)
    y -= 9 * mm

    # Other projects
    c.setFont(F_MONO, 6.5); c.setFillColor(INK_FAINT)
    c.drawString(MARGIN_X, y, t["p2_others_kicker"])
    y -= 7 * mm

    others = [
        (t["p2_others_1_t"], t["p2_others_1_d"]),
        (t["p2_others_2_t"], t["p2_others_2_d"]),
    ]
    o_col_w = (CONTENT_W - 14 * mm) / 2
    for i, (title_o, body_o) in enumerate(others):
        ox = MARGIN_X + i * (o_col_w + 14 * mm)
        c.setFont(F_SERIF_BOLD, 11); c.setFillColor(INK)
        c.drawString(ox, y, title_o)
        draw_text(c, body_o, ox, y - 5 * mm, o_col_w, F_SANS, 9, INK_SOFT, leading=12.5, max_lines=4)

    footer_band(c, lang="es" if t is COPY_ES else "en")


def page3_demos(c, t):
    header_band(c, 3, 4)

    big_section_number(c, t["p3_section_num"], t["p3_section_label"], color=ACCENT)

    # Title block
    title_x = MARGIN_X + 80 * mm
    title_y = PAGE_H - MARGIN_TOP - 24 * mm
    c.setFont(F_MONO, 6.5); c.setFillColor(ACCENT)
    c.drawString(title_x, title_y, t["p3_kicker"])
    c.setFont(F_SERIF_BOLD, 36); c.setFillColor(INK)
    c.drawString(title_x, title_y - 13 * mm, t["p3_h1"])
    # subtitle wrap
    draw_text(c, t["p3_h1_sub"], title_x, title_y - 21 * mm,
              CONTENT_W - 80 * mm, F_SERIF, 13, INK_SOFT, leading=17)

    y = PAGE_H - MARGIN_TOP - 78 * mm
    hr(c, MARGIN_X, y + 6 * mm, PAGE_W - MARGIN_X, LINE)
    y = draw_text(c, t["p3_intro"], MARGIN_X, y, CONTENT_W * 0.78, F_SERIF, 11, INK_SOFT, leading=15.5)
    y -= 8 * mm

    # 4 cards (2x2) — clean editorial style with thin hairline divider
    case_w = (CONTENT_W - 8 * mm) / 2
    case_h = 64 * mm
    for i, (name, sector, blurb, url) in enumerate(t["p3_cards"]):
        col = i % 2; row = i // 2
        cx = MARGIN_X + col * (case_w + 8 * mm)
        cy = y - row * (case_h + 6 * mm) - case_h

        # Top hairline + sector kicker
        c.setStrokeColor(INK); c.setLineWidth(1)
        c.line(cx, cy + case_h, cx + case_w, cy + case_h)
        c.setFont(F_MONO, 6.5); c.setFillColor(ACCENT)
        c.drawString(cx, cy + case_h - 5 * mm, sector)
        # Name
        c.setFont(F_SERIF_BOLD, 17); c.setFillColor(INK)
        c.drawString(cx, cy + case_h - 14 * mm, name)
        # Blurb
        draw_text(c, blurb, cx, cy + case_h - 22 * mm, case_w,
                  F_SANS, 9.2, INK_SOFT, leading=13, max_lines=4)
        # Open link button
        draw_link_button(c, t["p3_btn_label"] + " →", url,
                         cx, cy + 5 * mm, 28 * mm, 8 * mm,
                         fill=None, text=ACCENT, border=ACCENT, font_size=8.5)

    footer_band(c, lang="es" if t is COPY_ES else "en")


def page4_capsules(c, t):
    header_band(c, 4, 4)

    big_section_number(c, t["p4_section_num"], t["p4_section_label"], color=ACCENT)

    title_x = MARGIN_X + 80 * mm
    title_y = PAGE_H - MARGIN_TOP - 24 * mm
    c.setFont(F_MONO, 6.5); c.setFillColor(ACCENT)
    c.drawString(title_x, title_y, t["p4_kicker"])
    c.setFont(F_SERIF_BOLD, 36); c.setFillColor(INK)
    c.drawString(title_x, title_y - 13 * mm, t["p4_h1"])
    draw_text(c, t["p4_h1_sub"], title_x, title_y - 21 * mm,
              CONTENT_W - 80 * mm, F_SERIF, 12.5, INK_SOFT, leading=17)

    y = PAGE_H - MARGIN_TOP - 80 * mm

    # Capsules table (editorial · hairlines)
    hr(c, MARGIN_X, y + 4 * mm, PAGE_W - MARGIN_X, INK, 1)
    row_h = 11 * mm
    for num, name, when, price in t["capsules"]:
        is_pack = (num == "PACK")
        if is_pack:
            c.setFillColor(ACCENT_SOFT)
            c.rect(MARGIN_X, y - row_h + 1 * mm, CONTENT_W, row_h - 1 * mm, stroke=0, fill=1)
        # number
        c.setFont(F_MONO, 9); c.setFillColor(ACCENT_DEEP if is_pack else ACCENT)
        c.drawString(MARGIN_X + 2 * mm, y - 7 * mm, num)
        # name
        c.setFont(F_SERIF_BOLD, 12); c.setFillColor(INK)
        c.drawString(MARGIN_X + 24 * mm, y - 7 * mm, name)
        # plazo
        c.setFont(F_MONO, 7.5); c.setFillColor(INK_SOFT)
        c.drawString(MARGIN_X + 100 * mm, y - 7 * mm, when.upper())
        # price (right)
        c.setFont(F_SANS_MED, 10); c.setFillColor(INK)
        pw = c.stringWidth(price, F_SANS_MED, 10)
        c.drawString(PAGE_W - MARGIN_X - pw - 2 * mm, y - 7 * mm, price)
        y -= row_h
        if not is_pack:
            hr(c, MARGIN_X, y, PAGE_W - MARGIN_X, LINE, 0.4)

    y -= 10 * mm

    # Truco honesto (terracota soft band with kicker)
    th = 26 * mm
    c.setFillColor(ACCENT_SOFT)
    c.rect(MARGIN_X, y - th, CONTENT_W, th, stroke=0, fill=1)
    c.setFillColor(ACCENT)
    c.rect(MARGIN_X, y - th, 1.2 * mm, th, stroke=0, fill=1)
    c.setFont(F_MONO, 6.5); c.setFillColor(ACCENT_DEEP)
    c.drawString(MARGIN_X + 8 * mm, y - 5 * mm, t["trick_kicker"])
    draw_text(c, t["trick_body"], MARGIN_X + 8 * mm, y - 11 * mm,
              CONTENT_W - 16 * mm, F_SERIF, 11, INK, leading=15)
    y -= th + 14 * mm

    # Founder + final CTA
    c.setFont(F_MONO, 6.5); c.setFillColor(INK_FAINT)
    c.drawString(MARGIN_X, y, t["founder_kicker"])
    c.setFont(F_SERIF_BOLD, 22); c.setFillColor(INK)
    c.drawString(MARGIN_X, y - 9 * mm, t["founder_name"])
    c.setFont(F_SANS, 9.5); c.setFillColor(INK_SOFT)
    c.drawString(MARGIN_X, y - 14 * mm, t["founder_sub"])
    y -= 28 * mm

    # CTA black band
    cta_h = 38 * mm
    c.setFillColor(INK)
    c.rect(MARGIN_X, y - cta_h, CONTENT_W, cta_h, stroke=0, fill=1)
    # Title
    c.setFillColor(PAPER); c.setFont(F_SERIF_BOLD, 22)
    c.drawString(MARGIN_X + 8 * mm, y - 11 * mm, t["cta_h1"])
    c.setFont(F_SERIF, 22); c.setFillColor(ACCENT_SOFT)
    c.drawString(MARGIN_X + 8 * mm, y - 19 * mm, t["cta_h2"])
    # Caption
    c.setFont(F_SANS, 9.5); c.setFillColor(PAPER_DEEP)
    c.drawString(MARGIN_X + 8 * mm, y - 24 * mm, t["cta_caption"])
    # Button (terracota)
    btn_w = 56 * mm; btn_h = 10 * mm
    draw_link_button(c, t["cta_btn"] + " · 30 min", CAL_URL,
                     MARGIN_X + 8 * mm, y - cta_h + 6 * mm, btn_w, btn_h,
                     fill=ACCENT, text=PAPER, font_size=10)
    # Email next to button
    em_x = MARGIN_X + 8 * mm + btn_w + 8 * mm
    em_y = y - cta_h + 11 * mm
    c.setFont(F_MONO, 7); c.setFillColor(PAPER_DEEP)
    c.drawString(em_x, em_y + 3 * mm, t["cta_or"])
    c.setFont(F_SANS_MED, 10); c.setFillColor(PAPER)
    c.drawString(em_x, em_y - 2 * mm, EMAIL)
    em_w = c.stringWidth(EMAIL, F_SANS_MED, 10)
    c.linkURL(EMAIL_HREF, (em_x, em_y - 4 * mm, em_x + em_w, em_y + 6 * mm), relative=0, thickness=0)

    footer_band(c, lang="es" if t is COPY_ES else "en")


# ============================================================
# Main
# ============================================================
def build(out_path, lang="es"):
    t = COPY_ES if lang == "es" else COPY_EN
    c = canvas_module.Canvas(out_path, pagesize=A4)
    c.setTitle("Praxia Atelier · " + ("Servicios" if lang == "es" else "Services"))
    c.setAuthor("Marta Escobar Rojas")
    c.setSubject("Estudio de arquitectura de ecosistemas digitales · Servicios y casos")
    c.setCreator("Praxia Atelier")
    page1(c, t); c.showPage()
    page2_casavera(c, t); c.showPage()
    page3_demos(c, t); c.showPage()
    page4_capsules(c, t); c.showPage()
    c.save()
    print(f"PDF generated: {out_path}")


if __name__ == "__main__":
    import shutil
    es_path = Path("Praxia_Atelier_Servicios.pdf")
    en_path = Path("Praxia_Atelier_Services.pdf")
    build(str(es_path), lang="es")
    build(str(en_path), lang="en")
    shutil.copy(es_path, Path("deploy_netlify") / es_path)
    shutil.copy(en_path, Path("deploy_netlify") / en_path)
    print("Synced to deploy_netlify/")
