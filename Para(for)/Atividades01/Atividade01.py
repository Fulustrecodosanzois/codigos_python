soma = 0
pares = 0 

for i in range(50,71):
    if i % 2 == 0:
        soma += i
        pares += 1
        
media = soma / pares
        
print(f"A média dos números é {media}")

print(f"A quantidade de números pares é {pares}\n")
