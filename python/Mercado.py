acumuladototal=0
acupago=0
pdescuento=0
adescuento=0
descuento=0
for i in range(3):
    rproductor = input("Decime el producto ")
    valor=int(input("Dame el valor "))
    cmt=int(input("Dime la cantidad "))
    subtotal=valor*cmt
    acumuladototal=acumuladototal+subtotal

pdescuento=float(input("Ingrese el descuento"))
descuento=acumuladototal*pdescuento
pague=acumuladototal-descuento
acupago=acupago+pague
adescuento=adescuento+descuento
acupago=acupago+pague

print("El mercado te costo: ", acumuladototal, "Te descontaron: ",adescuento,"Vas a pagar", pague )