/* ============================================================
   Praxia · i18n switcher (ES/EN)
   Inyecta el switcher en el header y traduce TODOS los nodos de texto
   del body usando un diccionario ES → EN. Mantenemos el español como
   versión maestra y guardamos cada original para volver a ES sin recargar.
   ============================================================ */
(function () {
  if (window.__PRAXIA_I18N_LOADED__) return;
  window.__PRAXIA_I18N_LOADED__ = true;

  /* ============================================================
     Diccionario ES → EN
     Cada clave es la cadena exacta en español (después de trim()).
     ============================================================ */
  const DICT = {
    /* === HEADER === */
    'Ecosystem architecture': 'Ecosystem architecture',
    'Método': 'Method',
    'Para quién': 'Who for',
    'Cápsulas': 'Capsules',
    'Fundadora': 'Founder',
    'Asistente': 'Assistant',
    'Casos': 'Cases',
    'Habla con Praxia': 'Talk to Praxia',
    'Mesa de trabajo': 'Workspace',
    'Diario': 'Journal',
    'Insights': 'Insights',
    'Newsletter': 'Newsletter',
    'Colaboradores': 'Collaborators',
    'Contacto': 'Contact',
    'Reservar diagnóstico': 'Book a diagnostic',

    /* === HERO === */
    'Estudio · Madrid · 2026': 'Studio · Madrid · 2026',
    'Diseñamos ecosistemas digitales': 'We design digital ecosystems',
    'listos para captar capital': 'ready to raise capital',
    'o multiplicar el ROI de tu empresa.': 'or multiply your company\'s ROI.',
    'Si sólo tienes la idea, empezamos por ahí. Si ya tienes empresa, te diseñamos la capa siguiente. Estructura jurídico-fiscal, software, avatar con IA, modelo económico y materiales para inversores — un único estudio, una única voz.':
      'If you only have the idea, we start there. If you already have a company, we design the next layer. Legal-tax structure, software, AI avatar, economic model, and investor materials — one single studio, one single voice.',
    'Reservar 30 min con Marta · gratis': 'Book 30 min with Marta · free',
    'Ver demos navegables': 'See navigable demos',
    '· Sin coste · Sin compromiso': '· No cost · No commitment',
    'Reserva 30 min': 'Book 30 min',
    'y en las 48 horas siguientes recibes un one-pager gratis con': 'and within 48 hours you receive a free one-pager with',
    'tres movimientos accionables': 'three actionable moves',
    'específicos para tu proyecto. Sin contratar nada — el valor es tuyo aunque no sigamos juntos.':
      'specific to your project. No contract required — the value is yours even if we don\'t continue together.',
    'días para el blueprint': 'days to blueprint',
    'entidades coordinadas': 'entities coordinated',
    'disciplinas en una sola voz': 'disciplines, one voice',
    'prototipo navegable': 'navigable prototype',

    /* === MANIFIESTO IA === */
    'Una nota sobre cómo trabajamos': 'A note on how we work',
    'La IA es': 'AI is',
    'una herramienta más': 'just another tool',
    ', no el oficio.': ', not the craft.',
    'Hoy es muy fácil generar una landing o un esquema en cinco minutos. Lo que lleva más tiempo es':
      'Today it\'s easy to generate a landing page or an outline in five minutes. What takes more time is to',
    'escuchar': 'listen',
    'al fundador y entender qué empresa lleva dentro,': 'to the founder and understand the business they carry inside,',
    'sintetizar': 'synthesize',
    'ideas que aún no están del todo formuladas, y': 'ideas that aren\'t fully formed yet, and to',
    'conectar': 'connect',
    'lo fiscal con el producto, lo comercial con la operación, el modelo con la realidad del cliente.':
      'tax with product, sales with operations, the model with the client\'s reality.',
    'Ese trabajo lo seguimos haciendo a mano. La IA nos ayuda a ir más rápido — no piensa por nosotros.':
      'That work, we still do by hand. AI helps us move faster — it doesn\'t think for us.',

    /* === PROBLEMA === */
    'El problema que resolvemos': 'The problem we solve',
    'un despacho fiscal, una agencia de producto, una software house, un estudio de diseño, una consultora de marketing, un consultor de operaciones, una agencia comercial y un asesor de fundraising':
      'a tax firm, a product agency, a software house, a design studio, a marketing consultancy, an operations consultant, a sales agency, and a fundraising advisor',
    '. Ocho proveedores. Ocho contratos. Doce meses. Resultados desalineados.':
      '. Eight vendors. Eight contracts. Twelve months. Misaligned results.',
    'Praxia Atelier hace ese trabajo como': 'Praxia Atelier does that work as',
    'un único equipo de autor': 'a single authored team',
    '. Te entregamos la estructura jurídica, el software, la IA, el modelo económico, la estrategia de marketing, el diseño operativo, el playbook comercial y los materiales para inversores como un sistema coherente — listo para operar y para defenderse delante de un fondo, una notaría o un asesor fiscal.':
      '. We deliver the legal structure, the software, the AI, the economic model, the marketing strategy, the operations design, the sales playbook and investor materials as one coherent system — ready to operate and to defend before a fund, a notary or a tax advisor.',
    'Si has llegado hasta aquí, probablemente tienes un proyecto real, prisa por arrancar y la sensación de que ningún proveedor cubre el problema entero. Estás en el sitio correcto.':
      'If you\'ve made it this far, you probably have a real project, are in a hurry to start, and feel that no single vendor covers the whole problem. You\'re in the right place.',

    /* === MÉTODO === */
    'Método de ocho capas': 'Eight-layer method',
    'Las ocho disciplinas que normalmente viven en ocho proveedores distintos, integradas en un solo entregable y diseñadas por la misma cabeza.':
      'The eight disciplines that usually live in eight different vendors, integrated into a single deliverable, designed by the same mind.',
    'Capa 1': 'Layer 1', 'Capa 2': 'Layer 2', 'Capa 3': 'Layer 3', 'Capa 4': 'Layer 4',
    'Capa 5': 'Layer 5', 'Capa 6': 'Layer 6', 'Capa 7': 'Layer 7', 'Capa 8': 'Layer 8',
    'Jurídico-fiscal': 'Legal & tax',
    'Diseño de entidades (AIE, asociación, holdings, sociedades operativas), separación pertenencia / mercantil, riesgos tipificados.':
      'Entity design (EIG, association, holdings, operating companies), ownership/commercial separation, typified risks.',
    'Producto y software': 'Product & software',
    'Arquitectura modular, planos web / área socio / back office, stack RGPD, integraciones (Stripe, firma electrónica, WhatsApp).':
      'Modular architecture, blueprints for web / member area / back office, GDPR-ready stack, integrations (Stripe, e-signature, WhatsApp).',
    'IA aplicada': 'Applied AI',
    'Avatar conversacional, perfilado por embeddings, motor de matching híbrido, un único punto humano.':
      'Conversational avatar, embedding-based profiling, hybrid matching engine, a single human point.',
    'Modelo económico': 'Economic model',
    'Coste mínimo + a éxito, fases por activadores, tramos de mantenimiento, encaje fiscal para inversores.':
      'Floor cost + success-based fees, milestone-driven phases, maintenance tiers, fiscal alignment for investors.',
    'Storytelling de capital': 'Capital storytelling',
    'One-pager para inversores, deck navegable, argumentario fiscal (Ley 28/2022, AIE), prototipo enseñable a fondos.':
      'Investor one-pager, navigable deck, fiscal narrative (Law 28/2022, EIG), prototype demoable to funds.',
    'Estrategia de marketing': 'Marketing strategy',
    'Posicionamiento, buyer personas, plan 90 días, calendario editorial, funnel de captación, stack de herramientas.':
      'Positioning, buyer personas, 90-day plan, editorial calendar, acquisition funnel, tool stack.',
    'Operaciones y procesos': 'Operations & process',
    'Mapa de procesos as-is/to-be, automatizaciones con IA, RACI, SOPs, KPIs operativos y dashboard inicial.':
      'As-is/to-be process mapping, AI automations, RACI, SOPs, operational KPIs, initial dashboard.',
    'Estrategia comercial': 'Sales strategy',
    'Funnel TOFU/MOFU/BOFU, scripts, pricing, gestión de pipeline, plantillas de propuesta y contratos.':
      'TOFU/MOFU/BOFU funnel, scripts, pricing, pipeline management, proposal and contract templates.',
    'Lo entregable no es una presentación. Es': 'The deliverable isn\'t a presentation. It\'s',
    'un dossier + un prototipo navegable + un modelo financiero vivo + un set de contratos modelo':
      'a dossier + a navigable prototype + a live financial model + a set of model contracts',
    '. Lo puedes enseñar el lunes a tu notario, a tu asesor fiscal y a tu primer inversor — y los tres entienden lo mismo.':
      '. You can show it on Monday to your notary, your tax advisor and your first investor — and all three understand the same thing.',

    /* === DOS PUERTAS === */
    'Dos puertas de entrada,': 'Two ways in,',
    'un mismo entregable.': 'one same deliverable.',
    'Si vienes con una idea o si ya tienes empresa, el resultado es el mismo:': 'Whether you arrive with an idea or already have a company, the result is the same:',
    'un ecosistema completo diseñado en planos': 'a complete ecosystem designed in blueprints',
    '— listo para que tú o tu equipo lo aterricéis. Si quieres que lo aterricemos nosotros, eso es Cápsula 02.':
      ' — ready for you or your team to ground. If you want us to ground it, that\'s Capsule 02.',
    'Si sólo tienes la idea': 'If you only have the idea',
    'Empezamos por ahí.': 'We start there.',
    'Del audio al ecosistema': 'From audio to ecosystem',
    'No hace falta que llegues con un plan, un Notion ordenado o un brief de agencia. Hacemos contigo':
      'You don\'t need to arrive with a plan, a tidy Notion or an agency brief. We do',
    'una sesión de brainstorm': 'a brainstorm session',
    'para entender el negocio, ponerle palabras y proponerte opciones. Y a partir de ahí te devolvemos':
      'with you to understand the business, put words to it, and propose options. From there we deliver back',
    'el negocio entero diseñado': 'the entire business designed',
    ': sociedad, encaje fiscal, software, avatar, modelo económico, argumentario para inversores y materiales comerciales.':
      ': legal structure, fiscal alignment, software, AI avatar, economic model, investor narrative and sales materials.',
    'Founders solitarios o en equipo': 'Solo or team founders',
    'Family offices que arrancan vehículo nuevo': 'Family offices launching a new vehicle',
    'Promotores de club privado o asociación': 'Private club or association promoters',
    'Coaches y creadores con comunidad lista': 'Coaches and creators with an existing community',
    'Si ya tienes la empresa': 'If you already have the company',
    'Te diseñamos la capa siguiente.': 'We design the next layer.',
    'Del negocio actual al ecosistema': 'From the current business to the ecosystem',
    'Si tu empresa factura entre': 'If your company bills between',
    '1 y 10 M€': '€1M and €10M',
    'y está estancada, escalando o buscando salto de modelo, partimos de un': 'and is stuck, scaling, or looking for a model leap, we start from a',
    'brainstorm para entender el negocio': 'brainstorm to understand the business',
    'y proponerte opciones reales — y desde ahí diseñamos la capa nueva que multiplica el ROI o desbloquea una vertical entera, sin canibalizar el core.':
      'and propose real options — from there we design the new layer that multiplies ROI or unlocks an entire vertical, without cannibalizing the core.',
    'Nueva línea de ingresos (membresía, marketplace, SaaS)': 'New revenue line (membership, marketplace, SaaS)',
    'Automatización de procesos con IA': 'AI process automation',
    'Reestructuración para captar capital o vehículo de coinversión': 'Restructuring to raise capital or a co-investment vehicle',
    'Spin-off digital o vertical nueva': 'Digital spin-off or new vertical',
    'Cómo es el proceso': 'How the process works',
    'Mismo método para los dos puntos de entrada. Lo que cambia es la conversación inicial — no el resultado.':
      'Same method for both entry points. What changes is the initial conversation — not the outcome.',
    'Día 0': 'Day 0', 'Día 1': 'Day 1', 'Día 2–10': 'Day 2–10', 'Día 15': 'Day 15',
    'Brainstorm para entender tu negocio.': 'Brainstorm to understand your business.',
    'Te proponemos opciones.': 'We propose options.',
    'Diseñamos el ecosistema.': 'We design the ecosystem.',
    'Sales con los planos listos.': 'You leave with the blueprints ready.',
    'Nota': 'Note',
    'Praxia Atelier es un estudio de consultoría y diseño.': 'Praxia Atelier is a consulting and design studio.',
    'Si todavía no lo tienes claro, empezamos por la': 'If you\'re still not sure, we start with',
    'Cápsula 00 · Strategy Sprint': 'Capsule 00 · Strategy Sprint',
    '— desde 990 € — para entender tu negocio en una sesión de brainstorm y proponerte tres opciones. La Cápsula 01 entrega los planos completos del ecosistema, listos para que tú o tu equipo los aterricéis.':
      ' — from €990 — to understand your business in a brainstorm session and propose three options. Capsule 01 delivers the full ecosystem blueprints, ready for you or your team to ground.',
    'Si quieres que': 'If you want us to',
    'lo aterricemos nosotros': 'ground it ourselves',
    '(desarrollo, integraciones, go-live), eso es la Cápsula 02 — coordinamos al equipo externo (desarrolladores, diseñadores, integradores) y entregamos el sistema funcionando. Decides la frontera tú.':
      '(development, integrations, go-live), that\'s Capsule 02 — we coordinate the external team (developers, designers, integrators) and deliver the working system. You decide the boundary.',
    'Cuéntanos tu idea o tu empresa': 'Tell us about your idea or company',
    'Ver las cápsulas': 'See the capsules',

    /* === CÁPSULAS === */
    'Siete cápsulas. Precio cerrado.': 'Seven capsules. Fixed price.',
    'No vendemos horas. Cada cápsula tiene alcance, plazo y entregables fijos. Si no encajan, no hay propuesta.':
      'We don\'t sell hours. Each capsule has a fixed scope, timeline, and deliverables. If they don\'t fit, there\'s no proposal.',
    '00 es el punto de entrada — un sprint barato para validar que tu proyecto encaja.':
      '00 is the entry point — a low-cost sprint to validate that your project fits.',
    '01–03 son las cápsulas del ecosistema (diseño, aterrizaje y operación). 04–06 son las cápsulas funcionales para empresas que sólo necesitan reactivar marketing, operaciones o comercial.':
      '01–03 are the ecosystem capsules (design, grounding, operation). 04–06 are the functional capsules for companies that only need to reactivate marketing, operations or sales.',
    'Cápsula 00 · Punto de entrada': 'Capsule 00 · Entry point',
    '1 semana': '1 week',
    'Strategy Sprint': 'Strategy Sprint',
    'El escalón previo al Blueprint. Una sesión de brainstorm, tres opciones reales y una recomendación firmada — para que pruebes cómo trabajamos antes de comprometerte con un proyecto grande.':
      'The step before the Blueprint. A brainstorm session, three real options, and a signed recommendation — so you test how we work before committing to a larger project.',
    'Lo que entregamos': 'What we deliver',
    'Brainstorm de 3 h con la fundadora del estudio': '3-hour brainstorm with the studio founder',
    'Diagnóstico de viabilidad del proyecto': 'Project viability diagnosis',
    '3 opciones de ecosistema con pros y contras': '3 ecosystem options with pros and cons',
    'Memo profesional de 5–7 páginas firmado': 'Signed professional 5–7 page memo',
    'Recomendación clara del camino': 'Clear path recommendation',
    'Tres niveles según tu perfil': 'Three levels by profile',
    'Founders solitarios o coaches': 'Solo founders or coaches',
    'Para quien parte de una idea sin empresa todavía. Brainstorm + memo enfocado a viabilidad y siguiente paso.':
      'For those starting from an idea without a company yet. Brainstorm + memo focused on viability and next step.',
    'PYMEs 1–10 M€ / family business': 'SMEs €1–10M / family business',
    'Para empresas operando que quieren explorar nueva línea de ingresos, automatización con IA o spin-off. Memo con análisis de capa nueva.':
      'For operating companies exploring a new revenue line, AI automation or spin-off. Memo with new-layer analysis.',
    'Family offices y corporativos': 'Family offices and corporate',
    'Para vehículos patrimoniales que diseñan algo más complejo (club, AIE, vehículo de coinversión). Memo con encaje fiscal preliminar.':
      'For wealth vehicles designing something more complex (club, EIG, co-investment vehicle). Memo with preliminary fiscal alignment.',
    'Truco honesto': 'Honest tip',
    'Si después del sprint contratas la Cápsula 01 en los siguientes 30 días,': 'If after the sprint you contract Capsule 01 within the next 30 days,',
    'los honorarios del sprint se descuentan íntegramente': 'the sprint fee is fully credited',
    'de la factura del Blueprint. En la práctica, el sprint sale gratis si avanzamos. Si entras por':
      'against the Blueprint invoice. In practice, the sprint is free if we move forward. If you enter through',
    'Sprint + Launch':
      'Sprint + Launch',
    ', se descuentan los 2.500 € de consultoría — el desarrollo web ya está entregado.':
      ', €2,500 of consulting are credited — the web development is already delivered.',

    /* === SPRINT + LAUNCH (cuarto nivel destacado) === */
    '1 semana de sprint + 2 semanas de implementación': '1-week sprint + 2 weeks of implementation',
    'Si lo que necesitas es': 'If what you need is to',
    'lanzar ya': 'launch now',
    ', no solo diagnosticar.': ', not just diagnose.',
    'Mismo brainstorm, memo y diagnóstico que el Strategy Sprint estándar — y además dejamos tu negocio operativo: web profesional, dominio configurado, email corporativo, calendario, formulario y chatbox de captación. Sales con todo enchufado y un roadmap de 90 días para seguir tú.':
      'Same brainstorm, memo and diagnosis as the standard Strategy Sprint — and on top, we leave your business operational: professional website, configured domain, corporate email, calendar, form and lead-capture chatbox. You walk out with everything plugged in and a 90-day roadmap to keep going on your own.',
    'precio cerrado · una sola factura': 'fixed price · single invoice',
    'Qué entregamos': 'What we deliver',
    'Tu negocio, listo para operar el lunes siguiente.': 'Your business, ready to operate by Monday.',
    'Estrategia': 'Strategy',
    'Brainstorm 3 h, memo profesional firmado, 3 opciones de ecosistema, recomendación clara.':
      '3-hour brainstorm, signed professional memo, 3 ecosystem options, clear recommendation.',
    'Web dinámica': 'Dynamic website',
    'Web multi-página: home + página de servicio + sobre + contacto + aviso legal + privacidad.':
      'Multi-page website: home + service page + about + contact + legal notice + privacy.',
    'Dominio + hosting': 'Domain + hosting',
    'Dominio configurado y conectado a Netlify (hosting gratis). Cliente paga el dominio aparte (~12 €/año).':
      'Domain configured and connected to Netlify (free hosting). Client pays the domain separately (~€12/year).',
    'Email profesional': 'Professional email',
    'Cuenta info@tudominio configurada vía Google Workspace. Cliente paga la licencia (~6-18 €/mes).':
      'info@yourdomain account configured via Google Workspace. Client pays the licence (~€6-18/month).',
    'Calendario': 'Calendar',
    'Cal.com integrado en la web, conectado al calendario del cliente para reservas directas.':
      'Cal.com integrated in the web, connected to the client\'s calendar for direct bookings.',
    'Formulario de contacto': 'Contact form',
    'Formulario activo conectado al email del cliente. Captura leads desde el primer día.':
      'Active form connected to the client\'s email. Captures leads from day one.',
    'Chatbox de captación': 'Lead-capture chatbox',
    'Chatbox de cualificación de leads adaptado a tu negocio. Pregunta, filtra y deriva al calendario. Mismo motor que el de Praxia.':
      'Lead qualification chatbox adapted to your business. Asks, filters and routes to the calendar. Same engine as Praxia\'s.',
    'Roadmap 90 días': '90-day roadmap',
    'Plan accionable semana a semana para los 3 meses siguientes. Qué hacer, qué herramientas usar, cuándo plantear Cápsula 01.':
      'Week-by-week actionable plan for the next 3 months. What to do, which tools to use, when to consider Capsule 01.',
    'Founders y empresas que tienen claro que quieren validar lanzando algo real, no solo recibir un memo. El siguiente paso natural es Cápsula 01 si el negocio crece.':
      'Founders and companies that want to validate by launching something real, not just receive a memo. The natural next step is Capsule 01 if the business grows.',

    /* === Add-on premium · IA conversacional / avatar === */
    'Add-on premium': 'Premium add-on',
    '¿Quieres chatbox con IA conversacional real o avatar?': 'Want a real conversational AI chatbox or avatar?',
    'Sobre cualquier nivel del Strategy Sprint, podemos añadir un': 'On any Strategy Sprint level, we can add a',
    'chatbox con IA conversacional (Claude API)': 'conversational AI chatbox (Claude API)',
    'que entienda lenguaje natural y responda como un humano, o un': 'that understands natural language and responds like a human, or a',
    'avatar conversacional con voz e imagen': 'conversational avatar with voice and image',
    '. Implica configurar API, system prompt con la voz de tu negocio, backend serverless y costes recurrentes de uso.':
      '. Involves configuring API, system prompt with your business voice, serverless backend and recurring usage costs.',
    'Presupuesto personalizado': 'Custom quote',
    'según alcance. Pídelo al brief y te damos un número cerrado en 48 h.':
      'based on scope. Request it at briefing and we send a fixed number within 48h.',
    'Pedir presupuesto': 'Request quote',
    'Y luego, el ecosistema entero': 'And then, the entire ecosystem',
    'Si el sprint nos confirma que encajamos, las tres cápsulas siguientes cubren todo el ciclo — diseño, aterrizaje y operación.':
      'If the sprint confirms we fit, the next three capsules cover the full cycle — design, grounding and operation.',
    'Cápsula 01 · Consultoría': 'Capsule 01 · Consulting',
    '10–15 días': '10–15 days',
    'Ecosystem Blueprint': 'Ecosystem Blueprint',
    'Diseño completo del ecosistema en planos. Lo aterriza tu equipo o lo aterrizamos en Cápsula 02.':
      'Full ecosystem design in blueprints. Your team grounds it, or we ground it in Capsule 02.',
    'precio cerrado · una sola factura': 'fixed price · single invoice',
    'Mapa jurídico-fiscal de entidades': 'Legal-tax entity map',
    'Arquitectura de producto y software': 'Product and software architecture',
    'Prompt de avatar conversacional': 'Conversational avatar prompt',
    'Modelo económico por fases': 'Phased economic model',
    'Prototipo HTML navegable': 'Navigable HTML prototype',
    'One-pager + deck para inversores': 'Investor one-pager + deck',
    'Lo entregamos como': 'We deliver it as',
    'Dossier + prototipo navegable + modelo económico vivo + set de contratos modelo.':
      'Dossier + navigable prototype + live economic model + set of model contracts.',
    'Cápsula 02 · Aterrizaje': 'Capsule 02 · Grounding',
    '3–5 meses': '3–5 months',
    'Ecosystem Build': 'Ecosystem Build',
    'Si quieres que aterricemos los planos: coordinamos al equipo externo (desarrolladores, diseñadores, integradores) y entregamos el sistema funcionando.':
      'If you want us to ground the blueprints: we coordinate the external team (developers, designers, integrators) and deliver the working system.',
    '+ infraestructura y APIs externas': '+ infrastructure and external APIs',
    'Web pública + área de socio + back office': 'Public web + member area + back office',
    'Avatar conversacional integrado': 'Integrated conversational avatar',
    'Motor de matching híbrido': 'Hybrid matching engine',
    'Pagos, firma electrónica, comunicación': 'Payments, e-signature, communication',
    'RGPD + EU AI Act resueltos': 'GDPR + EU AI Act handled',
    'Go-live con primeros 30 socios': 'Go-live with first 30 members',
    'Cómo trabajamos': 'How we work',
    'Praxia dirige y garantiza el resultado. Los desarrolladores y especialistas son externos, contratados y coordinados por el estudio.':
      'Praxia directs and guarantees the outcome. Developers and specialists are external, contracted and coordinated by the studio.',
    'Cápsula 03 · Operación': 'Capsule 03 · Operation',
    'recurrente': 'recurring',
    'Ecosystem Operate': 'Ecosystem Operate',
    'Mantenimiento, iteración y reporting — escalado por volumen de socios o usuarios.':
      'Maintenance, iteration and reporting — scaled by member or user volume.',
    'tres tramos · revisión automática': 'three tiers · automatic review',
    'Tramo 1: hasta 300 — 5.500 €/mes': 'Tier 1: up to 300 — €5,500/mo',
    'Tramo 2: 300–600 — 6.500 €/mes': 'Tier 2: 300–600 — €6,500/mo',
    'Tramo 3: 600–1.000 — 8.000 €/mes': 'Tier 3: 600–1,000 — €8,000/mo',
    'Reporting trimestral a inversores': 'Quarterly investor reporting',
    'Iteración de prompts y matching': 'Prompt and matching iteration',
    'Sólo aplica si': 'Only applies if',
    'El ecosistema está aterrizado (Cápsula 02 o equivalente con tu equipo).':
      'The ecosystem is grounded (Capsule 02 or equivalent with your team).',
    '¿Ya tienes el ecosistema y necesitas reactivar marketing, operaciones o comercial?':
      'Do you already have the ecosystem and need to reactivate marketing, operations or sales?',
    'Tres cápsulas independientes para empresas operando que necesitan rediseñar una capa concreta del negocio sin tocar el resto. Mismo método, mismo nivel de detalle, alcance acotado.':
      'Three independent capsules for operating companies that need to redesign a specific layer without touching the rest. Same method, same level of detail, scoped.',
    'Cápsula 04 · Marketing': 'Capsule 04 · Marketing',
    '2–3 semanas': '2–3 weeks',
    'Marketing Blueprint': 'Marketing Blueprint',
    'Estrategia de marketing accionable a 90 días — listo para que tu equipo lo ejecute o lo coordinemos en C02.':
      'Actionable 90-day marketing strategy — ready for your team to execute or for us to coordinate in C02.',
    'precio cerrado · una factura': 'fixed price · one invoice',
    'Posicionamiento + buyer personas + JTBD': 'Positioning + buyer personas + JTBD',
    'Plan de canales 90 días (orgánico + paid + PR)': '90-day channel plan (organic + paid + PR)',
    'Calendario editorial + 12 piezas modelo': 'Editorial calendar + 12 model pieces',
    'Funnel de captación con métricas objetivo': 'Acquisition funnel with target metrics',
    'Stack tecnológico recomendado': 'Recommended tech stack',
    'Plantillas de campaña reutilizables': 'Reusable campaign templates',
    'Para quién': 'For whom',
    'PYMEs estancadas, marcas premium sin estrategia clara, empresas familiares en transición digital.':
      'Stalled SMEs, premium brands without a clear strategy, family businesses in digital transition.',
    'Cápsula 05 · Operaciones': 'Capsule 05 · Operations',
    'Operations Blueprint': 'Operations Blueprint',
    'Diseño operativo del negocio: procesos, automatización con IA, RACI y SOPs documentados.':
      'Operational design of the business: processes, AI automation, RACI and documented SOPs.',
    'Mapa de procesos críticos (as-is → to-be)': 'Critical process map (as-is → to-be)',
    'Identificación de cuellos de botella + ROI por proceso': 'Bottleneck identification + per-process ROI',
    'Diseño de automatizaciones con IA': 'AI automation design',
    'Matriz RACI por rol': 'RACI matrix by role',
    '8–12 SOPs documentados (procedimientos)': '8–12 documented SOPs (procedures)',
    'KPIs operativos y dashboard inicial': 'Operational KPIs and initial dashboard',
    'Empresas que escalan y se ahogan en operativa, equipos sin documentación, negocios que quieren incorporar IA sin saber dónde.':
      'Companies scaling and drowning in ops, teams without documentation, businesses wanting to add AI without knowing where.',
    'Cápsula 06 · Comercial': 'Capsule 06 · Sales',
    'Commercial Blueprint': 'Commercial Blueprint',
    'Playbook comercial completo: funnel, scripts, pricing, gestión de pipeline y cierre.':
      'Full sales playbook: funnel, scripts, pricing, pipeline management and closing.',
    'Funnel completo (TOFU/MOFU/BOFU) por persona': 'Full funnel (TOFU/MOFU/BOFU) per persona',
    'Pricing strategy + niveles + objection handling': 'Pricing strategy + tiers + objection handling',
    'Scripts de outbound, demo y cierre': 'Outbound, demo and closing scripts',
    'Estructura de pipeline en CRM (HubSpot / Pipedrive)': 'CRM pipeline structure (HubSpot / Pipedrive)',
    'Plantillas de propuesta y contratos': 'Proposal and contract templates',
    'Plan de incentivos comercial': 'Sales incentive plan',
    'Negocios con producto pero sin método de venta, founders que cierran ellos solos, equipos comerciales sin estructura repetible.':
      'Businesses with product but no sales method, founders who close alone, sales teams without repeatable structure.',
    'Pack GTM completo': 'Full GTM pack',
    '04 + 05 + 06 · Marketing, Operaciones y Comercial': '04 + 05 + 06 · Marketing, Operations & Sales',
    'Las tres cápsulas funcionales en un solo proyecto de 5 semanas. Diseñadas a la vez, con coherencia entre las tres capas. Si compraras cada una por separado pagarías hasta 22.500 €.':
      'The three functional capsules in a single 5-week project. Designed at once, with coherence across all three layers. Bought separately, you\'d pay up to €22,500.',
    'ahorro de 4.500 €': '€4,500 saved',
    'Pedir propuesta': 'Request proposal',
    'Modelo de incentivo alineado': 'Aligned incentive model',
    'Sobre cualquier cápsula, podemos añadir un': 'On any capsule, we can add a',
    'fee a éxito del 1–2 %': '1–2% success fee',
    'sobre la ronda que cierres con los materiales que entregamos, o un': 'on the round you close using our materials, or a',
    'royalty del 1–3 %': '1–3% royalty',
    'sobre los ingresos del año 1. Esto baja el ticket inicial y nos pone en el mismo lado de la mesa.':
      'on year-1 revenue. This lowers the initial ticket and puts us on the same side of the table.',
    'Pedir simulación': 'Request simulation',

    /* === FUNDADORA === */
    'Por qué': 'Why',
    'esto no lo hace una IA': 'AI alone can\'t do this',
    'La IA escribe código, redacta copy, ordena tablas. Lo que': 'AI writes code, drafts copy, organizes tables. What it',
    'no hace sola': 'doesn\'t do alone',
    'es escuchar a un fundador, directivo o empresario durante una hora y ver qué empresa lleva dentro. No conecta lo fiscal con':
      'is listen to a founder, executive or entrepreneur for an hour and see the business they carry inside. It doesn\'t connect tax with',
    'Esa es la pieza irreemplazable, y es exactamente lo que entrego.':
      'That\'s the irreplaceable piece — and it\'s exactly what I deliver.',
    'He pasado por cada parte del proceso que voy a diseñar para ti — no como observadora, sino como operadora. He vendido, he construido producto, he montado sociedades, he levantado capital, he gestionado equipos, he escrito el copy y he':
      'I\'ve been through every part of the process I\'ll design for you — not as an observer, but as an operator. I\'ve sold, built product, set up companies, raised capital, managed teams, written copy, and',
    'Comercial B2B': 'B2B Sales',
    '7+ años en venta B2B tech.': '7+ years in B2B tech sales.',
    'Cierre de contrato de 800 k€ con Consejería de Educación. Conozco el otro lado de la mesa.':
      '€800k contract closed with Spain\'s Department of Education. I know the other side of the table.',
    'Founder': 'Founder',
    'Founder de una plataforma con IA en producción.': 'Founder of an AI-powered platform in production.',
    'Sé qué duele construir desde cero, levantar ronda y operar al día siguiente.':
      'I know what it hurts to build from zero, raise a round, and operate the next day.',
    'Producto e IP': 'Product & IP',
    'Metodología propia registrada.': 'Proprietary registered methodology.',
    '40+ protocolos, motor clasificador propio. Diseño productos, no sólo asesoro sobre productos.':
      '40+ protocols, proprietary classifier engine. I design products — I don\'t just advise on them.',
    'Formación': 'Training',
    'MBA + Máster en Product Management.': 'MBA + Master\'s in Product Management.',
    'Soporte técnico para que las decisiones se sostengan delante de un fondo o un asesor fiscal.':
      'Technical grounding so decisions hold up in front of a fund or a tax advisor.',
    '"La IA me ayuda a ir más rápido. Lo que sigue siendo trabajo de persona — escuchar, entender el negocio que tienes en la cabeza y traducirlo en algo coherente — es lo que pongo encima de la mesa cuando trabajamos juntos."':
      '"AI helps me move faster. What\'s still human work — listening, understanding the business you carry in your head, and translating it into something coherent — is what I put on the table when we work together."',
    '— Marta Escobar': '— Marta Escobar',
    'Fundadora · Praxia Atelier': 'Founder · Praxia Atelier',
    'Marta Escobar Rojas': 'Marta Escobar Rojas',

    /* === FUNDADORA · NOTA NUEVA === */
    'Una nota sobre cómo trabajo': 'A note on how I work',
    'Lo raro no es saber de cada capa. Lo raro es integrarlas.': 'The rare part isn\'t knowing each layer. The rare part is integrating them.',
    'Lo que hace que Praxia funcione no es que yo "haga de todo". Es que sé lo suficiente de cada una de las ocho capas como para diseñar cómo se integran entre sí: qué decisión jurídica condiciona el modelo económico, qué pieza de IA cambia la economía unitaria, qué arquitectura técnica habilita o bloquea el GTM, qué storytelling de capital encaja con qué estructura societaria.':
      'What makes Praxia work isn\'t that I "do everything." It\'s that I know enough about each of the eight layers to design how they integrate: which legal decision conditions the economic model, which AI piece changes unit economics, which technical architecture enables or blocks the GTM, which capital story matches which corporate structure.',
    'Esa integración es el trabajo.': 'That integration is the work.',
    'Y se aprende habiéndolo hecho, no leyéndolo.': 'And it\'s learned by doing, not by reading.',
    'En la práctica, esto significa que un cliente que trabaja con Praxia se ahorra coordinar a seis o siete proveedores distintos. Llego con la documentación estructurada, las plantillas listas y las decisiones del modelo ya tomadas, de forma que':
      'In practice, this means a client working with Praxia saves coordinating six or seven different vendors. I arrive with structured documentation, ready-to-use templates and the model decisions already made, so that',
    'cuando entra el despacho de abogados, la asesoría fiscal o la auditoría, su trabajo es validar y firmar — no empezar de cero':
      'when the law firm, tax advisor or auditor steps in, their job is to validate and sign — not to start from scratch',
    '. Eso reduce honorarios, plazos y, sobre todo, errores de coordinación entre proveedores.':
      '. This reduces fees, timelines, and most of all, coordination errors between vendors.',
    'Lo único que sigue siendo trabajo de un tercero es la programación. Yo defino la arquitectura, el stack, las integraciones, los flujos, los datos y la lógica del producto, y entrego planos que un ingeniero ejecuta. Pero lo que se construye, cómo se conecta y para qué sirve dentro del modelo de negocio, eso ya está decidido antes de que el primer programador toque una línea de código.':
      'The only thing that remains a third party\'s job is the coding. I define the architecture, the stack, the integrations, the flows, the data and the product logic, and deliver blueprints an engineer executes. But what gets built, how it connects, and what it serves within the business model is already decided before the first developer touches a line of code.',
    'El ingeniero ensambla; el sistema ya está pensado.': 'The engineer assembles; the system is already thought through.',
    'Trabajo previo a': 'Prep work for',
    'Sustituye a': 'Replaces a',
    'Despacho jurídico-fiscal': 'Legal-tax firm',
    'Plantillas, estructura societaria propuesta y documentación lista para que el despacho valide y firme.':
      'Templates, proposed corporate structure and documentation ready for the firm to validate and sign.',
    'Consultora estratégica': 'Strategy consultancy',
    'Modelo de negocio, GTM y plan operativo entregados como sistema integrado.':
      'Business model, GTM and operating plan delivered as one integrated system.',
    'Agencia de producto y IA': 'Product & AI agency',
    'Arquitectura, stack y planos de producto listos para que un ingeniero los ejecute.':
      'Architecture, stack and product blueprints ready for an engineer to execute.',
    'Marketing, ops y comercial': 'Marketing, ops & sales',
    'Posicionamiento, funnel, procesos y scripts diseñados como un solo sistema GTM.':
      'Positioning, funnel, processes and scripts designed as one single GTM system.',
    'Una sola cabeza · responsabilidad única sobre cómo encajan las piezas': 'One single mind · single ownership of how the pieces fit',
    'Alcance de los servicios de Praxia': 'Scope of Praxia\'s services',
    'Praxia Atelier es un estudio de': 'Praxia Atelier is a',
    'consultoría estratégica y diseño de ecosistemas de negocio': 'strategic consulting and business ecosystem design studio',
    '. No prestamos servicios de abogacía, asesoría fiscal regulada, intermediación financiera ni representación letrada — para esas funciones trabajamos siempre con':
      '. We do not provide legal practice, regulated tax advisory, financial intermediation or legal representation services — for those functions we always work with',
    'despachos, asesorías y profesionales colegiados de confianza': 'trusted law firms, advisors and licensed professionals',
    'del cliente o de nuestra red, que son quienes firman, validan y se responsabilizan de los actos jurídicos correspondientes.':
      'from the client\'s or our network, who sign, validate and take responsibility for the corresponding legal acts.',
    'Lo que aporta Praxia es la': 'What Praxia provides is the',
    'arquitectura del proyecto': 'architecture of the project',
    ', las': ', the',
    'plantillas y documentación preparatoria': 'templates and preparatory documentation',
    ', y la': ', and the',
    'coordinación con esos profesionales': 'coordination with those professionals',
    ', de forma que su intervención sea más rápida, ordenada y eficiente. Las decisiones jurídico-fiscales finales, la firma de escrituras, el asesoramiento legal individualizado y la auditoría son siempre responsabilidad de los profesionales acreditados que cada cliente designe.':
      ', so their intervention is faster, more orderly and more efficient. Final legal-tax decisions, signing of deeds, individualized legal advice and auditing are always the responsibility of the accredited professionals each client designates.',

    /* === ASISTENTE === */
    'Asistente Praxia': 'Praxia Assistant',
    'Antes de la llamada,': 'Before the call,',
    'deja el contexto preparado': 'leave the context ready',
    '.': '.',
    'Cuéntale a nuestro asistente qué tienes entre manos. En unos minutos te dice si tu caso encaja con el estudio y, si encaja, deja a Marta el contexto preparado para que la primera conversación no empiece en cero.':
      'Tell our assistant what you have on your mind. In a few minutes it lets you know whether your case fits the studio and, if it does, leaves Marta the context ready so the first conversation doesn\'t start from zero.',
    'Cómo funciona': 'How it works',
    'Cuatro preguntas clave para entender dónde está tu proyecto y qué cápsula encaja contigo. Tarda unos cinco minutos.':
      'Four key questions to understand where your project is and which capsule fits you. Takes about five minutes.',
    'Confidencialidad': 'Confidentiality',
    'Toda la conversación es confidencial. Marta solo verá tus respuestas si decides agendar reunión.':
      'The whole conversation is confidential. Marta only sees your answers if you decide to book a meeting.',
    'Si prefieres hablar directamente': 'If you prefer to talk directly',
    'Sin presión. Puedes ir directo al calendario y reservar 45 minutos con Marta.':
      'No pressure. You can go straight to the calendar and book 45 minutes with Marta.',
    'Ir al contacto →': 'Go to contact →',
    'El asistente de Praxia te espera abajo a la derecha.': 'The Praxia assistant is waiting in the bottom-right.',
    'Pulsa la burbuja': 'Click the bubble',
    '"Habla con Praxia"': '"Talk to Praxia"',
    'y empezamos. Cuatro preguntas, cinco minutos, y tendrás claro si tu caso encaja con el estudio.':
      'and we begin. Four questions, five minutes, and you\'ll know whether your case fits the studio.',
    'minutos': 'minutes',
    'preguntas clave': 'key questions',
    'sin compromiso': 'no commitment',
    'Abrir asistente ahora': 'Open assistant now',

    /* === CASOS === */
    'Casos de demostración del estudio': 'Studio demo cases',
    'Dos casos ficticios construidos con el mismo método y el mismo rigor que aplicamos en un proyecto real. Sirven para que veas, antes de contratar nada, exactamente':
      'Fictional cases built with the same method and rigor we apply on real projects. So you can see, before contracting anything, exactly',
    'cómo se ve el entregable': 'what the deliverable looks like',
    ': estructura jurídica, software, mockups navegables, modelo económico y simulador interactivo. Cuando trabajamos contigo, esto se construye con tu marca, tus números y tus protocolos.':
      ': legal structure, software, navigable mockups, economic model and interactive simulator. When we work with you, this is built with your brand, your numbers and your protocols.',
    'Demos íntegras · navegables': 'Full demos · navigable',
    'Pulsa para abrir el caso completo': 'Click to open the full case',
    'Caso 01 · Family business': 'Case 01 · Family business',
    'Bodega Valdescuro': 'Bodega Valdescuro',
    'Tres generaciones haciendo vino. La cuarta abre un club privado y vehículo de coinversión.':
      'Three generations making wine. The fourth opens a private club and co-investment vehicle.',
    'crecimiento año 3': 'growth year 3',
    'vehículo año 2': 'vehicle year 2',
    'entidades': 'entities',
    'Landing · área del socio · avatar · back office · simulador': 'Landing · member area · avatar · back office · simulator',
    'Roadmap accionable 12 meses con responsables': 'Actionable 12-month roadmap with owners',
    'Estructura jurídica · AIE + Asociación + Holding': 'Legal structure · EIG + Association + Holding',
    'Sector · Ribera del Duero · vino premium': 'Sector · Ribera del Duero · premium wine',
    'Abrir demo →': 'Open demo →',
    'Caso 02 · Health-tech': 'Case 02 · Health-tech',
    'Clínica Lumen': 'Clínica Lumen',
    'De clínica privada a plataforma de longevidad con IA y comunidad de pacientes.':
      'From private clinic to longevity platform with AI and patient community.',
    'ARPU paciente': 'patient ARPU',
    'socios premium': 'premium members',
    'Mockups · pacientes · avatar Sofia · back office · simulador interactivo':
      'Mockups · patients · Sofia avatar · back office · interactive simulator',
    'Roadmap accionable 24 semanas con responsables': 'Actionable 24-week roadmap with owners',
    'Riesgos sanitarios + EU AI Act + RGPD art. 9 tipificados': 'Health risks + EU AI Act + GDPR art. 9 typified',
    'Sector · medicina integrativa · longevidad': 'Sector · integrative medicine · longevity',
    'Caso 03 · Real estate': 'Case 03 · Real estate',
    'Casa Vento': 'Casa Vento',
    'Estudio de diseño y reforma de pisos que se profesionaliza como operadora con vehículo de coinversión.':
      'Design and refurbishment studio professionalized as an operator with a co-investment vehicle.',
    'capacidad año 3': 'capacity year 3',
    'TIR coinversor': 'co-investor IRR',
    'Oportunidad · Living · Avatar · Panel · Simulador': 'Opportunity · Living · Avatar · Panel · Simulator',
    'Índice Calidad propio · 7 ejes de scoring': 'Proprietary Quality Index · 7 scoring axes',
    'Sector · residencial premium · Madrid': 'Sector · premium residential · Madrid',
    /* === Demo 4 · Mesa de Trabajo === */
    'Caso 04 · Founder-cliente': 'Case 04 · Founder-client',
    'Mesa de Trabajo': 'Workspace',
    'El método aplicado al propio estudio. Praxia operando con sus 8 capas integradas.':
      'The method applied to the studio itself. Praxia operating with its own 8 integrated layers.',
    'departamentos integrados': 'integrated departments',
    'visible y navegable': 'visible and navigable',
    'único cliente · el estudio': 'single client · the studio',
    '8 departamentos · backoffice · dashboards · simuladores': '8 departments · backoffice · dashboards · simulators',
    'Roadmap del propio estudio mostrado en abierto': 'Studio\'s own roadmap shown in the open',
    'Demo del método aplicado a sí mismo': 'Demo of the method applied to itself',
    'Tipo · meta-caso · método visible': 'Type · meta-case · visible method',
    'Cada demo abre en una pestaña nueva con mockups navegables, simulador económico y roadmap accionable':
      'Each demo opens in a new tab with navigable mockups, economic simulator and actionable roadmap',
    'Nota honesta': 'Honest note',
    'El estudio acaba de abrir y los primeros clientes están en conversación. Por eso preferimos enseñarte':
      'The studio has just opened and the first clients are in conversation. That\'s why we prefer to show you',
    'demos ficticias hechas con el mismo rigor que un proyecto real': 'fictional demos built with the same rigor as a real project',
    'antes que inflar testimonios. Cuando trabajemos juntos, todo lo que ves en las demos se construye con tu marca, tus números reales y tus protocolos — y, si lo autorizas, tu caso se convertirá en el siguiente.':
      'rather than inflate testimonials. When we work together, everything you see in the demos is built with your brand, your real numbers and your protocols — and, if you authorize it, your case will become the next one.',

    /* === TRAYECTORIA DETRÁS DEL ESTUDIO · 3 proyectos reales === */
    'Trayectoria detrás del estudio': 'Track record behind the studio',
    'El estudio es nuevo. La metodología no.': 'The studio is new. The methodology isn\'t.',
    'Praxia Atelier abre en 2026, pero el método se ha construido durante años diseñando y operando proyectos reales. Tres de ellos sostienen la experiencia que sustenta lo que hacemos hoy:':
      'Praxia Atelier opens in 2026, but the method has been built over years designing and operating real projects. Three of them ground the experience that backs what we do today:',
    'Proyecto 01': 'Project 01',
    'Proyecto 02': 'Project 02',
    'Proyecto 03': 'Project 03',
    'Ecosistema digital de una AIE con plataforma de educación emocional.': 'Digital ecosystem of an EIG with an emotional education platform.',
    'Diseño y aterrizaje del ecosistema completo de una': 'Design and grounding of the complete ecosystem of an',
    'Agrupación de Interés Económico': 'Economic Interest Grouping',
    'articulada con asociación y plataforma digital: producto web, área de socios, lógica de comunidad, integraciones de pago y comunicación, modelo económico de la AIE y operativa interna. Caso real, anonimizado por confidencialidad con la asociación.':
      'articulated with an association and a digital platform: web product, member area, community logic, payment and communication integrations, EIG economic model and internal operations. Real case, anonymized for confidentiality with the association.',
    'Las 8 capas · diseño y aterrizaje': 'All 8 layers · design and grounding',
    'Proyecto 02 · Propio': 'Project 02 · Own',
    'Ecosistema emocional propio con IA en producción.': 'Own emotional ecosystem with AI in production.',
    'Diseño, construcción y operación de un': 'Design, build and operation of a',
    'ecosistema digital propio en producción': 'proprietary digital ecosystem in production',
    'con tres líneas (B2C · marketplace · enterprise): avatar conversacional con RAG, motor de matching propio, autoría editorial, métricas beta, plan financiero, marco RGPD y cap table. Es donde se han probado las técnicas que hoy aplicamos en Cápsula 01 y 02.':
      'with three lines (B2C · marketplace · enterprise): conversational avatar with RAG, proprietary matching engine, editorial authoring, beta metrics, financial plan, GDPR framework and cap table. It\'s where the techniques we apply today in Capsules 01 and 02 have been tested.',
    'Las 8 capas · proyecto propio en activo': 'All 8 layers · own project, active',
    'Operaciones en real estate con vehículo de coinversión.': 'Real estate operations with co-investment vehicle.',
    'Estructuración de operaciones inmobiliarias con': 'Structuring of real estate operations with',
    'vehículo privado de coinversión': 'private co-investment vehicle',
    'entre socios, modelo económico por activos y separación clara entre operadora y propietaria. Trabajo previo al modelo que hoy aplicamos en casos como Casa Vento.':
      'between partners, asset-based economic model, and clear separation between operator and owner. Prior work to the model we apply today in cases like Casa Vento.',
    'Capas · Jurídico + Modelo + Capital': 'Layers · Legal + Model + Capital',
    'Tres formas distintas de haber tocado las 8 capas:': 'Three different ways of having touched the 8 layers:',
    'como diseñadora para un cliente': 'as designer for a client',
    '(proyecto 01),': '(project 01),',
    'como fundadora y operadora de un producto propio': 'as founder and operator of an own product',
    '(proyecto 02), y': '(project 02), and',
    'como estructuradora de operaciones reales': 'as structurer of real operations',
    '(proyecto 03). Por confidencialidad y por respeto a los socios y comunidades de cada uno, no nombramos los proyectos por su marca pública — pero la experiencia operativa, no solo consultora, es lo que sostiene el método. Cuando trabajemos juntos, todo lo que ves en los casos demo se construye con tu marca, tus números reales y tus protocolos.':
      '(project 03). For confidentiality and out of respect for each project\'s partners and communities, we don\'t name them by their public brand — but operational experience, not just consulting, is what backs the method. When we work together, everything you see in the demo cases is built with your brand, your real numbers and your protocols.',

    /* === PARA QUIÉN === */
    'Para quién trabajamos': 'Who we work with',
    'Encajamos contigo si…': 'We\'re a fit if…',
    'Tienes un proyecto real (no una idea suelta) y prisa por arrancar.':
      'You have a real project (not a loose idea) and are in a hurry to start.',
    'Quieres captar capital y necesitas que lo jurídico, lo fiscal y lo digital cuadren.':
      'You want to raise capital and need legal, tax and digital to line up.',
    'Estás cansado de proveedores que cubren un pedazo y no se hablan entre sí.':
      'You\'re tired of vendors who cover a slice and don\'t talk to each other.',
    'Eres family office, founder de health-tech / wellness, despacho boutique o promotor de club privado.':
      'You\'re a family office, health-tech / wellness founder, boutique firm, or private club promoter.',
    'No encajamos si…': 'We\'re not a fit if…',
    'Buscas una agencia que ejecute lo que ya tienes definido.':
      'You\'re looking for an agency to execute what you\'ve already defined.',
    'Quieres pagar por horas y micro-gestionar entregables.':
      'You want to pay by the hour and micromanage deliverables.',
    'No tienes claro el problema real; sólo "quiero una app".':
      'The real problem isn\'t clear yet; you just "want an app."',
    'Esperas que alguien externo asuma riesgo de fundador sin alineamiento.':
      'You expect an outsider to take founder risk without alignment.',

    /* === FAQ === */
    'Preguntas que recibimos a menudo': 'Questions we get often',
    '¿Por qué un estudio de autor y no una agencia?': 'Why an authored studio and not an agency?',
    'Las agencias venden horas y especializan al máximo. Un proyecto de ecosistema requiere una sola voz que decida simultáneamente cómo encaja la AIE, qué prompt usa el avatar y cuánto cobra el plan Pro. Esa decisión integrada no la puede tomar un comité.':
      'Agencies sell hours and specialize to the maximum. An ecosystem project requires a single voice that simultaneously decides how the EIG fits, what prompt the avatar uses, and how much the Pro plan charges. A committee can\'t make that integrated decision.',
    '¿Sois despacho fiscal?': 'Are you a tax firm?',
    'No. Diseñamos la estructura jurídico-fiscal y la dejamos lista para que un asesor fiscal y un notario la cierren. Trabajamos con un panel de despachos boutique de confianza, sin exclusividad. Tú eliges con quién firmar.':
      'No. We design the legal-tax structure and leave it ready for a tax advisor and a notary to close. We work with a panel of trusted boutique firms, without exclusivity. You choose who to sign with.',
    '¿Programáis vosotros el software?': 'Do you code the software yourselves?',
    'En Cápsula 01 no — entregamos arquitectura y prototipo navegable. En Cápsula 02 dirigimos el equipo técnico, integramos APIs y entregamos go-live. Si ya tienes equipo técnico, podemos coordinarlo en lugar de reemplazarlo.':
      'In Capsule 01 we don\'t — we deliver architecture and a navigable prototype. In Capsule 02 we direct the technical team, integrate APIs and deliver go-live. If you already have a technical team, we can coordinate it instead of replacing it.',
    '¿Trabajáis con NDA antes de hablar de números?': 'Do you work under NDA before discussing numbers?',
    'Sí. La primera llamada es bajo NDA mutuo. Si decidimos avanzar, el dossier completo se entrega contra señal del 30%.':
      'Yes. The first call is under mutual NDA. If we decide to move forward, the full dossier is delivered against a 30% deposit.',
    '¿Qué pasa con la propiedad intelectual?': 'What about intellectual property?',
    'Lo específico de tu proyecto es 100% tuyo desde el día uno. Los componentes genéricos del estudio (prompts base, plantillas de matching, modelos económicos) se ceden bajo licencia de uso. Es el equivalente a que un arquitecto te dé los planos de tu casa, pero sus técnicas y métodos sigan siendo suyos.':
      'What\'s specific to your project is 100% yours from day one. The studio\'s generic components (base prompts, matching templates, economic models) are licensed for use. It\'s the equivalent of an architect giving you the plans for your house, while their techniques and methods remain theirs.',

    /* === CONTACTO === */
    'Empezamos con una conversación.': 'We start with a conversation.',
    '30 minutos por videollamada con Marta. Sin coste. Sin compromiso. Y siempre te llevas algo a casa.':
      '30 minutes by video call with Marta. No cost. No commitment. And you always leave with something.',
    'Reservas la llamada': 'You book the call',
    '30 minutos en el calendario de Marta. Tú eliges el día y la hora.':
      '30 minutes on Marta\'s calendar. You pick the day and time.',
    'Hablamos de tu proyecto': 'We talk about your project',
    'Sin guion comercial. Marta escucha, hace preguntas, entiende tu caso. Si Praxia no encaja, te lo dice.':
      'No sales script. Marta listens, asks questions, understands your case. If Praxia isn\'t a fit, she\'ll tell you.',
    'Recibes el one-pager': 'You receive the one-pager',
    'En 48 horas recibes un PDF con': 'Within 48 hours you receive a PDF with',
    'específicos para tu proyecto. Gratis. El valor es tuyo aunque no sigamos juntos.':
      'specific to your project. Free. The value is yours even if we don\'t continue together.',
    'Sin compromiso. Si después decides que quieres seguir con Praxia, perfecto. Si no, te quedas con el one-pager y te ahorras decisiones equivocadas. Esa honestidad es parte de cómo trabajamos.':
      'No commitment. If you later decide to continue with Praxia, perfect. If not, you keep the one-pager and avoid wrong decisions. That honesty is part of how we work.',
    'Sin tarjeta · Sin compromiso · One-pager garantizado': 'No card · No commitment · One-pager guaranteed',
    '¿Prefieres otro canal?': 'Prefer another channel?',
    '· Madrid · Barcelona · Remote ·': '· Madrid · Barcelona · Remote ·',

    /* === SECCIÓN HOME · CONTENIDOS · DIARIO / NEWSLETTER / INSIGHTS / COLABORADORES === */
    'Lectura, suscripción y referencias.': 'Reading, subscription and references.',
    'Tres formas de seguir lo que hacemos sin tener que reservar una llamada.':
      'Three ways to follow what we do without having to book a call.',
    'Notas y ensayos del estudio.': 'Notes and essays from the studio.',
    'Lectura larga sobre cómo se diseñan ecosistemas digitales completos. Un ensayo cuando hay algo que decir.':
      'Long-form reading on how complete digital ecosystems are designed. An essay when there\'s something to say.',
    'Leer el Diario →': 'Read the Journal →',
    'Recibe el próximo Diario.': 'Get the next Journal.',
    'Una nota directa al email cada vez que publicamos algo en el Diario. Sin spam, sin promociones.':
      'A note straight to your email each time we publish something in the Journal. No spam, no promotions.',
    'Suscribirme →': 'Subscribe →',
    'Apariciones, podcasts y referencias.': 'Press, podcasts and references.',
    'Recopilación de prensa, entrevistas, podcasts y vídeos externos donde el estudio o Marta aparecen.':
      'A collection of press, interviews, podcasts and external videos where the studio or Marta appear.',
    'Ver insights →': 'See insights →',
    '¿Quieres trabajar con nosotros?': 'Want to work with us?',
    'Bolsa de freelancers y proveedores de confianza — desarrollo, diseño, IA, jurídico-fiscal, marketing. Inscríbete.':
      'Roster of trusted freelancers and providers — development, design, AI, legal-tax, marketing. Apply.',
    'Ver perfiles →': 'See roles →',

    /* === FOOTER === */
    'Ecosystem architecture · est. 2026': 'Ecosystem architecture · est. 2026',
    'Madrid, España': 'Madrid, Spain',
    'Aviso legal': 'Legal notice',
    'Alcance de servicios': 'Scope of services',
    'Política de privacidad': 'Privacy policy',
    'Praxia Atelier es un estudio de consultoría estratégica y diseño. No prestamos servicios de abogacía, asesoría fiscal regulada ni auditoría — esas funciones las ejercen siempre profesionales colegiados con los que coordinamos.':
      'Praxia Atelier is a strategic consulting and design studio. We do not provide legal practice, regulated tax advisory or auditing services — those functions are always performed by licensed professionals we coordinate with.',
    'Ver alcance →': 'See scope →',
    '© 2026 · Marta Escobar Rojas · Praxia Atelier · Todos los derechos reservados':
      '© 2026 · Marta Escobar Rojas · Praxia Atelier · All rights reserved',
    'Hecho en Madrid': 'Made in Madrid',

    /* === COLABORADORES · página de bolsa de freelancers === */
    'Atelier': 'Atelier',
    'Colaboradores · Praxia Atelier': 'Collaborators · Praxia Atelier',
    '¿Quieres trabajar con nosotros': 'Want to work with us',
    'Praxia Atelier diseña ecosistemas digitales completos. Yo dirijo, defino la arquitectura y entrego los planos. Quien construye, integra y opera son freelancers especialistas':
      'Praxia Atelier designs complete digital ecosystems. I lead, define the architecture and deliver the blueprints. The people who build, integrate and operate are specialist freelancers',
    'No es una agencia con plantilla fija. Es una bolsa abierta de profesionales que entran cuando un proyecto necesita su capa. Si tu trabajo encaja con cómo trabajamos, inscríbete y te tendremos en cuenta cuando aparezca un proyecto de tu perfil.':
      'This is not an agency with a fixed payroll. It is an open pool of professionals who join when a project needs their layer. If your work fits how we work, sign up and we will keep you in mind when a project matches your profile.',
    'Inscribirme en la bolsa': 'Join the pool',
    'Ver perfiles que buscamos': 'See profiles we look for',
    'Cómo trabajamos con freelancers.': 'How we work with freelancers.',
    'Por proyecto, no por horas.': 'By project, not by the hour.',
    'Cuando entra un proyecto de Cápsula 02, te llamamos con un alcance acotado, un plazo y un fee cerrado. No vendemos horas a cliente — tampoco las compramos.':
      'When a Capsule 02 project comes in, we call you with a defined scope, a timeline and a closed fee. We don\'t sell hours to clients — we don\'t buy them either.',
    'Praxia coordina y firma con cliente.': 'Praxia coordinates and signs with the client.',
    'Tú facturas a Praxia. Praxia factura al cliente. Tu interlocutor es siempre el estudio, nunca el cliente directamente — salvo que el proyecto lo requiera explícitamente y se acuerde así.':
      'You invoice Praxia. Praxia invoices the client. Your point of contact is always the studio, never the client directly — unless the project explicitly requires it and we agree to it.',
    'Sin exclusividad.': 'No exclusivity.',
    'No te pedimos exclusividad ni dedicación completa. Trabajamos con gente que ya tiene su propia cartera y dice que sí cuando un proyecto le encaja.':
      'We don\'t ask for exclusivity or full-time dedication. We work with people who already have their own portfolio and say yes when a project fits them.',
    'NDA de oficio.': 'NDA by default.',
    'Antes de entrar en cualquier proyecto firmamos un NDA mutuo. Los proyectos del estudio son frecuentemente sensibles — family business, captación de capital, vehículos de coinversión — y la confidencialidad es estructural.':
      'Before joining any project we sign a mutual NDA. Studio projects are often sensitive — family business, capital raising, co-investment vehicles — and confidentiality is structural.',
    'Pago a 15-30 días.': 'Payment in 15–30 days.',
    'Pagamos rápido y bien. Tarifa de mercado o por encima si el perfil es escaso. Sin regateos a posteriori, sin "esto entra en lo acordado" cuando claramente no entraba.':
      'We pay quickly and well. Market rate or above when the profile is scarce. No haggling after the fact, no "this was already in scope" when it clearly was not.',
    'Crédito visible si lo quieres.': 'Visible credit if you want it.',
    'Si el proyecto sale a la luz pública y tú quieres aparecer como colaborador en la página de créditos, perfecto. Si prefieres no aparecer, también. Tú decides.':
      'If the project goes public and you want to appear as a collaborator on the credits page, great. If you prefer not to appear, also fine. You decide.',
    'Los catorce perfiles que aparecen una y otra vez.': 'The fourteen profiles that come up again and again.',
    'Agrupados por la capa del método de Praxia con la que más colaboran. Si tu perfil no aparece literalmente pero crees que encaja, inscríbete igual y dilo en el campo libre del formulario.':
      'Grouped by the Praxia method layer they most collaborate with. If your profile doesn\'t appear literally but you think it fits, sign up anyway and say so in the free-text field of the form.',
    'Producto y Software · Cápsula 02': 'Product & Software · Capsule 02',
    'Quien construye el ecosistema.': 'Those who build the ecosystem.',
    'Full-stack Senior · Next.js / TypeScript / Node': 'Senior Full-stack · Next.js / TypeScript / Node',
    'El perfil base. Web pública, área de socio, back office, APIs. Idealmente con experiencia en proyectos donde lo legal-fiscal condiciona el producto (membresías, AIE, vehículos de coinversión).':
      'The base profile. Public site, member area, back office, APIs. Ideally with experience on projects where legal-tax design shapes the product (memberships, AIE, co-investment vehicles).',
    'Next.js · TypeScript · Postgres / Supabase · Vercel · Stripe · Cal.com · Resend':
      'Next.js · TypeScript · Postgres / Supabase · Vercel · Stripe · Cal.com · Resend',
    'Frontend Specialist con criterio editorial': 'Frontend Specialist with editorial sensibility',
    'Convertir Figma en código limpio sin perder sensibilidad de marca. Animación sutil, accesibilidad real, respeto del sistema de diseño. No agencia genérica.':
      'Turning Figma into clean code without losing brand sensibility. Subtle animation, real accessibility, respect for the design system. Not generic agency work.',
    'React / Next.js · Tailwind · Framer Motion · Figma · Storybook':
      'React / Next.js · Tailwind · Framer Motion · Figma · Storybook',
    'Backend e Integraciones': 'Backend & Integrations',
    'El conector. Pasarelas de pago, firma electrónica, WhatsApp Business API, webhooks, automatizaciones serias. Uno de los perfiles más raros y más necesarios del estudio.':
      'The connector. Payment gateways, e-signature, WhatsApp Business API, webhooks, serious automation. One of the rarest and most needed profiles in the studio.',
    'Node / Python · Stripe · DocuSign / Signaturit · WhatsApp Cloud API · Twilio · Resend':
      'Node / Python · Stripe · DocuSign / Signaturit · WhatsApp Cloud API · Twilio · Resend',
    'Diseñador/a UX/UI editorial': 'Editorial UX/UI Designer',
    'Diseño con criterio editorial, sistema de diseño coherente, sensibilidad de marca premium. Para áreas de socio, dossiers y materiales de inversor que se ven en una pantalla y se imprimen igual de bien.':
      'Design with editorial criteria, a coherent design system, premium brand sensibility. For member areas, dossiers and investor materials that look right on screen and print equally well.',
    'Figma · Tokens · Tipografía editorial · Sistemas de diseño escalables':
      'Figma · Tokens · Editorial typography · Scalable design systems',
    'DevOps / Infraestructura': 'DevOps / Infrastructure',
    'El que evita que las cosas se caigan. Despliegue, monitorización, backups, dominios, certificados, performance. Edge serverless, no Kubernetes pesado.':
      'The one who keeps things from falling over. Deployment, monitoring, backups, domains, certificates, performance. Edge serverless, not heavy Kubernetes.',
    'Vercel · Netlify · Cloudflare · Railway · Supabase · Sentry · monitorización':
      'Vercel · Netlify · Cloudflare · Railway · Supabase · Sentry · monitoring',
    'IA aplicada · Cápsula 02': 'Applied AI · Capsule 02',
    'Quien diseña la inteligencia del ecosistema.': 'Those who design the ecosystem\'s intelligence.',
    'Ingeniero/a de IA aplicada (LLMs, RAG, embeddings)': 'Applied AI Engineer (LLMs, RAG, embeddings)',
    'Diseño y construcción de avatares conversacionales, motores de matching, recomendadores y automatización con IA. Prompt engineering serio, no API call básica.':
      'Designing and building conversational avatars, matching engines, recommenders and AI automation. Serious prompt engineering, not basic API calls.',
    'Claude API · OpenAI · LangChain · Vector DBs (Pinecone / Weaviate / pgvector) · evaluación':
      'Claude API · OpenAI · LangChain · Vector DBs (Pinecone / Weaviate / pgvector) · evaluation',
    'Especialista en automatización (n8n, Make, Zapier, Notion API)': 'Automation Specialist (n8n, Make, Zapier, Notion API)',
    'El que conecta sistemas sin código pesado. Onboarding automatizado, flujos de notificación, sincronización entre Notion / Stripe / Cal.com / CRM, captura de leads.':
      'The one who connects systems without heavy code. Automated onboarding, notification flows, sync between Notion / Stripe / Cal.com / CRM, lead capture.',
    'n8n · Make · Zapier · Notion API · webhooks · Airtable · Google Apps Script':
      'n8n · Make · Zapier · Notion API · webhooks · Airtable · Google Apps Script',
    'Jurídico-fiscal y Capital · Cápsula 01': 'Legal-tax & Capital · Capsule 01',
    'Quien firma, valida y se responsabiliza.': 'Those who sign, validate and take responsibility.',
    'Praxia diseña la estructura y prepara la documentación. Estos profesionales colegiados son quienes firman, validan y se responsabilizan ante notarías, administraciones y reguladores. Trabajamos sin exclusividad — nuestros clientes pueden traer sus propios profesionales o usar nuestra red.':
      'Praxia designs the structure and prepares the documentation. These licensed professionals are the ones who sign, validate and take responsibility before notaries, administrations and regulators. We work without exclusivity — our clients can bring their own professionals or use our network.',
    'Abogado/a mercantil-fiscal · estructuras complejas': 'Corporate-tax Lawyer · complex structures',
    'Especializado/a en AIE, holdings, asociaciones del 49/2002, family office. Que entienda producto digital y modelo económico — no solo escrituras estándar. Despacho boutique mejor que big four.':
      'Specialised in AIE, holdings, 49/2002 non-profits, family office. Understands digital product and economic model — not just standard deeds. Boutique firm preferred over big four.',
    'Constitución de AIE · holdings familiares · vehículos privados de coinversión · contratos de membresía':
      'AIE incorporation · family holdings · private co-investment vehicles · membership agreements',
    'Notaría de confianza': 'Trusted Notary',
    'Para escrituras, AIE, modificaciones estatutarias, poderes. Idealmente en Madrid, con experiencia en estructuras societarias no estándar.':
      'For deeds, AIE, by-law amendments, powers of attorney. Ideally in Madrid, with experience in non-standard corporate structures.',
    'Escrituras de constitución · ampliaciones de capital · poderes de coinversión':
      'Incorporation deeds · capital increases · co-investment powers of attorney',
    'Asesor/a fiscal · Ley 49/2002, AIE y vehículos de inversión': 'Tax Advisor · Law 49/2002, AIE and investment vehicles',
    'Distinto del fiscal de cabecera del cliente: este sabe de lo no estándar. Mecenazgo, fiscalidad de socios, tributación de vehículos privados, optimización legal.':
      'Different from the client\'s regular tax advisor: this one knows non-standard work. Patronage, member taxation, private vehicle taxation, legal optimisation.',
    'Encaje fiscal de AIE · deducciones de mecenazgo · plan fiscal de socios fundadores':
      'AIE tax fit · patronage deductions · tax plan for founding members',
    'Marketing, Operaciones, Comercial y Contenido': 'Marketing, Operations, Sales & Content',
    'Quien le pone palabras, procesos y método de venta al ecosistema.': 'Those who give the ecosystem its words, processes and sales method.',
    'Editor/a y copywriter editorial bilingüe (ES/EN)': 'Bilingual Editor & Copywriter (ES/EN)',
    'Para artículos del Diario, dossiers de inversor, materiales comerciales con voz Praxia. Tono editorial cercano, no marketing barato. Que entienda de negocio y producto.':
      'For Journal articles, investor dossiers, sales materials with Praxia voice. Close editorial tone, not cheap marketing. Understands business and product.',
    'Diario editorial · one-pagers de inversor · landings de cápsula · case studies':
      'Editorial Journal · investor one-pagers · capsule landing pages · case studies',
    'Marketing técnico y SEO': 'Technical Marketing & SEO',
    'Implementación de estrategias de captación, SEO técnico, analítica seria, ads cuando aplique. Para clientes que pasan por Cápsula 04 y para el propio Praxia.':
      'Implementing acquisition strategies, technical SEO, serious analytics, ads when relevant. For clients going through Capsule 04 and for Praxia itself.',
    'GA4 · Search Console · Ahrefs / SEMrush · Schema · Meta / Google Ads':
      'GA4 · Search Console · Ahrefs / SEMrush · Schema · Meta / Google Ads',
    'Project Manager / Operadora de proyecto': 'Project Manager / Operator',
    'Quien coordina el día a día de Cápsula 02 cuando el estudio está en otro frente. RACI, sprint planning, coordinación de freelancers, comunicación con cliente.':
      'Coordinating the day-to-day of Capsule 02 when the studio is on another front. RACI, sprint planning, freelance coordination, client communication.',
    'Notion · Linear · Slack · sprints quincenales · stand-ups asíncronos':
      'Notion · Linear · Slack · biweekly sprints · async stand-ups',
    'Editor/a audiovisual y creador/a de contenido': 'Audiovisual Editor & Content Creator',
    'Vídeos cortos, podcast del estudio si sale, contenido para LinkedIn, casos de cliente en formato visual. Sensibilidad editorial, no agencia youtuber.':
      'Short videos, studio podcast if launched, LinkedIn content, client cases in visual format. Editorial sensibility, not a youtuber agency.',
    'Premiere / Final Cut · CapCut · Descript · Riverside · Figma':
      'Premiere / Final Cut · CapCut · Descript · Riverside · Figma',
    'Otros perfiles que buscamos puntualmente': 'Other profiles we look for occasionally',
    'No los abrimos como bolsa, pero si encajas, inscríbete igual con tu perfil concreto en el campo libre: fotógrafo/a editorial de retrato y producto':
      'We don\'t open these as a pool, but if you fit, sign up anyway with your specific profile in the free-text field: editorial photographer of portrait and product',
    'asesor/a en captación de capital y relación con fondos': 'capital-raising advisor and investor relations',
    'abogado/a de propiedad intelectual y privacidad': 'IP and privacy lawyer',
    'diseñador/a de marca y branding': 'brand and branding designer',
    'traductor/a profesional ES↔EN especializado en negocio y legal': 'professional ES↔EN translator specialised in business and legal',
    'Cuéntanos quién eres.': 'Tell us who you are.',
    'Rellena el formulario en cinco minutos. Lo leeremos personalmente. Si tu perfil encaja con algún proyecto en marcha o previsto, te contactaremos. Si no encaja todavía, te quedas en la bolsa para cuando aparezca algo.':
      'Fill in the form in five minutes. We will read it personally. If your profile fits an active or upcoming project, we will reach out. If not yet, you stay in the pool until something comes up.',
    'Nombre y apellidos': 'Full name',
    'Email': 'Email',
    'Ciudad / país': 'City / country',
    'Tipo de profesional': 'Type of professional',
    '¿Qué perfil(es) marcas? Puedes seleccionar varios.': 'Which profile(s) apply? You can select several.',
    '01 · Full-stack Senior (Next.js / TS / Node)': '01 · Senior Full-stack (Next.js / TS / Node)',
    '02 · Frontend editorial': '02 · Editorial Frontend',
    '03 · Backend e Integraciones': '03 · Backend & Integrations',
    '04 · Diseño UX/UI editorial': '04 · Editorial UX/UI Design',
    '05 · DevOps / Infraestructura': '05 · DevOps / Infrastructure',
    '06 · IA aplicada (LLMs / RAG)': '06 · Applied AI (LLMs / RAG)',
    '07 · Automatización (n8n / Make)': '07 · Automation (n8n / Make)',
    '08 · Abogado/a mercantil-fiscal': '08 · Corporate-tax Lawyer',
    '09 · Notaría de confianza': '09 · Trusted Notary',
    '10 · Asesor fiscal AIE / 49-2002': '10 · Tax Advisor AIE / 49-2002',
    '11 · Copywriter editorial bilingüe': '11 · Bilingual editorial Copywriter',
    '12 · Marketing técnico y SEO': '12 · Technical Marketing & SEO',
    '13 · Project Manager / Operadora': '13 · Project Manager / Operator',
    '14 · Editor/a audiovisual': '14 · Audiovisual Editor',
    'Otro perfil (especifícalo abajo)': 'Other profile (specify below)',
    'Si has marcado "Otro" o tu perfil es híbrido, descríbelo': 'If you ticked "Other" or your profile is hybrid, describe it',
    'Años de experiencia profesional': 'Years of professional experience',
    'Cuéntanos quién eres y qué te diferencia · 4-6 líneas': 'Tell us who you are and what sets you apart · 4–6 lines',
    'Portfolio / web / GitHub': 'Portfolio / website / GitHub',
    'LinkedIn (opcional)': 'LinkedIn (optional)',
    'Tarifa orientativa': 'Indicative rate',
    'Disponibilidad típica': 'Typical availability',
    'Idiomas de trabajo': 'Working languages',
    'Español': 'Spanish',
    'Inglés': 'English',
    'Catalán': 'Catalan',
    'Francés': 'French',
    'He leído y acepto la política de privacidad': 'I have read and accept the privacy policy',
    'Enviar inscripción': 'Submit application',
    'Confidencial · respondemos solo si encajas con un proyecto activo o previsto.': 'Confidential · we only reply if you fit an active or upcoming project.',
    'Inicio': 'Home',
    'Praxia Atelier es un estudio de consultoría estratégica y diseño. No prestamos servicios de abogacía, asesoría fiscal regulada ni auditoría — esas funciones las ejercen siempre profesionales colegiados con los que coordinamos. Ver alcance →':
      'Praxia Atelier is a strategic consulting and design studio. We do not provide legal practice, regulated tax advisory or auditing services — those functions are always performed by licensed professionals we coordinate with. See scope →',

    /* === CHIPS DE NAV adicionales (para colaboradores y otras páginas) === */
    'Estudio': 'Studio',
    'Bolsa': 'Pool',
    'Cómo trabajamos': 'How we work',
    'Perfiles': 'Profiles',
    'Inscripción': 'Apply',
    'Inscribirse': 'Apply now',

    /* === Hero · mensaje de aterrizaje === */
    'Aterrizamos tu idea y la convertimos en un': 'We ground your idea and turn it into a',
    'negocio real, digitalizado y optimizado': 'real, digitalised and optimised business',
    '— con sistema operativo, página web y todo lo que necesitas para empezar a funcionar.':
      '— with operating system, website and everything you need to start running.',

    /* === Hero rediseñado · panel Inicio (versión diseñador gráfico) === */
    'Estudio · Madrid': 'Studio · Madrid',
    'Reservar 30 min con Marta': 'Book 30 min with Marta',
    'Ver casos navegables': 'See navigable cases',
    '· Gratis · sin compromiso': '· Free · no commitment',

    /* Idea / Empresa cards rediseñadas */
    'Tienes una intuición de negocio pero no sabes por dónde empezar a estructurarla.':
      'You have a business intuition but don\'t know where to start structuring it.',
    'Empezamos por ahí — en un brainstorm te devolvemos opciones reales.':
      'We start there — in a brainstorm we hand you real options.',
    'Tu empresa funciona pero quieres abrir una nueva vía sin canibalizar el core.':
      'Your company works but you want to open a new line without cannibalising the core.',
    'Diseñamos la capa siguiente — completa, lista para operar.':
      'We design the next layer — complete, ready to operate.',

    /* Promesa */
    'La promesa': 'The promise',
    'Reserva 30 minutos y en las 48 horas siguientes recibes un one-pager gratis con tres movimientos accionables específicos para tu proyecto.':
      'Book thirty minutes and within 48 hours you receive a free one-pager with three actionable moves specific to your project.',
    '— Sin contratar nada · El valor es tuyo aunque no sigamos juntos':
      '— No contract required · The value is yours even if we don\'t continue together',

    /* Cuatro situaciones · header reescrito */
    'Si te reconoces en alguna, encajamos. Si no, mejor saberlo antes de gastar 30 minutos.':
      'If you recognise yourself in any, we fit. If not, better to know before spending 30 minutes.',

    /* Stat band kicker */
    'El formato': 'The format',
    'Días para el blueprint': 'Days to blueprint',
    'Entidades coordinadas': 'Entities coordinated',
    'Disciplinas, una voz': 'Disciplines, one voice',
    'Prototipo navegable': 'Navigable prototype',

    /* === Panel Inicio · optimización (claim ampliado + 4 perfiles + entrada suave) === */
    'listos para captar capital,': 'ready to raise capital,',
    'multiplicar el ROI o, simplemente, saber qué hacer la próxima semana.': 'multiply ROI or, simply, to know exactly what to do next week.',

    /* Subtítulo paralelo */
    'Idea sin aterrizar': 'Idea without grounding',
    'Tienes una intuición de negocio pero no sabes por dónde empezar a estructurarla.': 'You have a business intuition but don\'t know where to start structuring it.',
    'Empezamos por ahí — en un brainstorm te devolvemos opciones reales.': 'We start there — in a brainstorm we hand you real options.',
    'Empresa con nueva vía': 'Company with a new line',
    'Tu empresa funciona pero quieres abrir una nueva vía de monetización sin canibalizar el core.': 'Your company works but you want to open a new revenue line without cannibalising the core.',
    'Diseñamos la capa siguiente — completa, lista para operar.': 'We design the next layer — complete, ready to operate.',
    'Estructura jurídico-fiscal, software, avatar con IA, modelo económico y materiales para inversores — un único estudio, una única voz.':
      'Legal-tax structure, software, AI avatar, economic model and investor materials — one studio, one voice.',

    /* Bloque ¿Esto es para ti? */
    '¿Esto es para ti?': 'Is this for you?',
    'Cuatro situaciones donde nos llaman.': 'Four situations where we get called.',
    'Si te reconoces en alguna de estas cuatro, encajamos. Si no, probablemente no — y mejor sabérlo antes de gastar 30 minutos.':
      'If you recognise yourself in any of these four, we fit. If not, probably not — better to know before spending 30 minutes.',
    'Tipo 01': 'Type 01',
    'Tengo una idea pero no sé estructurarla.': 'I have an idea but don\'t know how to structure it.',
    'Founder solo o en pareja con una intuición clara. Necesitas saber si es viable y, si lo es, qué pieza primero.':
      'Solo or paired founder with a clear intuition. You need to know if it\'s viable and, if it is, which piece comes first.',
    'Tipo 02': 'Type 02',
    'Tengo empresa y quiero abrir una nueva vía.': 'I have a company and want to open a new line.',
    'Tu empresa factura entre 1 y 10 M€, está estancada o quiere salto de modelo. Necesitas la capa siguiente sin canibalizar el core.':
      'Your company bills between 1 and 10 M€, is stuck or wants a model leap. You need the next layer without cannibalising the core.',
    'Tipo 03': 'Type 03',
    'Family office montando vehículo nuevo.': 'Family office launching a new vehicle.',
    'Capital propio o mixto. Buscas estructura jurídico-fiscal, vehículo de coinversión y plan operativo defendible delante de fondos y notarías.':
      'Own or mixed capital. You\'re looking for legal-tax structure, co-investment vehicle and operating plan that holds up before funds and notaries.',
    'Tipo 04': 'Type 04',
    'Necesito captar capital con prototipo navegable.': 'I need to raise capital with a navigable prototype.',
    'Tienes ronda en 60-90 días. Necesitas one-pager, deck, modelo económico vivo y un prototipo que se enseñe a un fondo el lunes.':
      'You have a round in 60–90 days. You need a one-pager, deck, live economic model and a prototype to show a fund on Monday.',

    /* Frase de entrada suave en problema */
    'Si nunca has montado un proyecto digital serio, esto te va a sonar abstracto. Si lo has intentado, te va a sonar familiar.':
      'If you have never built a serious digital project, this will sound abstract. If you have tried, it will sound familiar.',

    /* === Botón descargar dossier PDF === */
    'Descargar dossier (PDF)': 'Download dossier (PDF)',

    /* === Casavera · copy 'Inmobiliaria Casavera quería...' === */
    'Inmobiliaria Casavera': 'Casavera real estate',
    'quería dejar de gestionar alquileres, ventas e inversión en Madrid con': 'wanted to stop running rentals, sales and investment in Madrid with',
    '. Tenía clientes recurrentes y reputación, pero ningún sistema que conectara captación con visita, visita con reserva, reserva con firma — y nada de eso con el plan financiero del año.':
      '. It had recurring clients and reputation, but no system connecting acquisition to visit, visit to booking, booking to signing — and none of that to the year\'s financial plan.',

    /* Block labels swapped */
    'Bloque 1 · Para entender la trayectoria': 'Block 1 · To understand the track record',
    'Bloque 2 · Para entender el método': 'Block 2 · To understand the method',
    'Destacado': 'Featured',

    /* === Casavera · versión anonimizada (sin nombre Carolina) === */
    'Lo que necesitaba Casavera': 'What Casavera needed',
    'Una agente boutique con cartera propia llevaba años gestionando alquileres, ventas e inversión en Madrid con':
      'A boutique agent with her own portfolio had spent years managing rentals, sales and investment in Madrid with',
    'la operativa repartida en cuatro Excels y el correo': 'operations scattered across four spreadsheets and email',
    '. Tenía clientes recurrentes y reputación, pero ningún sistema que conectara captación con visita, visita con reserva, reserva con firma — y nada de eso con el plan financiero del año.':
      '. She had recurring clients and reputation, but no system connecting acquisition to visit, visit to booking, booking to signing — and none of that to the year\'s financial plan.',
    'Lo que entregó Praxia': 'What Praxia delivered',
    'Un': 'A',
    ': la web pública con cuatro puertas de entrada (invertir, vender, alquilar, buscar) y el back office propio con vista panorámica de los 10 procesos del negocio — desde el catálogo hasta el cash flow proyectado mes a mes.':
      ': a public website with four entry doors (invest, sell, rent, search) and a custom back office with a panoramic view of the 10 business processes — from the catalogue to monthly projected cash flow.',

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
    '. Lo que no se puede enseñar por confidencialidad va anonimizado.': '. What can\'t be shown for confidentiality reasons is anonymised.',

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
      'Bilingual website with four entries (invest, sell or rent, search, "I can\'t find what I\'m looking for"), a deterministic chatbot that filters leads and an end-to-end acquisition flow up to e-signature. Designed so every visitor fits their intent in under 5 seconds.',

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
      '. For confidentiality reasons we don\'t name some projects by their public brand — but operational experience, not just consulting, is what sustains the method.',

    /* === DIARIO · página índice === */
    'Diario · Praxia Atelier · Notas sobre arquitectura de ecosistemas digitales':
      'Journal · Praxia Atelier · Notes on digital ecosystem architecture',
    'Diario · Praxia Atelier': 'Journal · Praxia Atelier',
    'Notas sobre cómo se diseñan': 'Notes on how to design',
    'ecosistemas digitales completos': 'complete digital ecosystems',
    'Ensayos, casos y notas operativas escritos desde el estudio. Cómo se conecta lo jurídico con el modelo económico, qué pieza de IA cambia la economía unitaria, qué decisión técnica habilita o bloquea la captación de capital. Lo que aprendemos diseñando, contado en voz directa.':
      'Essays, cases and operational notes written from the studio. How legal structure connects with the economic model, which AI piece changes unit economics, which technical decision enables or blocks capital raising. What we learn designing, told in direct voice.',
    'Por Marta Escobar Rojas': 'By Marta Escobar Rojas',
    'Madrid · 2026': 'Madrid · 2026',
    'Publicación irregular · cuando hay algo que decir': 'Irregular publishing · when there is something to say',
    'Listado de artículos': 'Article list',
    'Últimas entradas': 'Latest entries',
    'Recibir el próximo →': 'Get the next one →',

    /* Artículo 04 · ecosistema digital empresa atascada */
    'Artículo 04 · Diseñar ecosistema digital empresa atascada': 'Article 04 · Designing a digital ecosystem for a stuck company',
    '15 mayo 2026': 'May 15, 2026',
    'Lectura 12 min': '12 min read',
    'Diseño de ecosistemas': 'Ecosystem design',
    'Cómo diseñar un ecosistema digital cuando tu empresa está atascada — y por qué casi siempre el problema no está donde parece.':
      'How to design a digital ecosystem when your company is stuck — and why the problem is almost never where it seems to be.',
    'Los negocios no se atascan por falta de talento, ni por falta de mercado, ni por falta de dinero. Se atascan porque las piezas no están conectadas. Cinco síntomas, ocho capas y lo que he aprendido diseñando ecosistemas para fundadores, family offices y empresas operando.':
      'Businesses don\'t get stuck for lack of talent, market or money. They get stuck because the pieces aren\'t connected. Five symptoms, eight layers and what I have learned designing ecosystems for founders, family offices and operating companies.',
    'Leer →': 'Read →',

    /* Artículo 02 · IA aplicada a real estate */
    'Artículo 02 · IA aplicada a real estate': 'Article 02 · Applied AI in real estate',
    '8 mayo 2026': 'May 8, 2026',
    'Lectura 7 min': '7 min read',
    'Qué se puede automatizar con IA en una operadora de real estate — y qué conviene que siga haciendo una persona.':
      'What can be automated with AI in a real estate operator — and what should still be done by a person.',
    'Cuatro tareas donde la IA crea valor real en una operadora inmobiliaria, y cuatro donde destruye más del que crea. La diferencia no la marca la tecnología — la marca la naturaleza de la tarea.':
      'Four tasks where AI creates real value in a real estate operator, and four where it destroys more than it creates. The difference is not the technology — it is the nature of the task.',

    /* Artículo 03 · AIE coinversión privada */
    'Artículo 03 · AIE coinversión privada': 'Article 03 · AIE for private co-investment',
    '1 mayo 2026': 'May 1, 2026',
    'Por qué una AIE cambia la economía de cualquier vehículo de coinversión privado.':
      'Why an AIE changes the economics of any private co-investment vehicle.',
    'La Agrupación de Interés Económico no es solo una estructura jurídica. Es lo que permite que un grupo de socios coinvierta sin entrar en CNMV ni constituir un fondo regulado — y por qué ese matiz cambia modelos de negocio enteros.':
      'The Economic Interest Grouping (AIE) is not just a legal structure. It is what allows a group of partners to co-invest without entering CNMV oversight or setting up a regulated fund — and why that nuance changes entire business models.',

    /* Artículo 01 · Club de socios y ecosistema digital de comunidad */
    'Artículo 01 · Club de socios y ecosistema digital de comunidad': 'Article 01 · Members club and digital community ecosystem',
    'Producto digital y comunidad': 'Digital product and community',
    'Lo que un club de socios premium necesita para que el networking funcione de verdad — más allá de un grupo de WhatsApp.':
      'What a premium members club needs for networking to actually work — beyond a WhatsApp group.',
    'La mayoría de las comunidades B2B mueren al sexto mes. No por falta de socios, ni por falta de afinidad. Por falta de ecosistema. Lo que aprendí diseñando uno.':
      'Most B2B communities die by the sixth month. Not for lack of members, nor lack of affinity. For lack of ecosystem. What I learned designing one.',

    /* Newsletter section */
    'Suscripción': 'Subscription',
    'Una nota cada vez que publicamos algo en el Diario. Sin newsletter semanal de relleno. Sin promociones. Solo el ensayo cuando está listo, directo al email.':
      'A note every time we publish something in the Journal. No weekly filler newsletter. No promotions. Only the essay when it is ready, straight to your inbox.',
    'Confidencial · sin compartir · cancelas cuando quieras': 'Confidential · not shared · unsubscribe anytime',
    'Tu email': 'Your email',
    'Nombre (opcional)': 'Name (optional)',
    'Suscribirme al Diario': 'Subscribe to the Journal',
    'Al suscribirte aceptas la': 'By subscribing you accept the',

    /* CTA editorial */
    '¿Tienes una idea que se cuenta sola?': 'Do you have an idea that tells itself?',
    'Si el Diario te resuena, probablemente la conversación con Marta también lo haga. Reserva 30 minutos sin compromiso.':
      'If the Journal resonates, the conversation with Marta probably will too. Book 30 minutes, no commitment.',
    'hola@tuempresa.com': 'hello@yourcompany.com',
    'Tu nombre': 'Your name',

    /* Nav chips */
    'Artículos': 'Articles',
    'Newsletter': 'Newsletter',
    'Suscribirse': 'Subscribe',

    /* === INSIGHTS · página de apariciones === */
    'Insights · Praxia Atelier · Apariciones, podcasts y referencias externas':
      'Insights · Praxia Atelier · Press, podcasts and external references',
    'Insights · Praxia Atelier': 'Insights · Praxia Atelier',
    'Apariciones, podcasts y': 'Press, podcasts and',
    'referencias externas': 'external references',
    'Cuando el estudio aparece en prensa, en un podcast, en una entrevista o en un panel, lo recogemos aquí con el enlace original. Es la forma más rápida de ver la voz de Praxia fuera del propio estudio.':
      'When the studio appears in the press, on a podcast, in an interview or on a panel, we collect it here with the original link. It is the fastest way to see Praxia\'s voice outside the studio itself.',
    'Curado por Marta Escobar Rojas': 'Curated by Marta Escobar Rojas',
    'Ordenado por fecha': 'Sorted by date',
    'Filtros (placeholder · activarlo cuando haya >5 entradas)': 'Filters (placeholder · enable when there are more than 5 entries)',
    'Vídeo / charla': 'Video / talk',
    'Mención': 'Mention',
    'Listado de insights': 'Insights list',
    'Últimas apariciones': 'Latest appearances',
    'Estado vacío editorial · cuando aún no hay entradas': 'Editorial empty state · when there are no entries yet',
    'Esta página se irá llenando con el tiempo': 'This page will fill up over time',
    'Aún no hay apariciones públicas registradas.': 'No public appearances yet.',
    'El estudio acaba de abrir. A medida que vayamos apareciendo en medios, podcasts, entrevistas o paneles, este será el sitio donde se recogerán todos los enlaces — para que cualquier persona pueda escuchar y leer directamente las fuentes originales.':
      'The studio has just opened. As we appear in media, podcasts, interviews or panels, this is where every link will be collected — so anyone can hear and read the original sources directly.',
    'Si quieres entrevistarme, citar al estudio o invitarme a un panel, puedes escribirme a': 'If you want to interview me, cite the studio or invite me to a panel, you can write to',
    '¿Quieres entrevistarme o citar al estudio?': 'Want to interview me or cite the studio?',
    'Escribe a': 'Write to',
    '. Respondo a peticiones de prensa, podcasts y paneles si encajan con la voz del estudio.': '. I reply to press, podcast and panel requests when they fit the studio\'s voice.',

    /* nav chips for Insights page */
    'Suscríbete': 'Subscribe',
    'Bienvenida': 'Welcome',

    /* === COLABORADORES · ronda 3 (placeholders y precios) === */
    'fotógrafo/a editorial de retrato y producto': 'editorial photographer of portrait and product',
    '€40-60 / hora': '€40–60 / hour',
    '€60-90 / hora': '€60–90 / hour',
    '€90-150 / hora': '€90–150 / hour',
    '€150+ / hora': '€150+ / hour',
    'hola@tudominio.com': 'hello@yourdomain.com',
    'https://linkedin.com/in/...': 'https://linkedin.com/in/...',

    /* === COLABORADORES · ronda 2 (fragmentos y opciones de form) === */
    'Colaboradores · Praxia Atelier · Bolsa de freelancers y proveedores de confianza':
      'Collaborators · Praxia Atelier · Pool of trusted freelancers and providers',
    '¿Quieres trabajar': 'Want to work',
    'con nosotros': 'with us',
    'Praxia Atelier diseña ecosistemas digitales completos. Yo dirijo, defino la arquitectura y entrego los planos.':
      'Praxia Atelier designs complete digital ecosystems. I lead, define the architecture and deliver the blueprints.',
    'Quien construye, integra y opera son freelancers especialistas': 'The people who build, integrate and operate are specialist freelancers',
    'de confianza con los que colaboro proyecto a proyecto.': 'I trust and collaborate with on a project-by-project basis.',
    'Cómo trabajamos · expectativas': 'How we work · expectations',
    'Antes de inscribirte': 'Before you sign up',
    'Perfiles que buscamos': 'Profiles we look for',
    'Capa Producto y Software': 'Layer · Product & Software',
    '01 · Desarrollo': '01 · Development',
    'Stack típico': 'Typical stack',
    '03 · Integraciones': '03 · Integrations',
    '04 · Diseño': '04 · Design',
    '05 · Infraestructura': '05 · Infrastructure',
    'Capa IA': 'Layer · AI',
    '06 · IA aplicada': '06 · Applied AI',
    '07 · Automatización': '07 · Automation',
    'Capa Jurídico-fiscal': 'Layer · Legal-tax',
    '08 · Legal': '08 · Legal',
    'Casos típicos': 'Typical cases',
    '09 · Notaría': '09 · Notary',
    '10 · Fiscal': '10 · Tax',
    'Capa Marketing, Operaciones y Comercial': 'Layer · Marketing, Operations & Sales',
    '11 · Editorial': '11 · Editorial',
    '12 · Marketing': '12 · Marketing',
    '13 · Project': '13 · Project',
    '14 · Audiovisual': '14 · Audiovisual',
    'Otros perfiles': 'Other profiles',
    'No los abrimos como bolsa, pero si encajas, inscríbete igual con tu perfil concreto en el campo libre:':
      'We don\'t open these as a pool, but if you fit, sign up anyway with your specific profile in the free-text field:',
    'Inscripción a la bolsa': 'Pool application',
    'Datos básicos': 'Basic information',
    '— Selecciona —': '— Select —',
    'Freelance / autónomo': 'Freelance / self-employed',
    'Estudio o agencia pequeña': 'Small studio or agency',
    'Despacho profesional (jurídico, fiscal, notaría)': 'Professional firm (legal, tax, notary)',
    '0–3 años': '0–3 years',
    '3–7 años': '3–7 years',
    '7–15 años': '7–15 years',
    '15+ años': '15+ years',
    'Tarifa y disponibilidad': 'Rate and availability',
    'Por proyecto (acordamos al brief)': 'By project (agreed at brief)',
    'Proyectos puntuales': 'One-off projects',
    'Parcial (10-20 h/sem)': 'Part-time (10–20 h/week)',
    'Completa cuando hay proyecto': 'Full-time when there is a project',
    'Disponibilidad full-time': 'Full-time availability',
    'He leído y acepto la': 'I have read and accept the',
    'política de privacidad': 'privacy policy',
    '. Mis datos se usarán únicamente para evaluar la inscripción y contactarme cuando aparezca un proyecto compatible.':
      '. My data will be used solely to evaluate the application and contact me when a compatible project arises.',
    'Madrid · España': 'Madrid · Spain',
    'Ej. Dirección de arte editorial · Branding · Investigación de usuarios · Producción de eventos…':
      'E.g. Editorial art direction · Branding · User research · Event production…',
    'Empieza por una frase corta sobre lo que mejor haces. Después uno o dos proyectos concretos de los que estés orgulloso/a. Termina con qué tipo de proyecto te encaja más.':
      'Start with a short sentence about what you do best. Then one or two specific projects you are proud of. End with what kind of project fits you most.',
  };

  /* ============================================================
     LÓGICA · recorre nodos de texto y los traduce
     ============================================================ */

  // Cache: por cada nodo de texto que traducimos, guardamos el original ES.
  // Así podemos volver a ES sin recargar.
  const ORIGINAL = new WeakMap();

  function isSkipNode(node) {
    if (!node || !node.parentNode) return true;
    const tag = node.parentNode.tagName;
    if (!tag) return true;
    if (tag === 'SCRIPT' || tag === 'STYLE' || tag === 'NOSCRIPT') return true;
    // Saltar el chatbox flotante (que tiene su propio idioma)
    let p = node.parentNode;
    while (p) {
      if (p.id === 'pchat-panel' || p.id === 'pchat-fab') return true;
      if (p.classList && (p.classList.contains('praxia-lang-switcher'))) return true;
      p = p.parentNode;
    }
    return false;
  }

  function walkAndTranslate(root, lang) {
    const walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, null);
    const toUpdate = [];
    let n;
    while ((n = walker.nextNode())) {
      if (isSkipNode(n)) continue;
      const raw = n.nodeValue;
      const trimmed = raw.replace(/\s+/g, ' ').trim();
      if (!trimmed) continue;

      // Guardar original ES la primera vez
      if (!ORIGINAL.has(n)) ORIGINAL.set(n, raw);

      if (lang === 'es') {
        // Restaurar original
        const orig = ORIGINAL.get(n);
        if (n.nodeValue !== orig) toUpdate.push([n, orig]);
      } else if (lang === 'en') {
        if (DICT[trimmed]) {
          // Preservar espacios alrededor del texto
          const leading = raw.match(/^\s*/)[0];
          const trailing = raw.match(/\s*$/)[0];
          const translated = leading + DICT[trimmed] + trailing;
          if (n.nodeValue !== translated) toUpdate.push([n, translated]);
        }
      }
    }
    toUpdate.forEach(function (pair) { pair[0].nodeValue = pair[1]; });
  }

  /* ============================================================
     Mapeo de páginas internas ES → EN
     Estrategia actual: traducción in-place — la misma URL sirve
     contenido ES y EN según el switcher. NO reescribimos los hrefs
     porque las versiones _EN.html no existen como archivos separados.
     Si en el futuro se generan páginas EN dedicadas, basta con
     añadirlas aquí.
     ============================================================ */
  const PAGE_MAP_ES_TO_EN = {
    // intencionadamente vacío — todas las páginas se traducen in-place
  };
  const PAGE_MAP_EN_TO_ES = {};
  Object.keys(PAGE_MAP_ES_TO_EN).forEach(function (k) { PAGE_MAP_EN_TO_ES[PAGE_MAP_ES_TO_EN[k]] = k; });

  function rewriteInternalLinks(lang) {
    const map = lang === 'en' ? PAGE_MAP_ES_TO_EN : PAGE_MAP_EN_TO_ES;
    document.querySelectorAll('a[href]').forEach(function (a) {
      // Per-link override: data-i18n-href="en:Other.pdf" lets a single link
      // swap its href when the user switches language. Format "<lang>:<href>".
      // Multiple langs supported separated by '|', e.g. "en:foo.pdf|fr:bar.pdf".
      const i18nHref = a.dataset.i18nHref;
      if (i18nHref) {
        if (!a.dataset.origHref) a.dataset.origHref = a.getAttribute('href');
        let resolved = a.dataset.origHref;
        i18nHref.split('|').forEach(function (rule) {
          const idx = rule.indexOf(':');
          if (idx === -1) return;
          const ruleLang = rule.slice(0, idx).trim();
          const ruleHref = rule.slice(idx + 1).trim();
          if (ruleLang === lang) resolved = ruleHref;
        });
        a.setAttribute('href', resolved);
        return;
      }

      const href = a.getAttribute('href');
      if (!href) return;
      // ignorar enlaces externos, mailto, tel, anchors
      if (/^(https?:|mailto:|tel:|#)/.test(href)) return;
      // separar archivo y fragmento
      const hashIdx = href.indexOf('#');
      const file = hashIdx === -1 ? href : href.slice(0, hashIdx);
      const hash = hashIdx === -1 ? '' : href.slice(hashIdx);
      // strip "./"
      const cleanFile = file.replace(/^\.\//, '');
      if (map[cleanFile]) {
        a.setAttribute('href', map[cleanFile] + hash);
        // guardar el original para volver
        if (!a.dataset.origHref) a.dataset.origHref = href;
      } else if (a.dataset.origHref) {
        // si ya tenía un original guardado y no aplica el mapa, restaurar
        a.setAttribute('href', a.dataset.origHref);
      }
    });
  }

  function applyLang(lang) {
    document.documentElement.lang = lang;
    walkAndTranslate(document.body, lang);
    rewriteInternalLinks(lang);
    document.querySelectorAll('.praxia-lang-switcher button').forEach(function (b) {
      b.classList.toggle('is-active', b.getAttribute('data-lang') === lang);
    });
    try { localStorage.setItem('praxia_lang', lang); } catch (e) {}
    // Translated chips can take more or less width, which forces the deck
    // header to wrap differently. Notify deck.js so it re-measures and
    // re-positions the panel area below.
    document.dispatchEvent(new CustomEvent('praxia:i18n-applied', { detail: { lang: lang } }));
  }

  function getLang() {
    try { return localStorage.getItem('praxia_lang') || 'es'; } catch (e) { return 'es'; }
  }

  /* ============================================================
     UI · switcher en el header
     ============================================================ */
  function injectSwitcher() {
    const header = document.querySelector('header');
    if (!header) return;
    if (header.querySelector('.praxia-lang-switcher')) return;

    // Preferir el contenedor de acciones del header si existe (CTA + switcher juntos)
    const actions = header.querySelector('#praxia-header-actions');
    const wrapper = actions
      || header.querySelector('.flex.items-center.justify-between')
      || header.firstElementChild;
    if (!wrapper) return;

    const switcher = document.createElement('div');
    switcher.className = 'praxia-lang-switcher';
    switcher.innerHTML =
      '<button type="button" data-lang="es">ES</button>' +
      '<button type="button" data-lang="en">EN</button>';
    wrapper.appendChild(switcher);

    switcher.querySelectorAll('button').forEach(function (b) {
      b.addEventListener('click', function () { applyLang(b.getAttribute('data-lang')); });
    });
  }

  function injectStyles() {
    if (document.getElementById('praxia-i18n-styles')) return;
    const s = document.createElement('style');
    s.id = 'praxia-i18n-styles';
    s.textContent = [
      '.praxia-lang-switcher{display:inline-flex;border:1px solid var(--line,#e6e1d6);border-radius:2px;overflow:hidden;font-family:"JetBrains Mono",ui-monospace,monospace;font-size:10px;letter-spacing:.1em;text-transform:uppercase;align-self:center;flex-shrink:0;line-height:1;white-space:nowrap}',
      '.praxia-lang-switcher button{padding:6px 9px;background:transparent;color:var(--ink-soft,#44485a);border:0;cursor:pointer;font:inherit;letter-spacing:inherit;text-transform:inherit;transition:background .15s,color .15s;min-height:28px;display:inline-flex;align-items:center;justify-content:center}',
      '.praxia-lang-switcher button.is-active{background:var(--ink,#1a1f2e);color:var(--paper,#faf8f3)}',
      '.praxia-lang-switcher button:hover:not(.is-active){background:var(--line,#e6e1d6);color:var(--ink,#1a1f2e)}'
    ].join('');
    document.head.appendChild(s);
  }

  function init() {
    injectStyles();
    injectSwitcher();
    applyLang(getLang());
  }

  // Public API so other scripts (e.g. praxia-deck.js) can re-translate when
  // they inject new DOM nodes after the initial pass.
  window.PraxiaI18n = {
    current: function () { return getLang(); },
    refresh: function () { applyLang(getLang()); },
    set: function (lang) { applyLang(lang); }
  };

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
