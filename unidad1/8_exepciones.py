try:
   #Ejemplo 1 sin manejo de exepciones
   numero1=int(input("Ingresa el primer numero: "))
   numero2=int(input("Ingresa el segundo numero: "))
   resultado=numero1/numero2
   print(resultado)
except ZeroDivisionError:
    print("DIVICION ENTRE CERO FALLIDA")
except ValueError: 
    print("SOLO INTRODUCE NUMEROS")