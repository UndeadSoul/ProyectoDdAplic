import mysql.connector

def dbDoesntExist(nombredb):
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="contramysql"
    )
    mycursor = mydb.cursor()
    mycursor.execute("SHOW DATABASES")
    listdb=mycursor.fetchall()
    noseencuentra=True
    for i in listdb:
        print(i[0])
        print(type(i[0]))
        if i[0]==nombredb:
            noseencuentra=False
    print(noseencuentra)
    if noseencuentra:
        return True
    else:
        print("siga intentando")

def createDb(nombredb):
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="contramysql"
    )
    sq1=f'Create Database {nombredb}'
    mycursor=mydb.cursor()
    mycursor.execute(sq1)
    print(mydb)

def createTables(db):
    #################################
    sq0='CREATE TABLE vendedor (\
        rutVendedor VARCHAR(15) NOT NULL PRIMARY KEY,\
        userName VARCHAR(20),\
        password1 VARCHAR(20),\
        nombre VARCHAR(20),\
        apellidoPat VARCHAR(20),\
        fono INT\
        )  engine=innodb;'
    try:
        db.cursor.execute(sq0)
        print("tabla creada con exito")
    except Exception as err:
        db.conexion.rollback()
        print(err)
        pass
    #################################
    sq1='CREATE TABLE factura (\
        numFactura INT NOT NULL PRIMARY KEY,\
        razSocCli VARCHAR(20),\
        rutCli VARCHAR(15),\
        giro VARCHAR(20),\
        direccion VARCHAR(20),\
        totalNeto INT\
        )engine=innodb;'
    try:
        db.cursor.execute(sq1)
        print("tabla creada con exito")
    except Exception as err:
        db.conexion.rollback()
        print(err)
        pass
    #################################
    sq2='CREATE TABLE boleta (\
        numBoleta INT NOT NULL PRIMARY KEY,\
        totalNeto INT\
        )engine=innodb;'
    try:
        db.cursor.execute(sq2)
        print("tabla creada con exito")
    except Exception as err:
        db.conexion.rollback()
        print(err)
        pass
    #################################
    sq3='CREATE TABLE registroDeVenta (\
        codVenta INT NOT NULL PRIMARY KEY,\
        fecha DATE,\
        tipoDoc VARCHAR(10),\
        numFactura INT NOT NULL,\
        numBoleta INT NOT NULL,\
        rutVendedor VARCHAR(15) NOT NULL,\
        FOREIGN KEY (numFactura) REFERENCES factura(numFactura),\
        FOREIGN KEY (numBoleta) REFERENCES boleta(numBoleta),\
        FOREIGN KEY (rutVendedor) REFERENCES vendedor(rutVendedor)\
        )engine=innodb;'
    try:
        db.cursor.execute(sq3)
        print("tabla creada con exito")
    except Exception as err:
        db.conexion.rollback()
        print(err)
        pass
    #################################
    sq4='CREATE TABLE jefeDeVentas (\
        rutJefe VARCHAR(15) NOT NULL PRIMARY KEY,\
        userName VARCHAR(20),\
        password1 VARCHAR(20),\
        nombre VARCHAR(20),\
        apellidoPat VARCHAR(20),\
        fono INT\
        )engine=innodb;'
    try:
        db.cursor.execute(sq4)
        print("tabla creada con exito")
    except Exception as err:
        db.conexion.rollback()
        print(err)
        pass
    #################################
    sq5='CREATE TABLE producto (\
        codProd INT NOT NULL PRIMARY KEY,\
        nombreProd VARCHAR(20),\
        valorUnit INT,\
        rutJefe VARCHAR(15) NOT NULL,\
        FOREIGN KEY (rutJefe) REFERENCES jefeDeVentas(rutJefe)\
        )engine=innodb;'
    try:
        db.cursor.execute(sq5)
        print("tabla creada con exito")
    except Exception as err:
        db.conexion.rollback()
        print(err)
        pass
    #################################
    sq6='CREATE TABLE detalle (\
        numDetalle INT NOT NULL PRIMARY KEY,\
        tipoDoc VARCHAR(10),\
        cantProd INT,\
        numBoleta INT NOT NULL,\
        numFactura INT NOT NULL,\
        codProd INT NOT NULL,\
        FOREIGN KEY (numBoleta) REFERENCES boleta(numBoleta),\
        FOREIGN KEY (numFactura) REFERENCES factura(numFactura),\
        FOREIGN KEY (codProd) REFERENCES producto(codProd)\
        )engine=innodb;'
    try:
        db.cursor.execute(sq6)
        print("tabla creada con exito")
    except Exception as err:
        db.conexion.rollback()
        print(err)
        pass
    #################################

    #################################
    sq8='CREATE TABLE bazar (\
        idBazar INT NOT NULL PRIMARY KEY,\
        estadoDia VARCHAR(12),\
        ultModificador VARCHAR(15) NOT NULL,\
        FOREIGN KEY (ultModificador) REFERENCES jefeDeVentas(rutJefe),\
        cantBoletas INT,\
        cantFacturas INT,\
        cantVentas INT,\
        cantDetalles INT\
        )engine=innodb;'
    try:
        db.cursor.execute(sq8)
        print("tabla creada con exito")
    except Exception as err:
        db.conexion.rollback()
        print(err)
        pass
    #################################

def defaultValues(db):
    sq0=f'insert into jefeDeVentas values("20324143-7","adminjdv","contramysql","Victor","Fierro",12345678);\
            insert into vendedor values("20324143-7","adminv","contramysql","Victor","Fierro",12345678);\
            insert into producto values(12345678,"galleta",2990,"20324143-7");\
            insert into bazar values(1234,"abierto","20324143-7",0,0,0,0);'
    try:
        db.cursor.execute(sq0)
        print("valores por defecto creados")
    except Exception as err:
        db.conexion.rollback()
        print(err)
    pass