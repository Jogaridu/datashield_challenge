import subprocess

# Define o caminho da pasta
folder_path = r'"C:\Área de Trabalho\producaoquarentena\quarantine"'  # Caminho da pasta

# Comando PowerShell para obter a lista de permissões
ps_command = f"""
$acl = Get-Acl "{folder_path}"
$acl | Format-Table -Property AccessToString, Group
"""

# Executa o comando PowerShell e obtém a saída
result = subprocess.run(['powershell.exe', '-Command', ps_command], capture_output=True, text=True)
output_lines = result.stdout.split('\n')

# Gera uma lista de usuários/grupos a serem removidos
users_to_remove = [line.strip() for line in output_lines if line.strip()]

# Comando PowerShell para remover todas as permissões
ps_command_remove_all = f"""
$acl = Get-Acl "{folder_path}"
$acl.Access | ForEach-Object {{ $acl.RemoveAccessRule($_) }}
Set-Acl -Path "{folder_path}" -AclObject $acl
"""
# $acl.Access | %{$acl.RemoveAccessRule($_)}
# Executa o comando PowerShell para remover todas as permissões
subprocess.run(['powershell.exe', '-Command', ps_command_remove_all])

print("Todas as permissões foram revogadas com sucesso.")
