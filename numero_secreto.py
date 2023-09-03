import random

def adivinar_numero():
    numero_secreto = random.randint(1,50)

    while True:
        try:
            intento = int(input("adivina el numero entre 1 y 50: "))
            if intento == numero_secreto:
                print("Correcto ¡ADIVINASTE!")
                break
            elif intento < numero_secreto:
                print("El numero es mas alto, intenta nuevamente")
            else:
                print("El numero es mas bajo, intenta nuevamente")
        except ValueError:
            print ("ERROR, ingresa solo numeros validos")

adivinar_numero()