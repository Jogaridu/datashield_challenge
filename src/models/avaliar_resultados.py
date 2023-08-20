# CÓDIGO ABAIXO É PARA AVALIAR RESULTADOS DO MONGODB
colecao_processos.find()
documentos = list(colecao_processos.find())

resultado = {}

atributos_analise = ['handleCount', 'pageFaults', 'pageFileUsage', 'peakPageFileUsage', 'workingSetSize', 'threadCount', 'priority', 'privatePageCount']

for atributo in atributos_analise:
    resultado[atributo] = {
        'atributo': '',
        'maior_valor': float('-inf')
    }

for atributo in atributos_analise:
    maior_valor = float('-inf')
    processo_nome = ''
    for json_obj in documentos:
        if atributo in json_obj['dadosProcesso']:
            valor = json_obj['dadosProcesso'][atributo]
            if float(valor) > float(maior_valor):
                maior_valor = valor
                processo_nome = json_obj['nomeProcesso']
                resultado[atributo]['atributo'] = processo_nome
                resultado[atributo]['maior_valor'] = maior_valor

print(resultado)