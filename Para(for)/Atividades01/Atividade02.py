cont = 0

for i in range(1,6):
    idade = int(input("Digite um idade: "))
    if idade >= 18:
        cont += 1

print(f"A quantidade de pessoas que tem mais de 18 anos é {cont}")            