Figura=int(input("Ingrese 1 Si quiere calcular el area de un circulo o 2 si quiere calcular el area de un triangulo: "))

if Figura ==2:
    base=int(input("Ingrese la base del triangulo: "))
    Altura=int(input("Ingrese la altura del triangulo: "))
    area= (base*Altura)/2
    print("El area del triangulo es: ",area)
elif Figura==1:
    radio=int(input("Ingrese el radio del circulo: "))
    cuadrado=radio*radio
    area=3.141592*cuadrado
    print("El area del circulo es: ",area)