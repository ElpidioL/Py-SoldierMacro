import time
from modules import KeyFixTranslate
import pynput.mouse
from pynput.mouse import Button

def executarChaves(listaFinal ,tempo='False'):
    keyboard = pynput.keyboard.Controller()
    mouse = pynput.mouse.Controller()

    # Press and release space
    for i in range(len(listaFinal)):
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

        elif len(keyAtual) == 3 and "Key." not in listaFinal[i - 1].chave or len(keyAtual) == 5 and "Key." not in listaFinal[i -1].chave:
            keyAtual = keyAtual.replace("'","")
            if len(keyAtual) > 1:
                keyAtual = keyAtual.replace("[", "")
                keyAtual = keyAtual.replace("]", "")

            keyboard.press(keyAtual)
            keyboard.release(keyAtual)

        elif i > 0 and "Key.tab" in listaFinal[i].chave and keyAtual == listaFinal[i - 1].chave:
            KeyFixTranslate.tabChanger()

        elif i > 0 and "Key." in listaFinal[i -1].chave and keyAtual != listaFinal[i -1].chave and "Button" not in listaFinal[i -1].chave:
                KeyFixTranslate.solver(keyAtual, listaFinal[i - 1].chave)

        elif '\\' not in keyAtual:
            keyAtual = listaFinal[i].chave.replace("'", "")
            keyAtual = keyAtual.replace("Key.", "")
            contextVAR = getattr(keyboard._Key, keyAtual)
            keyboard.press(contextVAR)
            keyboard.release(contextVAR)