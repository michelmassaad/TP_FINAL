from datos.personajes import elegir_personaje
from funciones import *

#Listado cartas
# Crear los palos y valores
palos = ["oros", "copas", "espadas", "bastos"]
valores = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]

#Cantidad de puntos por partida
puntos_para_ganar = [15,30]

#Crear baraja para cada uno de los jugadores
cant_cartar_en_mano = 3
#Crear Jugadores
cant_jugadores = 2

partida_en_juego = True
ronda_ganada = False
while partida_en_juego == True:

    print("\nJuguemos al Truco!!!")
    print("\nElije que hacer:")
    print("1- Jugar nuevo juego")
    print("2- Salir")

    opcion = int(input("Ingrese la opción que desea realizar: "))

    match opcion:
        case 1:
            #Partida
            #Nombre de jugador
            nombre = input("Ingresa tu nombre para comenzar la partida: ")
            print(f"\nEmpecemos {nombre}")
            #verificar si esta registrado el usuario 
            # si esta actualizar puntaje historico (sumar al anterior) y 
            # sino crear puntaje y registrarlo en archivo
            
            # Este diccionario se utiliza mientras se ejecuta el juego
            datos_del_partida = {
                "Nombre" : nombre,
                "Puntos": 0
            }

            #Escojer personaje a enfrentar
            # personaje_seleccionado = elegir_personaje()
            # print(f"Has elegido jugar contra: {personaje_seleccionado['nombre']}")
            
            #escojer para cuantos puntos se quiere jugar
            print("\n¿A cuántos puntos quieres jugar?")
            puntos_a_jugar = int(input("Ingresa 15 o 30: "))

            while puntos_a_jugar not in puntos_para_ganar:
                print("Opción inválida. Solo puedes elegir 15 o 30.")
                puntos_a_jugar = int(input("Ingresa 15 o 30: "))
            
            print(f"La partida será a {puntos_a_jugar} puntos.\n")
            
            #Crear baraja con las cartas a jugar
            baraja = crear_baraja(palos,valores)
            # mostrar_barajas(baraja)            
            
            #Barajear las cartas
            cartas_barajeadas = barajear_cartas(baraja)
            # mostrar_barajas(cartas_barajeadas)

            #Empieza La Ronda
            # while ronda_ganada == True:
            if datos_del_partida["Puntos"] < puntos_a_jugar: 
                #Repartir las cartas
                mano_jugador = repartir_cartas(cartas_barajeadas)
                mano_computadora = repartir_cartas(cartas_barajeadas)
                # Mostrar las manos
                print("Mano del jugador:", mano_jugador)
                print("Mano de la máquina:", mano_computadora)

            #escojer si se quiere envido en la primera mano
            
            #escojer si se va a jugar truco en cada unas de las partidas
            
            #una vez se elijio si sera truco o envido, se juegan las cartas
            #por movimiento hasta terminar ronda
            
            #Sumar ronda a puntajes
        
        case 2:            
            partida_en_juego = False
            
        case _:
            print("Debe seleccionar una opcion valida!!")

