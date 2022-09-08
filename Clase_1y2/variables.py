import os
from typing import Type
clear = lambda: os.system("cls")
clear()

#Str
a = 'Esto es una "cadena"'
b = 'Esto es otra "cadena"'

print(a, type(a))
print(b, type(b))

c = str(120.56)
print(c, type(c))

print(a[0:4])
print(b[-1] )

#METODOS
print(a.lower())
print(a.upper())
print(len(a.split()))

#LIST
lista_1 = ['hola', 4, 2.5, [1,2,3,4], ('a', 'b')]
print(lista_1)
print(type(lista_1))
print(len(lista_1))
print(lista_1[2])

var_uno = lista_1[3]
print(var_uno)
print(type(var_uno))

#Metodos 
lista_1.append('lista')
print(lista_1.index(('a', 'b')))

lista_1.insert(1, 5)
print(lista_1)

#DICCIONARIO
usuario = {
    'nombre': 'Octavio',
    'apellido': 'Gomez',
    'edad': '38',
    'hobbies': ['futbol', 'musica'],
    'mascotas': False
}
print(usuario)
print(usuario['edad'])
print(len(usuario))

#METODOS
print(usuario.get('hobbies', ))
print(usuario.get('Puesto', 'No encontrado'))

Keys_usuario = list(usuario.keys())
print(type(Keys_usuario))
print(usuario.get(Keys_usuario[0]))

print(usuario.values())