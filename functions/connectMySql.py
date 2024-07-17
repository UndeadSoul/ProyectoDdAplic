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
#modificar estado del dia
def modifyDay(user,db):
  while True:
    system("cls")
    print('+'*4,'Menu estado del dia','+'*4)
    try:
      dia=int(input('\n1. Ver estado del dia.\
            \n2. Modificar estado del dia.\
            \n3. Salir.\
            \n =>'))
      while dia!=1 and dia!=2 and dia!=3:
        dia=int(input('Error, Opcion invalida\
          \n1. Ver estado del dia.\
          \n2. Modificar estado del dia.\
          \n3. Salir.\
          \n =>'))        
    except Exception as err:
      print(err)
    
    #ver estado del dia
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
        print('\nNo se ha ingresado estado del dia')
      
      input('\nPresione ENTER para continuar...')
    
    #Modificar estado del dia
    elif dia==2:
      sq1='select * from bazar'
      try:
        db.cursor.execute(sq1)
        estDia=db.cursor.fetchone()
        
      except Exception as err:
        print(err)
        
      if estDia!=None:
        print(f'Estado Del dia:\t{estDia[1]}')
        if estDia[1]=='abierto':
          est=input(f'El estado del dia esta {estDia[1]}\
                \n¿Desea cambiarlo a Cerrado?(s/n)')
          while est!='s' and est!='n':
            est=input('\nError, Opcion invalida\
                      \n¿Desea cambiarlo a Cerrado?(s/n)')
          if est.lower()=='s':
            try:
              rutjef=input('Ingrese su rut para confirmar(sin punto y con guion)\n\n')
              sq2=f'select * from jefeDeVentas where rutJefe={repr(rutjef)}'
              db.cursor.execute(sq2)
              rutCon=db.cursor.fetchone()
            except Exception as err:
              print(err)
            if rutCon!=None:
              print('rut confirmado\
                    \nCambiando el estado del dia a cerrado')
              sq3=f'update bazar set estadoDia="cerrado", ultModificador={repr(rutjef)} where idBazar={repr(estDia[0])}'
              try:
                db.cursor.execute(sq3)
                db.conexion.commit()
              except Exception as err:
                db.conexion.rollback()
                print(err)
              print('\nEstado del dia cambiado')
            else:
              pass
          else:
            pass
        elif estDia[1]=='cerrado':
          est=input(f'El estado del dia esta {estDia[1]}\
                \n¿Desea cambiarlo a Abierto?(s/n)')
          while est!='s' and est!='n':
            est=input('\nError, Opcion invalida\
                      \n¿Desea cambiarlo a Abierto?(s/n)')
          if est.lower()=='s':
            try:
              rutjef=input('Ingrese su rut para confirmar(sin punto y con guion)\n\n')
              sq2=f'select * from jefeDeVentas where rutJefe={repr(rutjef)}'
              db.cursor.execute(sq2)
              rutCon=db.cursor.fetchone()
            except Exception as err:
              print(err)
            if rutCon!=None:
              print('rut confirmado\
                    \nCambiando el estado del dia a abierto')
              sq3=f'update bazar set estadoDia="abierto", ultModificador={repr(rutjef)} where idBazar={repr(estDia[0])}'
              try:
                db.cursor.execute(sq3)
                db.conexion.commit()
              except Exception as err:
                db.conexion.rollback()
                print(err)
              print('\nEstado del dia cambiado')
            else:
              pass
          else:
            pass
      else:
        print('No se ha ingresado estado del dia')

      input('\nPresione ENTER para continuar...')
    
    #Salir del menu
    elif dia==3:
      print('Abandonando MODIFYDAY...')
      break

def getRecords(user,db):
  print("2. obtener registros")

