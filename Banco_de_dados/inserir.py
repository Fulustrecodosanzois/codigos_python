import pymysql
# Estabelecendo a conexão

conexao= pymysql.connect(
    host="localhost", 
    user="root",
    passwd="", # Caso não tenha senha, deixa-se em branco
    database="departamento_db"
)

# Inserindo dados no banco
codigo= int(input("Informe o código do funcionário: "))
nome= (input("Informe o nome do funcionário: "))
salario= float(input("Informe o salário do funcionário: "))
cargo= (input("Informe o cargo do funcionário: "))

#variável que irá usar o código de inserir os dados
comando= "insert into funcionario values(%s, %s, %s, %s)"
#para cada valor é colocado <%s> para evitar ataques de sql injection. Foi inplementado pela biblioteca

#Uma lista/tupla que irá substituir os <%s> (precisa estar na ordem)
campos= (codigo, nome, salario, cargo)

# Fará conexão direta com o banco de dados usando "cursor()"
consulta= conexao.cursor()

#execute precisa de dois parâmetros 
# Ele irá colocar na ordem os comandos, por isso deve ser colocado em ordem
consulta.execute(comando, campos)

conexao.commit() # após os comandos serem dados, o commit irá registrar os valores (como se fosse um ENTER) O commit é uma operação usada para confirmar e finalizar uma transação. Quando você executa o comando commit, todas as alterações feitas no banco de dados durante a transação são permanentemente salvas e se tornam visíveis para outros usuários ou processos que acessam o banco de dados.

#rowcount irá contar quantas linhas foram inseridas no código
print(consulta.rowcount, "linhas(s) inserida com sucesso\n")

#desconecta o banco de dados
conexao.close()