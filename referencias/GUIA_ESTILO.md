# Guía de estilo de los personajes

Referencia: `referencias/estilo/pixelart_medio_cuerpo.png` (Coffee Talk).

## Decisión tomada: opción A
- Pixel art de alta resolución ("HD pixel art"), a medio camino entre pixel art y animación.
- Pixelado parecido al de la referencia (se probó a bajarlo a 140 px, pero la cara perdía demasiado detalle).
- **Escala común: la cabeza (de la parte de arriba del pelo a la barbilla) mide unos 56 px.** Ramón, de la cintura para arriba, mide 210 px de alto. Con el juego a unos 720 px de ancho.
- Los sprites limpios están en `personajes_pixel/` y se generan con `scripts/limpiar_personaje.py` (fondo transparente, paleta de 48 colores).
- Se escala solo por múltiplos enteros (×2, ×3…) y sin suavizado.

## Encuadre y proporciones
- De la cintura para arriba, de frente o ligeramente girado.
- Proporciones realistas algo estilizadas (tipo anime): hombros anchos, cabeza más o menos 1/4 de la figura visible.
- El personaje tiene que reconocerse como la persona real de la foto.

## Estilo
- Contorno oscuro de color, no negro puro.
- Sombras en 2–3 tonos por color, sin degradados.
- Paleta cálida y algo apagada.
- Ojos y boca detallados para que se noten las expresiones.

## Formato de archivos
- PNG, a tamaño original y sin compresión JPG.
