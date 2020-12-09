import sqlite3

# criar uma conexão e um cursor

con = sqlite3.connect('dadosimc.db')
cur = con.cursor()


#SQL linguagem criar tabela 

sql = 'create table dados'\
      '(id integer primary key,'\
      ' nome varchar (100) NOT NULL,'\
      'altura varchar(10)NOT NULL,'\
      'peso varchar(10)NOT NULL,))
      
cur.execute(sql)

#fechar a conexao
con.close()
Print ("Dados IMC criado com sucesso")

#inserir dados na tabela
sql = 'insert into dados values (nome, altura, peso) values ('Rafael','1,90','80.0')

#gravando no banco

con.commit()

print('Dados inseridos com sucesso.')
con.close

#Realizado o calculo IMC

sql ='select from dados values(peso/(altura*altura))'

print('Dados inseridos')