#Agregar producto
def ProductManager(user,db):
  while True:
    system("cls")
    print('+'*4,'Menu De Productos','+'*4)
    try:
      opProd=int(input('\n1. Ver productos.\
            \n2. Agregar productos.\
            \n3. Modificar producto\
            \n4. Eliminar producto\
            \n5. Salir.\
            \n =>'))
      while opProd!=1 and opProd!=2 and opProd!=3 and opProd!=4 and opProd!=5:
        opProd=int(input('Error, Opcion invalida\
          \n1. Ver productos.\
          \n2. Agregar productos.\
          \n3. Modificar producto\
          \n4. Eliminar producto\
          \n5. Salir.\
          \n =>'))        
    except Exception as err:
      print(err)
    
    if opProd==1:
      sq1='select * from producto'
      try:
        db.cursor.execute(sq1)
        verProd=db.cursor.fetchone()
        print(verProd)
      except Exception as err:
        print(err)
      
      input('\nPresione ENTER para continuar...')  
      
    elif opProd==2:
      idprod=input('Ingrese Codigo del producto')

      sq1=f'select codProd from producto where codProd={repr(idprod)}'
      try:
        db.cursor.execute(sq1)
        if db.cursor.fetchone()==None:
          nombProd=input('Ingrese Nombre del producto: ')
          valorProd=int(input('Ingrese valor unitario del producto: '))
          rutJefe=input(f'Usted va a agregar el producto {nombProd}\
                        \nIngre su Rut para confirmar (sin puntos y con guion)\n=>')
          sq2=f'select * from jefeDeVentas where rutJefe={repr(rutJefe)}'
          try:
              db.cursor.execute(sq2)
              rutCon=db.cursor.fetchone()
          except Exception as err:
              print(err)
          if rutCon!=None:
              print('rut confirmado\
                    \nAgregando producto')
              sq3=f'insert into producto values({repr(idprod)},{repr(nombProd)},{repr(valorProd)},{repr(rutJefe)})'
              try:
                db.cursor.execute(sq3)
                db.conexion.commit()
              except Exception as err:
                db.conexion.rollback()
                print(err)
        
        else:
          print('Producto ya existente')

      except Exception as err:
        print(err)

    elif opProd==3:
      pass
    elif opProd==4:
      pass
    elif opProd==5:
      print('Abandonando Menu de productos...')
      break


def addUser(user,db):
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
  sq1=f'select codProd,nombreProd,valorUnit from producto where codprod={codigoProd}'
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

#Calcular el total de los productos
def productTotal(productList):
  total=0
  for i in range(len(productList)):
    total=total+(productList[i][4])
  return total

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
def generateSell(user,productList,total,db):
  #inicializacion
  tipoDoc=""
  claveDoc=""
  confirm=""
  numBoleta=1
  #ciclo para preguntar por modificaciones
  while True:
    #elegir documento
    system("cls")
    #mostrar la lista con el total
    print(productList)
    tipoDoc=input("Desea boleta o factura (b/f): ")
    while tipoDoc!="b" and tipoDoc!="f":
      system("cls")
      #mostrar la lista con el total
      print(productList)
      tipoDoc=input("Desea boleta o factura (b/f): ")
    #preguntar por confirmacion
    system("cls")
    #mostrar la lista con el total y eleccion de documento
    print(productList)
    print(tipoDoc)
    confirm=input("Está correcto? (si/no): ")
    while confirm!="si" and confirm!="no":
      system("cls")
      #mostrar la lista con el total
      print(productList)
      confirm=input("Está correcto? (si/no): ")
    if confirm=="no":
      print("Volviendo al menu de vendedor")
      return
    if tipoDoc=="b":
      #boleta
        #buscar numero de boleta
        sq1=(f'select cantBoletas from bazar where idbazar="1234"')
        #execucion consulta
        try:
          db.cursor.execute(sq1)
          num=db.cursor.fetchone()
          numBoleta=numBoleta+num[0]
          print("cantidad boletas:",numBoleta)
        except Exception as err:
          db.conexion.rollback()
          print(err)
        #actualizar cantidad de boletas
        sq2=(f'update bazar set cantBoletas=cantBoletas+1')
        #execucion update
        try:
          db.cursor.execute(sq2)
          db.conexion.commit()      
          print("cantidad de boletas actualizado")
        except Exception as err:
          db.conexion.rollback()
          print(err)
        #generar boleta
        totalNeto=total
        #subir a bdd
        sq3=(f'insert into boleta values({repr(numBoleta)},{repr(totalNeto)})')
        #execucion insert
        try:
          db.cursor.execute(sq3)
          db.conexion.commit()
          print("Boleta guardada")
        except Exception as err:
          db.conexion.rollback()
          print(err)
    elif tipoDoc=="f":
      #factura
        #preguntar datos
        #generar factura
        #subir a base de datos
        pass
    #registrar venta en bdd
    return