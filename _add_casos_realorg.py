"""Add EN translations for the new Casos · Prototipos / Proyectos reales section."""
from _add_translations import append_block

BLOCK = """
    /* === CASOS · reorganizado en Prototipos navegables + Proyectos reales === */
    'Casos del estudio': 'Studio cases',
    'Dos formas de ver cómo trabaja Praxia. Arriba,': 'Two ways to see how Praxia works. Above,',
    'prototipos ficticios navegables': 'fictional navigable prototypes',
    'que sirven para que entiendas cómo se ve un ecosistema entregado por el estudio — estructura jurídica, software, modelo, mockups y simulador interactivo. Abajo,':
      'so you can see what an ecosystem delivered by the studio looks like — legal structure, software, model, mockups and interactive simulator. Below,',
    'proyectos reales': 'real projects',
    'con clientes reales: enlaces a los prototipos en producción, anonimizando lo que toca.':
      'with real clients: links to live prototypes, anonymising whatever needs to be.',

    'Bloque 1 · Para entender el método': 'Block 1 · To understand the method',
    'Prototipos ficticios navegables.': 'Fictional navigable prototypes.',
    'Construidos con el mismo rigor que un encargo real. Web, back office, simulador interactivo y modelo económico — todo tocable. Cuando trabajamos contigo, esto se construye con tu marca, tus números y tus protocolos.':
      'Built with the same rigour as a real engagement. Website, back office, interactive simulator and economic model — all tactile. When we work with you, this is built with your brand, your numbers and your protocols.',
    'Ficticios · pulsa para abrir': 'Fictional · click to open',
    '4 sectores · 4 ecosistemas completos': '4 sectors · 4 complete ecosystems',

    'Bloque 2 · Para entender la trayectoria': 'Block 2 · To understand the track record',
    'Proyectos reales con clientes reales.': 'Real projects with real clients.',
    'Praxia Atelier abre en 2026, pero el método se ha construido diseñando y operando proyectos reales. Aquí los enlaces a algunos de ellos — los que tienen prototipo público están':
      'Praxia Atelier opens in 2026, but the method has been built by designing and operating real projects. Here are links to some of them — those with a public prototype are',
    'enteramente navegables': 'fully navigable',
    '. Lo que no se puede enseñar por confidencialidad va anonimizado.': '. What can\\'t be shown for confidentiality reasons is anonymised.',

    /* Casavera card */
    'Cliente real · 2025': 'Real client · 2025',
    'Real estate · Madrid': 'Real estate · Madrid',
    'Casavera · inmobiliaria boutique con sistema operativo propio.': 'Casavera · boutique real estate firm with its own operating system.',
    'Carolina llevaba años gestionando alquileres y ventas como agente independiente con la cabeza en cuatro Excels. El encargo fue convertir esa cadena de servicios en un':
      'Carolina had spent years managing rentals and sales as an independent agent with her head split across four spreadsheets. The brief was to turn that chain of services into a',
    'ecosistema digital con dos caras': 'digital ecosystem with two faces',
    ': la web pública con cuatro puertas de entrada (invertir, vender, alquilar, buscar) y el back office propio con vista panorámica de los 10 procesos del negocio.':
      ': a public website with four entry doors (invest, sell, rent, search) and a custom back office with a panoramic view of the 10 business processes.',
    'Los dos prototipos son': 'Both prototypes are',
    'navegables íntegramente': 'fully navigable',
    '— pulsa los botones de abajo y los abres en una pestaña nueva.': '— click the buttons below to open them in a new tab.',
    'Capas tocadas · Producto + IA + Modelo + Marketing + Operaciones + Comercial':
      'Layers touched · Product + AI + Model + Marketing + Operations + Sales',
    'Dos prototipos navegables': 'Two navigable prototypes',

    /* Prototipo A · interno */
    'Prototipo A · Interno': 'Prototype A · Internal',
    'Sistema operativo · back office': 'Operating system · back office',
    '10 pestañas con vista panorámica del negocio: producto digital, plan financiero, vías de ingreso, mapa del ecosistema, operaciones de proyecto y gestión continua. Diseñado para que la dueña tenga una sola fuente de verdad — no cuatro Excels.':
      '10 tabs with a panoramic view of the business: digital product, financial plan, revenue streams, ecosystem map, project operations and ongoing management. Designed so the owner has a single source of truth — not four spreadsheets.',
    'Abrir prototipo →': 'Open prototype →',

    /* Prototipo B · público */
    'Prototipo B · Público': 'Prototype B · Public',
    'Web cliente · 4 puertas de entrada': 'Client website · 4 entry doors',
    'Web bilingüe con cuatro entradas (invertir, vender o alquilar piso, buscar piso, "no encuentro lo que busco"), chatbot determinista que filtra leads y flujo de captación end-to-end hasta la firma electrónica. Diseñada para que cada visitante encaje su intención en menos de 5 segundos.':
      'Bilingual website with four entries (invest, sell or rent, search, "I can\\'t find what I\\'m looking for"), a deterministic chatbot that filters leads and an end-to-end acquisition flow up to e-signature. Designed so every visitor fits their intent in under 5 seconds.',

    /* Otros proyectos */
    'Otros proyectos · sin prototipo público': 'Other projects · no public prototype',
    'EdTech · educación emocional': 'EdTech · emotional education',
    'Proyecto propio · activo': 'Own project · active',

    /* Cierre */
    'Distintas formas de haber tocado las 8 capas:': 'Different ways of having touched the 8 layers:',
    'como diseñadora para un cliente': 'as a designer for a client',
    '(Casavera, EdTech),': '(Casavera, EdTech),',
    'como fundadora y operadora de un producto propio': 'as founder and operator of an own product',
    '. Por confidencialidad no nombramos algunos proyectos por su marca pública — pero la experiencia operativa, no solo consultora, es lo que sostiene el método.':
      '. For confidentiality reasons we don\\'t name some projects by their public brand — but operational experience, not just consulting, is what sustains the method.',
"""
if __name__ == "__main__":
    append_block(BLOCK)
