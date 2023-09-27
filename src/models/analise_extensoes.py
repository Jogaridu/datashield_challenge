import os

def get_file_extension(file_path):
    _, file_extension = os.path.splitext(file_path)
    return file_extension

file_path = 'C:\Área de Trabalho\producaoquarentena\quarantine\teste.sha256'
extension = get_file_extension(file_path)

bad_extensions = ['.exe', '.dll', '.bat','.cmd','.vbs', '.ps1','.js', '.sys', '.drv', '.com', '.ocx', '.md5', '.sha256', '.shasum']

if extension:
    print(f"a extensao desta pagina é : {extension}")

    for extensions in bad_extensions:
        if extension == extensions:
            print("Cuidado, essa extensao pode ser um ransomware")
            break
        else:
            pass    
else:
    print("O arquivo não tem extensão")
    