lista= [1, 4, 2, 8, 9, 7, 34, 32, 76, 43, 87, 56]

for percorre in lista: #a variável do for percorre a lista um elemento por vez
    if percorre % 2 == 0:
        lista.remove(percorre)
        
print(lista)
        
