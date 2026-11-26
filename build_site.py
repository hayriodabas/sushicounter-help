#!/usr/bin/env python3
"""Builds Sushi Night's standalone 12-locale Help & Privacy static site (Hinoki counter palette)."""
from __future__ import annotations

import html
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BASE_URL = "https://hayriodabas.github.io/sushicounter-help"
CONTACT_EMAIL = "hayriodabas@gmail.com"
UPDATED = "2026-11-26"

CSS = """\
:root {
  color-scheme: light dark;
  --counter: #f3eee4;
  --slip: #fcfaf5;
  --well: #eae3d5;
  --rule: #dcd3c4;
  --sumi: #1f1b17;
  --sumi-soft: #655b4f;
  --shu: #b3321c;
  --shu-wash: #f4e1d9;
}
@media (prefers-color-scheme: dark) {
  :root {
    --counter: #13110e;
    --slip: #1d1a16;
    --well: #2a2620;
    --rule: #37312a;
    --sumi: #eee8dc;
    --sumi-soft: #b4aa9a;
    --shu: #e65a3f;
    --shu-wash: #3a1f18;
  }
}
* { box-sizing: border-box; }
body {
  margin: 0;
  background: var(--counter);
  color: var(--sumi);
  font: 16.5px/1.64 -apple-system, BlinkMacSystemFont, "SF Pro Text", "Segoe UI", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
}
.hinoki-top {
  height: 4px;
  background: linear-gradient(90deg, var(--shu) 0 18%, var(--rule) 18% 100%);
}
main {
  max-width: 760px;
  margin: 0 auto;
  padding: 34px 20px 68px;
}
.hero {
  display: flex;
  align-items: center;
  gap: 18px;
  margin-bottom: 18px;
}
.hero img {
  width: 68px;
  height: 68px;
  border-radius: 16px;
  flex-shrink: 0;
  border: 1px solid var(--rule);
}
.eyebrow {
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--shu);
}
h1 {
  font-size: 32px;
  line-height: 1.12;
  font-weight: 700;
  margin: 4px 0 4px;
  letter-spacing: -0.02em;
}
.lede {
  font-size: 17px;
  color: var(--sumi-soft);
  margin: 0 0 22px;
}
nav.primary-nav {
  display: flex;
  flex-wrap: wrap;
  gap: 10px 20px;
  padding: 12px 0;
  border-top: 1px solid var(--rule);
  border-bottom: 1px solid var(--rule);
  margin-bottom: 16px;
  font-size: 14.5px;
  font-weight: 600;
}
.lang-strip {
  display: flex;
  flex-wrap: wrap;
  gap: 7px;
  margin: 0 0 26px;
}
.lang-chip {
  display: inline-block;
  padding: 4px 10px;
  border-radius: 6px;
  border: 1px solid var(--rule);
  background: var(--slip);
  font-size: 13px;
  text-decoration: none;
  color: var(--sumi);
}
.lang-chip.current {
  background: var(--shu);
  border-color: var(--shu);
  color: #fffbf5;
  font-weight: 600;
}
a {
  color: var(--shu);
  text-decoration-thickness: 1.5px;
  text-underline-offset: 3px;
}
h2 {
  font-size: 20px;
  line-height: 1.25;
  margin: 32px 0 12px;
  font-weight: 700;
}
.slip-steps {
  margin: 12px 0 0;
  padding: 0;
  list-style: none;
  counter-reset: step;
}
.slip-steps li {
  counter-increment: step;
  position: relative;
  margin: 0 0 12px;
  background: var(--slip);
  border: 1px solid var(--rule);
  border-radius: 8px;
  padding: 14px 16px 14px 52px;
}
.slip-steps li::before {
  content: counter(step);
  position: absolute;
  left: 16px;
  top: 15px;
  width: 24px;
  height: 24px;
  border-radius: 999px;
  border: 1.5px solid var(--shu);
  color: var(--shu);
  font-size: 13px;
  font-weight: 700;
  display: grid;
  place-items: center;
}
.slip-steps li strong {
  display: block;
  margin-bottom: 4px;
  font-size: 16px;
}
.slip-card {
  background: var(--slip);
  border: 1px solid var(--rule);
  border-radius: 8px;
  padding: 15px 17px;
  margin: 10px 0;
}
.slip-card h3, .slip-card h2 {
  font-size: 16.5px;
  line-height: 1.3;
  margin: 0 0 6px;
  font-weight: 650;
}
.slip-card p {
  margin: 0;
}
table.fact-table {
  width: 100%;
  border-collapse: collapse;
  margin: 14px 0;
  background: var(--slip);
  border: 1px solid var(--rule);
  border-radius: 8px;
  overflow: hidden;
}
.fact-table td {
  text-align: left;
  padding: 11px 14px;
  border-bottom: 1px solid var(--rule);
  font-size: 15px;
  vertical-align: top;
}
.fact-table tr:last-child td { border-bottom: none; }
.locale-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(215px, 1fr));
  gap: 10px;
  list-style: none;
  padding: 0;
}
.locale-grid li {
  background: var(--slip);
  border: 1px solid var(--rule);
  border-radius: 8px;
  padding: 12px 14px;
}
footer {
  margin-top: 44px;
  padding-top: 16px;
  border-top: 1px solid var(--rule);
  color: var(--sumi-soft);
  font-size: 14px;
}
@media (max-width: 560px) {
  h1 { font-size: 27px; }
  main { padding: 26px 16px 52px; }
  .hero img { width: 56px; height: 56px; }
}
"""

