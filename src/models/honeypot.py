import git
import win32file
import win32con
import winshell
import os


def iniciar():

    diretorios =  (r"c:", winshell.desktop(), winshell.application_data(), winshell.my_documents(), winshell.folder(0x0027), winshell.folder(0x000d), winshell.folder(0x0024), winshell.folder(0x0026), winshell.folder(0x000e))

    url_repo = "https://github.com/pedr0aug/honey.git"

    for caminho in diretorios:

        try:
            alvo_comeco = caminho + r"\acertificados"
            alvo_fim = caminho + r"\zcurriculos"

            if not os.path.exists(alvo_comeco):
                os.makedirs(alvo_comeco)

            if not os.path.exists(alvo_fim):
                os.makedirs(alvo_fim)
            
            git.Repo.clone_from(url_repo, alvo_comeco)
            git.Repo.clone_from(url_repo, alvo_fim)

            pasta_oculta(alvo_comeco)
            pasta_oculta(alvo_fim)

            print(f"Repositório clonado em: {caminho}")
        
        except:
            print(f"Repositório {caminho} ja existe ")
            pass

    return diretorios


def pasta_oculta(caminho_pasta):

    try:
        # Obtém os atributos atuais da pasta
        atributos_atuais = win32file.GetFileAttributesW(caminho_pasta)

        # Define o atributo de oculto
        novo_atributo = atributos_atuais | win32con.FILE_ATTRIBUTE_HIDDEN

        # Atualiza os atributos da pasta
        win32file.SetFileAttributesW(caminho_pasta, novo_atributo)
        print(f"Pasta '{caminho_pasta}' foi tornada oculta com sucesso!")
    except Exception as e:
        print(f"Erro ao tornar a pasta oculta: {e}")
