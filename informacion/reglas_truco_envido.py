#Reglas Truco
import random
from informacion.colores import COLOR_MARCADOR, COLOR_TEXTO_BOTON
from informacion.estado_juego import EstadoJuego
import pygame as pg
from informacion.pantalla import PANTALLA
from funciones.dibujo_pygame import dibujar_marcador

class Truco(EstadoJuego):
    def __init__(self,baraja_barajeadas:list, cantidad_cartas:int) -> None:
        '''instancio la clase Truco heredando variables de EstadoJuego '''
        super().__init__(baraja_barajeadas, cantidad_cartas)
        # Banderas del juego
        self.canto_actual = None
        self.respuesta_compu = ""
        self.respuestas_validas = []
        
        self.Truco = False
        self.Retruco = False
        self.Vale_4 = False
        
        self.Envido = False
        self.Real_Envido = False
        self.Falta_Envido = False
        
        
        self.Quiero = False
        self.No_quiero = False
        self.partida = True
        self.puntos_a_sumar = 1
        self.opciones_respuesta = []  # Opciones habilitadas para la respuesta
        
    def reiniciar_valores_truco(self) -> None:
        '''Reinicio las varibles de la Clase Truco a su valor predeterminado'''
        self.Truco = False
        self.Retruco = False
        self.Vale_4 = False
        self.Envido = False
        self.Real_Envido = False
        self.Falta_Envido = False
        self.Quiero = False
        self.No_quiero = False
        self.partida = True
        self.puntos_a_sumar = 1
        self.opciones_respuesta = []  # Opciones habilitadas para la respuesta
        self.canto_actual = None # Puede ser "Truco", "Retruco", "Vale 4"
        self.respuesta_compu = ""
        self.respuestas_validas = []
    
    def jugador_canta(self, canto:str) -> list:
        '''
        Verifico el canto del jugador y devuelvo las respuestas posibles a responder  a dicho canto
        '''
        # El jugador canta Truco
        dibujar_marcador(PANTALLA, canto, COLOR_MARCADOR, COLOR_TEXTO_BOTON, (700, 490), (100, 50))
        pg.display.update()
        
        if canto == "Truco" and not self.Truco:
            self.Truco = True
            return ["Quiero", "No quiero", "Retruco"] #respuestas de la compu
        
        # El jugador canta Retruco
        if canto == "Retruco" and self.Truco and not self.Retruco:
            self.Retruco = True
            return ["Quiero", "No quiero", "Vale 4"]
        
        # El jugador canta Vale 4
        if canto == "Vale 4" and self.Retruco and not self.Vale_4:
            self.Vale_4 = True
            return ["Quiero", "No quiero"]

        if canto == "Envido" and not self.Envido:
            self.Envido = True
            return ["Quiero", "No quiero", "Real Envido"] 
        
        if canto == "Real Envido" and self.Envido and not self.Real_Envido:
            self.Real_Envido = True
            return ["Quiero", "No quiero", "Falta Envido"]
        
        if canto == "Falta Envido" and self.Real_Envido and not self.Falta_Envido:
            self.Falta_Envido = True
            return ["Quiero", "No quiero"]
    
        return []

    def computadora_responde(self, opciones:list,PUNTOS_MAX:int) -> tuple:
        '''
        La computadora responde a los cantos y devuelve las respuestas posibles a dicho canto,
        lo que respondio, y los puntos a sumar 
        '''
        # Respuesta aleatoria de la computadora
        respuesta_computadora = random.choice(opciones)
        pg.time.wait(1000)
        dibujar_marcador(PANTALLA, f"{respuesta_computadora}" , COLOR_MARCADOR,COLOR_TEXTO_BOTON, (700, 50), (100,50))
        pg.display.update()

        if respuesta_computadora == "Retruco":
            self.Retruco = True
            self.partida = True
            return ["Quiero", "No quiero", "Vale 4"],respuesta_computadora,self.puntos_a_sumar
        
        if respuesta_computadora == "Real Envido":
            self.Real_Envido = True
            self.partida = True
            return ["Quiero", "No quiero","Falta Envido"], respuesta_computadora, self.puntos_a_sumar
        
        if respuesta_computadora == "Quiero":
            self.Quiero = True
            self.partida = True 
            
            # Determinar los puntos del quiero
            if self.Truco and not self.Retruco and not self.Vale_4:
                self.puntos_a_sumar = 2  
            elif self.Retruco and not self.Vale_4:
                self.puntos_a_sumar = 3  
            elif self.Vale_4:
                self.puntos_a_sumar = 4 
            
            # Determinar los puntos envido quiero
            if self.Envido and not self.Real_Envido and not self.Falta_Envido:
                self.puntos_a_sumar = 2  # Se juega por 2 puntos (Envido básico)
            elif self.Real_Envido and not self.Falta_Envido:
                self.puntos_a_sumar = 3  # Se juega por 3 puntos
            elif self.Falta_Envido:
                self.puntos_a_sumar = self.puntos_para_ganar(PUNTOS_MAX)  # Falta Envido: puntos hasta ganar
            
            return [],respuesta_computadora,self.puntos_a_sumar
                
        elif respuesta_computadora == "No quiero":
            self.No_quiero = True
            
            if self.Truco:
                self.partida = False 
            
            # Determinar los puntos del no quiero 
            if self.Truco and not self.Retruco and not self.Vale_4:
                self.puntos_a_sumar = 1             # Truco gana 1 punto 
            elif self.Retruco and not self.Vale_4:
                self.puntos_a_sumar = 2             # Retruco gana 2 punto
            elif self.Vale_4:
                self.puntos_a_sumar = 3             # Vale 4 gana 3 punto
                
            # Determinar los puntos sumados por el rechazo
            if self.Envido and not self.Real_Envido and not self.Falta_Envido:
                self.puntos_a_sumar = 1             # Envido gana 1 punto
            elif self.Real_Envido and not self.Falta_Envido:
                self.puntos_a_sumar = 2             # Real Envido gana 2 punto
            elif self.Falta_Envido:
                self.puntos_a_sumar = 3             # Falta Envido: 3 puntos por rechazo
            
            return [],respuesta_computadora,self.puntos_a_sumar

    def jugador_responde(self, respuesta:str) -> int:
        ''' 
        Jugador tiene 2 respuestas posibles quiero y no quiero, se verifica la respuesta y 
        se devuelve los puntos a sumar 
        '''
        # Respuesta del jugador
        dibujar_marcador(PANTALLA, respuesta, COLOR_MARCADOR, COLOR_TEXTO_BOTON, (700, 490), (100, 50))
        pg.display.update()
        
        if respuesta == "Quiero":
            self.Quiero = True
            # Determinar los puntos_a_sumar según el canto
            if self.Truco and not self.Retruco and not self.Vale_4:
                self.puntos_a_sumar = 2
                # print("El jugador acepta el Truco. Se juega por 2 puntos_a_sumar.")
            elif self.Retruco and not self.Vale_4:
                self.puntos_a_sumar = 3
                # print("El jugador acepta el Retruco. Se juega por 3 puntos_a_sumar.")
            elif self.Vale_4:
                self.puntos_a_sumar = 4
                # print("El jugador acepta el Vale 4. Se juega por 4 puntos_a_sumar.")
            
            return self.puntos_a_sumar
            
        
        elif respuesta == "No quiero":
            self.No_quiero = True
            # Determinar los puntos_a_sumar según el canto
            if self.Truco and not self.Retruco and not self.Vale_4:
                self.puntos_a_sumar = 1
                # print("El jugador rechaza el Truco. El jugador gana 1 punto.")
            elif self.Retruco and not self.Vale_4:
                self.puntos_a_sumar = 2
                # print("El jugador rechaza el Retruco. El jugador gana 2 puntos_a_sumar.")
            elif self.Vale_4:
                self.puntos_a_sumar = 3
                # print("El jugador rechaza el Vale 4. El jugador gana 3 puntos_a_sumar.")
            
            return self.puntos_a_sumar
        
    def puntos_para_ganar(self,PUNTOS_MAX:int) -> int:
        '''
        Calcula los puntos para ganar, esto es usado en Falta Envido, 
        devuelve los puntos necesarios para ganar la partida
        '''
        puntos_necesarios = PUNTOS_MAX - max(self.puntos_jugador, self.puntos_computadora)
        return puntos_necesarios


    def cantar_responder(self, canto_actual:str, PUNTOS_MAX:int) -> None:
        '''
        Esta engloba todo el proceso, primero canta el jugador, luego computadora responde, esto devuelve
        las respuestas validas a responder, lo que responde la computadora y los puntos a sumar 
        '''
        self.opciones_respuesta = self.jugador_canta(canto_actual)
        respuestas_validas, respuesta_compu, self.puntos_a_sumar = self.computadora_responde(
            self.opciones_respuesta, PUNTOS_MAX
        )
        return respuestas_validas, respuesta_compu, self.puntos_a_sumar
    
    def verficar_puntos_rechazos(self) -> int:
        '''
        Esto verifica que puntos hay que sumar cuando la respuesta en NO QUIERO,
        Devuelve puntos a sumar cuando se canta "No quiero" 
        '''
        puntos = 0
        if self.Vale_4:
            puntos = 3
        elif self.Retruco:
            puntos = 2
        elif self.Truco:
            puntos = 1
        elif self.Falta_Envido:
            puntos = 3  # Puedes cambiar esto según las reglas de Falta Envido
        elif self.Real_Envido:
            puntos = 2
        elif self.Envido:
            puntos = 1
            
        return puntos