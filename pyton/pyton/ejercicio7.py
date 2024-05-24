
selec=0
while selec == 1 or selec <= 4:
    print("1.ingresos")
    print("2.gastos")
    print("3.otros ingresos")
    print("4.otros gastos")
    print("5.fin")
    selec=int(input("seleccione un metodo:  "))
    if selec == 1:
        print("Estas con ingresos")
        print("")
    elif selec==2:
        print("Estas con gastos")
        print("")
    elif selec==3:
        print("Estas con otros ingresos")
        print("")
    elif selec==4:
        print("Estas con otros gastos")
        print("")
    elif selec==5:
        print("fin")
        print("")
    else:
        print("no funciona el programa")
        exit
        

    
