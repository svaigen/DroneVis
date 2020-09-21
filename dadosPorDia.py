import csv
from datetime import datetime

allData = []
inscricao = []
validade = []
operador = []
tipo_pessoa = []
tipo_uso = []
fabricante = []
modelo = []
numero_serie = []
peso_maximo = []
cidade = []
estado = []
ramo = []

def leituraDados():
    with open('base_dados/droneData.csv', newline='',encoding="UTF-8-sig") as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            drone = []
            for data in row:
                drone.append(data)
            allData.append(drone)

            inscricao.append(row[0])
            validade.append(row[1])
            operador.append(row[2])
            tipo_pessoa.append(row[3])
            tipo_uso.append(row[4])
            fabricante.append(row[5])
            modelo.append(row[6])
            numero_serie.append(row[7])
            peso_maximo.append(row[8])
            cidade.append(row[9])
            estado.append(row[10])
            ramo.append(row[11])
    return allData,inscricao,validade,operador,tipo_pessoa,tipo_uso,fabricante,modelo,numero_serie,peso_maximo,cidade,estado,ramo


def regiao(sigla):
    if(sigla in ['PR','SC','RS']):
        return 'Sul'
    if(sigla in ['SP','RJ','MG','ES',]):
        return 'Sudeste'
    if(sigla in ['DF','GO','MT','MS']):
        return 'Centro-Oeste'
    if(sigla in ['AC','RO','AM','RR','AP','PA','TO']):
        return 'Norte'
    return 'Nordeste'


allData,inscricao,validade,operador,tipo_pessoa,tipo_uso,fabricante,modelo,numero_serie,peso_maximo,cidade,estado,ramo = leituraDados()

allData = allData[1:]
inscricao = inscricao[1:]
validade = validade[1:]
operador = operador[1:]
tipo_pessoa = tipo_pessoa[1:]
tipo_uso = tipo_uso[1:]
fabricante = fabricante[1:]
modelo = modelo[1:]
numero_serie = numero_serie[1:]
peso_maximo = peso_maximo[1:]
cidade = cidade[1:]
estado = estado[1:]
ramo = ramo[1:]



dic = []
for row in allData:
    day = row[0].strip()
    day = datetime.strptime(day, '%d/%m/%Y')
    dic.append([day,row[10].strip()])


with open('base_dados/dadosPordia2.csv', 'w', newline='',encoding="UTF-8-sig") as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',')
    cont = 0
    spamwriter.writerow(["day","estado",'elemento'])
    for d in dic:
        r = []
      #  r.append(cont)
        r.append(d[0])
        r.append(d[1])
        r.append(1)
        spamwriter.writerow(r)
        cont +=1
