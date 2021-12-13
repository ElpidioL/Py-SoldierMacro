import os


class listDeChaves:
    def __init__(self, chave, tempo):
        self.chave = chave
        self.tempo = tempo

keyRd = []
timeRd = []
listaFinalChaves = []
def createMacro(macroKeys,name):
    save_path = './MacroScripts'
    completeNamePath = os.path.join(save_path, name)
    fi = open(completeNamePath, "w")
    for st in macroKeys:
        fi.write(st.chave + ";" + str(st.tempo) + ";")
    fi.close()

def readMacro(folder):
    fi = open(folder, "r")
    x = fi.read().split(";")
    x.pop()
    for idx, value in enumerate(x):
        if idx % 2 == 0:
            keyRd.append(value)
        else:
            timeRd.append(value)

    for idx, value in enumerate(keyRd):
        listaFinalChaves.append(listDeChaves(keyRd[idx],timeRd[idx]))

    fi.close()
    return listaFinalChaves