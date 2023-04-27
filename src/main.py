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
        

produto = Produto("FGH345", "Celular", "1400.00", "5")

#adiciona no estoque
estoque.add_produto(produto)

#Ordena o estoque por nome ou código -- True/False controlam se será ordem ascendente ou descendente
print("Estoque ordenado por codigo ascendente\n")
estoque.ordena_por_codigo(False)
print("\n")
#estoque.print_listaProdutos()
print("Estoque ordenado nome descendente\n")
estoque.ordena_por_nome(True)
print("\n")

#Remove do estoque
print("Estoque cheio: \n")
estoque.print_listaProdutos()
estoque.removerRegistro("Produtoteste")
print("\n")
print("Estoque após remover o produto: \n")
estoque.print_listaProdutos()

print("\nProduto que foi removido\n")
print(estoque.atualizar("Celular", "nome", "nome", "TESTE"))
#estoque.ordena_por_qtd(False)
#estoque.ordena_por_preco(True)
# estoque.get_qtd_produtos_total()
#estoque.get_qtd_produtos_unicos()
#estoque.pesquisa("Produto2", "nome")



