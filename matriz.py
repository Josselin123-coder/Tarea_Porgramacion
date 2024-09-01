lista = [
    [6,5,4,8,9,11,14],
    [3,7,7,8,5,1,10]
    ]   # Declaramos la lista bidimiensional

def buscando(n,l):    #Creamos una función llamada buscar
    for i in range(len(lista)):  #Recorremos filas
        for j in range(len(lista)): #Recorremos las columnas
          if lista[i] [j] == n :  #Si la posición en la lista es igual al numero que deseamos encontrar
             return i,j #Retornamos los indices de las filas y columnas


    return "No hay el numero en la lista"

print("LISTA")
for i in lista :
    print(i)


print(f"El numero esta en la posición {buscando(5,lista)} ")   #Imprimimos


