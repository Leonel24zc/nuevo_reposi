def division():
    try:
        n1 = float(input("Ingrese primer numero: "))
        n2 = float(input("Ingrese segundo numero: "))
        resultado = n1/n2
        print("El resultado de la division es:",resultado)

    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero ")
    except ValueError:
        print("Error: Ingrese solo numeros validos ")
    
division()