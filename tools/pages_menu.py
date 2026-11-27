"""Menù di Sala: la pagina che lo racconta e lo vende."""

APP = 'https://menu-di-sala-production.up.railway.app/nuovo'


def telefono_svg():
    """Il telefono con dentro un menù vero. Disegnato, non fotografato: una
    schermata finta fatta di rettangoli resta nitida a ogni dimensione e non
    invecchia il giorno che cambiamo una spaziatura nell'app."""
    piatti = [
        ('Culatello di Zibello', '16,00'),
        ('Torta fritta e salumi', '14,00'),
        ('Tortelli d’erbetta', '13,00'),
        ('Tagliatelle al ragù', '12,50'),
    ]
    righe = ''
    y = 220
    for nome, prezzo in piatti:
        righe += f'''
    <text x="38" y="{y}" class="mn-p">{nome}</text>
    <text x="282" y="{y}" class="mn-e" text-anchor="end">{prezzo} €</text>
    <line x1="38" y1="{y + 16}" x2="282" y2="{y + 16}" class="mn-l"/>'''
        y += 46
    return f'''<svg class="fone" viewBox="0 0 320 620" role="img"
     aria-label="Un telefono che mostra il menù di una trattoria con i prezzi e il filtro per gli allergeni">
  <defs><clipPath id="mn-sch"><rect x="12" y="12" width="296" height="596" rx="30"/></clipPath></defs>
  <rect x="2" y="2" width="316" height="616" rx="42" fill="#141414"/>
  <rect x="12" y="12" width="296" height="596" rx="30" fill="#FBF8F4"/>
  <g clip-path="url(#mn-sch)">
    <circle cx="160" cy="70" r="26" fill="#C20E1A"/>
    <text x="160" y="79" class="mn-i" text-anchor="middle">T</text>
    <text x="160" y="128" class="mn-t" text-anchor="middle">TRATTORIA DEL BORGO</text>
    <text x="160" y="150" class="mn-s" text-anchor="middle">Parma</text>
    <rect x="38" y="166" width="244" height="26" rx="6" fill="#C20E1A"/>
    <text x="160" y="184" class="mn-c" text-anchor="middle">ANTIPASTI E PRIMI</text>
    {righe}
    <rect x="38" y="418" width="244" height="46" rx="23" fill="#fff" stroke="#DDD8D5" stroke-width="1.5"/>
    <text x="160" y="447" class="mn-f" text-anchor="middle">Filtra per allergeni</text>
    <rect x="38" y="482" width="244" height="104" rx="16" fill="#fff" stroke="#DDD8D5" stroke-width="1.5"/>
    <text x="56" y="512" class="mn-s">Senza quali ingredienti?</text>
    <rect x="56" y="526" width="78" height="30" rx="15" fill="#C20E1A"/>
    <text x="95" y="546" class="mn-g" text-anchor="middle">Glutine</text>
    <rect x="142" y="526" width="62" height="30" rx="15" fill="#F1EEEC"/>
    <text x="173" y="546" class="mn-h" text-anchor="middle">Latte</text>
    <rect x="212" y="526" width="52" height="30" rx="15" fill="#F1EEEC"/>
    <text x="238" y="546" class="mn-h" text-anchor="middle">Uova</text>
  </g>
</svg>'''


