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

def geraPosicao(data):
    mes = int(data[3:5])
    ano = int(data[6:])

    if(ano == 2018):
        if(mes == 1):
            return 0
        if(mes == 2):
            return 1
        if(mes == 3):
            return 2
        if(mes == 4):
            return 3
        if(mes == 5):
            return 4
        if(mes == 6):
            return 5
        if(mes == 7):
            return 6
        if(mes == 8):
            return 7
        if(mes == 9):
            return 8
        if(mes == 10):
            return 9
        if(mes == 11):
            return 10
        if(mes == 12):
            return 11
    if(ano == 2019):
        if(mes == 1):
            return 12
        if(mes == 2):
            return 13
        if(mes == 3):
            return 14
        if(mes == 4):
            return 15
        if(mes == 5):
            return 16
        if(mes == 6):
            return 17
        if(mes == 7):
            return 18
        if(mes == 8):
            return 19
        if(mes == 9):
            return 20
        if(mes == 10):
            return 21
        if(mes == 11):
            return 22
        if(mes == 12):
            return 23
    if(ano == 2020):
        if(mes == 1):
            return 24
        if(mes == 2):
            return 25
        if(mes == 3):
            return 26
        if(mes == 4):
            return 27
        if(mes == 5):
            return 28
        if(mes == 6):
            return 29
        if(mes == 7):
            return 30
        if(mes == 8):
            return 31
        if(mes == 9):
            return 32

def getPallete27colors():
    return [[0,0,255],
            [0,19,245],
            [0,39,235],
            [0,58,225],
            [0,78,215],
            [0,98,206],
            [0,117,196],
            [0,137,186],
            [0,156,176],
            [0,176,167],
            [0,196,157],
            [0,215,147],
            [0,235,137],
            [0,255,128],
            [18,236,128],
            [36,218,128],
            [54,200,128],
            [72,182,128],
            [91,163,128],
            [109,145,128],
            [127,127,128],
            [145,109,128],
            [163,91,128],
            [182,72,128],
            [200,54,128],
            [218,36,128],
            [236,18,128]]