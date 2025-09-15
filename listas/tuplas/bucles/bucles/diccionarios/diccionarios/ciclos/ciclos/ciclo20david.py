# Ejercicio 20: Imprimir los números del 1 al 10 y mostrar si son pares o impares
for i in range(1, 11):
    if i % 2 == 0:
        print(i, 'par')
    else:
        print(i, 'impar')