carrito=[]#Lista vacia
n_productos=int(input("Ingresa el numero de productos: "))
for i in range(n_productos):
    producto=input("Ingresa el producto a tu carrito: ")
    carrito.append(producto)
print("Listas creada correctamente")
print(f"Tu carrito contiene{carrito}")
carrito[0]="barbitas"
print(f"Tu carrito contiene{carrito}")
