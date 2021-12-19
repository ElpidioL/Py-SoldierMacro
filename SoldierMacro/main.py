import PySimpleGUI as sg
from modules import ReadWriteFile
from modules import ExecMacro
from modules import ListenMacro


listaFinal = []

sg.theme('DarkBlue')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Button('Play', key='-play-', tooltip='Start the Macro script'), sg.Text('Repeat', tooltip='Times to repeat the Macro'), sg.InputText(key="-repeatTimes-", default_text=1,size=(5,5), tooltip='Times to repeat the Macro'),sg.Checkbox('Custom time between events', default=False, key="-customTimeCheck-",change_submits = True, enable_events=True, tooltip='Change the time between events (it will prevent the default)'), sg.InputText(key="-customTime-",visible=False,size=(5,5), tooltip='Change the time between events (it will prevent the default)')],
            [sg.Button('Record',key='-record-',tooltip="Start recording a new Macro"),sg.Button('Save Macro', key="-saveButton-", tooltip='Save the current Macro script to load it later'),sg.Button('Cancel', key="-cancelButton-", visible=False, tooltip='Dont save anyomore'), sg.InputText(key="-inputSaveFileName-", size=(15,15), visible=False, tooltip='Name of the file to be created (no extension needed)'), sg.Button('Confirm', key="-confirmButton-", visible=False, tooltip='Save the Macro')],
            [sg.FileBrowse(target="-folderText-",change_submits=True, tooltip='Select a Macro to load'), sg.InputText("", key="-folderText-", tooltip='Folder with the Macro to be loaded'), sg.Button('Apply', key='-applyMacro-', tooltip='Apply the Macro to be able to run it')],
            [sg.Text('Stop Key', tooltip='Key that will be used to stop during recording and playing'),sg.Combo(['esc','end','f12','pause'], readonly=True, default_value='esc', key="-stopKey-", size = 8, tooltip='Key that will be used to stop during recording and playing')]]

# Create the Window
window = sg.Window('Macro', layout, size=(800,300), resizable=True )
# Event Loop to process "events" and get the "values" of the inputs




while True:
    event, values = window.read()

    if values['-customTimeCheck-'] == True:
        window["-customTime-"].update(visible=True)
    else:
        window["-customTime-"].update(visible=False)

    if event == sg.WIN_CLOSED: # if user closes window or clicks cancel
        break
    if event == '-record-':
        window.minimize()
        listaFinal = ListenMacro.keylist()

    if event == '-saveButton-':
        window["-cancelButton-"].update(visible=True)
        window["-inputSaveFileName-"].update(visible=True)
        window["-confirmButton-"].update(visible=True)
        window["-saveButton-"].update(visible=False)

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

    if event == "-applyMacro-":
        if values["-folderText-"]:
            listaFinal = ReadWriteFile.readMacro(values["-folderText-"])
        else:
            sg.popup_ok('You need to choose a folder first')
    if event == '-play-':
        window.minimize()
        if values['-repeatTimes-'] != "":
            for i in range(int(values['-repeatTimes-'])):
                if values ['-customTime-'] != "":
                    ExecMacro.executarChaves(listaFinal,values['-stopKey-'],values['-customTime-'])
                else:
                    ExecMacro.executarChaves(listaFinal, values['-stopKey-'])
        sg.popup_ok('Macro finished')

window.close()


# problemas conhecido #
# cmd + E não abre a pasta inicialmente, depois que o cmd abre, ele não aceita mais o comando, é necessario apertar cmd > cmd + e
# ctr + a não funciona para tudo, as vezes dois clicks rapidos é mais efetivo.
#

