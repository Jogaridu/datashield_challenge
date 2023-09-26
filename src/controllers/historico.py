from flask import Blueprint
import sys
import os
import pythoncom
import datetime
import locale

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'models'))
from configuracoes import obj_configuracoes

historico = Blueprint('historico', __name__)

@historico.route('/api/processos')
def api_processos():

    dados = obj_configuracoes.pegar_processos_analisados()
    print(dados)
    if dados == False:
        return retornoAPI(404, 'bad request', dados)
    
    return retornoAPI(200, 'success', dados)


def retornoAPI(status_code, status, dados):
    return {
        'status_code': status_code,
        'status': status,
        'data': dados
    }