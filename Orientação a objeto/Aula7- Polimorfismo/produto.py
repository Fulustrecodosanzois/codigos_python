class Produto:
    def __init__(self, nome, preco):
        self._nome= nome
        self._preco= preco
        
    def descrever(self):
        print(f"O produto possui o preço R$ {self._preco}")
    
    def calcular_preco(self):
        pass
    

class Livro(Produto):
    def __init__(self, nome, preco, autor):
        super().__init__(nome, preco)
        self.__autor= autor
        
    def descrever(self):
        print(f"Livro: {self._nome} - Autor: {self.__autor}\n")
        
    def calcular_preco(self):
        print(F"O livro custa R$ {self._preco}")
        
        
class Eletronico(Produto):
    def __init__(self, nome, preco, marca):
        super().__init__(nome, preco)
        self.__marca= marca
    
    def calcular_preco(self):
        print("O eletrônico custa o valor de" ,self._preco*1.2, "da marca", self.__marca)