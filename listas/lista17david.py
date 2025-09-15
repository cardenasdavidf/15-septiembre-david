#17.Sumar los elementos en posiciones pares de una lista
lista = [10, 20, 30, 40, 50, 60]
suma_pares = sum(lista[i] for i in range(0, len(lista), 2))
print("Ejercicio 7:")
print("Suma de posiciones pares:", suma_pares)
print()