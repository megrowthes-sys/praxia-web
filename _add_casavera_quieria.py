"""Add EN translations for the new Casavera copy and the swapped block labels."""
from _add_translations import append_block

BLOCK = """
    /* === Casavera · copy 'Inmobiliaria Casavera quería...' === */
    'Inmobiliaria Casavera': 'Casavera real estate',
    'quería dejar de gestionar alquileres, ventas e inversión en Madrid con': 'wanted to stop running rentals, sales and investment in Madrid with',
    '. Tenía clientes recurrentes y reputación, pero ningún sistema que conectara captación con visita, visita con reserva, reserva con firma — y nada de eso con el plan financiero del año.':
      '. It had recurring clients and reputation, but no system connecting acquisition to visit, visit to booking, booking to signing — and none of that to the year\\'s financial plan.',

    /* Block labels swapped */
    'Bloque 1 · Para entender la trayectoria': 'Block 1 · To understand the track record',
    'Bloque 2 · Para entender el método': 'Block 2 · To understand the method',
    'Destacado': 'Featured',
"""
if __name__ == "__main__":
    append_block(BLOCK)
