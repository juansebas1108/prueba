acc1=0
acc2=0
acc3=0
acc4=0
acc5=0
acc6=0

for i in range(5):
    cedula=input("Entre su cedula: " )
    svoto=input("Por quien votaste? 1,2,3,4,5,6 ")
    if svoto=="1":
        acc1=acc1+1
        print(i)
    if svoto=="2":
        acc2=acc2+1
        print(i)
    if svoto=="3":
        acc3=acc3+1
        print(i)
    if svoto=="4":
        acc4=acc4+1
        print(i)
    if svoto=="5":
        acc5=acc5+1
        print(i)
    if svoto=="6":
        acc6=acc6+1
        print(i)
if acc1 > acc2 and acc1 > acc3 and acc1 > acc4 and acc1 > acc5 and acc1 > acc6:
    mayor=acc1
    print("El Ganador Fue el Candidato", 1)
if acc2 > acc1 and acc2 > acc3 and acc2 > acc4 and acc2 > acc5 and acc2 > acc6:
    mayor=acc2
    print("El Ganador Fue el Candidato", 2)
if acc3 > acc1 and acc3 > acc2 and acc3 > acc4 and acc3 > acc5 and acc3 > acc6:
    mayor=acc3
    print("El Ganador Fue el Candidato", 3)
if acc4 > acc1 and acc4 > acc2 and acc4 > acc3 and acc4 > acc5 and acc4 > acc6:
    mayor=acc4
    print("El Ganador Fue el Candidato", 4)
if acc5 > acc1 and acc5 > acc2 and acc5 > acc3 and acc5 > acc4 and acc5 > acc6:
    mayor=acc5
    print("El Ganador Fue el Candidato", 5)
if acc6 > acc1 and acc6 > acc2 and acc6 > acc3 and acc6 > acc4 and acc6 > acc5:
    mayor=acc6
    print("El Ganador Fue el Candidato", 6)
    print(i)
print("La Cantidad de Votos Fue: ", i+1)