"""Add EN translations for the anonymised Casavera card."""
from _add_translations import append_block

BLOCK = """
    /* === Casavera · versión anonimizada (sin nombre Carolina) === */
    'Lo que necesitaba Casavera': 'What Casavera needed',
    'Una agente boutique con cartera propia llevaba años gestionando alquileres, ventas e inversión en Madrid con':
      'A boutique agent with her own portfolio had spent years managing rentals, sales and investment in Madrid with',
    'la operativa repartida en cuatro Excels y el correo': 'operations scattered across four spreadsheets and email',
    '. Tenía clientes recurrentes y reputación, pero ningún sistema que conectara captación con visita, visita con reserva, reserva con firma — y nada de eso con el plan financiero del año.':
      '. She had recurring clients and reputation, but no system connecting acquisition to visit, visit to booking, booking to signing — and none of that to the year\\'s financial plan.',
    'Lo que entregó Praxia': 'What Praxia delivered',
    'Un': 'A',
    ': la web pública con cuatro puertas de entrada (invertir, vender, alquilar, buscar) y el back office propio con vista panorámica de los 10 procesos del negocio — desde el catálogo hasta el cash flow proyectado mes a mes.':
      ': a public website with four entry doors (invest, sell, rent, search) and a custom back office with a panoramic view of the 10 business processes — from the catalogue to monthly projected cash flow.',
"""
if __name__ == "__main__":
    append_block(BLOCK)
