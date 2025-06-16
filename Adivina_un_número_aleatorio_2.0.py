# Adivina un número aleatorio entre el 1 y el 100
# Cuenta los intentos
# Evita errores

import random
print ("Bienvenido al juego de adivinar un número al azar.\n")
print ("Estoy pensando un número del 1 al 100, ¿Adivinas cuál?")
numero = random.randint(1, 100)
intentos = 0
while True:
    try:
        respuesta = int (input ("Dime un número: "))
        intentos += 1
        if respuesta < numero:
            print (f"Es más alto que {respuesta}")
        elif respuesta > numero:
            print (f"Es más bajo que {respuesta}")
        else:
            print (f"\n¡Felicidades, has acertado en solo {intentos} intentos!")
            break
    except ValueError:
        print ("Introduce un número válido")
print ("\n¡Gracias por jugar!\n")