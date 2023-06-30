# from services import monitorar_portas

# portas_em_uso = monitorar_portas.iniciar()

# # Imprime as portas abertas
# # Imprime as portas em uso e seus respectivos processos
# print("Portas em uso na máquina local:")
# for porta, processo in portas_em_uso:
#     print(f"Porta: {porta} | Processo: {processo}")

import webview
import os

def main():

    # Obtém o caminho absoluto do arquivo HTML
    current_dir = os.path.dirname(os.path.abspath(__file__))
    html_file_path = os.path.join(current_dir, 'views', 'index.html')
    
    # Cria uma janela com WebView
    window = webview.create_window("Datashield", 'http://127.0.0.1:5500/src/views/index.html')
    
    # Carrega o arquivo HTML local
    # window.load_url('file://' + html_file_path)
    
    # Executa a janela
    webview.start()

if __name__ == '__main__':
    main()
