"""Add EN translation for the new dossier download button."""
from _add_translations import append_block

BLOCK = """
    /* === Botón descargar dossier PDF === */
    'Descargar dossier (PDF)': 'Download dossier (PDF)',
"""
if __name__ == "__main__":
    append_block(BLOCK)