def segnaposto_svg():
    """Il segnaposto 8×5 come esce dalla stampante: logo e nome a sinistra,
    il QR a destra, come nel PDF vero."""
    import hashlib
    # Un reticolo che somiglia a un QR senza esserlo: è un disegno, non un
    # codice, e nessuno deve provare a inquadrarlo.
    semi = hashlib.sha256(b'menu di sala').digest() * 10
    lato, x0, y0 = 8, 198, 46
    celle = ''
    n = 0
    for r in range(13):
        for c in range(13):
            if (r < 4 and c < 4) or (r < 4 and c > 8) or (r > 8 and c < 4):
                continue
            if semi[n % len(semi)] & 1:
                celle += f'<rect x="{x0 + c * lato}" y="{y0 + r * lato}" width="{lato}" height="{lato}"/>'
            n += 1
    mirino = ''
    for mx, my in ((x0, y0), (x0 + 9 * lato, y0), (x0, y0 + 9 * lato)):
        m = lato * 4
        mirino += (f'<rect x="{mx}" y="{my}" width="{m}" height="{m}"/>'
                   f'<rect x="{mx + lato * .7:.0f}" y="{my + lato * .7:.0f}" '
                   f'width="{m - lato * 1.4:.0f}" height="{m - lato * 1.4:.0f}" fill="#fff"/>'
                   f'<rect x="{mx + lato * 1.4:.0f}" y="{my + lato * 1.4:.0f}" '
                   f'width="{m - lato * 2.8:.0f}" height="{m - lato * 2.8:.0f}"/>')
    return f'''<svg class="carta" viewBox="0 0 340 215" role="img"
     aria-label="Il segnaposto da tavolo otto per cinque centimetri, con il logo del locale e il QR">
  <rect x="4" y="4" width="332" height="207" rx="10" fill="#fff" stroke="#DDD8D5" stroke-width="2"/>
  <circle cx="58" cy="58" r="24" fill="#C20E1A"/>
  <text x="58" y="67" class="mn-i" text-anchor="middle">T</text>
  <text x="34" y="110" class="cr-n">Trattoria</text>
  <text x="34" y="131" class="cr-n">del Borgo</text>
  <text x="34" y="170" class="cr-s">Inquadra per il menù</text>
  <text x="34" y="187" class="cr-m">Menù di Sala</text>
  <g fill="#141414">{mirino}{celle}</g>
</svg>'''


