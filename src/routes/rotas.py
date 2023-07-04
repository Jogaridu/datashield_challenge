from flask import Blueprint, render_template

rotas = Blueprint('rotas', __name__)

@rotas.route('/')
def index():
    return render_template('home.html')

@rotas.route('/sobre')
def sobre():
    return render_template('sobre.html')

