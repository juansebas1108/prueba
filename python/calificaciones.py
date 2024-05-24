cuenta70100=0
cuenta80=0

for i in range(5):
    code=input("Ingrese el Codigo del Estudiante: ")
    calificacion=float(input("Ingrese la Primera Calificacion del Estudiante: "))
    calificacion2=float(input("Ingrese la Seegunda Calificacion del Estudiante: "))
    promedio=(calificacion+calificacion2)/2
    
    if promedio >= 70 and promedio <= 100:
        cuenta70100 += 1
    if promedio >= 80:
        cuenta80 += 1
print("Entre 70 y 100 hay: ", cuenta70100)
print("Mas de 80 en Promedio hay: ", cuenta80)
    
    