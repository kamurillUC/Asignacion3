from mis_funciones import *
#lavar_platos()
#ir_de_compras()
#cenar()
#limpiarConsola()

bandera = 0
respuesta = 0

limpiarConsola()
while bandera == 0:
    
    print(f">< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< ><\nMenú de opciones:\n1. Lavar los platos\n2. Ir de compras\n3. Cenar\n4. Salir")
    respuesta = input(">< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< ><\nDigite su opción: ")
    if respuesta == "1":
        lavar_platos()
    elif respuesta == "2":
        ir_de_compras()
    elif respuesta == "3":   
        cenar() 
    else:
        break


