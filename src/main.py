from services import monitorar_portas

portas_em_uso = monitorar_portas.iniciar()

# Imprime as portas abertas
# Imprime as portas em uso e seus respectivos processos
print("Portas em uso na máquina local:")
for porta, processo in portas_em_uso:
    print(f"Porta: {porta} | Processo: {processo}")
