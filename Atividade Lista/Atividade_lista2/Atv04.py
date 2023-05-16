frutas= []
escolha= 0

for perc in range(1,4):
    frutas.append(str(input("Digite o nome de uma fruta: ")))
for i, fruta in enumerate(frutas):
    print(i+1,"...", fruta)# i+1 para que comece do 1

print("-"*30)   

while True:
    escolha = int(input("Escolha uma opção:\n1- Inseir uma fruta\n2- Excluir\nDigite uma opção: "))
    if escolha == 1:
        frutas.append(str(input("\nDigite o nome de uma fruta: ")))
        break
    elif escolha == 2:
        deletar= int(input("\nQual a posição da fruta? "))
        frutas.pop(deletar)#usado para deletar um elemento na lista com base na posição do indice e retorna o valor
        break
        
print("\n",frutas)