from random import randint

num=[]
posi= 0

for cont in range(1,11):
    num.append(randint(1, 15))
    print("-"*30)
    if num[cont - 1] == 10:
        posi= cont
        print(f"{num[cont-1]} é igual a 10, e esta na posição {cont}")# cont começa de 1, porém num(lista) começa de 0, para obter a posição correta é necessário voltar uma posição
     
     
print(num)