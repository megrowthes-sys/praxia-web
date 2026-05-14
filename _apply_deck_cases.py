"""Apply deck navigation to the 4 case study pages.

Each page gets:
- data-panel attribute on each top-level <section>
- site-header-original class on the existing <header> (for hide via deck-mode)
- A page-specific PANELS configuration injected before chatbox includes
- praxia-deck.css + praxia-deck.js loaded
"""
from pathlib import Path
import re

CASES = {
    "Praxia_Atelier_Caso_Bodega_Valdescuro.html": {
        "panels": [
            ("panel-intro",       "Punto de partida",   "Family business"),       # 1 (hero)
            ("panel-partida",     "El reto",            "El punto de partida"),   # 2
            ("panel-ideas",       "3 ideas",            "Tres ideas"),            # 3
            ("panel-juridico",    "Jurídico",           "Estructura"),            # 4
            ("panel-software",    "Software",           "Arquitectura software"), # 5 (simulador)
            ("panel-modelo",      "Modelo económico",   "Modelo"),                # 6 (simulador)
            ("panel-aterrizaje",  "Aterrizaje",         "Aterrizaje C02"),        # 7
            ("panel-equipo",      "Equipo",             "Equipo externo"),        # 8
            ("panel-disclaimer",  "Alcance",            "Disclaimer fiscal"),     # 9
            ("panel-cierre",      "Cierre",             "14 días"),               # 10
        ],
        "section_starts": [207, 249, 271, 301, 364, 454, 845, 940, 1009, 1045],
        "expected_classes": [
            'class="relative overflow-hidden border-b border-line"',
            'class="bg-card border-b border-line"',
            'class="bg-paper border-b border-line"',
            'class="bg-card border-b border-line"',
            'class="bg-paper border-b border-line"',
            'class="bg-paper border-b border-line"',
            'class="bg-card border-b border-line"',
            'class="bg-paper border-b border-line"',
            'class="bg-card border-b border-line"',
            'style="background: #2a0d10; color: #ffffff;"',
        ],
    },
    "Praxia_Atelier_Caso_Clinica_Lumen.html": {
        "panels": [
            ("panel-intro",       "Health-tech",       "Health-tech · longevidad"),
            ("panel-partida",     "El reto",           "El punto de partida"),
            ("panel-palancas",    "Palancas",          "Tres palancas"),
            ("panel-software",    "Software + IA",     "Arquitectura"),         # simulador
            ("panel-equipo",      "Equipo",            "Equipo externo"),
            ("panel-disclaimer",  "Alcance",           "Disclaimer sanitario"),
            ("panel-cierre",      "Cierre",            "14 días"),
        ],
        "section_starts": [198, 239, 261, 291, 684, 753, 789],
        "expected_classes": [
            'class="relative overflow-hidden border-b border-line"',
            'class="bg-white border-b border-line"',
            'class="bg-paper border-b border-line"',
            'class="bg-white border-b border-line"',
            'class="bg-paper border-b border-line"',
            'class="bg-white border-b border-line"',
            'style="background: #0e2a26; color: #ffffff;"',
        ],
    },
    "Praxia_Atelier_Caso_Casa_Vento.html": {
        "panels": [
            ("panel-intro",       "Real estate",       "Real estate · residencial"),
            ("panel-partida",     "El reto",           "El punto de partida"),
            ("panel-palancas",    "Palancas",          "Tres palancas"),
            ("panel-software",    "Software + IA",     "Arquitectura"),         # simulador
            ("panel-friend",      "Friend",            "Friend"),
            ("panel-equipo",      "Equipo",            "Equipo externo"),
            ("panel-disclaimer",  "Alcance",           "Disclaimer regulatorio"),
            ("panel-cierre",      "Cierre",            "14 días"),
        ],
        "section_starts": [149, 190, 212, 242, 659, 730, 798, 834],
        "expected_classes": [
            'class="relative overflow-hidden border-b border-line"',
            'class="bg-white border-b border-line"',
            'class="bg-paper border-b border-line"',
            'class="bg-white border-b border-line"',
            'class="bg-paper border-b border-line"',
            'class="bg-white border-b border-line"',
            'class="bg-paper border-b border-line"',
            'style="background: #1a2733; color: #ffffff;"',
        ],
    },
    "Praxia_Atelier_Caso_Mesa_de_Trabajo.html": {
        "panels": [
            ("panel-intro",       "Caso ficticio",     "Caso ficticio"),
            ("panel-vista",       "8 departamentos",   "Vista panorámica"),
            ("panel-detalle",     "Detalle",           "Detalle"),                # simulador
            ("panel-encurso",     "En curso",          "En curso"),
            ("panel-cierre",      "Cierre",            "El método aplicado"),
        ],
        "section_starts": [119, 151, 226, 754, 783],
        "expected_classes": [
            'class="relative overflow-hidden border-b border-line"',
            'class="bg-white border-b border-line"',
            'class="bg-paper border-b border-line" id="detalle"',
            'class="bg-white border-b border-line"',
            'style="background: #2a1f15; color: #ffffff;"',
        ],
    },
}


