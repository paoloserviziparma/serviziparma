# Sito Sistemi Parma – Servizi Informatici Srl

Sito statico (HTML/CSS/JS, nessun framework) di www.serviziparma.com, pubblicato su Netlify da questo repository.

## Struttura
- `/` home · `/professionisti/` e `/aziende/` (con una pagina per prodotto) · `/aziende/verticali/`
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

## Moduli (Netlify Forms)
- `contatti`: home, contatti, 100% Profis (campo nascosto `pagina`)
- `iscrizione-corso`: pagine dei corsi, con i dati per la fattura (la fattura è emessa a parte)
Entrambi hanno honeypot, campo nascosto `lingua` e privacy obbligatoria. Le notifiche email si impostano nel pannello Netlify (Forms → Notifications).

## Le Pillole (video)
I video vanno in `assets/video/<slug>.mp4`, dove lo slug è quello della pagina (es. `la-delega-unica.mp4`).
Poi si rilancia `python3 tools/gen.py`: la pagina mostra il video, che si carica solo al clic.
Per una nuova pillola si aggiunge una riga all'elenco `POSTS` in `tools/gen.py`.

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
