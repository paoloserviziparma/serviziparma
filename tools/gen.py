#!/usr/bin/env python3
"""Genera l'HTML statico del sito Sistemi Parma nel repository (nessuna build su Netlify)."""
import hashlib, json, os, html, datetime

R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = 'https://www.serviziparma.com'
TODAY = datetime.date(2026, 11, 12).isoformat()

def h(s):  # escape
    return html.escape(s, quote=True)

def vhash(p):
    return hashlib.md5(open(os.path.join(R, p), 'rb').read()).hexdigest()[:10]

CSSV = vhash('assets/css/site.css')
JSV = vhash('assets/js/site.js')

TEL = '0521 252824'
TEL_HREF = 'tel:+390521252824'
MAIL = 'info@serviziparma.com'
ADDR = 'Via Giulio e Giacinto Sicuri 42/a, 43124 Parma (PR)'
MAPS = 'https://www.google.com/maps/search/?api=1&query=Via+Sicuri+42%2Fa+43124+Parma'

ORG = {
    "@context": "https://schema.org",
    "@type": "ProfessionalService",
    "@id": SITE + "/#azienda",
    "name": "Servizi Informatici Srl",
    "alternateName": "Sistemi Parma",
    "description": "Concessionario Sistemi SpA dal 1990: software gestionali per studi professionali e aziende, assistenza e formazione a Parma.",
    "url": SITE + "/",
    "logo": SITE + "/assets/img/logo-sistemi-parma.png",
    "image": SITE + "/assets/img/og-sistemi-parma.jpg",
    "telephone": "+39 0521 252824",
    "email": MAIL,
    "vatID": "IT01721620340",
    "foundingDate": "1990",
    "numberOfEmployees": {"@type": "QuantitativeValue", "value": 14},
    "address": {"@type": "PostalAddress", "streetAddress": "Via Giulio e Giacinto Sicuri 42/a",
                "postalCode": "43124", "addressLocality": "Parma", "addressRegion": "PR", "addressCountry": "IT"},
    "areaServed": [{"@type": "AdministrativeArea", "name": n} for n in ("Provincia di Parma", "Provincia di Piacenza", "Provincia di Reggio Emilia")],
    "hasMap": MAPS,
}

NAV = [
    ('/professionisti/', 'Professionisti'),
    ('/aziende/', 'Aziende'),
    ('/corsi/', 'Corsi'),
    ('/pillole/', 'Le Pillole'),
    ('/assistenza/', 'Assistenza'),
    ('/#chi-siamo', 'Chi siamo'),
]

ICONS = {
    'cloud': '<path d="M18 10h-1.26A8 8 0 1 0 9 20h9a5 5 0 0 0 0-10z"/>',
    'lock': '<rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/>',
    'tool': '<path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/>',
    'globe': '<circle cx="12" cy="12" r="10"/><path d="M2 12h20"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/>',
    'users': '<path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/>',
    'check': '<path d="M20 6 9 17l-5-5"/>',
    'play': '',
    'grid': '<rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/>',
    'file': '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6"/>',
    'chart': '<path d="M3 3v18h18"/><path d="m7 15 4-4 3 3 5-6"/>',
    'calendar': '<rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/>',
    'phone': '<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.8 19.8 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.18 2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.9.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92z"/>',
}

def icon(name, cls='icon'):
    return f'<svg class="{cls}" aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">{ICONS[name]}</svg>'

PLAY = '<svg aria-hidden="true" width="22" height="22" viewBox="0 0 24 24" fill="#141414"><path d="M8 5v14l11-7z"/></svg>'

def header(current):
    items = ''.join(
        f'<li><a href="{u}"{" aria-current=\"page\"" if current and u.rstrip("/") and current.startswith(u) and not u.startswith("/#") else ""}>{t}</a></li>'
        for u, t in NAV)
    return f'''<a class="skip" href="#contenuto">Vai al contenuto</a>
<header class="site-header">
  <div class="site-header__in">
    <a class="brand" href="/" aria-label="Sistemi Parma – Servizi Informatici Srl, home"><img src="/assets/img/logo-sistemi-parma.png" alt="Sistemi Parma" width="900" height="391"></a>
    <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="nav" aria-label="Apri il menu"><span></span><span></span><span></span></button>
    <nav class="nav" id="nav" aria-label="Menu principale">
      <ul>{items}<li class="nav-cta"><a class="btn btn--red" href="/contatti/">Contattaci</a></li></ul>
    </nav>
    <a class="btn btn--red header-cta" href="/contatti/">Contattaci</a>
  </div>
</header>'''

FOOTER = f'''<footer class="site-footer">
  <div class="wrap site-footer__in">
    <div>
      <img class="site-footer__logo" src="/assets/img/logo-sistemi-parma-bianco.png" alt="Sistemi Parma" width="900" height="391" loading="lazy">
      <p>Servizi Informatici Srl<br>Via Sicuri 42/a · 43124 Parma (PR)<br>P.IVA 01721620340</p>
    </div>
    <div><b>Professionisti</b><ul>
      <li><a href="/professionisti/profis/">Profis</a></li><li><a href="/professionisti/studio/">Studio</a></li><li><a href="/professionisti/job/">Job</a></li></ul></div>
    <div><b>Aziende</b><ul>
      <li><a href="/aziende/spring/">Spring</a></li><li><a href="/aziende/esolver/">eSolver</a></li><li><a href="/aziende/profis-az/">Profis AZ</a></li><li><a href="/aziende/quadra/">Quadra</a></li><li><a href="/aziende/verticali/">Gestionali verticali</a></li></ul></div>
    <div><b>Servizi</b><ul>
      <li><a href="/corsi/">Corsi ed eventi</a></li><li><a href="/assistenza/">Assistenza remota</a></li><li><a href="/whistleblowing/">Whistleblowing</a></li><li><a href="/siti-web/">Siti web</a></li><li><a href="/pillole/">Le Pillole</a></li></ul></div>
    <div><b>Contatti</b><ul>
      <li><a href="{TEL_HREF}">{TEL}</a></li><li><a href="mailto:{MAIL}">{MAIL}</a></li><li><a href="{MAPS}" rel="noopener" target="_blank">Via Sicuri 42/a, Parma</a></li></ul></div>
  </div>
  <div class="wrap site-footer__bottom">
    <span>© <span data-year>2026</span> Servizi Informatici Srl · Concessionario Sistemi SpA · Marchi dei prodotti e illustrazioni della campagna: © Sistemi SpA</span>
    <span><a href="/privacy-policy/">Privacy policy</a> · <a href="/cookie-policy/">Cookie policy</a></span>
  </div>
</footer>'''

def crumbs_html(crumbs):
    if not crumbs:
        return ''
    lis = ''.join(f'<li><a href="{u}">{h(t)}</a></li>' if u else f'<li aria-current="page">{h(t)}</li>' for u, t in crumbs)
    return f'<nav class="crumbs" aria-label="Percorso"><ol><li><a href="/">Home</a></li>{lis}</ol></nav>'

