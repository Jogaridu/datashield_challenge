import subprocess
import git
import win32file
import win32con

def gitclone():
    resultado = subprocess.check_output('whoami', shell=True)
    saidacmd = resultado.decode('utf-8').strip()

    saidadiv = saidacmd.split("\\")
    nomeuser = saidadiv[-1]

    caminho = f"C:\\Users\\{nomeuser}\\Desktop\\1honeypot"

    url_repo = "https://github.com/pedr0aug/honey.git"

    git.Repo.clone_from(url_repo, caminho)

    print(f"Repositório clonado em: {caminho}")

    return caminho 

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


caminho_pasta = gitclone()
pasta_oculta(caminho_pasta)

