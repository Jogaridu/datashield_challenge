import psutil
import socket

def iniciar():
    portas_em_uso = []

    # Obtém todas as conexões de rede ativas
    conexoes = psutil.net_connections()

    # Filtra apenas as conexões TCP estabelecidas
    conexoes_tcp = [conn for conn in conexoes if conn.status == psutil.CONN_ESTABLISHED and conn.type == socket.SOCK_STREAM]

    # Obtém as portas das conexões TCP
    for conn in conexoes_tcp:
        porta_local = conn.laddr.port
        processo = psutil.Process(conn.pid)
        nome_processo = processo.name()
        portas_em_uso.append((porta_local, nome_processo))

    return portas_em_uso
