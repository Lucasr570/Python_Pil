import os
from xml.etree.ElementInclude import default_loader
clear = lambda: os.system("cls")
clear()

class Animal:
    
    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad
        
    def  hablar(self, sonido):
        print(sonido)
    
    
class Perro(Animal):
   
    
    def __init__(self, nombre,raza, especie, edad):
        #Atributos de la instancia == local
        self.nombre = nombre
        self.raza = raza
        
        super().__init__(especie, edad)
        
    #Metodos  
    def saludar(self):
        print(f'{self.nombre} dio la pata')
        
class Gato(Animal):
   
    
    def __init__(self, nombre,raza, especie, edad):
        #Atributos de la instancia == local
        self.nombre = nombre
        self.raza = raza
        
        super().__init__(especie, edad)
        
    #Metodos  
    def saludar(self):
        print(f'{self.nombre} ronronea')
        
        
perro_1 = Perro('Firulais', 'Salchicha', 'Perro', 5)
print(f'perro_1-> {perro_1.nombre}, {perro_1.raza}, {perro_1.especie}, {perro_1.edad}')
perro_1.saludar()

gato_1 = Gato('Tito', 'Calico', 'Felino', 3)
print(f'gato_1-> {gato_1.nombre}, {gato_1.raza}, {gato_1.especie}, {gato_1.edad}')
gato_1.saludar()

# perro_1 = Perro('Rex', 'Collie')
# print(f'Perr_1-> {perro_1.raza}, {perro_1.nombre}, {perro_1.especie}')
# perro_1.ladrar
# perro_1.jugar('pelota')
# perro_1.saludar

# perro_2 = Perro('Ana', 'Collie')
# print(f'Perro_2-> {perro_2.nombre}, {perro_2.raza}')


