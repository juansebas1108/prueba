preguntas_totales = int(input("Ingrese la cantidad total de preguntas: "))
preguntas_correctas = int(input("Ingrese la cantidad de preguntas respondidas correctamente: "))

if preguntas_totales < 0 or preguntas_correctas < 0:
    print("Por favor, ingrese valores no negativos.")
elif preguntas_correctas > preguntas_totales:
    print("La cantidad de preguntas correctas no puede ser mayor que la cantidad total de preguntas.")
else:
    porcentaje_correctas = (preguntas_correctas / preguntas_totales) * 100

    if porcentaje_correctas >= 90:
        print("Nivel máximo")
    elif 75 <= porcentaje_correctas < 90:
        print("Nivel medio")
    elif 50 <= porcentaje_correctas < 75:
        print("Nivel regular")
    else:
        print("Fuera de nivel")