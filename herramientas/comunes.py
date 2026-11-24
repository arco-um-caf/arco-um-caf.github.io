#!/usr/bin/env python3
"""Actualiza la cabecera y el pie de página comunes en todas las páginas del sitio.

Uso (desde la raíz del repositorio):
    python3 herramientas/comunes.py

El script reemplaza el bloque <header class="cabecera">…</header> y el bloque
<footer class="pie-sitio">…</footer> de cada página HTML de la raíz por las
plantillas definidas abajo, marcando como actual la sección correspondiente.
No modifica el contenido principal (<main>) de las páginas.
No requiere dependencias externas (solo Python 3).
"""
from pathlib import Path
import re

RAIZ = Path(__file__).resolve().parent.parent
REPO = "https://github.com/arco-um-caf/arco-um-caf.github.io"
VERSION = "Versión 2.0 del sitio web · Entrega final · Noviembre 2026"

# (archivo, etiqueta en el menú)
MENU = [
    ("index.html", "Inicio"),
    ("propuesta.html", "El proyecto"),
    ("investigacion.html", "Investigación"),
    ("mvp.html", "MVP"),
    ("desarrollo.html", "Evolución"),
    ("documentos.html", "Documentos"),
    ("equipo.html", "Equipo"),
    ("recorrido.html", "Historia"),
]
# páginas secundarias que marcan una sección del menú como actual
PADRE = {"galeria.html": "recorrido.html"}


def cabecera(actual: str) -> str:
    items = []
    for archivo, etiqueta in MENU:
        cur = ' aria-current="page"' if archivo == PADRE.get(actual, actual) else ""
        items.append(f'<li><a href="{archivo}"{cur}>{etiqueta}</a></li>')
    items.append(f'<li><a class="ext" href="{REPO}" rel="noopener" title="Repositorio en GitHub: acceso para administradores del sitio y desarrolladores de código" aria-label="GitHub, acceso para administradores y desarrolladores de código">GitHub ↗</a></li>')
    return (
        '<header class="cabecera">\n'
        '  <div class="contenedor">\n'
        '    <a class="marca" href="index.html"><img src="assets/img/logo-arco.png" alt="ARCO, inicio" width="58" height="42">'
        '<span>Acelerador de Reciclaje Colaborativo en Origen</span></a>\n'
        '    <button class="menu-btn" type="button" aria-expanded="false" aria-controls="menu-principal">Menú</button>\n'
        '    <nav class="nav" id="menu-principal" aria-label="Secciones del sitio"><ul>'
        + "".join(items)
        + "</ul></nav>\n  </div>\n</header>"
    )


PIE = f"""<footer class="pie-sitio">
  <div class="contenedor">
    <div class="columnas">
      <div>
        <img class="logo-pie" src="assets/img/logo-arco.png" alt="ARCO" width="58" height="42" loading="lazy">
        <p><strong>ARCO · Acelerador de Reciclaje Colaborativo en Origen.</strong> Proyecto de equipo del Diplomado en Gobernabilidad e Innovación Pública, CAF – Universidad de Montevideo, 2026.</p>
        <p>El piloto es una propuesta: no se ha ejecutado. La demostración del MVP usa datos simulados.</p>
      </div>
      <div>
        <h2>Sitio</h2>
        <ul>
          <li><a href="https://arco-um-caf.github.io/">arco-um-caf.github.io</a></li>
          <li><a href="propuesta.html">El proyecto</a></li>
          <li><a href="mvp.html">MVP</a></li>
          <li><a href="desarrollo.html">Evolución</a></li>
          <li><a href="galeria.html">Galería</a></li>
        </ul>
      </div>
      <div>
        <h2>Recursos</h2>
        <ul>
          <li><a href="index.html#videos">Videos</a></li>
          <li><a href="assets/video/arco-presentacion.mp4" download>Presentación (MP4)</a></li>
          <li><a href="assets/video/arco-demo-mvp.mp4" download>Demo del MVP (MP4)</a></li>
          <li><a href="documentos/2026-11-23_brief-arco-definitivo.pdf">Brief definitivo (PDF)</a></li>
          <li><a href="documentos.html">Documentación</a></li>
        </ul>
      </div>
      <div>
        <h2>Código</h2>
        <p class="nota-gh">Acceso para administradores del sitio y desarrolladores de código. Para conocer el proyecto no hace falta entrar a GitHub.</p>
        <ul>
          <li><a href="{REPO}" rel="noopener">Repositorio en GitHub</a></li>
          <li><a href="{REPO}#readme" rel="noopener">README</a></li>
          <li><a href="{REPO}/releases" rel="noopener">Versiones publicadas</a></li>
          <li><a href="{REPO}/issues" rel="noopener">Proponer mejoras</a></li>
        </ul>
      </div>
    </div>
    <p class="base">{VERSION}. La mención de CAF y de la Universidad de Montevideo indica el contexto académico del proyecto y no implica un aval institucional adicional. Contenidos sin licencia de reutilización asignada.</p>
  </div>
</footer>"""

RE_HEAD = re.compile(r'<header class="cabecera">.*?</header>', re.S)
RE_FOOT = re.compile(r'<footer class="pie-sitio">.*?</footer>', re.S)


def main() -> None:
    for pagina in sorted(RAIZ.glob("*.html")):
        if pagina.name == "404.html":
            continue
        html = pagina.read_text(encoding="utf-8")
        nuevo = RE_HEAD.sub(lambda _: cabecera(pagina.name), html, count=1)
        nuevo = RE_FOOT.sub(lambda _: PIE, nuevo, count=1)
        if nuevo != html:
            pagina.write_text(nuevo, encoding="utf-8")
            print("actualizada:", pagina.name)


if __name__ == "__main__":
    main()
