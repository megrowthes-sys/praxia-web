# Carpeta de imágenes · Praxia Atelier

Aquí viven todas las imágenes del sitio. Organizadas por sección para que sea fácil mantener.

## Estructura

```
imagenes/
├── insights/        ← imágenes de las apariciones externas (podcasts, prensa, vídeos)
├── diario/          ← imágenes destacadas y cuerpo de los artículos del Diario
├── colaboradores/   ← (futuro) fotos de freelancers que colaboren visiblemente
└── perfil/          ← fotos personales de Marta y del estudio
```

## Reglas de nombres

Para que las imágenes se mantengan ordenadas y sea fácil localizarlas:

- **Insights:** `[fecha]-[medio]-[descriptor-corto].jpg`
  - Ejemplos:
    - `2026-04-itnig-podcast.jpg`
    - `2026-05-elpais-aie-vehiculos.jpg`
    - `2026-06-startupfest-panel.jpg`

- **Diario:** `[slug-del-articulo]-[descriptor].jpg`
  - Ejemplos:
    - `aie-vehiculo-coinversion-cover.jpg`
    - `aie-vehiculo-coinversion-figura1.jpg`

- **Perfil:** `marta-[contexto].jpg`
  - Ejemplos: `marta-retrato.jpg`, `marta-estudio.jpg`, `marta-evento.jpg`

## Optimización antes de subir

Para que la web cargue rápido:

- **Tamaño máximo:** 1600 px de ancho. Más grande no aporta nada en pantallas web.
- **Peso máximo:** 200 KB por imagen. Si pesa más, comprímela.
- **Formato:** `.jpg` para fotos, `.png` para imágenes con transparencia o gráficos planos, `.webp` si quieres aún más ligero.
- **Alt text:** siempre se rellena cuando se inserta en HTML (lo hace el asistente). Es importante para SEO y accesibilidad.

### Herramientas gratis para optimizar

- **TinyJPG** (https://tinyjpg.com): comprime sin perder calidad visible.
- **Squoosh** (https://squoosh.app): permite ajustar calidad y formato manualmente.
- **Photoshop / Affinity / Pixelmator:** "Exportar para web" con calidad 75-85%.

---

**Última actualización:** 2026-05-01
