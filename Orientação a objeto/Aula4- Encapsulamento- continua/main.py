from funcionario import Funcionario

func= Funcionario ("Cleitin", "Boxeador")

print(f"Seu nome é {func.get_nome()}")

func.set_nome("Isabela")

print(f"Seu nome é {func.get_nome()}")

print(f"Seu cargo é {func.cargo}")

func.cargo= "Gerente"

print(f"Seu cargo é {func.cargo}")