print("Tablas de multiplicar 17 al 30")

a=0
for j in range(17, 31):
    for i in range(0,11):
        re =j*i
        print(f'{j} x {i} = {re}')
        if i ==7:
            a+= re
print(f'la suma de los multiplos de 7 es:  {a}')