#Ubicaciones de cartas dibujadas
# Posicionamos las cartas en el centro de la pantalla
from informacion.pantalla import *

cantidad_cartas = 3

espacio = 30  # Espacio entre cartas

#TAMANO CARTAS
ancho_carta = 90
alto_carta = 140
tamano_cartas = (ancho_carta, alto_carta)
# Ancho total de las cartas totales en el tablero a repartir
ancho_total_cartas = (cantidad_cartas * ancho_carta) + ((cantidad_cartas-1) * espacio)

#Elijo posiciones de x, y para jugadores
x_medio = (ANCHO - ancho_total_cartas) / 2  # X inicial para centrar las cartas
y_computadora = 10 #ubicamos parte superior
y_jugador = ALTO - alto_carta - y_computadora   # Parte inferior con igual alto de arriba

#Coordenadas de cartas repartidas de jugadores para dibujar en la mesa
coordenadas_j =(x_medio,y_jugador)
coordenadas_c =(x_medio,y_computadora)

#Coordenadas de cartas lanzadas de jugadores para dibujar en la mesa
coordenadas_mesa_jugador=(x_medio,300)
coordenadas_mesa_computadora = (x_medio,155)

#Botones
TAMANO_BOTONES = (50,50)
p_boton_truco = (100,100)
p_boton_envido = (100,200)

p_boton_nuevo_juego = (450,450)

#MARCADOR
TAMANO_MARCADOR = (30,30)
p_marcador_jugador = (700,y_jugador)
p_marcador_computadora = (700,y_computadora)

#posiciones cartas para repartir
# Posiciones
posicion_mazo = ((x_medio + (espacio*2) + (ancho_carta*2)), y_jugador)  # Esquina derecha superior
posiciones_jugadores = [
    (x_medio, y_computadora),  # Jugador abajo (tus cartas)
    (x_medio + espacio + ancho_carta, y_computadora),   # Computadora arriba
    (x_medio + espacio*2 + ancho_carta*2, y_computadora),   # Computadora izquierda
    (x_medio, y_jugador),  # Jugador abajo (tus cartas)
    (x_medio + espacio + ancho_carta, y_jugador),   # Computadora arriba
    (x_medio + (espacio*2) + (ancho_carta*2), y_jugador),   # Computadora izquierda
]

botones_cantos = {
    "Truco": (100,100),
    "Retruco": (100,160),
    "Vale 4": (100,220),
    "Envido": (170, 100),
    "Real Envido":(170, 160),
    "Falta Envido": (170, 220),
    "Quiero": (100,280),
    "No quiero": (170,280)
}
