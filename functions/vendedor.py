from os import system
from functions.connectMySql import *

def sellerMenu(user):
    system("cls")
    print("sellerMenu")
###########
    option=0
    while True:
        #TODO crear una lista con los productos que se vayan agregando a la venta y mostrarlos encima del menu
        productList=[]
        while True:
            try:
                option=int(input("Elija una opcion:\
                            \n1. Buscar Producto\
                            \n2. Agregar Producto\
                            \n3. Eliminar producto\
                            \n4. Generar Venta\
                            \n5. Cerrar sesión\
                            \n=> "))
                while option<=0 or option>5:
                    system("cls")
                    option=int(input("ERROR. Elija una opcion: \
                                \n1. Buscar Producto\
                                \n2. Agregar Producto\
                                \n3. Eliminar producto\
                                \n4. Generar Venta\
                                \n5. Cerrar sesión\
                                \n=> "))
                break
            except ValueError:
                input("Error. Ingrese una opcion valida para el menu(presione enter para continuar)...")
                system("cls")
        system("cls")
        match option:
            case 1: #buscar producto
                searchProd(user)
                pass
            case 2: #agregar producto
                addProduct(user)
                pass
            case 3: #eliminar producto
                delProduct(user)
                pass
            case 4: #generar venta
                generateSell(user)
                pass
            case 5: #salir a inicio de sesión
                print("5")
                break
        input("continuar")
        system("cls")

###########
    input("presione enter")
    pass