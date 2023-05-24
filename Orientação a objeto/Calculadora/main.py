from calculadora import Calculadora

num1= int(input("Digite um valor: "))
num2= int(input("Digite um valor: "))

calculadora= Calculadora (num1,num2)

while True:

    valor = input('''
            1 Somar
            2 Dividir
            3 Multiplicar
            4 Subtrair
            Digite um valor: 
            ''')

    if valor == "1":
        calculadora.somar()
    elif valor == "2":
        calculadora.div()
    elif valor == "3":
        calculadora.mult()
    elif valor == "4":
        calculadora.sub()
    else:
        print("Digite um valor válido!!")
