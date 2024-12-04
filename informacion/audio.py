import pygame as pg
# Cargar la música de fondo
sonido_barajear = pg.mixer.Sound("audio/sonido_lanzar_carta.wav")
sonido_lanzar_carta = pg.mixer.Sound("audio/sonido_lanzar_carta.wav")

# Ajustar el volumen de la música
pg.mixer.music.set_volume(0.3)  # Volumen de 0.0 a 1.0