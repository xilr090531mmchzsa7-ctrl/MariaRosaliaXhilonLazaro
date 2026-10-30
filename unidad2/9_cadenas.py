#Cadenas y concatenacion con (+)
cadena1='Hola'
cadena2="Mundo"
multilinia="""Esto es una cadena
de variaslineas"""
print(cadena1 + cadena2 + multilinia)
#Cadenas y repeticion
eco="ja"*3
print(eco)
#Cambiar una cadena de miniscula a masyusculas
tu_nombre='Rosalia'
print(tu_nombre.upper())
#Cambiar de mayuscula a miniscula
print(tu_nombre.lower())
#Remplazar texto en una cadena
frase="Me gusta la de vinculacion"
print(frase.replace("progrmacion","filosofia"))
#Formato de concatenar cadenas con valores(F-String)
edad=17
nombre='Rosalia'
mensaje=f"Hola, me llamo {nombre} y tengo\n{edad}años"
print(mensaje)
texto= "¡Felicidades por un continuar en el CECY!!!"
cantidad_caracteres=len(texto)
print(cantidad_caracteres)
#Comprobar si un texto contiene una palabra
oracion="Aprender python es divertido"
if "java" in oracion:
    print("Encontrado")
else:
 print("No esta")
#Validar contenido de una cadena
ncadena="a1"
print(ncadena.isalpha())#True
print(ncadena.isdigit())#False