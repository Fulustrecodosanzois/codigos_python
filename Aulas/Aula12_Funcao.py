

#função sem parâmetro 

def somar():
    valor1= int(input("informe um valor: "))
    valor2= int(input("informe outro valor: "))

    print(valor1+valor2)
    
    
    
#Função com parâmetro
num1= int(input("Informe o valor 1: "))
num2= int(input("Informe o valor 2: "))

def multiplicar(a, b):
    print(a * b)
    
multiplicar(num1,num2)