import pygame as pg
import sys

from informacion import *
from funciones import *

pg.init()
pg.mixer.init()
from informacion.audio import sonido_barajear, sonido_lanzar_carta

#Pantallas a para seleccionar por defecto comienzo en la 1
modalidad = 1

#Crear baraja con las cartas a jugar
baraja = crear_baraja(PALOS,VALORES,jerarquia_truco, ruta_base_imagenes)
baraja_barajeadas = barajear_cartas(baraja)  #Barajear las cartas
cantidad_cartas = 3

#Inicio la clase Estado Juego
estado_juego = EstadoJuego(baraja_barajeadas, cantidad_cartas)
estado_truco = Truco(baraja_barajeadas, cantidad_cartas)

# Variables para gestionar el estado inicial
modo_seleccionado = None
puntos_max = None

#creo reloj para administrar ftps
clock = pg.time.Clock()

ejecutar_juego = True
while ejecutar_juego:
    #Dibujar cartas ambos jugadores     
    
    #Hay que crear varias pantallas
    if modalidad == 1: #inicio
        #Elementos basicos del inicio
        pantalla_inicio(PANTALLA, FUENTE_TITULO, nombre_enviado ,nombre_ingresado , texto_historial)
        
        #dibujo los botones necesarios
        (rect_boton_enviar, rect_modo_aleatorio, rect_modo_inteligente,
         rect_puntos_15, rect_puntos_30, rect_boton_nuevo_juego) = dibujar_botones_inicio(
            nombre_enviado, modo_seleccionado, puntos_max, FUENTE_TEXTO)

        # Manejo de eventos
        for evento in pg.event.get():
            if evento.type == pg.QUIT:
                ejecutar_juego = False
    
            if evento.type == pg.MOUSEBUTTONDOWN and evento.button == 1:
                #Boton para enviar el nombre
                if not nombre_enviado and presionar_boton(rect_boton_enviar, evento): 
                    if nombre_ingresado.strip():  # Enviar nombre solo si no está vacío
                        texto_historial = verificar_historial(nombre_ingresado.capitalize())
                        nombre_enviado = True
                
                #Eleccion de oponente
                if presionar_boton(rect_modo_aleatorio, evento): 
                    modo_seleccionado = "Aleatorio"
                    personaje_elegido = personajes["Personaje 1"]
                elif presionar_boton(rect_modo_inteligente, evento):
                    modo_seleccionado = "Inteligente"
                    personaje_elegido = personajes["Personaje 2"]
                
                #Eleccion de puntos a jugar
                if presionar_boton(rect_puntos_15, evento):
                    puntos_max = 15
                if presionar_boton(rect_puntos_30, evento):
                    puntos_max = 30

                #Boton nuevo juego
                if presionar_boton(rect_boton_nuevo_juego, evento) and nombre_enviado and modo_seleccionado and puntos_max:
                    # print("Iniciar nuevo juego...")
                    modalidad = 2

            #Evento de entrada de Texto del usuario
            if evento.type == pg.KEYDOWN and not nombre_enviado:
                if evento.key == pg.K_BACKSPACE:
                    nombre_ingresado = nombre_ingresado[:-1]
                elif len(nombre_ingresado) < 20:  # Limitar la longitud del nombre
                    nombre_ingresado += evento.unicode
    
            # Actualizar pantalla
            pg.display.update()
                    
    elif modalidad == 2: # Pantalla Juego 
        
        if estado_juego.ronda == 0: #Inicio de juego
            estado_juego.iniciar_ronda()
            dibujar_pantalla_juego(PANTALLA, estado_juego.mano_jugador, estado_juego.mano_computadora,
                               estado_juego.puntos_jugador , estado_juego.puntos_computadora,
                               posiciones_jugadores, area_cartas, sonido_barajear, reverso_carta, posicion_mazo)
            
        #Verifico evento Mouse
        for evento in pg.event.get(): #verifico la salida
            if evento.type == pg.QUIT:
                ejecutar_juego = False
                
            elif evento.type == pg.MOUSEBUTTONDOWN and evento.button == 1: #seleccion por mouse 
                # Movimientos del jugador
                estado_juego.turno_jugador, estado_juego.turno_computadora = mover_jugador(
                    evento, estado_juego.mano_jugador, estado_juego.lista_carta_seleccionada, estado_juego.turno_jugador,
                    estado_juego.turno_computadora, PANTALLA)
                
                # Verificar evento botones
                for texto, boton in botones_activos:
                    if presionar_boton(boton, evento):
                        #region Actualizar el estado del juego_truco_envido según el botón presionado
                        if texto == "Truco" and not estado_truco.Truco:  # Si Truco aún no se ha cantado
                            estado_truco.canto_actual = "Truco"
                            (estado_truco.respuestas_validas, estado_truco.respuesta_compu, 
                             estado_truco.puntos_a_sumar) = estado_truco.cantar_responder(
                                estado_truco.canto_actual,puntos_max)

                        elif texto == "Retruco" and estado_truco.Truco and not estado_truco.Retruco:  # Si Truco ya fue cantado y Retruco no
                            estado_truco.canto_actual = "Retruco"
                            (estado_truco.respuestas_validas, estado_truco.respuesta_compu, 
                             estado_truco.puntos_a_sumar) = estado_truco.cantar_responder(
                                estado_truco.canto_actual,puntos_max)
                        
                        elif texto == "Vale 4" and estado_truco.Truco and estado_truco.Retruco and not estado_truco.Vale_4:  # Si Truco y Retruco fueron cantados y Vale 4 no
                            estado_truco.canto_actual = "Vale 4"
                            (estado_truco.respuestas_validas, estado_truco.respuesta_compu, 
                             estado_truco.puntos_a_sumar) = estado_truco.cantar_responder(
                                estado_truco.canto_actual,puntos_max)
                        
                        elif texto == "Envido" and not estado_truco.Envido :  # Si Envido aún no se ha cantado y Truco no está activo
                            estado_truco.canto_actual = "Envido"
                            (estado_truco.respuestas_validas, estado_truco.respuesta_compu, 
                             estado_truco.puntos_a_sumar) = estado_truco.cantar_responder(
                                estado_truco.canto_actual,puntos_max)

                        elif texto == "Real Envido" and estado_truco.Envido and not estado_truco.Real_Envido:  # Si Envido ya fue cantado, pero no Real Envido
                            estado_truco.canto_actual = "Real Envido"
                            (estado_truco.respuestas_validas, estado_truco.respuesta_compu, 
                             estado_truco.puntos_a_sumar) = estado_truco.cantar_responder(
                                estado_truco.canto_actual,puntos_max)

                        elif texto == "Falta Envido" and estado_truco.Envido and estado_truco.Real_Envido and not estado_truco.Falta_Envido:  # Si se cantó Envido o Real Envido, pero no Falta Envido
                            estado_truco.canto_actual = "Falta Envido"
                            (estado_truco.respuestas_validas, estado_truco.respuesta_compu, 
                             estado_truco.puntos_a_sumar) = estado_truco.cantar_responder(
                                estado_truco.canto_actual,puntos_max)

                        #respuestas del jugador
                        elif texto == "Quiero" and texto in estado_truco.opciones_respuesta and not estado_truco.No_quiero:  # Si las opciones habilitadas incluyen "Quiero"
                            estado_truco.canto_actual = "Quiero"  
                            estado_truco.puntos_a_sumar = estado_truco.jugador_responde(estado_truco.canto_actual)

                        elif texto == "No quiero" and texto in estado_truco.opciones_respuesta and not estado_truco.Quiero :  # Si las opciones habilitadas incluyen "No quiero"
                            estado_truco.canto_actual = "No quiero" 
                            if estado_truco.Truco or estado_truco.Retruco or estado_truco.Vale_4:
                                estado_truco.partida = False
                            estado_truco.puntos_a_sumar = estado_truco.jugador_responde(estado_truco.canto_actual)
                        #endregion
        
        # Dibujar los botones activos según el estado del juego
        botones_activos = mostrar_botones_canto(PANTALLA, botones_cantos, estado_juego.turno_jugador, 
                                                estado_truco.canto_actual, estado_truco.respuestas_validas)

        # Movimientos de la computadora
        estado_juego.turno_jugador, estado_juego.turno_computadora = mover_computadora(
        personaje_elegido, estado_juego.mano_computadora, estado_juego.lista_lanzada_computadora,estado_juego.lista_carta_seleccionada, estado_juego.turno_jugador,
        estado_juego.turno_computadora, PANTALLA)

        #Condicion para cuando quedan menos de 6 cartas en la baraja para que reinicie la baraja y 
        # no quedarse sin cartas de vuelta 
        if len(estado_juego.baraja_barajeadas) < 6:
            estado_juego.baraja_barajeadas = barajear_cartas(baraja)

        #Condicion para limpiar las cartas de la mesa cuando ya todas fueron elegidas o la partida es terminada
        if (all(carta["elegida"] for carta in estado_juego.mano_jugador) and 
            all(carta["elegida"] for carta in estado_juego.mano_computadora)) or estado_truco.partida == False:
            
            #Calcular_puntos
            if estado_truco.partida == True: #si la partida continuo con sus cantos respectivos
                estado_juego.puntos_jugador, estado_juego.puntos_computadora = verificar_ganador_truco(
                            estado_juego.lista_carta_seleccionada,estado_juego.lista_lanzada_computadora,
                            estado_juego.puntos_jugador,estado_juego.puntos_computadora,estado_truco.puntos_a_sumar)
            
            else:#si la partida se corto por algun canto 
                #efecto terminar ronda
                pg.draw.rect(PANTALLA, COLOR_FONDO, area_cartas)
                pg.display.update(area_cartas)
                
                if estado_truco.canto_actual == "No quiero": # si el jugador dice no quiero entonces sumamos puntos a computadora
                    estado_juego.puntos_computadora += estado_truco.verficar_puntos_rechazos()
                elif estado_truco.respuesta_compu == "No quiero":
                    estado_juego.puntos_jugador += estado_truco.verficar_puntos_rechazos()
                    
            
            #reinicio la ronda
            estado_truco.reiniciar_valores_truco()  #reinicio los valores de los cantos 
            pg.time.wait(1500)
            
            #Condicion para terminar partida completa
            if estado_juego.puntos_jugador >= puntos_max or estado_juego.puntos_computadora >= puntos_max:
                #actualizo el registro en el archivo 
                texto_historial = actualizar_puntuacion(nombre_ingresado.capitalize(),estado_juego.puntos_jugador)
                #reinicio los Botones
                
                # Limpiar la pantalla
                PANTALLA.fill(COLOR_FONDO)

                # Dibujar los marcadores
                dibujar_marcador(PANTALLA,f"{estado_juego.puntos_jugador}",COLOR_MARCADOR,BLANCO,
                                                p_marcador_jugador,TAMANO_MARCADOR)
                dibujar_marcador(PANTALLA,f"{estado_juego.puntos_computadora}",COLOR_MARCADOR,BLANCO,
                                                    p_marcador_computadora,TAMANO_MARCADOR)
                
                if estado_juego.puntos_jugador > estado_juego.puntos_computadora:
                    # Mensaje de ganador, centrarlo en la pantalla
                    mensaje = f"!!Felicidades!! Has ganado {nombre_ingresado}"
                    fuente = pg.font.SysFont("Arial", 36)
                    superficie_texto = fuente.render(mensaje, True, COLOR_TEXTO)
                    # Obtener el rectángulo para centrar el texto en la pantalla
                    rect_texto = superficie_texto.get_rect(center=(ANCHO // 2, ALTO // 2))
                    
                elif estado_juego.puntos_jugador < estado_juego.puntos_computadora:
                    # Mensaje de ganador, centrarlo en la pantalla
                    mensaje = f"!!Lo siento!! Has perdido {nombre_ingresado}"
                    fuente = pg.font.SysFont("Arial", 36)
                    superficie_texto = fuente.render(mensaje, True, COLOR_TEXTO)
                    # Obtener el rectángulo para centrar el texto en la pantalla
                    rect_texto = superficie_texto.get_rect(center=(ANCHO // 2, ALTO // 2))
                    
                # Dibujar el texto
                PANTALLA.blit(superficie_texto, rect_texto)

                # Actualizar la pantalla
                pg.display.update()
                # Esperar 5 segundos
                pg.time.delay(5000)
                
                #reinicio los valores de la partida
                estado_juego.reinicio_valores(estado_juego.baraja_barajeadas)
                modalidad = 1
            else:
                estado_juego.iniciar_ronda() 
                dibujar_pantalla_juego(PANTALLA,estado_juego.mano_jugador,estado_juego.mano_computadora,
                                estado_juego.puntos_jugador,estado_juego.puntos_computadora,
                                posiciones_jugadores,area_cartas,sonido_barajear,reverso_carta,posicion_mazo)
                

            
    #para finalizar pantallas
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            ejecutar_juego = False
    
    #actualizar pantalla
    clock.tick(60)
    pg.display.update()
    
pg.mixer.music.stop()
pg.quit()

    
