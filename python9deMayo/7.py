menor7=0
mayor7=0
for i in range(10):
    nota=int(input("Ingrese su nota de 1 a 10: "))
    if nota < 7:
        menor7=menor7+1
    elif nota >=7:
        mayor7=mayor7+1

print("Los estudiantes con notas menor o igual a 7 es: ",menor7)
print("Los estudiantes con notas superior a 7 es: ",mayor7)

