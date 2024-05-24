'''Ferreteria de 3 clientes 3 productos credito o de contado: credito recarga del 20% contado descuento del 10%'''
tventas=0
vcont=0
vcre=0
acpague=0
pague=0
i=0
j=0
tcred=0
tcont=0
for i in range(3):
    j=0
    for j in range(3):
        Prod = (input("entre el producto:  "))
        cantidad = int(input("entre cantidad del producto  "))
        precio= int(input("entre precio del producto  "))
        pague=cantidad*precio
        acpague=acpague+pague

    fp= int (input("entre la forma de pago 1.credito 2.contado  "))
    
    if fp==1:
        vcre=acpague+acpague*20/100
        print(acpague)
        print(vcre)
    else:
        vcont=acpague-acpague*10/100
        
        print(vcont)
    

    
    