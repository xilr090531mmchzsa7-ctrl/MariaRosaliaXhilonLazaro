dias_permitidos = ("lunes", "miercoles", "viernes")

print("Días de atención para préstamos:")
for indice, dia in enumerate(dias_permitidos):
    print(f"[{indice}] {dia}")

dia_solicitado = input("\nIngresa el día en que deseas solicitar el préstamo: ").strip().lower()

if dia_solicitado in dias_permitidos:
    print(f"Solicitud permitida: se atiende los {dia_solicitado}.")
else:
    print("No hay atención ese día.")