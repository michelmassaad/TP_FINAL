import time
import pygame as pg

from informacion.colores import *
from informacion.posiciones_dibujo import *

def cargar_imagen_carta(ruta_imagen:str, tamano:tuple) -> any:
    '''Carga imagenes y redimensiona la misma'''
    imagen = pg.image.load(ruta_imagen)  # Carga la imagen desde la ruta
    imagen = pg.transform.scale(imagen, tamano)  # Redimensiona la imagen
    return imagen


def dibujar_cartas(pantalla:any, mano:list, coordenadas:tuple, espacio:float, tamano:tuple)-> None:
    '''Dibuja las cartas en una coordenada pasada por parametro separadas por un espacio,
        verificando que no este elegida, si esta solo se deja el espacio '''
    (x,y) = coordenadas
    ancho,alto = tamano
    for carta in mano:
        if carta["elegida"] == False:
            imagen_carta = cargar_imagen_carta(carta["ruta"], tamano)
            pantalla.blit(imagen_carta, (x,y))  # Dibuja la carta

        x += ancho + espacio  
        
def dibujar_cartas_dorso(pantalla:any, mano:list, coordenadas:tuple, espacio:float, tamano:tuple)-> None:
    '''Dibuja el dorso de las cartas en una coordenada pasada por parametro separadas por un espacio,
        verificando que no este elegida, si esta solo se deja el espacio'''
    (x,y) = coordenadas
    ancho,alto = tamano
    for carta in mano:
        if carta["elegida"] == False:
            imagen_carta = cargar_imagen_carta("cartas/reverso_2.jpg", tamano)
            pantalla.blit(imagen_carta, (x,y))  # Dibuja la carta

        x += ancho + espacio 
    
def mover_carta(pantalla:any, mano:list, coordenadas_inicial:tuple, espacio:float, tamano:tuple,
                coordenadas_finales:tuple)-> None:
    '''Mueve sobre el eje y la carta desde una coordenada inicial a una coordenada final'''
    ancho,alto = tamano
    (x,y) = coordenadas_inicial
    (x_final,y_final) = coordenadas_finales
    velocidad = 5
    
    for carta in mano:
        imagen_carta = cargar_imagen_carta(carta["ruta"], tamano)
        while y != y_final:
            if y < y_final:
                y += velocidad
            if y > y_final:
                y -= velocidad
        
        coordenadas_finales = (x_final, y)
        pantalla.blit(imagen_carta, (coordenadas_finales))  # Dibuja la carta
        pg.display.flip()
        pg.display.update()
        
        x_final += ancho + espacio  # Separación horizontal
 
def dibujar_boton(superficie: any, texto: str, color: tuple, texto_color: tuple,
                  coordenadas:tuple, TAMANO_BOTONES:tuple) -> any:
    '''Dibuja un botón y devuelve el rectangulo con sus respectivas dimensiones.'''
    (x,y) = coordenadas
    ancho, alto = TAMANO_BOTONES
    boton = pg.Rect(x, y, ancho, alto)
    
    pg.draw.rect(superficie, color, boton)
    fuente = pg.font.SysFont("Arial", 13)
    superficie_texto = fuente.render(texto, True, texto_color)
    texto_color = superficie_texto.get_rect(center=boton.center)
    superficie.blit(superficie_texto, texto_color)
    return boton

def presionar_boton(boton: any, evento: any)->bool:
    ''' 
    Verifica si un botón fue presionado.
    True si el botón fue presionado, False en caso contrario.
    '''
    if boton.collidepoint(evento.pos):
        return True
    return False