LOCALES = {
    "en-US": {
        "name": "English",
        "html_lang": "en",
        "app": "Sushi Night",
        "subtitle": "All You Can Eat & Kaiten",
        "nav_help": "Help",
        "nav_privacy": "Privacy Policy",
        "nav_langs": "All languages",
        "contact_title": "Support & Contact",
        "contact_body": f'Questions, bug reports or feedback for Sushi Night: <a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a>.',
        "updated": f"Updated {UPDATED} · Sushi Night (app.klarwerk.sushicounter) · Hayri Odabaş",
        "help": {
            "title": "Help & Guide",
            "lede": "Count the whole table on one phone: tally marks for every diner, a restaurant time limit and a closing slip with how the night went.",
            "steps_title": "At the table",
            "steps": [
                ("Set up the table", "Pick avatars, enter optional names, choose All you can eat or Kaiten (Pro) and turn on In the middle of the table when friends sit across from you."),
                ("Keep count together", "When In the middle of the table is on, the far side's lanes turn 180° so everyone reads upright and taps from their own seat. Counts draw as groups of five tally strokes with a vermilion seal for the leader."),
                ("Watch the restaurant clock", "Enable Time limit before starting or from the More menu to track remaining minutes, see the last-order mark and receive local notifications before last order and at the end."),
                ("Finish on the slip", "Tap Finish to see standings, titles (Sushi champion, First bite, Last bite, Biggest bill) and the How the night went chart. Share the slip as an image or share the bill split as text."),
            ],
            "faq_title": "Questions & Answers",
            "faqs": [
                ("What is free and what is Sushi Night Pro?", "Free: two diners at an all-you-can-eat dinner, In the middle of the table facing both sides, tally marks and seals, Take one back and Undo, Time limit with local last-order alerts, and the closing slip with How the night went and Share slip. Sushi Night Pro is a one-time non-consumable purchase (no subscription) unlocking up to 12 diners, Kaiten plate colors and prices, Who pays what (with drinks, shared extras, set price per person and service), Your places and Past dinners with all-time records."),
                ("Why did no time-limit notification arrive?", "Local alerts only fire when a Time limit is turned on and notification permission is allowed. If you refused permission, the sitting clock still counts on screen. You can turn notifications on in iOS Settings > Notifications > Sushi Night."),
                ("Where do I restore my Pro purchase?", "Open the Pro sheet or Settings (the gear icon on the setup screen) and tap Restore Purchase while signed in to the Apple Account used for the purchase. Refunds are handled by Apple at reportaproblem.apple.com."),
                ("Do I need an internet connection?", "No. Counting, saved dinners, saved places and local alerts work offline on your device. Internet access is only used by Apple StoreKit when fetching prices, buying or restoring Sushi Night Pro."),
                ("Are the bill amounts official?", "No. Amounts on the slip and Who pays what are an estimate for the table; the restaurant's bill is always what counts."),
            ],
        },
        "privacy": {
            "title": "Privacy Policy",
            "lede": "Sushi Night works entirely offline on your device. No account, no analytics, no ads and no servers.",
            "summary_title": "Summary",
            "rows": [
                ("Data collected by us", "None"),
                ("Accounts & sign-in", "None required"),
                ("Ads & third-party SDKs", "None"),
                ("Storage", "On-device UserDefaults and local Application Support history file"),
                ("Delete all data", "Settings > Delete all past dinners, or remove the app"),
            ],
            "sections": [
                ("On-device storage", "Your active table, setup preferences (sound and haptics toggles), saved restaurants and past dinner slips remain exclusively on your iPhone or iPad. Nothing is uploaded or shared with us or third parties."),
                ("Permissions", "Notifications (optional) are scheduled locally on your device solely for the restaurant time-limit and last-order reminders. If you choose Save Image inside the iOS share sheet for a slip image, iOS uses add-only photo library write permission; Sushi Night never reads your photo library or uses the camera."),
                ("In-app purchase", "Sushi Night Pro (app.klarwerk.sushicounter.unlock) is a single non-consumable purchase handled directly by Apple through StoreKit 2. We never see your payment details or Apple Account."),
                ("Contact", f'For privacy or support questions, email <a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a>.'),
            ],
        },
    },
    "de-DE": {
        "name": "Deutsch",
        "html_lang": "de",
        "app": "Sushi-Abend",
        "subtitle": "All you can eat & Laufband",
        "nav_help": "Hilfe",
        "nav_privacy": "Datenschutz",
        "nav_langs": "Alle Sprachen",
        "contact_title": "Support & Kontakt",
        "contact_body": f'Fragen oder Hinweise zu Sushi-Abend: <a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a>.',
        "updated": f"Stand {UPDATED} · Sushi-Abend (app.klarwerk.sushicounter) · Hayri Odabaş",
        "help": {
            "title": "Hilfe & Anleitung",
            "lede": "Zähle den ganzen Tisch mit einem Handy: Strichlisten für jede Person, Zeitlimit mit letzter Bestellung und ein Zettel über den Verlauf des Abends.",
            "steps_title": "Am Tisch",
            "steps": [
                ("Tisch einrichten", "Wähle Avatare und optionale Namen, entscheide zwischen All you can eat und Laufband (Pro) und aktiviere In der Tischmitte, wenn ihr euch gegenübersitzt."),
                ("Gemeinsam zählen", "Ist In der Tischmitte aktiv, drehen sich die Bahnen der Gegenseite um 180°. Alle lesen richtig herum und tippen vom eigenen Platz aus."),
                ("Zeitlimit im Blick", "Aktiviere das Zeitlimit vor dem Start oder im Mehr-Menü, um Restzeit, Markierung für die letzte Bestellung und lokale Erinnerungen zu sehen."),
                ("Auf dem Zettel abschließen", "Tippe auf Beenden für Plätze, Titel des Abends und die Verlaufsgrafik. Teile den Zettel als Bild oder die Abrechnung als Text."),
            ],
            "faq_title": "Häufige Fragen",
            "faqs": [
                ("Was ist kostenlos und was bietet Sushi-Abend Pro?", "Kostenlos: 2 Personen beim All you can eat, In der Tischmitte für beide Seiten, Strichlisten und Siegel, Eins zurück und Rückgängig, Zeitlimit mit Erinnerung und Zettel mit Abendverlauf und Teilen. Sushi-Abend Pro (Einmalkauf, kein Abo) schaltet bis zu 12 Personen, Laufband-Tellerpreise, Wer zahlt was, Deine Lokale sowie Verlauf und Rekorde frei."),
                ("Warum kommt keine Erinnerung?", "Lokale Mitteilungen erscheinen nur bei aktivem Zeitlimit und erlaubten Mitteilungen. Aktiviere sie bei Bedarf unter iOS-Einstellungen > Mitteilungen > Sushi-Abend."),
                ("Wie stelle ich meinen Kauf wieder her?", "Öffne das Pro-Blatt oder die Einstellungen und tippe auf Kauf wiederherstellen mit demselben Apple Account. Erstattungen verwaltet Apple unter reportaproblem.apple.com."),
                ("Braucht die App Internet?", "Nein. Zählen, Zeitlimit und Verlauf laufen offline auf dem Gerät. Nur der App Store nutzt das Netz beim Kauf oder Wiederherstellen von Pro."),
            ],
        },
        "privacy": {
            "title": "Datenschutz",
            "lede": "Sushi-Abend arbeitet vollständig offline auf deinem Gerät. Kein Konto, keine Analyse und keine Werbung.",
            "summary_title": "Kurzfassung",
            "rows": [
                ("Erhobene Daten", "Keine"),
                ("Konto & Anmeldung", "Nicht erforderlich"),
                ("Werbung & Drittanbieter-SDKs", "Keine"),
                ("Speicherort", "Nur lokal auf dem Gerät"),
                ("Daten löschen", "Einstellungen > Alle früheren Essen löschen oder App entfernen"),
            ],
            "sections": [
                ("Lokale Speicherung", "Aktive Abende, Einstellungen, gespeicherte Lokale und der Verlauf bleiben ausschließlich auf deinem iPhone oder iPad."),
                ("Berechtigungen", "Mitteilungen werden nur lokal für das Zeitlimit geplant. Wenn du im Teilen-Menü Bild sichern wählst, nutzt iOS nur das Schreibrecht zum Hinzufügen; die Mediathek wird nicht gelesen."),
                ("In-App-Kauf", "Sushi-Abend Pro wird als Einmalkauf direkt über StoreKit 2 von Apple abgewickelt."),
            ],
        },
    },
    "es-ES": {
        "name": "Español",
        "html_lang": "es",
        "app": "Noche de Sushi",
        "subtitle": "Buffet Libre y Kaiten",
        "nav_help": "Ayuda",
        "nav_privacy": "Privacidad",
        "nav_langs": "Todos los idiomas",
        "contact_title": "Soporte y contacto",
        "contact_body": f'Dudas o sugerencias sobre Noche de Sushi: <a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a>.',
        "updated": f"Actualizado {UPDATED} · Noche de Sushi (app.klarwerk.sushicounter) · Hayri Odabaş",
        "help": {
            "title": "Ayuda y guía",
            "lede": "Cuenta toda la mesa con un solo móvil: grupos de cinco rayas, límite de tiempo con última ronda y ticket final con cómo fue la noche.",
            "steps_title": "En la mesa",
            "steps": [
                ("Prepara la mesa", "Elige avatares y nombres opcionales, selecciona Sushi libre o Kaiten (Pro) y activa En el centro de la mesa si os sentáis frente a frente."),
                ("Contad a la vez", "Con En el centro de la mesa activado, los marcadores del otro lado giran 180° para que cada persona lea del derecho y toque desde su sitio."),
                ("Controla el tiempo", "Activa Límite de tiempo antes de empezar o desde el menú Más para ver el tiempo restante y recibir avisos locales de última ronda y fin."),
                ("Cierra con el ticket", "Toca Terminar para ver puestos, títulos de la noche y el gráfico del recorrido. Comparte el ticket como imagen o la cuenta como texto."),
            ],
            "faq_title": "Preguntas frecuentes",
            "faqs": [
                ("¿Qué es gratis y qué incluye Noche de Sushi Pro?", "Gratis: mesa de 2 personas en sushi libre, En el centro de la mesa, rayas y sellos, Quitar una y deshacer, límite de tiempo y ticket con cómo fue la noche y compartir. Pro (pago único, sin suscripción) añade hasta 12 comensales, precios de platos kaiten, quién paga qué, Tus sitios e historial con récords."),
                ("¿Por qué no llegan avisos?", "Solo se envían con el límite de tiempo activo y notificaciones permitidas en Ajustes > Notificaciones > Noche de Sushi."),
                ("¿Cómo restauro Pro?", "En la hoja Pro o en Ajustes toca Restaurar compra con la misma cuenta de Apple. Reembolsos en reportaproblem.apple.com."),
            ],
        },
        "privacy": {
            "title": "Política de privacidad",
            "lede": "Noche de Sushi funciona sin conexión en tu dispositivo. Sin cuentas, sin análisis y sin anuncios.",
            "summary_title": "Resumen",
            "rows": [
                ("Datos recogidos", "Ninguno"),
                ("Cuentas o inicio de sesión", "No hace falta"),
                ("Anuncios y SDK de terceros", "Ninguno"),
                ("Almacenamiento", "Solo en este iPhone o iPad"),
                ("Borrar datos", "Ajustes > Borrar todas las cenas anteriores o desinstalar la app"),
            ],
            "sections": [
                ("Datos en el dispositivo", "Todas las cenas, restaurantes guardados y preferencias permanecen únicamente en tu dispositivo."),
                ("Permisos", "Las notificaciones son locales para el límite de tiempo. Al elegir Guardar imagen en la hoja de compartir, iOS solo añade esa imagen sin leer tu fototeca."),
                ("Compra integrada", "Noche de Sushi Pro es un pago único procesado directamente por Apple con StoreKit 2."),
            ],
        },
    },
    "fr-FR": {
        "name": "Français",
        "html_lang": "fr",
        "app": "Soirée Sushi",
        "subtitle": "À volonté & Kaiten",
        "nav_help": "Aide",
        "nav_privacy": "Confidentialité",
        "nav_langs": "Toutes les langues",
        "contact_title": "Assistance et contact",
        "contact_body": f'Questions ou retours sur Soirée Sushi : <a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a>.',
        "updated": f"Mis à jour le {UPDATED} · Soirée Sushi (app.klarwerk.sushicounter) · Hayri Odabaş",
        "help": {
            "title": "Aide et guide",
            "lede": "Comptez toute la tablée sur un seul téléphone : traits par groupes de cinq, limite de temps et ticket final avec le fil de la soirée.",
            "steps_title": "À table",
            "steps": [
                ("Préparer la table", "Choisissez les icônes et prénoms facultatifs, sélectionnez À volonté ou Kaiten (Pro) et activez Au milieu de la table."),
                ("Compter des deux côtés", "Avec Au milieu de la table, les lignes d'en face pivotent à 180° pour être lues à l'endroit depuis chaque place."),
                ("Suivre la limite de temps", "Activez Limite de temps pour afficher le temps restant, la marque de dernière commande et recevoir des rappels locaux."),
                ("Consulter le ticket", "Touchez Terminer pour voir le classement, les titres et le graphique de la soirée, puis partagez le ticket en image."),
            ],
            "faq_title": "Questions fréquentes",
            "faqs": [
                ("Qu'est-ce qui est gratuit et qu'ajoute Pro ?", "Gratuit : 2 convives à volonté, Au milieu de la table, traits et sceaux, Retirer une et annuler, limite de temps et ticket avec fil de la soirée. Soirée Sushi Pro (paiement unique sans abonnement) débloque jusqu'à 12 personnes, prix kaiten, qui paie quoi, Vos adresses et l'historique."),
                ("Comment restaurer mon achat ?", "Touchez Restaurer l'achat sur la feuille Pro ou dans Réglages avec le même compte Apple."),
            ],
        },
        "privacy": {
            "title": "Politique de confidentialité",
            "lede": "Soirée Sushi fonctionne hors ligne sur votre appareil. Sans compte, sans publicité et sans suivi.",
            "summary_title": "En bref",
            "rows": [
                ("Données collectées", "Aucune"),
                ("Compte ou connexion", "Aucun"),
                ("Publicité et SDK tiers", "Aucun"),
                ("Stockage", "Uniquement sur votre appareil"),
                ("Suppression", "Réglages > Supprimer tous les repas passés"),
            ],
            "sections": [
                ("Stockage local", "Les repas, adresses enregistrées et réglages restent uniquement sur votre iPhone ou iPad."),
                ("Autorisations", "Les notifications locales servent uniquement aux rappels de limite de temps. L'option Enregistrer l'image du menu Partager écrit sans jamais lire votre photothèque."),
                ("Achat intégré", "Soirée Sushi Pro est un achat unique traité exclusivement par Apple via StoreKit 2."),
            ],
        },
    },
    "it": {
        "name": "Italiano",
        "html_lang": "it",
        "app": "Serata Sushi",
        "subtitle": "All you can eat & Kaiten",
        "nav_help": "Aiuto",
        "nav_privacy": "Privacy",
        "nav_langs": "Tutte le lingue",
        "contact_title": "Assistenza e contatti",
        "contact_body": f'Domande o segnalazioni per Serata Sushi: <a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a>.',
        "updated": f"Aggiornato il {UPDATED} · Serata Sushi (app.klarwerk.sushicounter) · Hayri Odabaş",
        "help": {
            "title": "Aiuto e guida",
            "lede": "Conta tutto il tavolo su un solo telefono: segni a gruppi di cinque, limite di tempo e scontrino con l'andamento della serata.",
            "steps_title": "A tavola",
            "steps": [
                ("Prepara il tavolo", "Scegli gli avatar e i nomi facoltativi, seleziona All you can eat o Kaiten (Pro) e attiva Al centro del tavolo."),
                ("Conta da entrambi i lati", "Con Al centro del tavolo, le corsie del lato opposto ruotano di 180° per leggere e toccare dal proprio posto."),
                ("Controlla l'orologio", "Attiva Limite di tempo per vedere i minuti rimasti, l'ultimo ordine e ricevere avvisi locali."),
                ("Chiudi con lo scontrino", "Tocca Fine per classifiche, titoli, grafico della serata e condivisione come immagine."),
            ],
            "faq_title": "Domande frequenti",
            "faqs": [
                ("Cosa è gratis e cosa offre Pro?", "Gratis: 2 persone all you can eat, Al centro del tavolo, segni e sigilli, annulla, limite di tempo e scontrino con andamento della serata. Serata Sushi Pro (acquisto unico senza abbonamento) sblocca fino a 12 commensali, prezzi kaiten, chi paga cosa, I tuoi locali e storico."),
                ("Come ripristino l'acquisto?", "Apri la scheda Pro o Impostazioni e tocca Ripristina acquisto con lo stesso Apple Account."),
            ],
        },
        "privacy": {
            "title": "Informativa sulla privacy",
            "lede": "Serata Sushi funziona offline sul tuo dispositivo. Nessun account, nessuna analisi e nessuna pubblicità.",
            "summary_title": "Riepilogo",
            "rows": [
                ("Dati raccolti", "Nessuno"),
                ("Account e accesso", "Non richiesti"),
                ("Pubblicità e SDK di terzi", "Nessuno"),
                ("Archiviazione", "Solo locale sul dispositivo"),
                ("Eliminazione dati", "Impostazioni > Elimina tutte le cene passate"),
            ],
            "sections": [
                ("Archiviazione locale", "Cene, locali salvati e preferenze restano solo sul tuo iPhone o iPad."),
                ("Permessi", "Le notifiche locali valgono solo per il limite di tempo. Salva immagine dal foglio di condivisione scrive senza leggere la libreria foto."),
                ("Acquisto in-app", "Serata Sushi Pro è un acquisto unico gestito da Apple tramite StoreKit 2."),
            ],
        },
    },
    "pt-BR": {
        "name": "Português",
        "html_lang": "pt-BR",
        "app": "Noite de Sushi",
        "subtitle": "Rodízio & Esteira",
        "nav_help": "Ajuda",
        "nav_privacy": "Privacidade",
        "nav_langs": "Todos os idiomas",
        "contact_title": "Suporte e contato",
        "contact_body": f'Dúvidas ou sugestões sobre Noite de Sushi: <a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a>.',
        "updated": f"Atualizado em {UPDATED} · Noite de Sushi (app.klarwerk.sushicounter) · Hayri Odabaş",
        "help": {
            "title": "Ajuda e guia",
            "lede": "Conte a mesa toda em um só celular: riscos em grupos de cinco, limite de tempo e comanda com o resumo da noite.",
            "steps_title": "Na mesa",
            "steps": [
                ("Monte a mesa", "Escolha avatares e nomes opcionais, selecione Rodízio ou Esteira (Pro) e ative No meio da mesa."),
                ("Conte dos dois lados", "Com No meio da mesa ativo, as faixas do outro lado giram 180° para quem está à frente ler direito e tocar do seu lugar."),
                ("Acompanhe o tempo", "Ative Limite de tempo para ver o tempo restante, a marca de último pedido e receber avisos locais."),
                ("Feche na comanda", "Toque em Terminar para ver posições, títulos, o gráfico da noite e compartilhar como imagem."),
            ],
            "faq_title": "Perguntas frequentes",
            "faqs": [
                ("O que é grátis e o que vem no Pro?", "Grátis: mesa para 2 no rodízio, No meio da mesa, riscos e selos, desfazer, limite de tempo e comanda com gráfico da noite. Noite de Sushi Pro (pagamento único, sem assinatura) libera até 12 pessoas, preços da esteira, quem paga o quê, Seus restaurantes e histórico."),
                ("Como restaurar a compra?", "Toque em Restaurar compra na tela Pro ou em Ajustes com a mesma Conta Apple."),
            ],
        },
        "privacy": {
            "title": "Política de privacidade",
            "lede": "Noite de Sushi funciona offline no seu aparelho. Sem conta, sem rastreamento e sem anúncios.",
            "summary_title": "Resumo",
            "rows": [
                ("Dados coletados", "Nenhum"),
                ("Conta e login", "Não exige"),
                ("Anúncios e SDKs de terceiros", "Nenhum"),
                ("Armazenamento", "Somente local no aparelho"),
                ("Apagar dados", "Ajustes > Apagar todas as refeições anteriores"),
            ],
            "sections": [
                ("Dados locais", "Refeições, restaurantes salvos e preferências ficam apenas no seu iPhone ou iPad."),
                ("Permissões", "Notificações locais servem só para o limite de tempo. Salvar Imagem na folha de compartilhamento grava sem ler sua fototeca."),
                ("Compra no app", "Noite de Sushi Pro é uma compra única processada pela Apple via StoreKit 2."),
            ],
        },
    },
    "nl-NL": {
        "name": "Nederlands",
        "html_lang": "nl",
        "app": "Sushi-avond",
        "subtitle": "All you can eat & Lopende band",
        "nav_help": "Hulp",
        "nav_privacy": "Privacybeleid",
        "nav_langs": "Alle talen",
        "contact_title": "Ondersteuning & contact",
        "contact_body": f'Vragen of feedback over Sushi-avond: <a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a>.',
        "updated": f"Bijgewerkt {UPDATED} · Sushi-avond (app.klarwerk.sushicounter) · Hayri Odabaş",
        "help": {
            "title": "Hulp & uitleg",
            "lede": "Tel de hele tafel op één telefoon: turfstreepjes in groepjes van vijf, tijdslimiet met laatste bestelronde en een bonnetje van de avond.",
            "steps_title": "Aan tafel",
            "steps": [
                ("Tafel instellen", "Kies iconen en optionele namen, kies All you can eat of Lopende band (Pro) en zet In het midden van de tafel aan."),
                ("Samen tellen", "Staat In het midden aan, dan draaien de banen aan de overkant 180° zodat iedereen vanaf de eigen plek rechtop leest en tikt."),
                ("Tijdslimiet volgen", "Zet Tijdslimiet aan voor de resterende tijd, laatste bestelronde en lokale meldingen."),
                ("Afronden op het bonnetje", "Tik op Klaar voor de stand, titels, de grafiek van de avond en het delen als afbeelding."),
            ],
            "faq_title": "Veelgestelde vragen",
            "faqs": [
                ("Wat is gratis en wat zit in Pro?", "Gratis: 2 personen all you can eat, In het midden van de tafel, turfstreepjes en zegels, ongedaan maken, tijdslimiet en bonnetje met verloop van de avond. Sushi-avond Pro (eenmalig, geen abonnement) biedt tot 12 personen, bandprijzen, wie betaalt wat, Je restaurants en geschiedenis."),
                ("Hoe herstel ik mijn aankoop?", "Tik op Aankoop herstellen in het Pro-scherm of bij Instellingen met dezelfde Apple Account."),
            ],
        },
        "privacy": {
            "title": "Privacybeleid",
            "lede": "Sushi-avond werkt volledig offline op je apparaat. Geen account, geen analyses en geen reclame.",
            "summary_title": "Overzicht",
            "rows": [
                ("Verzamelde gegevens", "Geen"),
                ("Account of inloggen", "Niet nodig"),
                ("Reclame & externe SDK's", "Geen"),
                ("Opslag", "Alleen lokaal op het apparaat"),
                ("Gegevens wissen", "Instellingen > Wis alle eerdere etentjes"),
            ],
            "sections": [
                ("Lokale opslag", "Etentjes, bewaarde restaurants en voorkeuren blijven uitsluitend op je iPhone of iPad."),
                ("Machtigingen", "Lokale meldingen zijn alleen voor tijdslimieten. Bewaar afbeelding via het deelmenu schrijft zonder je fotobibliotheek te lezen."),
                ("In-app aankoop", "Sushi-avond Pro is een eenmalige aankoop via Apple StoreKit 2."),
            ],
        },
    },
    "ja": {
        "name": "日本語",
        "html_lang": "ja",
        "app": "寿司ナイト",
        "subtitle": "食べ放題・回転寿司カウンター",
        "nav_help": "ヘルプ",
        "nav_privacy": "プライバシーポリシー",
        "nav_langs": "すべての言語",
        "contact_title": "サポート・お問い合わせ",
        "contact_body": f'寿司ナイトに関するお問い合わせ：<a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a>',
        "updated": f"更新日 {UPDATED} · 寿司ナイト (app.klarwerk.sushicounter) · Hayri Odabaş",
        "help": {
            "title": "ヘルプと使い方",
            "lede": "テーブル全員を1台のスマホでカウント。正の字の記録、食べ放題の制限時間とラストオーダー通知、今夜の流れが伝票に残ります。",
            "steps_title": "テーブルでの使い方",
            "steps": [
                ("テーブルを設定", "アイコンと名前（任意）を選び、食べ放題または回転寿司（Pro）を選択します。向かい合って座る場合は「テーブルの真ん中に置く」をオンにします。"),
                ("両側からカウント", "「テーブルの真ん中に置く」をオンにすると向かいのレーンが180°回転し、自分の席から正しい向きで見てタップできます。"),
                ("制限時間とラストオーダー", "開始前やその他メニューから制限時間を設定すると、残り時間とラストオーダーの目安、ローカル通知が届きます。"),
                ("伝票で締める", "終了をタップすると順位、タイトル、今夜の流れグラフを表示し、画像や割り勘テキストとして共有できます。"),
            ],
            "faq_title": "よくある質問",
            "faqs": [
                ("無料版と寿司ナイト Proの違いは？", "無料版：食べ放題2人まで、テーブルの真ん中に置く、正の字と順位印、1つ戻す・取り消し、制限時間通知、今夜の流れ付き伝票と画像共有。Pro（買い切り・サブスクなし）で最大12人、回転寿司の色別価格、会計計算、お店の登録、履歴と記録が解放されます。"),
                ("購入を復元するには？", "設定またはPro画面の「購入を復元」を購入時のApple Accountでタップしてください。"),
            ],
        },
        "privacy": {
            "title": "プライバシーポリシー",
            "lede": "寿司ナイトはお使いの端末内で完全にオフライン動作します。アカウント登録、広告、計測SDKはありません。",
            "summary_title": "概要",
            "rows": [
                ("収集するデータ", "なし"),
                ("アカウント・ログイン", "不要"),
                ("広告・外部SDK", "なし"),
                ("保存場所", "端末内ローカルのみ"),
                ("データ削除", "設定 ＞ これまでの食事をすべて削除"),
            ],
            "sections": [
                ("端末内保存", "食事の記録、登録したお店、設定はすべてお使いのiPhoneまたはiPad内のみに保存され、外部に送信されません。"),
                ("権限について", "通知は制限時間とラストオーダーのローカル通知のみに使用します。共有シートで「画像を保存」を選んだ場合のみ追加保存を行い、写真ライブラリは読み取りません。"),
                ("アプリ内課金", "寿司ナイト Pro は Apple StoreKit 2 による1回限りの買い切り課金です。"),
            ],
        },
    },
    "ko": {
        "name": "한국어",
        "html_lang": "ko",
        "app": "스시 나이트",
        "subtitle": "무한리필 · 회전초밥",
        "nav_help": "도움말",
        "nav_privacy": "개인정보 처리방침",
        "nav_langs": "모든 언어",
        "contact_title": "지원 및 문의",
        "contact_body": f'스시 나이트 문의: <a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a>',
        "updated": f"업데이트 {UPDATED} · 스시 나이트 (app.klarwerk.sushicounter) · Hayri Odabaş",
        "help": {
            "title": "도움말 및 안내",
            "lede": "폰 한 대로 테이블 전체를 세세요. 바를 정(正)자 카운트, 제한 시간과 라스트 오더 알림, 오늘의 흐름이 전표로 남습니다.",
            "steps_title": "사용 방법",
            "steps": [
                ("테이블 설정", "아바타와 이름(선택)을 고르고 무한리필 또는 회전초밥(Pro)을 선택한 뒤, 마주 앉았다면 '테이블 가운데에 두기'를 켜세요."),
                ("양쪽에서 함께 세기", "가운데 두기를 켜면 맞은편 레인이 180° 회전해 맞은편에서도 똑바로 보고 자기 자리에서 탭할 수 있습니다."),
                ("제한 시간 확인", "시작 전이나 더 보기 메뉴에서 제한 시간을 켜면 남은 시간과 라스트 오더 표시, 로컬 알림을 받을 수 있습니다."),
                ("전표로 마무리", "종료를 누르면 순위, 타이틀, 오늘의 흐름 그래프가 표시되며 이미지나 정산 텍스트로 공유할 수 있습니다."),
            ],
            "faq_title": "자주 묻는 질문",
            "faqs": [
                ("무료 기능과 스시 나이트 Pro 차이는 무엇인가요?", "무료: 무한리필 2명, 테이블 가운데에 두기, 바를 정(正)자 및 순위 도장, 취소, 제한 시간 알림, 오늘의 흐름 전표와 공유. Pro(구독 없는 1회 결제)는 최대 12명, 회전초밥 접시 가격, 1인별 계산, 내 식당 저장, 히스토리 및 기록을 제공합니다."),
                ("구입 내역을 복원하려면?", "설정 또는 Pro 화면에서 구입 시 사용한 Apple 계정으로 '구입 복원'을 누르세요."),
            ],
        },
        "privacy": {
            "title": "개인정보 처리방침",
            "lede": "스시 나이트는 기기에서 완전히 오프라인으로 동작합니다. 계정, 광고, 추적 SDK가 없습니다.",
            "summary_title": "요약",
            "rows": [
                ("수집하는 데이터", "없음"),
                ("계정 및 로그인", "불필요"),
                ("광고 및 외부 SDK", "없음"),
                ("저장 위치", "기기 내부 전용 저장소"),
                ("데이터 삭제", "설정 > 지난 식사 모두 삭제"),
            ],
            "sections": [
                ("기기 내 저장", "모든 식사 기록과 저장된 식당, 설정은 사용자의 iPhone 또는 iPad에만 저장됩니다."),
                ("권한 안내", "알림은 제한 시간과 라스트 오더 로컬 알림에만 사용됩니다. 공유 시트에서 이미지 저장을 선택할 때만 저장하며 사진 보관함을 읽지 않습니다."),
                ("앱 내 구입", "스시 나이트 Pro는 Apple StoreKit 2로 처리되는 1회성 비소모성 구입입니다."),
            ],
        },
    },
    "zh-Hans": {
        "name": "简体中文",
        "html_lang": "zh-Hans",
        "app": "寿司之夜",
        "subtitle": "自助畅吃 · 回转寿司",
        "nav_help": "帮助",
        "nav_privacy": "隐私政策",
        "nav_langs": "全部语言",
        "contact_title": "支持与联系",
        "contact_body": f'关于寿司之夜的问题或建议：<a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a>',
        "updated": f"更新日期 {UPDATED} · 寿司之夜 (app.klarwerk.sushicounter) · Hayri Odabaş",
        "help": {
            "title": "帮助与指南",
            "lede": "一部手机数完整桌寿司：正字计数、限时与最后点单提醒，以及记录今晚走势的结算小票。",
            "steps_title": "餐桌使用",
            "steps": [
                ("设置餐桌", "选择头像并填写可选昵称，选择自助畅吃或回转寿司（Pro），对面有人时开启“放在桌子中间”。"),
                ("双向同桌计数", "开启“放在桌子中间”后，对面食客的计数栏会旋转 180°，坐在对面也能正着查看并直接点击。"),
                ("查看用餐限时", "在开始前或“更多”菜单中开启限时，即可查看剩余时间、最后点单标记和本地提醒。"),
                ("生成小票", "点击“结束”查看排名、夜场头衔和走势曲线图，并可将小票保存为图片或发送账单文本。"),
            ],
            "faq_title": "常见问题",
            "faqs": [
                ("免费版和寿司之夜 Pro 有什么区别？", "免费包含：2 人自助畅吃、放在桌子中间双向计数、正字划记与名次印章、撤销、限时提醒以及含走势图的小票与分享。Pro 为一次性买断（无订阅），解锁最多 12 人、回转寿司盘色价格、每人账单分摊、常去餐厅和历史纪录。"),
                ("如何恢复购买？", "请在设置或 Pro 页面使用购买时的 Apple 账户点击“恢复购买”。"),
            ],
        },
        "privacy": {
            "title": "隐私政策",
            "lede": "寿司之夜完全在设备本地离线运行。无需登录，无广告，无数据收集。",
            "summary_title": "摘要",
            "rows": [
                ("收集的数据", "无"),
                ("账号与登录", "无需账号"),
                ("广告与第三方 SDK", "无"),
                ("数据存储", "仅限设备本地"),
                ("删除数据", "设置 > 删除所有过往聚餐"),
            ],
            "sections": [
                ("本地存储", "所有聚餐记录、常去餐厅与设置均仅保留在您的 iPhone 或 iPad 上，不会上传至任何服务器。"),
                ("权限说明", "通知权限仅用于本地限时与最后点单提醒。仅当您在系统分享菜单选择保存图片时写入相册，应用不会读取相册或使用相机。"),
                ("应用内购买", "寿司之夜 Pro 通过 Apple StoreKit 2 一次性买断，我们无法获取您的支付信息。"),
            ],
        },
    },
    "ru": {
        "name": "Русский",
        "html_lang": "ru",
        "app": "Суши-вечер",
        "subtitle": "Безлимит и конвейер",
        "nav_help": "Помощь",
        "nav_privacy": "Конфиденциальность",
        "nav_langs": "Все языки",
        "contact_title": "Поддержка и контакты",
        "contact_body": f'Вопросы и отзывы о Суши-вечере: <a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a>.',
        "updated": f"Обновлено {UPDATED} · Суши-вечер (app.klarwerk.sushicounter) · Hayri Odabaş",
        "help": {
            "title": "Помощь и руководство",
            "lede": "Весь стол на одном телефоне: черточки по пять, таймер с последним заказом и итоговый чек с графиком вечера.",
            "steps_title": "За столом",
            "steps": [
                ("Настройте стол", "Выберите аватары и имена, укажите Безлимит или Конвейер (Pro) и включите «Посередине стола», если сидите напротив."),
                ("Считайте с двух сторон", "Когда телефон лежит посередине, дорожки напротив поворачиваются на 180°, чтобы каждый читал свой счёт прямо и нажимал со своего места."),
                ("Следите за временем", "Включите лимит времени, чтобы видеть остаток, отметку последнего заказа и получать локальные напоминания."),
                ("Завершите чеком", "Нажмите «Итоги», чтобы увидеть места, звания и график вечера, и поделитесь чеком картинкой."),
            ],
            "faq_title": "Частые вопросы",
            "faqs": [
                ("Что бесплатно, а что в Pro?", "Бесплатно: 2 гостя в безлимите, «Посередине стола», черточки и печати, отмена, лимит времени и чек с графиком вечера и отправкой. Суши-вечер Pro (разовая покупка без подписки) открывает до 12 гостей, цены тарелок конвейера, расчёт на каждого, ваши рестораны и историю с рекордами."),
                ("Как восстановить покупку?", "Нажмите «Восстановить покупку» в окне Pro или в Настройках с тем же Apple Account."),
            ],
        },
        "privacy": {
            "title": "Политика конфиденциальности",
            "lede": "Суши-вечер работает полностью офлайн на вашем устройстве. Без аккаунтов, рекламы и аналитики.",
            "summary_title": "Кратко",
            "rows": [
                ("Собираемые данные", "Нет"),
                ("Аккаунт и вход", "Не требуются"),
                ("Реклама и сторонние SDK", "Нет"),
                ("Хранение", "Только на вашем устройстве"),
                ("Удаление данных", "Настройки > Удалить все прошлые ужины"),
            ],
            "sections": [
                ("Хранение на устройстве", "Ужины, сохранённые рестораны и настройки остаются только на вашем iPhone или iPad."),
                ("Разрешения", "Уведомления локальные и нужны лишь для лимита времени. При выборе «Сохранить изображение» в системном меню iOS сохраняет чек без чтения медиатеки."),
                ("Встроенная покупка", "Суши-вечер Pro — разовая покупка, обрабатываемая Apple через StoreKit 2."),
            ],
        },
    },
    "tr": {
        "name": "Türkçe",
        "html_lang": "tr",
        "app": "Sushi Gecesi",
        "subtitle": "Sınırsız ve Kaiten",
        "nav_help": "Yardım",
        "nav_privacy": "Gizlilik",
        "nav_langs": "Tüm diller",
        "contact_title": "Destek ve iletişim",
        "contact_body": f'Sushi Gecesi hakkında soru ve geri bildirimler için: <a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a>.',
        "updated": f"Güncelleme {UPDATED} · Sushi Gecesi (app.klarwerk.sushicounter) · Hayri Odabaş",
        "help": {
            "title": "Yardım ve Kılavuz",
            "lede": "Tüm masayı tek telefonda say: beşli çentikler, son siparişli süre sınırı ve gecenin gidişatını çizen adisyon.",
            "steps_title": "Masada kullanım",
            "steps": [
                ("Masayı kur", "Avatar ve isteğe bağlı adları seç, Sınırsız veya Kaiten (Pro) kipini belirle ve karşılıklı oturuyorsanız Masanın ortasında seçeneğini aç."),
                ("İki taraftan say", "Masanın ortasında açıkken karşı tarafın kulvarları 180° döner; herkes kendi sayısını düz okur ve kendi yerinden dokunur."),
                ("Süre sınırını izle", "Başlamadan önce ya da Diğer menüsünden Süre sınırı ekleyerek kalan süreyi, son sipariş çizgisini ve yerel hatırlatmaları gör."),
                ("Adisyonla bitir", "Bitir'e dokunarak sıralamayı, unvanları ve gece grafiğini gör; adisyonu resim ya da hesap metni olarak paylaş."),
            ],
            "faq_title": "Sık sorulan sorular",
            "faqs": [
                ("Ücretsiz neler var, Sushi Gecesi Pro neler ekler?", "Ücretsiz: Sınırsız kipte 2 kişi, Masanın ortasında iki yönlü masa, beşli çentikler ve lider mühürleri, geri alma, son sipariş uyarılı süre sınırı ve gece grafiğiyle adisyon paylaşımı. Sushi Gecesi Pro (tek seferlik ödeme, abonelik yok) ile 12 kişiye kadar masa, kaiten tabak fiyatları, kişi başı hesap, kayıtlı restoranlar ve geçmiş rekorları açılır."),
                ("Satın almayı nasıl geri yüklerim?", "Pro sayfasında veya Ayarlar'da aynı Apple Hesabı ile Satın almayı geri yükle düğmesine dokunun. İadeler Apple (reportaproblem.apple.com) üzerinden yürütülür."),
            ],
        },
        "privacy": {
            "title": "Gizlilik Politikası",
            "lede": "Sushi Gecesi tamamen cihazınızda ve çevrimdışı çalışır. Hesap yok, reklam yok, veri toplama yok.",
            "summary_title": "Özet",
            "rows": [
                ("Toplanan veri", "Yok"),
                ("Hesap ve giriş", "Gerekmiyor"),
                ("Reklam ve üçüncü taraf SDK", "Yok"),
                ("Depolama", "Yalnızca cihaz içinde"),
                ("Verileri silme", "Ayarlar > Tüm geçmiş yemekleri sil"),
            ],
            "sections": [
                ("Cihaz içi saklama", "Aktif masa, kaydedilen restoranlar, tercihler ve geçmiş yemekler yalnızca iPhone veya iPad cihazınızda saklanır."),
                ("İzinler", "Bildirimler yalnızca süre sınırı ve son sipariş yerel uyarıları içindir. Paylaşım menüsünde Görüntüyü Kaydet seçilirse iOS yalnızca ekleme izniyle adisyon resmini kaydeder; fotoğraf arşivi okunmaz."),
                ("Uygulama içi satın alma", "Sushi Gecesi Pro, Apple StoreKit 2 üzerinden tek seferlik satın alma olarak sunulur; ödeme bilgilerinize erişilmez."),
            ],
        },
    },
}


