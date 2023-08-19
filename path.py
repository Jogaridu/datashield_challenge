import subprocess
import git

resultado = subprocess.check_output('whoami', shell=True)
saidacmd = resultado.decode('utf-8').strip()

saidadiv = saidacmd.split("\\")
nomeuser = saidadiv[-1]

caminho = f"C:\\Users\\{nomeuser}\\Desktop\\honeypot"

url_repo = "https://github.com/pedr0aug/honey.git"

git.Repo.clone_from(url_repo, caminho)

print(f"Repositório clonado em: {caminho}")

