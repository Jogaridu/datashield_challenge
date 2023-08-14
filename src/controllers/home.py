from flask import Blueprint
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'models'))

from monitorar_processos import iniciar

home = Blueprint('home', __name__)


@home.route('/api/teste')
def api_teste():

    iniciar()
    data = {'message': 'Monitoramento ligado!'}

    return data