def lang_bar(current_locale: str, page: str, in_root: bool) -> str:
    chips = []
    for loc, d in LOCALES.items():
        href = f"{loc}/{page}" if in_root else (page if loc == current_locale else f"../{loc}/{page}")
        cls = "lang-chip current" if (loc == current_locale and not in_root) else "lang-chip"
        chips.append(f'<a class="{cls}" href="{href}">{html.escape(d["name"])}</a>')
    return '<div class="lang-strip">' + "".join(chips) + "</div>"


def render_help(locale: str, data: dict, in_root: bool = False) -> str:
    h = data["help"]
    icon_src = "assets/icon.png" if in_root else "../assets/icon.png"
    canonical = f"{BASE_URL}/help.html" if in_root else f"{BASE_URL}/{locale}/help.html"
    idx_href = "index.html" if in_root else "../index.html"
    steps_html = "".join(f"<li><strong>{html.escape(t)}</strong>{html.escape(b)}</li>" for t, b in h["steps"])
    faq_html = "".join(
        f'<div class="slip-card"><h3>{html.escape(q)}</h3><p>{html.escape(a)}</p></div>' for q, a in h["faqs"]
    )
    return f"""<!doctype html>
<html lang="{data['html_lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(data['app'])} — {html.escape(h['title'])}</title>
<link rel="canonical" href="{canonical}">
<style>{CSS}</style>
</head>
<body>
<div class="hinoki-top" aria-hidden="true"></div>
<main>
  <div class="hero">
    <img src="{icon_src}" alt="{html.escape(data['app'])}">
    <div>
      <div class="eyebrow">{html.escape(data['app'])} · {html.escape(data['subtitle'])}</div>
      <h1>{html.escape(h['title'])}</h1>
    </div>
  </div>
  <p class="lede">{html.escape(h['lede'])}</p>
  <nav class="primary-nav">
    <a href="help.html">{html.escape(data['nav_help'])}</a>
    <a href="privacy.html">{html.escape(data['nav_privacy'])}</a>
    <a href="{idx_href}">{html.escape(data['nav_langs'])}</a>
  </nav>
  {lang_bar(locale, "help.html", in_root)}
  <h2>{html.escape(h['steps_title'])}</h2>
  <ol class="slip-steps">{steps_html}</ol>
  <h2>{html.escape(h['faq_title'])}</h2>
  {faq_html}
  <h2>{html.escape(data['contact_title'])}</h2>
  <p>{data['contact_body']}</p>
  <footer>{html.escape(data['updated'])}</footer>
</main>
</body>
</html>
"""


