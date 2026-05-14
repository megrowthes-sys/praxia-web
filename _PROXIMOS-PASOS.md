# Próximos pasos · Praxia Atelier

**Última actualización:** 2026-05-01

Este documento lista lo que queda por hacer en la web, en orden de prioridad.
Cuando completes algo, márcalo con `[x]` en lugar de `[ ]`.

---

## ✅ Hecho

- [x] Home con todas las secciones (método, para quién, cápsulas, casos, fundadora, contenidos, contacto).
- [x] Sprint + Launch como cuarto nivel del Strategy Sprint (4.500 €).
- [x] Add-on premium · IA conversacional / avatar (presupuesto personalizado).
- [x] Sección "Trayectoria detrás del estudio" con tres proyectos reales anonimizados.
- [x] Sección Asistente con CTA al chat lateral.
- [x] Disclaimer legal sobre alcance de servicios (home + aviso legal).
- [x] Página Diario (índice editorial preparada para artículos).
- [x] Página Insights (índice de apariciones externas).
- [x] Página Colaboradores (bolsa de freelancers con 14 perfiles + formulario).
- [x] Casos demo · Bodega Valdescuro · Clínica Lumen · Casa Vento · Mesa de Trabajo.
- [x] Switcher ES/EN funcional con diccionario de strings principales.
- [x] Chatbox lateral (FAB + panel) en todas las páginas.
- [x] Plantillas para añadir nuevos artículos e Insights sin tocar HTML.
- [x] Estructura de carpetas limpia (`diario/`, `_entradas-pendientes/`).

---

## 🟡 Pendiente urgente · antes del primer subida pública

- [ ] **Limpiar archivos basura** antes de subir a Netlify. Comando:
  ```
  cd ~/Documents/Claude/Projects/Consultoria\ Marta/Praxia-web/ && rm -f *.bak && rm -f .DS_Store && rm -f Praxia_Atelier_Landing.html && rm -rf deploy_netlify && ls
  ```

- [ ] **Conectar el formulario de contacto** a un servicio real (Formspree, 5 min · gratis hasta 50 envíos/mes).
  - Crear cuenta en formspree.io
  - En la home, sustituir el alert del formulario por: `<form action="https://formspree.io/f/TU_ID_REAL" method="POST">`

- [ ] **Conectar el chatbox a Formspree** para que los leads del chat lleguen al email.
  - En `praxia-chatbox.js` (línea ~17), reemplazar `formspreeUrl: "https://formspree.io/f/REEMPLAZA_CON_TU_ID"` por la URL real.

- [ ] **Conectar el formulario de Newsletter** del Diario.
  - En `diario.html`, sustituir el alert del formulario por la integración real (Resend, Mailchimp, ConvertKit o Beehiiv).

- [ ] **Conectar el formulario de Colaboradores** a Notion como base de datos (ideal) o a Formspree (rápido).

---

## 🟠 Pendiente media · primera semana en producción

- [ ] **Apuntar dominio `praxia-atelier.net`** desde DonDominio hacia Netlify.
  - Pasos: DonDominio → DNS → cambiar nameservers o crear A record + CNAME apuntando a Netlify.
  - Tiempo: 5-10 min en config + hasta 24h de propagación DNS.

- [ ] **Activar HTTPS** en Netlify (automático cuando el dominio esté apuntando · Let's Encrypt gratis).

- [ ] **Configurar email profesional `info@praxia-atelier.net`** vía Google Workspace.
  - Plan Business Starter: ~6€/usuario/mes.
  - Configurar registros MX en DonDominio.

- [ ] **Subir foto profesional** de Marta a la sección Fundadora.
  - Reemplazar la imagen base64 actual por `marta-escobar.jpg` (ya está en la carpeta).

- [ ] **Verificar Google Search Console** y **Google Analytics 4** para empezar a tracking SEO desde el día 1.

- [ ] **Crear sitemap.xml** y enviarlo a Google Search Console.

---

## 🔵 Pendiente baja · cuando haya contenido publicado

- [ ] **Traducir al inglés las páginas individuales** que aún no tienen versión EN paralela:
  - [ ] `Praxia_Atelier_Caso_Bodega_Valdescuro_EN.html`
  - [ ] `Praxia_Atelier_Caso_Clinica_Lumen_EN.html`
  - [ ] `Praxia_Atelier_Caso_Casa_Vento_EN.html`
  - [ ] `Praxia_Atelier_Caso_Mesa_de_Trabajo_EN.html`
  - [ ] `aviso-legal_EN.html`
  - [ ] `privacidad_EN.html`
  - [ ] `colaboradores_EN.html`

- [ ] **Añadir `_redirects`** de Netlify para limpiar URLs antiguas si las hay.

- [ ] **Crear página `/admin`** con Decap CMS para que puedas publicar artículos sin tocar HTML.
  - Requiere migrar a Git + GitHub primero.

- [ ] **Migrar a Git + GitHub**.
  - Mover la carpeta a un repositorio privado.
  - Conectar Netlify al repo (deploy automático).
  - Tiempo: 1-2 horas concentradas con ayuda.

- [ ] **Activar Cloudflare Email Routing** o **Zoho Mail** como alternativa gratuita a Workspace si decides no pagar Google.

---

## 🟢 Ideas y mejoras futuras (no urgente)

- [ ] Implementar el avatar IA conversacional (Cápsula premium add-on).
- [ ] Crear página específica para cada cápsula (`/capsula-00.html`, `/capsula-01.html`, etc.) con SEO específico.
- [ ] Galería de testimonios cuando haya 2-3 clientes reales.
- [ ] Página `/credits.html` agradeciendo a cada freelance que haya colaborado en cada proyecto (cuando haya proyectos cerrados).
- [ ] Integrar con un CRM (HubSpot, Pipedrive o Notion) para el flujo comercial.
- [ ] Newsletter automatizada con Resend + Notion API.
- [ ] Dashboard interno (Mesa de Trabajo) sincronizado con Notion para ver pipeline real.

---

## Notas

- **Cada vez que añadas algo nuevo (artículo, Insight, etc.), te marco aquí qué se hizo y cuándo.**
- **Si algo se rompe en producción**, lo primero que comprobamos es el último cambio de esta lista.
- **Backups**: antes de cada subida grande, duplica la carpeta entera y nómbrala `Praxia-web-backup-AAAA-MM-DD`.

---

**Última actualización:** 2026-05-01
