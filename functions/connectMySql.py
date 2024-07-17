import mysql.connector
import tabulate as tab
from os import system

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

#terminado ¡¡¡NO TOCAR!!!
def credentials(user,password,db):

    sq1=f'select * from vendedor where userName={repr(user)} and password1={repr(password)}'
    try:
      db.cursor.execute(sq1)
      result=db.cursor.fetchone()

    except Exception as err:
      db.conexion.rollback()
      print(err)
    
    if result!=None:
       if result[1]==user and result[2]==password:
        tipousuario='Vendedor'
    else:
      sq2=f'select * from jefeDeVentas where userName={repr(user)} and password1={repr(password)}'
      try:
        db.cursor.execute(sq2)
        result2=db.cursor.fetchone()
      except Exception as err:
        db.conexion.rollback()
        print(err)
      if result2!=None: 
        if result2[1]==user and result2[2]==password:
          tipousuario='Jefedeventas'
      else:
        tipousuario="Usuario invalido"
    return(tipousuario)

###Sales manager menu functions###
def modifyDay(user,db):
  while True:
    system("cls")
    print('+'*4,'Menu estado del dia','+'*4)
    try:
      dia=int(input('\n1.- Ver estado del dia.\
            \n2.- Modificar estado del dia.\
            \n3.- Salir.\
            \n =>'))
      while dia!=1 and dia!=2 and dia!=3:
        dia=int(input('Error, Opcion invalida\
          \n1.- Ver estado del dia.\
          \n2.- Modificar estado del dia.\
          \n3.- Salir.\
          \n =>'))        
    except Exception as err:
      print(err)
    
    if dia==1:
      sql1='select * from bazar'
      try:
        db.cursor.execute(sql1)
        verD=db.cursor.fetchone()
      except Exception as err:
        print(err)
      if verD!=None:
        print(f'Estado Del dia:\t{verD[1]}') 
      else:
        print('No se ha ingresado estado del dia')
      
      input('Presione ENTER para continuar...')
    
    elif dia==2:
    
      sq1='select estadoDia from bazar'
      try:
        db.cursor.execute(sq1)
        verD=db.cursor.fetchone()
        
      except Exception as err:
        print(err)
        
      if verD!=None:
        print(f'Estado Del dia:\t{verD[1]}')
        if verD[1]=='abierto':
          est=input(f'El estado del dia esta {verD[1]}\
                \n¿Desea cambiarlo a Cerrado?(s/n)')
          while est!='s' or est!='n':
            est=input('Error, Opcion invalida\
                      \n¿Desea cambiarlo a Cerrado?(s/n)')
          if est.lower()=='s':
            sq2=f'update bazar set estadoDia="cerrado", ultModificador={repr(user)} '
            try:
              db.cursor.execute(sq2)
              verD=db.cursor.fetchone()
            except Exception as err:
              print(err)  
            print('se ha actualizado el estado del dia a cerrado')
            input('Presione ENTER para continuar...')
          
          else:
            pass
        
        elif verD[1]=='cerrado':
          est=input(f'El estado del dia esta {verD[1]}\
                \n¿Desea cambiarlo a Abierto?(s/n)')
          while est!='s' or est!='n':
            est=input('Error, Opcion invalida\
                      \n¿Desea cambiarlo a Abierto?(s/n)')
          


      else:
        print('No se ha ingresado estado del dia')
      
      input('Presione ENTER para continuar...')
      

    elif dia==3:
      input('Abandonando MODIFYDAY presione ENTER para continuar...')
      break

def getRecords(user):
  print("2. obtener registros")

def addProduct(user):
  print("3. agregar producto")

def addUser(user):
  print("4. agregar usuario")

