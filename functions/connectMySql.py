import mysql.connector
import tabulate as tab
from os import system
import time
from datetime import date
from pwinput import pwinput
from functions.prints import *

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

def estadocheck(db):
  estado=""
  sq0=f'select estadodia from bazar'
  try:
    db.cursor.execute(sq0)
    result=db.cursor.fetchone()
    estado=str(result[0])
  except Exception as err:
    db.conexion.rollback()
    print(err)

  return estado

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
def modifyDay(db):
  while True:
    system("cls")
    print('+'*4,'Menu estado del dia','+'*4)
    try:
      dia=int(input('\n1. Ver estado del dia.\
            \n2. Modificar estado del dia.\
            \n3. Salir.\
            \n =>'))
      while dia!=1 and dia!=2 and dia!=3:
        system("cls")
        dia=int(input('Error, Opcion invalida\
          \n1. Ver estado del dia.\
          \n2. Modificar estado del dia.\
          \n3. Salir.\
          \n =>'))        
    except Exception as err:
      pass
    #ver estado del dia
    if dia==1:
      sql1='select estadoDia, ultModificador from bazar'
      try:
        db.cursor.execute(sql1)
        verD=db.cursor.fetchall()
      except Exception as err:
        print(err)
      if verD!=None:
        system("cls")
        print(tab.tabulate(verD,headers=["Estado del dia","Ultimo Modificador"],tablefmt="psql")) 
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
      system("cls")
      if estDia!=None:
        #################dia abierto###################
        if estDia[1]=='abierto':
          est=input(f'El estado del dia esta {estDia[1]}\
                \n¿Desea cambiarlo a Cerrado?(s/n) \n=> ')
          while est!='s' and est!='n':
            est=input('\nError, Opcion invalida\
                      \n¿Desea cambiarlo a Cerrado?(s/n) \n=> ')
          if est.lower()=='s':
            system("cls")
            try:
              rutjef=input('Ingrese su rut para confirmar(sin punto y con guion)\n\n=>')
              sq2=f'select * from jefeDeVentas where rutJefe={repr(rutjef)}'
              db.cursor.execute(sq2)
              rutCon=db.cursor.fetchone()
            except Exception as err:
              print(err)
            if rutCon!=None:
              system("cls")
              print('rut confirmado')
              sq3=f'update bazar set estadoDia="cerrado", ultModificador={repr(rutjef)} where idBazar={repr(estDia[0])}'
              try:
                db.cursor.execute(sq3)
                db.conexion.commit()
              except Exception as err:
                db.conexion.rollback()
                print(err)
              print('\nEstado del dia cambiado')
            else:
              system("cls")
              print("El rut de confirmación ingresado no concuerda")
          else:
            system("cls")
            print("\nEstado del dia no se ha modificado")
        ##################dia cerrado###################
        elif estDia[1]=='cerrado':
          est=input(f'El estado del dia esta {estDia[1]}\
                \n¿Desea cambiarlo a Abierto?(s/n) \n=>')
          system("cls")
          while est!='s' and est!='n':
            est=input('\nError, Opcion invalida\
                      \n¿Desea cambiarlo a Abierto?(s/n) \n=>')
            system("cls")
          if est.lower()=='s':
            try:
              rutjef=input('Ingrese su rut para confirmar(sin punto y con guion)\n\n=> ')
              system("cls")
              sq2=f'select * from jefeDeVentas where rutJefe={repr(rutjef)}'
              db.cursor.execute(sq2)
              rutCon=db.cursor.fetchone()
            except Exception as err:
              print(err)
            if rutCon!=None:
              print('Rut confirmado')
              sq3=f'update bazar set estadoDia="abierto", ultModificador={repr(rutjef)} where idBazar={repr(estDia[0])}'
              try:
                db.cursor.execute(sq3)
                db.conexion.commit()
              except Exception as err:
                db.conexion.rollback()
                print(err)
              print('\nEstado del dia cambiado')
            else:
              system("cls")
              print("El rut de confirmación ingresado no concuerda")
          else:
            system("cls")
            print("\nEstado del dia no se ha modificado")
      else:
        print('No se ha ingresado estado del dia')

      input('\nPresione ENTER para continuar...')
    
    #Salir del menu
    elif dia==3:
      system("cls")
      print('Abandonando Menu estado del día')
      break

