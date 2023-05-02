valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))

soma=0

for cont in range(valor1,valor2+1):
    soma+= cont

print(f"A Soma do intervalo dos valores é : {soma}")