def render_privacy(locale: str, data: dict, in_root: bool = False) -> str:
    p = data["privacy"]
    icon_src = "assets/icon.png" if in_root else "../assets/icon.png"
    canonical = f"{BASE_URL}/privacy.html" if in_root else f"{BASE_URL}/{locale}/privacy.html"
    idx_href = "index.html" if in_root else "../index.html"
    rows_html = "".join(f"<tr><td><strong>{html.escape(k)}</strong></td><td>{html.escape(v)}</td></tr>" for k, v in p["rows"])
    sec_html = "".join(
        f'<div class="slip-card"><h2>{html.escape(t)}</h2><p>{b}</p></div>' for t, b in p["sections"]
    )
    return f"""<!doctype html>
<html lang="{data['html_lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(data['app'])} — {html.escape(p['title'])}</title>
<link rel="canonical" href="{canonical}">
<style>{CSS}</style>
</head>
<body>
<div class="hinoki-top" aria-hidden="true"></div>
<main>
  <div class="hero">
    <img src="{icon_src}" alt="{html.escape(data['app'])}">
    <div>
      <div class="eyebrow">{html.escape(data['app'])} · {html.escape(data['subtitle'])}</div>
      <h1>{html.escape(p['title'])}</h1>
    </div>
  </div>
  <p class="lede">{html.escape(p['lede'])}</p>
  <nav class="primary-nav">
    <a href="help.html">{html.escape(data['nav_help'])}</a>
    <a href="privacy.html">{html.escape(data['nav_privacy'])}</a>
    <a href="{idx_href}">{html.escape(data['nav_langs'])}</a>
  </nav>
  {lang_bar(locale, "privacy.html", in_root)}
  <h2>{html.escape(p['summary_title'])}</h2>
  <table class="fact-table"><tbody>{rows_html}</tbody></table>
  {sec_html}
  <h2>{html.escape(data['contact_title'])}</h2>
  <p>{data['contact_body']}</p>
  <footer>{html.escape(data['updated'])}</footer>
</main>
</body>
</html>
"""


