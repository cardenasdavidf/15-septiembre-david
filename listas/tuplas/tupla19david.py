# Ejercicio 19: Multiplicar los elementos de una tupla por 2.
tupla = (1, 2, 3)
tupla2 = tuple(x*2 for x in tupla)
print('Multiplicados:', tupla2)