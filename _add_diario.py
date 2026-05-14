"""Add Diario index page translations."""
from _add_translations import append_block

BLOCK = """
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
      'Businesses don\\'t get stuck for lack of talent, market or money. They get stuck because the pieces aren\\'t connected. Five symptoms, eight layers and what I have learned designing ecosystems for founders, family offices and operating companies.',
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
"""
if __name__ == "__main__":
    append_block(BLOCK)
