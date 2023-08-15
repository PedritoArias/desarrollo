import random

def generar_lista_de_atletas():
    """
    Esta función genera aleatoriamente los datos de 20 atletas que participaron en una maratón.
    Devuelve una lista de atletas donde cada atleta es un diccionario con los campos:
        - nombre: el nombre del atleta
        - numero: el número con el que participó en la maratón
        - tiempo_llegada: la cantidad de segundos que tardó en llegar
    """
    lista_atletas = []
    nombres = ('Daniel', 'Alejandro', 'Pablo', 'Hugo', 'Álvaro', 'Adrián', 'David', 'Sergio', 'Diego')
    apellidos = ('García', 'Rodríguez', 'González', 'Fernández', 'López', 'Martínez', 'Sanchez', 'Pérez')
    for i in range(1, 21):
        atleta = {
            "nombre": random.choice(nombres) + " " + random.choice(apellidos),
            "numero": i,
            "tiempo_llegada": random.random() * 120
        }
        lista_atletas.append(atleta)
    return lista_atletas

def imprimir_resultados(lista_atletas):
    for atleta in lista_atletas:
        print(f"{atleta['numero']} - {atleta['nombre']}: ({atleta['tiempo_llegada']:.2f} segundos)")

def obtener_ganador(lista_atletas):
    ganador = min(lista_atletas, key=lambda x: x['tiempo_llegada'])
    return ganador['numero']

def obtener_datos_atleta(numero_atleta, lista_atletas):
    for atleta in lista_atletas:
        if atleta['numero'] == numero_atleta:
            return atleta

def obtener_podio(lista_atletas):
    podio = sorted(lista_atletas, key=lambda x: x['tiempo_llegada'])[:3]
    return tuple(atleta['numero'] for atleta in podio)

# Generar y almacenar una lista de atletas
lista_atletas = generar_lista_de_atletas()

# Imprimir los resultados
print("Resultados de la maratón:")
imprimir_resultados(lista_atletas)

# Obtener y mostrar el ganador
ganador = obtener_ganador(lista_atletas)
print(f"\nEl ganador de la maratón es el atleta número {ganador}.")

# Obtener y mostrar los datos de un atleta por su número
numero_atleta = int(input("\nIngrese el número de atleta para obtener sus datos: "))
datos_atleta = obtener_datos_atleta(numero_atleta, lista_atletas)
if datos_atleta:
    print(f"\nDatos del atleta número {numero_atleta}:")
    print(f"Nombre: {datos_atleta['nombre']}")
    print(f"Número: {datos_atleta['numero']}")
    print(f"Tiempo de llegada: {datos_atleta['tiempo_llegada']:.2f} segundos")
else:
    print(f"No se encontró ningún atleta con el número {numero_atleta}.")

# Obtener y mostrar el podio de ganadores
podio = obtener_podio(lista_atletas)
print("\nPodio de ganadores:")
for i, atleta_numero in enumerate(podio, start=1):
    datos_atleta = obtener_datos_atleta(atleta_numero, lista_atletas)
    print(f"{i}° Puesto: Atleta número {atleta_numero} - {datos_atleta['nombre']}")
