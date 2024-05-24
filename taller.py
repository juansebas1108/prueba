#ferreteria - 3 clientes (3 productos), credito o contado, Credito: recargo del 20%, Contado: descuento de 10%

vcont = 0
tventa = 0
vcred = 0
acpague=0
pague=0
i =1,3,1
j =1,3,1

for i  in range (3):
    j = 0 
    for j in range (3):
        producto= input ("Entre el nombre del producto ")
        cantidad= int(input("Entre la cantidad del producto "))
        precio= int(input("Entre el precio del producto "))
        pague=cantidad*precio
        acpague=acpague+pague
        
        
    fp= int (input("Ingrese la forma de pago ,1 credito , 2 contado "))
    if fp==1: 
            vcred=acpague+acpague*20/100
            print(acpague)
            print(vcred)
    else:
        vcont=acpague-acpague*10/100
        print(vcont)
        
           
        