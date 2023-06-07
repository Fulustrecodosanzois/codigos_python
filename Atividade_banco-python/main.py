from loja import Produto
import os

loja= Produto()


while True:
    escolha=input('''
                  
================================================
                  
1 - Cadastrar novo produto
2 - Listar produtos cadastrados
3 - Deletar produto
4 - Atualizar produto
5 - Sair

================================================    

Escolha uma opção: ''')

    if escolha == '1':
        #INSERIR VALORES:
        os.system('cls')
        loja.consultar()
        codigo= int(input("Digite o código do produto a ser cadastrado: "))
        nome= (input("Digite o nome do produto a ser cadastrado: "))
        preco= float(input("Digite o preço do produto a ser cadastrado: "))
        quantidade= int(input("Digite a quantidade do produto a ser cadastrado: "))
        loja.cadastrar(codigo, nome, preco, quantidade)
        

        
    elif escolha == "2":
        #CONSULTAR VALORES
        os.system('cls')
        loja.consultar()
        
        
    elif escolha == "3":
        #DELETAR VALORES
        os.system('cls')
        loja.consultar()
        codigo= int(input("Digite o código do produto a ser excluido: "))
        loja.deletar(codigo)
    
    elif escolha == "5":
        print("\nVai tinbora mermo, miseravi!!!\n")
        break 
            
    elif escolha == "4":
        os.system('cls')
        
        loja.consultar()
        
        escolha2= input('''
======================================   
                     
1- Atualizar nome do produto.
2- Atualizar preço do produto.
3- Atualizar estoque do produto.

======================================
Escolha uma opção:      ''')
    
    
        
        if escolha2 == "1":    
            #ATUALIZAR NOME:
            os.system('cls')
            loja.consultar()
            codigo=int(input("Digite o código do produto a ser atualizado: "))
            nome= input("Digite o nome a ser atualiado: ")
            loja.atualizar_nome(nome, codigo)

        if escolha2 == "2":
            # #ATUALIZAR PREÇO:
            os.system('cls')
            loja.consultar()
            codigo=int(input("Digite o código do produto a ser atualizado: "))
            preco= float(input("Digite o preço a ser atualiado: "))
            loja.atualizar_preco(preco, codigo)

        if escolha2 == "3":
            #ATUALIZAR QUANTIDADE
            os.system('cls')
            loja.consultar()
            codigo=int(input("Digite o código do produto a ser atualizado: "))
            quantidade= input("Digite a quantidade a ser atualiada: ")
            loja.atualizar_quantidade(quantidade, codigo)

    else:
        os.system('cls')
        print("Digite uma opção válida!") 