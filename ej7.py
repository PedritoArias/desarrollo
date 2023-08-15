#Franco está organizando un asado con sus amigos y necesita de 
#tu ayuda. Para estimar poder carne necesita comprar, va a 
#suponer que cada invitado viene 0.7 Kg de carne. Ayuda a 
#Franco escribiendo un programa que permita al usuario ingresar
#la cantidad de invitados y el precio de 1Kg. de carne , y 
#muestre cuantos Kg de carne en total debe pedir al carnicero y 
#cuanto dinero necesita para pagar.
def calcular_carne_y_costo(invitados, precio_por_kilo):
    cantidad_carne = invitados * 0.7  # Cada invitado trae 0.7 Kg de carne
    costo_total = cantidad_carne * precio_por_kilo
    return cantidad_carne, costo_total

# Pedir al usuario que ingrese la cantidad de invitados y el precio por kilo de carne
invitados = int(input("Ingrese la cantidad de invitados: "))
precio_por_kilo = float(input("Ingrese el precio por kilo de carne: "))

# Calcular la cantidad de carne y el costo total
cantidad_carne, costo_total = calcular_carne_y_costo(invitados, precio_por_kilo)

# Mostrar los resultados
print(f"Debes comprar {cantidad_carne:.2f} Kg de carne en total.")
print(f"Necesitas {costo_total:.2f} pesos para pagar.")