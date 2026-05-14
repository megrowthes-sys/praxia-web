"""Build Praxia_Atelier_Servicios.pdf · v4

Fixes vs v3:
- Auto-shrink: every headline measured against available width and shrunk if it
  doesn't fit (no more text running off the right margin).
- Editorial number ("02", "03", "04") moved to a SAFE zone — same line as the
  page kicker, in a fixed top band. NEVER overlaps title or body.
- Page 4 CTA tightened — caption no longer collides with email; everything
  fits inside the dark band; footer stays below as separate band.
- Stat band: dot separators replaced with adequate gap so numbers don't kiss
  adjacent labels.
- Card content uses ellipsis if it exceeds N lines; cards have explicit padding.
- Generous bleed: 8mm extra padding between every block.
"""
from pathlib import Path
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor, white
from reportlab.pdfgen import canvas as canvas_module
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import simpleSplit

# ── Palette ──
INK         = HexColor("#1a1f2e")
INK_SOFT    = HexColor("#44485a")
INK_FAINT   = HexColor("#8b8e98")
PAPER       = HexColor("#faf8f3")
PAPER_DEEP  = HexColor("#f3f0e6")
LINE        = HexColor("#e6e1d6")
ACCENT      = HexColor("#b9522e")
ACCENT_SOFT = HexColor("#f3ddd0")
ACCENT_DEEP = HexColor("#8a3d22")
MOSS        = HexColor("#4a5d3a")
GOLD        = HexColor("#b08d3a")
SLATE       = HexColor("#4b5d6e")

# ── URLs ──
CAL_URL = "https://cal.com/marta-escobar-rojas-teatxg/30min"
WEB_URL = "https://praxia-atelier.net"
EMAIL = "info@praxia-atelier.net"
EMAIL_HREF = f"mailto:{EMAIL}"

# ── Fonts ──
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
        if not path.exists():
            print(f"WARN missing font {path}"); continue
        try:
            pdfmetrics.registerFont(TTFont(name, str(path)))
        except Exception as e:
            print(f"WARN registering {name}: {e}")
register_fonts()

F_SERIF      = "Fraunces"
F_SERIF_BOLD = "Fraunces-Bold"
F_SANS       = "Plex"
F_SANS_MED   = "Plex-Med"
F_MONO       = "PlexMono"

# ── Geometry ──
PAGE_W, PAGE_H = A4
MARGIN_X       = 22 * mm
MARGIN_TOP     = 22 * mm
MARGIN_BOT     = 22 * mm
CONTENT_W      = PAGE_W - 2 * MARGIN_X
HEADER_HEIGHT  = 14 * mm
FOOTER_HEIGHT  = 12 * mm
CONTENT_TOP    = PAGE_H - MARGIN_TOP - HEADER_HEIGHT
CONTENT_BOT    = MARGIN_BOT + FOOTER_HEIGHT


# ============================================================
# Helpers
# ============================================================
def fit_size(c, text, font, max_size, min_size, max_w):
    """Return the largest size between min_size and max_size that fits text in max_w."""
    size = max_size
    while size > min_size:
        if c.stringWidth(text, font, size) <= max_w:
            return size
        size -= 0.5
    return min_size


def draw_text(c, text, x, y, w, font, size, color, leading=None, max_lines=None):
    if leading is None: leading = size * 1.42
    lines = simpleSplit(text, font, size, w)
    if max_lines and len(lines) > max_lines:
        # truncate with ellipsis on last allowed line
        kept = lines[:max_lines]
        last = kept[-1]
        # try shaving until adding "…" fits
        while c.stringWidth(last + "…", font, size) > w and len(last) > 0:
            last = last[:-1]
        kept[-1] = last + "…"
        lines = kept
    c.setFillColor(color); c.setFont(font, size)
    for line in lines:
        c.drawString(x, y, line)
        y -= leading
    return y


def hr(c, x1, y, x2, color=LINE, width=0.5):
    c.setStrokeColor(color); c.setLineWidth(width)
    c.line(x1, y, x2, y)


def draw_button(c, label, url, x, y, w, h,
                fill=None, text=None, border=None, font_size=10.5,
                font=None, shadow=False, shadow_color=None):
    if font is None: font = F_SANS_MED
    # Auto-shrink label if doesn't fit
    label_size = font_size
    while label_size >= 7 and c.stringWidth(label, font, label_size) > w - 8 * mm:
        label_size -= 0.5
    if shadow:
        sc = shadow_color or INK
        c.setFillColor(sc)
        c.rect(x + 1.4*mm, y - 1.4*mm, w, h, stroke=0, fill=1)
    if fill is not None:
        c.setFillColor(fill); c.rect(x, y, w, h, stroke=0, fill=1)
    if border is not None:
        c.setStrokeColor(border); c.setLineWidth(0.7)
        c.rect(x, y, w, h, stroke=1, fill=0)
    c.setFillColor(text or white); c.setFont(font, label_size)
    text_y = y + (h - label_size * 0.7) / 2
    text_w = c.stringWidth(label, font, label_size)
    c.drawString(x + (w - text_w) / 2, text_y, label)
    c.linkURL(url, (x, y, x + w, y + h), relative=0, thickness=0)


