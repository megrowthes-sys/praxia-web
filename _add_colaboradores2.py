"""Add the missing Colaboradores translations (round 2)."""
from _add_translations import append_block

BLOCK = """
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
      'We don\\'t open these as a pool, but if you fit, sign up anyway with your specific profile in the free-text field:',
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
"""

if __name__ == "__main__":
    append_block(BLOCK)
