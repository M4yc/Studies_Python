import psutil

# Lista de nomes de processos que você deseja encerrar
jogar_valorant = ["Discord.exe", "MouseWithoutBorders.exe", "hid.exe", "msedge.exe", "avpui.exe", "GoogleDriveFS.exe", "figma_agent.exe", "EpicGamesLauncher.exe"]
processes_to_terminate = ["Discord.exe", "notepad.exe"]

for process in psutil.process_iter(attrs=['pid', 'name']):
    if process.info['name'] in jogar_valorant:
        try:
            pid = process.info['pid']
            p = psutil.Process(pid)
            p.terminate()  # Encerra o processo
            print(f"Processo {process.info['name']} (PID {pid}) encerrado.")
        except psutil.NoSuchProcess:
            pass