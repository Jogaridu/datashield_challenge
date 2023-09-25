from flask import Flask
from livereload import Server

from routes.rotas import rotas
from controllers.home import home

app = Flask(__name__, static_folder='static')
app.secret_key = 'datashield'

server = Server(app)
server.watch('app.py')
server.watch('templates/*.html')
server.watch('static/css/*.css')

app.config['DEBUG'] = True
app.config['TEMPLATES_AUTO_RELOAD'] = True

app.register_blueprint(rotas)
app.register_blueprint(home)

if __name__ == '__main__': 
    app.run()
