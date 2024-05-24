sueldoquegana=int(input("Ingrese el sueldo que gana: "))
antiguedad=int(input("Ingrese cuantos años tiene en la empresa: "))
if sueldoquegana < 500 and antiguedad >= 10:
    sueldoquegana=sueldoquegana+sueldoquegana*20/100
    print("Su sueldo a pagar es de: ",sueldoquegana)
elif sueldoquegana<500 and antiguedad <10:
    sueldoquegana=sueldoquegana+sueldoquegana*5/100
    print("Su sueldo a pagar es de: ",sueldoquegana)
elif sueldoquegana > 500:
    print("Su sueldo no presenta cambios, sigue siendo de: ",sueldoquegana)

