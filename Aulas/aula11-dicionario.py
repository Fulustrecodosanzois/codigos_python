lista = ["João", 30, "Cohab"]
pessoa = {
    "nome":"Maria",
    "idade":24,
    "bairro":"Renascença"
}

print(lista[0])
print(pessoa,"\n")

# EXIBINDO AS CHAVES UTILIZANDO O COMANDO KEYS()
print(pessoa.keys())

# EXIBINDO OS VALORES UTILIZANDO O COMANDO VALUES()
print(pessoa.items())

# EXIBINDO O DICIONÁRIO MAIS DETALHADO
for chave, valor in pessoa.items():
    print(f"{chave}:{valor}")