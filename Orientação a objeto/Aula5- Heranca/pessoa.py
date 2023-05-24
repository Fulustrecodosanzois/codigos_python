class Pessoa: # SuperClasse ou classe mãe
    def __init__(self, nome, idade):
        self._nome= nome
        self._idade= idade
        
    def relatorio(self):
        print("Sou uma pessoa.")
        print(f"Olá {self._nome}, sua idade é {self._idade}\n")
        
        
class Aluno(Pessoa):# no parâmetro é recibido a 
    def mostraAluno(self):
        print(f"Sou aluno e meu nome é {self._nome}\n")
        
        
class Professor(Pessoa):
    def mostra_professor(self):
        print(f"Sou um professor {self._nome}\n")
        
    
# Público não tem underline = aberto a qualquer classe e função 
# Privado tem 2 underlines = apenas a classe mãe tem acesso aos atributos
# Protegido 1 underline = as classes filhas podem acessar os atributos