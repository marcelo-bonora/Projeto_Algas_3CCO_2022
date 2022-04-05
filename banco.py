import mysql.connector

con = mysql.connector.connect(
host='localhost',
database='ProjetoAlgas',
user='root',
password = 'urubu100')

print(con)

# ------------ SCRIPT ----------
# create table tblProjetoAlgas (
# 	id int primary key auto_increment,
#     tempo_seg decimal(18, 2),
#     espaco_byte decimal(18, 2),
#     tipo_rage varchar(100)
# )