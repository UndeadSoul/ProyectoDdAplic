from .functions.jefedeventas import *
from .functions.vendedor import *
from .functions.connectMySql import *
from os import system

while True:
    system("cls")
    user=input("Ingrese Usuario: ")
    password=input("ingrese Contraseña: ")
    typeOfUser=credentials(user,password)
    match typeOfUser.lower():
        case "vendedor":
            sellerMenu()
        case "jefedeventas":
            salesManagerMenu()
        case _:
            input("Las credenciales entregadas no coinciden con ninguna en nuestra base de datos.\
                  \nPresione Enter para intentar nuevamente")
    
