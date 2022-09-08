multiplos2 = 0
multiplos3 = 0
i = 0
cantidad = int(input("¿Cuantos dígtos desea ingresar?: "))

while(i < cantidad):
    numeros= int(input("Ingrese un dígito: "))
    if(numeros %3 == 0 and numeros %2 == 0):
        multiplos2 += 1
        multiplos3 += 1
        i +=1
    elif(numeros %3 == 0):
        multiplos2 += 1
        i +=1
    elif(numeros %2 == 0):
        multiplos3 += 1
        i +=1
    else:
        i +=1

print(F"Múltiplos de 2: {multiplos2}")
print(F"Múltiplos de 3: {multiplos3}")