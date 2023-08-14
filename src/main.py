import subprocess
import os

def iniciar_aplicacao():

    # Import de banco de dados
    venv = os.path.join(os.path.dirname(__file__), '..', 'venv', 'Scripts', 'python.exe')

    flask_command = subprocess.Popen([venv, ".\src\server.py"])
    webview_command = subprocess.Popen([venv, r".\src\app.py"])

    flask_command.wait()
    webview_command.wait()

    

if __name__ == '__main__':
    iniciar_aplicacao()
