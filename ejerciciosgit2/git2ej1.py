def mostrar_suma(valor1, valor2):
    return valor1 + valor2

def mostrar_resta(valor1, valor2):
    return valor1 - valor2

def mostrar_multiplicacion(valor1, valor2):
    return valor1 * valor2

def mostrar_division(valor1, valor2):
    if valor2 != 0:
        return valor1 / valor2
    else:
        return "Error: No se puede dividir por cero"

def main():
    valores = {
        1: None,
        2: None
    }
    
    while True:
        print("1. Ingresar valor 1", f"({valores.get(1)})" if valores[1] is not None else "")
        print("2. Ingresar valor 2", f"({valores.get(2)})" if valores[2] is not None else "")
        print("3. Mostrar suma")
        print("4. Mostrar resta")
        print("5. Mostrar multiplicacion")
        print("6. Mostrar division")
        print("7. Salir")
        
        opcion = int(input("\nElija una opcion: "))
        
        if opcion == 7:
            print("Saliendo del programa.")
            break
        elif opcion in (1, 2):
            valores[opcion] = float(input(f"Ingrese el valor {opcion}: "))
        elif opcion in (3, 4, 5, 6):
            if None in valores.values():
                print("Error: Ingrese valores primero")
            else:
                if opcion == 3:
                    resultado = mostrar_suma(valores[1], valores[2])
                elif opcion == 4:
                    resultado = mostrar_resta(valores[1], valores[2])
                elif opcion == 5:
                    resultado = mostrar_multiplicacion(valores[1], valores[2])
                elif opcion == 6:
                    resultado = mostrar_division(valores[1], valores[2])
                
                print("Resultado:", resultado)
        else:
            print("Opcion invalida. Por favor, elija una opcion valida.")

if __name__ == "__main__":
    main()