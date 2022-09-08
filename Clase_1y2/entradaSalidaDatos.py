import os
clear = lambda: os.system("cls")
clear()

#variables
mensaje_usuario = input("Ingrese el mensaje: ")
print(mensaje_usuario)
print("-----------------------------------")

x = int(input("Ingrese un numero: "))
y = int(input("Ingrese otro numero: "))

print("El tipo de dato de x es: ", type(x))
print("El tipo de dato de x es: ", type(y))

resultado = x + y
print("El resultado es: ",resultado)
