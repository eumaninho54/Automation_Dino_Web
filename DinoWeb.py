import pyautogui
import requests
import time
from PIL import ImageGrab
import sys
import keyboard


def check_internet():
    url = 'https://www.google.com'
    timeout = 5
    try:
        requests.get(url, timeout=timeout)
        return True
    except requests.exceptions.ConnectionError:
        return False


while True:
    confirm = pyautogui.confirm(text='Desligue sua internet para iniciar o programa!',
                                title='DESLIGUE A INTERNET',
                                buttons=['PRONTO', 'SAIR'])
    if confirm == 'SAIR':
        break
    elif check_internet():
        pyautogui.alert(text='VOCÊ NÃO DESLIGOU, VAMOS!!!', title='TÁ DE SACANAGEM NÉ?', button='FOI')
    if not check_internet():
        while True:
            pyautogui.press('win')
            pyautogui.write('google chrom')
            pyautogui.press('enter')
            time.sleep(1)
            pyautogui.write('chrome://dino')
            time.sleep(0.5)
            pyautogui.press('enter')
            pyautogui.hotkey('alt', 'space')
            time.sleep(0.5)
            pyautogui.press('x')
            time.sleep(1)
            pyautogui.alert(text='PRESSIONE A TECLA ESPAÇO PARA FINALIZAR O PROGRAMA!', title='É OS GURI', 
                            button='OK')
            pyautogui.press('space')
            time.sleep(1)
            X = 500
        

            def capture_tela():
                tela = ImageGrab.grab()
                return tela


            def capture_enemy(tela):
                for x in range(int(X), int(X-50), int(-1)):
                    for y in range(500, 630):
                        tela_2 = tela.getpixel((x, y))
                for x in range(int(X), int(X-50), int(-1)):
                    for y in range(500, 630):
                        cor = tela.getpixel((x, y))
                        if cor != tela_2:
                            return True
                        else:
                            tela_2 = tela
                            return False
            

            def capture_blue(tela):
                for x in range(int(X), int(X-50), int(-1)):
                    for y in range(600, 650):
                        cor = tela.getpixel((x, y))
                        if cor == (60, 187, 255) or cor == (0, 48, 209):
                            return True



            while True:
                if keyboard.is_pressed('space'):
                    pyautogui.alert(text='PROGRAMA DESLIGADO',
                                    title='ATÉ LOGO!')
                    pyautogui.hotkey('alt', 'f4')
                    sys.exit()
                tela = capture_tela()
                if capture_enemy(tela):
                    pyautogui.press('up')
                    X += 1
                if capture_blue(tela):
                    pyautogui.press('up')
                    X += 1
