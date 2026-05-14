"""Add EN translations for the optimised panel Inicio."""
from _add_translations import append_block

BLOCK = """
    /* === Panel Inicio · optimización (claim ampliado + 4 perfiles + entrada suave) === */
    'listos para captar capital,': 'ready to raise capital,',
    'multiplicar el ROI o, simplemente, saber qué hacer la próxima semana.': 'multiply ROI or, simply, to know exactly what to do next week.',

    /* Subtítulo paralelo */
    'Idea sin aterrizar': 'Idea without grounding',
    'Tienes una intuición de negocio pero no sabes por dónde empezar a estructurarla.': 'You have a business intuition but don\\'t know where to start structuring it.',
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
    'Tengo una idea pero no sé estructurarla.': 'I have an idea but don\\'t know how to structure it.',
    'Founder solo o en pareja con una intuición clara. Necesitas saber si es viable y, si lo es, qué pieza primero.':
      'Solo or paired founder with a clear intuition. You need to know if it\\'s viable and, if it is, which piece comes first.',
    'Tipo 02': 'Type 02',
    'Tengo empresa y quiero abrir una nueva vía.': 'I have a company and want to open a new line.',
    'Tu empresa factura entre 1 y 10 M€, está estancada o quiere salto de modelo. Necesitas la capa siguiente sin canibalizar el core.':
      'Your company bills between 1 and 10 M€, is stuck or wants a model leap. You need the next layer without cannibalising the core.',
    'Tipo 03': 'Type 03',
    'Family office montando vehículo nuevo.': 'Family office launching a new vehicle.',
    'Capital propio o mixto. Buscas estructura jurídico-fiscal, vehículo de coinversión y plan operativo defendible delante de fondos y notarías.':
      'Own or mixed capital. You\\'re looking for legal-tax structure, co-investment vehicle and operating plan that holds up before funds and notaries.',
    'Tipo 04': 'Type 04',
    'Necesito captar capital con prototipo navegable.': 'I need to raise capital with a navigable prototype.',
    'Tienes ronda en 60-90 días. Necesitas one-pager, deck, modelo económico vivo y un prototipo que se enseñe a un fondo el lunes.':
      'You have a round in 60–90 days. You need a one-pager, deck, live economic model and a prototype to show a fund on Monday.',

    /* Frase de entrada suave en problema */
    'Si nunca has montado un proyecto digital serio, esto te va a sonar abstracto. Si lo has intentado, te va a sonar familiar.':
      'If you have never built a serious digital project, this will sound abstract. If you have tried, it will sound familiar.',
"""
if __name__ == "__main__":
    append_block(BLOCK)
