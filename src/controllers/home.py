from flask import Blueprint
import sys
import os
import pythoncom

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'models'))
from monitorar_processos import monitoramento
# from uniao import
import configuracoes

home = Blueprint('home', __name__)

@home.route('/api/monitorar')
def api_monitorar():

    global teste
    pythoncom.CoInitialize()

    monitoramento.iniciar()

    pythoncom.CoUninitialize()
    
    data = {'status': 'sucesso'}

    return data


@home.route('/api/desligar')
def api_desligar():

    global teste
    monitoramento.parar()
    
    data = {'status': 'sucesso'}

    return data


@home.route('/api/configuracoes')
def api_configuracoes():

    if (configuracoes.validar_arquivo_config()):
        dados = configuracoes.pegar_config()
        data = {'status': 200, 'data': dados}
    else:
        data = {'status': 404, 'data': dados}

    return data
