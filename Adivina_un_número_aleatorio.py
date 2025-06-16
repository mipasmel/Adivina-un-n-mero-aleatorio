# Adivina un número aleatorio entre el 1 y el 100

import random
print ("Bienvenido al juego de adivinar un número al azar.\n")
print ("Estoy pensando un número del 1 al 100, ¿Adivinas cuál?")
numero = random.randint(1, 100)
while True:
    respuesta = int (input ("Dime un número: "))
    if respuesta < numero:
        print (f"Es más alto que {respuesta}")
    elif respuesta > numero:
        print (f"Es más bajo que {respuesta}")
    else:
        print (f"¡Felicidades, has acertado!")
        break