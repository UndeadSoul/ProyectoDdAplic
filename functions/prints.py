import tabulate as tab

def printPrLs(productList,lastSearch,productTotal):
    #TODO formatear las impresiones con tabulate
    #print("lastSearch",lastSearch) #una lista producto
    #print("productList",productList) #una lista de llistas producto con cantidad - total
    print(tab.tabulate(productList,headers=['Cod. Producto','Nombre Producto','Valor Producto','Cantidad','Valor total'],tablefmt="psql"))
    print("Total:",productTotal) #int
    print(tab.tabulate(lastSearch,headers=['Cod. Buscado','Nombre Buscado','Valor Buscado'],tablefmt="psql"))
    #TODO imprimir el total