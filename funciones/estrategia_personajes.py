def estrategia_inteligente(cartas:list, lista_carta_seleccionada:list) -> dict:
    '''
    Realiza la estrategia del jugador inteligente, 
    Juega primero siempre lanza su carta más alta y "
    "si juega segundo y tiene carta para empatar o ganar la mano jugará esa"
    " caso contrario jugará la más baja
    '''
    # Filtrar las cartas no elegidas (aquellas sin "elegida" o con "elegida" = False)
    cartas_no_elegidas = [carta for carta in cartas if not carta.get("elegida", False)]
    # print("Cartas disponibles:", cartas_no_elegidas)

    # Juega primero: no hay cartas en juego
    if not lista_carta_seleccionada or (len(cartas_no_elegidas) == 3 - len(lista_carta_seleccionada)):
        # print("juego primero")
        carta_a_jugar = max(cartas_no_elegidas, key=lambda carta: carta["jerarquia"])  # Juega la carta más alta
        carta_a_jugar["elegida"] = True  # Marca la carta como elegida
        return carta_a_jugar

    # Juega segundo: hay cartas jugadas
    carta_en_juego = lista_carta_seleccionada[-1]  # Última carta jugada por el otro jugador

    # Intentar ganar o empatar
    for carta in cartas_no_elegidas:
        if carta["jerarquia"] >= carta_en_juego["jerarquia"]:  # Puede ganar o empatar
            carta["elegida"] = True  # Marca la carta como elegida
            return carta

    # Si no puede ganar, juega la carta más baja
    carta_a_jugar = min(cartas_no_elegidas, key=lambda carta: carta["jerarquia"])
    carta_a_jugar["elegida"] = True  # Marca la carta como elegida
    return carta_a_jugar
