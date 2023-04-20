class Produto:
    def __init__(self, codigo, nome, preco, qtdEstoque):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco
        self.qtdEstoque = qtdEstoque

    def __str__(self):
        return f"{self.codigo}, {self.nome}, {self.preco}, {self.qtdEstoque}"


    # with open("produtos/produtos.csv", "r") as file:
    #     reader = csv.reader(file)
    #     for row in reader:
    #         print(row)

        
