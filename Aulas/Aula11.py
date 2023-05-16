lista= ["joão", 30, "cohab"]
pessoa= {
    "nome":"maria",
    "idade":24,
    "bairro":"renascença"
}

print(list[0])
print(pessoa, "\n")

#exibindo as chaves utilizando o comando keys()
print(pessoa.keys())

#exibindo os valores utilizando o comando values()
print(pessoa.values())

# Exibindo tanto a chave como valor utilizando o comando items()
print(pessoa.items())

# ixibindo o dicionario mais detalhado 
for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")