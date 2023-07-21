import pyautogui
import keyboard
import tkinter as tk
from threading import Thread

def mover_e_clicar(x, y):
    pyautogui.moveTo(x, y, duration=0.5)  # Move o cursor para a posição (x, y)
    pyautogui.click()  # Executa o clique esquerdo

def executar_macro():
    x_pos1, y_pos1 = 1123, 1071
    x_pos2, y_pos2 = 959, 799

    while not keyboard.is_pressed('ctrl') and not keyboard.is_pressed('2'):
        mover_e_clicar(x_pos1, y_pos1)
        mover_e_clicar(x_pos2, y_pos2)

def iniciar_thread():
    t = Thread(target=executar_macro)
    t.start()

# Interface Gráfica
root = tk.Tk()
root.title("Executar Macro")
root.geometry("300x100")

label = tk.Label(root, text="Pressione Ctrl+2 para parar o loop")
label.pack()

botao_iniciar = tk.Button(root, text="Iniciar Macro", command=iniciar_thread)
botao_iniciar.pack()

root.mainloop()