###Seller menu functions###
#Buscar producto
def searchProd(db):  
  codigoProd=0
  #Consulta codigo de producto a buscar
  while True:
    try:
      codigoProd=int(input("Ingrese codigo producto: "))
      break
    except ValueError:
      print("Error, el codigo de producto debe ser numerico (8 digitos)")
      input("Presione enter para continuar... ")
  #comando Consulta Sql
  sq1=f'select * from producto where codprod={codigoProd}'
  #execucion consulta
  try:
    db.cursor.execute(sq1)
    result=db.cursor.fetchone()
  except Exception as err:
    db.conexion.rollback()
    print(err)
  #retorno
  print("Producto Encontrado")
  print(result) #TODO formatear el resultado
  return(result)

#Agregar producto
def addProduct(producto,productList): 
  #revisa si se ha buscado un producto
  if(producto==None or len(producto)<1):
    print("Debe haber buscado un producto valido")
    return productList
  #si hay un producto
  else:
    #transformar el producto de ty
    producto=list(producto)
    #preguntar por cantidad a agregar
    while True:
      try:
        system("cls")
        #presentar datos del producto
        print(producto)
        cantidad=int(input("Ingrese cantidad a agregar del producto: "))
        while cantidad<1:
          system("cls")
          #presentar datos del producto
          print(producto) #TODO formatear el producto
          cantidad=int(input("Ingrese cantidad a agregar del producto(Mayor a 0): "))
        break
      except ValueError:
        print("Error, la cantidad de producto debe ser numerico")
        input("Presione enter para continuar... ")
    #añadirlo a la lista
    producto.append(cantidad)
    producto.append(cantidad*producto[2])
    productList.append(producto)
    return productList

#Eliminar producto
def delProduct(productList):
  #preguntar cual quiere eliminar
  codigo=0
  eleccion=""
  while True:
    #imprimir la lista de productos para elegir el producto a eliminar
    system("cls")
    print(productList)  #TODO formatear lista de productos
    try:
      #mostrar los elementos de la lista de ventas
      codigo=int(input("Ingrese el codigo del producto que desea eliminar: "))
      break
    except ValueError:
      print("Error, el codigo de producto debe ser numerico (8 digitos)")
      input("Presione enter para continuar... ")
  #buscar el producto en la lista
  for i in range(len(productList)):
    print(productList[i])
    if productList[i][0]==codigo:
      #si está correcto, preguntar confirmacion
      while eleccion!="no" and eleccion!="si":
        system("cls")
        eleccion=input(f"Desea eliminar el producto {productList[i]}?(si/no) ").lower()
      if eleccion=="si":
        del productList[i]
        print("Producto eliminado")
        print(productList)  #? conservar?
      else:
        print("Producto no eliminado")
      return productList
  #si no se encuentra el producto se termina la funcion y se vuelve al menu
  print("El producto ingresado no se ha encontrado")
  #? no si está incorrecto podria preguntar si quiere cancelar o intentarlo denuevo

#Generar venta
def generateSell(user,productList,db):
  #inicializacion
  tipoDoc=""
  confirm=""
  #ciclo para preguntar por modificaciones
  while True:
    #elegir documento
    system("cls")
    #mostrar la lista con el total
    print(productList)
    tipoDoc=int(input("Desea boleta o factura (b/f): "))
    while tipoDoc!="b" and tipoDoc!="f":
      system("cls")
      #mostrar la lista con el total
      print(productList)
      tipoDoc=int(input("Desea boleta o factura (b/f): "))
    #preguntar por confirmacion
    system("cls")
    #mostrar la lista con el total y eleccion de documento
    print(productList)
    print(tipoDoc)
    tipoDoc=int(input("Está correcto? (si/no): "))
    while confirm!="si" and confirm!="no":
      system("cls")
      #mostrar la lista con el total
      print(productList)
      tipoDoc=int(input("Está correcto? (si/no): "))
    if confirm=="no":
      print("Volviendo al menu de vendedor...")
      
      #boleta
        #generar boleta
        #subir a bdd
      #factura
        #preguntar datos
        #generar factura
        #subir a base de datos
    #registrar venta en bdd
  print("4. Generar venta") #!borrar en version final