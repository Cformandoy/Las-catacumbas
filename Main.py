""" Cformandoy@gmail.com
Cristopher Pozas Formandoy

Desafio Final Boss Aprende a programar con Python
 """

import time
import msvcrt
import os
import random


clear = lambda: os.system('cls')
hacha = False


clear()

print("________________________________________________________________________________________________________________________\n")
print("Bienveni@ a las catacumbas, un laverinto en el que tendras que dar todo tu esfuerzo para salir con vida. jajaja suerte...")
print("\n________________________________________________________________________________________________________________________")


print("Presione una tecla para continuar...")
msvcrt.getch()

clear()

print("________________________________________________________________________________________________________________________\n")
print("Luego de una noche de fiesta, has despertado en medio de unas sombrias catacumbas. Con la poca luz que proviene de unas ")
print("antiguas antorchas, logras divisar que el lugar se encuentra repleto de telarañas gigantes, lo que te hace entrar en ")
print("desesperacion y querer huir del lugar lo mas rapido posible.")
print("\n________________________________________________________________________________________________________________________")

print("Presione una tecla para continuar...")
msvcrt.getch()

clear()

print("________________________________________________________________________________________________________________________\n")
print("Logras divisar tres caminos:")
print("\n-A El primero se ve oscuro y estrecho.")
print("-B En el segundo se logra ver luz al final de este.")
print("-C Mientras que de el tercero, se ve una escalera de mano que guia hacia arriba.")

opcion = input("\n¿Por cual camino deseas huir? [A-B-C]").upper()

print("\n________________________________________________________________________________________________________________________")

if opcion == "A":
    clear()

    print("________________________________________________________________________________________________________________________\n")
    print("El camino comienza estrecho continuando con una leve curva hacia la derecha, en donde llegas a un cuarto con muchos huevos de araña(si son gigantes)")
    print("y la madre araña esta cuidando de ellos, pero entremedio de todos los huevos, logras divisar un hacha resplandeciente.")
    print("\n________________________________________________________________________________________________________________________")
    
    print("Presione una tecla para continuar...")
    msvcrt.getch()
    
    clear()
    opcion = input("\n¿Tomaras el hacha, considerando que esta entremedio de todos los huevos? [S/N]").upper()
    if opcion == "S" or opcion =="SI":
        clear()

        numero_random = random.randint(1,100)

        print("________________________________________________________________________________________________________________________\n")
        print("Para lograr recoger el hacha sin despertar a la araña madre, deberas acertar al siguiente desafio aritmetico:")
        print("\nIngrese el resultado de : 15 * {} ".format(numero_random))
        print("\n________________________________________________________________________________________________________________________")

        desafio = input("Resultado:")
        
        if desafio == str(15*numero_random):
            clear()

            hacha = True

            print("________________________________________________________________________________________________________________________\n")
            print("Genial haz logrado tomar el hacha sin despertar a la araña, eres genial.")
            print("\n+1 Hacha")
            print("\n________________________________________________________________________________________________________________________")
        else:
            clear()
            
            print("________________________________________________________________________________________________________________________\n")
            print("Oh... no, la araña se ha comenzado a mover, es mejor que salgas de aqui lo mas rapido posible. Tendras que dejar el hacha donde esta.")
            print("\n________________________________________________________________________________________________________________________")
    else:
        clear()

        print("________________________________________________________________________________________________________________________\n")
        print("Es mejor concentrarte en escapar, ademas quien necesita un hacha.")
        print("\n________________________________________________________________________________________________________________________")
    
    print("Presione una tecla para continuar...")
    msvcrt.getch()

    clear()

    print("________________________________________________________________________________________________________________________\n")
    print("Para continuar tu camino, hay dos caminos diferentes:")
    print("\n-A Un pasillo en el que al fondo se logra ver luz, pero esta lleno de telarañas.")
    print("-B Un pasillo oscuro, pero sin telarañas.")

    opcion = input("\n¿Por cual camino deseas huir? [A-B]").upper()

    print("\n________________________________________________________________________________________________________________________")


    if opcion =="A":
        clear()

        print("________________________________________________________________________________________________________________________\n")
        print("Haz crusado el pasillo, y tu cuerpo esta lleno de telarañas, y lo peor de todo es que haz ")
        print("llegado al nido de la araña mas gigante que ha existido en la tierra.")
        print("\nLamentablemente tus opciones para huir han llegado hasta aqui. Esperemos que la araña te mate antes de comerte.\n\nFIN")
        print("\n________________________________________________________________________________________________________________________")
        
        print("Presione una tecla para salir...")
        msvcrt.getch()
    elif opcion =="B":
        clear()
        
        print("________________________________________________________________________________________________________________________\n")
        print("Cruzas el pasillo oscuro lentamente, y cuando vas llegando al final, miras hacia atras y ves muchos ojos rojos mirandote(si es momento de correr).")
        print("\nPara tu suerte al final del pasillo hay unas escaleras de mano, las subes con todo tu esfuerzo, pero para lograr ")
        print("salir hacia arriba hay una trampilla de madera muy gruesa.")
        print("\n________________________________________________________________________________________________________________________")
        
        print("Presione una tecla para continuar...")
        msvcrt.getch()

        if hacha == True:
            clear()
        
            print("________________________________________________________________________________________________________________________\n")
            print("recuerdas que tomaste el hacha entre los huevos de araña, rompes la madera, y logras salir a la superficie.")
            print("\nHaz logrado escapar de las catacumbas, y es momento de regresar a casa.\n\nFIN ")
            print("\n________________________________________________________________________________________________________________________")
            
            print("Presione una tecla para salir...")
            msvcrt.getch()
        else:
            clear()

            print("________________________________________________________________________________________________________________________\n")
            print("Intentas romper la madera con tus puños... si tan solo tuvieses una herramienta para romperla.")
            print("Los ojos rojos se acercan cada vez mas, ya logras ver que es una araña gigante, la araña mas gigante que ha existido en la tierra.")
            print("\nLamentablemente tus opciones para huir han llegado hasta aqui. Esperemos que la araña te mate antes de comerte.\n\nFIN")
            print("\n________________________________________________________________________________________________________________________")
            
            print("Presione una tecla para salir...")
            msvcrt.getch()
    else:
        clear()

        print("________________________________________________________________________________________________________________________\n")
        print("Haz ingresado una opcion no valida \nLamentablemente una araña gigante te ha visto. Esperemos que la araña te mate antes de comerte.\nFIN")
        print("\n________________________________________________________________________________________________________________________")
        print("Presione una tecla para salir...")
        msvcrt.getch()

