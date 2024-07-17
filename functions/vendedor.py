from os import system;
from functions.connectMySql import *
from functions.prints import *

def sellerMenu(user,db):
    print("Menú Vendedor") 
    productList=[]
    productListTotal=0
    lastSearch=""
    option=0
    while True:
        while True:
            try:
                system("cls")
                printPrLs(productList,lastSearch,productListTotal)
                option=int(input("Elija una opcion:\
                            \n1. Buscar Producto\
                            \n2. Agregar Producto\
                            \n3. Eliminar producto\
                            \n4. Generar Venta\
                            \n5. Cerrar sesión\
                            \n=> "))
                while option<=0 or option>5:
                    system("cls")
                    printPrLs(productList,lastSearch,productListTotal)
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
        system("cls")   #cls previo a las opciones del menu
        match option:
            case 1: #buscar producto
                lastSearch=searchProd(db)
                input("Presione enter para continuar... ")
                pass
            case 2: #agregar producto
                productList=addProduct(lastSearch,productList)
                productListTotal=productTotal(productList)
                input("Presione enter para continuar... ")
                pass
            case 3: #eliminar producto
                delProduct(productList)
                productListTotal=productTotal(productList)
                input("Presione enter para continuar... ")
                pass
            case 4: #generar venta
                generateSell(user,productList,productListTotal,db)
                input("Presione enter para continuar... ")
                pass
            case 5: #salir a inicio de sesión
                print("5")
                break
        system("cls")
    input("presione enter")
    pass