#Funcion de Lavar los platos
def lavar_platos():

    respuesta = ""

    print('Caminar al fregadero...')

    respuesta = input('¿Hay platos sucios para lavar?(Si/No)')
    if respuesta.lower() == 'si':        
        respuesta = input('¿Quiero lavar los platos en este momento?(Si/No)')
        if respuesta.lower() == 'si':            
            respuesta = input('¿Hay agua, jabón y esponja?(Si/No)')
            if respuesta.lower() == 'si':
                print('Lavar los platos')
                print('Secar los platos')
                print('Guardar los platos')
                print('Fin')
            else:
                print('Fin')
        else:
            print('Fin')
    else:
        print('Fin')


#Funcion de Ir de compras
def ir_de_compras():

    respuesta = ""
    bandera = 0

    respuesta = input('¿Tengo dinero para gastar?(Si/No)')    
    if respuesta.lower() == 'si':        
        print("Ir a un centro comercial")        
        
        while bandera == 0:
            respuesta = input('¿Hay alguna tienda que me interese comprar?(Si/No)')
            if respuesta.lower() == 'si':
                print("Ir a la tienda")
                print("Ver productos de la tienda...")
                respuesta = input('¿Encontré algún producto que quiera comprar?(Si/No)')
                if respuesta.lower() == 'si':
                    print("Comprar producto")
                print("Salir de la tienda") 
            else:
                break
        print("Salir del centro comercial")    
        print("Fin")                    
    else:
        print("Fin")


#Funcion de Cenar
def cenar():
    
    respuesta = ""

    respuesta = input('¿Tengo hambre?(Si/No)') 
    if respuesta.lower() == 'si':             
        respuesta = input('¿Hay cena hecha?(Si/No)')
        if respuesta.lower() == 'no':        
            print("Hacer la cena")            
        
        print("Servir la comida")
        print("Cenar")
        print("Llevar los platos al fregadero")
    
    print("Fin")


#Funcion para limpiar consola segun OS
def limpiarConsola():
    import os
    if os.name == "posix" or os.name == "mac":
        os.system("clear")
    elif os.name == "ce" or os.name == "dos" or os.name == "nt":
        os.system("cls")
