"""Add the last 9 missing Colaboradores translations."""
from _add_translations import append_block

BLOCK = """
    /* === COLABORADORES · ronda 3 (placeholders y precios) === */
    'fotógrafo/a editorial de retrato y producto': 'editorial photographer of portrait and product',
    '€40-60 / hora': '€40–60 / hour',
    '€60-90 / hora': '€60–90 / hour',
    '€90-150 / hora': '€90–150 / hour',
    '€150+ / hora': '€150+ / hour',
    'hola@tudominio.com': 'hello@yourdomain.com',
    'https://linkedin.com/in/...': 'https://linkedin.com/in/...',
"""
if __name__ == "__main__":
    append_block(BLOCK)
