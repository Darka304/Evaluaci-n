frutas = []
i = 0

print("Digite acontinuación 10 frutas para el salpicón")

while(i < 10):
    fruta = {}

    fruta['nombre'] = input("\nDigite el nombre de la fruta: ")
    fruta['color'] = input ("Digite el color de la fruta: ")
    fruta['precio'] = input("Digite el precio de la fruta: ")
    frutas.append(fruta)
    i += 1
frutas.reverse()
print(frutas)