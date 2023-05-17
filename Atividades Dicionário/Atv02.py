pessoas= {}
lista= []

for perc in range(1,3):
    nome= input("Qual seu nome: ")
    pessoas[nome]= input("Digite seu número: ")
    lista.append(pessoas.copy())
    pessoas.clear()
    
print(lista)
    
    