def header_band(c, page_num, total_pages, edition_label=None, edition_num=None):
    """Top band: brand left + page indicator right + optional editorial 'NN' on the right
    next to the page number. The big editorial number for each section now lives
    inline with the page kicker, NOT as a giant glyph on the body."""
    c.setFillColor(PAPER); c.rect(0, 0, PAGE_W, PAGE_H, stroke=0, fill=1)
    mark_size = 9 * mm
    by = PAGE_H - MARGIN_TOP - mark_size
    c.setStrokeColor(INK); c.setLineWidth(0.8)
    c.rect(MARGIN_X, by, mark_size, mark_size, stroke=1, fill=0)
    c.setFillColor(INK); c.setFont(F_SERIF_BOLD, 14.5)
    c.drawString(MARGIN_X + 2.6 * mm, by + 2.3 * mm, "P")
    c.setFont(F_SERIF, 12)
    c.drawString(MARGIN_X + mark_size + 3 * mm, PAGE_H - MARGIN_TOP - 3.6 * mm, "Praxia Atelier")
    c.setFont(F_MONO, 6.5); c.setFillColor(INK_FAINT)
    c.drawString(MARGIN_X + mark_size + 3 * mm, PAGE_H - MARGIN_TOP - 7 * mm, "ECOSYSTEM ARCHITECTURE")
    c.setFont(F_MONO, 8); c.setFillColor(INK_FAINT)
    label = f"{page_num:02d}/{total_pages:02d}"
    tw = c.stringWidth(label, F_MONO, 8)
    c.drawString(PAGE_W - MARGIN_X - tw, PAGE_H - MARGIN_TOP - 3.6 * mm, label)
    hr(c, MARGIN_X, PAGE_H - MARGIN_TOP - 11 * mm, PAGE_W - MARGIN_X)


def footer_band(c, lang="es"):
    y_base = MARGIN_BOT
    y = y_base - 4.5 * mm
    hr(c, MARGIN_X, y_base, PAGE_W - MARGIN_X, LINE)
    c.setFont(F_MONO, 6.5); c.setFillColor(INK_FAINT)
    tag = "ESTUDIO · MADRID · 2026" if lang == "es" else "STUDIO · MADRID · 2026"
    c.drawString(MARGIN_X, y, tag)
    web_label = WEB_URL.replace("https://", "").upper()
    web_w = c.stringWidth(web_label, F_MONO, 6.5)
    web_x = (PAGE_W - web_w) / 2
    c.setFillColor(INK); c.drawString(web_x, y, web_label)
    c.linkURL(WEB_URL, (web_x, y - 1, web_x + web_w, y + 8), relative=0, thickness=0)
    em_label = EMAIL.upper()
    em_w = c.stringWidth(em_label, F_MONO, 6.5)
    em_x = PAGE_W - MARGIN_X - em_w
    c.drawString(em_x, y, em_label)
    c.linkURL(EMAIL_HREF, (em_x, y - 1, em_x + em_w, y + 8), relative=0, thickness=0)


def section_kicker(c, y, num, label, color=ACCENT):
    """Draws a section header line: '02 · CASOS · TRAYECTORIA' on a single row.
    Avoids the previous problem where the giant number overlapped the body."""
    c.setFillColor(color); c.setFont(F_SERIF_BOLD, 22)
    num_w = c.stringWidth(num, F_SERIF_BOLD, 22)
    c.drawString(MARGIN_X, y, num)
    c.setFont(F_MONO, 7.5); c.setFillColor(INK_SOFT)
    c.drawString(MARGIN_X + num_w + 5 * mm, y + 4, label)
    hr(c, MARGIN_X, y - 4 * mm, PAGE_W - MARGIN_X, INK, 1)
    return y - 14 * mm


