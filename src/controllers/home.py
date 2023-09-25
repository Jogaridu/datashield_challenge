from flask import Blueprint
import sys
import os
import pythoncom
import datetime
import locale

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'models'))
from monitorar_processos import monitoramento
from configuracoes import obj_configuracoes

home = Blueprint('home', __name__)

@home.route('/api/monitorar')
def api_monitorar():

    locale.setlocale(locale.LC_TIME, 'pt_BR')
    data_atual = datetime.datetime.now()

    dia_atual = data_atual.strftime('%d')
    mes_atual = data_atual.strftime('%B').capitalize()
    
    obj_configuracoes.definir_status('ativo')
    obj_configuracoes.definir_ultima_analise(f"{dia_atual} de {mes_atual}")

    pythoncom.CoInitialize()

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
    
    obj_configuracoes.definir_processos_analisados()

    obj_configuracoes.validar_config()
    dados = obj_configuracoes.pegar_config()
    
    if dados:
        return retornoAPI(200, 'success', dados)
    else:
        return retornoAPI(404, 'bad request', {})
    

@home.route('/api/status')
def api_status_health():
    
    return retornoAPI(200, 'success', {'status_health': monitoramento.status_health()})


def retornoAPI(status_code, status, dados):
    return {
        'status_code': status_code,
        'status': status,
        'data': dados
    }