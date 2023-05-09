""" As coleções são: Tupla, Lista, Dicionário
"""
#Tuplas são imutáveis
# Ex de Tuplas:

lanche = ("pizza", "hotdog", "refri", "batata")
idades= tuple(18,25,63) # outra forma de criar tupla

print(lanche)
print("-"*50)
print(type(lanche)) # Saber o tipo de variável (Tupla)
print(lanche[1]) #print da posição 1 da tupla
print(f"O total de lanches é {len(lanche)}\n")

#lanche[2] = "suco"

for cont in range (4): # Para exibir um elemento após o outro na tupla
    print(lanche[cont])

print("-"*50)

for item in lanche:
    print(item)
    
print("-"*50)

for indice,elemento in enumerate(lanche):# Enumera os itens
    print(f"{indice} = {elemento}")

# Enumerate serve para permitir acessar os índices da tupla. já a variável indice, irá armazenar os valores do indice