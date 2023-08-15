'''Generar una lista con 10 valores enteros aleatorios entre 1 
y 20 (se puede usar randint() del módulo random). Luego:

Muestre la lista
El usuario ingresa debe ingresar un valor un valor. El programa
debe informar cuántos valores de la lista son mayores a dicho 
valor, para eso debe utilizar una función. La función debe 
recibir como argumentos la lista y un entero, y debe retornar 
la cantidad de valores de la lista mayores a dicho entero.
Crear una función que calcule el promedio de la lista y utilizarla.
Crear una función que encuentre el valor más grande y el más 
pequeño de la lista y los retorne.'''
import random

def contar_mayores(lista, valor):
    count = 0
    for num in lista:
        if num > valor:
            count += 1
    return count

def calcular_promedio(lista):
    return sum(lista) / len(lista)

def encontrar_extremos(lista):
    min_val = min(lista)
    max_val = max(lista)
    return min_val, max_val

# Generar lista de 10 valores enteros aleatorios entre 1 y 20
lista = [random.randint(1, 20) for _ in range(10)]

# Mostrar la lista
print("Lista generada:", lista)

# Pedir al usuario que ingrese un valor
valor_ingresado = int(input("Ingrese un valor: "))

# Contar valores mayores al valor ingresado
mayores = contar_mayores(lista, valor_ingresado)
print(f"Hay {mayores} valores mayores a {valor_ingresado} en la lista.")

# Calcular el promedio de la lista
promedio = calcular_promedio(lista)
print("El promedio de la lista es:", promedio)

# Encontrar el valor más grande y más pequeño
minimo, maximo = encontrar_extremos(lista)
print("El valor más pequeño en la lista es:", minimo)
print("El valor más grande en la lista es:", maximo)