import subprocess
import os

def iniciar_aplicacao():

    venv_python = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'venv', 'Scripts', 'python.exe'))

    # Obtenha os caminhos absolutos para os scripts
    server_script = os.path.abspath(r'server.py')
    app_script = os.path.abspath(r'app.py')

    flask_command = subprocess.Popen([venv_python, server_script])
    webview_command = subprocess.Popen([venv_python, app_script])

    flask_command.wait()
    webview_command.wait()

    

if __name__ == '__main__':
    iniciar_aplicacao()
