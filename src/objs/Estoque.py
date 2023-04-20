


class Estoque:
    
    def __init__(self):
        self.ordenado_por = ""
        self.__listaProdutos = []
        self.qtdProdutos = 0
        self.qtdProdutosUnicos = 0

    def get_codigo(self, produto):
        return produto.codigo
    
    def get_nome(self, produto):
        return produto.nome
    
    def get_qtd(self, produto):
        return int(produto.qtdEstoque)
        
    def get_preco(self, produto):
        return float(produto.preco)
    
    def ordena_por_codigo(self, asc):
        estoque_ordenado = sorted(self.__listaProdutos, key=self.get_codigo, reverse=asc)     
        self.__listaProdutos = estoque_ordenado[:]
        self.ordenado_por = "codigo"
        self.__print_listaProdutos()
    
    def ordena_por_nome(self, asc):
        estoque_ordenado = sorted(self.__listaProdutos, key=self.get_nome, reverse=asc)
        self.__listaProdutos = estoque_ordenado[:]
        self.ordenado_por = "nome"
        self.__print_listaProdutos()

    def ordena_por_qtd(self, asc):
        estoque_ordenado = sorted(self.__listaProdutos, key=self.get_qtd, reverse=asc)
        self.__listaProdutos = estoque_ordenado[:]
        self.ordenado_por = "qtd"
        self.__print_listaProdutos()

    def ordena_por_preco(self, asc):
        estoque_ordenado = sorted(self.__listaProdutos, key=self.get_preco, reverse=asc)
        self.__listaProdutos = estoque_ordenado[:]
        self.ordenado_por = "preco"
        self.__print_listaProdutos()

    def add_produto(self, produto):
        self.__listaProdutos.append(produto)
        if self.ordenado_por == "":
            return
        elif self.ordenado_por == "nome":
            self.ordena_por_nome()
            return
        elif self.ordenado_por == "codigo":
            self.ordena_por_codigo()
            return
        elif self.ordenado_por == "qtd":
            self.ordena_por_codigo()
            return
        elif self.ordenado_por == "preco":
            self.ordena_por_codigo()
            return
    
    def __print_listaProdutos(self):
        for item in self.__listaProdutos:
            print(str(item))

    def get_estoque(self):
        return self.__listaProdutos

    

    # with open("produtos/produtos.csv", "r") as file:
            
            # reader = csv.reader(file)
            # for row in reader:
            #     listaProdutos.append(row)
            
        # listaProdutosOrdenada = sorted(self.listaProdutos, key=getKey)
        