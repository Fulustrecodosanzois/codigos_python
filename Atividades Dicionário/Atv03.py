menu= {}
lista= []

for perc in range(1,9):
    prato= input("Qual o nome do prato? ")
    menu[prato]= input("Digite o preço: ")
    lista.append(menu.copy())
    menu.clear()

print(lista, end=" ")