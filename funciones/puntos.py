def verificar_rondas_ganadas_truco(lista_carta_seleccionada:list,
                                   lista_lanzada_computadora:list) -> tuple:
    '''
    verifica cada una de las manos jugadas con respecto a su jerarquia y toma los criterios 
    de deseempates posibles y lo almacena en un marcador de rondas luego retorna el marcador 
    de rondas ganadas
    '''
    rondas_ganadas_jugador = 0
    rondas_ganadas_computadora = 0
    manos_ganadas = []  # Lista para almacenar quién ganó cada mano
    
    for i in range(len(lista_carta_seleccionada)):
        carta_jugador = lista_carta_seleccionada[i]
        carta_computadora = lista_lanzada_computadora[i]
        
        if carta_jugador["jerarquia"] > carta_computadora["jerarquia"]:
            rondas_ganadas_jugador += 1
            manos_ganadas.append("jugador")  # El jugador gana esta mano
        elif carta_computadora["jerarquia"] >  carta_jugador["jerarquia"]:
            rondas_ganadas_computadora += 1
            manos_ganadas.append("computadora")  # La computadora gana esta mano
        else:
            manos_ganadas.append("empate")  # Empate en la mano

    #CRITERIO DE DESEMPATE
    # Ahora verificamos si las 3 rondas fueron jugadas
    if len(manos_ganadas) == 3:
        # Si las rondas ganadas son iguales, verificamos el empate en las manos
        if rondas_ganadas_jugador == rondas_ganadas_computadora:
            # Verificar si la primera mano fue empate
            if manos_ganadas[0] == "empate":
                # Si la primera fue empate, ver la segunda mano
                if manos_ganadas[1] == "jugador":
                    rondas_ganadas_jugador += 1  
                elif manos_ganadas[1] == "computadora":
                    rondas_ganadas_computadora += 1 
                else:
                    # Si también hay empate en la segunda, decidir con la tercera mano
                    if manos_ganadas[2] == "jugador":
                        rondas_ganadas_jugador += 1  
                    elif manos_ganadas[2] == "computadora":
                        rondas_ganadas_computadora += 1  
            else:
                # Si la primera mano no fue empate, le asignamos la ronda al que ganó la primera mano
                if manos_ganadas[0] == "jugador":
                    rondas_ganadas_jugador += 1  # El jugador gana la ronda por la primera mano
                else:
                    rondas_ganadas_computadora += 1  # La computadora gana la ronda por la primera mano

    # Al final, devolvemos el marcador
    return rondas_ganadas_jugador, rondas_ganadas_computadora

def verificar_ganador_truco(lista_carta_seleccionada:list,lista_lanzada_computadora:list,
                            puntos_jugador:int,puntos_computadora:int,puntos_a_sumar:int) -> tuple:
    '''
    Verifica quien tiene mas rondas ganadas
    devuelve los puntos de cada uno, recibiendo como parametro los puntos a sumar 
    '''
    rondas_ganadas_jugador, rondas_ganadas_computadora = verificar_rondas_ganadas_truco(
        lista_carta_seleccionada,lista_lanzada_computadora)
    
    puntos_ganados = puntos_a_sumar #parametro recibido dependiendo de lo que suceda con los cantos 
    
    if rondas_ganadas_jugador > rondas_ganadas_computadora:
        puntos_jugador += puntos_ganados
    elif rondas_ganadas_computadora > rondas_ganadas_jugador:
        puntos_computadora += puntos_ganados
    else:
        return 0

    return puntos_jugador, puntos_computadora

