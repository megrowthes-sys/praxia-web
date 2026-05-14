# Praxia Atelier · Manual de la carpeta web

**Última actualización:** 1 de mayo de 2026

Este documento explica cómo está organizada la carpeta `Praxia-web` y cómo trabajar contigo (Marta) y conmigo (el asistente) cuando quieras añadir contenido nuevo o actualizar la web.

---

## 1 · Qué hay en esta carpeta

Esta es **la carpeta que se sube a Netlify** cada vez que actualizas la web. Todo lo que está aquí dentro queda público en `praxia-atelier.net`. Cualquier archivo que NO debe ser público no debe estar dentro de esta carpeta.

### Archivos centrales (no se tocan a mano)

| Archivo | Qué es |
|---|---|
| `index.html` | Home del sitio |
| `diario.html` | Página índice del Diario |
| `insights.html` | Página índice de Insights |
| `colaboradores.html` | Bolsa de freelancers |
| `aviso-legal.html` | Aviso legal con sección de alcance |
| `privacidad.html` | Política de privacidad |
| `Praxia_Atelier_Caso_Bodega_Valdescuro.html` | Demo de caso · family business · vino |
| `Praxia_Atelier_Caso_Casa_Vento.html` | Demo de caso · real estate |
| `Praxia_Atelier_Caso_Clinica_Lumen.html` | Demo de caso · health-tech |
| `Praxia_Atelier_Caso_Mesa_de_Trabajo.html` | Demo · founder-cliente · método aplicado al estudio |
| `Praxia_Atelier_Chat.html` | Página dedicada del asistente |
| `Avatar_Proximamente.html` | Página placeholder del avatar (próximamente) |
| `praxia-chatbox.css` | Estilos del chatbot lateral |
| `praxia-chatbox.js` | Lógica del chatbot lateral |
| `praxia-i18n.js` | Switcher ES/EN y traducciones |

### Subcarpetas

| Carpeta | Para qué |
|---|---|
| `diario/` | Aquí van las entradas individuales del Diario. Cada artículo es un archivo `[slug].html`. |
| `imagenes/` | Todas las imágenes del sitio, organizadas por sección (`imagenes/insights/`, `imagenes/diario/`, `imagenes/perfil/`). Cada subcarpeta tiene su propio README explicando convenciones de nombre y optimización. |
| `_entradas-pendientes/` | Borradores y plantillas. **Esta carpeta empieza con guion bajo a propósito** — es señal interna de que es un archivo de trabajo, no público (Netlify lo sube igual, pero ningún enlace de la web pública apunta aquí, así que nadie lo encuentra por casualidad). |

---

## 2 · Cómo añadir un artículo nuevo al Diario

### Lo que tú haces

Me mandas un mensaje con esta información:

```
Tengo un artículo nuevo para el Diario:

TÍTULO: [título del artículo]
SUBTÍTULO/ENTRADILLA: [1-2 frases gancho]
CATEGORÍA: [ej. Modelo económico, IA aplicada, Jurídico-fiscal, Capital]
FECHA: [hoy o la que quieras]
LECTURA APROXIMADA: [X minutos]
ETIQUETAS: [3-5 etiquetas separadas por coma]

CUERPO:

[el texto del artículo, en párrafos. Puedes usar **negrita**, _cursiva_ y enlaces como [texto](url). Si quieres dividirlo en secciones, usa H2: ## Subtítulo grande, H3: ### Subtítulo pequeño. Si quieres una cita destacada, ponla con > delante.]
```

### Lo que yo hago

1. Duplico la plantilla `diario/PLANTILLA-articulo.html`.
2. La renombro a `diario/[slug].html` (slug = título corto en minúsculas, sin tildes ni espacios, separado por guiones · ej. `aie-vehiculo-coinversion-family-business`).
3. Relleno todos los marcadores `[TÍTULO]`, `[FECHA]`, `[CUERPO]`, etc.
4. Genero la versión inglesa `diario/[slug]_EN.html` si me pasas también la traducción (o me dices que la hagamos juntos).
5. Edito `diario.html` para añadir la tarjeta del artículo nuevo en el listado, en orden cronológico (lo más reciente arriba).
6. Te aviso de que está listo.

### Lo que tú haces después

1. Abres la carpeta `Praxia-web` en Finder.
2. La arrastras entera al panel de Netlify (zona "Drag and drop your site folder here").
3. En 30-60 segundos está online.

---

## 3 · Cómo añadir un Insight (aparición externa) nuevo

Insights son apariciones tuyas en prensa, podcasts, vídeos, paneles, entrevistas, menciones, etc.

### Lo que tú haces

Me mandas un mensaje con esta información (la plantilla completa está en `_entradas-pendientes/PLANTILLA-insight.txt`):

```
Nuevo Insight:

TIPO: [Prensa · Podcast · Vídeo · Entrevista · Mención · Panel]
FECHA: [YYYY-MM o YYYY-MM-DD]
MEDIO: [ej. El País Negocios · Itnig Podcast · LinkedIn]
TÍTULO: [título exacto del artículo o episodio]
RESUMEN: [2-3 líneas sobre el tema y por qué importa]
ENLACE: [URL pública al contenido]
IMAGEN: [opcional · adjúntala al chat]
```

