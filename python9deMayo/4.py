numero = input("Ingrese un número entero positivo de hasta tres cifras: ")

if numero.isdigit():
    numero = int(numero)
    if numero < 0:
        print("El número debe ser positivo.")
    elif 0 < numero < 10:
        print("El número tiene 1 cifra.")
    elif 10 <= numero < 100:
        print("El número tiene 2 cifras.")
    elif 100 <= numero < 1000:
        print("El número tiene 3 cifras.")
    else:
        print("El número tiene más de tres cifras.")
else:
    print("Por favor, ingrese un número entero válido.")