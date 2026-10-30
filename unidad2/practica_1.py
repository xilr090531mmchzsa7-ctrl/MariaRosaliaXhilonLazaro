alumno = []
promedio = []

cantidad = int(input("¿Cuántos alumnos vas a registrar?: "))

for i in range(cantidad):
    nombre = input("Coloca el nombre del estudiante: ")
    calificacion = float(input("¿Cuál es su promedio?: "))
    alumno.append(nombre)
    promedio.append(calificacion)

promedio_bajo = promedio[0]
promedio_alto = promedio[0]

for contador in promedio:
    if contador < promedio_bajo:
        promedio_bajo = contador
    elif contador > promedio_alto:
        promedio_alto = contador

print("El promedio más alto es:", promedio_alto)
print("El promedio más bajo es:", promedio_bajo)