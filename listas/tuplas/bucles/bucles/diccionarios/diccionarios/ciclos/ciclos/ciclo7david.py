# Ejercicio 7: Imprimir los números del 1 al 10, pero saltar el 5
for i in range(1, 11):
    if i == 5:
        continue
    print(i)