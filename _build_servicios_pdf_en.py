"""Build Praxia_Atelier_Services.pdf — English version, identical layout
to the Spanish one but with translated copy. 18 clickable links preserved.
"""
from pathlib import Path
import sys

# Reuse the structure of the ES builder
sys.path.insert(0, ".")
import _build_servicios_pdf as base
from _build_servicios_pdf import (
    INK, INK_SOFT, PAPER, LINE, ACCENT, ACCENT_SOFT, white,
    PAGE_W, PAGE_H, MARGIN_X, MARGIN_Y,
    FONT_SERIF, FONT_SERIF_REG, FONT_SANS, FONT_SANS_BOLD, FONT_MONO,
    CAL_URL, WEB_URL, EMAIL, EMAIL_HREF,
    draw_text_block, draw_link_button, draw_text_link,
)
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas as canvas_module
from reportlab.lib.utils import simpleSplit
from reportlab.lib.colors import HexColor

CASES_REAL_EN = [
    {
        "tag": "Real client · 2025",
        "name": "Casavera",
        "tagline": "Boutique real estate · Madrid",
        "needed": "To stop running rentals, sales and investment with operations scattered across four spreadsheets and email.",
        "delivered": "A digital ecosystem with two faces: public website with 4 entry doors + back office with a panoramic view of the 10 business processes.",
        "links": [
            ("Operating system · back office (internal)",
             "https://resilient-arithmetic-182add.netlify.app/"),
            ("Public website · 4 entry doors (client)",
             "https://rococo-sawine-40e557.netlify.app/"),
        ],
    },
]

CASES_DEMO_EN = [
    {
        "name": "Bodega Valdescuro",
        "sector": "Family business · wine",
        "blurb": "Three generations making wine. The fourth opens a private members club and co-investment vehicle.",
        "url": f"{WEB_URL}/Praxia_Atelier_Caso_Bodega_Valdescuro.html",
        "color": HexColor("#6b1d23"),
    },
    {
        "name": "Clínica Lumen",
        "sector": "Health-tech · longevity",
        "blurb": "Integrative longevity medicine with Plus membership, Sofia avatar and SaaS for practitioners.",
        "url": f"{WEB_URL}/Praxia_Atelier_Caso_Clinica_Lumen.html",
        "color": HexColor("#0e2a26"),
    },
    {
        "name": "Casa Vento",
        "sector": "Real estate · residential",
        "blurb": "Operator of refurbished apartments with a private co-investment vehicle and tenants' club.",
        "url": f"{WEB_URL}/Praxia_Atelier_Caso_Casa_Vento.html",
        "color": HexColor("#1a2733"),
    },
    {
        "name": "Mesa de Trabajo",
        "sector": "Founder-client · method applied",
        "blurb": "The studio's method applied to the studio itself. Praxia's 8 departments designed with its own logic.",
        "url": f"{WEB_URL}/Praxia_Atelier_Caso_Mesa_de_Trabajo.html",
        "color": HexColor("#2a1f15"),
    },
]

CAPSULES_EN = [
    ("00", "Strategy Sprint",       "1 week",        "990 – 2,500 €"),
    ("01", "Ecosystem Blueprint",   "10–15 days",    "12,000 – 18,000 €"),
    ("02", "Ecosystem Build",       "3–5 months",    "60,000 – 120,000 €"),
    ("03", "Ecosystem Operate",     "recurring",     "5,500 – 8,000 €/month"),
    ("04/05/06", "Marketing · Ops · Sales", "2–3 wk", "6,500 – 9,500 €"),
    ("PACK", "GTM (04+05+06 integrated)", "5 wk",    "18,000 € · save 4,500 €"),
]


