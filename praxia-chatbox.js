/* ============================================================
   Praxia Chatbox · script único
   Se carga en todas las páginas. Auto-inyecta el HTML del widget.
   Cualquier cambio aquí se aplica en todo el sitio sin tocar HTMLs.
   ============================================================ */
(function () {
  // Si ya está inyectado en esta página, salir
  if (window.__PRAXIA_CHAT_LOADED__) return;
  window.__PRAXIA_CHAT_LOADED__ = true;

  // ============================================================
  // CONFIGURACIÓN — cambia estos valores cuando los tengas
  // ============================================================
  const CONFIG = {
    calendarUrl: "https://cal.com/marta-escobar-rojas-teatxg/30min",
    avatarUrl: "Avatar_Proximamente.html",
    // Web3Forms · entrega a info@praxia-atelier.net
    web3formsKey: "8effa420-bfc6-4dd2-a6d7-da63237755af",
    web3formsEndpoint: "https://api.web3forms.com/submit",
    // Tras este número de ms sin actividad, enviamos un snapshot de la
    // conversación al email (lead "en curso"). Permite recibir chats
    // incompletos cuando el visitante abandona sin terminar el flujo.
    inactivitySnapshotMs: 60000, // 1 minuto sin actividad
    // Mínimo de turnos para que valga la pena enviar un snapshot
    minTurnsToSend: 2,
    autoOpenDelay: -1   // ms al cargar. 0 = inmediato. -1 = no auto-abrir (recomendado).
  };

  // ============================================================
  // INYECCIÓN DEL HTML EN LA PÁGINA
  // ============================================================
  function injectMarkup() {
    if (document.getElementById("pchat-fab")) return; // ya estaba

    const fab = document.createElement("button");
    fab.className = "pchat-fab";
    fab.id = "pchat-fab";
    fab.setAttribute("aria-label", "Habla con Praxia");
    fab.innerHTML =
      '<span class="pchat-fab-dot" aria-hidden="true"></span>' +
      '<svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">' +
      '<path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>' +
      '</svg>' +
      '<span class="pchat-fab-label">Habla con Praxia</span>';
    document.body.appendChild(fab);

    const panel = document.createElement("div");
    panel.className = "pchat-panel";
    panel.id = "pchat-panel";
    panel.innerHTML =
      '<div class="pchat-header">' +
      '  <div class="pchat-logo">P</div>' +
      '  <div>' +
      '    <div class="pchat-header-title">Praxia Atelier</div>' +
      '    <div class="pchat-header-sub"><span class="pchat-status-dot"></span>Asistente · en línea</div>' +
      '  </div>' +
      '  <button class="pchat-close" id="pchat-close" aria-label="Minimizar" title="Minimizar">' +
      '    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" aria-hidden="true"><path d="M5 12h14"/></svg>' +
      '  </button>' +
      '</div>' +
      '<div class="pchat-msgs" id="pchat-msgs"></div>' +
      '<div class="pchat-foot">Confidencial · Marta solo lee tus respuestas si decides seguir.</div>';
    document.body.appendChild(panel);
  }

  injectMarkup();

  const fab = document.getElementById("pchat-fab");
  const panel = document.getElementById("pchat-panel");
  const close = document.getElementById("pchat-close");
  const msgs = document.getElementById("pchat-msgs");

  const state = {
    isOpen: false,
    step: "start",
    lead: {
      nombre: "",
      email: "",
      actividad_actual: "",
      fase_proyecto: "",
      dolor_principal: "",
      sector: "",
      sector_libre: "",
      tipo_cliente: "",
      vision_12_meses: "",
      presupuesto_rango: "",
      capsula_encajada: "",
      siguiente_accion: "",
      score: 0,
      transcript: []
    }
  };

  // ============================================================
  // SECTORES EXCLUIDOS
  // ============================================================
  const EXCLUDED_KEYWORDS = [
    "cripto", "crypto", "bitcoin", "blockchain especulativ", "nft", "defi",
    "casino", "apuestas", "juego online", "betting",
    "mlm", "multinivel", "venta multinivel", "piramide", "pirámide",
    "pseudo", "homeopati", "milagro"
  ];

  function _afterSectorLibreText() {
    const txt = (state.lead.sector_libre || "").toLowerCase();
    const isExcluded = EXCLUDED_KEYWORDS.some(function (k) { return txt.indexOf(k) !== -1; });
    if (isExcluded) return "Gracias por la honestidad.";
    return "Perfecto, sigamos.";
  }

  function _afterSectorLibreButtons() {
    const txt = (state.lead.sector_libre || "").toLowerCase();
    const isExcluded = EXCLUDED_KEYWORDS.some(function (k) { return txt.indexOf(k) !== -1; });
    if (isExcluded) {
      return [{ label: "Continuar", next: "excluded", value: { alertas: "SECTOR EXCLUIDO · " + state.lead.sector_libre } }];
    }
    return [{ label: "Continuar", next: "ask_tipo" }];
  }

  // ============================================================
  // ÁRBOL DE CONVERSACIÓN
  // ============================================================
  const FLOW = {
    start: {
      bot: "Hola 👋 Soy el asistente de Praxia Atelier. En unos minutos te ayudo a saber si nuestro estudio encaja con tu proyecto. Todo lo que me cuentes queda bajo confidencialidad — Marta solo verá tus respuestas si decides seguir adelante.\n\n¿Empezamos, o prefieres ir directo al calendario?",
      buttons: [
        { label: "Empezamos", primary: true, next: "ask_name" },
        { label: "Ir al calendario", href: CONFIG.calendarUrl, target: "_blank", action: "calendar_direct" }
      ]
    },
    ask_name: {
      bot: "Antes de meternos en materia: ¿cómo te llamas, y a qué te dedicas hoy?",
      input: { placeholder: "Ej. Carlos, abogado mercantil", field: "nombre_actividad", next: "ask_email" }
    },
    ask_email: {
      bot: function () { return "Encantado, " + (state.lead.nombre || "") + ". Para mandarte luego un resumen de lo que hablemos, ¿qué email me das?"; },
      input: { placeholder: "tu@email.com", field: "email", validate: "email", next: "ask_fase" }
    },
    ask_fase: {
      bot: "Perfecto. Cuéntame: ¿qué tienes ya, y qué te gustaría tener?",
      buttons: [
        { label: "Una idea que aún no he aterrizado", next: "ask_dolor", value: { fase_proyecto: "idea_bruta" } },
        { label: "Empresa funcionando, quiero abrir línea nueva", next: "ask_dolor", value: { fase_proyecto: "empresa_operando_nueva_linea", scoreAdd: 30 } },
        { label: "Proyecto grande con socios o inversores", next: "ask_dolor", value: { fase_proyecto: "proyecto_grande_estructurado", scoreAdd: 30 } },
        { label: "Algo intermedio", next: "ask_dolor", value: { fase_proyecto: "idea_bruta" } }
      ]
    },
    ask_dolor: {
      bot: "De todo lo que tienes en la cabeza, ¿qué es lo que más te está costando aterrizar?",
      buttons: [
        { label: "Lo legal y fiscal", next: "ask_sector", value: { dolor_principal: "juridico_fiscal", capsula_encajada: "C01", scoreAdd: 15 } },
        { label: "El producto o la web", next: "ask_sector", value: { dolor_principal: "producto_digital", capsula_encajada: "C01", scoreAdd: 15 } },
        { label: "El modelo económico", next: "ask_sector", value: { dolor_principal: "modelo_economico", capsula_encajada: "C00", scoreAdd: 15 } },
        { label: "Captar inversores", next: "ask_sector", value: { dolor_principal: "captacion_capital", capsula_encajada: "C01", scoreAdd: 15 } },
        { label: "Marketing y captación", next: "ask_sector", value: { dolor_principal: "marketing", capsula_encajada: "C04", scoreAdd: 15 } },
        { label: "Operaciones y procesos", next: "ask_sector", value: { dolor_principal: "operaciones", capsula_encajada: "C05", scoreAdd: 15 } },
        { label: "Cómo vender lo que tengo", next: "ask_sector", value: { dolor_principal: "comercial", capsula_encajada: "C06", scoreAdd: 15 } },
        { label: "Quiero un avatar de IA", next: "ask_sector", value: { dolor_principal: "ia_avatar", capsula_encajada: "C01", scoreAdd: 15 } },
        { label: "Varios a la vez (marketing + ops + ventas)", next: "ask_sector", value: { dolor_principal: "transversal", capsula_encajada: "Pack_GTM", scoreAdd: 20 } }
      ]
    },
    ask_sector: {
      bot: "Una más, para entender el contexto: ¿en qué sector estás?",
      buttons: [
        { label: "Real estate / inmobiliario", next: "ask_tipo", value: { sector: "real_estate", scoreAdd: 20 } },
        { label: "Health-tech / wellness", next: "ask_tipo", value: { sector: "health_tech", scoreAdd: 20 } },
        { label: "Family business (vino, alimentación, artesanía)", next: "ask_tipo", value: { sector: "family_business", scoreAdd: 20 } },
        { label: "EdTech / formación / comunidad", next: "ask_tipo", value: { sector: "edtech", scoreAdd: 20 } },
        { label: "Finance / wealth / family office", next: "ask_tipo", value: { sector: "finance", scoreAdd: 20 } },
        { label: "Industrial / manufactura", next: "ask_tipo", value: { sector: "industrial" } },
        { label: "Servicios profesionales", next: "ask_tipo", value: { sector: "servicios" } },
        { label: "Otro", next: "ask_sector_otro", value: { sector: "otro" } }
      ]
    },
    ask_sector_otro: {
      bot: "Cuéntame en una palabra o dos qué tipo de proyecto es. Así me aseguro de que Praxia es el estudio adecuado para ti.",
      input: { placeholder: "Ej. SaaS B2B, hostelería, agritech…", field: "sector_libre", next: "check_excluded" }
    },
    check_excluded: {
      bot: function () { return _afterSectorLibreText(); },
      buttons: function () { return _afterSectorLibreButtons(); }
    },
    excluded: {
      bot: "Por el tipo de regulación que envuelve a este sector, Praxia no es el estudio adecuado para ti. Te recomendaría buscar consultoras especializadas en ese ámbito.\n\nSi te has equivocado o quieres comentarlo de todas formas, puedes escribir a Marta directamente a marta@praxia-atelier.net.",
      buttons: [
        { label: "Gracias, lo miro por mi cuenta", action: "save_lead", value: { siguiente_accion: "descartado_sector_excluido" } }
      ]
    },
    ask_tipo: {
      bot: "Para entender mejor: ¿cómo estás constituido?",
      buttons: [
        { label: "Soy autónomo / freelance", next: "ask_vision", value: { tipo_cliente: "autonomo" } },
        { label: "SL pequeña (hasta 10 personas)", next: "ask_vision", value: { tipo_cliente: "pyme_pequena", scoreAdd: 5 } },
        { label: "SL mediana (10–50)", next: "ask_vision", value: { tipo_cliente: "pyme_mediana", scoreAdd: 10 } },
        { label: "Family office o empresa familiar", next: "ask_vision", value: { tipo_cliente: "family_office", scoreAdd: 20 } },
        { label: "Corporativo / fondo", next: "ask_vision", value: { tipo_cliente: "corporativo", scoreAdd: 20 } }
      ]
    },
    ask_vision: {
      bot: "Última pregunta importante: si dentro de 12 meses miras hacia atrás y todo ha ido bien, ¿qué habría pasado en tu negocio para que estés contento?",
      input: { placeholder: "Cuéntamelo en una o dos frases", field: "vision_12_meses", next: "ask_presupuesto", multiline: true }
    },
    ask_presupuesto: {
      bot: "Perfecto. Y para que Marta prepare la conversación con contexto: ¿qué presupuesto orientativo tienes para esta fase? No tiene que ser exacto.",
      buttons: [
        { label: "1.000 – 3.000 €", next: "closing", value: { presupuesto_rango: "1k-3k" } },
        { label: "5.000 – 15.000 €", next: "closing", value: { presupuesto_rango: "5k-15k", scoreAdd: 25 } },
        { label: "15.000 – 50.000 €", next: "closing", value: { presupuesto_rango: "15k-50k", scoreAdd: 25 } },
        { label: "+50.000 €", next: "closing", value: { presupuesto_rango: "+50k", scoreAdd: 25 } },
        { label: "Aún no lo tengo claro", next: "closing", value: { presupuesto_rango: "no_definido" } }
      ]
    },
    closing: {
      bot: function () {
        const dolor = state.lead.dolor_principal || "";
        const dolorMap = {
          "juridico_fiscal": "estructurar lo legal y fiscal con coherencia",
          "producto_digital": "darle forma al producto digital",
          "modelo_economico": "aterrizar el modelo económico",
          "captacion_capital": "preparar la captación de inversión",
          "marketing": "rediseñar el marketing y la captación",
          "operaciones": "ordenar y automatizar la operativa",
          "comercial": "construir un método de venta sólido",
          "ia_avatar": "diseñar la capa de IA aplicada",
          "transversal": "trabajar marketing, operaciones y ventas como un sistema"
        };
        const fraseDolor = dolorMap[dolor] || "ordenar lo que tienes en la cabeza";
        return "Te entiendo. Lo que veo es que necesitas " + fraseDolor + ".\n\n**Praxia se adapta a tu presupuesto.** Podemos hacerte una propuesta ajustada a lo que tengas en mente, manteniendo siempre los entregables que aporten valor real a tu caso.\n\nLa mejor forma de seguir es reservar **30 min con Marta**. Sin coste, sin compromiso. Y en las 48 horas siguientes recibes un **one-pager gratis con tres movimientos accionables** específicos para tu proyecto — el valor es tuyo aunque no sigamos juntos.\n\n¿Cómo prefieres seguir?";
      },
      buttons: [
        { label: "📅 Reservar 30 min con Marta · recibo el one-pager gratis", primary: true, href: CONFIG.calendarUrl, target: "_blank", action: "save_lead", value: { siguiente_accion: "agendar_reunion", scoreAdd: 30 } },
        { label: "💬 Tengo más dudas, sigo aquí", next: "free_chat", value: { siguiente_accion: "seguir_chat" }, action: "save_lead" },
        { label: "🎙️ Hablar con el avatar (próximamente)", href: CONFIG.avatarUrl, action: "save_lead", value: { siguiente_accion: "hablar_avatar", scoreAdd: 15 } }
      ]
    },
    free_chat: {
      bot: "Sin problema. Pregúntame lo que necesites: precios, plazos, casos parecidos, cómo trabajamos. Cuando lo tengas claro, lo más útil es reservar 30 min con Marta — y te llevas el one-pager gratis con tres movimientos para tu caso.\n\n¿Por dónde empiezo?",
      buttons: [
        { label: "¿Qué incluye exactamente cada cápsula?", next: "info_capsulas" },
        { label: "¿Cómo es el método de las 8 capas?", next: "info_metodo" },
        { label: "¿Puedo ver casos parecidos al mío?", next: "info_casos" },
        { label: "¿Qué pasa después de la primera reunión?", next: "info_proceso" },
        { label: "📅 Mejor reservo · recibo el one-pager", primary: true, href: CONFIG.calendarUrl, target: "_blank" }
      ]
    },
    info_capsulas: {
      bot: "Las cápsulas son unidades de servicio con alcance, plazo y precio cerrado:\n\n• **C00 Strategy Sprint** · 1 semana · 990–2.500 € · valida la dirección\n• **C01 Ecosystem Blueprint** · 10–15 días · 12–18k € · diseña el plano completo\n• **C02 Ecosystem Build** · 3–5 meses · 60–120k € · aterrizaje con equipo coordinado\n• **C03 Operate** · recurrente · 5,5–8k €/mes · mantenimiento\n• **C04/05/06** · 2–3 sem · 6,5–9,5k € cada una · marketing, operaciones, comercial\n• **Pack 04+05+06** · 5 sem · 18k € (ahorra 4.500 €)",
      buttons: [
        { label: "¿Cómo se elige la mía?", next: "info_proceso" },
        { label: "Ver el método", next: "info_metodo" },
        { label: "📅 Reservar reunión", href: CONFIG.calendarUrl, target: "_blank" }
      ]
    },
    info_metodo: {
      bot: "El método integra 8 disciplinas que normalmente vienen separadas:\n\n1. Jurídico-fiscal\n2. Producto y software\n3. IA aplicada\n4. Modelo económico\n5. Storytelling de capital\n6. Marketing\n7. Operaciones\n8. Comercial\n\nLas trabajamos como un único equipo, no como ocho proveedores. Por eso el resultado queda coherente: lo que firmas en lo legal cuadra con lo que dice tu landing y con lo que vendes.",
      buttons: [
        { label: "Ver casos demo", next: "info_casos" },
        { label: "📅 Reservar reunión", href: CONFIG.calendarUrl, target: "_blank" }
      ]
    },
    info_casos: {
      bot: "Tenemos tres casos demo navegables:\n\n• **Bodega Valdescuro** — family business · vino · Ribera del Duero\n• **Clínica Lumen** — health-tech · medicina de longevidad · Madrid\n• **Casa Vento** — real estate · pisos reformados · Madrid\n\nLos puedes ver desde la sección Casos de la home.",
      buttons: [
        { label: "Ver Casos", href: "index.html#casos" },
        { label: "📅 Reservar reunión", href: CONFIG.calendarUrl, target: "_blank" }
      ]
    },
    info_proceso: {
      bot: "El proceso típico es así:\n\n1. **Llamada inicial 30 min** (gratis, sin compromiso) — Marta te oye, hace preguntas, te dice si encaja.\n2. **One-pager gratis en 48h** — recibes un PDF con tres movimientos accionables específicos para tu caso, encajemos o no.\n3. **Si encaja**, te manda propuesta ajustada a tu presupuesto con plazo y entregables cerrados en 24h.\n4. **Si firmas**, arrancamos en menos de una semana. Pago 50/50.\n5. **Entregables a plazo cerrado** — si nos retrasamos, lo asumimos nosotros.",
      buttons: [
        { label: "📅 Reservar 30 min · recibo el one-pager", primary: true, href: CONFIG.calendarUrl, target: "_blank" },
        { label: "🎙️ Hablar con avatar (próximamente)", href: CONFIG.avatarUrl }
      ]
    }
  };

  // ============================================================
  // RENDER + LÓGICA
  // ============================================================

  function open() {
    state.isOpen = true;
    panel.classList.add("open");
    fab.classList.add("collapsed");
    if (msgs.children.length === 0) goTo("start");
    try { sessionStorage.setItem("pchatOpened", "1"); } catch (e) {}
  }

  function closeChat() {
    state.isOpen = false;
    panel.classList.remove("open");
    fab.classList.remove("collapsed");
    try { sessionStorage.setItem("pchatDismissed", "1"); } catch (e) {}
  }

  fab.onclick = function () { state.isOpen ? closeChat() : open(); };
  close.onclick = closeChat;

  function botSay(text) {
    const div = document.createElement("div");
    div.className = "pchat-msg bot";
    div.innerHTML = text.replace(/\n/g, "<br>").replace(/\*\*(.+?)\*\*/g, "<strong>$1</strong>");
    msgs.appendChild(div);
    state.lead.transcript.push({ role: "bot", text: text });
    scroll();
    if (typeof scheduleSnapshot === "function") scheduleSnapshot();
  }

  function userSay(text) {
    const div = document.createElement("div");
    div.className = "pchat-msg user";
    div.textContent = text;
    msgs.appendChild(div);
    state.lead.transcript.push({ role: "user", text: text });
    scroll();
    if (typeof scheduleSnapshot === "function") scheduleSnapshot();
  }

  function scroll() { msgs.scrollTop = msgs.scrollHeight; }

  function goTo(step) {
    state.step = step;
    const node = FLOW[step];
    if (!node) return;
    const text = typeof node.bot === "function" ? node.bot() : node.bot;
    setTimeout(function () {
      botSay(text);
      if (node.input) renderInput(node.input);
      if (node.buttons) {
        const btns = typeof node.buttons === "function" ? node.buttons() : node.buttons;
        renderButtons(btns);
      }
    }, 400);
  }

  function renderButtons(buttons) {
    const wrap = document.createElement("div");
    wrap.className = "pchat-actions";
    buttons.forEach(function (b) {
      let el;
      if (b.href) {
        el = document.createElement("a");
        el.href = b.href;
        if (b.target) el.target = b.target;
        if (b.target === "_blank") el.rel = "noopener";
      } else {
        el = document.createElement("button");
      }
      el.className = "pchat-btn" + (b.primary ? " primary" : " outline");
      el.textContent = b.label;
      el.onclick = function (e) {
        if (b.value) applyValue(b.value);
        userSay(b.label);
        wrap.remove();
        if (b.action === "save_lead") submitLead();
        if (b.action === "calendar_direct") {
          setTimeout(function () { botSay("Te dejo el calendario abierto. Si después quieres volver y comentar algo, aquí estaré."); }, 400);
        }
        if (b.next) goTo(b.next);
      };
      wrap.appendChild(el);
    });
    msgs.appendChild(wrap);
    scroll();
  }

  function renderInput(input) {
    const wrap = document.createElement("div");
    wrap.className = "pchat-input-area";
    wrap.style.position = "static";
    wrap.style.borderTop = "0";
    wrap.style.padding = "0";
    wrap.style.background = "transparent";
    wrap.style.alignSelf = "stretch";

    const tag = input.multiline ? "textarea" : "input";
    const inp = document.createElement(tag);
    inp.className = "pchat-input";
    inp.placeholder = input.placeholder || "";
    if (!input.multiline) inp.type = "text";
    if (input.multiline) inp.rows = 2;

    const btn = document.createElement("button");
    btn.className = "pchat-send";
    btn.textContent = "Enviar";

    function submit() {
      const v = inp.value.trim();
      if (!v) return;
      if (input.validate === "email" && !/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(v)) {
        inp.style.borderColor = "#b04a30";
        return;
      }
      if (input.field === "nombre_actividad") {
        const parts = v.split(/[,·\-]/);
        state.lead.nombre = (parts[0] || v).trim();
        state.lead.actividad_actual = parts.slice(1).join(", ").trim() || v;
      } else {
        state.lead[input.field] = v;
      }
      userSay(v);
      wrap.remove();
      if (input.next) goTo(input.next);
    }

    btn.onclick = submit;
    inp.onkeydown = function (e) { if (e.key === "Enter" && !e.shiftKey) { e.preventDefault(); submit(); } };

    wrap.appendChild(inp);
    wrap.appendChild(btn);
    msgs.appendChild(wrap);
    scroll();
    setTimeout(function () { inp.focus(); }, 100);
  }

  function applyValue(value) {
    Object.keys(value).forEach(function (k) {
      if (k === "scoreAdd") state.lead.score += value[k];
      else state.lead[k] = value[k];
    });
  }

  // Conversation snapshot dispatcher — sends every meaningful state of the
  // conversation to Web3Forms so Marta receives even abandoned chats.
  // Strategies:
  //   1) After "minTurnsToSend" turns, schedule a debounced snapshot.
  //   2) On final submit (lead complete), send marked as "completo".
  //   3) Before page unload, fire a final beacon if the conversation has
  //      moved since the last send.
  let _lastSentHash = "";
  let _snapshotTimer = null;
  let _lastSentAt = 0;

  function _hashState() {
    // Cheap signature so we don't resend the same content.
    return [
      state.lead.score,
      state.lead.transcript.length,
      state.lead.email,
      state.lead.dolor_principal,
      state.lead.capsula_encajada,
      state.step
    ].join("|");
  }

  function _categoria() {
    if (state.lead.score >= 80) return "caliente";
    if (state.lead.score >= 40) return "tibio";
    return "frio";
  }

  function _transcriptText() {
    return state.lead.transcript.map(function (t) {
      return (t.role === "bot" ? "[Praxia] " : "[Visitante] ") + t.text;
    }).join("\n\n");
  }

  function _buildPayload(reason) {
    state.lead.categoria = _categoria();
    const transcript = _transcriptText();
    const nombre = state.lead.nombre || "(sin nombre)";
    const email = state.lead.email || "(sin email)";
    const subject =
      "Praxia · Chat " + state.lead.categoria + " · " + nombre +
      " · score " + state.lead.score + (reason === "abandono" ? " · ABANDONO" : reason === "completo" ? " · completo" : " · en curso");

    return {
      access_key: CONFIG.web3formsKey,
      subject: subject,
      from_name: "Web Praxia · Chatbot",
      // Anti-spam honeypot (Web3Forms ignora envíos donde botcheck = true)
      botcheck: "",
      // Campos legibles en el email
      tipo_envio: reason || "snapshot",
      score: state.lead.score,
      categoria: state.lead.categoria,
      capsula_encajada: state.lead.capsula_encajada,
      nombre: state.lead.nombre,
      email: state.lead.email,
      actividad: state.lead.actividad_actual,
      fase_proyecto: state.lead.fase_proyecto,
      dolor_principal: state.lead.dolor_principal,
      sector: state.lead.sector,
      sector_libre: state.lead.sector_libre,
      tipo_cliente: state.lead.tipo_cliente,
      vision_12_meses: state.lead.vision_12_meses,
      presupuesto: state.lead.presupuesto_rango,
      siguiente_accion: state.lead.siguiente_accion,
      paso_actual: state.step,
      n_turnos: state.lead.transcript.length,
      url_origen: location.href,
      transcript: transcript
    };
  }

  function _sendPayload(payload, useBeacon) {
    if (!CONFIG.web3formsKey || CONFIG.web3formsKey.indexOf("REEMPLAZA") !== -1) {
      console.log("[Praxia Chat] Snapshot capturado (sin enviar — falta key):", payload);
      return;
    }
    try {
      if (useBeacon && navigator.sendBeacon) {
        // sendBeacon es la forma fiable de enviar antes de que la pestaña
        // se cierre. Web3Forms acepta JSON con Content-Type adecuado.
        const blob = new Blob([JSON.stringify(payload)], { type: "application/json" });
        navigator.sendBeacon(CONFIG.web3formsEndpoint, blob);
      } else {
        fetch(CONFIG.web3formsEndpoint, {
          method: "POST",
          headers: { "Content-Type": "application/json", "Accept": "application/json" },
          body: JSON.stringify(payload),
          keepalive: true
        }).catch(function (err) { console.warn("[Praxia Chat] Web3Forms fallo:", err); });
      }
    } catch (e) {
      console.warn("[Praxia Chat] Error enviando:", e);
    }
  }

  function sendSnapshot(reason) {
    // No enviar si el visitante apenas ha interactuado.
    if (state.lead.transcript.length < CONFIG.minTurnsToSend) return;
    const sig = _hashState();
    // Evitar duplicados consecutivos idénticos (excepto si es cierre o final).
    if (sig === _lastSentHash && reason !== "abandono" && reason !== "completo") return;
    _lastSentHash = sig;
    _lastSentAt = Date.now();
    const payload = _buildPayload(reason || "snapshot");
    _sendPayload(payload, reason === "abandono");
  }

  function scheduleSnapshot() {
    if (_snapshotTimer) clearTimeout(_snapshotTimer);
    _snapshotTimer = setTimeout(function () {
      sendSnapshot("snapshot");
    }, CONFIG.inactivitySnapshotMs);
  }

  // Final submit (cuando el flujo completa): manda con marca "completo"
  function submitLead() {
    sendSnapshot("completo");
  }

  // Antes de cerrar pestaña, intentar enviar lo último.
  window.addEventListener("beforeunload", function () {
    if (state.lead.transcript.length >= CONFIG.minTurnsToSend) {
      sendSnapshot("abandono");
    }
  });

  // También al esconder la página (móvil cambia app, pestaña pasa a fondo)
  document.addEventListener("visibilitychange", function () {
    if (document.visibilityState === "hidden" &&
        state.lead.transcript.length >= CONFIG.minTurnsToSend) {
      sendSnapshot("abandono");
    }
  });

  // Auto-apertura al cargar (en TODAS las páginas) — se desactiva si la página
  // pide modo inline vía window.PraxiaChat.embed()
  if (CONFIG.autoOpenDelay >= 0) {
    let dismissed = false;
    try { dismissed = sessionStorage.getItem("pchatDismissed") === "1"; } catch (e) {}
    if (!dismissed) {
      setTimeout(function () {
        if (state._inlineMode) return;
        if (!state.isOpen) open();
      }, CONFIG.autoOpenDelay);
    }
  }

  // ============================================================
  // API PÚBLICA · permite embebido inline en cualquier sección
  // ============================================================
  window.PraxiaChat = {
    open: open,
    close: closeChat,
    isOpen: function () { return state.isOpen; },
    /**
     * Embebe el chat en un contenedor de la página (inline mode).
     * El panel flotante deja de aparecer solo cuando se llama a esto.
     */
    /** Reservado: embebido inline. Desactivado por decisión de producto. */
    embed: function () { return false; }
  };
})();
