from audioop import reverse
from importlib.resources import read_text
import os
from xml.sax.handler import feature_external_ges
clear = lambda: os.system("cls")
clear()

'''Las funciones tienen nombre, argumentos,codigo y retorno'''

def suma(a, b):
    
    resultado = a + b
    
    return resultado
print(suma(2,3))

'''Funcion 2'''
print('\n----------------------------------')

def resta():
    print(3-2)    
resta()

'''Funcion 3'''
print('\n----------------------------------')

def saludo(cantidad_saludos):
    
    lista_nombres = []
    
    for i in range(cantidad_saludos):
        nombre = input('Ingrese su nombre: ')
        print('Hola', nombre)
        
        lista_nombres.append(nombre)
    print(lista_nombres)    
    return lista_nombres

nombres = saludo(int(input('Ingrese la cantidad de saludos a ejecutar: ')))

'''Funcion 4'''
print('\n----------------------------------')

def  prueba(a,b,c):
    print(a, b, c)
    
a = 420
b = 3
c = 5

prueba(b=b, c=c, a=a)

'''Funcion 4'''
print('\n----------------------------------')

def orden(lista, sentido):
    lista.sort(reverse=sentido)
    return lista

nombres = saludo(int(input('Ingrese la cantidad de saludos a ejecutar: ')))

print(
    orden(nombres, True)
)



    
    
    
    
    
    
    

