elif opcion == "B":
    clear()

    print("________________________________________________________________________________________________________________________\n")
    print("Creo que haz tomado la peor decision de toda tu vida, haz crusado el pasillo, y haz llegado al nido de la araña mas gigante que ha existido en la tierra.")
    print("\nLamentablemente tus opciones para huir han llegado hasta aqui. Esperemos que la araña te mate antes de comerte.\n\nFIN")
    print("\n________________________________________________________________________________________________________________________")
    
    print("Presione una tecla para salir...")
    msvcrt.getch()


elif opcion == "C":
    clear()

    print("________________________________________________________________________________________________________________________\n")
    print("Decides ir directamente a la escalera y cuando estas a punto de llegar, miras hacia atras y ves unos muchos ojos rojos mirandote(si es momento de correr).")
    print("Llegas a las escaleras, las subes con todo tu esfuerzo, pero para lograr salir hacia arriba hay una trampilla de madera muy gruesa.")
    print("Intentas romper la madera con tus puños... si tan solo tuvieses una herramienta para romperla.")
    print("\nLos ojos rojos se acercan cada vez mas, ya logras ver que es una araña gigante, la araña mas gigante que ha existido en la tierra.")
    print("\nLamentablemente tus opciones para huir han llegado hasta aqui. Esperemos que la araña te mate antes de comerte.\n\nFIN")
    print("\n________________________________________________________________________________________________________________________")
    
    print("Presione una tecla para salir...")
    msvcrt.getch()

else:
    clear()

    print("________________________________________________________________________________________________________________________\n")
    print("Haz ingresado una opcion no valida \nLamentablemente una araña gigante te ha visto. Esperemos que la araña te mate antes de comerte.\nFIN")
    print("\n________________________________________________________________________________________________________________________")
    print("Presione una tecla para salir...")
    msvcrt.getch()


