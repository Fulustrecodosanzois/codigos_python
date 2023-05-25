class Funcionario:
    def __init__(self, cargo, nome):
        self._cargo= cargo #atributo protegido(as filhas tem acesso)
        self._nome= nome
        
    def informacoes(self):
        print(f"Olá {self._nome} seu cargo é {self._cargo}\n")
        
class Gerente(Funcionario):
    def __init__(self, cargo, nome, salario): #se constroi um contrutor pois foi necessário criar atributos especificos para a classe gerente
        super().__init__( cargo, nome) # repeti-se o init da classe mãe para que a filha tenha acesso, não precisando assim repetir os atributos
        self._salario= salario #Porém a novo atributo deve ser adicionado
    def exibir(self):
        print(f"Seu nome é {self._nome} seu salário é {self._salario} ")    
