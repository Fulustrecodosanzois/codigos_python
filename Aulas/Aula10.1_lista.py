#import random
from random import randint
import os

os.system("cls")
sorteio =[] #criando uma lista vazia

for cont in range(1,11):
    sorteio.append(randint(1,100))#gera os valores e salva na lista

#valor= randint (1,100) #o randint irá gerar um valor aleatório \ ele não é expressado com .randint porque ele recebe um valor e precisa armazenar em variável 
print("-"*30)
print(sorteio,"\n")
print("-"*30)
sorteio.sort(reverse=True)#a função sorte() ordena de forma crescente. o parâmento reverse=True, faz o contrário, ordena de forma decrescemte
sorteio.sort 
print(sorteio, )
os.system("pause") # irá pausar o sistema até o usuário pressionar uma tecla. 

