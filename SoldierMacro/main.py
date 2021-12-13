import PySimpleGUI as sg
from modules import ReadWriteFile
from modules import ExecMacro
from modules import ListenMacro


listaFinal = []

sg.theme('DarkBlue')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('MacroTest')],
            [sg.Button('listen')],
            [sg.Text('Number of times to repeat'), sg.InputText(key="-repeatTimes-", default_text=1,size=(5,5))],
            [sg.Checkbox('Custom time between events', default=False, key="-customTimeCheck-",change_submits = True, enable_events=True), sg.InputText(key="-customTime-",visible=False,size=(5,5))],
            [sg.Button('Ok')],
            [sg.Button('Save Macro', key="-saveButton-"),sg.Button('Cancel', key="-cancelButton-", visible=False), sg.InputText(key="-inputSaveFileName-", size=(15,15), visible=False), sg.Button('Confirm', key="-confirmButton-", visible=False)],
            [sg.FileBrowse(target="-folderText-",change_submits=True), sg.InputText("", key="-folderText-"), sg.Button('Apply')]]

# Create the Window
window = sg.Window('Macro', layout)
# Event Loop to process "events" and get the "values" of the inputs


while True:
    event, values = window.read()

    if values['-customTimeCheck-'] == True:
        window["-customTime-"].update(visible=True)
    else:
        window["-customTime-"].update(visible=False)

    if event == sg.WIN_CLOSED: # if user closes window or clicks cancel
        break
    if event == 'listen':
        listaFinal = ListenMacro.keylist()

    if event == '-saveButton-':
        print("k")
        window["-cancelButton-"].update(visible=True)
        window["-inputSaveFileName-"].update(visible=True)
        window["-confirmButton-"].update(visible=True)
        window["-saveButton-"].update(visible=False)
        print("Saved")

    if event == '-confirmButton-' and values["-inputSaveFileName-"]:
        ReadWriteFile.createMacro(listaFinal,values["-inputSaveFileName-"] +".txt")
        window["-inputSaveFileName-"].update(visible=False)
        window["-confirmButton-"].update(visible=False)
        window["-cancelButton-"].update(visible=False)
        window["-saveButton-"].update(visible=True)

    if event == '-cancelButton-':
        window["-inputSaveFileName-"].update(visible=False)
        window["-confirmButton-"].update(visible=False)
        window["-cancelButton-"].update(visible=False)
        window["-saveButton-"].update(visible=True)

    if event == "Apply":
       listaFinal = ReadWriteFile.readMacro(values["-folderText-"])
    if event == 'Ok':
        window.minimize()
        print(values['-repeatTimes-'])
        if values['-repeatTimes-'] != "":
            for i in range(int(values['-repeatTimes-'])):
                if values ['-customTime-'] != "":
                    ExecMacro.executarChaves(listaFinal,values['-customTime-'])
                else:
                    ExecMacro.executarChaves(listaFinal)
        print('Done')

window.close()


# problemas conhecido #
# cmd + E não abre a pasta inicialmente, depois que o cmd abre, ele não aceita mais o comando, é necessario apertar cmd > cmd + e
# ctr + a não funciona para tudo, as vezes dois clicks rapidos é mais efetivo.
#

