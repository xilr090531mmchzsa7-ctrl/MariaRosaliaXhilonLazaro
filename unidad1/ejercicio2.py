try:
  alumnos=["Vanessa", "Manu", "Monse", "Julio", "Pao", "Adri", "Máxi", "Juan Carlos"]
  calificaciones = [9.5, 8.8, 9.0, 8.5, 9.2, 8.7, 9.4, 10.0]

  print(alumnos[0], calificaciones[0])
  print(alumnos[1], calificaciones[1])
  print(alumnos[2], calificaciones[2])
  print(alumnos[3], calificaciones[3])
  print(alumnos[4], calificaciones[4])
  print(alumnos[5], calificaciones[5])
  print(alumnos[6], calificaciones[6])
  print(alumnos[7], calificaciones[7])

except IndexError:
    print("Indice incorrecto")
except TypeError:
    print("error tipo de dato")