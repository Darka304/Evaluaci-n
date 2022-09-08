opcion = 100

print("19 Ingresar producto")
print("2) Mostra todos los productos")
print("3) Buscar producto y editar")
print("4) Buscar producto y eliminar")
print("0) Salir")


productos = []

while(opcion != 0):
    opcion = int(input("Digite la opcion elegida: "))
    producto = {}
    
    if(opcion == 1):
        producto['nombre'] = input("Digite nombre de produto: ")
        producto['codigo'] = input("Digite código del producto: ")
        producto['precio'] = input("Digite precio del producto: ")
        productos.append(producto)
    elif(opcion == 2):
        print(productos)
    elif(opcion == 3):
        codigoProducto = int(input("Digite el código de producto: "))
        print(producto.get(codigoProducto, "no está"))
    elif(opcion == 0):
        print("a")
        break
    else:
        print("Digite una opcion válida")