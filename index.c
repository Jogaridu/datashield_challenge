#include <stdio.h>
#include <windows.h>
#include <tlhelp32.h>

int main()
{
    // Obter uma snapshot dos processos
    HANDLE snapshot = CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, 0);
    if (snapshot == INVALID_HANDLE_VALUE)
    {
        printf("Erro ao obter snapshot dos processos.\n");
        return 1;
    }

    // Inicializar a estrutura de dados de processo
    PROCESSENTRY32 processEntry;
    processEntry.dwSize = sizeof(PROCESSENTRY32);

    // Ler as informações do primeiro processo
    if (!Process32First(snapshot, &processEntry))
    {
        printf("Erro ao ler informações do primeiro processo.\n");
        CloseHandle(snapshot);
        return 1;
    }

    // Iterar sobre todos os processos e exibir suas informações
    do
    {
        printf("PID: %d, Nome: %ls\n", processEntry.th32ProcessID, processEntry.szExeFile);
    } while (Process32Next(snapshot, &processEntry));

    // Fechar o snapshot dos processos
    CloseHandle(snapshot);

    return 0;
}
