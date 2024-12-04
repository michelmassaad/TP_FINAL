from informacion.colores import BLANCO
from informacion.pantalla import ANCHO, PANTALLA
from funciones.dibujo_pygame import dibujar_texto
import pygame as pg


RUTA_ARCHIVO = "archivos/historial.csv"  # Archivo donde se guardan los puntajes

def leer_historial():
    """leer el historial existente desde el archivo csv."""
    historial = {}
    with open(RUTA_ARCHIVO, mode="r", encoding="utf-8") as archivo:
        next(archivo)  # Saltar la cabecera
        for linea in archivo:
            nombre, puntaje = linea.strip().split(",")  # Separar por comas
            historial[nombre] = int(puntaje)  #guardo en el diccionario como {"nombre": puntaje}

    return historial

def guardar_puntuaciones(puntuaciones:dict) -> None:
    """
    Guarda las puntuaciones en el archivo csv
    """
    with open(RUTA_ARCHIVO, mode="w", encoding="utf-8") as archivo:
        archivo.write("Nombre,Puntaje\n")  
        for nombre in puntuaciones:  
                puntaje = puntuaciones[nombre]  
                archivo.write(f"{nombre},{puntaje}\n")  # Escribe en el archivo

def actualizar_puntuacion(nombre:str, puntaje:int) -> None:
    """
    Suma el puntaje total del jugador en todas sus partidas jugadas.
    devuelve mensaje correspondiente a dicho usuario
    """
    puntuaciones = leer_historial()
    
    if nombre in puntuaciones:
        puntuaciones[nombre] += puntaje
        guardar_puntuaciones(puntuaciones)
        return (f"¡Increible {nombre}! Tu historial de puntos actualizado es {puntuaciones[nombre]}.")
    else:
        puntuaciones[nombre] = puntaje  # Agrega nuevo jugador
        guardar_puntuaciones(puntuaciones)
        return (f"Se agregó un nuevo jugador: {nombre} con puntaje {puntaje}.")
    
    
def verificar_historial(nombre:str) -> None:
    """
    Verifica si el jugador existe y muestra su puntaje.
    devuelve el mensaje con su puntaje, sino existe lo guarda
    """
    puntuaciones = leer_historial()  # lee puntuaciones desde el archivo
    
    if nombre in puntuaciones:
        return f"¡Hola {nombre}! Tu puntaje histórico es: {puntuaciones[nombre]}"
    
    else:# Guardar el nuevo jugador en el archivo
        puntuaciones[nombre] = 0  # Puntaje inicial al nuevo jugador
        guardar_puntuaciones(puntuaciones)  
        return (f"¡Bienvenido, {nombre}! Eres un nuevo jugador.")
        
