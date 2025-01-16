#Desarrolla en Python el juego de Piedra, Papel y Tijeras en donde pedirás 
# por teclado la opción del jugador 1, luego la opción del jugador 2,
 #y posteriormente dará el resultado diciendo quien gano.
menu_jugador_1="""
    JUGADOR 1 Ingrese el numero de la opcion que desea escoger  
    1. PIEDRA
    2. PAPEL
    3. TIJERA
    """
option_1=int(input(menu_jugador_1))

menu_jugador_2="""
    JUGADOR 2 Ingrese el numero de la opcion que desea escoger  
    1. PIEDRA
    2. PAPEL
    3. TIJERA
    """
option_2=int(input(menu_jugador_2))


if option_1==2 and option_2==1:
    print('JUGADOR 1 ha ganado')
elif option_1==3 and option_2==1:
    print('JUGADOR 2 ha ganado ')
elif option_1==1 and option_2==2:
    print('JUGADOR 2 ha ganado')
elif option_1==3 and option_2==2:
    print('JUGADOR 1 ha ganado ')
elif option_1==1 and option_2==3:
    print('JUGADOR 1 ha ganado ')
elif option_1==2 and option_2==3:
    print('JUGADOR 2 ha ganado ')
else:
    print('Quedan empatados')



