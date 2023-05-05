while True:
    num= int(input("Informe um valor eentre 1 a 9: "))
    if num >= 1 and num <= 9:
        break

contador = 1

while contador <= 10:
    if num% 2 == 0:
        print(f"{num} x {contador} = {num * contador}")
    else:
        print(f"{num} + {contador} = {num + contador}")
        
    contador += 1