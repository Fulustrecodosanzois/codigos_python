""" Listas é uma estrutura de dados que permite armazenar múltiplos valores em uma única variável. As listas são mutáveis, o que significa que você pode adicionar, remover ou modificar elementos após sua criação. """

notas= [9.5,7.0,6.5,9]

print(notas)
print(type(notas))

for item in notas:
    print(item, end=" ")

print("-"*40)
    
#alterando item da lista

notas[2]= 8.5

print("-"*40)

print(notas,"\n", end=" ")

print("-"*40)
# inserindo valores na lista:

# Forma 1:

print("-"*40)
notas.append(4) # append inserir item no final da lista
print(notas, "\n")
print("-"*40)

# Forma 2
notas.insert(1,10) # Insert necessita de 2 parâmetros, o primeiro é o índice (posição) que deseja inserir o valor. o segundo é o valor a ser inserido
print(notas,"\n")
print("-"*40)

# Removendo valores

# Forma 1:

notas.pop() #remove o ultimo elemento
print(notas, "\n")

#Forma 2:
notas.pop(2)# Removendo pelo indice
print(notas, "\n")

# Forma 3:

notas.remove(9.5) #O remove() exclui usando o conteúdo da lista como paramêtro
print(notas,"\n")