**Si tienes imagen** (carátula del podcast, foto del artículo, miniatura del vídeo, etc.): adjúntala al chat junto con el texto. La tarjeta saldrá con imagen al lado, mucho más vistosa.

**Si no tienes imagen**: sin problema, la tarjeta sale en formato solo texto, también editorial.

### Lo que yo hago

1. Si me has pasado imagen, la guardo en `imagenes/insights/[fecha]-[medio].jpg` con nombre limpio.
2. Edito `insights.html` para añadir la nueva tarjeta en el listado, en orden cronológico (lo más reciente arriba), con o sin imagen según corresponda.
3. Te aviso de qué archivos he tocado.

### Lo que tú haces después

Mismo proceso: arrastras la carpeta `Praxia-web` entera a Netlify.

---

## 4 · Cómo actualizar otras secciones de la web

Para cambios en cualquier otra sección (cápsulas, casos demo, sobre mí, FAQ, etc.):

1. Me dices: *"En la sección X de la home, cambia Y por Z"* — o lo que sea.
2. Yo lo edito.
3. Tú arrastras la carpeta a Netlify.

---

## 5 · Reglas de oro para no romper nada

1. **No edites tú directamente los HTML** salvo que sepas exactamente lo que haces. Cualquier carácter mal puesto puede romper la maquetación de toda una sección. Si quieres cambiar algo, mejor pídemelo.
2. **No subas archivos sueltos a Netlify**. Sube siempre la carpeta `Praxia-web` entera. Si subes solo un archivo, Netlify cree que tu web es ese archivo y borra todo lo demás.
3. **Antes de cada subida, verifica que no haya basura.** Borra archivos `.bak`, `.DS_Store` o subcarpetas viejas tipo `deploy_netlify/`. El comando rápido en Terminal es:

   ```
   cd ~/Documents/Claude/Projects/Consultoria\ Marta/Praxia-web/ && rm -f *.bak && rm -f .DS_Store && rm -f Praxia_Atelier_Landing.html && rm -rf deploy_netlify && ls
   ```

4. **Antes de un cambio grande, haz copia de seguridad.** Duplica la carpeta entera y le pones nombre `Praxia-web-backup-AAAA-MM-DD`. Si algo sale mal, vuelves a esa copia.
5. **Cuando montemos GitHub** (siguiente paso recomendado), todo esto se vuelve automático y mucho más seguro.

---

## 6 · Estado actual del sitio

### Idiomas
- **Español:** todas las páginas funcionan en ES.
- **Inglés:** el switcher EN funciona en home, diario y insights con un diccionario de strings clave. Las páginas de casos demo, mesa de trabajo, aviso legal y privacidad **aún no tienen versión EN paralela**. Cuando alguien estando en EN haga clic en una de esas, el switcher i18n traduce los strings comunes pero las cabeceras y partes específicas de cada caso siguen en español. Es funcional para una primera fase, pero conviene cerrar las versiones `_EN` cuando haya tiempo.

### Conexiones técnicas pendientes
- **Formulario de contacto / inscripción de colaboradores / suscripción al Diario:** ahora mismo todos muestran un alert de "próximamente". Hay que conectarlos a Formspree, Resend, Mailchimp o similar.
- **Chatbox del estudio:** funciona, captura conversación. Para que los leads se guarden automáticamente hay que rellenar `formspreeUrl` en `praxia-chatbox.js`.
- **Cal.com:** ya está enlazado al calendario de Marta en todas las páginas (`https://cal.com/marta-escobar-rojas-teatxg/30min`).

### Próximos pasos sugeridos
1. Conectar formulario de contacto y chatbox a un sistema real (Formspree es lo más rápido, 5 min).
2. Apuntar el dominio `praxia-atelier.net` desde DonDominio hacia Netlify (5 min en DNS).
3. Cerrar versiones EN de las páginas de casos demo cuando haya tiempo.
4. Migrar todo a Git + GitHub para automatizar deploys (cuando hayas publicado los primeros 2-3 artículos a mano).

---

## 7 · Convenciones de nombres

Para que las URLs sean limpias y SEO-friendly:

- **Slugs en minúsculas, sin tildes, separados por guiones.**
  - Bien: `aie-vehiculo-coinversion-family-business`
  - Mal: `AIE_Vehículo de Coinversión.html`

- **Categorías estables.** Las que ya están en uso:
  - `Modelo económico`
  - `Jurídico-fiscal`
  - `IA aplicada`
  - `Capital y captación`
  - `Producto digital`
  - `Operaciones`
  - `Marketing y posicionamiento`
  - `Comercial`
  - `Estrategia`

- **Tipos de Insight:**
  - `Prensa`
  - `Podcast`
  - `Vídeo`
  - `Entrevista`
  - `Panel`
  - `Mención`

---

## 8 · Contacto interno

Si tienes dudas sobre cómo trabajar con esta carpeta, o si algo se rompe:
- Pregunta directamente al asistente de Praxia (este chat).
- O si necesitas ayuda externa, contacta con el desarrollador de turno.

---

**Final del manual.** Última actualización: 2026-05-01.
