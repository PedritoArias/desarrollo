def determinar_categoria(edad):

    if 13 <= edad <= 15:
        return "infantiles"
    elif 15 < edad <= 17:
        return "cadetes"
    elif 17 < edad <= 19:
        return "juveniles"
    else:
        return "mayores"

# Pedir al usuario que ingrese el nombre y la edad del socio
nombre = input("Ingrese el nombre del socio: ")
edad = int(input("Ingrese la edad del socio: "))

# Determinar la categoría del socio
categoria = determinar_categoria(edad)

# Mostrar la categoría del socio
print(f"El socio {nombre} está en la categoría de {categoria}.")