import subprocess

# Execute o comando tasklist no CMD e capture a saída
comando = "tasklist"
saida = subprocess.check_output(comando, shell=True, text=True)

# Separe as linhas da saída em uma lista
linhas = saida.split('\n')

# Crie um dicionário para armazenar os detalhes dos processos
processos = {}

# Itere sobre as linhas e extraia os detalhes dos processos
for linha in linhas[3:]:
    partes = linha.split()
    if len(partes) >= 5:
        pid = partes[1]
        nome = partes[0]
        processos[pid] = {"nome": nome}

# Imprima a lista de processos e seus IDs
print("Lista de Processos:")
for pid, detalhes in processos.items():
    print(f"PID: {pid}, Nome: {detalhes['nome']}")

# Solicite ao usuário que escolha um PID para encerrar
pid_para_encerrar = input("Digite o PID do processo que deseja encerrar: ")

# Execute o comando taskkill para encerrar o processo escolhido
comando_encerrar = f"taskkill /F /PID {pid_para_encerrar}"
try:
    subprocess.run(comando_encerrar, shell=True, text=True, check=True)
    print(f"Processo com PID {pid_para_encerrar} encerrado com sucesso.")
except subprocess.CalledProcessError:
    print(f"Não foi possível encerrar o processo com PID {pid_para_encerrar}.")

# teste teste