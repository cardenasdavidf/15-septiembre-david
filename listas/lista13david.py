#13.Reemplazar todos los valores negativos por cero
lista = [5, -3, 7, -1, 0, -6]
lista = [0 if x < 0 else x for x in lista]
print("Ejercicio 3:")
print("Lista sin negativos:", lista)
print()