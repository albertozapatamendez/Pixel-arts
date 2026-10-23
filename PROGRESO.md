# Progreso del proyecto

Pixel arts de personajes basados en gente real, para un videojuego de diálogos estilo *Coffee Talk*.

## Hecho
1. **Estilo definido**: está en `referencias/GUIA_ESTILO.md`. Es HD pixel art de la cintura para arriba, con la referencia de *Coffee Talk* en `referencias/estilo/pixelart_medio_cuerpo.png`.
2. **Fotos reales**: la foto de grupo está en `referencias/personas/Personajes.png`, y los recortes de cada uno en `1_tomas`, `2_jorge`, `3_chamizo`, `4_ramon` y `5_eduardo`.
3. **Pruebas**:
   - Pixelar la foto con un script no sirve: sale una foto pixelada, no pixel art.
   - Gemini mantiene el estilo pero no el parecido (`prototipos/ramon/`).
   - Con otra IA se consiguieron versiones con cara y ropa correctas. Hay que apuntar qué IA y qué prompt se usaron.
4. **Personajes base (validados)**: en `personajes_definitivos_prototipo/` están Tomás (con el perro), Jorge, Chamizo, Ramón y Eduardo. Son imágenes grandes de IA que imitan el pixel art; todavía no son pixel art real.
5. **Escala común**: la cabeza mide unos 56 px. Con `scripts/escalar_personaje.py` (que solo escala), los altos son:

   | Personaje | Alto (px) |
   |---|---|
   | Ramón | 210 |
   | Tomás | 249 |
   | Jorge | 198 |
   | Chamizo | 187 |
   | Eduardo | 292 |

   Las imágenes escaladas no se guardaron: hay que generarlas cuando se necesiten.

## Pendiente
1. **Encontrar una forma de limpiar bien el pixel art.** Se probó con un script (fondo por color y paleta de 48 colores) y no quedó limpio del todo; se descartó. Opciones a investigar:
   - Herramientas específicas para pasar imágenes de IA a pixel art real.
   - Limpieza manual en Aseprite.
   - Pedir a la IA directamente fondo transparente o una cuadrícula exacta.
2. **Limpiar los 5 personajes**: quitar el fondo (dejarlo transparente), ajustar a una cuadrícula de píxel real y usar una paleta común.
3. **Cortar a todos a la misma altura del cuerpo**, por ejemplo a la cintura. Ahora cada uno está encuadrado de forma distinta.
4. **Expresiones** de cada personaje (neutral, contento, enfadado, sorprendido, triste…). Es lo prioritario para un juego de diálogos.
5. **Poses** (brazos cruzados, saludando, con objetos…).
6. **Apuntar la IA y el prompt** con los que se hicieron los personajes base, para repetir el proceso.
