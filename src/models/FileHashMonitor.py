#importa as bibliotecas necessarias
import hashlib
import os.path
from os import listdir
from os.path import isfile, join


#funcao para listar o conteudo da pasta e verifica se é um arquivo 
def nameOfFiles(folder_path):
    filesNames = [f for f in listdir(folder_path) if isfile(join(folder_path, f))]
    return filesNames

#calcula a entropia da pasta e retorna um hash unico
def main(filesNames, folder_path):
    filesHash = ''
    sha512 = hashlib.sha512()
    for i in filesNames:
        try: 
            with open(os.path.join(folder_path, i), "rb") as f:
                while True:
                    data = f.read()
                    if not data:
                        break
                    sha512.update(data)
            filesHash += sha512.hexdigest()
        
        except PermissionError:
            print(f"Erro de permissão ao acessar o arquivo: {i}")
            continue
        except FileNotFoundError:
            print(f"Arquivo não encontrado: {i}")
            continue

    return filesHash

#funcao que cria o arquivo com a hash para verificacao constante
def createControlFile(folder_path):
    filesNames = nameOfFiles(folder_path)
    fileControl = main(filesNames, folder_path)
    with open('fileControlData.txt', 'w', encoding='utf-8') as f:
        f.write(fileControl)
    print("File generated. Everything is OK!")

# Defina o caminho da pasta que deseja monitorar
folder_path = "C:\Área de Trabalho\Challenge\Honeypots\Honeypots\AaHoneyPot"

#inicio do processo de verificação e comparação do arquivo FileControl com o atual 
while True:

    if os.path.exists(folder_path):
        filesNames = nameOfFiles(folder_path)
        fileControl = main(filesNames, folder_path)

        if os.path.exists("fileControlData.txt"):
            with open('fileControlData.txt', 'r', encoding='utf-8') as file:
                fileContent = file.read()
                if fileContent == fileControl:
                    print("Monitoring...")
                else:
                    print("A pasta foi editada.")
                    break
        else:
            createControlFile(folder_path)
    else:
        print("O caminho da pasta não existe")
    