# ============================================================
# COPY (igual que v3, sin cambios)
# ============================================================
COPY_ES = {
    "kicker_top": "ESTUDIO · MADRID · 2026",
    "p1_h1_a": "Diseñamos ecosistemas",
    "p1_h1_b": "digitales",
    "p1_h1_b_accent": "listos para captar capital,",
    "p1_h1_c": "multiplicar el ROI o, simplemente, saber qué hacer la próxima semana.",
    "p1_aterrizaje": ("Aterrizamos tu idea y la convertimos en un negocio real, "
                       "digitalizado y optimizado — con sistema operativo, página "
                       "web y todo lo que necesitas para empezar a funcionar."),
    "btn_primary": "Reservar 30 min con Marta",
    "btn_secondary": "Ver casos navegables",
    "btn_caption": "Gratis · Sin compromiso",
    "idea_kicker": "IDEA SIN ATERRIZAR",
    "idea_lead":   "Tienes una intuición de negocio pero no sabes por dónde empezar a estructurarla.",
    "idea_caption":"Empezamos por ahí — en un brainstorm te devolvemos opciones reales.",
    "comp_kicker": "EMPRESA CON NUEVA VÍA",
    "comp_lead":   "Tu empresa funciona pero quieres abrir una nueva vía sin canibalizar el core.",
    "comp_caption":"Diseñamos la capa siguiente — completa, lista para operar.",
    "promise_kicker": "LA PROMESA",
    "promise_quote": ("Reserva 30 minutos y en las 48 horas siguientes recibes un "
                       "one-pager gratis con tres movimientos accionables específicos "
                       "para tu proyecto."),
    "promise_caption": "— Sin contratar nada · El valor es tuyo aunque no sigamos juntos",
    "stats_kicker": "EL FORMATO",
    "stats": [("10–15", "DÍAS PARA EL BLUEPRINT"),
              ("7",     "ENTIDADES COORDINADAS"),
              ("8",     "DISCIPLINAS · UNA VOZ"),
              ("100%",  "PROTOTIPO NAVEGABLE")],
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
    "p2_block2_body": ("Un ecosistema digital con dos caras. La web pública con cuatro "
                       "puertas — invertir, vender, alquilar, buscar piso. Y el back "
                       "office propio, con vista panorámica de los diez procesos del "
                       "negocio: desde el catálogo hasta el cash flow proyectado mes a mes."),
    "p2_pull_quote": "“Una sola fuente de verdad — no cuatro Excels.”",
    "p2_link1_kicker": "PROTOTIPO A · INTERNO",
    "p2_link1_label": "Sistema operativo · back office",
    "p2_link2_kicker": "PROTOTIPO B · PÚBLICO",
    "p2_link2_label": "Web pública · 4 puertas",
    "p2_layers_kicker": "CAPAS",
    "p2_layers": "PRODUCTO · IA · MODELO · MARKETING · OPERACIONES · COMERCIAL",
    "p2_others_kicker": "OTROS PROYECTOS · SIN PROTOTIPO PÚBLICO",
    "p2_others_1_t": "EdTech · educación emocional",
    "p2_others_1_d": "Ecosistema de AIE con plataforma de educación emocional. Caso real, anonimizado por confidencialidad.",
    "p2_others_2_t": "Proyecto propio · activo",
    "p2_others_2_d": "Ecosistema emocional propio con IA en producción. Tres líneas (B2C · marketplace · enterprise).",
    "p3_section_label": "CASOS · MÉTODO",
    "p3_kicker": "PROTOTIPOS NAVEGABLES",
    "p3_h1": "Cuatro casos.",
    "p3_h1_sub": "Para entender cómo se ve un ecosistema de Praxia.",
    "p3_intro": ("Construidos con el mismo rigor que un encargo real. Web, back "
                  "office, simulador interactivo y modelo económico — todo tocable. "
                  "Cuando trabajamos contigo, esto se construye con tu marca, tus "
                  "números y tus protocolos."),
    "p3_cards": [
        ("BODEGA VALDESCURO", "FAMILY BUSINESS · VINO",
         "Tres generaciones haciendo vino. La cuarta abre un club privado y vehículo de coinversión.",
         f"{WEB_URL}/Praxia_Atelier_Caso_Bodega_Valdescuro.html"),
        ("CLÍNICA LUMEN", "HEALTH-TECH · LONGEVIDAD",
         "Medicina integrativa con membresía Plus, avatar Sofia y SaaS para practitioners.",
         f"{WEB_URL}/Praxia_Atelier_Caso_Clinica_Lumen.html"),
        ("CASA VENTO", "REAL ESTATE · RESIDENCIAL",
         "Operadora de pisos reformados con vehículo privado de coinversión y club de inquilinos.",
         f"{WEB_URL}/Praxia_Atelier_Caso_Casa_Vento.html"),
        ("MESA DE TRABAJO", "FOUNDER-CLIENTE · MÉTODO",
         "El método del estudio aplicado al propio estudio. Ocho departamentos diseñados con su misma lógica.",
         f"{WEB_URL}/Praxia_Atelier_Caso_Mesa_de_Trabajo.html"),
    ],
    "p3_btn_label": "Abrir caso",
    "p4_section_label": "QUÉ CONSTRUIMOS",
    "p4_kicker": "SIETE CÁPSULAS · PRECIO CERRADO",
    "p4_h1": "No vendemos horas.",
    "p4_h1_sub": "Cada cápsula tiene alcance, plazo y entregables fijos. Si no encajan, no hay propuesta.",
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
                    "de la factura del Blueprint."),
    "founder_kicker": "FUNDADORA",
    "founder_name": "Marta Escobar Rojas",
    "founder_sub": "MBA · Founder con IA en producción · Madrid",
    "cta_h1": "Treinta minutos.",
    "cta_h2": "Sin compromiso.",
    "cta_btn": "Reservar diagnóstico · 30 min",
    "cta_or": "O ESCRIBE A:",
}

