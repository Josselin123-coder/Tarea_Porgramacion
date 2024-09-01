#ORDENAR

def ordenar(arr):
    n = len(arr)
    # Recorremos  todos los elementos de la lista
    for i in range(n):
        # Últimos i elementos ya están en su lugar
        for j in range(0, n - i - 1):
            # Compararamos el elemento actual con el siguiente
            if arr[j] > arr[j + 1]:
                # Intercambiamos  si están en el orden incorrecto
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Creamos la lista
lista = [
    [6, 5, 4, 8, 9, 11, 14],
    [3, 7, 7, 8, 5, 1, 10]
]
print("LISTA INICIAL")
for l in lista :
    print(l)
# Llamamos a nuestra funcion y  ordenamos  la segunda sublista
ordenar(lista[1])
print("\n")

print("LISTA ORDENADA")
for j in lista :
    print(j)  # Imprimimos la función ya ordenada

