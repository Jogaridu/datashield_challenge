import subprocess
import os
import time

def iniciar_aplicacao():

    # Obtenha os caminhos absolutos para os scripts
    server_script = os.path.abspath(r'.\src\server.py')
    time.sleep(1)
    app_script = os.path.abspath(r'.\src\app.py')

    flask_command = subprocess.Popen(["python", server_script])
    webview_command = subprocess.Popen(["python", app_script])

    flask_command.wait()
    webview_command.wait()


if __name__ == '__main__':
    iniciar_aplicacao()