def crumbs_ld(crumbs, path):
    items = [{"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"}]
    for i, (u, t) in enumerate(crumbs, start=2):
        items.append({"@type": "ListItem", "position": i, "name": t, "item": SITE + (u or path)})
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": items}

def faq_ld(faqs):
    return {"@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]}

def faq_html(faqs, title='Domande frequenti'):
    items = ''.join(f'<details><summary>{h(q)}</summary><p>{h(a)}</p></details>' for q, a in faqs)
    return f'''<section class="section" id="faq"><div class="wrap">
  <h2 class="h2 js-split" style="margin-bottom:28px">{title}</h2>
  <div class="faq reveal">{items}</div></div></section>'''

PAGES = []

def page(path, title, desc, body, crumbs=None, ld=None, robots='index,follow', current=None, og_type='website'):
    url = SITE + path
    lds = [ORG] if path == '/' else []
    if crumbs:
        lds.append(crumbs_ld(crumbs, path))
    if ld:
        lds.extend(ld)
    ld_html = ''.join(f'\n<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in lds)
    doc = f'''<!doctype html>
<html lang="it">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{h(title)}</title>
<meta name="description" content="{h(desc)}">
<meta name="robots" content="{robots}">
<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="it" href="{url}">
<link rel="alternate" hreflang="x-default" href="{url}">
<meta property="og:type" content="{og_type}">
<meta property="og:locale" content="it_IT">
<meta property="og:site_name" content="Sistemi Parma – Servizi Informatici Srl">
<meta property="og:title" content="{h(title)}">
<meta property="og:description" content="{h(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/assets/img/og-sistemi-parma.jpg">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#C20E1A">
<link rel="icon" href="/favicon.png" type="image/png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="preload" href="/assets/fonts/montserrat-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/css/site.css?v={CSSV}">{ld_html}
</head>
<body>
{header(current or path)}
<main id="contenuto">
{body}
</main>
{FOOTER}
<script src="/assets/js/site.js?v={JSV}" defer></script>
</body>
</html>
'''
    out = os.path.join(R, path.lstrip('/'))
    if path.endswith('/'):
        out = os.path.join(out, 'index.html')
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, 'w').write(doc)
    if robots.startswith('index'):
        PAGES.append(path)

def page_hero(crumbs, kicker, h1, lead, logo=None, logo_alt='', extra=''):
    lg = f'<img class="page-hero__logo" src="{logo}" alt="{h(logo_alt)}" width="640" height="200">' if logo else ''
    return f'''<section class="page-hero"><div class="wrap">
  {crumbs_html(crumbs)}
  <div class="hero-seq">
    {lg}
    <h1><span class="kicker">{kicker}</span>{h1}</h1>
    <p class="lead">{lead}</p>
    {extra}
  </div>
</div></section>'''

def slogan(img, alt):
    return f'<section class="slogan" aria-label="Campagna Sistemi"><div class="wrap"><img class="reveal" src="/assets/img/campagna/{img}.jpg" alt="{h(alt)}" width="1158" height="280" loading="lazy"></div></section>'

def cta_band(title, text, btn_href, btn_text, second=None):
    sec = f'<a class="btn btn--ghost" href="{second[0]}">{second[1]}</a>' if second else ''
    return f'''<section class="section section--dark"><div class="wrap split" style="align-items:center">
  <div><h2 class="h2 js-split">{title}</h2><p class="lead" style="margin-top:16px">{text}</p></div>
  <div class="btn-row reveal" style="justify-content:flex-start"><a class="btn btn--red" href="{btn_href}">{btn_text}</a>{sec}</div>
</div></section>'''

# ---------------------------------------------------------------- Prodotti
P = {
 'profis': dict(name='PROFIS', sito='https://www.sistemi.com/software-gestionali/profis/', schede=[('Profis', 'PROFIS-scheda.pdf'), ('Società e bilanci', 'PROFIS_Bilanci-scheda.pdf'), ('Gestione pratiche', 'PROFIS-pratiche-scheda.pdf'), ('Contratti di locazione', 'PROFIS_contratti-locazione-immobiliare_scheda.pdf'), ('Revisione legale', 'PROFIS-Revisione-scheda.pdf'), ('Analisi crisi d’impresa', 'PROFIS-Analisi-crisi-di-impresa-scheda.pdf'), ('Pianificazione fiscale', 'PROFIS-Pianificazione-fiscale-scheda.pdf'), ('Budget e business plan', 'PROFIS-Budget-e-Business-Plan-scheda.pdf'), ('Consulenza', 'PROFIS-Consulenza-scheda.pdf'), ('Enti del Terzo Settore', 'PROFIS_ETS-scheda.pdf'), ('Bonus ZES', 'PROFIS-Bonus-ZES_scheda.pdf'), ('Profis per le aziende', 'PROFIS_AZIENDE-scheda.pdf')], title='Profis', cat='professionisti', logo='profis', camp='profis',
   local='Software per commercialisti a Parma', claim='Il consulente dei commercialisti.',
   sub='Qualità, competenza e innovazione',
   intro='PROFIS è l’insieme di applicazioni Sistemi per gli studi professionali e le associazioni che offrono consulenza amministrativa e fiscale: contabilità, fiscale, bilanci e pratiche in un unico ambiente di lavoro.',
   modules=[('Contabilità','Contabilità ordinaria, semplificata e dei professionisti, con tutti gli adempimenti collegati.'),
            ('Beni ammortizzabili e in leasing','L’intero ciclo di vita del bene, dall’acquisizione alla cessione o all’eliminazione dal processo produttivo.'),
            ('Fiscale','Tutti i modelli dichiarativi in un unico ambiente di lavoro, comprese le comunicazioni per gli adempimenti antielusione.'),
            ('Società e Bilanci','Bilanci d’esercizio e periodici, in forma ordinaria e abbreviata, con la documentazione generata in automatico.'),
            ('Gruppi societari','Gestione IVA di gruppo, consolidato fiscale e bilancio consolidato.'),
            ('Gestione pratiche','Comunicazione Unica al Registro Imprese, deposito del bilancio, pratiche fiscali e contratti di locazione.')],
   also=['Gestione documentale','Pianificazione fiscale','Analisi finanziaria e benchmarking','Contratti di locazione','Privacy GDPR','PROFIS/pratiche e PROFIS/revisione'],
   who='Commercialisti, studi professionali e associazioni che offrono consulenza amministrativa e fiscale.',
   desc='Profis di Sistemi a Parma: contabilità, fiscale, bilanci e pratiche per commercialisti. Installazione, assistenza e corsi da Servizi Informatici, concessionario dal 1990.'),
 'studio': dict(name='STUDIO', sito='https://www.sistemi.com/software-gestionali/studio/', schede=[('Studio', 'STUDIO-scheda.pdf'), ('Studi legali', 'STUDIO_Studi-legali-scheda.pdf'), ('Processo Civile Telematico', 'STUDIO_PCT_scheda.pdf'), ('Antiriciclaggio', 'STUDIO_Antiriciclaggio-scheda.pdf')], title='Studio', cat='professionisti', logo='studio', camp='studio',
   local='Gestionale per studi professionali a Parma', claim='Studiato per il tuo lavoro.',
   sub='Organizzazione, condivisione, mobilità',
   intro='STUDIO è il gestionale Sistemi per commercialisti, consulenti del lavoro e avvocati: supporta la gestione amministrativa e operativa dello studio professionale, dai mandati al controllo di gestione.',
   modules=[('Amministrazione','Formalizza i servizi con la gestione dei mandati, definendo per ogni cliente condizioni economiche e amministrative.'),
            ('Organizzazione','Pianificazione ed erogazione complete dei servizi offerti dallo studio.'),
            ('Controllo di gestione','Report automatici su andamento e redditività dello studio, dei clienti e dei servizi.'),
            ('Area Legale','Per gli studi legali: Pratiche Giudiziarie, integrazione con PolisWeb, Redattore Atti Giudiziari e Mediazione Civile.')],
   also=['Fatturazione elettronica per i professionisti','Gestione documentale','Processo Civile Telematico','Antiriciclaggio','Documenti/Web'],
   who='Commercialisti, consulenti del lavoro, avvocati e CTU.',
   desc='Studio di Sistemi a Parma: mandati, parcellazione, pratiche, agende e controllo di gestione per commercialisti, consulenti del lavoro e avvocati.'),
 'job': dict(name='JOB', sito='https://www.sistemi.com/software-gestionali/job/job-paghe/', schede=[('Job per i consulenti del lavoro', 'JOB_CONSULENTI-scheda.pdf'), ('Job per le aziende', 'JOB_AZIENDE-scheda.pdf'), ('Gestione dei CCNL', 'JOB-Gestione-dei-CCNL_scheda.pdf'), ('Assistente normativo CCNL', 'JOB_Assistente-Normativo-CCNL-scheda.pdf'), ('Pratiche', 'JOB-Pratiche-scheda.pdf'), ('Analisi dei costi', 'JOB_AnalisiCosti-scheda.pdf'), ('Budget del personale', 'JOB_Budget-del-personale-scheda.pdf'), ('Planner: pianificazione dei processi', 'JOB-Planner_Pianificazione-processi-operativi_scheda.pdf')], title='Job', cat='professionisti', logo='job', camp='job',
   local='Software paghe e personale a Parma', claim='A lavoro per chi lavora.',
   sub='Sicurezza, semplicità, integrazione',
   intro='JOB è la soluzione Sistemi multiaziendale e multicontrattuale per studi professionali, imprese e associazioni che vogliono gestire l’amministrazione del personale in modo semplice ed efficiente.',
   modules=[('Organizzazione','Meno tempo sulle operazioni cicliche mensili o plurimensili, con l’aggiornamento automatico dei contratti.'),
            ('Amministrazione del Personale','Tutte le elaborazioni obbligatorie, dal Libro Unico del Lavoro all’Autoliquidazione.'),
            ('Controllo di Gestione','Elaborati per l’analisi dei costi del personale e la predisposizione del budget.'),
            ('Pratiche','Le pratiche che regolano il rapporto tra aziende, dipendenti ed enti.'),
            ('Fiscale','Modelli 730 e 770 in un unico ambiente di lavoro, con inserimento dati facilitato.'),
            ('Presenze','Applicazione in rete con cui il cliente dello studio inserisce le ore di presenza.'),
            ('DOCUMENTI/web','Pubblica online modelli fiscali, F24, parcelle e cedolini e avvisa il cliente.'),
            ('Risorse umane con PeopleLink','La gestione delle risorse umane, delle presenze e delle note spese è affidata a PeopleLink, la piattaforma HR cloud di Sistemi, che si sincronizza con JOB.'),
            ('Time','Rilevazione presenze per aziende pubbliche o private, con esportazione verso la procedura paghe.')],
   also=['JOB/Presenze','Gestione documentale integrata','Documenti/Web','Assistente normativo','Privacy GDPR'],
   who='Consulenti del lavoro, studi professionali, imprese e associazioni.',
   desc='Job di Sistemi a Parma: paghe, Libro Unico, 730 e 770, presenze online e cedolini pubblicati sul web. Per studi, imprese e associazioni.'),
 'spring': dict(name='SPRING', sito='https://www.sistemi.com/software-gestionali/spring/', schede=[('Spring', 'SPRING-scheda.pdf'), ('Gestione documentale', 'Gestione-documentale_scheda.pdf')], title='Spring', cat='aziende', logo='spring', camp=None,
   local='Gestionale per piccole aziende a Parma', claim='Partire bene, crescere meglio.',
   sub='Affidabilità, qualità, assistenza',
   intro='SPRING è il gestionale Sistemi pensato per le piccole aziende: unisce un’ampia completezza funzionale a tempi di implementazione rapidi.',
   modules=[('Contabilità ed IVA','Adempimenti contabili e fiscali, con schede contabili, quadrature giornaliere, bilanci di verifica ed elaborazioni IVA.'),
            ('Gestione vendite','Flusso documentale di vendita, documenti di trasporto e fatture, statistiche di vendita.'),
            ('Gestione acquisti','Documenti di trasporto e fatture d’acquisto, documenti per i resi ai fornitori.'),
            ('Gestione magazzino','Movimenti e giacenze, contabilità fiscale e valorizzazione del magazzino a fini fiscali e gestionali.'),
            ('Gestione cespiti','Dall’acquisto alla dismissione, con ammortamenti civilistici e fiscali, anche simulati.'),
            ('Dati fiscali','Liquidazione IVA, elenchi INTRASTAT, sostituti d’imposta e preparazione dei dati per gli adempimenti annuali.')],
   also=['Gestione documentale','Controllo di gestione e reporting','Gestionali verticali per settore'],
   who='Piccole e micro imprese che cercano un sistema informativo completo e rapido da avviare.',
   desc='Spring di Sistemi a Parma: contabilità, vendite, acquisti, magazzino e cespiti per piccole e micro imprese. Installazione e assistenza da Servizi Informatici.'),
 'esolver': dict(name='eSOLVER', sito='https://www.sistemi.com/software-gestionali/esolver/', schede=[('eSolver', 'eSOLVER-scheda.pdf'), ('eSolver GRP', 'eSOLVER-GRP-scheda.pdf'), ('Produzione manifatturiera', 'ESOLVER-Produzione-manifatturiera_scheda.pdf'), ('CRM', 'eSOLVER-CRM-scheda.pdf'), ('Gestione documentale', 'Gestione-documentale_scheda.pdf')], title='eSolver', cat='aziende', logo='esolver', camp='esolver',
   local='ERP per aziende a Parma', claim='Tutti i vantaggi del fare sistema.',
   sub='Processi, gestione, controllo',
   intro='eSOLVER è il gestionale ERP Sistemi per imprese e associazioni di diversi settori: gestisce le attività amministrative, controlla la gestione e automatizza i processi aziendali.',
   modules=[('Area amministrativa','Piano dei conti multilivello, partite aperte su qualsiasi conto, divisioni aziendali e centri di imputazione, movimenti provvisori, cespiti e Intrastat.'),
            ('Ciclo attivo','Offerte ai clienti e contratti quadro, condizioni commerciali integrate, monitoraggio dell’evasione degli ordini.'),
            ('Ciclo passivo','Richieste di preventivo, ordini con più livelli di autorizzazione, ricevimenti con collaudo e movimenti di magazzino automatici.'),
            ('Logistica','Tracciabilità per matricola o lotto, scorte minime e lotti di riordino, pianificazione degli approvvigionamenti con MRP.'),
            ('Contabilità analitica','Sistema configurabile per misurare gli obiettivi, con Piano delle Voci e Piano dei Centri di Analisi.'),
            ('Produzione servizi','Contratti clienti per canoni e prestazioni a consuntivo, noleggi, manutenzioni programmate e canoni a consumo.')],
   also=['Controllo di gestione e reporting','Gestionali verticali per settore','Business intelligence'],
   who='Imprese e associazioni che vogliono un ERP per amministrazione, logistica e controllo.',
   desc='eSolver di Sistemi a Parma: ERP per amministrazione, ciclo attivo e passivo, logistica con MRP, contabilità analitica e produzione servizi.'),
 'profis-az': dict(name='PROFIS AZ', sito='https://www.sistemi.com/software-gestionali/profis/profis-az/', schede=[('Profis AZ per l’azienda', 'PROFIS-AZ-aziende-scheda.pdf'), ('Profis AZ per il professionista', 'PROFIS-Az_professionisti_scheda.pdf')], title='Profis AZ', cat='aziende', logo='profis-az', camp=None,
   local='Gestionale azienda e commercialista a Parma', claim='L’azienda e il commercialista, sugli stessi dati.',
   sub='Gestione coadiuvata dal commercialista',
   intro='PROFIS AZ è la soluzione pensata per il commercialista che offre consulenza gestionale e fiscale, lasciando l’azienda autonoma nella gestione quotidiana.',
   modules=[('Per l’azienda: fatturazione','Emissione dei documenti di vendita e delle fatture.'),
            ('Per l’azienda: acquisti','Registrazione degli acquisti.'),
            ('Per l’azienda: incassi e pagamenti','Gestione di incassi e pagamenti.'),
            ('Per l’azienda: magazzino','Movimenti e giacenze di magazzino.'),
            ('Per lo studio: adempimenti','Adempimenti periodici, dichiarazioni e bilanci.'),
            ('Per lo studio: controllo di gestione','Analisi e controllo di gestione per il cliente.')],
   also=[], who='Piccole imprese seguite da un commercialista che usa Profis.',
   desc='Profis AZ di Sistemi a Parma: l’azienda gestisce fatture, acquisti e magazzino, il commercialista adempimenti, dichiarazioni e bilanci.'),
 'peoplelink': dict(name='PEOPLELINK', sito='https://www.sistemi.com/peoplelink/', schede=[('PeopleLink','Peoplelink-Sistemi_scheda.pdf')],
   title='PeopleLink', cat='aziende', logo='peoplelink', camp='peoplelink',
   local='Software HR e rilevazione presenze a Parma', claim='Le persone, i turni e le spese in un posto solo.',
   breve='La piattaforma HR cloud e mobile di Sistemi: presenze e turni, ferie, timesheet e commesse, note spese e controllo accessi. Si integra con Job.',
   sub='Risorse umane, presenze, commesse, note spese',
   intro='PEOPLELINK è la piattaforma HR cloud e mobile di Sistemi: gestisce i processi delle risorse umane, la rilevazione delle presenze, la pianificazione delle ferie, i timesheet e le commesse, le note spese. Si usa da browser o da app, ed è pensata per aziende di tutte le dimensioni.',
   cloud_q=('PeopleLink si installa in azienda?', 'No: PeopleLink è una piattaforma cloud e mobile. Si usa dal browser o dall’app, senza installazioni sui PC e senza server in sede.'),
   avvio='attivazione della piattaforma cloud, configurazione di turni, causali e profili, importazione delle anagrafiche',
   modules=[('Timbratura e rilevazione presenze','Timbrature con badge, tag NFC, PC, smartphone e geolocalizzazione; turni, smartworking e hybrid work, straordinari, trasferte, giustificativi e piani ferie, fino all’invio dei dati per il cedolino.'),
            ('Il cartellino, in autonomia','Il dipendente vede il proprio cartellino, giustifica le assenze, chiede ferie o extra orari e consulta i totalizzatori; il responsabile gestisce le richieste, organizza i turni e controlla presenti e assenti.'),
            ('Commesse e attività','Rapportini di lavoro, commesse e progetti: compilazione e validazione del timesheet da browser o da app, anagrafica clienti, costi orari e spese accessorie, attività programmate a calendario.'),
            ('Gestione risorse umane','Anagrafica avanzata e storicizzata, documenti e attestati, competenze e schede di valutazione, corsi e gap formativi, sondaggi aziendali, aspetti retributivi, asset e DPI, scadenziario e promemoria.'),
            ('Rendicontazione e note spese','Spese generiche, rimborsi chilometrici, ospiti, valuta estera, allegati e anticipi in contanti, con associazione a commessa e centro di costo e l’intero flusso autorizzativo fino al pagamento.'),
            ('Controllo accessi e varchi','Le regole di ingresso sono associate alla persona e al suo badge: zone ad accesso limitato, fasce orarie, profili per dipendenti e visitatori, esportazione dei passaggi.'),
            ('Business Intelligence integrata','Oltre 15 tipi di grafici, raggruppamenti per periodo o anagrafica e filtri personalizzati su organizzazione, presenze, dati amministrativi e timesheet.'),
            ('Integrazione con JOB','I dati dei rapporti di lavoro e le anagrafiche di aziende e dipendenti arrivano in automatico da JOB e restano sincronizzati.')],
   also=[], who='Aziende di tutte le dimensioni che vogliono gestire presenze, risorse umane, commesse e note spese in un unico ambiente, da web e da app.',
   desc='PeopleLink di Sistemi a Parma: piattaforma HR cloud e mobile per presenze, ferie, timesheet e commesse, note spese e controllo accessi. Si integra con Job.'),
 'quadra': dict(name='QUADRA', sito='https://www.sistemi.com/software-gestionali/quadra/', schede=[('Quadra', 'QUADRA-scheda.pdf')], title='Quadra', cat='aziende', logo='quadra', camp=None,
   local='Software di fatturazione elettronica a Parma', claim='Fatturazione web, semplice da avviare.',
   sub='Fatturazione web',
   intro='QUADRA è il software Sistemi per la fatturazione web: semplice e veloce da avviare e da usare, anche per i forfettari.',
   modules=[('Fattura elettronica','Emissione e ricezione delle fatture elettroniche, anche per i forfettari.'),
            ('Documenti di vendita','Preventivi, ordini e documenti di vendita.'),
            ('Incassi e pagamenti','Scadenze, incassi e pagamenti sotto controllo.'),
            ('Report e analisi','Report e analisi sull’andamento delle vendite.')],
   also=[], who='Ditte individuali, professionisti e piccole attività, anche in regime forfettario.',
   desc='Quadra di Sistemi a Parma: fatturazione elettronica web semplice, anche per i forfettari. Attivazione e assistenza da Servizi Informatici.'),
}

def product_card(key, cls='card reveal'):
    p = P[key]
    marchio = (f'<img class="card__logo" src="/assets/img/prodotti/{p["logo"]}.jpg" alt="{p["title"]} – Sistemi" width="640" height="200" loading="lazy">'
               if p.get('logo') else f'<span class="card__word">{h(p["name"])}</span>')
    return f'''<a class="{cls}" href="/{p["cat"]}/{key}/">
  {marchio}
  <span class="card__tag">{h(p["sub"])}</span>
  <p>{h(p.get("breve") or (p["intro"].split(":")[0] + "." if len(p["intro"]) > 200 else p["intro"]))}</p>
  <span class="link-arrow">Scopri {p["title"]} →</span></a>'''

def product_page(key):
    p = P[key]
    catname = 'Professionisti' if p['cat'] == 'professionisti' else 'Aziende'
    path = f'/{p["cat"]}/{key}/'
    crumbs = [(f'/{p["cat"]}/', catname), (None, p['title'])]
    mods = ''.join(f'<div class="reveal"><h3 style="font-size:20px;margin-bottom:8px">{h(t)}</h3><p>{h(d)}</p></div>' for t, d in p['modules'])
    also = ''
    if p['also']:
        also = '<div class="note reveal" style="margin-top:36px"><b style="color:#000">Inoltre:</b> ' + ' · '.join(h(a) for a in p['also']) + '</div>'
    camp = ''
    if p['camp'] and p.get('logo'):
        camp = f'<div class="reveal" style="margin-top:40px"><span class="campaign"><img src="/assets/img/campagna/{p["camp"]}.png" alt="Campagna Sistemi 2026 dedicata a {p["title"]}" width="349" height="120" loading="lazy"></span></div>'
    cloud_q = p.get('cloud_q') or (f'Posso usare {p["title"]} in cloud?', f'Sì: con Sistemi in Rete i software Sistemi si usano dal web, ospitati nelle Service Farm Sistemi, senza server in ufficio. Ti aiutiamo a scegliere tra installazione in locale e cloud.')
    faqs = [
        (f'Chi installa e assiste {p["title"]} a Parma?', f'Servizi Informatici Srl (Sistemi Parma), concessionario certificato Sistemi SpA dal 1990 per le province di Parma, Piacenza e Reggio Emilia. Installiamo, configuriamo e seguiamo {p["title"]} con personale certificato Sistemi.'),
        (f'A chi è adatto {p["title"]}?', p['who']),
        cloud_q,
        ('Come chiedo assistenza?', 'Apri un ticket dal menu del tuo software Sistemi (così puoi allegare log e diagnostica) oppure chiamaci allo 0521 252824. Per l’accesso remoto usiamo TeamViewer o AnyDesk.'),
        (f'Posso vedere {p["title"]} prima di sceglierlo?', 'Sì, scrivici dal modulo contatti: organizziamo una demo e ti aiutiamo a capire quale soluzione fa per te.'),
    ]
    if key in ('profis', 'studio'):
        faqs.insert(3, ('Fate corsi di formazione?', 'Sì, organizziamo corsi pratici in aula nella nostra sede di Via Sicuri 42/a a Parma, sui tuoi dati, con un massimo di 6 partecipanti. Trovi il calendario nella pagina Corsi.'))
    DL = 'https://www.sistemi.com/downloads/'
    schede = ''.join(
        f'<li><a class="pdf-link" href="{DL}{f}" rel="noopener" target="_blank">{icon("file","icon pdf-ico")}'
        f'<span>{h(t)}</span><small>PDF · sistemi.com</small></a></li>' for t, f in p['schede'])
    scheda1 = p['schede'][0][1]
    body = page_hero(crumbs, h(p['local']), h(p['claim']), h(p['intro']),
                     logo=(f'/assets/img/prodotti/{p["logo"]}.jpg' if p.get('logo')
                           else (f'/assets/img/campagna/{p["camp"]}.png' if p.get('camp') else None)),
                     logo_alt=(f'{p["title"]} – Sistemi' if p.get('logo') else f'Campagna Sistemi dedicata a {p["title"]}'),
                     extra=f'<div class="btn-row" style="margin-top:32px"><a class="btn btn--red" href="/contatti/?prodotto={p["title"].replace(" ","%20")}#modulo">Chiedi una demo di {p["title"]}</a><a class="btn btn--line" href="{DL}{scheda1}" rel="noopener" target="_blank">Scheda PDF</a><a class="btn btn--line" href="#moduli">Cosa fa</a></div>')
    body += f'''
<section class="section" id="moduli"><div class="wrap">
  <div class="head-row"><h2 class="h2 js-split">{h(p["sub"])}</h2><p>{h(p["who"])}</p></div>
  <div class="grid grid--3" style="gap:36px 40px">{mods}</div>
  {also}{camp}
</div></section>
<section class="section section--soft" id="schede"><div class="wrap">
  <div class="head-row"><div><span class="kicker">Documentazione</span><h2 class="h2 js-split">Schede prodotto</h2></div><p>Le schede ufficiali di Sistemi SpA, in PDF. Si aprono sul sito sistemi.com.</p></div>
  <ul class="pdf-list reveal">{schede}</ul>
</div></section>
<section class="section section--soft"><div class="wrap split">
  <div><span class="kicker">Come lavoriamo</span><h2 class="h2 js-split">Dalla scelta all’assistenza, a Parma</h2></div>
  <ol class="list-check reveal" style="font-size:17px">
    <li><b>Analisi</b>: capiamo come lavori e ti mostriamo {p["title"]} in una demo.</li>
    <li><b>Avvio</b>: {p.get('avvio', 'installazione in locale o in cloud con Sistemi in Rete, configurazione e recupero dati')}.</li>
    <li><b>Formazione</b>: affiancamento e corsi in aula con docenti certificati Sistemi.</li>
    <li><b>Assistenza</b>: ticket dal software, telefono e accesso remoto.</li>
  </ol>
</div></section>
{faq_html(faqs)}
{cta_band(f"Vuoi saperne di più su {p['title']}?", "Scrivici: ti rispondiamo noi e organizziamo una demo. Le schede tecniche complete sono sul sito di Sistemi.", f"/contatti/?prodotto={p['title'].replace(' ','%20')}#modulo", "Contattaci", (p['sito'], f"{p['title']} su sistemi.com ↗"))}'''
    ld = [faq_ld(faqs), {"@context": "https://schema.org", "@type": "SoftwareApplication", "name": p['title'],
          "applicationCategory": "BusinessApplication", "operatingSystem": "Windows, Web",
          "description": p['intro'], "brand": {"@type": "Brand", "name": "Sistemi"},
          "publisher": {"@type": "Organization", "name": "Sistemi SpA", "url": "https://www.sistemi.com/"},
          "provider": {"@id": SITE + "/#azienda"}, "url": SITE + path, "sameAs": p['sito']}]
    page(path, f'{p["title"]} – {p["local"]} | Sistemi Parma', p['desc'], body, crumbs, ld)

# ---------------------------------------------------------------- Corsi
COURSES = {
 'contabilita-cespiti': dict(title='Contabilità e Cespiti Base', prod='Profis', ore='4 mezze giornate · 12 ore',
   intro='Un percorso introduttivo alla contabilità e alla gestione dei cespiti in Profis, con particolare attenzione all’impostazione contabile e IVA e agli aspetti specifici della contabilità semplificata, ordinaria e dei professionisti. Si parte dai concetti base della ragioneria e si applicano le regole standard in Profis, sfruttando gli automatismi della procedura.',
   per=['neoassunti negli studi professionali','chi ha iniziato a usare Profis senza una formazione adeguata','chi usa Profis da tempo e vuole ripassare i concetti di base aggiornati di recente'],
   prog=[('Servizi Contabili (Profis SQL)',['Gestione anagrafica e tabelle','Avviamento della ditta','Caricamento registrazioni e modelli di registrazione','Gestione flussi di fatture elettroniche attive e passive','Registrazione dei corrispettivi (import dal cassetto fiscale)','Ciclo di lavoro IVA','Contabilità di impresa ordinaria e semplificata','Contabilità dei professionisti ordinaria e semplificata','Integrazioni e gestioni complementari','Elaborazioni per dichiarazioni fiscali','Gestione F24']),
         ('Cespiti',['Fasi di avviamento','Caricamento registrazioni con integrazione cespiti','Caricamento movimenti dei cespiti','Calcolo degli ammortamenti e contabilizzazione da rettifiche contabili','Stampa del registro dei beni ammortizzabili','Elaborazioni per dichiarazioni fiscali'])]),
 'studio-4': dict(title='Studio 4 – Amministrazione e organizzazione dello studio', short='Studio 4', prod='Studio', ore='4 mezze giornate · 12 ore',
   intro='Il corso per organizzare lo studio professionale con Studio 4: si imparano le regole standard della procedura sfruttandone gli automatismi, per lavorare in modo più rapido e ordinato. È il primo passo di un percorso di crescita per chi usa Profis.',
   per=['chi ha iniziato a usare Studio senza una formazione adeguata','chi vuole migliorare la gestione dello studio','chi sta usando Studio al di sotto delle sue reali potenzialità'],
   prog=[('Programma',['Definizione del Catalogo Servizi','Mandati professionali: stampa, firma e scansione del mandato','Rilevazione delle prestazioni extra mandato','Addebiti','Avvisi di parcella','Parcellazione automatica','Piani attività','Gestione delle pratiche','Agende','Archiviazione della posta elettronica','Archiviazione documentale','Analisi'])]),
 'pratiche-locazioni': dict(title='Profis Pratiche e Contratti di Locazione', prod='Profis', ore='2 mezze giornate · 6 ore',
   intro='Un corso pratico su Profis/Pratiche e sui contratti di locazione: il docente svolge gli esempi e i partecipanti li rifanno sui propri dati. Lavorare dal vivo permette di portare a casa risultati concreti, non solo teoria.',
   per=['chi gestisce le pratiche per il Registro Imprese e l’Agenzia delle Entrate','chi registra e gestisce contratti di locazione in Profis'],
   prog=[('Profis / Pratiche',['Gestione tabelle','Attivazione ditta Profis/Pratiche','Gestione Comunicazione Unica','Gestione pratiche Agenzia delle Entrate e Registro Imprese','Scarico ricevute Agenzia delle Entrate']),
         ('Contratti di Locazione',['Gestione tabelle','Creazione del contratto di locazione','Registrazione','Annualità successiva','Altri eventi','Scadenziario','Integrazione fiscale'])]),
}

PRIVACY_CHECK = '<label class="check full"><input type="checkbox" name="privacy" value="accettata" required> <span>Ho letto l’<a href="/privacy-policy/" target="_blank" rel="noopener">informativa privacy</a> e acconsento al trattamento dei dati per ricevere una risposta.</span></label>'

def contact_form(prodotto_default='', pagina='contatti'):
    opts = ['Informazioni generali', 'Profis', 'Studio', 'Job', 'Spring', 'eSolver', 'Profis AZ', 'Quadra', 'Gestionali verticali', 'Sistemi in Rete (cloud)', 'Whistleblowing', 'Siti web', '100% Profis', 'Assistenza']
    o = ''.join(f'<option value="{h(x)}"{" selected" if x == prodotto_default else ""}>{h(x)}</option>' for x in opts)
    return f'''<form class="form" id="modulo" name="contatti" method="POST" action="/grazie/" data-netlify="true" netlify-honeypot="bot-field">
  <input type="hidden" name="form-name" value="contatti">
  <input type="hidden" name="lingua" value="it">
  <input type="hidden" name="pagina" value="{pagina}">
  <p class="hp"><label>Non compilare: <input name="bot-field" tabindex="-1" autocomplete="off"></label></p>
  <label class="field">Nome<input type="text" name="nome" autocomplete="given-name" required></label>
  <label class="field">Cognome<input type="text" name="cognome" autocomplete="family-name" required></label>
  <label class="field">Email<input type="email" name="email" autocomplete="email" required></label>
  <label class="field">Telefono (facoltativo)<input type="tel" name="telefono" autocomplete="tel"></label>
  <label class="field">Studio o azienda (facoltativo)<input type="text" name="azienda" autocomplete="organization"></label>
  <label class="field">Argomento<select name="prodotto">{o}</select></label>
  <label class="field full">Messaggio<textarea name="messaggio" rows="5" required></textarea></label>
  {PRIVACY_CHECK}
  <div class="full"><button class="btn btn--red" type="submit">Invia la richiesta</button></div>
</form>'''

def course_form(course_title):
    opts = [c.get('short', c['title']) for c in COURSES.values()]
    o = ''.join(f'<option value="{h(x)}"{" selected" if x == course_title else ""}>{h(x)}</option>' for x in opts)
    return f'''<form class="form" id="iscrizione" name="iscrizione-corso" method="POST" action="/grazie-iscrizione/" data-netlify="true" netlify-honeypot="bot-field">
  <input type="hidden" name="form-name" value="iscrizione-corso">
  <input type="hidden" name="lingua" value="it">
  <p class="hp"><label>Non compilare: <input name="bot-field" tabindex="-1" autocomplete="off"></label></p>
  <label class="field full">Corso<select name="corso" required>{o}</select></label>
  <p class="legend">Partecipante</p>
  <label class="field">Nome<input type="text" name="nome" autocomplete="given-name" required></label>
  <label class="field">Cognome<input type="text" name="cognome" autocomplete="family-name" required></label>
  <label class="field">Email<input type="email" name="email" autocomplete="email" required></label>
  <label class="field">Telefono<input type="tel" name="telefono" autocomplete="tel" required></label>
  <label class="field">Numero di partecipanti<input type="number" name="partecipanti" min="1" max="6" value="1" required></label>
  <label class="field">Lavori in cloud?<select name="cloud"><option>No</option><option>Sì, porto il mio portatile</option></select></label>
  <p class="legend">Dati per la fattura</p>
  <label class="field full">Studio o ragione sociale<input type="text" name="ragione_sociale" autocomplete="organization" required></label>
  <label class="field">Partita IVA<input type="text" name="partita_iva" inputmode="numeric" required></label>
  <label class="field">Codice destinatario SDI o PEC<input type="text" name="codice_sdi" required></label>
  <label class="field full">Note (nomi degli altri partecipanti, date preferite…)<textarea name="note" rows="3"></textarea></label>
  {PRIVACY_CHECK}
  <p class="full note" style="margin:0">L’iscrizione è una richiesta: ti confermiamo noi date e quota di partecipazione e la fattura arriva a parte.</p>
  <div class="full"><button class="btn btn--red" type="submit">Invia l’iscrizione</button></div>
</form>'''

def course_page(key):
    c = COURSES[key]
    path = f'/corsi/{key}/'
    crumbs = [('/corsi/', 'Corsi ed eventi'), (None, c.get('short', c['title']))]
    prog = ''.join(f'<div class="reveal"><h3 style="font-size:20px;margin-bottom:14px">{h(t)}</h3><ul class="list-check">{"".join(f"<li>{h(i)}</li>" for i in items)}</ul></div>' for t, items in c['prog'])
    per = ''.join(f'<li>{h(x)}</li>' for x in c['per'])
    faqs = [('Dove si svolge il corso?', 'Nell’aula corsi della nostra sede in Via Sicuri 42/a a Parma. Ogni partecipante lavora su una postazione dell’aula multimediale; chi lavora in cloud è invitato a portare il proprio portatile.'),
            ('Quante persone partecipano?', 'Al massimo 6 partecipanti per edizione, così il docente può seguire ognuno.'),
            ('Chi sono i docenti?', 'Personale certificato costantemente con i percorsi formativi ufficiali Sistemi SpA, requisito obbligatorio per fare assistenza e formazione ai clienti.'),
            ('Come funziona l’iscrizione?', 'Compili il modulo di iscrizione con i dati del partecipante e quelli per la fattura: ti confermiamo noi date e quota di partecipazione e la fattura arriva a parte. Per più partecipanti dello stesso studio è previsto uno sconto.')]
    body = page_hero(crumbs, f'Corso in aula a Parma · {h(c["prod"])}', h(c['title']), h(c['intro']),
                     extra=f'<p style="margin-top:22px;font-weight:600;color:#000">{h(c["ore"])} · massimo 6 partecipanti · esercitazioni e coffee break</p><div class="btn-row" style="margin-top:24px"><a class="btn btn--red" href="#iscrizione">Iscriviti</a><a class="btn btn--line" href="#programma">Programma</a></div>')
    body += f'''
<section class="section" id="programma"><div class="wrap">
  <div class="split" style="margin-bottom:56px">
    <div><h2 class="h2 js-split">A chi è rivolto</h2></div>
    <ul class="list-check reveal">{per}</ul>
  </div>
  <h2 class="h2 js-split" style="margin-bottom:32px">Programma</h2>
  <div class="grid grid--2" style="gap:40px">{prog}</div>
  <div class="grid grid--3" style="margin-top:56px">
    <div class="card card--soft reveal">{icon("calendar")}<h3>Durata</h3><p>{h(c["ore"])}. Prossima edizione: [DATA DA DEFINIRE].</p></div>
    <div class="card card--soft reveal reveal-d1">{icon("users")}<h3>Metodo</h3><p>Corso pratico e intensivo: gli esempi del docente si rifanno sui propri dati.</p></div>
    <div class="card card--soft reveal reveal-d2">{icon("check")}<h3>Docenti certificati</h3><p>Formazione continua sui percorsi ufficiali Sistemi SpA.</p></div>
  </div>
</div></section>
<section class="section section--soft" id="iscrizione-box"><div class="wrap">
  <div class="contact-box" style="background:#fff">
    <div><span class="kicker">Iscrizione</span><h2 class="h2">Iscriviti al corso</h2><p class="lead" style="margin-top:14px">Compila il modulo: ti ricontattiamo per confermare date e quota.</p>
    <ul class="contact-list"><li><a href="{TEL_HREF}">{TEL}</a></li><li><a href="mailto:{MAIL}">{MAIL}</a></li></ul></div>
    {course_form(c.get("short", c["title"]))}
  </div>
</div></section>
{faq_html(faqs)}'''
    ld = [faq_ld(faqs), {"@context": "https://schema.org", "@type": "Course", "name": c['title'], "description": c['intro'],
          "inLanguage": "it", "provider": {"@id": SITE + "/#azienda", "@type": "Organization", "name": "Servizi Informatici Srl"},
          "hasCourseInstance": {"@type": "CourseInstance", "courseMode": "Onsite",
            "location": {"@type": "Place", "name": "Aula corsi Servizi Informatici", "address": ORG['address']}}}]
    page(path, f'Corso {c.get("short", c["title"])} in aula a Parma | Sistemi Parma', f'Corso pratico {c.get("short", c["title"])} ({c["ore"]}) a Parma, Via Sicuri 42/a: massimo 6 partecipanti, docenti certificati Sistemi. Iscriviti online.', body, crumbs, ld)

# ---------------------------------------------------------------- Pillole
# (slug, titolo, data, id del video YouTube del canale aziendale oppure None, tag)
# Canale: https://www.youtube.com/@serviziinformaticisrl-parm8248
# Un video locale in assets/video/<slug>.mp4 ha la precedenza sul video YouTube.
POSTS = [
 ('la-delega-unica','La Delega Unica','2025-12-23',None,'Delega Unica'),
 ('i-documenti-della-conservazione','I Documenti della Conservazione','2023-12-14',None,'Conservazione digitale, Profis'),
 ('notifiche-web-sportello-conservazione','Notifiche Web – Sportello Conservazione','2023-12-11',None,'Sportello Conservazione'),
 ('download-massivo-fatture-agenzia-delle-entrate','Download massivo fatture Agenzia delle Entrate','2023-03-29',None,'Fatture elettroniche'),
 ('sportello-documenti-condivisi-mobile','Sportello Documenti Condivisi MOBILE','2022-04-22',None,'Sportello'),
 ('conservazione-digitale-il-controllo-del-cruscotto','Conservazione digitale: il controllo del cruscotto','2022-01-18','WvZDsLNwcjU','Conservazione digitale'),
 ('esolver-come-aggiornare-i-codici-iva','eSolver: come aggiornare i codici IVA','2021-09-24','WWMsv2aYCnc','eSolver, IVA'),
 ('contabilizzazione-automatica-fatture-e-corrispettivi','Contabilizzazione automatica fatture e corrispettivi','2021-09-23','FkSBprllt68','Profis, Fatture elettroniche'),
 ('gestione-documenti-integrativi','Gestione documenti integrativi','2021-09-13','4ayJ9CkR3SI','Profis'),
 ('i-contratti-di-locazione','I Contratti di Locazione','2020-11-24','gASvLNzW5H0','Contratti di locazione'),
 ('la-riconciliazione-fatture','La Riconciliazione fatture','2020-11-10','IkwlLcdsrkw','Fatture elettroniche'),
 ('registrazione-automatica-cassa-banca-paghe','Registrazione automatica cassa, banca, paghe','2020-10-27','Fdj6J7a5Pmk','Contabilità'),
 ('analisi-crisi-di-impresa','Analisi crisi di Impresa','2020-10-13','u6HswNBZgfQ','Crisi d’impresa'),
]
PROMO_YT = 'fFs1ofhfDec'  # Servizi Informatici Video Promo Mercato Studio
MESI = ['gennaio','febbraio','marzo','aprile','maggio','giugno','luglio','agosto','settembre','ottobre','novembre','dicembre']
def itdate(d):
    y, m, g = d.split('-'); return f'{int(g)} {MESI[int(m)-1]} {y}'
THUMBS = ['thumb--red', '', 'thumb--grey']

def video_src(slug, yt):
    """mp4 locale se presente, altrimenti il video YouTube, altrimenti nessun video."""
    if os.path.exists(os.path.join(R, 'assets/video', slug + '.mp4')):
        return '/assets/video/' + slug + '.mp4'
    return 'https://www.youtube.com/watch?v=' + yt if yt else None

def post_card(i, slug, title, date, yt=None):
    has = video_src(slug, yt)
    badge = f'<span class="thumb__play">{PLAY}</span>' if has else '<span class="thumb__soon">in arrivo</span>'
    meta = 'video' if has else 'video in arrivo'
    return f'''<a class="post-card reveal" href="/pillole/{slug}/">
  <div class="thumb {THUMBS[i % 3]}"><span class="thumb__t">{h(title)}</span>{badge}</div>
  <span class="post-card__meta"><time datetime="{date}">{itdate(date)}</time> · {meta}</span>
  <h3>{h(title)}</h3></a>'''

def post_page(i, slug, title, date, yt, tags):
    path = f'/pillole/{slug}/'
    crumbs = [('/pillole/', 'Le Pillole'), (None, title)]
    src = video_src(slug, yt)
    if src:
        video = f'<button type="button" class="video-btn" data-video="{src}" data-title="{h(title)}" aria-label="Riproduci il video: {h(title)}"><div class="thumb {THUMBS[i % 3]}"><span class="thumb__t">{h(title)}</span><span class="thumb__play">{PLAY}</span></div></button>'
        if yt and not src.startswith('/'):
            video += f'<p class="video-note">Il video si apre qui nella pagina e viene caricato da YouTube solo quando premi play. Puoi anche <a href="https://www.youtube.com/watch?v={yt}" rel="noopener" target="_blank">guardarlo su YouTube</a>.</p>'
    else:
        video = '<div class="video-missing"><p><b>Video in arrivo.</b><br>Stiamo trasferendo le pillole sul nuovo sito. Nel frattempo <a href="/contatti/?prodotto=Assistenza#modulo">scrivici</a> per riceverlo.</p></div>'
    extra = ''
    if slug == 'notifiche-web-sportello-conservazione':
        extra = '<p>Collegato: <a href="/pillole/conservazione-digitale-il-controllo-del-cruscotto/">il controllo del cruscotto dello Sportello Conservazione</a>.</p>'
    others = [p for p in POSTS if p[0] != slug and video_src(p[0], p[3])][:3]
    cards = ''.join(post_card(j, s, t, d, y) for j, (s, t, d, y, _tg) in enumerate(others))
    body = f'''<section class="page-hero"><div class="wrap">{crumbs_html(crumbs)}
  <div class="hero-seq"><h1><span class="kicker">Le Pillole · videotutorial</span>{h(title)}</h1>
  <p class="lead"><time datetime="{date}">{itdate(date)}</time> · {h(tags)}</p></div></div></section>
<section class="section"><div class="wrap"><div class="video-box reveal">{video}</div>
  <div class="prose" style="margin-top:28px">{extra}<p>Le Pillole sono brevi video in cui il nostro team mostra come usare al meglio una funzione dei software Sistemi. Hai dubbi? <a href="/contatti/?prodotto=Assistenza#modulo">Scrivici</a> o apri un ticket dal tuo software.</p></div>
</div></section>
<section class="section section--soft"><div class="wrap"><h2 class="h2" style="margin-bottom:32px">Altre pillole</h2><div class="grid grid--3">{cards}</div></div></section>'''
    ld = [{"@context": "https://schema.org", "@type": "BlogPosting", "headline": title, "datePublished": date,
           "author": {"@type": "Organization", "name": "Servizi Informatici Srl"}, "publisher": {"@id": SITE + "/#azienda"},
           "mainEntityOfPage": SITE + path, "inLanguage": "it", "keywords": tags}]
    if yt:
        ld.append({"@context": "https://schema.org", "@type": "VideoObject", "name": title,
                   "description": f'Videotutorial de Le Pillole di Sistemi Parma: {title.lower()}.',
                   "uploadDate": date, "thumbnailUrl": f'https://i.ytimg.com/vi/{yt}/hqdefault.jpg',
                   "embedUrl": f'https://www.youtube-nocookie.com/embed/{yt}',
                   "contentUrl": f'https://www.youtube.com/watch?v={yt}',
                   "publisher": {"@id": SITE + "/#azienda"}, "inLanguage": "it"})
    page(path, f'{title} – Le Pillole | Sistemi Parma', f'{title}: videotutorial de Le Pillole di Sistemi Parma sui software Sistemi ({tags}).', body, crumbs, ld, og_type='article')

# ---------------------------------------------------------------- Pagine
def build():
    for k in P: product_page(k)
    for k in COURSES: course_page(k)
    for i, p in enumerate(POSTS): post_page(i, *p)
    import pages_main
    pages_main.build(globals())
    # sitemap
    urls = ''.join(f'<url><loc>{SITE}{p}</loc><lastmod>{TODAY}</lastmod><xhtml:link rel="alternate" hreflang="it" href="{SITE}{p}"/></url>\n' for p in sorted(set(PAGES)))
    open(os.path.join(R, 'sitemap.xml'), 'w').write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n{urls}</urlset>\n')
    print('pagine:', len(PAGES))

if __name__ == '__main__':
    import sys; sys.path.insert(0, os.path.dirname(__file__))
    build()
