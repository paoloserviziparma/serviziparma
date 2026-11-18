#!/usr/bin/env python3
"""Costruisce una copia del sito con percorsi RELATIVI, per le anteprime.

Il sito vero usa percorsi assoluti (/assets/..., /contatti/) perché sta nella
radice del dominio. Un'anteprima servita in una sottocartella (per esempio un
artifact) non li risolve: qui li riscriviamo in percorsi relativi, facendo
puntare ogni cartella al suo index.html.

    python3 tools/preview.py [cartella-di-destinazione]   (default: /tmp/anteprima)
"""
import os, re, shutil, sys

R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = sys.argv[1] if len(sys.argv) > 1 else '/tmp/anteprima'
SKIP_DIRS = {'.git', 'tools'}
SKIP_FILES = {'netlify.toml', 'README.md', 'sitemap.xml', 'robots.txt', 'llms.txt', '.gitkeep'}

ABS = re.compile(r'(?<=["\'])/([^"\'\s>]*)')


def to_rel(path_and_tail, prefix):
    m = re.match(r'([^?#]*)([?#].*)?$', path_and_tail)
    path, tail = m.group(1), m.group(2) or ''
    if path == '' or path.endswith('/'):
        path += 'index.html'
    return prefix + path + tail


def convert(text, depth):
    prefix = '../' * depth
    text = ABS.sub(lambda m: to_rel(m.group(1), prefix), text)
    # i moduli Netlify non esistono nell'anteprima: li rendiamo navigabili
    text = text.replace(' method="POST"', ' method="GET"').replace(' data-netlify="true"', '')
    # Nel riquadro di un'anteprima la pagina nuova si apre con il riquadro ancora
    # scorso a metà: dopo ogni navigazione riportiamo la vista in cima.
    text = text.replace('</body>',
                        '<script>(function(){try{if(window.top===window.self)return;var fermo=false;'
                        '["wheel","touchstart","keydown","mousedown"].forEach(function(ev){'
                        'addEventListener(ev,function(){fermo=true},{passive:true,once:true})});'
                        'function su(){if(fermo)return;try{var t=null;'
                        'if(location.hash){try{t=document.querySelector(location.hash)}catch(e){}}'
                        '(t||document.documentElement).scrollIntoView({block:"start",behavior:"instant"})}catch(e){}}'
                        'addEventListener("DOMContentLoaded",su);addEventListener("load",su);'
                        '[0,80,250,600,1200].forEach(function(ms){setTimeout(su,ms)})}catch(e){}})();'
                        '</script>\n</body>')
    text = text.replace('<main id="contenuto">',
                        '<div style="background:#141414;color:#fff;font:600 14px/1.4 Montserrat,sans-serif;'
                        'padding:10px 20px;text-align:center">Anteprima privata del nuovo sito · '
                        'moduli e statistiche attivi solo dopo la pubblicazione</div>\n<main id="contenuto">')
    return text


def main():
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    n_html = n_other = 0
    for d, dirs, files in os.walk(R):
        dirs[:] = [x for x in dirs if x not in SKIP_DIRS]
        for f in files:
            if f in SKIP_FILES:
                continue
            src = os.path.join(d, f)
            rel = os.path.relpath(src, R)
            dst = os.path.join(OUT, rel)
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            if f.endswith('.html'):
                depth = rel.count(os.sep)
                open(dst, 'w').write(convert(open(src).read(), depth))
                n_html += 1
            else:
                shutil.copy2(src, dst)
                n_other += 1
    print(f'anteprima in {OUT}: {n_html} pagine, {n_other} file')


if __name__ == '__main__':
    main()
