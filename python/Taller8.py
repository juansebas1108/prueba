selec=0
ing=0
ing=int(input("Ingrese su cantidad de ingresos:  "))
resultado=0
ingr=0
while selec == 1 or selec <= 4:
    print("1.ingresos")
    print("2.gastos")
    print("3.otros ingresos")
    print("4.otros gastos")
    print("5.fin")
    selec=int(input("seleccione un que metodo desa ingresar:  "))
    while selec == 1  or selec <= 4 :
        ingr=int(input("ingrese la cantidad de ingresos de este mes:  "))
        resultado=ing+ingr
        print("")
    
    
    while selec == 1  or selec <= 4 :
        gastos=int(input("ingrese la cantidad de gastos de este mes:  "))
        resultado=ing+ingr-gastos
        print("")
   
    while selec == 1  or selec <= 4 :
        oingr=int(input("ingrese la cantidad de otros ingresos de este mes:  "))
        resultado=ing+ingr-gastos+oingr
        print("")
    while selec == 1  or selec <= 4 :
        ogastos=int(input("ingrese la cantidad de otros gastos de este mes:  "))
        resultado=ing+ingr-gastos+oingr-ogastos
        print("")
       
    else:
        resultado=resultado
        print("Total: ", resultado)
        exit