def header(c, page_num, total_pages):
    c.setFillColor(PAPER)
    c.rect(0, 0, PAGE_W, PAGE_H, stroke=0, fill=1)
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
    c.setFont(FONT_MONO, 8)
    c.setFillColor(INK_SOFT)
    label = f"{page_num:02d} / {total_pages:02d}"
    tw = c.stringWidth(label, FONT_MONO, 8)
    c.drawString(PAGE_W - MARGIN_X - tw, PAGE_H - MARGIN_Y - 4*mm, label)
    c.setStrokeColor(LINE)
    c.setLineWidth(0.5)
    c.line(MARGIN_X, PAGE_H - MARGIN_Y - 11*mm, PAGE_W - MARGIN_X, PAGE_H - MARGIN_Y - 11*mm)


def footer(c):
    y = MARGIN_Y - 4*mm
    c.setStrokeColor(LINE); c.setLineWidth(0.5)
    c.line(MARGIN_X, MARGIN_Y, PAGE_W - MARGIN_X, MARGIN_Y)
    c.setFont(FONT_MONO, 8); c.setFillColor(INK_SOFT)
    c.drawString(MARGIN_X, y, "STUDIO · MADRID · 2026")
    web_label = WEB_URL.replace("https://", "").upper()
    web_w = c.stringWidth(web_label, FONT_MONO, 8)
    web_x = (PAGE_W - web_w) / 2
    c.setFillColor(INK)
    c.drawString(web_x, y, web_label)
    c.linkURL(WEB_URL, (web_x, y - 1, web_x + web_w, y + 8), relative=0, thickness=0)
    em_label = EMAIL.upper()
    em_w = c.stringWidth(em_label, FONT_MONO, 8)
    em_x = PAGE_W - MARGIN_X - em_w
    c.drawString(em_x, y, em_label)
    c.linkURL(EMAIL_HREF, (em_x, y - 1, em_x + em_w, y + 8), relative=0, thickness=0)


