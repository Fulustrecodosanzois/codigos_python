import os
pessoa = dict()
grupo = list()

grupo.append({"nome":"João", "idade":56})
grupo.append({"nome":"Maria", "idade":27})
grupo.append({"nome":"José", "idade":32})

os.system("cls")

print(grupo,"\n")
"""
for contador in range(0,3):
    pessoa["nome"] = input("Qual seu nome: ")
    pessoa["idade"] = int(input("Qual sua idade: "))

    grupo.append(pessoa.copy())#Criando cópias do dicionário, sem criar vínculo ao dicionário(copiando e limpando)

print(grupo)
"""
# ACESSANDO ITENS DO DICIONÁRIO
for contador in range(0,3):
    print(f"{grupo[contador]['nome']}: {grupo[contador]['idade']}")

# OUTRA FORMA DE ACESSAR DICIONÁRIO
for linha in grupo:
    for elemento in linha.values():
        print(f"{elemento}", end="-- ")
    print()
