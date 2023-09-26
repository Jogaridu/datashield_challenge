import subprocess
caminho = "C:\Área de Trabalho\teste"

subprocess.call(r'C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe  Get-Acl -Path {caminho}"', shell=True)