COPY_EN = dict(COPY_ES)
COPY_EN.update({
    "kicker_top": "STUDIO · MADRID · 2026",
    "p1_h1_a": "We design digital",
    "p1_h1_b": "ecosystems",
    "p1_h1_b_accent": "ready to raise capital,",
    "p1_h1_c": "multiply ROI or, simply, to know what to do next week.",
    "p1_aterrizaje": ("We ground your idea and turn it into a real, digitalised "
                       "and optimised business — with operating system, website "
                       "and everything you need to start running."),
    "btn_primary": "Book 30 min with Marta",
    "btn_secondary": "See navigable cases",
    "btn_caption": "Free · No commitment",
    "idea_kicker": "IDEA WITHOUT GROUNDING",
    "idea_lead":   "You have a business intuition but you don't know where to start structuring it.",
    "idea_caption":"We start there — in a brainstorm we hand you real options.",
    "comp_kicker": "COMPANY · NEW LINE",
    "comp_lead":   "Your company works but you want to open a new line without cannibalising the core.",
    "comp_caption":"We design the next layer — complete, ready to operate.",
    "promise_kicker": "THE PROMISE",
    "promise_quote": ("Book thirty minutes and within 48 hours you receive a free "
                      "one-pager with three actionable moves specific to your project."),
    "promise_caption": "— No contract required · The value is yours even if we don't continue together",
    "stats_kicker": "THE FORMAT",
    "stats": [("10–15", "DAYS TO BLUEPRINT"),
              ("7",     "ENTITIES COORDINATED"),
              ("8",     "DISCIPLINES · ONE VOICE"),
              ("100%",  "NAVIGABLE PROTOTYPE")],
    "p2_section_label": "CASES · TRACK RECORD",
    "p2_kicker": "REAL PROJECT · 2025",
    "p2_h1_sub": "Boutique real estate · Madrid",
    "p2_block1_kicker": "WHAT CASAVERA NEEDED",
    "p2_block1_body": ("Casavera real estate wanted to stop running rentals, sales "
                       "and investment in Madrid with operations scattered across "
                       "four spreadsheets and email."),
    "p2_block2_kicker": "WHAT PRAXIA DELIVERED",
    "p2_block2_body": ("A digital ecosystem with two faces. The public website with "
                       "four entry doors — invest, sell, rent, search. And the custom "
                       "back office with a panoramic view of the ten business "
                       "processes: from catalogue to monthly projected cash flow."),
    "p2_pull_quote": "“A single source of truth — not four spreadsheets.”",
    "p2_link1_kicker": "PROTOTYPE A · INTERNAL",
    "p2_link1_label": "Operating system · back office",
    "p2_link2_kicker": "PROTOTYPE B · PUBLIC",
    "p2_link2_label": "Public website · 4 doors",
    "p2_layers_kicker": "LAYERS",
    "p2_layers": "PRODUCT · AI · MODEL · MARKETING · OPERATIONS · SALES",
    "p2_others_kicker": "OTHER PROJECTS · NO PUBLIC PROTOTYPE",
    "p2_others_1_t": "EdTech · emotional education",
    "p2_others_1_d": "AIE ecosystem with emotional education platform. Real case, anonymised for confidentiality.",
    "p2_others_2_t": "Own project · active",
    "p2_others_2_d": "Own emotional ecosystem with AI in production. Three lines (B2C · marketplace · enterprise).",
    "p3_section_label": "CASES · METHOD",
    "p3_kicker": "NAVIGABLE PROTOTYPES",
    "p3_h1": "Four cases.",
    "p3_h1_sub": "To understand what a Praxia ecosystem looks like.",
    "p3_intro": ("Built with the same rigour as a real engagement. Website, back "
                 "office, interactive simulator and economic model — all tactile. "
                 "When we work with you, this is built with your brand, your numbers "
                 "and your protocols."),
    "p3_cards": [
        ("BODEGA VALDESCURO", "FAMILY BUSINESS · WINE",
         "Three generations making wine. The fourth opens a private members club and co-investment vehicle.",
         f"{WEB_URL}/Praxia_Atelier_Caso_Bodega_Valdescuro.html"),
        ("CLÍNICA LUMEN", "HEALTH-TECH · LONGEVITY",
         "Integrative medicine with Plus membership, Sofia avatar and SaaS for practitioners.",
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
    "p4_h1_sub": "Each capsule has a defined scope, timeline and deliverables. If they don't fit, there's no proposal.",
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
                    "Sprint fee is deducted in full from the Blueprint invoice."),
    "founder_kicker": "FOUNDER",
    "founder_sub": "MBA · Founder with AI in production · Madrid",
    "cta_h1": "Thirty minutes.",
    "cta_h2": "No commitment.",
    "cta_btn": "Book diagnostic · 30 min",
    "cta_or": "OR WRITE TO:",
})


# ============================================================
# Page 1 · Hero
# ============================================================
def page1(c, t):
    is_es = t["kicker_top"].startswith("ESTUDIO")
    header_band(c, 1, 4)
    y = CONTENT_TOP - 4 * mm

    # Pill kicker
    pill_label = t["kicker_top"]
    pill_w = c.stringWidth(pill_label, F_MONO, 7) + 7 * mm
    c.setFillColor(ACCENT_SOFT)
    c.roundRect(MARGIN_X, y - 6 * mm, pill_w, 6 * mm, 3 * mm, stroke=0, fill=1)
    c.setFillColor(ACCENT); c.setFont(F_MONO, 7)
    c.drawString(MARGIN_X + 3.5 * mm, y - 4.2 * mm, pill_label)
    y -= 14 * mm

    # H1 lines · auto-shrink each one to fit CONTENT_W
    line_a_size = fit_size(c, t["p1_h1_a"], F_SERIF_BOLD, 32, 22, CONTENT_W)
    c.setFillColor(INK); c.setFont(F_SERIF_BOLD, line_a_size)
    c.drawString(MARGIN_X, y, t["p1_h1_a"])
    y -= line_a_size * 1.05 + 1 * mm

    line_b_size = fit_size(c, t["p1_h1_b"], F_SERIF_BOLD, 32, 22, CONTENT_W)
    c.setFont(F_SERIF_BOLD, line_b_size)
    c.drawString(MARGIN_X, y, t["p1_h1_b"])
    y -= line_b_size * 1.05 + 5 * mm

    # Accent line · "listos para captar capital,"
    line_acc_size = fit_size(c, t["p1_h1_b_accent"], F_SERIF_BOLD, 26, 18, CONTENT_W)
    c.setFillColor(ACCENT); c.setFont(F_SERIF_BOLD, line_acc_size)
    c.drawString(MARGIN_X, y, t["p1_h1_b_accent"])
    y -= line_acc_size * 1.1 + 4 * mm

    # Italic line · multi-line allowed
    italic_size = 16
    c.setFillColor(INK_SOFT); c.setFont(F_SERIF, italic_size)
    italic_lines = simpleSplit(t["p1_h1_c"], F_SERIF, italic_size, CONTENT_W)
    for ln in italic_lines:
        c.drawString(MARGIN_X, y, ln); y -= italic_size * 1.15
    y -= 8 * mm

    # Hairline
    c.setStrokeColor(ACCENT); c.setLineWidth(1)
    c.line(MARGIN_X, y, MARGIN_X + 28 * mm, y)
    y -= 8 * mm

    # Aterrizaje paragraph
    y = draw_text(c, t["p1_aterrizaje"], MARGIN_X, y, CONTENT_W,
                  F_SERIF, 11, INK, leading=16)
    y -= 9 * mm

    # CTAs
    btn_h = 12 * mm
    bw1 = c.stringWidth(t["btn_primary"], F_SANS_MED, 10.5) + 14 * mm
    draw_button(c, t["btn_primary"], CAL_URL,
                MARGIN_X, y - btn_h, bw1, btn_h,
                fill=ACCENT, text=PAPER, font_size=10.5, shadow=True, shadow_color=INK)
    bw2 = c.stringWidth(t["btn_secondary"], F_SANS_MED, 10) + 12 * mm
    draw_button(c, t["btn_secondary"], f"{WEB_URL}/#casos",
                MARGIN_X + bw1 + 5 * mm, y - btn_h, bw2, btn_h,
                fill=None, text=INK, border=INK, font_size=10)
    cap_x = MARGIN_X + bw1 + 5 * mm + bw2 + 6 * mm
    cap_y = y - btn_h + (btn_h / 2) - 2
    if cap_x + 50 * mm < PAGE_W - MARGIN_X:
        c.setFont(F_MONO, 7); c.setFillColor(INK_FAINT)
        c.drawString(cap_x, cap_y, "· " + t["btn_caption"].upper())
    y -= btn_h + 14 * mm

    # Idea / Empresa · two cards with proper padding
    card_w = (CONTENT_W - 1 * mm) / 2
    card_h = 38 * mm
    cy = y - card_h

    def draw_card(x, kicker, lead, caption, accent_color, num):
        c.setFillColor(white); c.rect(x, cy, card_w, card_h, stroke=0, fill=1)
        c.setFillColor(accent_color); c.rect(x, cy + card_h - 1.2 * mm, card_w, 1.2 * mm, stroke=0, fill=1)
        c.setStrokeColor(LINE); c.setLineWidth(0.4)
        c.rect(x, cy, card_w, card_h, stroke=1, fill=0)
        # Padding
        pad = 5 * mm
        cx = x + pad
        cyt = cy + card_h - 7 * mm
        # Kicker (top-left) and number (top-right) on the SAME line · keep clear
        c.setFont(F_MONO, 6.5); c.setFillColor(accent_color)
        c.drawString(cx, cyt, kicker)
        c.setFont(F_SERIF, 14); c.setFillColor(accent_color)
        nw = c.stringWidth(num, F_SERIF, 14)
        c.drawString(x + card_w - pad - nw, cyt, num)
        cyt -= 7 * mm
        # Lead serif · max 2 lines
        cyt = draw_text(c, lead, cx, cyt, card_w - 2 * pad,
                        F_SERIF, 11, INK, leading=14.5, max_lines=2)
        cyt -= 1 * mm
        # Caption sans soft · max 2 lines
        draw_text(c, caption, cx, cyt, card_w - 2 * pad,
                  F_SANS, 8.5, INK_SOFT, leading=11.5, max_lines=2)

    draw_card(MARGIN_X, t["idea_kicker"], t["idea_lead"], t["idea_caption"], ACCENT, "01")
    draw_card(MARGIN_X + card_w + 1 * mm, t["comp_kicker"], t["comp_lead"], t["comp_caption"], MOSS, "02")

    y = cy - 12 * mm

    # Pull quote
    c.setFont(F_MONO, 6.5); c.setFillColor(ACCENT)
    c.drawString(MARGIN_X, y, t["promise_kicker"])
    y -= 6 * mm
    quote_lines = simpleSplit(t["promise_quote"], F_SERIF, 12.5, CONTENT_W)
    c.setFillColor(INK); c.setFont(F_SERIF, 12.5)
    for ln in quote_lines:
        c.drawString(MARGIN_X, y, ln); y -= 6.5 * mm
    y -= 1 * mm
    c.setFont(F_MONO, 6.5); c.setFillColor(INK_SOFT)
    cap = t["promise_caption"]
    # Auto-truncate caption if too wide
    while c.stringWidth(cap, F_MONO, 6.5) > CONTENT_W - 2*mm and len(cap) > 5:
        cap = cap[:-2]
    c.drawString(MARGIN_X, y, cap)
    y -= 11 * mm

    # Stat band — controlled
    if y > CONTENT_BOT + 30 * mm:
        c.setFont(F_MONO, 6.5); c.setFillColor(ACCENT)
        c.drawString(MARGIN_X, y, t["stats_kicker"])
        y -= 4 * mm
        hr(c, MARGIN_X, y, PAGE_W - MARGIN_X, INK, 0.7)
        y -= 12 * mm
        cell_w = CONTENT_W / 4
        for i, (big, small) in enumerate(t["stats"]):
            ax = MARGIN_X + i * cell_w + 4 * mm  # extra inner pad
            col = ACCENT if i in (1, 3) else INK
            c.setFillColor(col); c.setFont(F_SERIF_BOLD, 26)
            c.drawString(ax, y, big)
            c.setFont(F_MONO, 5.8); c.setFillColor(INK_FAINT)
            c.drawString(ax, y - 5 * mm, small)
        y -= 9 * mm
        hr(c, MARGIN_X, y, PAGE_W - MARGIN_X, INK, 0.7)

    footer_band(c, lang="es" if is_es else "en")


# ============================================================
# Page 2 · Casavera
# ============================================================
def page2(c, t):
    is_es = t["p2_kicker"].startswith("PROYECTO")
    header_band(c, 2, 4)

    y = CONTENT_TOP - 4 * mm
    # Section header line: '02 · CASOS · TRAYECTORIA'
    y = section_kicker(c, y, "02", t["p2_section_label"])

    # Title block — full width
    c.setFont(F_MONO, 6.5); c.setFillColor(ACCENT)
    c.drawString(MARGIN_X, y, t["p2_kicker"])
    y -= 9 * mm
    h1_size = fit_size(c, t["p2_h1"], F_SERIF_BOLD, 38, 26, CONTENT_W)
    c.setFont(F_SERIF_BOLD, h1_size); c.setFillColor(INK)
    c.drawString(MARGIN_X, y, t["p2_h1"])
    y -= h1_size * 0.9 + 3 * mm
    c.setFont(F_SERIF, 13); c.setFillColor(INK_SOFT)
    c.drawString(MARGIN_X, y, t["p2_h1_sub"])
    y -= 14 * mm

    # Two columns
    col_w = (CONTENT_W - 8 * mm) / 2
    # Left
    c.setFont(F_MONO, 6.5); c.setFillColor(ACCENT)
    c.drawString(MARGIN_X, y, t["p2_block1_kicker"])
    yy_l = draw_text(c, t["p2_block1_body"], MARGIN_X, y - 6 * mm,
                     col_w, F_SERIF, 10.5, INK, leading=14.5)
    # Right
    rx = MARGIN_X + col_w + 8 * mm
    c.setFont(F_MONO, 6.5); c.setFillColor(ACCENT)
    c.drawString(rx, y, t["p2_block2_kicker"])
    yy_r = draw_text(c, t["p2_block2_body"], rx, y - 6 * mm,
                     col_w, F_SERIF, 10.5, INK, leading=14.5)
    y = min(yy_l, yy_r) - 12 * mm

    # Pull quote · auto-shrink
    pq = t["p2_pull_quote"]
    pq_size = fit_size(c, pq, F_SERIF, 16, 11, CONTENT_W - 10*mm)
    c.setFont(F_SERIF, pq_size); c.setFillColor(ACCENT)
    pqw = c.stringWidth(pq, F_SERIF, pq_size)
    c.drawString((PAGE_W - pqw) / 2, y, pq)
    y -= 14 * mm

    # Two action buttons
    btn_h = 13 * mm
    bw = (CONTENT_W - 8 * mm) / 2
    c.setFont(F_MONO, 6.5); c.setFillColor(ACCENT)
    c.drawString(MARGIN_X, y, t["p2_link1_kicker"])
    draw_button(c, t["p2_link1_label"], "https://resilient-arithmetic-182add.netlify.app/",
                MARGIN_X, y - btn_h - 5 * mm, bw, btn_h,
                fill=INK, text=PAPER, font_size=10, shadow=True, shadow_color=ACCENT)
    c.setFont(F_MONO, 6.5); c.setFillColor(ACCENT)
    c.drawString(MARGIN_X + bw + 8 * mm, y, t["p2_link2_kicker"])
    draw_button(c, t["p2_link2_label"], "https://rococo-sawine-40e557.netlify.app/",
                MARGIN_X + bw + 8 * mm, y - btn_h - 5 * mm, bw, btn_h,
                fill=INK, text=PAPER, font_size=10, shadow=True, shadow_color=ACCENT)
    y -= btn_h + 14 * mm

    # Layers tag · auto-fit
    layers_text = t["p2_layers_kicker"] + " · " + t["p2_layers"]
    layers_size = fit_size(c, layers_text, F_MONO, 6.5, 5.5, CONTENT_W)
    c.setFont(F_MONO, layers_size); c.setFillColor(INK_FAINT)
    c.drawString(MARGIN_X, y, layers_text)
    y -= 9 * mm
    hr(c, MARGIN_X, y, PAGE_W - MARGIN_X, LINE)
    y -= 7 * mm

    # Other projects
    c.setFont(F_MONO, 6.5); c.setFillColor(INK_FAINT)
    c.drawString(MARGIN_X, y, t["p2_others_kicker"])
    y -= 6 * mm
    o_col_w = (CONTENT_W - 8 * mm) / 2
    others = [(t["p2_others_1_t"], t["p2_others_1_d"]),
              (t["p2_others_2_t"], t["p2_others_2_d"])]
    for i, (oname, obody) in enumerate(others):
        ox = MARGIN_X + i * (o_col_w + 8 * mm)
        c.setFont(F_SERIF_BOLD, 11); c.setFillColor(INK)
        c.drawString(ox, y, oname)
        draw_text(c, obody, ox, y - 5 * mm, o_col_w,
                  F_SANS, 8.5, INK_SOFT, leading=12, max_lines=3)

    footer_band(c, lang="es" if is_es else "en")


# ============================================================
# Page 3 · 4 cases
# ============================================================
def page3(c, t):
    is_es = t["p3_section_label"].startswith("CASOS")
    header_band(c, 3, 4)

    y = CONTENT_TOP - 4 * mm
    y = section_kicker(c, y, "03", t["p3_section_label"])

    c.setFont(F_MONO, 6.5); c.setFillColor(ACCENT)
    c.drawString(MARGIN_X, y, t["p3_kicker"])
    y -= 9 * mm
    h1_size = fit_size(c, t["p3_h1"], F_SERIF_BOLD, 32, 22, CONTENT_W)
    c.setFont(F_SERIF_BOLD, h1_size); c.setFillColor(INK)
    c.drawString(MARGIN_X, y, t["p3_h1"])
    y -= h1_size * 0.9 + 3 * mm
    c.setFont(F_SERIF, 12); c.setFillColor(INK_SOFT)
    sub_lines = simpleSplit(t["p3_h1_sub"], F_SERIF, 12, CONTENT_W)
    for ln in sub_lines:
        c.drawString(MARGIN_X, y, ln); y -= 6 * mm
    y -= 4 * mm

    # Intro
    y = draw_text(c, t["p3_intro"], MARGIN_X, y, CONTENT_W,
                  F_SANS, 10, INK_SOFT, leading=14)
    y -= 8 * mm

    # 4 cards 2x2
    case_w = (CONTENT_W - 8 * mm) / 2
    case_h = 56 * mm
    for i, (name, sector, blurb, url) in enumerate(t["p3_cards"]):
        col = i % 2; row = i // 2
        cx = MARGIN_X + col * (case_w + 8 * mm)
        cy = y - row * (case_h + 6 * mm) - case_h
        c.setStrokeColor(INK); c.setLineWidth(0.8)
        c.line(cx, cy + case_h, cx + case_w, cy + case_h)
        c.setFont(F_MONO, 6.5); c.setFillColor(ACCENT)
        c.drawString(cx, cy + case_h - 5 * mm, sector)
        # Name auto-shrink to card width
        name_size = fit_size(c, name, F_SERIF_BOLD, 16, 12, case_w)
        c.setFont(F_SERIF_BOLD, name_size); c.setFillColor(INK)
        c.drawString(cx, cy + case_h - 13 * mm, name)
        draw_text(c, blurb, cx, cy + case_h - 21 * mm, case_w,
                  F_SANS, 9, INK_SOFT, leading=12.5, max_lines=4)
        draw_button(c, t["p3_btn_label"] + " →", url,
                    cx, cy + 4 * mm, 30 * mm, 8 * mm,
                    fill=None, text=ACCENT, border=ACCENT, font_size=8.5)

    footer_band(c, lang="es" if is_es else "en")


# ============================================================
# Page 4 · capsules + final CTA
# ============================================================
def page4(c, t):
    is_es = t["p4_section_label"].startswith("QUÉ")
    header_band(c, 4, 4)

    y = CONTENT_TOP - 4 * mm
    y = section_kicker(c, y, "04", t["p4_section_label"])

    c.setFont(F_MONO, 6.5); c.setFillColor(ACCENT)
    c.drawString(MARGIN_X, y, t["p4_kicker"])
    y -= 9 * mm
    h1_size = fit_size(c, t["p4_h1"], F_SERIF_BOLD, 30, 22, CONTENT_W)
    c.setFont(F_SERIF_BOLD, h1_size); c.setFillColor(INK)
    c.drawString(MARGIN_X, y, t["p4_h1"])
    y -= h1_size * 0.9 + 3 * mm
    c.setFont(F_SERIF, 12); c.setFillColor(INK_SOFT)
    sub_lines = simpleSplit(t["p4_h1_sub"], F_SERIF, 12, CONTENT_W)
    for ln in sub_lines:
        c.drawString(MARGIN_X, y, ln); y -= 6 * mm
    y -= 8 * mm

    # Capsules table
    hr(c, MARGIN_X, y + 3 * mm, PAGE_W - MARGIN_X, INK, 0.8)
    row_h = 9.5 * mm
    for num, name, when, price in t["capsules"]:
        is_pack = (num == "PACK")
        if is_pack:
            c.setFillColor(ACCENT_SOFT)
            c.rect(MARGIN_X, y - row_h + 0.6 * mm, CONTENT_W, row_h - 0.6 * mm, stroke=0, fill=1)
        c.setFont(F_MONO, 8.5); c.setFillColor(ACCENT_DEEP if is_pack else ACCENT)
        c.drawString(MARGIN_X + 2 * mm, y - 6.5 * mm, num)
        c.setFont(F_SERIF_BOLD, 11); c.setFillColor(INK)
        c.drawString(MARGIN_X + 26 * mm, y - 6.5 * mm, name)
        c.setFont(F_MONO, 7); c.setFillColor(INK_SOFT)
        c.drawString(MARGIN_X + 100 * mm, y - 6.5 * mm, when.upper())
        c.setFont(F_SANS_MED, 9.5); c.setFillColor(INK)
        pw = c.stringWidth(price, F_SANS_MED, 9.5)
        c.drawString(PAGE_W - MARGIN_X - pw - 2 * mm, y - 6.5 * mm, price)
        y -= row_h
        if not is_pack:
            hr(c, MARGIN_X, y, PAGE_W - MARGIN_X, LINE, 0.4)
    y -= 8 * mm

    # Honest trick — compact
    th = 18 * mm
    c.setFillColor(ACCENT_SOFT)
    c.rect(MARGIN_X, y - th, CONTENT_W, th, stroke=0, fill=1)
    c.setFillColor(ACCENT); c.rect(MARGIN_X, y - th, 1.2 * mm, th, stroke=0, fill=1)
    c.setFont(F_MONO, 6.5); c.setFillColor(ACCENT_DEEP)
    c.drawString(MARGIN_X + 7 * mm, y - 4.5 * mm, t["trick_kicker"])
    draw_text(c, t["trick_body"], MARGIN_X + 7 * mm, y - 10 * mm,
              CONTENT_W - 14 * mm, F_SERIF, 10, INK, leading=13.5, max_lines=2)
    y -= th + 10 * mm

    # Founder
    c.setFont(F_MONO, 6.5); c.setFillColor(INK_FAINT)
    c.drawString(MARGIN_X, y, t["founder_kicker"])
    c.setFont(F_SERIF_BOLD, 18); c.setFillColor(INK)
    c.drawString(MARGIN_X, y - 7.5 * mm, t["founder_name"])
    c.setFont(F_SANS, 9); c.setFillColor(INK_SOFT)
    c.drawString(MARGIN_X, y - 12 * mm, t["founder_sub"])
    y -= 18 * mm

    # CTA black band — RESERVE the space, place above footer with margin
    cta_h = 32 * mm
    cta_top = y - 2 * mm
    cta_bot = cta_top - cta_h
    # Make sure footer doesn't overlap (footer band starts at MARGIN_BOT)
    if cta_bot < MARGIN_BOT + 6 * mm:
        cta_bot = MARGIN_BOT + 6 * mm
        cta_top = cta_bot + cta_h
    c.setFillColor(INK)
    c.rect(MARGIN_X, cta_bot, CONTENT_W, cta_h, stroke=0, fill=1)
    # Title
    c.setFillColor(PAPER); c.setFont(F_SERIF_BOLD, 18)
    c.drawString(MARGIN_X + 7 * mm, cta_top - 8 * mm, t["cta_h1"])
    c.setFont(F_SERIF, 18); c.setFillColor(ACCENT_SOFT)
    c.drawString(MARGIN_X + 7 * mm, cta_top - 14 * mm, t["cta_h2"])
    # Button
    btn_w = 56 * mm; btn_h = 9 * mm
    btn_x = MARGIN_X + 7 * mm
    btn_y = cta_bot + 5 * mm
    draw_button(c, t["cta_btn"], CAL_URL,
                btn_x, btn_y, btn_w, btn_h,
                fill=ACCENT, text=PAPER, font_size=9.5)
    # Email · placed as a separate line, NEVER overlapping
    em_x = btn_x + btn_w + 8 * mm
    c.setFont(F_MONO, 6.5); c.setFillColor(PAPER_DEEP)
    c.drawString(em_x, btn_y + 5 * mm, t["cta_or"])
    c.setFont(F_SANS_MED, 9.5); c.setFillColor(PAPER)
    c.drawString(em_x, btn_y + 0.5 * mm, EMAIL)
    em_w = c.stringWidth(EMAIL, F_SANS_MED, 9.5)
    c.linkURL(EMAIL_HREF, (em_x, btn_y - 1 * mm, em_x + em_w, btn_y + 8 * mm), relative=0, thickness=0)

    footer_band(c, lang="es" if is_es else "en")


# ============================================================
# Build
# ============================================================
def build(out_path, lang="es"):
    t = COPY_ES if lang == "es" else COPY_EN
    c = canvas_module.Canvas(out_path, pagesize=A4)
    c.setTitle("Praxia Atelier · " + ("Servicios" if lang == "es" else "Services"))
    c.setAuthor("Marta Escobar Rojas")
    c.setSubject("Estudio de arquitectura de ecosistemas digitales · Servicios y casos")
    c.setCreator("Praxia Atelier")
    page1(c, t); c.showPage()
    page2(c, t); c.showPage()
    page3(c, t); c.showPage()
    page4(c, t); c.showPage()
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
