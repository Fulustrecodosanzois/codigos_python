imp= []
par= []

for cont in range(1,11):
    if cont % 2 == 0:
        par.append(cont)
    elif cont % 2 != 0:
        imp.append(cont)

print("A quantidade de númeoros pares é :",(len(par)))
print("A quantidade de númeoros impares é :",(len(imp)))