def build(g):
    page = g['page']; page_hero = g['page_hero']; cta_band = g['cta_band']
    faq_html = g['faq_html']; faq_ld = g['faq_ld']; icon_tile = g['icon_tile']; SITE = g['SITE']

    passi = [
        ('camera', 'Fotografi il menù che hai già',
         'Con il telefono, una pagina per volta. Va bene anche il PDF, o il testo incollato. '
         'Il nostro software lo legge e ne ricava piatti, descrizioni e prezzi: non devi riscrivere niente.'),
        ('sparkles', 'Scegli come si veste',
         'Ti proponiamo tre grafiche costruite sul tuo logo e sul tipo di locale: '
         'la carta avorio del ristorante classico, il nero del pub, il bianco del bistrot. '
         'Ne scegli una e la cambi quando vuoi.'),
        ('qr', 'Stampi il QR e sei in sala',
         'Ti diamo il QR in PNG, il cartoncino A5 e il segnaposto 8×5 cm col tuo logo, '
         'già pronto su un foglio A4 da dieci con le righe per tagliarli.'),
    ]
    passi_html = ''.join(f'''
  <article class="card reveal">
    <span class="card__word">{i + 1}</span>
    <h3>{t}</h3>
    <p>{d}</p>
  </article>''' for i, (_ic, t, d) in enumerate(passi))

    dentro = [
        ('Il menù lo legge il software',
         'Foto o PDF: ne tira fuori categorie, piatti e prezzi. Quello che non è chiaro te lo segna, '
         'perché tu lo controlli prima di pubblicare.'),
        ('Il filtro degli allergeni',
         'Il cliente spunta i suoi e vede subito cosa può mangiare, sui quattordici allergeni di legge. '
         'Mettiamo solo quello che dichiari tu: non li indoviniamo dal nome del piatto, '
         'perché è una responsabilità tua e di chi legge il menù può esserne allergico davvero.'),
        ('Il QR non cambia mai',
         'Cambi i piatti, i prezzi, la grafica: il codice sui tavoli resta quello. '
         'Si stampa una volta sola.'),
        ('Segni cosa è finito',
         'Un tocco e il piatto resta scritto ma barrato. Il cliente lo sa prima di chiederlo, '
         'e nessuno deve spiegarlo al tavolo.'),
        ('Il menù in altre lingue',
         'Inglese, francese, tedesco, e altre otto. La traduzione la propone il software e la correggi tu, '
         'che sui piatti di casa è l’unico modo per non dire sciocchezze.'),
        ('Nessuna app per il cliente',
         'Inquadra il QR con la fotocamera e legge. Niente da scaricare, niente registrazione, '
         'niente dati da lasciare.'),
    ]
    dentro_html = ''.join(f'''
  <article class="card reveal">
    {icon_tile('check')}
    <h3>{t}</h3>
    <p>{d}</p>
  </article>''' for t, d in dentro)

    confronto = [
        ('Cambiare un prezzo', 'Lo cambi dal telefono: in sala si vede subito.',
         'Rifai il file, lo ricarichi, e speri che il QR punti ancora dove deve.'),
        ('Un piatto finito', 'Lo segni esaurito in un tocco.', 'Niente da fare: lo dici a voce, tavolo per tavolo.'),
        ('Allergeni', 'Il cliente spunta i suoi e vede cosa può mangiare.',
         'Una riga di sigle in fondo alla pagina, da decifrare.'),
        ('Da leggere sul telefono', 'Scritto per lo schermo: si legge senza ingrandire.',
         'Un A4 da allargare con due dita, cercando la riga.'),
        ('Altre lingue', 'Il cliente sceglie la sua e il menù cambia.', 'Un file per lingua, e un QR per file.'),
        ('Quanto costa cambiare', 'Niente: lo fai tu, quando vuoi.', 'Il tempo di chi lo rifà, ogni volta.'),
    ]
    righe_conf = ''.join(f'''
    <tr><th scope="row">{c}</th>
      <td data-label="Con Menù di Sala">{a}</td>
      <td data-label="Con un PDF appeso al QR">{b}</td></tr>''' for c, a, b in confronto)

    faqs = [
        ('Il cliente deve scaricare un’app?',
         'No. Inquadra il QR con la fotocamera del telefono e il menù si apre nel browser, come una pagina qualsiasi. '
         'Non deve registrarsi e non lascia dati.'),
        ('Devo riscrivere tutto il menù?',
         'No. Lo fotografi con il telefono, una pagina per volta, oppure carichi il PDF che hai già. '
         'Il software lo legge e ti presenta piatti e prezzi da controllare.'),
        ('Se cambio un prezzo devo ristampare il QR?',
         'No, mai. Il QR punta al tuo indirizzo e quello non cambia: cambia il menù che ci trovi dietro. '
         'È la differenza principale rispetto a un PDF appeso a un QR.'),
        ('Quanto ci metto davvero?',
         'Dalla foto al QR stampabile si fa in cinque minuti. Il tempo in più lo passi a rileggere i piatti, '
         'che conviene fare con calma: i prezzi li vedono i clienti.'),
        ('Come funzionano gli allergeni?',
         'Nel menù finisce solo quello che dichiari tu. Non deduciamo un allergene dal nome del piatto, '
         'nemmeno quando sembra ovvio: la dichiarazione è tua, e chi legge può essere allergico sul serio. '
         'Se il tuo menù non porta gli allergeni, il filtro non compare affatto.'),
        ('Posso avere il menù in inglese?',
         'Sì, e in altre dieci lingue. Ogni lingua costa 2 € + IVA al mese. La traduzione te la propone il software, '
         'tu la correggi: sui piatti di casa è l’unico modo per non far ridere i clienti stranieri.'),
        ('Come si paga e come si disdice?',
         'Con carta, mensile o annuale, rinnovo automatico. Si disdice quando vuoi: il menù resta online '
         'fino alla fine del periodo già pagato e non ti chiediamo perché.'),
        ('Se mi blocco, chi mi aiuta?',
         'Noi: Servizi Informatici Srl, in Via Sicuri 42/a a Parma, al telefono 0521 252824. '
         'Non un modulo di contatto che risponde fra tre giorni.'),
    ]

    crumbs = [(None, 'Menù di Sala')]
    body = page_hero(
        crumbs,
        'Menù digitale con QR per ristoranti, bar e trattorie',
        'Il tuo menù sul telefono dei clienti. Pronto in cinque minuti.',
        'Fotografi il menù che hai già, scegli come vestirlo, e ti diamo il QR da mettere sui tavoli. '
        'Poi lo cambi quando vuoi — prezzi, piatti, quello che è finito — e il QR resta sempre lo stesso.',
        extra=f'''<div class="btn-row">
      <a class="btn btn--red" href="{APP}" rel="noopener">Ottieni subito il tuo QR code</a>
      <a class="btn btn--line" href="#prezzi">Quanto costa</a>
    </div>''')

    body += f'''
<section class="facts" aria-label="In breve"><div class="wrap facts__in">
  <div class="reveal"><b>Tutto dal telefono</b>lo fai e lo gestisci dal cellulare</div>
  <div class="reveal reveal-d1"><b>Pronto in 5 minuti</b>dalla foto del menù al QR</div>
  <div class="reveal reveal-d2"><b>Lo modifichi quando vuoi</b>e in sala si vede subito</div>
  <div class="reveal reveal-d3"><b>Disdici quando vuoi</b>nessun vincolo, nessuna penale</div>
</div></section>

<section class="section"><div class="wrap split split--art" style="align-items:center">
  <div>
    <h2 class="h2 js-split">Ecco cosa vede chi si siede al tuo tavolo</h2>
    <p class="lead" style="margin-top:16px">Il menù è scritto per lo schermo di un telefono, non è un foglio
      rimpicciolito: si legge senza ingrandire, anche in una sala poco illuminata.</p>
    <ul class="list-check" style="margin-top:20px">
      <li>I piatti nell’ordine che decidi tu, con i prezzi a destra</li>
      <li>Il filtro degli allergeni, se il tuo menù li dichiara</li>
      <li>Quello che è finito resta scritto, ma barrato</li>
      <li>La veste grafica costruita sul tuo logo</li>
    </ul>
    <div class="btn-row" style="margin-top:24px">
      <a class="btn btn--red" href="{APP}" rel="noopener">Ottieni subito il tuo QR code</a>
    </div>
  </div>
  <div class="art-box reveal">{telefono_svg()}</div>
</div></section>

<section class="section section--soft"><div class="wrap">
  <h2 class="h2 js-split" style="margin-bottom:28px">Come si fa</h2>
  <div class="grid grid--3">{passi_html}</div>
</div></section>

<section class="section"><div class="wrap split split--art" style="align-items:center">
  <div class="art-box reveal">{segnaposto_svg()}</div>
  <div>
    <h2 class="h2 js-split">Il QR arriva già pronto da stampare</h2>
    <p class="lead" style="margin-top:16px">Appena attivi il menù ti mandiamo per email il QR in tre formati:
      l’immagine, il cartoncino A5 da leggio, e il segnaposto 8×5 cm con il tuo logo — su un foglio A4 ne trovi
      dieci, con le righe per tagliarli.</p>
    <p style="margin-top:14px">Un consiglio che nessuno segue mai: stampane uno e provalo in sala,
      prima di farne cento.</p>
  </div>
</div></section>

<section class="section section--soft"><div class="wrap">
  <h2 class="h2 js-split" style="margin-bottom:12px">Non è un PDF appeso a un QR</h2>
  <p class="lead" style="margin-bottom:28px">La differenza non si vede il primo giorno. Si vede la prima volta
    che devi cambiare un prezzo.</p>
  <div class="table-wrap reveal"><table class="compare">
    <thead><tr><th></th><th>Con Menù di Sala</th><th>Con un PDF appeso al QR</th></tr></thead>
    <tbody>{righe_conf}</tbody>
  </table></div>
</div></section>

<section class="section"><div class="wrap">
  <h2 class="h2 js-split" style="margin-bottom:28px">Cosa c’è dentro</h2>
  <div class="grid grid--3">{dentro_html}</div>
</div></section>

<section class="section section--soft" id="prezzi"><div class="wrap">
  <h2 class="h2 js-split" style="margin-bottom:12px">Quanto costa</h2>
  <p class="lead" style="margin-bottom:28px">Un prezzo solo, tutto compreso. Nessun costo di attivazione,
    nessuna percentuale sugli incassi, nessun numero di tavoli da dichiarare.</p>
  <div class="table-wrap reveal"><table class="compare">
    <thead><tr><th></th><th>Mensile</th><th>Annuale</th></tr></thead>
    <tbody>
      <tr><th scope="row">Canone</th>
        <td data-label="Mensile"><b>15 €</b> + IVA al mese</td>
        <td data-label="Annuale"><b>120 €</b> + IVA all’anno</td></tr>
      <tr><th scope="row">Quanto ti addebitiamo</th>
        <td data-label="Mensile">18,30 € al mese</td>
        <td data-label="Annuale">146,40 € all’anno</td></tr>
      <tr><th scope="row">Quanto risparmi</th>
        <td data-label="Mensile">—</td>
        <td data-label="Annuale">60 € l’anno: quattro mesi in regalo</td></tr>
      <tr><th scope="row">Attivazione</th>
        <td data-label="Mensile">Nessuna</td><td data-label="Annuale">Nessuna</td></tr>
      <tr><th scope="row">Disdetta</th>
        <td data-label="Mensile">Quando vuoi</td><td data-label="Annuale">Quando vuoi</td></tr>
      <tr><th scope="row">Lingua aggiuntiva</th>
        <td data-label="Mensile">2 € + IVA al mese</td>
        <td data-label="Annuale">24 € + IVA all’anno</td></tr>
    </tbody>
  </table></div>
  <p class="note" style="margin-top:18px">Nel canone: il menù online, il filtro degli allergeni, il QR nei tre
    formati, le modifiche quante vuoi e l’assistenza di una persona che risponde al telefono.</p>
  <div class="btn-row" style="margin-top:26px">
    <a class="btn btn--red" href="{APP}" rel="noopener">Ottieni subito il tuo QR code</a>
    <a class="btn btn--line" href="/contatti/#modulo">Parlane con noi</a>
  </div>
</div></section>

{faq_html(faqs)}

{cta_band('Il tuo menù è già pronto: è quello che hai in mano.',
          'Fotografalo, guarda come diventa, e decidi dopo. Per vedere le tre proposte grafiche non serve pagare '
          'niente e non serve lasciare una carta.',
          APP, 'Ottieni subito il tuo QR code', ('/contatti/#modulo', 'Chiamaci invece'))}
'''

    ld = [faq_ld(faqs), {
        "@context": "https://schema.org", "@type": "Product",
        "name": "Menù di Sala",
        "description": "Menù digitale con QR code per ristoranti, bar e trattorie: "
                       "il menù si legge dal telefono del cliente, si modifica in qualunque momento "
                       "e il QR resta sempre lo stesso.",
        "brand": {"@type": "Brand", "name": "Sistemi Parma"},
        "offers": [
            {"@type": "Offer", "name": "Mensile", "price": "15.00", "priceCurrency": "EUR",
             "url": SITE + "/menu/", "availability": "https://schema.org/InStock"},
            {"@type": "Offer", "name": "Annuale", "price": "120.00", "priceCurrency": "EUR",
             "url": SITE + "/menu/", "availability": "https://schema.org/InStock"},
        ],
    }]

    page('/menu/',
         'Menù digitale con QR per ristoranti a Parma | Menù di Sala',
         'Il menù del tuo locale sul telefono dei clienti: lo fotografi, scegli la grafica e stampi il QR. '
         'Lo modifichi quando vuoi, il QR resta lo stesso. 15 € + IVA al mese, disdici quando vuoi.',
         body, crumbs, ld)
