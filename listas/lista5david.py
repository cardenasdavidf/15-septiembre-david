#5.Palabras con más de 5 letras
palabras = input("Ejercicio 5: Ingrese palabras separadas por espacio: ").split()
largas = [p for p in palabras if len(p) > 5]
print("Palabras con más de 5 letras:", largas)
print()