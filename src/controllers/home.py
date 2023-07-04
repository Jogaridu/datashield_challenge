from flask import Blueprint
from models.monitorar_processos import monitorar_processos

home = Blueprint('home', __name__)


@home.route('/api/teste')
def api_teste():

    # monitorar_processos()
    data = {'message': 'Monitoramento ligado!'}

    return data
