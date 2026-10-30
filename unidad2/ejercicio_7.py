mapa=[
    [".","B",".","."],
    [".",".",".","."],
    [".",".",".","A"],
    [".",".",".","."]
]
filas=len(mapa)
columnas=len(mapa[0])
#Recorriendo la matriz con ciclos anidados
#Ciclo externo para manejar filas(i)
for i in range(filas):#i<4
    #Ciclo interno para manejar columnas(j)
    for j in range(columnas):
        #Verificamos si encontramos el tesoro
        if mapa[i][j]=="A":
            print(f"Tesoro encontrado en la posicion [{i}][{j}]")
        if mapa[i][j]=="B":
            print(f"Tesoro encontrado en la posicion [{i}][{j}]")