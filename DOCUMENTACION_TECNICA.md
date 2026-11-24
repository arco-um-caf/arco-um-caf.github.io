# Documentación técnica

Este documento tiene dos partes. La primera describe **lo que existe** en el repositorio. La segunda es una **propuesta técnica** para la herramienta del piloto, que todavía no existe.

## Parte 1 · Lo que existe

### Sitio web estático

| Aspecto | Detalle |
|---|---|
| Tipo | Sitio estático, sin compilación |
| Lenguajes | HTML5, CSS3, JavaScript (≈60 líneas, sin dependencias) |
| Publicación | GitHub Pages, rama `main`, carpeta raíz |
| Tipografía | Montserrat 400, 600 y 700 en `woff2`, alojada localmente |
| Videos | MP4 H.264 + AAC con `faststart`, `preload="none"`, sin reproducción automática |
| Accesibilidad | Enlace «Saltar al contenido», foco visible, `aria-expanded` en el menú, texto alternativo, respeto de `prefers-reduced-motion` |
| Mantenimiento | `herramientas/comunes.py` regenera cabecera y pie en todas las páginas |

### Videos

| Archivo | Duración | Formato | Tamaño | Origen |
|---|---|---|---|---|
| `assets/video/arco-presentacion.mp4` | 5:00 | 1280×720, 30 fps | 24 MB | Versión web del original (1280×720, 60 fps, 137 MB), codificada en dos pasadas a ~540 kb/s de video y 96 kb/s de audio |
| `assets/video/arco-demo-mvp.mp4` | 3:49 | 1920×1080, 30 fps | 21 MB | Archivo original sin recodificar |
| `assets/video/arco-centenario.mp4` | 0:10 | 1280×720 | 3,8 MB | Versión 1 del sitio (histórico) |
| `assets/video/arco-mvp-demo.mp4` | 2:00 | 1920×1080 | 6,6 MB | Demo preliminar (histórico) |

Límites de GitHub considerados: 25 MiB por archivo subido desde el navegador, advertencia a partir de 50 MiB, bloqueo a partir de 100 MiB, 2 GiB por archivo adjunto a una *release*.

## Parte 2 · Propuesta técnica para la herramienta del piloto

> **Propuesta, no implementada.** Surge de los estados, roles y pantallas del brief y de la demostración del MVP. Requiere validación con el equipo y los actores antes de construirse.

### Requisitos funcionales propuestos

1. Configurar un edificio participante: unidades, material (máx. 2), contenedores y gestor receptor.
2. Registrar cada visita de operación como un **lote** con código único (ejemplo de la demo: `ARCO-E01-001`).
3. Registrar pesos depositados por unidad y rechazo en origen.
4. Confirmar el retiro con peso y constancia.
5. Registrar la recepción del gestor con el mismo código y su comprobante.
6. Registrar la clasificación: aceptado y rechazado en kg, con motivo.
7. Acreditar la valorización solo con comprobante de venta, destino o proceso.
8. Registrar incidencias por lote y etapa.
9. Generar un resumen semanal agregado para el edificio y un tablero de indicadores para el equipo.

### Reglas de negocio propuestas

- Un estado solo se marca con su evidencia.
- Los pesos de distintas etapas no se suman entre sí.
- Aceptado + rechazado = recibido.
- Valorizado ≤ aceptado.
- Los residentes no tienen cuenta; los reportes al edificio no contienen datos personales.

### Modelo de datos propuesto

```
Edificio (id, zona, unidades, material[], gestor_id)
Lote (codigo, edificio_id, semana, fecha_visita, operador)
RegistroPeso (lote, unidad, kg_depositado, kg_rechazo_origen)
Retiro (lote, kg, recolector, fecha, constancia)
Recepcion (lote, kg, gestor, fecha, comprobante)
Clasificacion (lote, kg_aceptado, kg_rechazado, motivo)
Valorizacion (lote, kg, destino, comprobante, fecha)
Incidencia (lote, etapa, descripcion, accion, fecha)
```

### Arquitectura sugerida por etapas (propuesta)

| Etapa | Opción | Motivo |
|---|---|---|
| Piloto ARCO 1.0 | Formularios y planillas con validaciones, más WhatsApp | Coherente con el brief: bajo costo, sin app propia |
| Después del piloto | Aplicación web con perfiles por rol y base de datos | Solo si el piloto valida la operación |
| ARCO 2.0 en adelante | Integración con pesaje digital, sensores y datos municipales | Condicionada a evidencia y viabilidad |

### Pendientes transversales

- Protección de datos personales y consentimiento (Ley N.º 18.331).
- Evaluación de seguridad y gobernanza de los datos.
- Definición de quién administra la herramienta y los datos.
