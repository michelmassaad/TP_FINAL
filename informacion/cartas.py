
#Crear Jerarquia de Cartas
# cartas
from funciones.baraja import *
PALOS = ("oro", "copa", "espada", "basto")
VALORES = (1, 2, 3, 4, 5, 6, 7, 10, 11, 12)
ruta_base_imagenes = "cartas"
cantidad_cartas = 3
reverso_carta = pg.image.load("cartas/reverso_2.jpg")  # Imagen de la carta
reverso_carta = pg.transform.scale(reverso_carta, (90, 140))  # Redimensionar carta

jerarquia_truco = {
    ('espada', 1): 14,
    ('basto', 1): 13,
    ('espada', 7): 12,
    ('oro', 7): 11,
    ('', 3): 10,
    ('', 2): 9,
    ('oro', 1): 8,
    ('copa', 1): 8,
    ('', 12): 7,
    ('', 11): 6,
    ('', 10): 5,
    ('basto', 7): 4,
    ('copa', 7): 4,
    ('', 6): 3,
    ('', 5): 2,
    ('', 4): 1
}

