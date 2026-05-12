
import subprocess
import sys
import os
import hashlib

def instalar_silencioso(pacote):
    # Configuração para esconder a janela no Windows
    startupinfo = None
    if os.name == 'nt':  # Verifica se o sistema é Windows
     startupinfo = subprocess.STARTUPINFO()
     startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    startupinfo.wShowWindow = 0 # 0 significa SW_HIDE (esconder)

    try:
        # stdout e stderr como DEVNULL removem os textos que apareceriam no console
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", pacote],
            startupinfo=startupinfo,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        print(f"Instalação de '{pacote}' concluída em segundo plano.")
    except Exception as e:
        print(f"Erro ao instalar: {e}")

instalar_silencioso("pynput")
instalar_silencioso("psutil")
instalar_silencioso("pyautogui")
passw = 342312
stop = False

from pynput import mouse,keyboard
import pyautogui
import psutil


google = "Google Chrome.exe"


def on_click(): # MATAR O ROBLOX
    for process in psutil.process_iter():
        if process.name() == "Google Chromeex":
            process.kill()
        

def ctrl_wc():
    newsenha = pyautogui.password("Senha:")
    newsenha = hashlib.sha256(newsenha.encode())
    newsenha = newsenha.hexdigest()

    if newsenha != passw:
        pyautogui.alert("Senha Incorreta")
    else:
        pyautogui.alert("Acesso liberado!")
        for process in psutil.process_iter():
            if process.name() == "python.exe":
                process.kill()

mouse_listener = mouse.Listener(on_click=on_click)

# 2. Definimos o GlobalHotKeys do Teclado
# Note o '+' entre as teclas. É isso que impede de disparar só com o Ctrl.
key_hotkeys = keyboard.GlobalHotKeys({
    '<ctrl>+n': ctrl_wc
})

# 3. Iniciamos ambos
mouse_listener.start()
key_hotkeys.start()

# 4. Agora sim usamos o join para manter o script rodando
# O join() impede que o programa feche enquanto os listeners estiverem ativos
try:
    mouse_listener.join()
    key_hotkeys.join()
except KeyboardInterrupt:
    print("Encerrando...")