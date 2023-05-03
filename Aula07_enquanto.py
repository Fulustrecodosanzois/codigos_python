# while funcionando como loop contador
"""
contador = 1 
while contador <= 5:
    print(contador)
    contador += 1
    
# while funcionando como loop condicional 

senha= ""
while senha != "123":
    senha= input ("informe sua senha: ")
    
print("obrigado por usar o sistema\n")
"""

# While como se fosse o faça enquanto

while True:
    senha= input("Informe sua senha: ")
    if senha == "123":
        break # se a condição é verdadeira ele irá para o loop

print("deu")