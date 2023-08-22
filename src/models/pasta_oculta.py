import os
import win32file
import win32con

def tornar_pasta_oculta(caminho_pasta):
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

caminho_da_pasta = r"C:\Área de Trabalho\123"
tornar_pasta_oculta(caminho_da_pasta)
