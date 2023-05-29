import pymysql

conexao= pymysql.connect(
    host="localhost",
    user= "root",
    passwd="",
    database= "departamento_db"
)

comando= "select * from funcionario"

consulta= conexao.cursor()

consulta.execute(comando)

#fetchall() irá trazer todas as linhas de registro que existe no banco
resultado= consulta.fetchall()

print(resultado,"\n")

for itens in resultado:
    print(f"nome: {itens[1]}, Salário: {itens[2]}")

conexao.close()