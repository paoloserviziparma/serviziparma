# Sito Sistemi Parma – Servizi Informatici Srl

Sito statico (HTML/CSS/JS, nessun framework) di www.serviziparma.com, pubblicato su Netlify da questo repository.

## Struttura
- `/` home · `/professionisti/` (Profis, Studio, Job) e `/aziende/` (Quadra, Profis AZ, Spring, eSolver, PeopleLink) · `/aziende/verticali/`
- `/corsi/` (corsi in aula, 100% Profis, eventi gratuiti) · `/pillole/` (blog video)
- `/assistenza/` · `/whistleblowing/` · `/siti-web/` · `/contatti/`
- `/privacy-policy/` · `/cookie-policy/` · `/grazie/` · `/grazie-iscrizione/` · `404.html`
- `assets/` css, js, font (Montserrat, licenza OFL, in locale), immagini, video
- `netlify.toml` redirect 301 dai vecchi indirizzi Wix, intestazioni di sicurezza, cache
- `sitemap.xml`, `robots.txt`, `llms.txt`

## Come si modificano le pagine
Le pagine HTML sono generate da `tools/gen.py` e `tools/pages_main.py` (Python 3, nessuna dipendenza).
Dopo ogni modifica a testi, CSS o JS:

    python3 tools/gen.py

Lo script riscrive tutte le pagine, la sitemap e aggiorna il numero di versione `?v=` di CSS e JS.
Netlify non esegue nessuna build: pubblica i file così come sono.

## Link al sito Sistemi
I prodotti sono descritti nel dizionario `P` di `tools/gen.py`; `cat` decide se la pagina
finisce sotto `/professionisti/` o `/aziende/`, `logo` è il nome del file in
`assets/img/prodotti/` (se manca, come per PeopleLink, al suo posto va l'illustrazione
della campagna indicata da `camp`). Ogni prodotto ha inoltre:
- `sito=` la pagina ufficiale su sistemi.com (pulsante nella fascia finale e `sameAs` nei dati strutturati);
- `schede=` l'elenco delle schede PDF, come coppie (titolo, nome del file in
  `https://www.sistemi.com/downloads/`). La prima è anche il pulsante "Scheda PDF" nell'intestazione.

Attenzione ai nomi dei file: non seguono una regola unica (es. `eSOLVER-scheda.pdf` con la e
minuscola ma `ESOLVER-Produzione-manifatturiera_scheda.pdf` maiuscolo). Prima di aggiungerne uno,
conviene aprirlo nel browser per controllare che risponda.

## Moduli (Netlify Forms)
- `contatti`: home, contatti, 100% Profis (campo nascosto `pagina`)
- `iscrizione-corso`: pagine dei corsi, con i dati per la fattura (la fattura è emessa a parte)
Entrambi hanno honeypot, campo nascosto `lingua` e privacy obbligatoria. Le notifiche email si impostano nel pannello Netlify (Forms → Notifications).

## Le Pillole (video)
Ogni pillola è una riga dell'elenco `POSTS` in `tools/gen.py`:
`(slug, titolo, data, id-del-video-YouTube o None, tag)`.

Due modi per collegare il video:
- **YouTube** (quello che usiamo ora): si mette l'id del video del canale
  [Servizi Informatici Srl - Parma](https://www.youtube.com/@serviziinformaticisrl-parm8248)
  — l'id è la parte dopo `watch?v=`. Il video si apre in una finestra nella pagina e viene
  caricato da youtube-nocookie.com solo al clic sul play: prima di allora nessuna richiesta a YouTube.
- **File locale**: si mette `assets/video/<slug>.mp4`. Ha la precedenza sul video YouTube.

Poi `python3 tools/gen.py`. Le pillole senza video finiscono nel gruppo "In arrivo" in fondo a
`/pillole/`; quando il video c'è, risalgono da sole nell'elenco principale.

Perché i video YouTube devono essere incorporabili: in YouTube Studio, video → Altre opzioni →
Licenza e distribuzione → "Consenti incorporamento". Se l'incorporamento è disattivato,
la finestra mostra il pulsante "Guarda il video su YouTube".

Il video di presentazione nella sezione "Chi siamo" della home è `PROMO_YT` in `tools/gen.py`.

## Eventi gratuiti (Eventbrite)
In `/corsi/` c'è un commento con il pulsante da usare: `data-eventbrite="ID_EVENTO"`.
Lo script di Eventbrite si carica solo quando si preme il pulsante.

## Statistiche e cookie
Nessun cookie e nessuno script di tracciamento: le statistiche si attivano da Netlify Analytics (log del server). Per questo non c'è banner.

## Da completare
- Date dei prossimi corsi (`[DATA DA DEFINIRE]`)
- File mp4 delle Pillole
- PDF "esempio di circolare ai dipendenti" nella pagina Whistleblowing (`[SEGNAPOSTO]`)
- Verifica dei testi legali da parte di un consulente

## Crediti
Loghi dei prodotti e illustrazioni della campagna: © Sistemi SpA, usati come Partner Sistemi.