def getRecords(user,db):
  while True:
    system("cls")
    print('+'*4,'Gestor de Ventas','+'*4)
    try:
      ###Aqui bro
      reps=int(input('1. Ver Tabla Registro de ventas\
                 \n2. Salir\
                  \n=> '))
    except Exception:
      pass
    system("cls")
    print('Registros de venta')
    if reps==1:
      sq1='select * from registroDeVenta'
      try:
        db.cursor.execute(sq1)
        verVents=db.cursor.fetchall()
        print(tab.tabulate(verVents,headers=['Codigo Venta','Fecha de venta','Tipo de Doc','Numero de Factura','Numero de Boleta','Rut Vendedor'],tablefmt="psql"))
      except Exception:
        pass
    elif reps==2:
      print('\nAbandonando Registros de Ventas...\n')
      break
    else:
      print('Opcion invalida')
    input('\nPresione ENTER para continuar...')

#Agregar producto
def ProductManager(user,db):
  while True:
    system("cls")
    print('+'*4,'Gestor de Productos','+'*4)
    try:  #TODO validar que sea entre esos valores y que sea un int, como medida temporal la excepcion lo transforma en un 5 para que vuelva al menu
      opProd=int(input('\n1. Ver productos.\
            \n2. Agregar productos.\
            \n3. Modificar producto\
            \n4. Eliminar producto\
            \n5. Salir.\
            \n => '))      
    except Exception:
      opProd=5
      pass
    system("cls")
    #verproductos
    if opProd==1:
      sq1='select * from producto'
      try:
        db.cursor.execute(sq1)
        verProd=db.cursor.fetchall()
        print(tab.tabulate(verProd,headers=["Id Producto","Nombre producto","Valor producto","Rut jefe agregado"],tablefmt="psql"))
      except Exception as err:
        print(err)
    #agregar producto  
    elif opProd==2:
      try:
        while True:
          try:
            system("cls")
            idprod=int(input('Ingrese Codigo del producto: '))
            system("cls")
            break
          except ValueError:
            print("Error. Intente nuevamente usando digitos")
        sq1=f'select codProd from producto where codProd={repr(idprod)}'
        db.cursor.execute(sq1)
        if db.cursor.fetchone()==None:
          system("cls")
          nombProd=input('Ingrese Nombre del producto: ')
          system("cls")
          valorProd=0
          while True:
            try:
              system("cls")
              valorProd=int(input('Ingrese valor unitario del producto: '))
              system("cls")
              while(valorProd<=0):
                system("cls")
                valorProd=int(input('Ingrese valor unitario del producto valido(Mayor a 0): '))
              system("cls")
              break
            except ValueError:
              print("Error. Intente nuevamente usando digitos")
          system("cls")
          rutJefe=input(f'Usted va a agregar el producto {nombProd}\
                        \nIngrese su Rut para confirmar (sin puntos y con guion)\n=> ')
          system("cls")
          sq2=f'select * from jefeDeVentas where rutJefe={repr(rutJefe)}'
          try:
              db.cursor.execute(sq2)
              rutCon=db.cursor.fetchone()
          except Exception as err:
              pass
          if rutCon!=None:
              sq3=f'insert into producto values({repr(idprod)},{repr(nombProd)},{repr(valorProd)},{repr(rutJefe)})'
              try:
                db.cursor.execute(sq3)
                db.conexion.commit()
              except Exception as err:
                db.conexion.rollback()
                print(err)
              print('Producto agregado')
          else:
            print('Rut Invalido')
        else:
          print('Producto ya existente')
      except Exception as err:
        print(err)
    #modificar productos
    elif opProd==3:
      try:
        idprod=int(input('Ingrese Codigo del producto(numerico): '))
        system("cls")
        sq1=f'select * from producto where codProd={repr(idprod)}'
        db.cursor.execute(sq1)
        prodMod=db.cursor.fetchone()
        if prodMod[0]!=None:
          nomMod=input(f'Ingrese nuevo nombre: {prodMod[1]} => ')
          system("cls")
          valorModProd=int(input(f'Ingrese nuevo valor: {prodMod[2]}=> '))
          while valorModProd<=0:
            system("cls")
            valorModProd=int(input(f'Error. Ingrese nuevo valor(Mayor a cero): {prodMod[2]}=> '))
          system("cls")
          rutJefe=input(f'Usted va a modificar el producto: \n{prodMod[1]}-{prodMod[2]}=>{nomMod}-{valorModProd}\
                        \nIngrese su Rut para confirmar (sin puntos y con guion)\n=> ')
          #verificar el rut del que ingresa
          ########
          try:
            sql2=f'select rutJefe from jefeDeVentas where rutJefe={repr(rutJefe)}'
            db.cursor.execute(sql2)
            if db.cursor.fetchone()!=None:
              sq3=f'update producto set nombreProd={repr(nomMod)}, valorUnit={repr(valorModProd)}, rutJefe={repr(rutJefe)} where codProd={repr(idprod)}'
              db.cursor.execute(sq3)
              db.conexion.commit()
            else:
              print("El rut ingresado no cuenta con las credenciales para modificar")
          except Exception as err:
            db.conexion.rollback()
            print("El rut ingresado no cuenta con las credenciales para modificar")
          system("cls")
          print('El producto se ha modificado de manera exitosa')
        else:
          print('Producto no encontrado')
      except Exception as err:
        print("El producto no ha podido ingresarse, intentelo nuevamente")
      
    elif opProd==4:
      try:
        idprod=int(input('Ingrese Codigo del producto: '))
        sq1=f'select * from producto where codProd={repr(idprod)}'
        db.cursor.execute(sq1)
        prodMod=db.cursor.fetchone()
        if prodMod[0]!=None:
          respDel=input(f'Usted va a eliminar el producto "{prodMod[1]}"\
                        \n¿Desea eliminarlo?(s/n)=> ')
          while respDel.lower()!='s' and respDel.lower()!='n':
            respDel=input(f'Error, Opcion invalida\n\
                          \nUsted va a eliminar el producto "{prodMod[1]}"\
                        \n¿Desea eliminarlo?(s/n)=> ')
          sq2=f'delete from producto where codProd={repr(idprod)}'
          try:
            db.cursor.execute(sq2)
            db.conexion.commit()
          except Exception as err:
            db.conexion.rollback()
            pass
          system("cls")
          print('\nProducto eliminado\n')
      except Exception as err:
        print(err)

    elif opProd==5:
      print('\nAbandonando Menu de productos\n')
      break

    else:
      print('\nOpcion no valida')
    
    input('\nPresione ENTER para continuar...')

