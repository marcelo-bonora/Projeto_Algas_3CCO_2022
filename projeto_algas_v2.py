import sys, random, time
import banco

mycursor = banco.con.cursor()

def insert(values):
  sql = "INSERT INTO tblProjetoAlgas (cidade, produto, formaPagamento, dia, quantidade, tempoSeg, tamanhoByte) VALUES (%s, %s, %s, %s, %s, %s, %s)"

  mycursor.execute(sql, values)

  banco.con.commit()
  print(mycursor.rowcount, "record inserted.")

cidades = ['Sao Paulo', 'Rio de Janeiro',]
produtos = ['Bebidas', 'Carnes']
pagamento = ['Debito', 'Credito']
semana = ['Domingo', 'Sabado']

def transaction(range):
    tempo_inicial = (time.time())
    lista = []
    for item in range:
        cidade = cidades[random.randrange(0, (len(cidades)), 1)]
        produto = produtos[random.randrange(0, (len(produtos)), 1)]
        formaPagamento = pagamento[random.randrange(0, (len(pagamento)), 1)]
        dia = semana[random.randrange(0, (len(semana)), 1)]
        quantidade = random.randint(1, 10)
        tempo_append = (time.time())
        tempo_final = (tempo_append - tempo_inicial)
        lista.append(item)
        tamanho = sys.getsizeof(lista)
        values = (cidade, produto, formaPagamento, dia, quantidade, tempo_final, tamanho)
        print(values)
        insert(values)

print('---- [ MENU ] ----')
print('Inserir')
print('Sair')
 
while True:
    do = input('O que voce deseja fazer?').split()
    
    operation = do[0]
    if operation == 'Inserir':
      valorInicial = input('Digite o valor inicial: ')
      valorFinal = input('Digite o valor final: ')
      intervalo = input('Digite o intervalo: ')
      transaction(range(int(valorInicial), int(valorFinal), int(intervalo)))

    elif operation == 'Sair':
        print('--- [ OPERAÇÃO ENCERRADA ] ---')
        break