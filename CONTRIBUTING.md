# Cómo contribuir

Gracias por tu interés en ARCO. El proyecto nació en un diplomado académico y busca colaboradores para su eventual implementación.

## Antes de empezar

- Leé el [README](README.md), el [brief definitivo](documentos/2026-11-23_brief-arco-definitivo.pdf) y la [hoja de ruta](ROADMAP.md).
- Tené presente que hoy el repositorio contiene un **sitio estático y documentación**. No hay aplicación, backend ni base de datos.
- El equipo todavía **no asignó una licencia**. Antes de reutilizar código o contenidos fuera de este repositorio, consultá con el equipo.

## Proponer mejoras

1. Abrí un *issue* en <https://github.com/arco-um-caf/arco-um-caf.github.io/issues> (requiere cuenta de GitHub).
2. Indicá qué querés mejorar, por qué y, si aplica, en qué página o archivo.
3. Para cambios de código, esperá una respuesta del equipo antes de enviar un *pull request*.

## Reglas de contenido

- Distinguir siempre lo realizado, lo propuesto y lo simulado.
- No presentar el piloto como ejecutado ni resultados esperados como alcanzados.
- No atribuir compromisos institucionales o financieros no documentados.
- No publicar datos personales: la planilla original de la encuesta no forma parte del repositorio.
- No modificar documentos históricos; las diferencias se explican en el sitio.

## Cambios en el sitio

- Probá localmente con `python3 -m http.server 8000`.
- Si cambiás el menú o el pie, editá `herramientas/comunes.py` y ejecutalo; no edites esos bloques a mano en cada página.
- Las imágenes llevan texto alternativo. Los archivos nuevos usan nombres sin espacios ni tildes.
- Los archivos de más de 50 MB no van al repositorio: se publican como adjuntos de una *release*.