def addUser(user,db):
  while True:
    while True:
      system("cls")
      print('+'*4,'Gestor de Usuarios','+'*4)
      try:
        resp=int(input('1. Ver Lista de Usuario\
                      \n2. Agregar Usuario\
                      \n3. Modificar Usuario\
                      \n4. salir\
                      \n=> '))
        break
      except Exception:
        print('Ingrese una de las opciones validas')
        pass
    #Ver lista de Usuarios Vendedores
    if resp==1:
      system("cls")
      sq1='select rutVendedor,userName,nombre,apellidoPat,fono from vendedor'
      try:
          db.cursor.execute(sq1)
          verUs=db.cursor.fetchall()
          print(tab.tabulate(verUs,headers=['Rut Vend.','Nombre de Us.','Nombre Vendedor','Apellido Vendedor','Fono vendedor'],tablefmt="psql"))
      except Exception:
          pass
    #Agregar Usuarios Vendedores
    elif resp==2:
      system("cls")
      rutUs=input('Ingrese Rut de nuevo usuario(sin puntos y con guion)\n=> ')
      sq1=f'Select rutVendedor from Vendedor where rutVendedor={repr(rutUs)}'
      try:
        db.cursor.execute(sq1)
        if db.cursor.fetchone()==None:
          system("cls")
          nomUsVend=input('Ingrese el nombre de usuario del vendedor: ')
          system("cls")
          passwordVend=input('Ingrese la contrasenha del usuario: ')
          system("cls")
          nomVend=input('Ingrese nombre del Vendedor: ')
          system("cls")
          apVend=input('Ingrese el primer apellido del vendedor: ')
          while True:
            try:
              system("cls")
              fonoVend=int(input('Ingrese numero del vendedor: '))
              while fonoVend<=0 or len(fonoVend)!=9:
                system("cls")
                fonoVend=int(input('Error, Ingrese numero del vendedor(9 digitos): '))
              break
            except ValueError:
              system("cls")
              print("Intente con un numero de 9 digitos")
              input("Presione Enter para continuar... ")
          system("cls")
          sq2=f'insert into vendedor values({repr(rutUs)},{repr(nomUsVend)},{repr(passwordVend)},{repr(nomVend)},{repr(apVend)},{repr(fonoVend)})'
          try:
            db.cursor.execute(sq2)
            print("insert de vendedor exitoso")
            db.conexion.commit()
          except Exception:
            db.conexion.rollback()
            system("cls")
            print("Los datos de usuario no se han ingresado correctamente ")
          print('Nuevo Usuario creado exitosamente')
        else:
          print('Vendedor ya existe')    
      except Exception:
        pass
    #Modificar Usuarios Vendedores
    elif resp==3:
      system("cls")
      rutUs=input('Ingrese Rut del usuario a modificar(sin puntos y con guion)\n=> ')
      sq1=f'Select * from Vendedor where rutVendedor={repr(rutUs)}'
      try:
        db.cursor.execute(sq1)
        VendMod=db.cursor.fetchone()
        if VendMod!=None:
          while True:
            system("cls")
            print(f'Rut del Usuario a modificar => {rutUs}')
            print('\nEscoja una opcion')
            resp=int(input('1. cambiar Usuario\
                          \n2. cambiar contrasenha\
                          \n3. cambiar Nombre\
                          \n4. cambiar Apellido\
                          \n5. cambiar fono\
                          \n6. salir\
                          \n=> '))
            #Cambiar nombre de usuario
            if resp==1:
              system("cls")
              newUs=input(f'Ingrese nuevo nombre de usuario: {VendMod[1]} => ')
              resp1=input(f'¿Esta seguro de cambiar el nombre de ususario?(s/n)\
                          \n\n{VendMod[1]} => {newUs}')
              while resp1.lower()!='s' and resp1!='n':
                system("cls")
                resp1=input(f'¿Esta seguro de cambiar el nombre de ususario?(s/n)\
                          \n\n{VendMod[1]} => {newUs}')
              if resp1.lower()=='s':
                modUs=f'update vendedor set userName={repr(newUs)} where rutVendedor={repr(rutUs)}'
                try:
                  db.cursor.execute(modUs)
                  db.conexion.commit()
                except Exception:
                  db.conexion.rollback()
                  system("cls")
                  print('Error al Modificar usuario')
                  pass
                system("cls")
                print('Usuario modificado con exito')
              else:
                system("cls")
                print('Usuario no modificado')
            #Cambiar contraseña
            elif resp==2:
              system("cls")
              newPass=pwinput(f'Ingrese nueva Contraseña: ')
              resp1=input('¿Esta seguro de cambiar la contrasenha?(s/n) ')
              while resp1.lower()!='s' and resp1!='n':
                system("cls")
                resp1=input('¿Esta seguro de cambiar la contrasenha?(s/n) ')
              if resp1.lower()=='s':
                modPass=f'update vendedor set password1={repr(newPass)} where rutVendedor={repr(rutUs)}'
                try:
                  db.cursor.execute(modPass)
                  db.conexion.commit()
                except Exception:
                  db.conexion.rollback()
                  print('Error al Modificar contrasenha')
                  pass
                system("cls")
                print('Contrasenha modificada con exito')
              else:
                system("cls")
                print('Contrasenha no modificada')              
            elif resp==3:
              system("cls")
              newNom=input(f'Ingrese nuevo nombre de usuario: {VendMod[3]} => ')
              resp1=input(f'¿Esta seguro de cambiar el nombre de vendedor?(s/n)\
                          \n\n{VendMod[3]} => {newNom}')
              while resp1.lower()!='s' and resp1!='n':
                system("cls")
                resp1=input(f'¿Esta seguro de cambiar el nombre de vendedor?(s/n)\
                          \n\n{VendMod[3]} => {newNom}')
              if resp1.lower()=='s':
                modNom=f'update vendedor set nombre={repr(newNom)} where rutVendedor={repr(rutUs)}'
                try:
                  db.cursor.execute(modNom)
                  db.conexion.commit()
                except Exception:
                  db.conexion.rollback()
                  print('Error al Modificar el nombre del vendedor')
                  pass
                system("cls")
                print('Nombre del vendedor modificado con exito')
              else:
                system("cls")
                print('Nombre de vendedor no modificado')
            elif resp==4:
              system("cls")
              newApe=input(f'Ingrese nuevo Apellido del Vendedor: {VendMod[4]} => ')
              resp1=input(f'¿Esta seguro de cambiar el Apellido del Vendedor?(s/n)\
                          \n\n{VendMod[4]} => {newApe}')
              while resp1.lower()!='s' and resp1!='n':
                system("cls")
                resp1=input(f'¿Esta seguro de cambiar el Apellido del Vendedor?(s/n)\
                          \n\n{VendMod[4]} => {newApe}')
              if resp1.lower()=='s':
                modAp=f'update vendedor set apellidoPat={repr(newApe)} where rutVendedor={repr(rutUs)}'
                try:
                  db.cursor.execute(modAp)
                  db.conexion.commit()
                except Exception:
                  db.conexion.rollback()
                  print('Error al Modificar el Apellido del Vendedor')
                  pass
                print('Apellido del Vendedor modificado con exito')
              else:
                print('Apellido del Vendedor no modificado')
            elif resp==5:
              system("cls")
              newFono=input(f'Ingrese nuevo Fono: {VendMod[5]} => ')
              resp1=input(f'¿Esta seguro de cambiar el Fono?(s/n)\
                          \n\n{VendMod[5]} => {newFono}')
              while resp1.lower()!='s' and resp1.lower()!='n':
                system("cls")
                resp1=input(f'¿Esta seguro de cambiar el Fono?(s/n)\
                          \n\n{VendMod[5]} => {newFono}\n => ')
              if resp1.lower()=='s':
                modFono=f'update vendedor set fono={repr(newFono)} where rutVendedor={repr(rutUs)}'
                try:
                  db.cursor.execute(modFono)
                  db.conexion.commit()
                except Exception:
                  db.conexion.rollback()
                  print('Error al Modificar el Fono')
                  pass
                system("cls")
                print('Fono modificado con exito')
              else:
                system("cls")
                print('Fono no modificado')
            elif resp==6:
              system("cls")
              print('\nVolviendo a Gestor de Usuarios\n')
              break
            else:
              system("cls")
              print('\nOpcion Invalida\n')
            input('\nPresione ENTER para continuar...')
        else:
          print("EL rut ingresado no concuerda con ninguno resgistrado. ")
      except Exception:
        print("Ha ocurrido un error, intentelo nuevamente")
    elif resp==4:
      system("cls")
      print('\nAbandonando Gestor de Usuarios\n')
      break
    else:
      system("cls")
      print('\nOpcion Invalida...\n')
      
    input('\nPresione ENTER para continuar...')

