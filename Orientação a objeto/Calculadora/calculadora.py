class Calculadora:
    def __init__(self, numero1, numero2):
        self.__numero1= numero1
        self.__numero2= numero2
     
       
    def somar (self):
        print(f" {self.__numero1} + {self.__numero2} =", self.__numero1 + self.__numero2)
    def div (self):
        print(f" {self.__numero1} / {self.__numero2} =", self.__numero1 / self.__numero2)
    def mult (self):
        print(f" {self.__numero1} * {self.__numero2} =", (self.__numero1 * self.__numero2))
    def sub (self):
        print(f" {self.__numero1} - {self.__numero2} =", self.__numero1 - self.__numero2)
        