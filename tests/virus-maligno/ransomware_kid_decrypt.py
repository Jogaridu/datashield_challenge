import os
import pyaes

# Abrindo arquivos
for index in range(9):
    file_name = os.path.join(os.path.dirname(__file__), '..', 'vitima', f"img{index}.jpeg.pyransom")
    file = open(file_name, "rb")
    file_data = file.read()
    file.close()

    # Remover arquivo
    os.remove(file_name)

    # Chave para descriptografar
    key = "0143256879fravtr"
    key = key.encode()
    aes = pyaes.AESModeOfOperationCTR(key)
    decrypto_data = aes.decrypt(file_data)

    # Criação do arquivo criptografado
    new_file_name = os.path.join(os.path.dirname(__file__), '..', 'vitima', f"img{index}.jpeg")
    new_file = open(new_file_name, "wb")
    new_file.write(decrypto_data)
    new_file.close()
