acutotal=0
nombre=0
vhora=0
horas=0
ganancia=0
for j in range(3):
    nombre=input("Ingrese el nombre: ")
    vhora=float(input("Ingrese lo que gana por hora: "))
    horas=float(input("Ingrese las horas trabajadas: "))
    ganancia=horas*vhora
    acutotal=acutotal+ganancia

    print("Su ganancia por hora es: ", vhora , "Trabajo: ", horas , "Horas","Se le pago: ", ganancia)
print("La nomina de la empresa cuesta; ",acutotal)

