"""Durante los 5 días de una semana se tomó medida de temperatura en la ciudad.
Se desea conocer cual fue la temperatura promedio de la semana. Escriba 
un programa que permita calcularla a partir de 5 valores de temperatura que ingresará el usuario."""
t1= float(input("Tempreatura: "))
t2= float(input("Tempreatura: "))
t3= float(input("Tempreatura: "))
t4= float(input("Tempreatura: "))
t5= float(input("Tempreatura: "))

promedio =(t1 + t2+ t3+ t4 +t5)/5
print(f"el promedio es {promedio}")