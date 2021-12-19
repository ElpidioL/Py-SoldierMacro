import time
from modules import KeyFixTranslate
from pynput import keyboard
from pynput.keyboard import Listener as KeyboardListener
import pynput.mouse
from pynput.mouse import Button

def executarChaves(listaFinal,stopKey,tempo='False', ):
    keyboardController = pynput.keyboard.Controller()
    mouse = pynput.mouse.Controller()
    stopKey = getattr(keyboardController._Key, stopKey)
    breakCode = [False]

    for i in range(len(listaFinal)):
        def on_release(key):
            print('{0} released'.format(key))
            if key == stopKey:
                breakCode[0] = True
                keyboard_listener.stop()
                return False
        if i == 0:
            keyboard_listener = KeyboardListener(on_release=on_release)
            keyboard_listener.start()

        if tempo != 'False':
            time.sleep(float(tempo))
        else:
            time.sleep(float(listaFinal[i].tempo))

        keyAtual = listaFinal[i].chave #.replace("'", "")

        if "Button" in keyAtual:
            ondeClicar = keyAtual.split(",")
            cliquePosX = ondeClicar[0]
            cliquePosY = ondeClicar[1]
            cliqueType = ondeClicar[2]
            mouse.position = (int(cliquePosX), int(cliquePosY))
            cliqueTypeGet = getattr(Button, cliqueType.replace("Button.",""))
            mouse.press(cliqueTypeGet)
            mouse.release(cliqueTypeGet)

        elif len(keyAtual) == 3 and "Key." not in listaFinal[i - 1].chave or len(keyAtual) == 5 and "Key." not in listaFinal[i -1].chave or len(keyAtual) == 5 and ("Key." not in listaFinal[i -1].chave or "enter" in listaFinal[i -1].chave or "backspace" in listaFinal[i -1].chave):
            keyAtual = keyAtual.replace("'","")
            if len(keyAtual) > 1:
                keyAtual = keyAtual.replace("[", "")
                keyAtual = keyAtual.replace("]", "")

            keyboardController.press(keyAtual)
            keyboardController.release(keyAtual)

        elif i > 0 and "Key.tab" in listaFinal[i].chave and keyAtual == listaFinal[i - 1].chave:
            KeyFixTranslate.tabChanger()

        elif i > 0 and "Key." in listaFinal[i -1].chave and keyAtual != listaFinal[i -1].chave and "Button" not in listaFinal[i -1].chave:
                KeyFixTranslate.solver(keyAtual, listaFinal[i - 1].chave)

        elif '\\' not in keyAtual:
            keyAtual = listaFinal[i].chave.replace("'", "")
            keyAtual = keyAtual.replace("Key.", "")
            contextVAR = getattr(keyboardController._Key, keyAtual)
            keyboardController.press(contextVAR)
            keyboardController.release(contextVAR)

        if breakCode[0]:
            keyboard_listener.stop()
            return False
        if i == (len(listaFinal) -1):
            keyboard_listener.stop()
            return False


