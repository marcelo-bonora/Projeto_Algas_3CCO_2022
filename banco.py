import mysql.connector

con = mysql.connector.connect(
host='127.0.0.1',
database='analise_algoritmos',
user='aluno',
password = 'sptech')

print(con)

# ------------ SCRIPT ----------
# create table tblProjetoAlgas (
# 	id int primary key auto_increment,
#     tempo_seg decimal(18, 2),
#     espaco_byte decimal(18, 2)
# )