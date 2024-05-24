hombres_casados_mayores = 0
mujeres_casadas_mayores = 0
hombres_solteros_mayores = 0
mujeres_solteras_mayores = 0

for _ in range(6):  # Recorremos 4 personas
    nombre = input("Ingrese el nombre: ")
    sexo = int(input("Ingrese el sexo del usuario (1 para Hombre, 2 para Mujer): "))
    edad = int(input("Ingrese la edad del individuo: "))
    estado_civil = int(input("Ingrese el estado civil del usuario (1 para Casado, 2 para Soltero): "))

    print("El nombre es:", nombre)
    if edad < 18:
        print("Menor de edad.el Programa no usara tus datos.")
        

    print("Mayor de edad")

    if estado_civil == 1:
        print("Casado")
    else:
        print("Soltero")

    if sexo == 1:
        print("Hombre")
    else:
        print("Mujer")

    if edad >= 18:
        if estado_civil == 1:
            if sexo == 1:
                hombres_casados_mayores += 1
            else:
                mujeres_casadas_mayores += 1
        else:
            if sexo == 1:
                hombres_solteros_mayores += 1
            else:
                mujeres_solteras_mayores += 1

print("La cantidad de Hombres casados mayores de edad son: ", hombres_casados_mayores)
print("La cantidad de Hombres solteros mayores de edad son: ", hombres_solteros_mayores)
print("La cantidad de Mujeres casados mayores de edad son: ", mujeres_casadas_mayores)
print("La cantidad de Mujeres solteros mayores de edad son: ", mujeres_solteras_mayores)