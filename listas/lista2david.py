#2.Nombres ordenados
nombres = []
for i in range(5):
	nombre = input(f"Ingrese el nombre {i+1}: ")
	nombres.append(nombre)
print("Ejercicio 2:")
print("Nombres ordenados:", sorted(nombres))
print()