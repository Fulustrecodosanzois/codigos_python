import os
estado = {"uf": "Maranhão", "sigla":"MA"}

os.system("cls")
print(estado)

# INSERINDO DADOS EM UM DICIONÁRIO
# FORMA 1
estado["populacao"] = "20.000.000"
print(estado)

#FORMA 2
estado.update({"capital":"São Luis"})
print(estado)

#REMOVENDO ITENS DO DICIONÁRIO
#FORMA 1
estado.pop("uf")
print(estado)

#FORMA 2
del(estado["populacao"])
print(estado)

# FORMA 3 - APAGAR TODO CONTEÚDO
estado.clear()
print(estado)