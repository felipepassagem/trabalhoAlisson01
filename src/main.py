import csv  
# import objs.Produto as Produto
from objs.Produto import Produto

listaProdutos = []

with open("produtos/produtos.csv", "r") as file:
            
    reader = csv.reader(file)
    for row in reader:
        listaProdutos.append(Produto(row[0], row[1], row[2], row[3]))
    
    print(listaProdutos)






