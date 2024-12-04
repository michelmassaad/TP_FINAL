from .baraja import *
from .repartir import *
from .dibujo_pygame import *
from informacion.posiciones_dibujo import *
from informacion.colores import COLOR_FONDO
    
def mover_jugador(evento:any, mano_jugador:list, lista_carta_seleccionada:list, turno_jugador:bool, turno_computadora:bool, 
                  PANTALLA:any) -> tuple:
    """Maneja el movimiento de las cartas del jugador."""
    if turno_jugador:
        for carta in mano_jugador:
            if carta["rect"].collidepoint(evento.pos) and not carta["elegida"]:
                lista_carta_seleccionada.append(carta)
                carta["elegida"] = True

                pg.draw.rect(PANTALLA, COLOR_FONDO, carta["rect"])
                mover_carta(PANTALLA, lista_carta_seleccionada, coordenadas_j, espacio, tamano_cartas,
                            coordenadas_mesa_jugador)

                turno_jugador = False
                turno_computadora = True
                break
    return turno_jugador, turno_computadora


def mover_computadora(personaje_elegido:dict, mano_computadora:list, lista_lanzada_computadora:list,
                      lista_carta_seleccionada:list, turno_jugador:bool, turno_computadora:bool, PANTALLA:any) -> tuple:
    """Maneja el movimiento de las cartas de la computadora."""
    if turno_computadora:
        for carta_lanzada_computadora in mano_computadora:
            if not carta_lanzada_computadora["elegida"]:
                carta_lanzada_computadora = personaje_elegido["estrategia"](mano_computadora,lista_carta_seleccionada)

                carta_lanzada_computadora["elegida"] = True
                lista_lanzada_computadora.append(carta_lanzada_computadora)

                pg.time.wait(800)
                pg.draw.rect(PANTALLA, COLOR_FONDO, carta_lanzada_computadora["rect"])
                mover_carta(PANTALLA, lista_lanzada_computadora, coordenadas_c, espacio, tamano_cartas, 
                            coordenadas_mesa_computadora)

                turno_jugador = True
                turno_computadora = False
                break
    return turno_jugador, turno_computadora

def dibujar_pantalla_juego(PANTALLA:any, mano_jugador:list, mano_computadora:list, puntos_jugador:int, 
                             puntos_computadora:int, posiciones_jugadores:list,area_cartas:any, sonido_barajear:any, 
                             reverso_carta:any, posicion_mazo:tuple):
    """
    Dibuja todos los elementos principales en la pantalla para jugar cada ronda.
    """
    PANTALLA.fill(COLOR_FONDO)  # Redibuja la pantalla
    
    dibujar_marcador(PANTALLA,f"{puntos_jugador}",COLOR_MARCADOR,BLANCO,
                                    p_marcador_jugador,TAMANO_MARCADOR)
    dibujar_marcador(PANTALLA,f"{puntos_computadora}",COLOR_MARCADOR,BLANCO,
                                        p_marcador_computadora,TAMANO_MARCADOR)
    animacion_repartir(posiciones_jugadores,area_cartas,sonido_barajear,reverso_carta,posicion_mazo)

    dibujar_cartas(PANTALLA, mano_jugador, coordenadas_j, espacio, tamano_cartas)
    dibujar_cartas_dorso(PANTALLA, mano_computadora, coordenadas_c, espacio, tamano_cartas)

    pg.display.flip()