def build_en(out_path):
    c = canvas_module.Canvas(out_path, pagesize=A4)
    c.setTitle("Praxia Atelier · Services")
    c.setAuthor("Marta Escobar Rojas")
    c.setSubject("Studio of digital ecosystem architecture · Services and cases")
    c.setCreator("Praxia Atelier")

    TOTAL = 4
    content_w = PAGE_W - 2*MARGIN_X

    # ---------- PAGE 1 ----------
    header(c, 1, TOTAL)
    y = PAGE_H - MARGIN_Y - 22*mm
    c.setFillColor(ACCENT_SOFT)
    label = "STUDIO · MADRID · 2026"
    pill_w = c.stringWidth(label, FONT_MONO, 8) + 6*mm
    c.roundRect(MARGIN_X, y, pill_w, 6*mm, 3*mm, stroke=0, fill=1)
    c.setFillColor(ACCENT); c.setFont(FONT_MONO, 8)
    c.drawString(MARGIN_X + 3*mm, y + 1.8*mm, label)
    y -= 12*mm

    c.setFillColor(INK); c.setFont(FONT_SERIF, 28)
    c.drawString(MARGIN_X, y, "We design digital ecosystems")
    y -= 11*mm
    c.setFillColor(ACCENT)
    c.drawString(MARGIN_X, y, "ready to raise capital")
    c.setFillColor(INK)
    base_w = c.stringWidth("ready to raise capital", FONT_SERIF, 28)
    c.drawString(MARGIN_X + base_w, y, "  or multiply your ROI.")
    y -= 14*mm

    body = ("If you only have the idea, we start there. If you already have a company, "
            "we design the next layer. Legal-tax structure, software, AI avatar, "
            "economic model and investor materials — one studio, one voice.")
    y = draw_text_block(c, body, MARGIN_X, y, content_w, FONT_SANS, 11, INK_SOFT, leading=15)
    y -= 6*mm

    btn_w = 65*mm; btn_h = 11*mm
    draw_link_button(c, "Book 30 min with Marta · free", CAL_URL,
                     MARGIN_X, y - btn_h, btn_w, btn_h,
                     fill_color=INK, text_color=PAPER, font_size=11)
    draw_link_button(c, "See navigable cases", f"{WEB_URL}/#casos",
                     MARGIN_X + btn_w + 4*mm, y - btn_h, 45*mm, btn_h,
                     fill_color=None, text_color=INK, border_color=INK, font_size=10)
    y -= btn_h + 3*mm
    c.setFont(FONT_MONO, 8); c.setFillColor(INK_SOFT)
    c.drawString(MARGIN_X, y, "· NO COST · NO COMMITMENT ·")
    y -= 14*mm

    c.setFillColor(ACCENT)
    c.rect(MARGIN_X, y - 22*mm, 0.8*mm, 22*mm, stroke=0, fill=1)
    promise = ("Book 30 min and within 48h you receive a free one-pager with three "
               "actionable moves specific to your project. No contract required — the "
               "value is yours even if we don't continue together.")
    draw_text_block(c, promise, MARGIN_X + 4*mm, y - 4*mm, content_w - 4*mm, FONT_SANS, 10, INK, leading=14)
    y -= 30*mm

    stats = [("10–15", "DAYS TO BLUEPRINT"),
             ("7", "ENTITIES COORDINATED"),
             ("8", "DISCIPLINES · ONE VOICE"),
             ("100%", "NAVIGABLE PROTOTYPE")]
    cell_w = content_w / 4
    for i, (big, small) in enumerate(stats):
        cx = MARGIN_X + i * cell_w
        c.setFillColor(INK); c.setFont(FONT_SERIF, 22)
        c.drawString(cx, y - 8*mm, big)
        c.setFont(FONT_MONO, 6.5); c.setFillColor(INK_SOFT)
        c.drawString(cx, y - 13*mm, small)
        if i < 3:
            c.setStrokeColor(LINE); c.setLineWidth(0.5)
            c.line(cx + cell_w - 2*mm, y - 14*mm, cx + cell_w - 2*mm, y)
    y -= 22*mm

    c.setFont(FONT_MONO, 8); c.setFillColor(ACCENT)
    c.drawString(MARGIN_X, y, "HOW THE PROCESS WORKS")
    y -= 6*mm
    c.setFont(FONT_SERIF, 16); c.setFillColor(INK)
    c.drawString(MARGIN_X, y, "Same method, two entry points.")
    y -= 8*mm
    process = [("Day 0", "Brainstorm to understand your business."),
               ("Day 1", "We propose options."),
               ("Days 2–10", "We design the ecosystem."),
               ("Day 15", "You leave with the blueprints.")]
    pcell_w = content_w / 4
    for i, (when, what) in enumerate(process):
        cx = MARGIN_X + i * pcell_w
        c.setFont(FONT_MONO, 7); c.setFillColor(ACCENT)
        c.drawString(cx, y - 5*mm, when.upper())
        c.setFont(FONT_SERIF, 11); c.setFillColor(INK)
        for j, line in enumerate(simpleSplit(what, FONT_SERIF, 11, pcell_w - 3*mm)):
            c.drawString(cx, y - 10*mm - j * 4*mm, line)

    footer(c); c.showPage()

    # ---------- PAGE 2 ----------
    header(c, 2, TOTAL)
    y = PAGE_H - MARGIN_Y - 22*mm
    c.setFont(FONT_MONO, 8); c.setFillColor(ACCENT)
    c.drawString(MARGIN_X, y, "CASES · BLOCK 1 · TRACK RECORD")
    y -= 7*mm
    c.setFont(FONT_SERIF, 22); c.setFillColor(INK)
    c.drawString(MARGIN_X, y, "Real projects with real clients.")
    y -= 8*mm
    intro = ("Praxia Atelier opens in 2026, but the method has been built by designing "
             "and operating real projects. Those with a public prototype are fully navigable.")
    y = draw_text_block(c, intro, MARGIN_X, y, content_w, FONT_SANS, 10, INK_SOFT, leading=14)
    y -= 5*mm

    box_h = 110*mm
    box_y = y - box_h
    c.setFillColor(ACCENT)
    c.rect(MARGIN_X, y - 6*mm, content_w, 6*mm, stroke=0, fill=1)
    c.setFillColor(white); c.setFont(FONT_MONO, 7.5)
    c.drawString(MARGIN_X + 3*mm, y - 4.4*mm, "FEATURED · REAL PROJECT · 2025")
    c.setFillColor(white)
    c.rect(MARGIN_X, box_y, content_w, box_h - 6*mm, stroke=0, fill=1)
    c.setStrokeColor(LINE); c.setLineWidth(0.5)
    c.rect(MARGIN_X, box_y, content_w, box_h - 6*mm, stroke=1, fill=0)

    inner_x = MARGIN_X + 6*mm
    inner_y = y - 12*mm
    inner_w = content_w - 12*mm

    case = CASES_REAL_EN[0]
    c.setFont(FONT_MONO, 7); c.setFillColor(INK_SOFT)
    c.drawString(inner_x, inner_y, case["tagline"].upper())
    inner_y -= 7*mm
    c.setFont(FONT_SERIF, 19); c.setFillColor(INK)
    c.drawString(inner_x, inner_y, case["name"])
    name_w = c.stringWidth(case["name"], FONT_SERIF, 19)
    c.setFillColor(INK_SOFT)
    c.drawString(inner_x + name_w + 3*mm, inner_y, "· boutique real estate")
    inner_y -= 9*mm

    c.setFont(FONT_MONO, 7); c.setFillColor(ACCENT)
    c.drawString(inner_x, inner_y, "WHAT CASAVERA NEEDED")
    inner_y -= 5*mm
    inner_y = draw_text_block(c, case["needed"], inner_x, inner_y, inner_w, FONT_SANS, 10, INK, leading=14)
    inner_y -= 4*mm

    c.setFont(FONT_MONO, 7); c.setFillColor(ACCENT)
    c.drawString(inner_x, inner_y, "WHAT PRAXIA DELIVERED")
    inner_y -= 5*mm
    inner_y = draw_text_block(c, case["delivered"], inner_x, inner_y, inner_w, FONT_SANS, 10, INK, leading=14)
    inner_y -= 6*mm

    c.setFont(FONT_MONO, 7); c.setFillColor(INK_SOFT)
    c.drawString(inner_x, inner_y, "TWO NAVIGABLE PROTOTYPES")
    inner_y -= 6*mm
    btn_h = 9*mm
    btn_w = (inner_w - 4*mm) / 2
    for i, (label, url) in enumerate(case["links"]):
        bx = inner_x + i * (btn_w + 4*mm)
        draw_link_button(c, label, url, bx, inner_y - btn_h, btn_w, btn_h,
                         fill_color=INK, text_color=PAPER, font_size=8.5)
    inner_y -= btn_h + 4*mm
    c.setFont(FONT_MONO, 6.5); c.setFillColor(ACCENT)
    c.drawString(inner_x, inner_y, "LAYERS · PRODUCT + AI + MODEL + MARKETING + OPERATIONS + SALES")

    y = box_y - 8*mm
    c.setFont(FONT_MONO, 7.5); c.setFillColor(INK_SOFT)
    c.drawString(MARGIN_X, y, "OTHER PROJECTS · NO PUBLIC PROTOTYPE")
    y -= 6*mm
    others = [
        ("EdTech · emotional education", "AIE ecosystem with emotional education platform · 8 layers · design and grounding"),
        ("Own project · active",         "Own emotional ecosystem with AI in production · 3 lines (B2C / marketplace / enterprise)"),
    ]
    for title, desc in others:
        c.setFont(FONT_SANS_BOLD, 9); c.setFillColor(INK)
        c.drawString(MARGIN_X, y, title)
        y -= 4.5*mm
        y = draw_text_block(c, desc, MARGIN_X, y, content_w, FONT_SANS, 9, INK_SOFT, leading=13, max_lines=2)
        y -= 2*mm

    footer(c); c.showPage()

    # ---------- PAGE 3 ----------
    header(c, 3, TOTAL)
    y = PAGE_H - MARGIN_Y - 22*mm
    c.setFont(FONT_MONO, 8); c.setFillColor(ACCENT)
    c.drawString(MARGIN_X, y, "CASES · BLOCK 2 · TO UNDERSTAND THE METHOD")
    y -= 7*mm
    c.setFont(FONT_SERIF, 22); c.setFillColor(INK)
    c.drawString(MARGIN_X, y, "Fictional navigable prototypes.")
    y -= 8*mm
    intro = ("Built with the same rigour as a real engagement. Website, back office, "
             "interactive simulator and economic model — all tactile. When we work "
             "with you, this is built with your brand, your numbers and your protocols.")
    y = draw_text_block(c, intro, MARGIN_X, y, content_w, FONT_SANS, 10, INK_SOFT, leading=14)
    y -= 6*mm

    case_w = (content_w - 6*mm) / 2
    case_h = 60*mm
    for i, dc in enumerate(CASES_DEMO_EN):
        col = i % 2; row = i // 2
        cx = MARGIN_X + col * (case_w + 6*mm)
        cy = y - row * (case_h + 6*mm) - case_h
        c.setFillColor(dc["color"])
        c.rect(cx, cy + case_h - 14*mm, case_w, 14*mm, stroke=0, fill=1)
        c.setFillColor(white); c.setFont(FONT_MONO, 6.5)
        c.drawString(cx + 4*mm, cy + case_h - 5*mm, dc["sector"].upper())
        c.setFont(FONT_SERIF, 14)
        c.drawString(cx + 4*mm, cy + case_h - 11*mm, dc["name"])
        c.setFillColor(white)
        c.rect(cx, cy, case_w, case_h - 14*mm, stroke=0, fill=1)
        c.setStrokeColor(LINE); c.setLineWidth(0.5)
        c.rect(cx, cy, case_w, case_h, stroke=1, fill=0)
        draw_text_block(c, dc["blurb"], cx + 4*mm, cy + case_h - 19*mm, case_w - 8*mm,
                        FONT_SANS, 9, INK_SOFT, leading=12, max_lines=4)
        draw_link_button(c, "Open navigable case →", dc["url"],
                         cx + 4*mm, cy + 4*mm, case_w - 8*mm, 7*mm,
                         fill_color=None, text_color=ACCENT, border_color=ACCENT, font_size=8.5)
    y -= 2 * (case_h + 6*mm) + 6*mm

    note = ("These four cases are fictional. They show exactly what Praxia’s deliverable "
            "looks like: legal structure, software, navigable mockups, economic model and "
            "interactive simulator — before you commit to anything.")
    y = draw_text_block(c, note, MARGIN_X, y, content_w, FONT_SANS, 9, INK_SOFT, leading=13)

    footer(c); c.showPage()

    # ---------- PAGE 4 ----------
    header(c, 4, TOTAL)
    y = PAGE_H - MARGIN_Y - 22*mm
    c.setFont(FONT_MONO, 8); c.setFillColor(ACCENT)
    c.drawString(MARGIN_X, y, "WHAT WE BUILD · CUSTOM TECHNOLOGY")
    y -= 7*mm
    c.setFont(FONT_SERIF, 22); c.setFillColor(INK)
    c.drawString(MARGIN_X, y, "Seven capsules. Closed price.")
    y -= 8*mm
    intro = ("We don’t sell hours. Each capsule has a defined scope, timeline and "
             "deliverables. If they don’t fit, there’s no proposal.")
    y = draw_text_block(c, intro, MARGIN_X, y, content_w, FONT_SANS, 10, INK_SOFT, leading=14)
    y -= 4*mm

    row_h = 12*mm
    for num, name, when, price in CAPSULES_EN:
        if num == "PACK":
            c.setFillColor(ACCENT_SOFT)
            c.rect(MARGIN_X, y - row_h, content_w, row_h, stroke=0, fill=1)
        else:
            c.setStrokeColor(LINE); c.setLineWidth(0.5)
            c.line(MARGIN_X, y, PAGE_W - MARGIN_X, y)
        c.setFont(FONT_MONO, 9); c.setFillColor(ACCENT)
        c.drawString(MARGIN_X + 2*mm, y - 7*mm, num)
        c.setFont(FONT_SERIF, 12); c.setFillColor(INK)
        c.drawString(MARGIN_X + 22*mm, y - 7*mm, name)
        c.setFont(FONT_MONO, 8); c.setFillColor(INK_SOFT)
        c.drawString(MARGIN_X + 95*mm, y - 7*mm, when.upper())
        c.setFont(FONT_SANS_BOLD, 10); c.setFillColor(INK)
        pw = c.stringWidth(price, FONT_SANS_BOLD, 10)
        c.drawString(PAGE_W - MARGIN_X - pw - 2*mm, y - 7*mm, price)
        y -= row_h
    c.setStrokeColor(LINE); c.line(MARGIN_X, y, PAGE_W - MARGIN_X, y)
    y -= 12*mm

    c.setFillColor(ACCENT)
    c.rect(MARGIN_X, y - 16*mm, 0.8*mm, 16*mm, stroke=0, fill=1)
    c.setFont(FONT_MONO, 7); c.setFillColor(ACCENT)
    c.drawString(MARGIN_X + 4*mm, y - 4*mm, "HONEST TRICK")
    truco = ("If after the Sprint you book Capsule 01 within 30 days, the Sprint fee is "
             "deducted in full from the Blueprint invoice. In practice, the Sprint is "
             "free if we move forward.")
    draw_text_block(c, truco, MARGIN_X + 4*mm, y - 9*mm, content_w - 4*mm, FONT_SANS, 9, INK, leading=13)
    y -= 24*mm

    c.setFont(FONT_MONO, 7.5); c.setFillColor(INK_SOFT)
    c.drawString(MARGIN_X, y, "FOUNDER")
    y -= 5*mm
    c.setFont(FONT_SERIF, 18); c.setFillColor(INK)
    c.drawString(MARGIN_X, y, "Marta Escobar Rojas")
    y -= 6*mm
    c.setFont(FONT_SANS, 9.5); c.setFillColor(INK_SOFT)
    c.drawString(MARGIN_X, y, "MBA · Founder with AI in production · Madrid")
    y -= 14*mm

    c.setFillColor(INK)
    c.rect(MARGIN_X, y - 28*mm, content_w, 28*mm, stroke=0, fill=1)
    c.setFillColor(PAPER); c.setFont(FONT_SERIF, 16)
    c.drawString(MARGIN_X + 6*mm, y - 9*mm, "Book 30 minutes, no commitment.")
    c.setFont(FONT_SANS, 9.5)
    c.drawString(MARGIN_X + 6*mm, y - 14*mm, "A clear conversation — not a sales call.")
    btn_w = 60*mm; btn_h = 10*mm
    draw_link_button(c, "Book diagnostic · 30 min", CAL_URL,
                     MARGIN_X + 6*mm, y - 25*mm, btn_w, btn_h,
                     fill_color=ACCENT, text_color=white, font_size=10)
    c.setFillColor(PAPER); c.setFont(FONT_MONO, 8)
    c.drawString(MARGIN_X + 6*mm + btn_w + 6*mm, y - 22*mm, "OR WRITE TO:")
    em_x = MARGIN_X + 6*mm + btn_w + 6*mm
    em_y = y - 25.5*mm
    c.setFont(FONT_SANS_BOLD, 9.5)
    c.drawString(em_x, em_y, EMAIL)
    em_w = c.stringWidth(EMAIL, FONT_SANS_BOLD, 9.5)
    c.linkURL(EMAIL_HREF, (em_x, em_y - 1, em_x + em_w, em_y + 9), relative=0, thickness=0)

    footer(c); c.showPage()
    c.save()
    print(f"PDF generated: {out_path}")


if __name__ == "__main__":
    out_root = Path("Praxia_Atelier_Services.pdf")
    out_deploy = Path("deploy_netlify/Praxia_Atelier_Services.pdf")
    build_en(str(out_root))
    import shutil
    shutil.copy(out_root, out_deploy)
    print(f"Copied to {out_deploy}")
