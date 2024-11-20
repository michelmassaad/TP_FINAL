
personajes = {
    "Personaje 1": {
        "nombre": "Don PEPE",
        "descripcion": (
            "Juega  sus cartas aleatoriamente y que siempre que tiene envido"
            "(dos cartas del mismo palo) lo canta o acepta si le cantan, y si "
            "tiene más de 30 puntos canta falta envido "
        ),
        "estrategia": "aleatoria",
        # "envido": lambda dos_cartas_mismo_palo: canta_envido(dos_cartas_mismo_palo),
        "falta envido": lambda puntos: puntos >= 30,
    },
    
    "Personaje 2": {
        "nombre": "Don JUAN",
        "descripcion": (
            " Juega primero siempre su carta más alta y "
            "si juega segundo y tiene carta para empatar o ganar la mano jugará esa"
            " caso contrario jugará la más baja, "
            "con respecto al envido lo canta o acepta solo cuando tiene más de"
            "27 puntos."
        ),
        "estrategia": "inteligente",
        "envido": lambda puntos: puntos > 27,
    },
}

def elegir_personaje():
    pass
#     input(f"Elije contra quien deseas jugar:")