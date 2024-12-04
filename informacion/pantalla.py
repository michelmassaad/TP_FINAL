import pygame as pg
#DATOS pantalla
ANCHO = 900
ALTO = 600
TAMANIO_PANTALLA = (ANCHO,ALTO)

#Creo pantalla
PANTALLA = pg.display.set_mode(TAMANIO_PANTALLA)
pg.display.set_caption("Truco MM")
icono_esquina = pg.image.load("cartas/1 de basto.jpg")
pg.display.set_icon(icono_esquina)
