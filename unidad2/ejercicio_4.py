promedio=[9,8,5,10,6]
#1. Encontrar el promedio mas bajo usando el ciclo for
#Suponemos inicialmente que el promedio mas bajo es el primer elemento
promedio_bajo=promedio[0]
for contador in promedio:
    if contador<promedio_bajo:
        promedio_bajo=contador
print(promedio_bajo)
#promedio alto
promedio=[9,8,5,10,6]
promedio_alto=promedio[0]
for contador in promedio:
    if contador>promedio_alto:
        promedio_alto=contador
print(promedio_alto)
