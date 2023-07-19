import pyautogui
import keyboard

def mover_e_clicar(x, y):
    pyautogui.moveTo(x, y, duration=0.5)  # Move o cursor para a posição (x, y)
    pyautogui.click()  # Executa o clique esquerdo

def main():
    x_pos1, y_pos1 = 1123, 1071
    x_pos2, y_pos2 = 959, 799

    print("Pressione Control + 2 para parar o loop.")
    while True:
        # Executa a macro
        mover_e_clicar(x_pos1, y_pos1)
        mover_e_clicar(x_pos2, y_pos2)

        # Verifica se a tecla Control + 2 foi pressionada para parar o loop
        if keyboard.is_pressed('ctrl') and keyboard.is_pressed('2'):
            print("Loop parado.")
            break

main()
