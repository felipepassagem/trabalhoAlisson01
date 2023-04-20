
def getKey(self,key):
    return key[0]

class Estoque:
    def __init__(self, listaProdutos, qtdProdutos, qtdProdutosUnique):
        self.listaProdutos = []
        self.qtdProdutos = qtdProdutos
        qtdProdutosUnique = qtdProdutosUnique

    def getKey(self,key):
         return key[0]
    
    def ordena_estoque(self):
        sorted(self.listaProdutos, key=getKey)
    # with open("produtos/produtos.csv", "r") as file:
            
            # reader = csv.reader(file)
            # for row in reader:
            #     listaProdutos.append(row)
            
        # listaProdutosOrdenada = sorted(self.listaProdutos, key=getKey)
        