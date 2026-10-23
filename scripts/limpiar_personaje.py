"""Convierte una imagen de IA "estilo pixel art" en pixel art real.

Uso: python3 scripts/limpiar_personaje.py ENTRADA SALIDA ALTO_PX [TOLERANCIA_FONDO]
- Reduce la imagen a ALTO_PX de alto (cada píxel = un píxel real).
- Quita el fondo (relleno desde los bordes) y lo deja transparente.
- Limita la paleta a 48 colores.
"""
import sys
from collections import deque
import numpy as np
from PIL import Image

ent, sal, alto = sys.argv[1], sys.argv[2], int(sys.argv[3])
tol = int(sys.argv[4]) if len(sys.argv) > 4 else 25

im = Image.open(ent).convert("RGB")
ancho = round(im.width * alto / im.height)
peq = np.asarray(im.resize((ancho, alto), Image.BOX)).astype(int)

# Color de fondo = esquinas de arriba (las de abajo pueden ser ropa)
fondo = (peq[0, 0] + peq[0, -1]) / 2
parecido = np.abs(peq - fondo).sum(2) < tol
mask = np.zeros(parecido.shape, bool)
H, W = parecido.shape
cola = deque([(y, x) for y in range(H) for x in (0, W - 1)] + [(0, x) for x in range(W)])
while cola:
    y, x = cola.popleft()
    if 0 <= y < H and 0 <= x < W and not mask[y, x] and parecido[y, x]:
        mask[y, x] = True
        cola.extend([(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)])

q = Image.fromarray(peq.astype(np.uint8)).quantize(
    48, method=Image.Quantize.MEDIANCUT, kmeans=3, dither=Image.Dither.NONE).convert("RGBA")
o = np.asarray(q).copy()
o[mask, 3] = 0
Image.fromarray(o).save(sal)
print(sal, ancho, "x", alto)
