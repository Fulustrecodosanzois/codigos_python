import pymysql

conexao= pymysql.connect(
    host="localhost",
    user="root",
    passwd="",
    database="departamento_db"    
) 

codigo= int(input("Qual o código do funcionario deseja apagar? "))

#usa-se "=" para sinalizar a variável
comando= "delete from funcionario where cod_funcionario = %s"

consulta= conexao.cursor()

consulta.execute(comando, codigo)

conexao.commit()# É o ENTER

print(consulta.rowcount, "linha foi excluida com sucesso\n")

conexao.close()