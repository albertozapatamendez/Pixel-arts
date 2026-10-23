"""Escala una imagen a un alto dado, manteniendo la proporción.

Uso: python3 scripts/escalar_personaje.py ENTRADA SALIDA ALTO_PX
Solo cambia el tamaño: no quita el fondo ni toca los colores.
"""
import sys
from PIL import Image

ent, sal, alto = sys.argv[1], sys.argv[2], int(sys.argv[3])
im = Image.open(ent)
ancho = round(im.width * alto / im.height)
im.resize((ancho, alto), Image.BOX).save(sal)
print(sal, ancho, "x", alto)
