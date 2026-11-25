"""Pagine principali (home, categorie, servizi, corsi, contatti, legali)."""

def build(g):
    h = g['h']; page = g['page']; page_hero = g['page_hero']; P = g['P']; icon = g['icon']
    slogan = g['slogan']; cta_band = g['cta_band']; faq_html = g['faq_html']; faq_ld = g['faq_ld']
    icon_tile = g['icon_tile']
    product_card = g['product_card']; post_card = g['post_card']; POSTS = g['POSTS']; COURSES = g['COURSES']
    video_src = g['video_src']; PROMO_YT = g['PROMO_YT']; THUMBS = g['THUMBS']
    contact_form = g['contact_form']; TEL = g['TEL']; TEL_HREF = g['TEL_HREF']; MAIL = g['MAIL']; MAPS = g['MAPS']; ADDR = g['ADDR']
    SITE = g['SITE']; PLAY = g['PLAY']

    # ------------------------------------------------------------ HOME
    home_faqs = [
        ('Dove si trova Sistemi Parma?', 'Siamo Servizi Informatici Srl, in Via Giulio e Giacinto Sicuri 42/a, 43124 Parma. Seguiamo clienti nelle province di Parma, Piacenza e Reggio Emilia.'),
        ('Quali software trattate?', 'Siamo concessionario certificato Sistemi SpA dal 1990: Profis, Studio e Job per gli studi professionali; Spring, eSolver, Profis AZ e Quadra per le aziende, oltre ai gestionali verticali e al software Whistleblowing.'),
        ('Posso usare il gestionale in cloud?', 'Sì: con Sistemi in Rete i software Sistemi si usano dal web, ospitati nelle Service Farm Sistemi, senza server in ufficio.'),
        ('Come funziona l’assistenza?', 'Il modo più rapido è aprire un ticket dal menu del tuo software Sistemi, allegando log e diagnostica. Per l’accesso remoto usiamo TeamViewer e AnyDesk; puoi anche chiamarci allo 0521 252824.'),
        ('Organizzate corsi di formazione?', 'Sì: corsi pratici nella nostra aula di Parma, sui tuoi dati, con un massimo di 6 partecipanti e docenti certificati Sistemi. Organizziamo anche gli incontri gratuiti 100% Profis direttamente nel tuo studio.'),
        ('Come chiedo una demo?', 'Compila il modulo contatti o chiamaci: ti mostriamo il software più adatto e ti aiutiamo a scegliere.'),
    ]
    con_video = [p for p in POSTS if video_src(p[0], p[3])]
    latest = ''.join(post_card(i, s, t, d, y, sc) for i, (s, t, d, y, _tg, sc) in enumerate(con_video[:3]))
    body = f'''<section class="hero"><div class="wrap hero__in">
  <div class="hero__text hero-seq">
    <h1><span class="kicker">Software gestionali a Parma · Via Sicuri 42/a</span>Il software giusto per lo studio e per l’azienda.</h1>
    <p class="hero__lead">Dal 1990 installiamo, configuriamo e seguiamo i gestionali Sistemi per studi professionali e piccole e medie imprese di Parma, Piacenza e Reggio Emilia: fattura elettronica, contabilità, paghe e controllo di gestione.</p>
    <div class="btn-row"><a class="btn btn--red" href="/contatti/#modulo">Chiedi una demo</a><a class="btn btn--line" href="#selettore">Quale software fa per me?</a></div>
  </div>
  <div class="hero__art" aria-hidden="true">
    <img class="hero__dog" src="/assets/img/campagna/cane-scafandro.png" alt="" width="190" height="226" data-parallax="-0.05" fetchpriority="high">
  </div>
</div></section>
<section class="facts" aria-label="In breve"><div class="wrap facts__in">
  <div class="reveal"><b>Dal 1990</b>partner Sistemi a Parma</div>
  <div class="reveal reveal-d1"><b>Parma · Piacenza · Reggio Emilia</b>le province che seguiamo</div>
  <div class="reveal reveal-d2"><b>Aula corsi in sede</b>massimo 6 partecipanti</div>
  <div class="reveal reveal-d3"><b>Assistenza remota</b>ticket, TeamViewer e AnyDesk</div>
</div></section>

<section class="section section--dark" id="assistenza"><div class="wrap split" style="align-items:center">
  <div><h2 class="h2 js-split">Serve assistenza?</h2><p class="lead" style="margin-top:16px">Apri un ticket dal menu del tuo software Sistemi per allegare log e diagnostica, oppure avvia l’accesso remoto quando te lo chiede il tecnico.</p></div>
  <div class="assist reveal">
    <a href="https://assistenza.sistemi.com/" rel="noopener" target="_blank"><b>Assistenza Online</b><span>apri un ticket</span></a>
    <a href="/assistenza/#remoto"><b>TeamViewer</b><span>QuickSupport</span></a>
    <a href="/assistenza/#remoto"><b>AnyDesk</b><span>accesso remoto</span></a>
    <a class="is-red" href="{TEL_HREF}"><b>{TEL}</b><span>chiamaci</span></a>
  </div>
</div></section>

<section class="section" id="professionisti"><div class="wrap">
  <div class="head-row"><h2 class="h2 js-split">Per gli studi professionali</h2><p>Commercialisti, consulenti del lavoro, avvocati e CTU: attività amministrative, organizzative e di controllo dello studio in un unico ambiente.</p></div>
  <div class="grid grid--3">{product_card("profis")}{product_card("studio","card reveal reveal-d1")}{product_card("job","card reveal reveal-d2")}</div>
  <div class="extra reveal"><span>Completa l’offerta per lo studio</span><a href="https://www.sistemi.com/software-gestionali/profis/sportellocloud/" rel="noopener" target="_blank" aria-label="Sportello Cloud su sistemi.com"><img src="/assets/img/prodotti/sportello-cloud.jpg" alt="Sportello Cloud – Sistemi" width="900" height="148" loading="lazy" style="height:40px"></a></div>
</div></section>

<section class="section" id="aziende" style="padding-top:24px"><div class="wrap">
  <div class="head-row"><h2 class="h2 js-split">Per le aziende</h2><p>Dalla fatturazione web della ditta individuale all’ERP per i processi aziendali: scegliamo insieme la soluzione e la seguiamo nel tempo.</p></div>
  <div class="tiles reveal">
    <a href="/aziende/quadra/"><span class="card__eyebrow">Fatturazione web</span><img class="card__logo" src="/assets/img/prodotti/quadra.jpg" alt="Quadra – Sistemi" width="640" height="191" loading="lazy" style="height:56px"><p>Fattura elettronica anche per i forfettari, documenti di vendita, incassi e pagamenti.</p></a>
    <a href="/aziende/profis-az/"><span class="card__eyebrow">Con il commercialista</span><img class="card__logo" src="/assets/img/prodotti/profis-az.jpg" alt="Profis AZ – Sistemi" width="640" height="160" loading="lazy" style="height:56px"><p>L’azienda gestisce fatture, acquisti e magazzino; lo studio adempimenti, dichiarazioni e bilanci.</p></a>
    <a href="/aziende/spring/"><span class="card__eyebrow">Piccole e micro imprese</span><img class="card__logo" src="/assets/img/prodotti/spring.jpg" alt="Spring – Sistemi" width="640" height="196" loading="lazy" style="height:56px"><p>Contabilità e IVA, vendite, acquisti, magazzino e cespiti: completo e rapido da avviare.</p></a>
    <a href="/aziende/esolver/"><span class="card__eyebrow">ERP</span><img class="card__logo" src="/assets/img/prodotti/esolver.jpg" alt="eSolver – Sistemi" width="640" height="176" loading="lazy" style="height:56px"><p>Amministrazione, ciclo attivo e passivo, logistica con MRP, analitica e produzione servizi.</p></a>
  </div>
</div></section>

{slogan("slogan-voci", "sentite le <voci>? è il nostro [servizio] #clienti.")}

<section class="section section--dark" id="selettore"><div class="wrap selector">
  <div class="selector__intro"><span class="kicker">Tre domande, un consiglio</span><h2 class="h2 js-split">Quale software fa per te?</h2>
    <p class="lead" style="margin-top:20px">Rispondi a tre domande: ti suggeriamo il gestionale più adatto e precompiliamo la richiesta di demo.</p></div>
  <script type="application/json" id="sel-prodotti">{{"studio-contabilita":["PROFIS","/professionisti/profis/","Contabilità ordinaria, semplificata e dei professionisti, dichiarativi e bilanci."],"studio-paghe":["JOB","/professionisti/job/","Amministrazione del personale multiaziendale e multicontrattuale."],"studio-organizzazione":["STUDIO","/professionisti/studio/","Mandati, parcellazione, pratiche, agende e controllo di gestione."],"azienda-contabilita":["SPRING","/aziende/spring/","Gestionale completo per piccole aziende, rapido da mettere in funzione."],"azienda-processi":["eSOLVER","/aziende/esolver/","ERP per amministrazione, logistica, produzione servizi e analitica."],"azienda-commercialista":["PROFIS AZ","/aziende/profis-az/","L’azienda gestisce il quotidiano, lo studio segue adempimenti e bilanci."],"azienda-paghe":["JOB","/professionisti/job/","Amministrazione del personale, anche per le aziende."],"ditta-fatture":["QUADRA","/aziende/quadra/","Fatturazione web semplice, anche per i forfettari."],"ditta-commercialista":["PROFIS AZ","/aziende/profis-az/","Fatture e incassi in azienda, adempimenti allo studio."]}}</script>
  <form class="selector__box reveal" id="selettore-form" data-url-contatti="/contatti/" onsubmit="return false">
    <fieldset><legend>1. Chi sei?</legend><div class="chips">
      <label class="chip"><input type="radio" name="chi" value="studio" checked><span>Studio professionale</span></label>
      <label class="chip"><input type="radio" name="chi" value="azienda"><span>Azienda</span></label>
      <label class="chip"><input type="radio" name="chi" value="ditta"><span>Ditta individuale o forfettario</span></label></div></fieldset>
    <fieldset><legend>2. Di cosa hai bisogno soprattutto?</legend><div class="chips" id="sel-bisogno"></div></fieldset>
    <fieldset><legend>3. Dove vuoi lavorare?</legend><div class="chips">
      <label class="chip"><input type="radio" name="dove" value="locale" checked><span>Sui miei PC</span></label>
      <label class="chip"><input type="radio" name="dove" value="cloud"><span>In cloud (Sistemi in Rete)</span></label></div></fieldset>
    <div class="grid grid--2 selector__opt" style="gap:14px">
      <div><label for="sel-settore">Settore o attività (facoltativo)</label><input id="sel-settore" type="text" placeholder="es. autotrasporti, studio associato"></div>
      <div><label for="sel-utenti">Quante persone lo useranno? (facoltativo)</label><input id="sel-utenti" type="number" min="1" placeholder="es. 3"></div>
    </div>
    <div class="selector__result" aria-live="polite">
      <div><small>Il nostro consiglio</small><strong id="sel-nome">PROFIS</strong><p id="sel-desc"></p></div>
      <div class="btn-row"><a class="btn btn--white" id="sel-cta" href="/contatti/#modulo">Richiedi una demo</a><a class="btn btn--ghost" id="sel-more" href="/professionisti/profis/">Scheda</a></div>
    </div>
  </form>
</div></section>

<section class="section" id="guida"><div class="wrap">
  <div class="head-row"><h2 class="h2 js-split">Guida rapida: quale prodotto scegliere</h2><p>Un orientamento veloce. Per la scelta definitiva ti consigliamo una demo con noi.</p></div>
  <div class="table-wrap reveal"><table class="compare">
    <thead><tr><th scope="col">Prodotto</th><th scope="col">Per chi</th><th scope="col">Cosa gestisce</th></tr></thead>
    <tbody>
      <tr><th scope="row"><a href="/professionisti/profis/">Profis</a></th><td data-label="Per chi">Commercialisti e studi che offrono consulenza fiscale</td><td data-label="Cosa gestisce">Contabilità, fiscale, bilanci, gruppi, pratiche</td></tr>
      <tr><th scope="row"><a href="/professionisti/studio/">Studio</a></th><td data-label="Per chi">Commercialisti, consulenti del lavoro, avvocati</td><td data-label="Cosa gestisce">Mandati, parcelle, pratiche, agende, controllo di gestione</td></tr>
      <tr><th scope="row"><a href="/professionisti/job/">Job</a></th><td data-label="Per chi">Consulenti del lavoro, studi, imprese</td><td data-label="Cosa gestisce">Paghe, presenze, 730 e 770, cedolini online</td></tr>
      <tr><th scope="row"><a href="/aziende/quadra/">Quadra</a></th><td data-label="Per chi">Ditte individuali e forfettari</td><td data-label="Cosa gestisce">Fattura elettronica, vendite, incassi</td></tr>
      <tr><th scope="row"><a href="/aziende/profis-az/">Profis AZ</a></th><td data-label="Per chi">Piccole imprese seguite da un commercialista con Profis</td><td data-label="Cosa gestisce">Fatture, acquisti, magazzino; adempimenti allo studio</td></tr>
      <tr><th scope="row"><a href="/aziende/spring/">Spring</a></th><td data-label="Per chi">Piccole e micro imprese</td><td data-label="Cosa gestisce">Contabilità, vendite, acquisti, magazzino, cespiti</td></tr>
      <tr><th scope="row"><a href="/aziende/esolver/">eSolver</a></th><td data-label="Per chi">Imprese strutturate e associazioni</td><td data-label="Cosa gestisce">ERP: amministrazione, logistica con MRP, analitica, servizi</td></tr>
    </tbody></table></div>
</div></section>

<section class="section section--soft" id="cloud"><div class="wrap">
  <div class="head-row"><div><span class="kicker">Metodi a confronto</span><h2 class="h2 js-split">In ufficio o in cloud?</h2></div><p>I software Sistemi si possono installare sui tuoi PC o usare dal web con Sistemi in Rete. Ecco le differenze principali.</p></div>
  <div class="table-wrap reveal"><table class="compare">
    <thead><tr><th scope="col">Aspetto</th><th scope="col">Installazione in ufficio</th><th scope="col">Sistemi in Rete (cloud)</th></tr></thead>
    <tbody>
      <tr><th scope="row">Server</th><td data-label="In ufficio">Serve un server o un PC dedicato in sede</td><td data-label="In cloud">Ospitato nelle Service Farm Sistemi</td></tr>
      <tr><th scope="row">Accesso</th><td data-label="In ufficio">Dalla rete dell’ufficio</td><td data-label="In cloud">Dal web, anche fuori sede</td></tr>
      <tr><th scope="row">Backup e aggiornamenti</th><td data-label="In ufficio">Da organizzare in sede</td><td data-label="In cloud">Gestiti nell’infrastruttura Sistemi</td></tr>
      <tr><th scope="row">Connessione</th><td data-label="In ufficio">Lavori anche senza internet</td><td data-label="In cloud">Serve una connessione stabile</td></tr>
    </tbody></table></div>
  <div class="reveal" style="margin-top:40px;display:flex;flex-wrap:wrap;gap:24px 40px;align-items:center">
    <img src="/assets/img/campagna/slogan-nuvola-800.jpg" alt="il {{futuro digitale}}? è nella rete delle [soluzioni software] #Sistemi." width="800" height="300" loading="lazy" style="max-width:480px;width:100%">
    <a class="link-arrow" href="https://www.sistemi.com/sistemi-in-rete/" rel="noopener" target="_blank">SISTEMINRETE su sistemi.com ↗</a></div>
</div></section>

<section class="section" id="servizi"><div class="wrap">
  <h2 class="h2 js-split" style="margin-bottom:40px">Non solo gestionali</h2>
  <div class="grid grid--4">
    <a class="card card--soft reveal" href="#cloud">{icon("cloud")}<h3>Sistemi in Rete</h3><p>I tuoi gestionali dal web, ospitati nelle Service Farm Sistemi: niente server in ufficio.</p></a>
    <a class="card card--soft reveal reveal-d1" href="/whistleblowing/">{icon("lock")}<h3>Whistleblowing</h3><p>Il canale di segnalazione riservato previsto dal D.lgs. 24/2023, in cloud, da PC, tablet e smartphone.</p></a>
    <a class="card card--soft reveal reveal-d2" href="/aziende/verticali/">{icon("tool")}<h3>Gestionali verticali</h3><p>Agrifarm, Autotrasporti, Green Services, Manutenzione impianti, Euritmo e Filconad per Spring ed eSolver.</p></a>
    <a class="card card--soft reveal reveal-d3" href="/siti-web/">{icon("globe")}<h3>Siti web</h3><p>Siti per aziende e studi, anche integrati con il gestionale e con l’e-commerce.</p></a>
    <a class="card card--soft reveal" href="/aziende/peoplelink/">{icon("users")}<h3>PeopleLink</h3><p>La piattaforma HR cloud e mobile: presenze, ferie, commesse e note spese, integrata con Job.</p></a>
  </div>
</div></section>

<section class="section section--soft" id="corsi"><div class="wrap">
  <div class="head-row"><div><span class="kicker">Corsi ed eventi</span><h2 class="h2 js-split">Impara a usare davvero il tuo gestionale</h2></div><p>Corsi pratici in aula a Parma, sui tuoi dati, con docenti certificati Sistemi. Massimo 6 partecipanti.</p></div>
  <div class="grid grid--4">
    <article class="card card--course reveal"><span class="card__eyebrow">In aula · 12 ore</span><h3>Contabilità e Cespiti Base</h3><p>Impostazione contabile e IVA in Profis, dalle fatture elettroniche al registro dei beni ammortizzabili.</p><a class="btn btn--dark" href="/corsi/contabilita-cespiti/" style="margin-top:auto">Programma e iscrizione</a></article>
    <article class="card card--course reveal reveal-d1"><span class="card__eyebrow">In aula · 12 ore</span><h3>Studio 4</h3><p>Catalogo servizi, mandati, parcellazione automatica, pratiche, agende e archiviazione documentale.</p><a class="btn btn--dark" href="/corsi/studio-4/" style="margin-top:auto">Programma e iscrizione</a></article>
    <article class="card card--course reveal reveal-d2"><span class="card__eyebrow">In aula · 6 ore</span><h3>Profis Pratiche e Locazioni</h3><p>Comunicazione Unica, pratiche Agenzia delle Entrate e Registro Imprese, contratti di locazione.</p><a class="btn btn--dark" href="/corsi/pratiche-locazioni/" style="margin-top:auto">Programma e iscrizione</a></article>
    <article class="card card--dark card--course reveal reveal-d3"><span class="card__eyebrow" style="color:var(--red-soft)">Gratuito · nel tuo studio · 1 h 30</span><h3>100% Profis</h3><p>Incontri gratuiti di approfondimento per sfruttare le funzioni avanzate di Profis.</p><a class="btn btn--red" href="/corsi/100-profis/" style="margin-top:auto">Prenota un incontro</a></article>
  </div>
</div></section>

<section class="section" id="pillole"><div class="wrap">
  <div class="head-row"><div><span class="kicker">Blog · videotutorial</span><h2 class="h2 js-split">Le Pillole</h2></div><a class="link-arrow" href="/pillole/">Tutte le pillole →</a></div>
  <div class="grid grid--3">{latest}</div>
</div></section>

<section class="section" id="chi-siamo"><div class="wrap split">
  <div><span class="kicker">Chi siamo</span><h2 class="h2 js-split">Partner Sistemi dal 1990</h2>
    <button type="button" class="video-btn reveal" style="margin-top:28px;max-width:460px" data-video="https://www.youtube.com/watch?v={PROMO_YT}" data-title="Servizi Informatici – il software per lo studio professionale" aria-label="Riproduci il video di presentazione">
      <div class="thumb thumb--red"><span class="thumb__t">Guarda chi siamo<br>in un minuto</span><span class="thumb__play">{PLAY}</span></div></button></div>
  <div class="reveal" style="color:#444">
    <p>Servizi Informatici Srl nasce nel 1990 come concessionario certificato Sistemi SpA per le province di Parma, Piacenza e Reggio Emilia. Grazie a competenze e certificazioni ha ottenuto la qualifica SISTEMI CITTÀ e il nome Sistemi Parma.</p>
    <p>Abbiamo sviluppato competenze soprattutto per gli studi professionali, con la linea Profis, e per le aziende, con le linee Spring ed eSolver. Oggi siamo in 14, distribuiti tra le diverse linee di prodotto. Realizziamo anche siti web per aziende e studi e integriamo i gestionali con le piattaforme di e-commerce.</p>
  </div>
</div></section>

{faq_html(home_faqs)}

<section class="section" id="contatti" style="padding-top:0"><div class="wrap">
  <div class="contact-box">
    <div><h2 class="h2">Scrivici</h2><p class="lead" style="margin-top:14px">Informazioni, demo o un preventivo: ti rispondiamo noi.</p>
      <ul class="contact-list"><li><a href="{MAPS}" rel="noopener" target="_blank"><b>Servizi Informatici Srl</b><br>{ADDR}</a></li><li><a href="{TEL_HREF}">{TEL}</a></li><li><a href="mailto:{MAIL}">{MAIL}</a></li></ul></div>
    {contact_form(pagina="home")}
  </div>
</div></section>'''
    page('/', 'Software gestionali a Parma per studi e aziende | Sistemi Parma', 'Sistemi Parma (Servizi Informatici Srl), concessionario Sistemi dal 1990: Profis, Studio, Job, Spring, eSolver, Quadra. Assistenza, corsi e cloud a Parma, Piacenza e Reggio Emilia.', body, None, [faq_ld(home_faqs)])

    # ------------------------------------------------------------ Categorie
    crumbs = [(None, 'Professionisti')]
    body = page_hero(crumbs, 'Software per studi professionali a Parma', 'Software gestionali per gli studi professionali', 'Gestisci in modo integrato le attività amministrative, organizzative e di controllo dello studio: commercialisti, consulenti del lavoro, avvocati e CTU.')
    body += f'''<section class="section"><div class="wrap"><div class="grid grid--3">{product_card("profis")}{product_card("studio","card reveal reveal-d1")}{product_card("job","card reveal reveal-d2")}</div>
<div class="extra reveal"><span>Completa l’offerta</span><a href="https://www.sistemi.com/software-gestionali/profis/sportellocloud/" rel="noopener" target="_blank" aria-label="Sportello Cloud su sistemi.com"><img src="/assets/img/prodotti/sportello-cloud.jpg" alt="Sportello Cloud – Sistemi" width="900" height="148" loading="lazy" style="height:40px"></a></div></div></section>
<section class="section section--soft" id="sportello"><div class="wrap">
  <div class="head-row"><div><span class="kicker">Documentazione</span><h2 class="h2 js-split">Sportello Cloud: le schede</h2></div><p>I servizi web che lo studio mette a disposizione dei clienti. Schede ufficiali di Sistemi SpA, in PDF.</p></div>
  <ul class="pdf-list reveal">
    <li><a class="pdf-link" href="https://www.sistemi.com/downloads/SPORTELLO_cloud-scheda.pdf" rel="noopener" target="_blank">{icon("file","icon pdf-ico")}<span>Sportello Cloud</span><small>PDF · sistemi.com</small></a></li>
    <li><a class="pdf-link" href="https://www.sistemi.com/downloads/Sportello-QUADRA-scheda.pdf" rel="noopener" target="_blank">{icon("file","icon pdf-ico")}<span>Sportello Quadra</span><small>PDF · sistemi.com</small></a></li>
    <li><a class="pdf-link" href="https://www.sistemi.com/downloads/Sportello-Documenti-condivisi-scheda.pdf" rel="noopener" target="_blank">{icon("file","icon pdf-ico")}<span>Sportello Documenti condivisi</span><small>PDF · sistemi.com</small></a></li>
    <li><a class="pdf-link" href="https://www.sistemi.com/downloads/Sportello-Interrogazione-conti-bancari_scheda.pdf" rel="noopener" target="_blank">{icon("file","icon pdf-ico")}<span>Sportello Interrogazione conti bancari</span><small>PDF · sistemi.com</small></a></li>
  </ul>
</div></section>
{slogan("slogan-luna", "più <vicini> ai vostri #clienti; anche da molto_remoto.")}
{cta_band("Corsi in aula per il tuo studio", "Contabilità e Cespiti, Studio 4, Pratiche e Locazioni e gli incontri gratuiti 100% Profis.", "/corsi/", "Vedi i corsi", ("/contatti/#modulo", "Chiedi una demo"))}'''
    page('/professionisti/', 'Software per commercialisti e studi professionali a Parma | Sistemi Parma', 'Profis, Studio e Job di Sistemi per commercialisti, consulenti del lavoro e avvocati a Parma: installazione, assistenza e corsi da Servizi Informatici.', body, crumbs)

    crumbs = [(None, 'Aziende')]
    body = page_hero(crumbs, 'Software gestionali per aziende a Parma', 'Software gestionali per le aziende', 'Una suite di gestionali Sistemi per gestire in modo integrato amministrazione, vendite, acquisti, magazzino e controllo: dalla ditta individuale all’ERP.')
    body += f'''<section class="section"><div class="wrap"><div class="grid grid--2">{product_card("quadra")}{product_card("profis-az","card reveal reveal-d1")}{product_card("spring")}{product_card("esolver","card reveal reveal-d1")}{product_card("peoplelink")}</div></div></section>
<section class="section section--soft"><div class="wrap split" style="align-items:center"><div><span class="kicker">Per settore</span><h2 class="h2 js-split">Gestionali verticali</h2><p class="lead" style="margin-top:14px">Agricoltura, autotrasporti, aree verdi, manutenzione impianti e formati EDI per la grande distribuzione.</p></div><div class="reveal"><a class="btn btn--dark" href="/aziende/verticali/">Scopri i verticali</a></div></div></section>
{slogan("slogan-cane", "i [software] #Sistemi sono i migliori amici del vostro {futuro}.")}'''
    page('/aziende/', 'Software gestionali per aziende a Parma: Spring, eSolver, Quadra | Sistemi Parma', 'Gestionali Sistemi per aziende a Parma: Quadra per la fatturazione web, Profis AZ, Spring per piccole imprese ed eSolver ERP. Installazione e assistenza.', body, crumbs)

    # ------------------------------------------------------------ Verticali
    V = [('AGRIFARM','Spring / eSolver','Software gestionale e analitico per la conduzione delle aziende agricole.'),
         ('EURITMO','Spring','Esportazione dei documenti di trasporto e di vendita nel formato EURITMO.'),
         ('GREEN SERVICES','Spring','Software per le aziende di gestione e manutenzione di aree verdi pubbliche e private.'),
         ('AUTOTRASPORTI','Spring / eSolver','Software gestionale per le ditte di autotrasporti.'),
         ('FILCONAD','Spring / eSolver','Esportazione dei documenti di vendita nel formato FILCONAD.'),
         ('MANUTENZIONE IMPIANTI','Spring','Software per le aziende di servizi di manutenzione programmata agli impianti.')]
    crumbs = [('/aziende/', 'Aziende'), (None, 'Gestionali verticali')]
    cards = ''.join(f'<div class="card reveal"><span class="card__eyebrow">{h(b)}</span><h3>{h(n.title())}</h3><p>{h(d)}</p></div>' for n, b, d in V)
    body = page_hero(crumbs, 'Software verticali per settore a Parma', 'Software verticali per le aziende', 'Soluzioni per settori specifici che si integrano con Spring ed eSolver.')
    body += f'''<section class="section"><div class="wrap"><div class="grid grid--3">{cards}</div>
<div class="reveal" style="margin-top:40px;display:flex;flex-wrap:wrap;gap:16px"><span class="campaign"><img src="/assets/img/campagna/enologia.png" alt="Campagna Sistemi: il software per l’enologia" width="349" height="120" loading="lazy"></span><span class="campaign"><img src="/assets/img/campagna/oleario.png" alt="Campagna Sistemi: il software per il settore oleario" width="349" height="120" loading="lazy"></span></div></div></section>
{cta_band("Il tuo settore non è in elenco?", "Raccontaci come lavori: verifichiamo insieme la soluzione più adatta.", "/contatti/?prodotto=Gestionali%20verticali#modulo", "Contattaci")}'''
    page('/aziende/verticali/', 'Gestionali verticali: Agrifarm, Autotrasporti, Green Services | Sistemi Parma', 'Software verticali Sistemi a Parma per aziende agricole, autotrasporti, aree verdi, manutenzione impianti e formati Euritmo e Filconad.', body, crumbs)

    # ------------------------------------------------------------ Whistleblowing
    crumbs = [(None, 'Whistleblowing')]
    wb_faqs = [
        ('Quali aziende devono avere un canale di whistleblowing?', 'Secondo il D.lgs. 24/2023, i soggetti privati che nell’ultimo anno hanno impiegato la media di almeno 50 lavoratori subordinati, quelli che hanno adottato un modello organizzativo ai sensi del D.lgs. 231/2001 (anche sotto i 50 dipendenti) e quelli che operano nei settori indicati dalla normativa europea.'),
        ('Quali sanzioni sono previste?', 'L’ANAC può applicare sanzioni amministrative da 10.000 a 50.000 euro, ad esempio quando accerta che non sono stati istituiti canali di segnalazione o non sono state adottate le procedure previste.'),
        ('Il segnalante può restare anonimo?', 'Sì: il software gestisce la corrispondenza anche con un segnalante anonimo e protegge la riservatezza della sua identità con codici sostitutivi dei dati identificativi.'),
        ('Come si calcola il costo del servizio?', 'L’offerta è definita per classi di numero di dipendenti e prevede un costo di attivazione e un canone che decorre dal primo giorno del mese successivo all’attivazione. Contattaci per un preventivo.'),
    ]
    body = page_hero(crumbs, 'Software whistleblowing a Parma', 'Sistemi Whistleblowing: la piattaforma per gestire le segnalazioni', 'Il canale interno e riservato per la segnalazione di illeciti previsto dal D.lgs. 24/2023, in cloud e accessibile da PC, tablet e smartphone.',
                     extra='<div class="btn-row" style="margin-top:32px"><a class="btn btn--red" href="/contatti/?prodotto=Whistleblowing#modulo">Chiedi informazioni</a></div>')
    body += f'''<section class="section"><div class="wrap prose">
<h2>Cos’è il whistleblowing?</h2>
<p>Con il termine whistleblowing si intende la segnalazione di illeciti aziendali. La materia è regolata dal decreto legislativo 10 marzo 2023, n. 24, che recepisce la direttiva (UE) 2019/1937: le aziende obbligate devono predisporre un canale interno e riservato per la segnalazione delle condotte illecite. Per chi non si adegua l’ANAC può applicare sanzioni da 10.000 a 50.000 euro.</p>
<p>L’ANAC ha inoltre emanato il Regolamento sull’esercizio del potere sanzionatorio in materia di tutela degli autori di segnalazioni e ha reso disponibile una propria piattaforma per le segnalazioni esterne.</p>
<h2>Chi è obbligato</h2>
<ul>
<li>i soggetti privati che, nell’ultimo anno, hanno impiegato la media di almeno 50 lavoratori subordinati;</li>
<li>i soggetti che hanno adottato un modello di organizzazione e gestione ai sensi del D.lgs. 231/2001, anche sotto i 50 dipendenti;</li>
<li>i soggetti che rientrano nei settori disciplinati dagli atti dell’Unione europea richiamati dal decreto, indipendentemente dal numero di dipendenti.</li>
</ul>
<p>Gli obblighi sono in vigore dal 15 luglio 2023 per le pubbliche amministrazioni e per le aziende con più di 249 dipendenti, e dal 17 dicembre 2023 per le aziende da 50 a 249 dipendenti.</p>
<h2>Cosa si può segnalare?</h2>
<ul>
<li>illeciti amministrativi, contabili, civili e penali;</li>
<li>condotte illecite ai sensi del decreto legislativo 231/2001;</li>
<li>illeciti che rientrano negli atti dell’Unione europea o nazionali relativi a: appalti pubblici; servizi, prodotti e mercati finanziari e prevenzione del riciclaggio e del finanziamento del terrorismo; sicurezza e conformità dei prodotti; sicurezza dei trasporti; tutela dell’ambiente; radioprotezione e sicurezza nucleare; sicurezza degli alimenti e dei mangimi, salute e benessere degli animali; salute pubblica; protezione dei consumatori; tutela della vita privata, protezione dei dati personali e sicurezza delle reti e dei sistemi informativi.</li>
</ul>
<h2>Chi può inviare una segnalazione?</h2>
<p>Dipendenti, consulenti, collaboratori, ex dipendenti, clienti, fornitori, tirocinanti e azionisti possono fare una segnalazione scritta o orale tramite il software Sistemi Whistleblowing, accessibile da PC, tablet e smartphone.</p>
<h2>Come viene tutelato il segnalante?</h2>
<p>L’identità del segnalante non può essere rivelata a persone diverse da quelle competenti a ricevere o a dare seguito alle segnalazioni, nel rispetto del GDPR. Il software Sistemi Whistleblowing assicura la riservatezza del segnalante e del contenuto della segnalazione con strumenti di crittografia.</p>
<h2>Quali adempimenti sono previsti?</h2>
<h3>1. Istituzione di canali interni di segnalazione</h3>
<p>Canali che consentano alle persone legittimate di segnalare violazioni, cioè comportamenti, atti od omissioni che ledono l’interesse pubblico o l’integrità dell’ente privato, elencate all’art. 1 del D.lgs. 24/2023. L’istituzione dei canali deve essere preceduta da un confronto sindacale: quanto meno una comunicazione alle organizzazioni sindacali esterne o alla rappresentanza sindacale interna.</p>
<h3>2. Individuazione del soggetto incaricato della gestione</h3>
<p>L’azienda individua chi gestisce le segnalazioni: non può essere uno degli amministratori della società, ma può essere un dipendente, purché autonomo, oppure un soggetto esterno, anch’esso in posizione di autonomia. Il soggetto incaricato deve essere formato e avere gli strumenti per gestire il canale e le segnalazioni secondo la procedura e i termini fissati dal D.lgs. 24/2023.</p>
<h3>3. Informativa</h3>
<p>Le aziende con un sito internet devono pubblicare in una sezione dedicata le informazioni sul canale di segnalazione; le stesse informazioni vanno rese disponibili anche all’interno dell’azienda.</p>
<h3>4. Archiviazione</h3>
<p>Serve un sistema di conservazione, non necessariamente digitale, per le segnalazioni ricevute, qualunque sia la forma in cui sono state presentate, e per la documentazione relativa alla gestione di ciascuna pratica.</p>
<h2>Qual è l’obiettivo?</h2>
<p>Oltre a essere un obbligo di legge, la gestione del whistleblowing permette di ridurre i rischi di illeciti, garantendo trasparenza e integrità verso i collaboratori interni ed esterni.</p>
<p class="note">Per approfondire: il testo del <a href="https://www.gazzettaufficiale.it/eli/id/2023/03/15/23G00032/sg" rel="noopener" target="_blank">D.lgs. 10 marzo 2023, n. 24 sulla Gazzetta Ufficiale</a> e la sezione whistleblowing del sito <a href="https://www.anticorruzione.it/-/whistleblowing" rel="noopener" target="_blank">ANAC</a>. [SEGNAPOSTO: esempio di circolare da inviare ai dipendenti, in PDF]</p>
</div></section>
<section class="section section--soft"><div class="wrap">
  <div class="head-row"><div><span class="kicker">La soluzione Sistemi</span><h2 class="h2 js-split">Software Sistemi Whistleblowing</h2></div><p>La piattaforma cloud Sistemi che permette a chi assiste ad attività irregolari o condotte illecite di segnalarle attraverso canali interni all’azienda, con la massima riservatezza.</p></div>
  <div class="grid grid--2">
    <div class="card reveal"><h3>I punti di forza</h3><ul class="list-check">
      <li>Interfaccia intuitiva per inserire e gestire le segnalazioni da PC, smartphone o tablet</li>
      <li>Riservatezza dell’identità del segnalante con codici sostitutivi, mantenendo la tracciabilità del processo</li>
      <li>Contenuto delle segnalazioni riservato e non modificabile durante tutta la gestione</li>
      <li>Notifica di avvenuta ricezione delle segnalazioni</li></ul></div>
    <div class="card reveal reveal-d1"><h3>Le funzionalità</h3><ul class="list-check">
      <li>Comunicazione informatica che tutela riservatezza e immodificabilità della segnalazione ed eventuale anonimato</li>
      <li>Gestione della corrispondenza con il segnalante, anche anonimo</li>
      <li>Notifica di ricezione delle segnalazioni</li>
      <li>Modello di segnalazione e successivi adempimenti</li>
      <li>Conservazione (non digitale) delle segnalazioni e relativo registro</li></ul></div>
  </div>
  <div class="note reveal" style="margin-top:28px"><b style="color:#000">L’offerta commerciale</b> è definita per classi di numero di dipendenti: un costo di attivazione e un canone che decorre dal primo giorno del mese successivo all’attivazione. Il servizio permette di attivare più ditte; per motivi di riservatezza in fase di accesso se ne raccomanda l’uso solo all’interno di un gruppo societario.</div>
</div></section>
{faq_html(wb_faqs)}
{cta_band("Vuoi attivare il canale di segnalazione?", "Ti spieghiamo come funziona e ti prepariamo l’offerta in base al numero di dipendenti.", "/contatti/?prodotto=Whistleblowing#modulo", "Chiedi informazioni", ("https://www.sistemi.com/segnalazioni-illeciti-whistleblowing/", "La scheda su sistemi.com ↗"))}'''
    page('/whistleblowing/', 'Software whistleblowing D.lgs. 24/2023 a Parma | Sistemi Parma', 'Sistemi Whistleblowing a Parma: il canale di segnalazione riservato previsto dal D.lgs. 24/2023, in cloud, con anonimato e registro. Obblighi, sanzioni e adempimenti.', body, crumbs, [faq_ld(wb_faqs)])

    # ------------------------------------------------------------ Siti web
    crumbs = [(None, 'Siti web')]
    port = [('Piccinini Autotrasporti', 'https://www.transilospiccinini.com/', 'www.transilospiccinini.com', 'piccinini'),
            ('Il Parmense Trasporti', 'https://www.ilparmensetrasporti.it/', 'www.ilparmensetrasporti.it', 'il-parmense'),
            ('Carlo Mora Parrucchieri', 'https://www.carlomora.com/', 'www.carlomora.com', None),
            ('JAM Photo', 'https://www.jamphoto.it/', 'www.jamphoto.it', 'jam-photo'),
            ('Tymex', 'https://www.tymex.it/', 'www.tymex.it', 'tymex'),
            ('Go Forrest', 'https://www.goforrest.it/', 'www.goforrest.it', 'go-forrest'),
            ('UMA Parrucchieri', 'https://www.umaparrucchieri.it/', 'www.umaparrucchieri.it', 'uma-parrucchieri'),
            ('Tecnogronda', 'https://www.tecnogronda.it/', 'www.tecnogronda.it', 'tecnogronda'),
            ('Officina Agricola Ghisotti', 'https://www.officinaghisotti.it/', 'www.officinaghisotti.it', 'officina-ghisotti'),
            ('Castaldini Autotrasporti', 'https://www.castaldinisas.it/', 'www.castaldinisas.it', 'castaldini')]
    cards = ''.join(f'<a class="card reveal" href="{u}" rel="noopener" target="_blank">'
                    + (f'<img class="card__marchio" src="/assets/img/portfolio/{lg}.png" alt="" width="200" height="64" loading="lazy">'
                       if lg else '<span class="card__marchio card__marchio--vuoto">Sito realizzato</span>')
                    + f'<h3>{h(n)}</h3><p>{h(d)}</p><span class="link-arrow">Visita il sito ↗</span></a>' for n, u, d, lg in port)
    body = page_hero(crumbs, 'Realizzazione siti web a Parma', 'Siti web per aziende e studi professionali', 'Progettiamo e realizziamo siti web per aziende e studi: ottimizzati per smartphone, in https, attenti al GDPR e, se serve, integrati con il gestionale e con l’e-commerce.')
    body += f'''<section class="section"><div class="wrap"><h2 class="h2 js-split" style="margin-bottom:36px">Alcuni lavori</h2><div class="grid grid--3">{cards}</div></div></section>
{cta_band("Vuoi un sito nuovo?", "Raccontaci cosa ti serve: ti proponiamo una soluzione su misura.", "/contatti/?prodotto=Siti%20web#modulo", "Chiedi informazioni")}'''
    page('/siti-web/', 'Realizzazione siti web per aziende e studi a Parma | Sistemi Parma', 'Siti web per aziende e studi professionali a Parma: mobile friendly, https, GDPR, integrati con gestionale ed e-commerce. Servizi Informatici Srl.', body, crumbs)

    # ------------------------------------------------------------ Assistenza
    crumbs = [(None, 'Assistenza')]
    as_faqs = [('Qual è il modo più rapido per chiedere assistenza?', 'Aprire la richiesta direttamente dal menu del tuo software Sistemi: puoi allegare il log degli errori e la diagnostica, seguire lo stato della richiesta e consultare lo storico dei casi risolti.'),
               ('Quando devo scaricare TeamViewer o AnyDesk?', 'Solo quando te lo chiede un nostro tecnico: servono per l’accesso remoto al tuo computer e velocizzano l’individuazione del problema.'),
               ('Posso telefonare?', 'Certo, il numero è 0521 252824.')]
    body = page_hero(crumbs, 'Assistenza software Sistemi a Parma', 'Assistenza remota',
                     'Apri la richiesta dal menu del tuo software Sistemi, oppure avvia l’accesso remoto quando te lo chiede il tecnico.',
                     compatta=True)
    body += f'''<section class="section" style="padding-top:24px"><div class="wrap"><div class="grid grid--3 grid--alto">
  <div class="card reveal"><img class="logo-tile" src="/assets/img/loghi/sistemi.png" alt="Sistemi" width="52" height="52"><h3>Assistenza Online (AOL)</h3><p>Apri un ticket: puoi allegare log e diagnostica e seguire lo stato.</p><a class="btn btn--dark" href="https://assistenza.sistemi.com/" rel="noopener" target="_blank" style="margin-top:auto">Accedi</a></div>
  <div class="card reveal reveal-d1" id="remoto"><img class="logo-tile" src="/assets/img/loghi/teamviewer.png" alt="" width="52" height="52"><h3>TeamViewer QuickSupport</h3><p>Il programma per l’accesso remoto: avvialo quando te lo chiede il tecnico.</p>
    <div style="margin-top:auto"><span class="card__eyebrow" style="display:block;margin-bottom:10px">Scarica per Windows o Mac</span>
    <div class="btn-row btn-row--uno"><a class="btn btn--dark" href="https://download.teamviewer.com/download/TeamViewerQS_x64.exe" rel="noopener">64 bit</a><a class="btn btn--line" href="https://download.teamviewer.com/download/TeamViewerQS.exe" rel="noopener">32 bit</a><a class="btn btn--line" href="https://download.teamviewer.com/download/TeamViewerQS.dmg" rel="noopener">Mac</a></div></div></div>
  <div class="card reveal reveal-d2"><img class="logo-tile logo-tile--chip" src="/assets/img/loghi/anydesk.png" alt="" width="169" height="52"><h3>AnyDesk</h3><p>In alternativa a TeamViewer, quando te lo chiede il tecnico.</p><a class="btn btn--dark" href="https://anydesk.com/it/downloads" rel="noopener" target="_blank" style="margin-top:auto">Scarica AnyDesk</a></div>
</div>
</div>
</div></section>
{slogan("slogan-voci", "sentite le <voci>? è il nostro [servizio] #clienti.")}
{faq_html(as_faqs)}
{slogan("slogan-luna", "più <vicini> ai vostri #clienti; anche da molto_remoto.")}'''
    page('/assistenza/', 'Assistenza remota software Sistemi a Parma | Sistemi Parma', 'Assistenza sui software Sistemi a Parma: ticket AOL, TeamViewer QuickSupport, AnyDesk e telefono 0521 252824. Servizi Informatici Srl.', body, crumbs, [faq_ld(as_faqs)])

    # ------------------------------------------------------------ Corsi
    crumbs = [(None, 'Corsi ed eventi')]
    co_faqs = [('Dove si svolgono i corsi?', 'Nell’aula corsi della nostra sede in Via Sicuri 42/a a Parma, con un massimo di 6 partecipanti. Gli incontri 100% Profis si svolgono invece nel tuo studio.'),
               ('Come mi iscrivo a un corso in aula?', 'Dalla pagina del corso compili il modulo con i dati del partecipante e quelli per la fattura. Ti confermiamo noi date e quota; la fattura arriva a parte.'),
               ('Come mi iscrivo agli eventi gratuiti?', 'Webinar e incontri gratuiti si prenotano online con il pulsante di iscrizione nella scheda dell’evento.'),
               ('Organizzate corsi su richiesta?', 'Scrivici: valutiamo insieme argomenti e date.')]
    body = page_hero(crumbs, 'Corsi Profis e Studio a Parma', 'Corsi ed eventi', 'Corsi pratici in aula sui software Sistemi e incontri gratuiti di approfondimento, con docenti certificati Sistemi. Lavori sui tuoi dati e porti a casa risultati concreti.')
    body += f'''<section class="section"><div class="wrap">
  <h2 class="h2 js-split" style="margin-bottom:36px">Corsi in aula</h2>
  <div class="grid grid--3">
    <article class="card card--course reveal"><span class="card__eyebrow">Profis · 4 mezze giornate · 12 ore</span><h3>Contabilità e Cespiti Base</h3><p>Impostazione contabile e IVA, fatture elettroniche, corrispettivi, F24 e gestione dei cespiti.</p><a class="btn btn--dark" href="/corsi/contabilita-cespiti/" style="margin-top:auto">Programma e iscrizione</a></article>
    <article class="card card--course reveal reveal-d1"><span class="card__eyebrow">Studio · 4 mezze giornate · 12 ore</span><h3>Studio 4</h3><p>Catalogo servizi, mandati, parcellazione automatica, pratiche, agende e archiviazione.</p><a class="btn btn--dark" href="/corsi/studio-4/" style="margin-top:auto">Programma e iscrizione</a></article>
    <article class="card card--course reveal reveal-d2"><span class="card__eyebrow">Profis · 2 mezze giornate · 6 ore</span><h3>Profis Pratiche e Contratti di Locazione</h3><p>Comunicazione Unica, pratiche Agenzia delle Entrate e Registro Imprese, locazioni.</p><a class="btn btn--dark" href="/corsi/pratiche-locazioni/" style="margin-top:auto">Programma e iscrizione</a></article>
  </div>
</div></section>
<section class="section section--soft"><div class="wrap split">
  <div><span class="kicker">Gratuito</span><h2 class="h2 js-split">100% Profis</h2><p class="lead" style="margin-top:14px">Incontri gratuiti di approfondimento su Profis, direttamente nel tuo studio. Durata 1 ora e 30 minuti.</p><a class="btn btn--red" href="/corsi/100-profis/" style="margin-top:24px">Prenota un incontro</a></div>
  <div class="reveal"><span class="kicker">Eventi gratuiti e webinar</span><h2 class="h2" style="font-size:28px">Prossimi eventi</h2>
    <p style="margin-top:14px">Al momento non ci sono eventi gratuiti in calendario. Quando pubblichiamo un webinar o un Focus lo trovi qui, con l’iscrizione online.</p>
    <!-- Per aggiungere un evento Eventbrite: <button id="eb-ID" class="btn btn--dark" type="button" data-eventbrite="ID_EVENTO">Iscriviti gratis</button> -->
    <a class="link-arrow" href="/contatti/?prodotto=Informazioni%20generali&amp;nota=Vorrei%20essere%20avvisato%20dei%20prossimi%20eventi%20gratuiti.#modulo">Avvisami dei prossimi eventi →</a></div>
</div></section>
{faq_html(co_faqs)}'''
    page('/corsi/', 'Corsi Profis e Studio in aula a Parma | Sistemi Parma', 'Corsi pratici sui software Sistemi a Parma: Contabilità e Cespiti, Studio 4, Pratiche e Locazioni. Massimo 6 partecipanti. Incontri gratuiti 100% Profis.', body, crumbs, [faq_ld(co_faqs)])

    crumbs = [('/corsi/', 'Corsi ed eventi'), (None, '100% Profis')]
    body = page_hero(crumbs, 'Incontri gratuiti su Profis', '100% Profis', 'Incontri gratuiti di approfondimento per sfruttare le funzionalità avanzate di Profis, direttamente nel tuo studio professionale.',
                     extra='<p style="margin-top:22px;font-weight:600;color:#000">Gratuito · presso il tuo studio · durata 1 ora e 30 minuti</p>')
    body += f'''<section class="section"><div class="wrap"><div class="contact-box">
  <div><span class="kicker">Prenotazione</span><h2 class="h2">Prenota il tuo incontro</h2><p class="lead" style="margin-top:14px">Indicaci gli argomenti che ti interessano e i giorni che preferisci: ti ricontattiamo per fissare l’appuntamento.</p>
  <ul class="contact-list"><li><a href="{TEL_HREF}">{TEL}</a></li><li><a href="mailto:{MAIL}">{MAIL}</a></li></ul></div>
  {contact_form("100% Profis", pagina="100-profis")}
</div></div></section>'''
    page('/corsi/100-profis/', '100% Profis: incontri gratuiti nel tuo studio | Sistemi Parma', 'Incontri gratuiti 100% Profis: 1 ora e 30 minuti di approfondimento sulle funzioni avanzate di Profis, direttamente nel tuo studio. Prenota online.', body, crumbs)

    # ------------------------------------------------------------ Pillole
    crumbs = [(None, 'Le Pillole')]
    pronte = [p for p in POSTS if video_src(p[0], p[3])]
    attesa = [p for p in POSTS if not video_src(p[0], p[3])]
    cards = ''.join(post_card(i, s, t, d, y, sc) for i, (s, t, d, y, _tg, sc) in enumerate(pronte))
    body = page_hero(crumbs, 'Videotutorial software Sistemi', 'Le Pillole', 'Brevi video in cui ti mostriamo come usare al meglio le funzioni dei software Sistemi: conservazione digitale, fatture elettroniche, pratiche e molto altro.')
    body += f'<section class="section"><div class="wrap"><div class="grid grid--3" style="gap:40px 24px">{cards}</div></div></section>'
    if attesa:
        cards2 = ''.join(post_card(i, s, t, d, y, sc) for i, (s, t, d, y, _tg, sc) in enumerate(attesa))
        body += f'''<section class="section section--soft"><div class="wrap">
  <div class="head-row"><h2 class="h2 js-split">In arrivo</h2><p>{"Stiamo trasferendo questa pillola" if len(attesa) == 1 else "Stiamo trasferendo queste pillole"} sul nuovo sito. Nel frattempo puoi chiedercel{"a" if len(attesa) == 1 else "e"} scrivendo a <a href="mailto:{g["MAIL"]}">{g["MAIL"]}</a>.</p></div>
  <div class="grid grid--3" style="gap:40px 24px">{cards2}</div></div></section>'''
    page('/pillole/', 'Le Pillole: videotutorial sui software Sistemi | Sistemi Parma', 'Le Pillole di Sistemi Parma: brevi videotutorial su Profis, conservazione digitale, fatture elettroniche, Sportello e altri software Sistemi.', body, crumbs)

    # ------------------------------------------------------------ Contatti
    crumbs = [(None, 'Contatti')]
    body = page_hero(crumbs, 'Sistemi Parma · Via Sicuri 42/a', 'Contatti', 'Informazioni, demo, preventivi o assistenza: scrivici o chiamaci.')
    body += f'''<section class="section"><div class="wrap"><div class="contact-box">
  <div><h2 class="h2" style="font-size:32px">Servizi Informatici Srl</h2>
    <ul class="contact-list">
      <li><a href="{MAPS}" rel="noopener" target="_blank">{ADDR}<br><span style="color:var(--red)">Apri in Mappe ↗</span></a></li>
      <li><a href="{TEL_HREF}">Tel. {TEL}</a></li>
      <li><a href="mailto:{MAIL}">{MAIL}</a></li>
      <li style="color:#5C5C5C">P.IVA 01721620340</li>
    </ul>
    <p style="margin-top:24px;font-size:15px;color:#444">Per l’assistenza sui software Sistemi è più rapido aprire un ticket dal menu del prodotto. <a href="/assistenza/">Vai all’assistenza</a>.</p></div>
  {contact_form(pagina="contatti")}
</div></div></section>'''
    page('/contatti/', 'Contatti – Sistemi Parma, Via Sicuri 42/a Parma', 'Contatta Servizi Informatici Srl (Sistemi Parma): Via Sicuri 42/a, 43124 Parma, tel. 0521 252824, info@serviziparma.com. Demo, preventivi e informazioni.', body, crumbs)

    # ------------------------------------------------------------ Grazie
    for path, title, text in [('/grazie/', 'Grazie, abbiamo ricevuto la tua richiesta', 'Ti rispondiamo il prima possibile. Se è urgente, chiamaci allo 0521 252824.'),
                              ('/grazie-iscrizione/', 'Grazie, abbiamo ricevuto la tua iscrizione', 'Ti ricontattiamo per confermare date e quota di partecipazione. La fattura arriva a parte.')]:
        body = f'''<section class="page-hero" style="min-height:60vh;display:flex;align-items:center"><div class="wrap hero-seq">
  <h1><span class="kicker">Messaggio inviato</span>{title}</h1><p class="lead">{text}</p>
  <div class="btn-row" style="margin-top:28px"><a class="btn btn--red" href="/">Torna alla home</a><a class="btn btn--line" href="/pillole/">Guarda Le Pillole</a></div></div></section>'''
        page(path, title + ' | Sistemi Parma', text, body, robots='noindex,follow')

    # ------------------------------------------------------------ 404
    body = f'''<section class="page-hero" style="min-height:64vh;display:flex;align-items:center"><div class="wrap split" style="align-items:center">
  <div class="hero-seq"><h1><span class="kicker">Errore 404</span>Questa pagina non c’è.</h1><p class="lead">Forse è stata spostata con il nuovo sito. Prova dalla home o scrivici.</p>
  <div class="btn-row" style="margin-top:28px"><a class="btn btn--red" href="/">Vai alla home</a><a class="btn btn--line" href="/contatti/">Contatti</a></div></div>
  <div><img src="/assets/img/campagna/slogan-cane-800.jpg" alt="i [software] #Sistemi sono i migliori amici del vostro {{futuro}}." width="800" height="193"></div></div></section>'''
    page('/404.html', 'Pagina non trovata | Sistemi Parma', 'La pagina cercata non esiste o è stata spostata.', body, robots='noindex,follow', current='/')

    legal(g)


