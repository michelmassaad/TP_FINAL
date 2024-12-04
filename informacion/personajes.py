import random
from funciones.estrategia_personajes import estrategia_inteligente

personajes = {
    "Personaje 1": {
        "nombre": "Aleatorio",
        "descripcion": (
            "Juega  sus cartas aleatoriamente y que siempre que tiene envido"
            "(dos cartas del mismo palo) lo canta o acepta si le cantan, y si "
            "tiene más de 30 puntos canta falta envido "
        ),
        #En la estrategia puse dos parametros porque uso el mismo llamado para ambos personajes, por lo tanto como tienen distintos parametros me saltaria error
        "estrategia": lambda cartas,lista_carta_seleccionada=None: random.choice([carta for carta in cartas if not carta.get("elegida", False)])
,
        # "envido": lambda dos_cartas_mismo_palo: canta_envido(dos_cartas_mismo_palo),
        "falta envido": lambda puntos: puntos >= 30,
    },
    
    "Personaje 2": {
        "nombre": "Inteligente",
        "descripcion": (
            " Juega primero siempre lanza su carta más alta y "
            "si juega segundo y tiene carta para empatar o ganar la mano jugará esa"
            " caso contrario jugará la más baja, "
            "con respecto al envido lo canta o acepta solo cuando tiene más de"
            "27 puntos."
        ),
        "estrategia": estrategia_inteligente,
        "envido": lambda puntos: puntos > 27,
    },
}
 