

import statistics

class Estoque:
    
    def __init__(self):
        self.ordenado_por = ""
        self.__listaProdutos = []
        self.qtdProdutos = 0
        self.qtdProdutosUnicos = len(self.__listaProdutos)
        self.ordenadaNomeAsc = False
        self.ordenadaNomeDesc = False
        self.ordenadaCodigoAsc = False
        self.ordenadaCodigoDesc = False

    def get_codigo(self, produto):
        return produto.codigo
    
    def get_nome(self, produto):
        return produto.nome
    
    def get_qtd(self, produto):
        return int(produto.qtdEstoque)
        
    def get_preco(self, produto):
        return float(produto.preco)
    
    def __atualiza_qtd_produtos_unicos(self):
        self.qtdProdutosUnicos = len(self.__listaProdutos)
    
    def ordena_por_codigo(self, asc):
        estoque_ordenado = sorted(self.__listaProdutos, key=self.get_codigo, reverse=asc)     
        self.__listaProdutos = estoque_ordenado[:]
        self.ordenado_por = "codigo"
        if asc:
            self.ordenadaCodigoAsc = False
            self.ordenadaCodigoDesc = True
        if not asc:
            self.ordenadaCodigoAsc = True
            self.ordenadaCodigoDesc = False

        self.ordenadaNomeAsc = False
        self.ordenadaNomeDesc = False
        self.__print_listaProdutos()
    
    def ordena_por_nome(self, asc):
        estoque_ordenado = sorted(self.__listaProdutos, key=self.get_nome, reverse=asc)
        self.__listaProdutos = estoque_ordenado[:]
        self.ordenado_por = "nome"
        if asc:
            self.ordenadaNomeAsc = True
            self.ordenadaNomeDesc = False
        if not asc:
            self.ordenadaNomeAsc = False
            self.ordenadaNomeDesc = True

        self.ordenadaCodigoAsc = False
        self.ordenadaCodigoDesc = False
        self.__print_listaProdutos()

    def ordena_por_qtd(self, asc):
        estoque_ordenado = sorted(self.__listaProdutos, key=self.get_qtd, reverse=asc)
        self.__listaProdutos = estoque_ordenado[:]
        self.ordenado_por = "qtd"
        self.ordenadaNomeAsc = False
        self.ordenadaNomeDesc = False
        self.ordenadaCodigoAsc = False
        self.ordenadaCodigoDesc = False
        self.__print_listaProdutos()

    def ordena_por_preco(self, asc):
        estoque_ordenado = sorted(self.__listaProdutos, key=self.get_preco, reverse=asc)
        self.__listaProdutos = estoque_ordenado[:]
        self.ordenado_por = "preco"
        self.ordenadaNomeAsc = False
        self.ordenadaNomeDesc = False
        self.ordenadaCodigoAsc = False
        self.ordenadaCodigoDesc = False
        self.__print_listaProdutos()

    def get_qtd_produtos_total(self):
        # x = statistics.sum((float(o.qtdEstoque) for o in self.__listaProdutos))
        x = sum((float(o.qtdEstoque) for o in self.__listaProdutos))
        print(f"Quantidade total de produtos em estoque: {int(x)}")
        self.ordenadaNomeAsc = False
        self.ordenadaNomeDesc = False
        self.ordenadaCodigoAsc = False
        self.ordenadaCodigoDesc = False

    def get_qtd_produtos_unicos(self):
        print(self.qtdProdutosUnicos)
        # print(f"Qunatidade de produtos únicos em estoque: {len(self.__listaProdutos)}")
        
    def pesquisa(self, pesquisa, atributo):
        tamanholista = len(self.__listaProdutos)
        atributo = str(atributo)

        print(self.ordenado_por)
        
        if self.ordenado_por == atributo:
            if self.ordenadaCodigoDesc:
                if atributo == "codigo":
                    left = 0
                    right = tamanholista - 1

                    while left <= right:
                        mid = (left + right) // 2
                    
                        if self.__listaProdutos[mid].codigo == pesquisa:
                            print(self.__listaProdutos[mid])
                            break
                        elif self.__listaProdutos[mid].codigo < pesquisa:
                            right = mid - 1
                        else:
                            left = mid + 1

            if self.ordenadaNomeDesc:
                if atributo == "codigo":
                    left = 0
                    right = tamanholista - 1

                    while left <= right:
                        mid = (left + right) // 2
                    
                        if self.__listaProdutos[mid].codigo == pesquisa:
                            print(self.__listaProdutos[mid])
                            break
                        elif self.__listaProdutos[mid].codigo < pesquisa:
                            right = mid - 1
                        else:
                            left = mid + 1
        
            if self.ordenadaNomeAsc:
                if atributo == "codigo":
                    left = 0
                    right = tamanholista - 1

                    while left <= right:
                        mid = (left + right) // 2
                        print(pesquisa > self.__listaProdutos[mid].codigo )
                        if self.__listaProdutos[mid].codigo == pesquisa:
                            print(self.__listaProdutos[mid])
                            break
                        elif self.__listaProdutos[mid].codigo < pesquisa:
                            left = mid + 1
                        else:
                            right = mid - 1

            if self.ordenadaCodigoAsc:
                if atributo == "codigo":
                    left = 0
                    right = tamanholista - 1

                    while left <= right:
                        mid = (left + right) // 2
                        print(pesquisa > self.__listaProdutos[mid].codigo )
                        if self.__listaProdutos[mid].codigo == pesquisa:
                            print(self.__listaProdutos[mid])
                            break
                        elif self.__listaProdutos[mid].codigo < pesquisa:
                            left = mid + 1
                        else:
                            right = mid - 1

        else:
            if atributo == "nome":
                for i in range(tamanholista):
                    if self.__listaProdutos[i].nome == pesquisa:
                        print(self.__listaProdutos[i])
                        break
            elif atributo == "codigo":
                for i in range(tamanholista):
                    if self.__listaProdutos[i].codigo == pesquisa:
                        print(self.__listaProdutos[i]) 
                    break
            
        

    def add_produto(self, produto):
        self.__listaProdutos.append(produto)
        self.__atualiza_qtd_produtos_unicos()
        if self.ordenado_por == "":
            self.estaOrdenada = False
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
        