def apply_to_case(filename, cfg):
    p = Path(filename)
    text = p.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)

    # Apply data-panel to each section start line
    panels = cfg["panels"]
    starts = cfg["section_starts"]
    expected = cfg["expected_classes"]

    for i, lineno in enumerate(starts):
        idx = lineno - 1
        current = lines[idx].rstrip("\n").rstrip("\r")
        panel_id = panels[i][0]
        # Sanity check
        if expected[i] not in current:
            print(f"  WARN line {lineno} ({panel_id}): expected class fragment not found.")
            print(f"       got: {current[:120]}")
            continue
        # Insert data-panel attribute right after <section
        new = current.replace("<section ", f'<section data-panel="{panel_id}" ', 1)
        # Handle bare <section> (no attrs)
        if new == current:
            new = current.replace("<section>", f'<section data-panel="{panel_id}">', 1)
        lines[idx] = new + ("\r\n" if lines[idx].endswith("\r\n") else "\n")

    s = "".join(lines)

    # Mark original header so deck-mode hides it
    s = s.replace(
        '<header class="border-b border-line bg-paper sticky top-0 z-30">',
        '<header class="site-header-original border-b border-line bg-paper sticky top-0 z-30">',
        1
    )
    # Casa Vento has a slightly different header signature
    s = s.replace(
        '<header class="border-b border-line bg-paper sticky top-0 z-30" style="background: var(--paper);">',
        '<header class="site-header-original border-b border-line bg-paper sticky top-0 z-30" style="background: var(--paper);">',
        1
    )

    # Build PANELS config block
    chips_lines = []
    chips_lines.append("  { href: 'index.html', label: 'Estudio', dataI18n: 'nav-estudio' },")
    for pid, label, _ in panels:
        chips_lines.append(f"  {{ id: '{pid}', label: '{label}' }},")
    chips_lines.append("  { href: 'index.html#casos', label: 'Otros casos', dataI18n: 'nav-otros-casos' },")
    chips_lines.append("  { href: 'index.html#contacto', label: 'Contacto', dataI18n: 'nav-contacto' }")

    chips_block = "\n".join(chips_lines)

    custom_panels = (
        "<script>\n"
        "window.PRAXIA_DECK_PANELS = [\n"
        + chips_block + "\n"
        "];\n"
        "window.PRAXIA_DECK_CTA = { label: 'Reservar diagnóstico', href: 'index.html#contacto' };\n"
        "</script>\n"
        '<link rel="stylesheet" href="praxia-deck.css">\n'
        '<script src="praxia-deck.js" defer></script>\n'
    )

    # Inject before chatbox or before </body>
    chatbox_marker = '<!-- Praxia Chatbox · cargado externo'
    if chatbox_marker in s:
        s = s.replace(chatbox_marker, custom_panels + chatbox_marker, 1)
    else:
        s = s.replace("</body>", custom_panels + "\n</body>", 1)

    p.write_text(s, encoding="utf-8")
    print(f"  ✓ {filename} transformed.")


if __name__ == "__main__":
    for filename, cfg in CASES.items():
        print(f"\n=== {filename} ===")
        apply_to_case(filename, cfg)
