from flask import Flask
from livereload import Server

from routes.rotas import rotas
from controllers.home import home
from controllers.historico import historico

app = Flask(__name__, static_folder='static')
app.secret_key = 'datashield'

server = Server(app)
server.watch('app.py')
server.watch('templates/*.html')
server.watch('static/css/*.css')

app.config['DEBUG'] = False
app.config['TEMPLATES_AUTO_RELOAD'] = True

app.register_blueprint(rotas)
app.register_blueprint(home)
app.register_blueprint(historico)

if __name__ == '__main__': 
    app.run()
