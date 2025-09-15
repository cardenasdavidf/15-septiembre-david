# Ejercicio 1: Crear una tupla de 5 elementos y mostrarla
tupla1 = (1, 2, 3, 4, 5)
print("Ejercicio 1:", tupla1)
print()

# Ejercicio 2: Acceder al tercer elemento de una tupla
tupla2 = (10, 20, 30, 40, 50)
print("Ejercicio 2:", tupla2[2])
print()

# Ejercicio 3: Contar cuántas veces aparece un elemento en una tupla
tupla3 = (1, 2, 2, 3, 2, 4)
print("Ejercicio 3:", tupla3.count(2))
print()

# Ejercicio 4: Encontrar el índice de un elemento en una tupla
tupla4 = (5, 8, 12, 8, 7)
print("Ejercicio 4:", tupla4.index(8))
print()

# Ejercicio 5: Convertir una lista en tupla
lista = [1, 2, 3]
tupla5 = tuple(lista)
print("Ejercicio 5:", tupla5)
print()

# Ejercicio 6: Sumar todos los elementos de una tupla
tupla6 = (4, 7, 1, 6)
print("Ejercicio 6:", sum(tupla6))
print()

# Ejercicio 7: Concatenar dos tuplas
tupla7a = (1, 2, 3)
tupla7b = (4, 5, 6)
tupla7c = tupla7a + tupla7b
print("Ejercicio 7:", tupla7c)
print()

# Ejercicio 8: Multiplicar los elementos de una tupla
tupla8 = (2, 3, 4)
producto = 1
for n in tupla8:
	producto *= n
print("Ejercicio 8:", producto)
print()

# Ejercicio 9: Verificar si un elemento está en una tupla
tupla9 = (10, 20, 30)
print("Ejercicio 9:", 20 in tupla9)
print()

# Ejercicio 10: Obtener la longitud de una tupla
tupla10 = (1, 2, 3, 4)
print("Ejercicio 10:", len(tupla10))
print()

# Ejercicio 11: Tupla con diferentes tipos de datos
tupla11 = (1, "dos", 3.0, True)
print("Ejercicio 11:", tupla11)
print()

# Ejercicio 12: Convertir una cadena en tupla de caracteres
cadena = "Python"
tupla12 = tuple(cadena)
print("Ejercicio 12:", tupla12)
print()

# Ejercicio 13: Obtener el máximo y mínimo de una tupla
tupla13 = (5, 9, 2, 8)
print("Ejercicio 13: Máximo:", max(tupla13), "Mínimo:", min(tupla13))
print()

# Ejercicio 14: Repetir una tupla n veces
tupla14 = (1, 2)
tupla14r = tupla14 * 3
print("Ejercicio 14:", tupla14r)
print()

# Ejercicio 15: Desempaquetar una tupla en variables
tupla15 = (10, 20, 30)
a, b, c = tupla15
print("Ejercicio 15:", a, b, c)
print()

# Ejercicio 16: Crear una tupla de tuplas
tupla16 = ((1, 2), (3, 4), (5, 6))
print("Ejercicio 16:", tupla16)
print()

# Ejercicio 17: Buscar un elemento en una tupla de tuplas
tupla17 = ((1, "a"), (2, "b"), (3, "c"))
buscado = 2
encontrado = [t for t in tupla17 if t[0] == buscado]
print("Ejercicio 17:", encontrado)
print()

# Ejercicio 18: Ordenar una tupla (convertir a lista y ordenar)
tupla18 = (5, 2, 8, 1)
ordenada = tuple(sorted(tupla18))
print("Ejercicio 18:", ordenada)
print()

# Ejercicio 19: Filtrar elementos mayores a 5 en una tupla
tupla19 = (2, 6, 8, 3, 7)
mayores = tuple(x for x in tupla19 if x > 5)
print("Ejercicio 19:", mayores)
print()

# Ejercicio 20: Crear una tupla con los números pares del 1 al 20
tupla20 = tuple(x for x in range(1, 21) if x % 2 == 0)
print("Ejercicio 20:", tupla20)
print()
