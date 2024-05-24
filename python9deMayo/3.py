sumnega=0
contposi=0
sumposi=0

for i in range(6):
    num=int(input(f"Ingrese un numero: {i+1}"))
    if num<0:
        sumnega=sumnega+num

    elif num > 0:
        contposi=contposi+1
        sumposi=sumposi+num

        if contposi > 0:
            promedioposi=sumposi/contposi
            print("El promedio de los numeros positivos es de: ",promedioposi )
        else:
            print("No se ingresaron numeros positivos")
print("La suma de los numeros negativos es: ",sumnega)