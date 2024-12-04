from funciones.repartir import repartir_cartas
from funciones.baraja import asignar_posiciones
from informacion.posiciones_dibujo import *

class EstadoJuego:
    def __init__(self, baraja_barajeadas:list, cantidad_cartas:int) -> None:
        '''instancio la clase EstadoJuego para la administracion de las variables del juego'''
        self.baraja_barajeadas = baraja_barajeadas
        self.cantidad_cartas = cantidad_cartas
        self.ronda = 0

        self.mano_jugador = []
        self.mano_computadora = []
        self.lista_carta_seleccionada = []
        self.lista_lanzada_computadora = []
        self.turno_jugador = True
        self.turno_computadora = not self.turno_jugador
        self.puntos_jugador = 0
        self.puntos_computadora = 0
        
    def reinicio_valores(self, baraja_barajeadas:list) -> None:
        '''reinicio los valores de la clase EstadoJuego a sus valores predeterminados'''
        self.baraja_barajeadas = baraja_barajeadas
        self.ronda = 0

        self.mano_jugador = []
        self.mano_computadora = []
        self.lista_carta_seleccionada = []
        self.lista_lanzada_computadora = []
        self.turno_jugador = True
        self.turno_computadora = not self.turno_jugador
        self.puntos_jugador = 0
        self.puntos_computadora = 0

    def iniciar_ronda(self) -> None:
        '''inicia la ronda de reparto de cartas, limpio las cartas lanzadas y se reparten nuevas, 
        asigno posiciones, defino turnos '''
        self.mano_jugador = repartir_cartas(self.baraja_barajeadas, self.cantidad_cartas)
        self.mano_computadora = repartir_cartas(self.baraja_barajeadas, self.cantidad_cartas)
        
        self.lista_carta_seleccionada = []
        self.lista_lanzada_computadora = []

        asignar_posiciones(self.mano_computadora, coordenadas_c, espacio, tamano_cartas)
        asignar_posiciones(self.mano_jugador, coordenadas_j, espacio, tamano_cartas)
        
        #Definir Turno ()
        self.turno_jugador = self.ronda % 2 == 0
        self.turno_computadora = not self.turno_jugador
        self.ronda += 1
    
    


