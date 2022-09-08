from ast import While
import os
clear = lambda: os.system("cls")
clear()

lista = []

for i in range(1):
    dato_ingresado = input('Ingrese un numero: ')
    
    if dato_ingresado.isnumeric():
        lista.append(int(dato_ingresado))
    
    else:
        print('No es un numero')
        break
        
print(lista)

print('------------------------------------')

'''WHILE'''


saldo = 10000

while True:
            
    print("\n\n MENU \n")
    print("El saldo actual de su cuenta es: $", saldo)
    print("1. Deposito")
    print("2. Extraccion")
    print("3. Transferencia")
    print("4. Salir")
    opcion = input("Selecciona una opcion: ")
       
    if( opcion == "1"):
        
        valorIngresado = int(input('\nCuanto dinero desea ingresar: $'))
        
        if valorIngresado > 0:        
            print('La operacion ha sido realizada correctamente')
            
        saldo += valorIngresado    
        print('Su saldo actual es: $', saldo)
            
        '''break'''
        
    elif( opcion == "2"):
        
        valorIngresado = int(input('\nCuanto dinero desea extraer: $')) 
          
        if saldo >= valorIngresado:            
            print('La operacion ha sido realizada correctamente')
            saldo -= valorIngresado
        else:
            print('No hay saldo suficientes para realizar la operacion')
                
        print('Su saldo actual es: $', saldo)

               
    elif( opcion == "3"):
        
        valorIngresado = int(input('\nCuanto dinero desea transferir: $'))
        input('Ingrese el numero de cuenta: ') 
          
        if saldo >= valorIngresado:            
            print('La operacion ha sido realizada correctamente')
            saldo -= valorIngresado
        else:
            print('No hay saldo suficientes para realizar la operacion')
                
        print('Su saldo actual es: $', saldo)
        
        
    elif(opcion == "4"):
        print("\nAdios")
        break
    else:
        print("Opcion no valida")


















