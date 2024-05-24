#En una empresa trabajan n empleados cuyos sueldos oscilan entre $100 y $500,
#realizar un programa que lea los sueldos que cobra cada empleado e informe
#cuántos empleados cobran entre $100 y $300 y cuántos cobran más de $300.
#Además el programa deberá informar el importe que gasta la empresa en sueldos
#al personal.

acusueldo=0.0
conta100500=0
contamas500=0

nempleados=int(input("Ingrese el Numero de Empleados: "))
for i in range(nempleados):
    sueldo=float(input("Ingrese su sueldo  : "))
    if sueldo >100 and sueldo <=300:
        conta100500 +=1
        acusueldo=acusueldo+sueldo 

    if sueldo > 300:
        contamas500 +=1
        acusueldo=acusueldo+sueldo 

print("El numero de empleados que ganan entre 100 y 300 es: ",conta100500)
print("El numero de empleados que cobran mas de 300 es: ",contamas500)
print("El total que gasta la empresa en sueldos es: ",acusueldo)


