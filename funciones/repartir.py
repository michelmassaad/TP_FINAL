
def repartir_cartas(baraja:list, cantidad_cartas:int=3) -> list:
    """
    Reparte una cantidad específica de cartas de la baraja.
    Recibe
    Devuelve
    """
    mano = baraja[:cantidad_cartas]  # Toma las primeras cartas disponibles
    del baraja[:cantidad_cartas]    # Elimina esas cartas de la baraja
    return mano
