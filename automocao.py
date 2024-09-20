import pyautogui
import time

apagar = "backspace"

# pausa entre os comandos do pyautogui 
pyautogui.PAUSE = 0.35

# abrir excel
pyautogui.click(x=564, y=1056)

# selecionar primeiro nome visivel/
pyautogui.click(x=312, y=228)

while True:
    pyautogui.hotkey("ctrl", "c")

    # abrir sigest
    pyautogui.click(x=513, y=1068)

    # sigest pesquisa
    pyautogui.click(x=977, y=262)
    start_time = time.time()
    while time.time() - start_time < 7:
        pyautogui.hotkey("ctrl", "backspace")
        time.sleep(0.1)
    pyautogui.hotkey("ctrl", "v")

    # abrir chrome
    pyautogui.click(x=611, y=1060)
    pyautogui.hotkey("ctrl", "f")
    pyautogui.hotkey("ctrl", "v")
    time.sleep(1.15)

    # RG no sheets
    pyautogui.click(x=432, y=977)
    pyautogui.hotkey("ctrl", "c")


    # abrir sigest
    pyautogui.click(x=513, y=1068)

    # pessoa
    pyautogui.click(x=727, y=308, clicks=2)
    time.sleep(1)

    # editar
    pyautogui.click(x=521, y=526)

    # campo RG
    pyautogui.click(x=696, y=466)
    pyautogui.hotkey("ctrl", "v")

    # salvar sigest
    pyautogui.click(x=562, y=531)

    # confirmar
    pyautogui.click(x=960, y=604)

    # sair
    pyautogui.click(x=634, y=525)


    # abrir excel
    pyautogui.click(x=564, y=1056)


    # pintar 
    pyautogui.click(x=359, y=112)

    # salvar
    pyautogui.hotkey("ctrl", "b")

    # ir para o proximo
    pyautogui.press("down")