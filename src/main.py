import csv  
from objs.Produto import Produto
from objs.Estoque import Estoque

listaProdutos = []

estoque = Estoque()

obj = Produto("ASD", "ASD", "ASD", "ASD")



with open("produtos/produtos.csv", "r") as file:
            
    reader = csv.reader(file)
    for row in reader:
        estoque.add_produto(Produto(row[0], row[1], row[2], row[3]))
        

produto = Produto("FGH345", "Celular Samsung Podrao", "1400.00", "5")

estoque.add_produto(produto)

estoque.ordena_por_nome(False)
estoque.ordena_por_codigo(True)
estoque.ordena_por_qtd(False)
estoque.ordena_por_preco(True)



