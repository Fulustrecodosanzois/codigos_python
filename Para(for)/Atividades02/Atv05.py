num1= int(input("Digite o primeiro número: "))
num2= int(input("Digite o segundo número: "))
num3= int(input("Digite o terceiro número: "))

if num1 > num2:
    print(num1,)
elif num2 > num1:
    lista = num2
elif num3 > num1 and num2:
    lista = num3
else:
    pass

print(lista)
    