def dibujar_marcador(superficie: any, texto: str, color_fondo: tuple, color_texto: tuple,
                     coordenadas: tuple, TAMANO_MARCADOR: tuple) -> any:
    '''
    Dibuja un marcador(cuadro con texto) en la superficie especificada.
    devuelve el rectangulo con sus respectivas dimensiones.
    '''
    (x, y) = coordenadas
    ancho, alto = TAMANO_MARCADOR
    
    # Crear el rectángulo para el fondo del marcador
    marcador_rect = pg.Rect(x, y, ancho, alto)
    # Dibujar el fondo del marcador
    pg.draw.rect(superficie, color_fondo, marcador_rect)
    
    # Crear el texto a mostrar en el marcador
    fuente = pg.font.SysFont("Arial", 14)  # Tamaño de la fuente
    superficie_texto = fuente.render(texto, True, color_texto)
    # Centrar el texto en el rectángulo
    texto_rect = superficie_texto.get_rect(center=marcador_rect.center)
    # Dibujar el texto en la superficie
    superficie.blit(superficie_texto, texto_rect)
    
    return marcador_rect

def dibujar_texto(superficie: any, texto: str, color:tuple, coordenadas:tuple, tamano:int=18) -> any:
    '''
    Dibuja texto, especifica su color tamano y coordenadas
    '''
    fuente = pg.font.SysFont("Arial", tamano)
    superficie_texto = fuente.render(texto, True, color)
    superficie.blit(superficie_texto, coordenadas)


# Mostrar botones para que el jugador seleccione Truco o Envido
def mostrar_botones_canto(superficie, botones, turno_jugador, canto_actual, respuestas_validas):
    '''
    Muestra dinamicamente los botones correspondientes al canto actual.
    devuelve la lista de botones activos en pantalla
    '''
    
    botones_activos = []  # Lista para guardar los botones activos en pantalla

    if turno_jugador and canto_actual is None:
        # Si no hay canto, mostrar botones para que el jugador seleccione Truco o Envido
        opciones = ["Truco", "Envido"]
        for texto in opciones:
            coordenadas = botones[texto]
            boton = dibujar_boton(superficie, texto, COLOR_BOTON, COLOR_TEXTO_BOTON, coordenadas, TAMANO_BOTONES)
            botones_activos.append((texto, boton))

    elif turno_jugador and canto_actual is not None:
        # Si hay un canto actual, mostrar las respuestas válidas para ese canto
        for texto in respuestas_validas:
            if texto in botones:
                coordenadas = botones[texto]
                boton = dibujar_boton(superficie, texto, COLOR_BOTON, COLOR_TEXTO_BOTON, coordenadas, TAMANO_BOTONES)
                botones_activos.append((texto, boton))

    return botones_activos

# Función para animar el reparto de cartas
def repartir_carta(pantalla, carta, inicio, fin, cartas_sobre_mesa, area_cartas, pasos=9):
    '''
    Anima el reparto de una carta desde la posición inicial a la final.
    '''
    x_inicial, y_inicial = inicio
    x_final, y_final = fin
    pasos = 9 # Asumiendo 60 FPS
    dx = (x_final - x_inicial) / pasos
    dy = (y_final - y_inicial) / pasos

    for paso in range(pasos):
        x_actual = x_inicial + dx * paso
        y_actual = y_inicial + dy * paso

        pg.draw.rect(PANTALLA, COLOR_FONDO, area_cartas)

        # Dibujar las cartas ya repartidas
        for pos in cartas_sobre_mesa:
            pantalla.blit(carta, pos)

        # Dibujar carta en movimiento
        pantalla.blit(carta, (x_actual, y_actual))
        pg.display.flip()
        pg.time.delay(10)

    # Añadir la posición final de la carta a la lista de cartas sobre la mesa
    cartas_sobre_mesa.append(fin)

def animacion_repartir(posiciones_jugadores,area_cartas,sonido_barajear,sprite_carta,posicion_mazo):
    '''
    Realiza la animación de repartir cartas a varios jugadores.
    '''
    pg.draw.rect(PANTALLA, COLOR_FONDO, area_cartas)
    pg.display.update(area_cartas)
    cartas_sobre_mesa = []
    for posicion in posiciones_jugadores:
        sonido_barajear.play()
        repartir_carta(PANTALLA, sprite_carta, posicion_mazo, posicion,cartas_sobre_mesa,area_cartas)
        time.sleep(0.2)  # Pausa entre cada carta repartida
