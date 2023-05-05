import os

dentro_intervalo = 0
fora_intervalo = 0
contador = 1 

os.system("cls")

while contador <= 5:
    valor= int(input(f"Informe o {contador}°: "))
    if valor >= 10 and valor <= 20:
        dentro_intervalo += 1
    else:
        fora_intervalo += 1
    contador += 1
    
print(F"valores dentro do intervalo: {dentro_intervalo}")
print(F"valores dentro do intervalo: {fora_intervalo}")