###Seller menu functions###
#Buscar producto
def searchProd(db):  
  codigoProd=0
  #Consulta codigo de producto a buscar
  while True:
    try:
      system("cls")
      codigoProd=int(input("Ingrese codigo producto: "))
      system("cls")
      break
    except ValueError:
      system("cls")
      print("Error, el codigo de producto debe ser numerico (8 digitos)")
      input("Presione enter para continuar... ")
      system("cls")
  #comando Consulta Sql
  sq1=f'select codProd,nombreProd,valorUnit from producto where codprod={codigoProd}'
  #execucion consulta
  try:
    db.cursor.execute(sq1)
    result=db.cursor.fetchall()
  except Exception as err:
    db.conexion.rollback()
    print(err)
  #retorno
  # print(result)
  # print(type(result))
  # # print(result[0])
  # print(type(result[0]))
  # print(type(None))
  if len(result)>=1:
    print("Producto Encontrado")
    print(tab.tabulate(result,headers=["Codigo Producto","Nombre del Producto","Valor del unitario del Producto"],tablefmt="psql"))
    return(result)
  else:
    print("No se ha encontrado el producto")
    return(None)

#Agregar producto
def addProduct(producto,productList): 
  #revisa si se ha buscado un producto
  if(producto==None or len(producto)<1):
    print("Debe haber buscado un producto valido")
    return productList
  #si hay un producto
  else:
    #transformar el producto de ty
    productoprime=list(producto[0])
    #preguntar por cantidad a agregar
    while True:
      try:
        system("cls")
        #presentar datos del producto
        print(tab.tabulate(producto,headers=['Codigo Prod.','Nombre Prod.','Valor Prod.'],tablefmt="psql"))
        cantidad=int(input("Ingrese cantidad a agregar del producto: "))
        while cantidad<1:
          system("cls")
          #presentar datos del producto
          print(productoprime) #TODO formatear el producto
          cantidad=int(input("Ingrese cantidad a agregar del producto(Mayor a 0): "))
        break
      except ValueError:
        print("Error, la cantidad de producto debe ser numerico")
        input("Presione enter para continuar... ")
    #añadirlo a la lista
    productoprime.append(cantidad)
    productoprime.append(cantidad*productoprime[2])
    productList.append(productoprime)
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
    print(tab.tabulate(productList,headers=["Cod prod","Nombre prod","Valor unitario","Cantidad","Valor Total"],tablefmt="psql"))  #TODO formatear lista de productos
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
        system("cls")
      if eleccion=="si":
        del productList[i]
        print("Producto eliminado")
        # print(productList)  #? conservar?
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
  confirm=""
  numBoleta=1
  numFactura=1
  numVenta=1
  numDetalle=1
  formatDoc=[]
  if(len(productList)<1):
    print("Debe haber agregado por lo menos un producto a la lista de compra ")
    return(False)
  #ciclo para preguntar por modificaciones
  while True:
    #elegir documento
    system("cls")
    #mostrar la lista con el total
    print(tab.tabulate(productList,headers=['Codigo Produc.','Nombre Produc.','Valor unitario','Cantidad','Valor Total'],tablefmt='psql'))
    tipoDoc=input("Desea boleta o factura (b/f): ")
    while tipoDoc!="b" and tipoDoc!="f":
      system("cls")
      #mostrar la lista con el total
      print(tab.tabulate(productList,headers=['Codigo Produc.','Nombre Produc.','Valor unitario','Cantidad','Valor Total'],tablefmt='psql'))
      tipoDoc=input("Desea boleta o factura (b/f): ")
    #preguntar por confirmacion
    system("cls")
    #mostrar la lista con el total y eleccion de documento
    print(productList)
    print(tipoDoc)
    confirm=input("Está correcto? (si/no): ")
    system("cls")
    while confirm!="si" and confirm!="no":
      system("cls")
      #mostrar la lista con el total
      print(productList)
      confirm=input("Está correcto? (si/no): ")
      system("cls")
    if confirm=="no":
      print("Volviendo al menu de vendedor")
      return False
    if tipoDoc=="b":
      #boleta######################################
        formatDoc.append("Boleta")
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
        formatDoc.append(f'N°: {numBoleta}')
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
        formatDoc.append(totalNeto)
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
      #factura#########################################
        formatDoc.append("Factura")
        #preguntar datos
        razsoccli=input("Ingrese razón social cliente: ")
        rutcli=input("Ingrese rut cliente: ")
        giro=input("Ingrese giro cliente: ")
        direccion=input("Ingrese direccion: ")
        formatDoc.append([razsoccli,rutcli,giro,direccion])
        #generar factura
        #subir a base de datos
        ###################################
        #factura
        #buscar numero de factura
        sq1=(f'select cantFacturas from bazar where idbazar="1234"')
        #execucion consulta
        try:
          db.cursor.execute(sq1)
          num=db.cursor.fetchone()
          numFactura=numFactura+num[0]
          print("cantidad facturas:",numFactura)
        except Exception as err:
          db.conexion.rollback()
          print(err)
        formatDoc.append(f'N°: {numFactura}')
        #actualizar cantidad de facturas
        sq2=(f'update bazar set cantFacturas=cantFacturas+1')
        #execucion update
        try:
          db.cursor.execute(sq2)
          db.conexion.commit()      
          print("cantidad de facturas actualizado")
        except Exception as err:
          db.conexion.rollback()
          print(err)
        #generar boleta
        totalNeto=total
        formatDoc.append(totalNeto)
        #subir a bdd
        sq3=(f'insert into factura values({numFactura},{repr(razsoccli)},{repr(rutcli)},{repr(giro)},{repr(direccion)},{totalNeto})')
        #execucion insert
        try:
          db.cursor.execute(sq3)
          db.conexion.commit()
          print("Boleta guardada")
        except Exception as err:
          db.conexion.rollback()
          print(err)
        pass
    ##########################################
    #registrar venta en bdd
    #obtener numero de venta
    sq6=(f'select cantVentas from bazar')
    try:
      db.cursor.execute(sq6)
      elem=db.cursor.fetchone()
      codventa=elem[0]+numVenta
      db.conexion.commit()
    except Exception as err:
      db.conexion.rollback()
      print(err)
    formatDoc.append(codventa)
    #modificar el numero de venta de bazar
    sq7=(f'update bazar set cantVentas={codventa}')
    #execucion update
    try:
      db.cursor.execute(sq7)
      db.conexion.commit()      
      print("cantidad de ventas actualizado")
    except Exception as err:
      db.conexion.rollback()
      print(err)
    today=date.today()
    tipoDoc=tipoDoc
    if(tipoDoc=="b"):
      numBoleta
      numFactura=0
    else:
      numBoleta=0
      numFactura
    #obtener rut vendedor
    sq4=(f'select rutvendedor from vendedor where username={repr(user)}')
    try:
      db.cursor.execute(sq4)
      elem=db.cursor.fetchone()
      rutVendedor=elem[0]
      print(rutVendedor)
      db.conexion.commit()
    except Exception as err:
      db.conexion.rollback()
      print(err)
    #execucion insert
    formatofecha=str(today.year)+"-"+str(today.month)+"-"+str(today.day)
    formatDoc.append(formatofecha)
    sq5=(f'insert into registrodeventa values({codventa},{repr(formatofecha)},{repr(tipoDoc)},{numFactura},{numBoleta},{repr(rutVendedor)})')
    try:
      db.cursor.execute(sq5)
      db.conexion.commit()
      print("venta registrada")
    except Exception as err:
      db.conexion.rollback()
      print(err)
    #registrar detalle
    for i in range(len(productList)):
      #obtener numero de detalle
      sq8=(f'select cantDetalles from bazar')
      try:
        db.cursor.execute(sq8)
        elem=db.cursor.fetchone()
        numDetalle=elem[0]+numDetalle
        db.conexion.commit()
      except Exception as err:
        db.conexion.rollback()
        print(err)
      #aumentar el numero de detalle
      sq9=(f'update bazar set cantDetalles=cantDetalles+1')
      #execucion update
      try:
        db.cursor.execute(sq9)
        db.conexion.commit()      
        print("cantidad de detalles actualizado")
      except Exception as err:
        db.conexion.rollback()
        print(err)
      
      #execucion insert
      sq10=(f'insert into detalle values({numDetalle},{repr(tipoDoc)},{productList[i][3]},{numBoleta},{numFactura},{productList[i][0]})')
      try:
        db.cursor.execute(sq10)
        db.conexion.commit()
        print("venta detalle registrado")
      except Exception as err:
        db.conexion.rollback()
        print(err)
      formatDoc.append([productList[i][1],productList[i][2],productList[i][3],productList[i][4]])
    #####imprimir boleta o factura#########
    printDoc(formatDoc,tipoDoc)
    return True