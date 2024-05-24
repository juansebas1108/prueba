reten=0
sneto=0

sreten=0

for x in range(1):
        nombre=(input("ingrese el nombre: "))
        reten= int(input("ingrese el valor de su salario: "))
        
        if reten < 1500:
            sneto=reten
            
        else:
            sneto=reten*5/100
            sreten=5/100
            
        if reten > 3000:
            sneto=reten*8/100
            sreten=8/100
        sbruto=sneto-reten

  
print("el nombre del usuario es: ",nombre)
print("el salario bruto es: ",reten)
print("el salario neto es: ",sbruto)
print("el Reten de su salario es: ",sreten)