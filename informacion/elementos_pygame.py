import pygame as pg
from .posiciones_dibujo import x_medio,ancho_total_cartas,ALTO
# Fuentes
pg.init()
FUENTE_TITULO = pg.font.SysFont("Arial", 40, bold=True)
FUENTE_TEXTO = pg.font.SysFont("Arial", 18)

area_cartas = pg.Rect(x_medio, 0, ancho_total_cartas, ALTO)
