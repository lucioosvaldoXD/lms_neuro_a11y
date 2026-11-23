"""Contenido completo de los Cursos 1 y 2 para la Ruta Ejecutiva B2B."""

COURSES_1_AND_2 = [
	{
		"title": "Curso 1: Traducción Técnico -> Negocio (El Arte del 'So What?')",
		"short_introduction": "Aprende a transformar hallazgos de ciberseguridad y arquitectura técnica en impacto operativo, financiero y legal que un CEO o CFO aprueba.",
		"description": "<p>Domina la traducción de riesgos técnicos a decisiones de negocio mediante la Regla de las 3 Capas, el diccionario ejecutivo y la estructura BLUF.</p>",
		"chapters": [
			{
				"title": "Módulo 1.1: Psicología del Tomador de Decisiones (CFO / CEO / Director de Operaciones)",
				"lessons": [
					{
						"title": "Lección 1: Por qué a los directivos no les importa tu stack tecnológico",
						"tldr_summary": "- Los directivos compran continuidad operativa y protección de margen, no licencias ni siglas.\n- Cada minuto hablando de herramientas sin riesgo de negocio reduce tu autoridad en la mesa.\n- Traduce toda capacidad técnica a tiempo de paro evitado, multas prevenidas o ventas protegidas.",
						"body": """### Concepto Clave (Ciberseguridad B2B)
Un **CEO, CFO o Director de Operaciones** evalúa el mundo en tres variables: **flujo de efectivo, continuidad operativa y riesgo legal/reputacional**. Cuando presentas un firewall, un EDR o una arquitectura Zero Trust como "tecnología superior", el directivo escucha *gasto complejo*. Cuando lo presentas como *seguro de continuidad para la facturación*, escucha *inversión estratégica*.

### Comparativa Real
| Enfoque Técnico (Qué evitar) | Enfoque Asesor Ejecutivo (Qué decir) |
| :--- | :--- |
| "Implementamos un XDR con correlación heurística en endpoints y SIEM centralizado." | "Reducimos de días a minutos el tiempo para detener un ataque antes de que frene la operación de planta y facturación." |

> **Guion listo para usar:** "Director, no venimos a hablarle de software nuevo. Venimos a revisar dónde podría detenerse su operación mañana por la mañana y cuánto costaría cada hora parada."

### Ejercicio Accionable (3 minutos)
Graba una nota de voz de **45 segundos** explicando tu servicio principal de ciberseguridad **sin usar ninguna sigla en inglés**. Escúchala y verifica si un gerente de logística o finanzas entendería exactamente qué riesgo le quitas de encima.""",
					},
					{
						"title": "Lección 2: La Regla de las 3 Capas (Hallazgo -> Interrupción -> Impacto)",
						"tldr_summary": "- Nunca entregues un hallazgo técnico aislado; conéctalo siempre con operación y dinero.\n- Capa 1 (Qué falla) -> Capa 2 (Qué se detiene) -> Capa 3 (Cuánto cuesta en dinero o ley).\n- Esta secuencia convierte reportes ignorados en presupuestos aprobados en una sola reunión.",
						"body": """### Concepto Clave (Ciberseguridad B2B)
Todo argumento técnico ante dirección debe cruzar **tres capas obligatorias**:
1. **Hallazgo Técnico:** Qué vulnerabilidad o brecha existe.
2. **Interrupción Operativa:** Qué proceso crítico deja de funcionar si se explota.
3. **Impacto Financiero / Legal:** Cuánto dinero se pierde por hora, qué contrato se incumple o qué multa aplica.

### Comparativa Real
| Enfoque Técnico | Enfoque Asesor Ejecutivo (3 Capas) |
| :--- | :--- |
| "El servidor ERP tiene puertos RDP expuestos y falta de parches críticos CVE-2024." | "**[Capa 1]** El acceso remoto al sistema administrativo está expuesto sin doble verificación. **[Capa 2]** Si alguien entra, puede cifrar la base de pedidos y detener embarques 48 horas. **[Capa 3]** Eso representa pérdida directa de facturación de dos días más penalizaciones por entrega tardía." |

> **Plantilla rápida:** "Detectamos **[Hallazgo simple]**. Si se materializa, se detiene **[Proceso crítico]**, lo cual expone a la empresa a **[Costo / Multa / Pérdida de clientes]**."

### Ejercicio Accionable (4 minutos)
Toma el último hallazgo técnico que hayas reportado a un cliente o jefe y escríbelo en **3 líneas exactas**, una por cada capa. Si en la Capa 3 no hay dinero, tiempo o riesgo legal, reescríbela.""",
					},
					{
						"title": "Lección 3: Diccionario de Traducción (15 siglas -> Flujo de Efectivo)",
						"tldr_summary": "- Las siglas técnicas generan distancia cognitiva y sensación de riesgo oculto en dirección.\n- Reemplaza términos como WAF, XDR, SIEM, DMARC y Ransomware por consecuencias de negocio.\n- Quien domina el lenguaje del cliente controla la velocidad de la decisión.",
						"body": """### Concepto Clave (Ciberseguridad B2B)
Cuando un directivo no entiende una sigla, rara vez pregunta; simplemente **pospone la decisión**. Traducir las 15 siglas más comunes elimina esa fricción.

### Diccionario de Traducción Rápida
| Sigla Técnica | Traducción Ejecutiva (Flujo de Efectivo y Continuidad) |
| :--- | :--- |
| **Ransomware** | Secuestro de operación que paraliza facturación y cobra rescate para liberar datos. |
| **WAF** | Filtro en la puerta de tu tienda o portal web para evitar caídas y robo de datos de clientes. |
| **XDR / EDR** | Vigilancia activa en cada computadora para frenar un ataque antes de que se propague. |
| **SIEM** | Bitácora centralizada que detecta movimientos anómalos y sirve de evidencia legal. |
| **SOC** | Equipo de guardia 24/7 que responde en minutos cuando ocurre un incidente nocturno. |
| **DMARC / SPF** | Sello de autenticidad para que nadie suplante tu correo y cobre facturas falsas a tus clientes. |
| **MFA / 2FA** | Doble llave de acceso: aunque roben una contraseña, no pueden entrar a cuentas bancarias o ERP. |
| **Zero Trust** | Regla de acceso mínimo: si comprometen un usuario, el daño queda contenido en una sola área. |
| **DLP** | Control de fuga para evitar que listas de precios, clientes o nómina salgan por correo o USB. |
| **Pentesting** | Auditoría controlada para encontrar puertas abiertas antes de que las encuentre un atacante. |
| **Phishing** | Engaño por correo o WhatsApp para robar credenciales o desviar transferencias. |
| **Backup Inmutable** | Copia de seguridad a prueba de borrado para recuperar la empresa en horas tras un siniestro. |
| **VPN** | Túnel cifrado para que el equipo remoto trabaje sin exponer información en redes públicas. |
| **IAM** | Control de permisos para que cada colaborador acceda solo a lo que necesita hoy. |
| **SLA** | Garantía contractual de tiempo máximo de respuesta cuando algo falla. |

> **Regla de oro:** Si necesitas usar una sigla por contexto contractual, di primero el beneficio en español y luego la sigla entre paréntesis.

### Ejercicio Accionable (3 minutos)
Elige **5 siglas** que uses cada semana en tus propuestas y reemplázalas en tu plantilla comercial actual por las frases de la columna derecha.""",
					},
				],
			},
			{
				"title": "Módulo 1.2: Síntesis Ejecutiva y Narrativa",
				"lessons": [
					{
						"title": "Lección 4: Estructura BLUF (Bottom Line Up Front) para correos y propuestas",
						"tldr_summary": "- Pon la conclusión, decisión requerida y costo/beneficio en las primeras 3 líneas.\n- Los directivos leen correos ejecutivos en menos de 20 segundos desde el móvil.\n- El detalle técnico va en anexo o debajo de la línea de decisión.",
						"body": """### Concepto Clave (Ciberseguridad B2B)
**BLUF (Bottom Line Up Front)** significa colocar la **conclusión y acción solicitada al principio**. El enfoque académico tradicional construye suspenso hasta el final; en negocios B2B, si no capturas la decisión en el primer párrafo, el correo queda archivado para "después".

### Comparativa Real
| Correo Técnico Tradicional | Correo con Estructura BLUF |
| :--- | :--- |
| "Estimado, adjunto los logs de la revisión del martes donde analizamos 14 puertos, el estado del certificado SSL y las políticas de retención... (4 párrafos)... por lo que sugerimos aprobar $1,200." | "**Decisión requerida:** Aprobar actualización de acceso remoto ($1,200 único pago) esta semana para evitar paro de facturación.<br>**Por qué importa:** Hoy cualquier contraseña filtrada da acceso directo al servidor administrativo.<br>**Siguiente paso:** Confirmar ventana de 30 min el jueves 7:00 PM." |

> **Fórmula BLUF en 3 bloques:** 1) Qué recomiendo/necesito hoy. 2) Qué riesgo o ganancia está en juego. 3) Próximo paso con fecha.

### Ejercicio Accionable (5 minutos)
Abre tu carpeta de "Enviados", toma un correo largo dirigido a un cliente o director y reescribe únicamente sus **primeras 4 líneas** usando la fórmula BLUF.""",
					},
					{
						"title": "Lección 5: Cómo reescribir un reporte de vulnerabilidades en 1 página",
						"tldr_summary": "- Un reporte de 40 páginas sin resumen de 1 página no se lee ni se aprueba.\n- Estructura la carátula en: Estado actual, Top 3 riesgos de negocio, Inversión y Roadmap 30-60-90.\n- Convierte la evidencia técnica en un anexo consultable solo por el equipo de TI.",
						"body": """### Concepto Clave (Ciberseguridad B2B)
Un reporte de vulnerabilidades de 60 páginas sirve para el ingeniero que debe parchar, **no para quien firma el cheque**. Tu documento ejecutivo de 1 página es el puente entre ambos mundos.

### Comparativa Real
| Reporte Técnico Clásico | Caso de Negocio de 1 Página |
| :--- | :--- |
| Lista de 85 CVEs ordenados por score CVSS sin contexto operativo. | **Semáforo de Riesgo Operativo** (3 hallazgos críticos traducidos a impacto financiero) + **Plan 30/60/90 días** + **Costo de mitigar vs. Costo de incidente**. |

> **Estructura de 1 página:**
> 1. **Diagnóstico en una frase:** Nivel de exposición actual de la operación.
> 2. **Top 3 Riesgos de Negocio:** Hallazgo + Proceso afectado + Impacto estimado.
> 3. **Plan de Acción (30-60-90 días):** Qué se resuelve primero y con qué presupuesto.

### Ejercicio Accionable (5 minutos)
Redacta un resumen de 1 página (máximo 250 palabras) para un cliente ficticio cuya mayor debilidad es no tener respaldos aislados ni doble factor en su correo directivo.""",
					},
				],
				"quiz": {
					"title": "Quiz 1: Escenarios de traducción ejecutivo-financiera",
					"passing_percentage": 70,
					"questions": [
						{
							"question": "Estás frente al CFO de una distribuidora y detectaste que sus respaldos están en la misma red que sus servidores principales (sin copia inmutable). ¿Cuál es la mejor forma de presentarlo?",
							"options": [
								("Explicar la arquitectura de snapshots VSS y el protocolo SMBv3 vulnerable.", 0, "El CFO no evalúa protocolos; hablar de SMBv3 desvía la atención hacia tecnicismos."),
								("Aplicar las 3 capas: si entra un ransomware, cifra operación y respaldos al mismo tiempo, deteniendo embarques y cobranza varios días.", 1, "Correcto: conectas el fallo técnico con la interrupción operativa y el impacto en flujo de efectivo."),
								("Enviar un PDF de 35 páginas con el detalle de permisos NTFS para que lo lea el fin de semana.", 0, "Un documento extenso sin síntesis BLUF raramente se lee ni acelera decisiones."),
							],
						},
						{
							"question": "Debes pedir por correo la aprobación de un presupuesto para activar doble factor (MFA) y DMARC en la empresa. ¿Cómo debe iniciar el correo según BLUF?",
							"options": [
								("Con el historial de incidentes globales de phishing del último trimestre.", 0, "El contexto general al inicio retrasa el propósito del mensaje."),
								("Con la solicitud clara de aprobación, el riesgo concreto de desvío de transferencias/suplantación y la fecha sugerida de ejecución.", 1, "Correcto: BLUF coloca decisión, impacto y siguiente paso en las primeras líneas."),
								("Con la lista completa de RFCs que respaldan el protocolo DMARC.", 0, "Los detalles técnicos normativos pertenecen a un anexo, no a la apertura ejecutiva."),
							],
						},
						{
							"question": "Un Director General te pregunta qué es exactamente un WAF que aparece en tu cotización. ¿Qué respuesta mantiene tu autoridad ejecutiva?",
							"options": [
								("Es un Web Application Firewall de capa 7 que inspecciona paquetes HTTP contra SQLi y XSS.", 0, "Responde con más siglas técnicas que no explican el valor para el negocio."),
								("Es un filtro inteligente en la puerta de su portal web y facturación en línea para bloquear intentos de caída o robo de datos de clientes.", 1, "Correcto: traduce la sigla a protección directa de un activo visible del negocio."),
								("Es un estándar obligatorio que todos los proveedores de nube piden hoy en día.", 0, "Suena genérico y no conecta con el riesgo particular del cliente."),
							],
						},
					],
				},
			},
		],
	},
	{
		"title": "Curso 2: Ingeniería de Conversaciones y Ventas Consultivas B2B",
		"short_introduction": "Domina la prospección sin fricción (SCQA) y la metodología SPIN Selling para que el propio prospecto cuantifique el valor de tu solución.",
		"description": "<p>Aprende a abrir conversaciones B2B de alto nivel y conducir llamadas de descubrimiento consultivo sin sonar a vendedor agresivo ni a soporte técnico.</p>",
		"chapters": [
			{
				"title": "Módulo 2.1: Prospección y Apertura sin Fricción",
				"lessons": [
					{
						"title": "Lección 1: El error de vender en el primer contacto",
						"tldr_summary": "- Enviar catálogos o PDFs en frío activa el rechazo automático del comprador B2B.\n- El objetivo del primer contacto no es cerrar una venta, sino ganar 15 minutos de diagnóstico.\n- Genera curiosidad con un problema específico del sector del prospecto.",
						"body": """### Concepto Clave (Ciberseguridad B2B)
En ventas B2B de ciberseguridad, **vender en el primer mensaje destruye la confianza**. Un directivo recibe decenas de mensajes ofreciendo "soluciones integrales". Tu único objetivo en el primer toque es demostrar que entiendes un problema real de su industria y abrir una conversación breve.

### Comparativa Real
| Primer Contacto Genérico | Primer Contacto Consultivo |
| :--- | :--- |
| "Hola, somos LogiSentinel, líderes en ciberseguridad. Adjunto nuestro brochure con 20 servicios. ¿Cuándo nos reunimos?" | "Hola Carlos, he visto que varias empresas de logística en la región están sufriendo bloqueos por suplantación de correos a proveedores. ¿Cómo validan hoy que una orden de pago no venga alterada?" |

> **Regla de oro:** Cero adjuntos en el primer mensaje. Una sola observación relevante + una pregunta abierta de baja fricción.

### Ejercicio Accionable (3 minutos)
Revisa tu último mensaje de prospección en LinkedIn o correo. Elimina cualquier descripción de tu empresa y cámbiala por **un problema específico del sector del prospecto**.""",
					},
					{
						"title": "Lección 2: El Pitch de 45 segundos con framework SCQA",
						"tldr_summary": "- SCQA (Situación, Complicación, Pregunta, Respuesta) ordena tu mensaje en 45 segundos.\n- Evita recitar listas de características; enfócate en la complicación que cuesta dinero.\n- Termina siempre con una respuesta orientada a resultado medible.",
						"body": """### Concepto Clave (Ciberseguridad B2B)
El framework **SCQA** (*Situation, Complication, Question, Answer*) permite explicar qué haces en **45 segundos** con claridad ejecutiva:
- **S (Situación):** Contexto actual del cliente que ambos reconocen.
- **C (Complicación):** Qué cambió o qué brecha pone en riesgo la operación.
- **Q (Pregunta):** La pregunta que el directivo debería hacerse hoy.
- **A (Respuesta):** Cómo lo resuelves sin fricción operativa.

### Comparativa Real
| Pitch Desordenado | Pitch SCQA (45 segundos) |
| :--- | :--- |
| "Hacemos monitoreo, pentesting, firewalls, capacitación y también soporte cloud..." | "**[S]** Hoy las empresas medianas operan 100% conectadas con clientes y bancos. **[C]** El problema es que un solo correo engañoso o acceso sin control puede detener la operación días enteros. **[Q]** ¿Cuánto tiempo aguantaría su empresa sin facturar si hoy cifran sus sistemas? **[A]** En LogiSentinel blindamos su operación y detectamos amenazas en minutos sin frenar a su equipo." |

> **Guion SCQA listo para adaptar:** "Hoy [Situación del sector]. Sin embargo, [Complicación real]. Eso obliga a preguntarse [Pregunta de impacto]. Nosotros [Respuesta enfocada en resultado]."

### Ejercicio Accionable (4 minutos)
Escribe tu pitch SCQA en máximo **90 palabras** y grábate leyéndolo en voz alta cronometrando no pasar de **45 segundos**.""",
					},
					{
						"title": "Lección 3: Guiones de apertura para llamadas en frío, LinkedIn y presencial",
						"tldr_summary": "- Cada canal exige un ritmo distinto, pero todos comparten respeto por el tiempo del otro.\n- Pedir permiso explícito en los primeros 10 segundos reduce la resistencia en llamadas.\n- En eventos presenciales, pregunta antes de presentar.",
						"body": """### Concepto Clave (Ciberseguridad B2B)
Una apertura profesional desarma la defensiva porque **no finge amistad ni presiona**.

### Guiones Palabra por Palabra
> **Llamada en frío (primeros 15 segundos):**
> "Hola [Nombre], te saluda [Tu Nombre] de LogiSentinel. Sé que te tomo de imprevisto; ¿tienes 30 segundos para contarte por qué te llamo y tú decides si seguimos?"

> **Mensaje breve de LinkedIn:**
> "Hola [Nombre], sigo de cerca el crecimiento de [Empresa]. Trabajamos con directores de operaciones para evitar paros por incidentes digitales sin inflar su área de TI. Si te hace sentido, te comparto en 2 líneas qué estamos viendo en tu sector."

> **Networking presencial:**
> "Interesante lo que manejan en [Sector]. Por curiosidad, con tantos cambios en facturación y operación remota, ¿qué es lo que más les preocupa hoy respecto a continuidad tecnológica?"

### Ejercicio Accionable (4 minutos)
Practica el guion de **llamada en frío** 3 veces seguidas en voz alta cuidando un tono calmado, grave y sin prisa.""",
					},
				],
			},
			{
				"title": "Módulo 2.2: Descubrimiento Consultivo (Framework SPIN Selling)",
				"lessons": [
					{
						"title": "Lección 4: Preguntas de Situación y Problema (Sin interrogatorio)",
						"tldr_summary": "- Investiga datos públicos antes de la llamada para no hacer preguntas de Situación obvias.\n- Limita Situación a 2 preguntas y pasa rápido a preguntas de Problema.\n- Las preguntas de Problema revelan dolores que el cliente ya siente pero no ha priorizado.",
						"body": """### Concepto Clave (Ciberseguridad B2B)
En **SPIN Selling**, las preguntas de **Situación** recopilan contexto ("¿Cuántos empleados tienen?") y las de **Problema** descubren fricciones ("¿Dónde sienten mayor vulnerabilidad hoy?"). El error técnico es abusar de las preguntas de Situación y aburrir al directivo.

### Comparativa Real
| Interrogatorio de Situación | Transición Fluida a Problema |
| :--- | :--- |
| "¿Qué antivirus usan? ¿Qué firewall tienen? ¿Cuántas sucursales son? ¿Usan Office 365?" | "Vi en su sitio que operan con 4 sucursales y equipo híbrido. En ese esquema, ¿qué tan difícil ha sido mantener control sobre quién accede a información crítica cuando alguien trabaja desde fuera?" |

> **Banco de preguntas de Problema:**
> - "¿Qué parte de su operación depende 100% de que el sistema nunca se caiga?"
> - "¿Han tenido algún susto reciente con correos falsos o intentos de fraude?"

### Ejercicio Accionable (3 minutos)
Prepara **3 preguntas de Problema** específicas para un cliente del giro manufactura o logística antes de tu próxima junta.""",
					},
					{
						"title": "Lección 5: Preguntas de Implicación (El costo de no hacer nada)",
						"tldr_summary": "- Las preguntas de Implicación convierten un problema pequeño en una urgencia financiera.\n- Nunca calcules el daño por el cliente; haz preguntas para que él lo dimensione.\n- Conectan el riesgo técnico con pérdida de ventas, horas hombre y reputación.",
						"body": """### Concepto Clave (Ciberseguridad B2B)
Un problema sin urgencia **no genera compra**. Las preguntas de **Implicación** ayudan al directivo a ver las consecuencias en cadena de no resolver ese problema hoy.

### Comparativa Real
| Empujar Urgencia (Se siente agresivo) | Pregunta de Implicación (Consultiva) |
| :--- | :--- |
| "Si no compran esto hoy, los van a hackear y van a quebrar." | "Si ese servidor de facturación quedara inaccesible durante 48 horas a fin de mes, ¿qué impacto tendría en sus entregas y en el flujo de cobranza?" |

> **Banco de preguntas de Implicación:**
> - "Si un colaborador pierde acceso o cae en un engaño, ¿cuántas horas de su equipo directivo se consumen resolviendo la crisis?"
> - "¿Qué pasaría con la renovación de su cliente principal si se filtraran sus listas de precios o contratos?"

### Ejercicio Accionable (4 minutos)
Escribe **2 preguntas de Implicación** para el problema de *"no tener respaldos probados fuera de línea"*.""",
					},
					{
						"title": "Lección 6: Preguntas de Necesidad-Beneficio (El prospecto verbaliza el valor)",
						"tldr_summary": "- Las preguntas de Necesidad-Beneficio hacen que el cliente diga en voz alta por qué necesita la solución.\n- Cambian la conversación de 'cuánto cuesta' a 'cuánto nos ahorra o protege'.\n- Cuando el cliente verbaliza el beneficio, las objeciones caen drásticamente.",
						"body": """### Concepto Clave (Ciberseguridad B2B)
Si tú dices que tu solución es excelente, es publicidad. Si el cliente lo dice en respuesta a una pregunta tuya, es **convicción propia**.

### Comparativa Real
| Monólogo de Características | Pregunta de Necesidad-Beneficio |
| :--- | :--- |
| "Nuestro servicio tiene monitoreo 24/7, reportes mensuales y respuesta rápida." | "¿Qué tranquilidad operativa le daría a dirección saber que cualquier anomalía nocturna se frena en minutos antes de afectar el turno de la mañana?" |

> **Banco de preguntas de Necesidad-Beneficio:**
> - "Si lográramos automatizar esa validación sin frenar a sus vendedores, ¿qué tanto tiempo recuperaría su área de sistemas para proyectos estratégicos?"
> - "¿Cómo ayudaría contar con evidencia auditable de seguridad al momento de negociar contratos con clientes corporativos?"

### Ejercicio Accionable (4 minutos)
En tu siguiente reunión (o en un roleplay de 3 minutos con un compañero), aplica la secuencia completa: **1 Problema -> 1 Implicación -> 1 Necesidad-Beneficio** antes de mostrar una sola diapositiva.""",
					},
				],
				"quiz": {
					"title": "Quiz 2: Simulación de llamada de descubrimiento",
					"passing_percentage": 70,
					"questions": [
						{
							"question": "Un prospecto te responde en LinkedIn: 'Mándame tu brochure en PDF para revisarlo'. ¿Cuál es la mejor respuesta consultiva?",
							"options": [
								("Enviar inmediatamente el PDF de 20 páginas con todas las soluciones y precios.", 0, "Enviar el catálogo completo suele terminar en silencio; el cliente compara solo por precio o lo archiva."),
								("Agradecer el interés y hacer una pregunta breve de diagnóstico para enviarle únicamente lo relevante a su operación actual.", 1, "Correcto: calificas primero con una pregunta corta para mantener la conversación consultiva."),
								("Insistir en agendar una llamada de 1 hora antes de darle cualquier dato.", 0, "Pedir 60 minutos sin contexto genera fricción innecesaria."),
							],
						},
						{
							"question": "Durante la llamada, el Director de Operaciones dice: 'A veces el equipo remoto usa computadoras personales para entrar al sistema'. ¿Qué pregunta de Implicación debes hacer ahora?",
							"options": [
								("'¿Qué sistema operativo tienen esas computadoras?'", 0, "Es una pregunta técnica de Situación; no eleva la conciencia del impacto de negocio."),
								("'Si uno de esos equipos personales se infecta en casa, ¿qué información crítica de clientes o pedidos quedaría expuesta?'", 1, "Correcto: ayudas al directivo a dimensionar la consecuencia operativa de esa práctica."),
								("'Deberían comprar nuestro paquete Enterprise de inmediato.'", 0, "Presionar antes de que el cliente sienta el impacto genera resistencia."),
							],
						},
						{
							"question": "¿Cuál pregunta corresponde a Necesidad-Beneficio (N) dentro de SPIN Selling?",
							"options": [
								("'¿Cuántos empleados tienen actualmente?'", 0, "Es una pregunta básica de Situación."),
								("'¿Qué valor tendría para ustedes demostrar ante sus clientes grandes que operan con controles auditables de seguridad?'", 1, "Correcto: invita al prospecto a verbalizar el beneficio comercial de implementar la solución."),
								("'¿Han sufrido caídas de red el último año?'", 0, "Es una pregunta de Problema, no de Necesidad-Beneficio."),
							],
						},
					],
				},
			},
		],
	},
]
