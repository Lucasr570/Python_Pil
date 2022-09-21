import os
clear = lambda: os.system("cls")
clear()
 


class Personaje:
   
    nombre = ""
    fuerza = 0
    inteligencia = 0
    defensa = 0
    vida = 0
    
    
    
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida
        
        
    def atributos(self):
        print(self.nombre, ":", sep="")
        print("# Fuerza:", self.fuerza)
        print("# Inteligencia:", self.inteligencia)
        print("# Defensa:", self.defensa)
        print("# Vida", self.vida)
        
    def  subir_nivel( self, fuerza, inteligencia, defensa):
        self.fuerza = self.fuerza + fuerza
        self.inteligencia = self.inteligencia + inteligencia
        self.defensa = self.defensa + defensa
        
    def  esta_vivo(self):
        return self.vida > 0
    
    def  morir(self):
        self.vida = 0
        print(self.nombre, "ha muerto")
        
    def daño(self, enemigo):
        return self.fuerza - enemigo.defensa
    
    def  atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.vida = enemigo.vida - daño
        print(self.nombre, " \nha realizado", daño, "puntos de daño a", enemigo.nombre)
        if enemigo.esta_vivo():
            print("La vida de", enemigo.nombre, "es", enemigo.vida, "puntos")
        else:
            enemigo.morir()
            
        def get_fuerza(self):
            return self.fuerza
        
        def  set_fuerza(self, fuerza):
            if fuerza < 0:
                print("Error, has introducido un valor negativo")
            else:
                self.fuerza = fuerza
                
class Guerrero(Personaje):
    
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada
        
    def  atributos(self):
        super().atributos()
        print("# Espada:", self.espada)
        
    def  daño(self, enemigo):
        return self.fuerza * self.espada - enemigo.defensa
    
    
class Arquero(Personaje):
    
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, arco):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.arco = arco
        
    def  atributos(self):
        super().atributos()
        print("# arco:", self.arco)
        
    def  daño(self, enemigo):
        return self.inteligencia * self.arco - enemigo.defensa

def salir_juego():    
    print("Adios")    
    
def comenzar():
    
    mago = Personaje("Mago", 20, 15, 10, 100)
    guerrero = Guerrero("Guerrero", 20, 15, 10, 100, 5)
    arquero = Arquero("Arquero", 20, 15, 10, 100, 5)
    

    
    while True:
        
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
            salir_juego()
            break
        
        else:
            print("La opcion ingresa es incorrecta, por favor ingresa nuevamente\n")
               
    
comenzar()        
        