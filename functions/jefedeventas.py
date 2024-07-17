from os import system
from functions.connectMySql import *

def salesManagerMenu(user,db):
    system("cls")
    print("salesManMenu")
###########
    option=0
    while True:
        while True:
            try:
                option=int(input("Elija una opcion:\
                            \n1. Modificar día\
                            \n2. Obtener registros\
                            \n3. Agregar producto\
                            \n4. Agregar Nuevo Usuario\
                            \n5. Cerrar sesión\
                            \n=> "))
                while option<=0 or option>5:
                    system("cls")
                    option=int(input("ERROR. Elija una opcion: \
                                \n1. Modificar día\
                                \n2. Obtener registros\
                                \n3. Agregar producto\
                                \n4. Agregar Nuevo Usuario\
                                \n5. Cerrar sesión\
                                \n=> "))
                break
            except ValueError:
                input("Error. Ingrese una opcion valida para el menu(presione enter para continuar)...")
                system("cls")
        system("cls")
        match option:
            case 1: #modificar día
                modifyDay(user,db)
                pass
            case 2: #obtener registros
                getRecords(user,db)
                pass
            case 3: #agregar producto
                ProductManager(user,db)
                pass
            case 4: #agregar nuevo usuario
                addUser(user,db)
                pass
            case 5: #salir a inicio de sesión
                print("5")
                break
        input("continuar")
        system("cls")

###########
    input("presione enter")
    pass