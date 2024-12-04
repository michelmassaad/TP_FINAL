from informacion.colores import *
from .dibujo_pygame import *
from informacion.elementos_inicio import *

def pantalla_inicio(superficie:any, FUENTE_TITULO:any, nombre_enviado:bool,
                    nombre_ingresado:str, texto_historial:str)-> None:
    '''Crea todos los elementos basicos necesarios para la pantalla de inicio '''
    
    superficie.fill(COLOR_FONDO) 
    # Texto explicativo del nombre
    dibujar_texto(PANTALLA, "Ingrese su nombre:", COLOR_TEXTO, 
                (x_texto, 150 + 10))

    # Texto explicativo del modo de juego
    dibujar_texto(PANTALLA, "Elija un oponente: ", COLOR_TEXTO, 
                (x_texto, coordenadas_aleatorio[1] + 10))

    # Texto explicativo de los puntos
    dibujar_texto(PANTALLA, "Elije puntos a jugar:", COLOR_TEXTO, 
                (x_texto, coordenadas_puntos_15[1] + 10))
    
    # Título
    texto_titulo = FUENTE_TITULO.render("JUEGO DEL TRUCO!!!", True, BLANCO)
    PANTALLA.blit(texto_titulo, ((ANCHO - texto_titulo.get_width()) // 2, 50))
    
    # Dibujar entrada de texto
    rect_caja_texto = pg.Rect((ANCHO - 300) // 2, 150, 300, 40)
    pg.draw.rect(PANTALLA, COLOR_CAJA_TEXTO if not nombre_enviado else COLOR_BLOQUEADO, rect_caja_texto)
    texto_nombre = pg.font.SysFont("Arial", 20).render(nombre_ingresado.capitalize(), True, BLANCO)
    PANTALLA.blit(texto_nombre, (rect_caja_texto.x + 10, rect_caja_texto.y + 5))
    
    #dibujo respuesta nombre
    dibujar_texto(PANTALLA, f"{texto_historial}", BLANCO, (280,200), 22)
        
    
def dibujar_botones_inicio(nombre_enviado:bool, modo_seleccionado:str, PUNTOS_MAX:int, FUENTE_TEXTO:any) -> any:
    '''
    Dibujo los botones con sus verificaciones y devuelvo el rectangulo del mismo con sus dimensiones
    '''
    # Botón "Enviar"
    rect_boton_enviar = dibujar_boton(PANTALLA, "Enviar", COLOR_BOTON if not nombre_enviado else COLOR_BLOQUEADO, 
                                COLOR_TEXTO_BOTON, coordenadas_enviar, (100, 40))
    
    # Botones de modo
    rect_modo_aleatorio = dibujar_boton(PANTALLA, "Aleatorio", 
                                        COLOR_BOTON_SELECCIONADO if modo_seleccionado == "Aleatorio" else COLOR_BOTON, 
                                        COLOR_TEXTO_BOTON, coordenadas_aleatorio, (150, 60))
    rect_modo_inteligente = dibujar_boton(PANTALLA, "Inteligente", 
                                        COLOR_BOTON_SELECCIONADO if modo_seleccionado == "Inteligente" else COLOR_BOTON, 
                                        COLOR_TEXTO_BOTON, coordenadas_inteligente, (150, 60))

    # Botones de puntos
    rect_puntos_15 = dibujar_boton(PANTALLA, "15", 
                                COLOR_BOTON_SELECCIONADO if PUNTOS_MAX == 15 else COLOR_BOTON, 
                                COLOR_TEXTO_BOTON, coordenadas_puntos_15, (150, 60))
    rect_puntos_30 = dibujar_boton(PANTALLA, "30", 
                                COLOR_BOTON_SELECCIONADO if PUNTOS_MAX == 30 else COLOR_BOTON, 
                                COLOR_TEXTO_BOTON, coordenadas_puntos_30, (150, 60))
    
    # Verificación de la habilitación del botón "Nuevo Juego"
    if nombre_enviado and modo_seleccionado and PUNTOS_MAX:
        rect_boton_nuevo_juego = dibujar_boton(PANTALLA, "Nuevo Juego", COLOR_BOTON_SELECCIONADO, COLOR_TEXTO_BOTON, 
                                                coordenadas_nuevo_juego, (150, 60))
    else:
        rect_boton_nuevo_juego = dibujar_boton(PANTALLA, "Nuevo Juego", COLOR_BOTON, COLOR_TEXTO_BOTON, 
                                                coordenadas_nuevo_juego, (150, 60))
        # Mensaje de advertencia si no se han completado todos los campos
        texto_Advertencia = FUENTE_TEXTO.render("Por favor, complete todos los campos antes de iniciar el juego.",
                                                    True, ROJO)
        PANTALLA.blit(texto_Advertencia, ((ANCHO - texto_Advertencia.get_width()) // 2, 450))
    
    
    return (rect_boton_enviar , rect_modo_aleatorio , rect_modo_inteligente,
            rect_puntos_15 , rect_puntos_30 , rect_boton_nuevo_juego)
