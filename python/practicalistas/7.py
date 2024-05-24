ls=["a","b","c","d","e","f"]
#Rebanar elementos 1 y 2
lsrl = ls[1:3]
print(ls)
print("Elementos 1 y 2",lsrl)

#Rebanar elementos 3 y 4
lsr2 = ls[3:5]
print(ls)
print("Elementos 3 y 4",lsr2)

#Rebanar el elemento 1
lsr3 = ls[0:1]
print(ls)
print("Elemento 1 ",lsr3)

#Rebanar hasta el elemento 4
lsr4 = ls[:4]
print(ls)
print("Elementos 4 ",lsr4)

#Rebanar desde el elemento 2 
lsr5 = ls[2:]
print(ls)
print("Elemento 2 en adelante ",lsr5)

ls.append("z")
print(ls)
ls.append("p")
print(ls)