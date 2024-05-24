Año1=int(input("Ingrese el primer año: "))
Año2=int(input("Ingrese el segundo año: "))
if Año1 < Año2:
    total=Año2-Año1
    print("Desde el año ",Año1," Hasta el año ",Año2," Han pasado ",total," Años")

else:
    total2=Año1-Año2
    print("Al año ",Año1," Para llegar al ",Año2," Le faltan ",total2," Años ")