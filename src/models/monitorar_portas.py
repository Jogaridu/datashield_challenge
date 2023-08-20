import psutil
import socket

def iniciar():
    portas_em_uso = []

    # Obtém todas as conexões de rede ativas
    conexoes = psutil.net_connections()

    # Filtra apenas as conexões UDP estabelecidas
    conexoes_udp = [conn for conn in conexoes if conn.status == psutil.CONN_NONE and conn.type == socket.SOCK_DGRAM]

    # Obtém as portas das conexões UDP
    for conn in conexoes_udp:
        porta_local = conn.laddr.port
        processo = psutil.Process(conn.pid)
        nome_processo = processo.name()
        portas_em_uso.append((porta_local, nome_processo))

    portas_em_uso_ordenadas = sorted(portas_em_uso, key=lambda x: x[0])  # Ordena pelo número da porta

    for porta, processo in portas_em_uso_ordenadas:
        print(f"Porta: {porta}, Processo: {processo}")

iniciar()
