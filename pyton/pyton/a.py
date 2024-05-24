i=1,3,1
sub=0
cantidad=0
Prod=0
acsub=0
acdes=0
actotal=0
for i in range(3):
    Prod= (input("entre producto  "))
    cantidad = int(input("entre cantidad del producto  "))
    precio= int(input("entre precio del producto  "))
    sub=cantidad*precio
    acsub=acsub+sub
    des=(sub*10)/100
    acdes=acdes+des
    total=sub-des
    actotal=actotal+total
    
    
print( "El valor: ",actotal)

