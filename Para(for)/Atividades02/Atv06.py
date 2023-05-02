nome = input("Digite seu nome: ")
diaria = int(input("Quantos dias pretende se hospedar? "))

if diaria > 15:
    soma = (diaria * 60) + (diaria * 5.50)
    print(f"Olá {nome}, o tatal de sua conta é {soma}")
elif diaria == 15:
    soma = (diaria * 60) + (diaria * 6)
    print(f"Olá {nome}, o tatal de sua conta é {soma}")
elif diaria < 15:
    soma = (diaria * 60) + (diaria * 8)
    print(f"Olá {nome}, o tatal de sua conta é {soma}")
else:
    print(f"Olá {nome}, o tatal de sua conta é {soma}")
    
    
