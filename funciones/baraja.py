import random

def crear_baraja(palos,valores):
    baraja = []
    for palo in palos:
        for valor in valores:
            baraja += [(valor, palo)]
            
    return baraja

def barajear_cartas(baraja:list)->list:
    baraja_mezclada = baraja[:]
    random.shuffle(baraja_mezclada)
    return baraja_mezclada

def mostrar_barajas(cartas:list)->None:
    for filas in cartas:
        print(filas)
        