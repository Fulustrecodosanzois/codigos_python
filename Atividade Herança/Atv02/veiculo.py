class Veiculo:
    def __init__(self, marca, ano):
        self.marca= marca
        self.ano= ano
    
    def inserir_valor(self):
        self.marca= input("Qual a marca do carro? ")
        self.ano= input("Qual o ano do carro? ")
        
    def get_marc(self):
        print(f"A marca do veículo é {self.marca}")
    
    def get_ano(self):
        print(f"A marca do veículo é {self.ano}")
        
class Carro(Veiculo):
    def __init__(self, marca, ano, portas, mala):
        super().__init__(marca, ano)
        self.portas=portas
        self.mala=mala
        
    def get_portas(self):
        return self.portas
    
    def get_mala(self):
        return self.mala