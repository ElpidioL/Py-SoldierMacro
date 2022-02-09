import time
from pynput import keyboard
from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener


listDeComandos =[]
listaFinal = []
stopAwait = []

class listDeChaves:
    def __init__(self, chave, tempo):
        self.chave = chave
        self.tempo = tempo

def keylist():
    pegarLista = []
    listaTempo = [time.perf_counter()]

    def on_click(x, y, button, pressed):
        if pressed:
            print('{0}, {1}) with {2}'.format(x, y, button))
            end = time.perf_counter() - sum(listaTempo)
            listaTempo.append(float('%f' % end))
            pegarLista.append(listDeChaves('{0},{1},{2}'.format(x, y, button), listaTempo[-1]))

    def on_press(key):
        try:
            end = time.perf_counter() - sum(listaTempo)
            listaTempo.append(float('%f' % end ))
            pegarLista.append(listDeChaves('{0}'.format(key), listaTempo[-1]))

        except AttributeError:
            pegarLista.append(listDeChaves('{0}'.format(key), "1"))

    def on_release(key):
        print('{0} released'.format(key))
        if key == keyboard.Key.esc:
            # Stop listener
            stopAwait.append(True)
            mouse_listener.stop()
            pegarLista.pop()
            return False

        # Setup the listener threads

    keyboard_listener = KeyboardListener(on_press=on_press, on_release=on_release)
    mouse_listener = MouseListener(on_click=on_click)

    # Start the threads and join them so the script doesn't end early
    keyboard_listener.start()
    mouse_listener.start()

    return pegarLista, stopAwait