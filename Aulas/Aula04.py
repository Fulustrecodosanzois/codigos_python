texto = "Técnico em Desenvolvimento de Sistemas"
print("******* Título *******")
print("*"*10)
print(texto)

idade = int(input ("Digite sua idade : \n"))
print("- "*idade)

# Manipulando textos (string)

print(f"O total de letras é  {len(texto)}") # len() vem de length, que significa total de contagem

print(texto.upper()) #upper() coloca todo texto em maiúsculo.
print(texto.lower()) #upper() coloca todo texto em minúsculo.
print(texto.capitalize()) #upper() coloca a primeira letra da palavra em maiúsculo.

print(texto.replace("Sistemas","web")) # Modificar palavra por outra = variavel.replace("a que deve ser mudada, a que irá substituir")

# TRABALHANDO COM FATIAMENTO

print("BOM DIA")

print(texto[3]) # a contagem começa do zero
print(texto[:3]) # vai exibir todo o texto até a posição 2, no caso a posição a posição 3 não conta.
print(texto[3:])#vai exibir todo o texto que esta na posição 3 até a 10.