def render_index() -> str:
    items = "".join(
        f'<li><strong>{html.escape(d["name"])}</strong><br>'
        f'<a href="{loc}/help.html">{html.escape(d["nav_help"])}</a> · '
        f'<a href="{loc}/privacy.html">{html.escape(d["nav_privacy"])}</a></li>'
        for loc, d in LOCALES.items()
    )
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Sushi Night: All You Can Eat — Help &amp; Privacy</title>
<link rel="canonical" href="{BASE_URL}/">
<style>{CSS}</style>
</head>
<body>
<div class="hinoki-top" aria-hidden="true"></div>
<main>
  <div class="hero">
    <img src="assets/icon.png" alt="Sushi Night">
    <div>
      <div class="eyebrow">Sushi Night · All You Can Eat &amp; Kaiten</div>
      <h1>Help &amp; Privacy</h1>
    </div>
  </div>
  <p class="lede">Count the whole table on one phone. Offline-first iOS sushi counter with tally marks, time limit alerts and closing slip. Choose your language below.</p>
  <nav class="primary-nav">
    <a href="help.html">English Help</a>
    <a href="privacy.html">Privacy Policy</a>
  </nav>
  <ul class="locale-grid">{items}</ul>
  <footer>Updated {UPDATED} · Sushi Night (app.klarwerk.sushicounter) · Hayri Odabaş · <a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a></footer>
</main>
</body>
</html>
"""


def main() -> None:
    (ROOT / ".nojekyll").write_text("", encoding="utf-8")
    for locale, data in LOCALES.items():
        loc_dir = ROOT / locale
        loc_dir.mkdir(parents=True, exist_ok=True)
        (loc_dir / "help.html").write_text(render_help(locale, data, in_root=False), encoding="utf-8")
        (loc_dir / "privacy.html").write_text(render_privacy(locale, data, in_root=False), encoding="utf-8")
    (ROOT / "index.html").write_text(render_index(), encoding="utf-8")
    (ROOT / "help.html").write_text(render_help("en-US", LOCALES["en-US"], in_root=True), encoding="utf-8")
    (ROOT / "privacy.html").write_text(render_privacy("en-US", LOCALES["en-US"], in_root=True), encoding="utf-8")
    print(f"Generated {len(LOCALES) * 2 + 3} HTML pages in {ROOT}")


if __name__ == "__main__":
    main()
