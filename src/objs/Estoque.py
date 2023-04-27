

import statistics
from objs.Produto import Produto

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

        
        
        if self.ordenado_por == atributo:
            if self.ordenadaCodigoDesc:
                #########################
                if atributo == "codigo":
                    left = 0
                    right = tamanholista - 1

                    while left <= right:
                        mid = (left + right) // 2
                    
                        if self.__listaProdutos[mid].codigo == pesquisa:
                            return(self.__listaProdutos[mid])
                            
                        elif self.__listaProdutos[mid].codigo < pesquisa:
                            right = mid - 1
                        else:
                            left = mid + 1

                ################################

            if self.ordenadaNomeAsc:
                if atributo == "nome":
                    left = 0
                    right = tamanholista - 1

                    while left <= right:
                        mid = (left + right) // 2
                    
                        if self.__listaProdutos[mid].nome == pesquisa:
                            return(self.__listaProdutos[mid])
                            
                        elif self.__listaProdutos[mid].nome < pesquisa:
                            right = mid - 1
                        else:
                            left = mid + 1
        
            if self.ordenadaNomeDesc:
                if atributo == "nome":
                    left = 0
                    right = tamanholista - 1

                    while left <= right:
                        mid = (left + right) // 2
                        #print(pesquisa > self.__listaProdutos[mid].nome )
                        if self.__listaProdutos[mid].nome == pesquisa:
                            return(self.__listaProdutos[mid])
                            break
                        elif self.__listaProdutos[mid].nome < pesquisa:
                            left = mid + 1
                        else:
                            right = mid - 1

            if self.ordenadaCodigoAsc:
                if atributo == "codigo":
                    left = 0
                    right = tamanholista - 1

                    while left <= right:
                        mid = (left + right) // 2
                        #print(pesquisa > self.__listaProdutos[mid].codigo )
                        if self.__listaProdutos[mid].codigo == pesquisa:
                            return(self.__listaProdutos[mid])
                            
                        elif self.__listaProdutos[mid].codigo < pesquisa:
                            left = mid + 1
                        else:
                            right = mid - 1

        else:
            if atributo == "nome":
                for i in range(tamanholista):
                    if self.__listaProdutos[i].nome == pesquisa:
                        return(self.__listaProdutos[i])
                        
            elif atributo == "codigo":
                for i in range(tamanholista):
                    if self.__listaProdutos[i].codigo == pesquisa:
                        return(self.__listaProdutos[i]) 
                    
            
        

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

    def print_listaProdutos(self):
        for item in self.__listaProdutos:
            print(str(item))

    def get_estoque(self):
        return self.__listaProdutos

    def removerRegistro(self, codigo):
        tamanholista = len(self.__listaProdutos)
        if self.ordenado_por == "codigo":
            
            if self.ordenadaCodigoDesc:
                
                left = 0
                right = tamanholista - 1

                while left <= right:
                    mid = (left + right) // 2
                    
                    if self.__listaProdutos[mid].codigo == codigo:
                        # print(self.__listaProdutos[mid])
                        temp = self.__listaProdutos[mid]
                        self.__listaProdutos.pop(mid)
                        return(temp)
                    elif self.__listaProdutos[mid].codigo < codigo:
                        right = mid - 1
                    else:
                        left = mid + 1
            
            if self.ordenadaCodigoAsc:
                
                left = 0
                right = tamanholista - 1

                while left <= right:
                    mid = (left + right) // 2
                    
                    if self.__listaProdutos[mid].codigo == codigo:
                        # print(self.__listaProdutos[mid])
                        temp = self.__listaProdutos[mid]
                        self.__listaProdutos.pop(mid)
                        return(temp)
                    elif self.__listaProdutos[mid].codigo < codigo:
                        left = mid + 1
                    else:
                        right = mid - 1

        if self.ordenado_por == "nome":
            if self.ordenadaNomeDesc:
                
                left = 0
                right = tamanholista - 1

                while left <= right:
                    mid = (left + right) // 2
                    
                    if self.__listaProdutos[mid].nome == codigo:
                        
                        temp = self.__listaProdutos[mid]
                        self.__listaProdutos.pop(mid)
                        return(temp)
                    elif self.__listaProdutos[mid].nome < codigo:
                        left = mid + 1
                    else:
                        right = mid - 1

            if self.ordenadaNomeAsc:
                
                left = 0
                right = tamanholista - 1

                while left <= right:
                    mid = (left + right) // 2
                    
                    if self.__listaProdutos[mid].nome == codigo:
                        
                        temp = self.__listaProdutos[mid]
                        self.__listaProdutos.pop(mid)
                        return(temp)
                        
                    elif self.__listaProdutos[mid].nome < codigo:
                        right = mid - 1
                    else:
                        left = mid + 1

        if self.ordenado_por == "":
            for i in range(tamanholista):
                if codigo == self.__listaProdutos[i].codigo or codigo == self.__listaProdutos[i].nome:
                    self.__listaProdutos.pop(i)
                    return i
            print("Produto não encontrado.")

    def atualizar(self, codigo, campoBusca, campo, novoValor):
        x = self.pesquisa(codigo, campoBusca)
        
        
        if x != None:
            if campo == "nome":
                x.setNome(novoValor)
            
                return x
            if campo == "codigo":
                x.setCodigo(novoValor)
                
                return x
            if campo == "preco":
                x.setPreco(novoValor)
            
                return x
            if campo == "qtdEstoque":
                x.setQtdEstoque(novoValor)
                
                return x
        else:
            print("Produto não encontrado")
            

                        
        
    

    # with open("produtos/produtos.csv", "r") as file:
            
            # reader = csv.reader(file)
            # for row in reader:
            #     listaProdutos.append(row)
            
        # listaProdutosOrdenada = sorted(self.listaProdutos, key=getKey)
        