edad = int(input("Por favor, introduce la edad del cliente: "))

if edad < 0:
    print("La edad no puede ser un número negativo.")
elif edad < 4:
    print("El cliente puede entrar gratis.")
elif edad <= 18:
    print("El precio de la entrada es: 5€")
else:
    print("El precio de la entrada es: 10€")