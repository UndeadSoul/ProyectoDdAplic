import tabulate as tab
from os import system

def printPrLs(productList,lastSearch,productTotal):
    #TODO formatear las impresiones con tabulate
    #print("lastSearch",lastSearch) #una lista producto
    #print("productList",productList) #una lista de llistas producto con cantidad - total
    print(tab.tabulate(productList,headers=['Cod. Producto','Nombre Producto','Valor Producto','Cantidad','Valor total'],tablefmt="psql"))
    print("Total:",productTotal) #int
    print(tab.tabulate(lastSearch,headers=['Cod. Buscado','Nombre Buscado','Valor Buscado'],tablefmt="psql"))
    #TODO imprimir el total

def printDoc(formatDoc,tipoDoc):
    if(tipoDoc=="b"):
        # print(formatDoc)
        system("cls")
        #      ++++++++++++++++++ Boleta ++++++++++++++++++
        print('+'*18,f'{formatDoc[0]}','+'*18)
        #        Boleta N°: 0
        print(f'  Boleta {formatDoc[1]}')
        #        Fecha: 2024-12-31 
        print(f'  Fecha: {formatDoc[4]}')
        #        Venta N°: 1
        print(f'  Venta N°: {formatDoc[3]}')
        #        Detalle:
        print(f'  \n\n Detalle: \n')
        for i in range(5,len(formatDoc)):
        #           galleta     2990       5     14950
            print(f'\t{formatDoc[i][0]}\t{formatDoc[i][1]}\t{formatDoc[i][2]}\t{formatDoc[i][3]}')
        #        Total Neto:                    14950
        print(f'  Total Neto: \t\t\t\t\t{formatDoc[2]}')
        #      ++++++++++++++++++++++++++++++++++++++++++++
        print('+'*44)
    elif tipoDoc=="f":
        # print(formatDoc)
        system("cls")
        #      ++++++++++++++++++ Factura ++++++++++++++++++
        print('+'*18,f'{formatDoc[0]}','+'*18)
        #        Factura N°: 0
        print(f'  Factura {formatDoc[2]}')
        #        Fecha: 2024-12-31 
        print(f'  Fecha: {formatDoc[5]}')
        #        Venta N°: 1
        print(f'  Venta N°: {formatDoc[4]}')
        #        Datos Cliente:
        print(f' Datos Cliente:')
        #         Razón social cliente: lo que sea
        print(f'   Razón social: {formatDoc[1][0]}')
        #         Rut: 12345678-9
        print(f'   Rut: {formatDoc[1][1]}')
        #         Giro: girando
        print(f'   Giro: {formatDoc[1][2]}')
        #         Dirección: calle falsa #123
        print(f'   Dirección: {formatDoc[1][3]}')
        #        Detalle:
        print(f'  \n\n Detalle: \n')
        #         
        for i in range(6,len(formatDoc)):
        #           galleta     2990       5     14950
            print(f'\t{formatDoc[i][0]}\t{formatDoc[i][1]}\t\t{formatDoc[i][2]}\t{formatDoc[i][3]}')
        #        Total Bruto:                    14950
        print(f'  Total Bruto: \t\t\t\t{round(formatDoc[3]-(formatDoc[3]*0.19),0)}')
        #        IVA:                           14950
        print(f'  IVA:  \t\t\t\t{round((formatDoc[3]*0.19),0)}')        
        #        Total Neto:                    14950
        print(f'  Total Neto:  \t\t\t\t{formatDoc[3]}')
        #      +++++++++++++++++++++++++++++++++++++++++++++
        print('+'*45)

