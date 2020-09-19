import csv

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
    with open('../base_dados/droneData.csv', newline='',encoding="UTF-8-sig") as csvfile:
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

