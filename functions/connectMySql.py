import mysql.connector
import tabulate as tab

#ingresa de bdd
class Database():
    def __init__(self):
        self.conexion = mysql.connector.connect(
            user='root',
            password='contramysql',
            host='127.0.0.1',
            database='nona')
        self.cursor = self.conexion.cursor()
    
    def cerrarBD(self):
        self.cursor.close()
        self.conexion.close()


def credentials(user,password,db):
    
    tipousuario="algo"
    sq1=f'select * from vendedor where userName={repr(user)} and password1={repr(password)}'

    try:
      db.cursor.execute(sq1)
      result=db.cursor.fetchone()
    
    except Exception as err:
      print(err)

    return(tipousuario)

###Sales manager menu functions###
def modifyDay(user):
  print("1. modificar dia")

def getRecords(user):
  print("2. obtener registros")

def addProduct(user):
  print("3. agregar producto")

def addUser(user):
  print("4. agregar usuario")

###Seller menu functions###
def searchProd(user):
  print("1. Buscar producto")

def addProduct(user):
  print("2. Agregar producto")

def delProduct(user):
  print("3. Eliminar producto")

def generateSell(user):
  print("4. Generar venta")