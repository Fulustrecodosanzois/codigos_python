import pymysql

class Produto:
    def conexao(self):
        con= pymysql.connect(
            host="localhost",
            user="root",
            password="",
            database="loja_db"
        )
        return con
    
    def cadastrar(self, codigo, nome, preco, quantidade):
        
        conexao= self.conexao()
        self.codigo= codigo
        self.nome= nome
        self.preco= preco
        self.quantidade= quantidade
        
        comando= "insert into produto values(%s, %s, %s, %s)"
        
        valores= (codigo, nome, preco, quantidade)
        
        consulta= conexao.cursor()
        
        consulta.execute(comando, valores)
        
        conexao.commit()
        
        print(consulta.rowcount, "linhas inseridas com sucesso\n")
        
        conexao.close()
        
    def consultar(self):
        
        conexao= self.conexao()
        
        comando= "select * from produto"
        
        consulta= conexao.cursor()
        
        consulta.execute(comando)
        
        resultado= consulta.fetchall()
        
        print(" TABELA PRDUTOS ===========================")
        
        cont=0
        for perc in resultado:
            cont+=1
            print(f"Código: {perc[0]}\t Nome: {perc[1]}\t Preço: {perc[2]}\t Quantidade: {perc[3]}\n")
         
        print(" PRODUTOS CADASTRTADOS ==================\n") 
        print(f"Há {cont} produtos cadastrados.\n")
        print("===========================================")
        
    def deletar(self, codigo):
        self.codigo= codigo
        conexao= self.conexao()
        
        comando= "delete from produto where codigo =%s"
        
        consulta= conexao.cursor()
        
        consulta.execute(comando, self.codigo)
        
        conexao.commit()
        
        
        if consulta.rowcount == 0:
            print("Erro: Nenhum item foi deletado")
        elif consulta.rowcount > 0:
            print(consulta.rowcount, "linhas exluidas com sucesso!")
        
        conexao.close()
        
        
    def atualizar_nome(self, nome, codigo):
        
        conexao= self.conexao()
        self.nome= nome
        self.codigo= codigo
        
        comando= "update produto set nome = %s where codigo = %s"
        
        valores= (self.nome, self.codigo)
        
        consulta= conexao.cursor()
        
        consulta.execute(comando, valores)
        
        conexao.commit()
        
        print(consulta.rowcount, "linha foi atualizada com sucesso!")
        
        conexao.close()   
        
     
    def atualizar_preco(self, preco, codigo):
        
        conexao= self.conexao()
        self.preco= preco
        self.codigo= codigo
        
        comando= "update produto set preco = %s where codigo = %s"
        
        valores= (self.preco, self.codigo)
        
        consulta= conexao.cursor()
        
        consulta.execute(comando, valores)
        
        conexao.commit()
        
        print(consulta.rowcount, "linha foi atualizada com sucesso!")
        
        conexao.close()
        
    def atualizar_quantidade(self, quantidade, codigo):
        conexao= self.conexao()
        self.quantidade= quantidade
        self.codigo= codigo
        
        comando= "update produto set quantidade_disponivel = %s where codigo = %s"
        
        valores= (self.quantidade, self.codigo)
        
        consulta= conexao.cursor()
        
        consulta.execute(comando, valores)
        
        conexao.commit()
        
        print(consulta.rowcount, "linha foi atualizada com sucesso")
        
        conexao.close()
        