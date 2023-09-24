from flask import Blueprint
import sys
import os
import pythoncom

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'models'))
from monitorar_processos import monitoramento
from configuracoes import obj_configuracoes
# from uniao import

home = Blueprint('home', __name__)

@home.route('/api/monitorar')
def api_monitorar():

    pythoncom.CoInitialize()

    obj_configuracoes.definir_status('ativo')
    monitoramento.iniciar()

    pythoncom.CoUninitialize()
    
    data = {'status': 'sucesso'}

    return data


@home.route('/api/desligar')
def api_desligar():

    monitoramento.parar()
    obj_configuracoes.definir_status('inativo')
    
    data = {'status': 'sucesso'}

    return data


@home.route('/api/configuracoes')
def api_configuracoes():
    
    obj_configuracoes.validar_config()
    dados = obj_configuracoes.pegar_config()
    
    if dados:
        return retornoAPI(200, 'success', dados)
    else:
        return retornoAPI(404, 'bad request', {})


def retornoAPI(status_code, status, dados):
    return {
        'status_code': status_code,
        'status': status,
        'data': dados
    }