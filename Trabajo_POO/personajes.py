"""Importamos os y creamos una funcion lamda para que en cada ejecucion la consola se ejecute limpia"""
import os
clear = lambda: os.system("cls")
clear()

"""Se crea la clase personajes, padre..""" 
class Personaje:
   
    nombre = ""
    fuerza = 0
    inteligencia = 0
    defensa = 0
    vida = 0
    
    
    """dentro de la clase principal creamos la funcion init con los atributos que recibe la clase"""
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida
        
    """funcion con la cual podemos mostrar en consola los atributos que se le asignan a la clase"""    
    def atributos(self):
        print(self.nombre, ":", sep="")
        print("# Fuerza:", self.fuerza)
        print("# Inteligencia:", self.inteligencia)
        print("# Defensa:", self.defensa)
        print("# Vida", self.vida)
    """con esta funcion se puede modificar algunos atributos"""    
    def  subir_nivel( self, fuerza, inteligencia, defensa):
        self.fuerza = self.fuerza + fuerza
        self.inteligencia = self.inteligencia + inteligencia
        self.defensa = self.defensa + defensa
    """funcion que determina el valor del atributo vida"""   
    def  esta_vivo(self):
        return self.vida > 0
    """si el valor del atributo vida es menos o igual a 0 imprimimos el msj informandolo"""
    def  morir(self):
        self.vida = 0
        print(self.nombre, "ha muerto")
    """con esta funcion determinamos el daño en puntos teniendo en cuenta atributos de ambos personajes"""    
    def daño(self, enemigo):
        return self.fuerza - enemigo.defensa
    """con esta funcion iniciamos un ataque utilizando la funcion daño atravez de self"""
    def  atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.vida = enemigo.vida - daño
        print(self.nombre, " \nha realizado", daño, "puntos de daño a", enemigo.nombre)
        if enemigo.esta_vivo():
            print("La vida de", enemigo.nombre, "es", enemigo.vida, "puntos")
        else:
            enemigo.morir()
"""creamos la clase guerrro que hereda de la clase personaje y se le agrega un atributo en el init"""               
class Guerrero(Personaje):
    
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada
    """"agregamos a los atributos de la clase padre, el atributo perteneciente a la clase hija"""    
    def  atributos(self):
        super().atributos()
        print("# Espada:", self.espada)
    """funcion del daño que realiza teniendo en cuenta los atributos heredados mas los propios"""    
    def  daño(self, enemigo):
        return self.fuerza * self.espada - enemigo.defensa
    
"""creamos la clase arquero que hereda de la clase personaje y se le agrega un atributo en el init"""    
class Arquero(Personaje):
    
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, arco):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.arco = arco
    """"agregamos a los atributos de la clase padre, el atributo perteneciente a la clase hija"""    
    def  atributos(self):
        super().atributos()
        print("# arco:", self.arco)
    """funcion del daño que realiza teniendo en cuenta los atributos heredados mas propios"""    
    def  daño(self, enemigo):
        return self.inteligencia * self.arco - enemigo.defensa

"""funcion que se va unitilizar para salir del juego"""
def salir_juego():    
    print("Adios")    
"""funcion en donde se encuentran las distintas opciones para reaaliar y dar funcionalidad al juego"""    
def comenzar():
    """se crean los personajes y se pasan los parametros para que el usuario no deba ingresarlos y los
    mostramos ya defenidos"""
    mago = Personaje("Mago", 20, 15, 10, 100)
    guerrero = Guerrero("Guerrero", 20, 15, 10, 100, 5)
    arquero = Arquero("Arquero", 20, 15, 10, 100, 5)
    

    """creamos un bucle para mostrar las opciones a las q se va tener acceso"""
    while True:
        """establecemos el menu principal"""
        print("\nOPCIONES DEL JUEGO")
        print("Para ver los personajes presione 1.")
        print("Para elejir un personaje presione 2.")
        print("Para salir presione 3.")
        #print("\nPARA INICIAR EL JUEGO SELECCIONE UN PERSONAJE\n1.MAGO\n2.GUERRERO\n3.ARQUERO")
        opcion = input("\nIngrese una opcion: ")
        
        if (opcion == "1"):
            mago.atributos()
            guerrero.atributos()
            arquero.atributos()
            
        elif (opcion == "2"):   
            print("\nELIJE UN PERSONAJE \n1.MAGO\n2.GUERRERO\n3.ARQUERO")
            seleccion = input("Personaje n: ")
            
            if (seleccion == "1"):
                print("\nHas elejido al mago")
                atacarA = input("Quieres atacar a: \n1.Guerrero \n2.Arquero\n_")
                
                if (atacarA == "1"):
                    mago.atacar(guerrero)
                elif (atacarA == "2"):
                    mago.atacar(arquero)
                else:
                    print("Has ingresado una opcion no valida")
                    
            elif (seleccion == "2"):
                print("\nHas elejido al guerrero")
                atacarA = input("Quieres atacar a: \n1.Mago \n2.Arquero\n_")
                
                if (atacarA == "1"):
                    guerrero.atacar(mago)
                elif (atacarA == "2"):
                    guerrero.atacar(arquero)
                else:
                    print("Has ingresado una opcion no valida")
                    
            elif(seleccion == "3"):
                print("\nHas elejido al Arquero")
                atacarA = input("Quieres atacar a: \n1.Mago \n2.Guerrero\n_")
            
                if (atacarA == "1"):
                    arquero.atacar(mago)
                elif (atacarA == "2"):
                    arquero.atacar(guerrero)
                else:
                    print("Has ingresado una opcion no valida")
            
        elif (opcion == "3"):
            """llamamos a la funcion q termina la ejecucion del codigo"""
            salir_juego()
            break
        
        else:
            print("La opcion ingresa es incorrecta, por favor ingresa nuevamente\n")
               
"""llamamos a la funcion que contiene el menu de inicio, la ejecucion del codigo"""    
comenzar()        
        