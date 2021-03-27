import datetime
import numpy as np
c='COSMETICOS AARON'
a='Lo atendio: Aaron Sanchez'
productos_cosmeticos = {'Nombre del articulo':['Decolorante','Protector solar','Lapiz labial','Delineador'],
                        'Codigo del articulo':[1215,2069,3030,4045],
                        'Descripcion del articulo':['Sirve para decolorar el cabello','Te proteje de los rayos UV','Hidrata tus labios','Define el contorno de los ojos'],
                        'Cantidad en almacen':[60,80,40,60,50],
                        'Precio de venta':[120,100,85,90]}
print(f"Esto es lo que cuenta la cosmetica: {productos_cosmeticos}")
while True:
    print("Menu")
    print("[1]Registar una venta")
    print("[2]Consultar una venta")
    print("[3] Salir")
    pre1= int(input('escoge una opcion: \n'))
    if (pre1<=0) or (pre1>=4):
        print("Esta opcion no esta dispnible.")
        print("Intente de nuevo.")
    else:
        if (pre1==1):
            print("Registro de venta")
            print("")
            pre2= int(input("Quieres registar una venta? \n(1-Si / 0-No):\n"))
            if(pre2==0):
                print("Gracias por su tiempo.")
            if (pre2==1):
                opciones= int(input("Ingrese 1 si solo llevara un articulo, de lo contrario ingrese 2: \n"))
                if (opciones==1):
                    pre3=input('Ingrese la fecha (dd/mm/aaaa):  \n')
                    convercion_fecha = datetime.datetime.strptime(pre3, "%d/%m/%Y").date()
                    pre4=int(input('Ingrese el codigo de la venta: \n'))
                    while True:
                        pre5=int(input('Ingrese el codigo del articulo: \n'))
                        if (pre5==1215) or (pre5==2069) or (pre5==3030) or (pre5==4045):
                            break
                        else:
                            print("Vuelva a intentar de nuevo con otro codigo")
                    pre6=input("Ingrese una descripcion del articulo:\n")
                    pre7=int(input("Ingrese la cantidad de piezas a vender:\n"))
                    pre8=float(input("Ingrese el precio de venta: \n"))
                    multiplicacion=pre7 * pre8
                    print(c)
                    print(a)
                    print(pre3)
                    print(f"Codigo de venta: {pre4}")
                    print(f"Codigo del articulo: {pre5}")
                    print(f"Descripcion del producto: {pre6}")
                    print(f"el total de su compra es: {multiplicacion}")
                if(opciones==2):
                    lista_articulo=[]
                    lista_descripcion=[]
                    lista_cantidad=[]
                    lista_precio=[]
                    pre3=input('Ingrese la fecha (dd/mm/aaaa):  \n')
                    convercion_fecha = datetime.datetime.strptime(pre3, "%d/%m/%Y").date()
                    pre4=int(input('Ingrese el codigo de la venta: \n'))
                    for elemento in range(3):
                        pre5=int(input('Ingrese el codigo del articulo: \n'))
                        lista_articulo.append(pre5)
                    for elemento in range(3):
                        pre6=input("Ingrese una descripcion del articulo:\n")
                        lista_descripcion.append(pre6)
                    for elemento in range(3):
                        pre7=int(input("Ingrese la cantidad de piezas a vender:\n"))
                        lista_cantidad.append(pre7)
                    for elemento in range(3):
                        pre8=int(input("Ingrese el precio de venta: \n"))
                        lista_precio.append(pre8)
                    print(c)
                    print(a)
                    print(pre3)
                    print(f"Codigo de venta: {pre4}")
                    print(f"Codigos de los articulos: {lista_articulo}")
                    print(f"Descripcion de cada producto: {lista_descripcion}")
                    print(f"Cantidad de piezas a vender por cada articulo:{lista_cantidad}")
                    print(f"Precio por unidad de articulo:{lista_precio}")
                    arraypre7= np.array(lista_cantidad)
                    arraypre8= np.array(lista_precio)
                    multiplicacion= arraypre7 * arraypre8
                    print(f"El total de cada articulo es:{multiplicacion}")
                    suma=sum(multiplicacion)
                    print(f"El total a pagar es de: ${suma}")
        if (pre1==2):
            opciones= int(input("Ingresa 1 si quieres ver ventas de 1 articulo, ingresa 2 si compraste mas de un articulo: \n"))
            if (opciones==1):#esto hace que se mande a imprimir si solo ingreso un articulo
                while True:
                    busqueda= int(input("Ingrese el codigo de la venta: \n"))
                    if (busqueda==pre4):
                        diccionario_clientes={'Informacion de venta ecnontrada':[c,a,pre3,pre4,pre5,pre6,pre7,pre8,multiplicacion]}
                        for cliente in diccionario_clientes:
                            print(diccionario_clientes)#aqui debe de imprimir el diccionario que hice en la opcion de arriba
                    else:
                        print("No se encontro el codigo.")
                        break
            if (opciones==2):#en esta opcion debe de mostrar lo que se vendio de mas de un articulo
                while True:
                    busqueda= int(input("Ingrese el codigo de la venta: \n"))
                    if (busqueda==pre4):
                        diccionario_clientes={'Informacion de venta ecnontrada':[c,a,pre3,pre4,lista_articulo,lista_descripcion,lista_cantidad,lista_precio,multiplicacion,suma]}
                        for cliente in diccionario_clientes:
                            print(diccionario_clientes)#aqui debe de imprimir el diccionario que hice en la opcion de arriba
                    else:
                        print("No se encontro el codigo.")
                        break
        if (pre1==3):
            print('Por favor espere')
            print('...')
            print("Gracias por su visita ,vuelva pronto")
            break
