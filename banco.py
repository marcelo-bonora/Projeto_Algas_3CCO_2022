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
#     cidade varchar(45),
#     produto varchar(45),
#     pagamento varchar(45),

#     tempoSeg decimal(18, 2),
#     espacoByte decimal(18, 2),
#     tipoRage varchar(100)
# )