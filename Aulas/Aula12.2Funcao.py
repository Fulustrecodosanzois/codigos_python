#Função com retorna

nome= input("Informe seu nome: ")

def contar_letras(texto):
    #print(f"O nome possui o total de {len(texto)} letras")
    return len(texto)
    
print(contar_letras(nome))