import uuid
import sys
import os
import subprocess

# import datetime
# import locale

# # Defina o local para português do Brasil (pt_BR)
# locale.setlocale(locale.LC_TIME, 'pt_BR')

# # Obtenha a data atual
# data_atual = datetime.datetime.now()

# # Obtenha o dia e o mês atual em formato de texto
# dia_atual = data_atual.strftime('%d')
# mes_atual = data_atual.strftime('%B').capitalize()  # %B retorna o nome do mês

# Exiba o dia e o mês
print(f'Dia: {dia_atual}')
print(f'Mês: {mes_atual}')

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'database'))
from conexao_db  import instanciar_usuarios, instanciar_analise

# def pegar_uuid():
#     try:

#         mac = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(2, -1, -1)])
#         machine_uuid = uuid.uuid5(uuid.NAMESPACE_DNS, mac)
#         return machine_uuid
    
#     except Exception as e:
#         print(f"Erro ao obter o número de série da placa-mãe: {str(e)}")
#         return None

# id = str(pegar_uuid())

# colecao_usuarios = instanciar_usuarios()
# colecao_analise = instanciar_analise()
# # dados = colecao_usuarios.find_one({"uuid": id})

# # print(dados)
# colecao_usuarios.update_one({"uuid": id}, {'$set': {'processos_analisados': len(list(colecao_analise.find({"uuid": id})))}})
