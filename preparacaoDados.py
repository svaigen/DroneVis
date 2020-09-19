import csv
import json

inputFile = "base_dados/SISANT.json"
outputFile = "base_dados/droneData.csv"

cabecalhoOutput = ["inscrição","validade","operador","tipo_pessoa","tipo_uso","fabricante","modelo","numero_serie","peso_maximo_decolagem","cidade","estado","ramo"]

jsonFile = open(inputFile, "r", encoding="utf-8-sig")
jsonData = json.loads(jsonFile.read())
jsonFile.close()

dictOperador = {}
countPF = 1
countPJ = 1

with open(outputFile, 'w',newline='', encoding='utf-8') as csvfile:
    csvWriter = csv.writer(csvfile)
    csvWriter.writerow(cabecalhoOutput)
    rows = []
    for raw in jsonData:
        if not raw["Operador"] in dictOperador:
            if raw["CPFCNPJ"].find("/") != -1: #é pessoa jurídica
                dictOperador[raw["Operador"]] = "PJ{}".format(countPJ)
                countPJ += 1
            else: #é pessoa física
                dictOperador[raw["Operador"]] = "PF{}".format(countPF)
                countPF += 1
        # rows.append([raw["DataValidade"], dictOperador[raw["Operador"]], "PJ" if raw["CPFCNPJ"].find("/") != -1 else "PF", raw["TipoUso"].encode("utf-8"), raw["Fabricante"].encode("utf-8"), raw["Modelo"].encode("utf-8"), raw["Numerodeserie"], raw["Pesomaximodedecolagem"], raw["CidadeEstado"][:-3].encode("utf-8"), raw["CidadeEstado"][-2:], raw["Ramodeatividade"].encode("utf-8") if raw["Ramodeatividade"] != None else "Não Informado"])
        rows.append(["{}{}".format(raw["DataValidade"][:-2],int(raw["DataValidade"][-2:])-2),raw["DataValidade"], dictOperador[raw["Operador"]], "PJ" if raw["CPFCNPJ"].find("/") != -1 else "PF", raw["TipoUso"], raw["Fabricante"], raw["Modelo"], raw["Numerodeserie"], raw["Pesomaximodedecolagem"], raw["CidadeEstado"][:-3], raw["CidadeEstado"][-2:], raw["Ramodeatividade"] if raw["Ramodeatividade"] != None else "Não Informado"])
    csvWriter.writerows(rows)

