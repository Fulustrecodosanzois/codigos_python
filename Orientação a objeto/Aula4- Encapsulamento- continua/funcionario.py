# emcapsulamento é a restinção de acesso

class Funcionario:
    def __init__(self, nome, cargo): #inicializa as variavéis 
        self.__nome= nome 
        self.__cargo = cargo
        
    def get_nome(self): #o get nunca precisa de variável, pois apenas exibe o retorno 
        return self.__nome
    
    def set_nome(self, texto):
        self.__nome= texto
    
    # CRIANDO O GET DO CARGO

    @property # Esse elemnto irá criar um get mais amigável (usado somente para get)
    def cargo(self):
        return self.__cargo
    
    @cargo.setter #irá criar um set para cargo mais amigável
    def cargo(self, info):
        self.__cargo = info
    
    