def legal(g):
    page = g['page']; page_hero = g['page_hero']
    crumbs = [(None, 'Privacy policy')]
    body = page_hero(crumbs, 'Informativa ai sensi dell’art. 13 del Regolamento (UE) 2016/679', 'Privacy policy', 'Informazioni sul trattamento dei dati personali degli utenti che consultano il sito web di Servizi Informatici Srl.')
    body += '''<section class="section"><div class="wrap prose">
<p>Ai sensi del Regolamento (UE) 2016/679 (di seguito "Regolamento"), questa pagina descrive le modalità di trattamento dei dati personali degli utenti che consultano il sito web di Servizi Informatici Srl accessibile per via telematica al seguente indirizzo: <a href="https://www.serviziparma.com/">https://www.serviziparma.com/</a></p>
<p>La presente informativa è formulata anche in attuazione della Raccomandazione n. 2/2001 che il Gruppo di Lavoro Articolo 29 ha adottato il 17 maggio 2001 per individuare alcuni requisiti minimi per la raccolta di dati personali on-line, e, in particolare, le modalità, i tempi e la natura delle informazioni che i titolari del trattamento devono fornire agli utenti quando questi si collegano a pagine web, indipendentemente dagli scopi del collegamento.</p>
<p>Le presenti informazioni non riguardano altri siti, pagine o servizi online raggiungibili tramite link ipertestuali eventualmente pubblicati nel sito.</p>
<h2>Titolare del trattamento</h2>
<p>A seguito della consultazione del sito sopra indicato possono essere trattati dati relativi a persone fisiche identificate o identificabili.</p>
<p>Titolare del trattamento è Servizi Informatici Srl, con sede in via Sicuri 42/a, Parma (PR), 43124, telefono 0521 252824, e-mail <a href="mailto:info@serviziparma.com">info@serviziparma.com</a>.</p>
<h2>Base giuridica del trattamento</h2>
<p>I dati personali indicati in questa pagina sono trattati in quanto necessari al perseguimento del legittimo interesse del titolare a garantire il regolare funzionamento dei servizi web offerti e ad ottenere informazioni statistiche sulle visite e sull’uso dei servizi stessi (art. 6, par. 1, lett. f) del Regolamento) ed in quanto necessari all’esecuzione di un contratto o di misure precontrattuali (art. 6, par. 1, lett. b) del Regolamento) al fine di rispondere alle richieste inviateci e di gestire le iscrizioni ai corsi effettuate mediante l’apposito modulo.</p>
<h2>Tipi di dati trattati e finalità del trattamento</h2>
<h3>Dati di navigazione</h3>
<p>I sistemi informatici e le procedure software preposte al funzionamento di questo sito acquisiscono, nel corso del loro normale esercizio, alcuni dati personali la cui trasmissione è implicita nell’uso dei protocolli di comunicazione di Internet.</p>
<p>In questa categoria di dati rientrano gli indirizzi IP o i nomi a dominio dei computer e dei terminali utilizzati dagli utenti, gli indirizzi in notazione URI/URL (Uniform Resource Identifier/Locator) delle risorse richieste, l’orario della richiesta, il metodo utilizzato nel sottoporre la richiesta al server, la dimensione del file ottenuto in risposta, il codice numerico indicante lo stato della risposta data dal server (buon fine, errore, ecc.), alcune informazioni riguardanti la geolocalizzazione della richiesta ed altri parametri relativi al sistema operativo e all’ambiente informatico dell’utente.</p>
<p>Si tratta di informazioni che non sono raccolte con lo scopo di essere associate a interessati identificati, ma che per loro stessa natura potrebbero permettere di identificare gli utenti.</p>
<p>Tali dati, necessari per la fruizione dei servizi web, vengono anche trattati allo scopo di: ottenere informazioni statistiche sull’uso dei servizi (pagine più visitate, numero di visitatori per fascia oraria o giornaliera, aree geografiche di provenienza, ecc.); controllare il corretto funzionamento dei servizi offerti. Le statistiche sono elaborate da Netlify Analytics a partire dai log del server, senza cookie e senza script di tracciamento nel browser.</p>
<p>I dati (log-file, dati di traffico) potrebbero essere utilizzati per l’accertamento di responsabilità in caso di ipotetici reati informatici ai danni del sito, e per lo stesso motivo conservati dall’ISP (Internet Service Provider, fornitore di connettività Internet) e dal web host.</p>
<h3>Dati comunicati dall’utente</h3>
<p>L’invio facoltativo, esplicito e volontario di messaggi agli indirizzi di contatto indicati all’interno del sito comporta l’acquisizione dei dati di contatto del mittente (indirizzo e-mail) necessari a rispondere, nonché di tutti i dati personali inclusi nelle comunicazioni. Il trattamento in questione non richiede l’acquisizione del consenso dal momento che è necessario all’esecuzione di un contratto o di misure precontrattuali a richiesta dell’interessato al fine di rispondere alle richieste pervenuteci; pertanto il conferimento dei dati è da considerarsi necessario per l’esaurimento della richiesta: il mancato conferimento degli stessi comporterebbe l’impossibilità di dare seguito alla richiesta pervenutaci.</p>
<p>L’invio di messaggi non comporta l’automatica iscrizione a mailing list avente scopo promozionale o commerciale.</p>
<p>I dati così raccolti sono conservati il tempo strettamente necessario per rispondere ai messaggi. Nel caso in cui si instauri un rapporto commerciale i dati saranno conservati almeno per tutta la durata del rapporto stesso.</p>
<h3>Form di contatto</h3>
<p>La compilazione del form presente nel sito con lo scopo di richiedere informazioni comporta l’acquisizione dei dati di contatto del mittente (nome, cognome, indirizzo e-mail ed eventuali altri dati facoltativi come telefono e azienda) necessari a rispondere, nonché di tutti i dati personali inclusi nelle comunicazioni. Il trattamento in questione non richiede l’acquisizione del consenso dal momento che è necessario all’esecuzione di un contratto o di misure precontrattuali a richiesta dell’interessato al fine di rispondere alle richieste ed ai contatti commerciali pervenutici; pertanto il conferimento dei dati è da considerarsi necessario per l’esaurimento della richiesta: il mancato conferimento degli stessi comporterebbe l’impossibilità di dare seguito alla richiesta pervenutaci.</p>
<p>La compilazione del form non comporta l’automatica iscrizione a mailing list avente scopo promozionale o commerciale.</p>
<p>I dati così raccolti sono conservati il tempo strettamente necessario per rispondere ai messaggi. Nel caso in cui si instauri un rapporto commerciale i dati saranno conservati almeno per tutta la durata del rapporto stesso.</p>
<h3>Iscrizione ai corsi</h3>
<p>La compilazione del modulo di iscrizione ai corsi comporta l’acquisizione dei dati del partecipante (nome, cognome, e-mail, telefono) e dei dati necessari alla fatturazione (ragione sociale, partita IVA, codice destinatario o PEC). Il trattamento è necessario all’esecuzione di misure precontrattuali e del contratto richiesti dall’interessato (art. 6, par. 1, lett. b) del Regolamento) e all’adempimento degli obblighi contabili e fiscali (art. 6, par. 1, lett. c) del Regolamento). I dati sono conservati il tempo necessario a gestire l’iscrizione e, per i dati contabili e di fatturazione, per il tempo previsto dalla normativa.</p>
<h3>Servizi esterni aperti dai pulsanti</h3>
<p>Alcuni pulsanti del sito aprono servizi di terzi, che trattano i dati secondo le proprie informative: l’iscrizione agli eventi gratuiti tramite Eventbrite (lo script di Eventbrite viene caricato solo quando si preme il pulsante di iscrizione), il portale di assistenza Sistemi, i siti di download di TeamViewer e AnyDesk e Google Maps per le indicazioni stradali. I video del sito sono ospitati sul sito stesso.</p>
<h2>Destinatari dei dati</h2>
<p>I dati di navigazione sono conservati dall’ISP (Internet Service Provider) e dal web host (soggetto che ospita il server web su proprie macchine fisiche) i quali li conservano secondo i tempi previsti dalla normativa.</p>
<p>I dati personali raccolti a seguito di ricezione di messaggi e contatti tramite i form sono altresì trattati dal personale interno autorizzato dal Titolare, che agisce sulla base di specifiche istruzioni fornite in ordine a finalità e modalità del trattamento medesimo.</p>
<p>Non viene effettuata profilazione ed i dati raccolti non sono oggetto di processi decisionali automatizzati.</p>
<p>Il sito è ospitato da Netlify, Inc., che agisce in qualità di responsabile del trattamento e riceve anche i dati inviati tramite i moduli (Netlify Forms). I server possono essere posizionati sia all’interno dell’Unione Europea sia al di fuori dell’Unione Europea (ad esempio negli Stati Uniti), e pertanto anche le informazioni personali dei visitatori possono essere conservate in questi paesi. I trasferimenti di dati al di fuori dell’Unione Europea vengono effettuati garantendo un adeguato livello di protezione, sulla base delle Clausole Contrattuali Standard approvate dalla Commissione Europea. A questo link è possibile consultare l’accordo sul trattamento dei dati: <a href="https://www.netlify.com/pdf/netlify-dpa.pdf" rel="noopener" target="_blank">https://www.netlify.com/pdf/netlify-dpa.pdf</a>.</p>
<p>A questo link è invece possibile consultare la policy sui dati personali: <a href="https://www.netlify.com/privacy/" rel="noopener" target="_blank">https://www.netlify.com/privacy/</a>.</p>
<h2>Diritti degli interessati e diritto di reclamo</h2>
<p>Gli interessati hanno il diritto di ottenere dal Titolare, nei casi previsti, l’accesso ai propri dati personali e la rettifica o la cancellazione degli stessi o la limitazione del trattamento che li riguarda o di opporsi al trattamento, oltre al diritto alla portabilità dei dati (artt. da 15 a 22 del Regolamento).</p>
<p>Gli interessati che ritengono che il trattamento dei dati personali a loro riferiti effettuato attraverso questo sito avvenga in violazione di quanto previsto dal Regolamento hanno il diritto di proporre reclamo ad un’autorità di vigilanza (ad esempio il Garante per la protezione dei dati personali), come previsto dall’art. 77 del Regolamento stesso, o di adire le opportune sedi giudiziarie (art. 79 del Regolamento).</p>
<p>Le richieste relative agli articoli sopra citati devono essere inoltrate al Titolare del trattamento utilizzando i contatti indicati in testa al presente documento informativo.</p>
<h2>Note legali</h2>
<h3>A) Disclaimer</h3>
<p>L’utente riconosce ed accetta che l’uso di questo sito è a suo esclusivo rischio e pericolo. L’utente accetta che il sito e tutti i suoi contenuti, ivi compresi i servizi eventualmente offerti, sono forniti "così come sono" e "con tutti gli errori".</p>
<p>La nostra azienda pertanto non rilascia alcun tipo di garanzia, esplicita o implicita, riguardo tali contenuti, ivi compresi, senza alcuna limitazione, la liceità, il diritto di proprietà, la convenienza o l’adeguatezza a particolari scopi o usi.</p>
<p>La nostra azienda non garantisce che il sito sia compatibile con le apparecchiature dell’utente o che sia privo di errori o virus, bachi o "cavalli di Troia". La nostra azienda non è responsabile per i danni subiti dall’utente a causa di tali elementi di carattere distruttivo.</p>
<p>L’utente riconosce e accetta che la nostra azienda, i suoi collaboratori o i suoi fornitori non sono responsabili:</p>
<ol><li>per i danni causati da negligenze di questa azienda, dei suoi collaboratori, subappaltatori, fornitori o per i danni comunque derivanti da questo sito, nonché per i mancati guadagni, per le perdite, per i danni incidentali o consequenziali o per qualsiasi altro danno parziale o totale, diretto o indiretto;</li>
<li>per disfunzioni nell’utilizzazione dei materiali o dei servizi di questo sito causate dal computer o dalle apparecchiature dell’utente.</li></ol>
<p>La nostra azienda non è in alcun modo responsabile dei contenuti e dei servizi posti in siti web a cui doveste accedere tramite il presente sito.</p>
<p>Quando accedete ad un altro sito web, ricordate che esso è indipendente dal presente sito e che quest’ultimo non ha alcun controllo sul contenuto del sito in questione. Inoltre l’esistenza di un collegamento ipertestuale (link) verso un altro sito non comporta l’approvazione o un’accettazione di responsabilità, neanche parziale e/o indiretta, da parte della nostra azienda circa il contenuto o l’utilizzazione del sito.</p>
<p>La nostra azienda inoltre non è responsabile in alcun modo per la bontà dei servizi di connettività da voi utilizzati per connettervi alla rete e raggiungere il sito e fruire dei servizi nello stesso accessibili.</p>
<p>La nostra azienda non può in alcun modo essere ritenuta responsabile per la disponibilità continua delle linee telefoniche e delle apparecchiature che l’utente utilizza per accedere al presente sito.</p>
<p>La nostra azienda si riserva il diritto di inibire o proibire o sospendere, in qualsiasi momento e senza preavviso, l’accesso al presente sito ed ai relativi servizi.</p>
<h3>B) Limitazione di responsabilità</h3>
<p>In nessuna circostanza, ivi compresa, senza alcuna limitazione, la negligenza, la nostra azienda, i suoi fornitori o i collaboratori potranno essere ritenuti responsabili per qualsiasi danno diretto, indiretto, incidentale, consequenziale, legato all’uso del presente sito web o di altri siti web ad esso collegati da un link ipertestuale, ivi compresi senza alcuna limitazione i danni quali la perdita di profitti o fatturato, l’interruzione di attività aziendale o professionale, la perdita di programmi o altro tipo di dati ubicati sul sistema informatico dell’utente o altro sistema, e ciò anche qualora la nostra azienda fosse stata espressamente messa al corrente della possibilità del verificarsi di tali danni. La presente clausola di esclusione della responsabilità non ha lo scopo di eludere il rispetto dei requisiti prescritti dalla normativa vigente, né di escludere la responsabilità per i casi nei quali essa non possa essere esclusa ai sensi della normativa applicabile.</p>
<h3>C) Copyright</h3>
<p>I contenuti del sito – codice di script, grafica, testi, tabelle, immagini, suoni, e ogni altra informazione disponibile in qualunque forma – sono protetti ai sensi della normativa in tema di opere dell’ingegno.</p>
<p>Ogni prodotto o società menzionati in questo sito sono marchi dei rispettivi proprietari o titolari e possono essere protetti da brevetti e/o copyright concessi o registrati dalle autorità preposte. I marchi e i loghi dei prodotti Sistemi e le illustrazioni della campagna Sistemi appartengono a Sistemi SpA.</p>
<p>Per fini di lucro è consentito utilizzare, copiare e distribuire i documenti e le relative immagini disponibili su questo sito solo dietro permesso scritto (o egualmente valido a fini legali) della nostra azienda, fatte salve eventuali spettanze di diritto. Le note di copyright, gli autori ove indicati o la fonte stessa devono in tutti i casi essere citati nelle pubblicazioni in qualunque forma realizzate e diffuse.</p>
<p>Qualsiasi forma di link al presente sito, se inserita da soggetti terzi, non deve recare danno all’immagine ed alle attività della nostra azienda.</p>
<p>È vietato il cd. deep linking ossia l’utilizzo non trasparente, su siti di soggetti terzi, di parti del sito.</p>
<p>L’eventuale inosservanza delle presenti disposizioni, salvo esplicita autorizzazione scritta, sarà perseguita nelle competenti sedi giudiziarie civili e penali.</p>
<p class="note">Ultimo aggiornamento: novembre 2026.</p>
</div></section>'''
    page('/privacy-policy/', 'Privacy policy | Sistemi Parma – Servizi Informatici Srl', 'Informativa sul trattamento dei dati personali degli utenti del sito di Servizi Informatici Srl ai sensi dell’art. 13 del Regolamento (UE) 2016/679.', body, crumbs)

    crumbs = [(None, 'Cookie policy')]
    body = page_hero(crumbs, 'Cookie e strumenti di tracciamento', 'Cookie policy', 'Questo sito non usa cookie né script di tracciamento: per questo non trovi nessun banner.')
    body += '''<section class="section"><div class="wrap prose">
<p>L’informativa di seguito riportata, relativa all’uso di cookie ed altre tecnologie traccianti l’attività dell’utente nel web, è resa all’utente/navigatore ad integrazione della <a href="/privacy-policy/">privacy policy</a> e in attuazione della Raccomandazione n. 2/2001 che il Gruppo di Lavoro art. 29 ha adottato il 17 maggio 2001 per individuare alcuni requisiti minimi per la raccolta di dati personali on-line, e, in particolare, le modalità, i tempi e la natura delle informazioni che i titolari del trattamento devono fornire agli utenti quando questi si collegano a pagine web, indipendentemente dagli scopi del collegamento, nonché nel rispetto dell’art. 13 del Regolamento UE 2016/679 (GDPR).</p>
<p>Il Titolare del trattamento è Servizi Informatici Srl, con sede in via Sicuri 42/a, Parma (PR), 43124, telefono 0521 252824, e-mail <a href="mailto:info@serviziparma.com">info@serviziparma.com</a>.</p>
<p>Le presenti informazioni non riguardano altri siti, pagine o servizi online raggiungibili tramite link ipertestuali eventualmente pubblicati nel sito.</p>
<h2>Che cosa sono i cookie?</h2>
<p>I cookie sono stringhe di testo di piccola dimensione che un sito web può inviare ed installare, durante la navigazione, sul dispositivo dell’utente, al fine di memorizzare alcune informazioni riguardanti l’utente stesso; queste informazioni saranno poi ritrasmesse al server web che ospita il sito ai successivi accessi.</p>
<h2>A cosa servono i cookie?</h2>
<p>I cookie sono usati per differenti finalità: per eseguire autenticazioni informatiche (per accedere ad esempio all’account personale), monitorare le sessioni e preservare le impostazioni dell’utente nel passaggio da una pagina web ad un’altra (ricordando ad esempio la lingua di visualizzazione del sito), memorizzare informazioni su specifiche configurazioni riguardanti gli utenti che accedono al server web, memorizzare le preferenze di navigazione, raccogliere dati statistici anonimi (per monitorare ad esempio gli accessi al sito), fare marketing.</p>
<p>I cookie si possono dividere innanzitutto in due grandi categorie, riguardanti il profilo soggettivo: cookie di prima parte, installati dal gestore del sito che l’utente sta visitando, e cookie di terze parti, installati da servizi diversi (ad esempio Google, Facebook, ecc.).</p>
<p>Riguardo il profilo temporale invece abbiamo i cookie di sessione, che vengono automaticamente cancellati alla chiusura del browser, e i cookie persistenti, che invece permangono fino alla scadenza prestabilita.</p>
<p>Infine i cookie possono essere suddivisi in cookie tecnici o necessari, necessari alla navigazione del sito web al fine di garantire il servizio; cookie analytics o statistici, utilizzati dai gestori dei siti web per raccogliere informazioni sul numero degli utenti e su come questi visitano il sito stesso; cookie di profilazione o di marketing, utilizzati per ricondurre a soggetti determinati, identificati o identificabili, specifiche azioni o schemi comportamentali ricorrenti al fine di creare profili e inviare messaggi pubblicitari mirati.</p>
<p>Al fine della loro installazione e del loro utilizzo i cookie tecnici non richiedono il consenso dell’utente, mentre i cookie di profilazione, sia di prima sia di terze parti, possono essere utilizzati solo previo consenso da parte dell’utente; i cookie analytics o statistici infine sono paragonati ai cookie tecnici solo se raccolgono dati anonimi, in caso contrario sono anch’essi sottoposti al previo consenso da parte dell’utente.</p>
<h2>Che tipo di cookie utilizza questo sito?</h2>
<p><b>Questo sito non installa cookie</b>, né tecnici né statistici né di profilazione, e non usa altri strumenti di tracciamento nel browser (pixel, fingerprinting, archiviazione locale a fini di tracciamento). Per questo motivo non è presente alcun banner per il consenso.</p>
<p>Le statistiche sulle visite sono elaborate da Netlify Analytics a partire dai log del server che ospita il sito (vedi la sezione "Dati di navigazione" della <a href="/privacy-policy/">privacy policy</a>), senza scrivere nulla sul dispositivo dell’utente.</p>
<p>Alcuni pulsanti aprono servizi di terzi, che possono installare i propri cookie solo dopo che l’utente li ha attivati: il modulo di iscrizione di Eventbrite agli eventi gratuiti (lo script viene caricato soltanto al clic sul pulsante di iscrizione), il portale di assistenza Sistemi, i siti di download di TeamViewer e AnyDesk e Google Maps. Per questi servizi valgono le rispettive informative.</p>
<h2>Disattivazione dei cookie sul browser</h2>
<p>Ogni utente può configurare il proprio browser in modo da non accettare automaticamente cookie. È possibile eliminare tutti i cookie installati all’interno del browser o bloccarne l’installazione di nuovi. Per ottenere le istruzioni specifiche per ogni tipologia di browser seleziona uno dei link seguenti:</p>
<ul>
<li>Safari: <a href="https://support.apple.com/it-it/guide/safari/sfri11471/mac" rel="noopener" target="_blank">support.apple.com</a></li>
<li>Chrome: <a href="https://support.google.com/accounts/answer/61416?hl=it" rel="noopener" target="_blank">support.google.com</a></li>
<li>Firefox: <a href="https://support.mozilla.org/it/kb/Attivare%20e%20disattivare%20i%20cookie" rel="noopener" target="_blank">support.mozilla.org</a></li>
<li>Edge: <a href="https://support.microsoft.com/it-it/microsoft-edge" rel="noopener" target="_blank">support.microsoft.com</a></li>
</ul>
<p>È possibile infine attivare l’opzione "Do Not Track", presente nella maggior parte dei browser di ultima generazione. I siti web progettati in modo da rispettare questa opzione, quando viene attivata, dovrebbero automaticamente smettere di raccogliere alcuni dati di navigazione. Non tutti i siti web, tuttavia, sono impostati in modo da rispettare questa opzione.</p>
<h2>Diritti degli interessati e diritto di reclamo</h2>
<p>Gli interessati hanno il diritto di ottenere dal Titolare, nei casi previsti, l’accesso ai propri dati personali e la rettifica o la cancellazione degli stessi o la limitazione del trattamento che li riguarda o di opporsi al trattamento, oltre al diritto alla portabilità dei dati (artt. da 15 a 22 del Regolamento).</p>
<p>Gli interessati che ritengono che il trattamento dei dati personali a loro riferiti effettuato attraverso questo sito avvenga in violazione di quanto previsto dal Regolamento hanno il diritto di proporre reclamo ad un’autorità di vigilanza (ad esempio il Garante per la protezione dei dati personali), come previsto dall’art. 77 del Regolamento stesso, o di adire le opportune sedi giudiziarie (art. 79 del Regolamento).</p>
<p>Le richieste relative agli articoli sopra citati possono essere inoltrate al Titolare del trattamento utilizzando i contatti indicati in testa al presente documento informativo.</p>
<p class="note">Ultimo aggiornamento: novembre 2026.</p>
</div></section>'''
    page('/cookie-policy/', 'Cookie policy | Sistemi Parma – Servizi Informatici Srl', 'Cookie policy del sito di Servizi Informatici Srl: il sito non usa cookie né strumenti di tracciamento; statistiche dai log del server con Netlify Analytics.', body, crumbs)
