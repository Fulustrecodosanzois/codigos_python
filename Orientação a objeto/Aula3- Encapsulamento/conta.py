class Conta:
    def __init__(self, numero, titular, saldo, limite=100):
        self.__numero = numero # emcapsulamento -> Tornamos um elemento privado com 2 underlines. com 1 underline ele esta protegido. Com nenhum ele é público
        self.__titular = titular 
        self.__saldo = saldo
        self.__limite= limite # Esse atributo possui um valor padão de maneira que o usuário poderá ou não informar este valor
        
    def relatorio(self):
        print(f"Olá {self.__titular} o número da sua conta é {self.__numero} e o seu limite {self.__limite}, Caralho!!!")
    
    def so_saldo(self):
        print(f"Seu saldo é {self.__saldo}")
        
     # O método get irá retornar ou exibir o valor do tributo.
    def get_limite(self):
        return self.__limite
    
    
    # O método set irá alterar o conteúdo do atributo, sem exibir nada
    def set_limite(self, valor):
        if valor < 0:
            print("Valor menor que zero, informe outro valor")
        else: 
            self.__limite= valor
    
    # MODIFICAR O ATIBUTO SALDO COM @PROPERTY E @SETTER 
    
    @property
    def saldo(self):
        print(f"Seu saldo é {self.__saldo}\n")
        
    @saldo.setter
    def saldo(self, valor):
        if valor <= 0:
            print(f"Digite um número maior que zero\n")
        else:
            self.__saldo =valor