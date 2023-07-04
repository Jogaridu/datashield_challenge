import webview
import requests
import time
from flask import Flask
from multiprocessing import Process

from routes.rotas import rotas
from controllers.home import home

app = Flask(__name__, static_folder='static')
app.secret_key = 'datashield'

app.register_blueprint(rotas)
app.register_blueprint(home)


def waitUntilServerReady():
    while True:
        try:
            response = requests.get('http://localhost:5000/')
            if response.status_code == 200:
                break
        except requests.exceptions.ConnectionError:
            pass
        time.sleep(1)


def iniciar_aplicacao():
    waitUntilServerReady()
    webview.create_window("Datashield", 'http://localhost:5000/')
    webview.start()


def iniciar_flask():
    app.run()


if __name__ == '__main__':
    flask_process = Process(target=iniciar_flask)
    webview_process = Process(target=iniciar_aplicacao)

    flask_process.start()
    webview_process.start()

    flask_process.join()
    webview_process.join()
