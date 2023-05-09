import ctypes


def main():
    print('Início EDR')

    # carrega a DLL do Windows que contém a função EnumProcesses
    kernel32 = ctypes.windll.kernel32

    # define o tamanho inicial do array de processos
    size = 256
    
    # cria um array com o tamanho definido
    pids = (ctypes.c_ulong * size)()

    # obtém a lista de processos
    while True:
        # chama a função EnumProcesses com o array de pids e seu tamanho
        bytes_needed = ctypes.c_ulong()
        if not kernel32.EnumProcesses(ctypes.byref(pids), ctypes.sizeof(pids), ctypes.byref(bytes_needed)):
            print("Não foi possível obter a lista de processos")
            break

        # verifica se o tamanho do array foi suficiente
        if bytes_needed.value <= ctypes.sizeof(pids):
            break

        # aumenta o tamanho do array e tenta novamente
        size *= 2
        pids = (ctypes.c_ulong * size)()

    # imprime a lista de processos
    num_processes = int(bytes_needed.value / ctypes.sizeof(ctypes.c_ulong()))
    print("Lista de processos:")
    for i in range(num_processes):
        pid = pids[i]
        print(f"PID: {pid}")


main()
