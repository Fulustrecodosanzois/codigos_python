class Personagem:
    def __init__(self, nome, vida):
        self.nome= nome
        self.vida= vida
        
    def atacar(self):
        print(f"O personagem esta atacando!")
    
    def life(self):
        self.vida=5
        print(f"Sua vida é: {self.vida}")
    
class Jogador(Personagem):
    def __init__(self, nome, vida, raca):
        super().__init__(nome, vida)
        self.raca=raca
    def usar_habilidade(self, poder):
        self.poder=poder
        print(f"{self.nome}, O {self.raca}, usou o poder {self.poder}!!!")