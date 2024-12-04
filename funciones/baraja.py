import random
import pygame as pg

def crear_carta(palo:tuple, valor:tuple, jerarquia:dict, envido:any, ruta_base:str)->dict:
    '''Crea un diccionario para una cada una de las cartas'''
    return {
        "palo": palo,
        "valor": valor,
        "jerarquia": jerarquia,
        "envido": envido,
        "ruta": f"{ruta_base}/{valor} de {palo}.jpg"
    }
    
def crear_baraja(palos:tuple, valores:tuple, jerarquia_truco:dict, ruta:str)-> list:
    '''Crea la baraja entera y llama a la funcion crear_carta para asignarle los 
        valores al diccionario a crear para cada una de las carta'''
    baraja = []
    for palo in palos:
        for valor in valores:
            #Analizo jerarquia para guardarla en diccionario
            if (palo, valor) in jerarquia_truco:
                jerarquia = jerarquia_truco[(palo, valor)]
            elif ('', valor) in jerarquia_truco:
                jerarquia = jerarquia_truco[('', valor)]
                
            envido = valor if valor <= 7 else 0
            
            #agrego al diccionario
            baraja.append(crear_carta(palo, valor, jerarquia, envido, ruta))
    return baraja

def barajear_cartas(baraja:list)->list:
    '''Barajea la baraja completa '''
    baraja_mezclada = baraja[:]
    random.shuffle(baraja_mezclada)
    return baraja_mezclada


def asignar_posiciones(cartas:list, coordenadas_iniciales:tuple, espacio:float, tamano_carta:tuple) -> None:
    """Asigna las posiciones iniciales a las cartas."""
    x, y = coordenadas_iniciales
    for carta in cartas:
        carta["x"] = x
        carta["y"] = y
        carta["rect"] = pg.Rect(x, y, tamano_carta[0], tamano_carta[1])  # Define un área de interacción.
        x += tamano_carta[0] + espacio
        #creo un atributo dentro del diccionario
        carta["elegida"] = False
