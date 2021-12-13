from pynput.keyboard import Key, Controller
keyboard = Controller()

class commandTransform:
    x01 = '\x01'; x02 = '\x02';x03 = '\x03';x04 = '\x04';x05 = '\x05';x06 = '\x06';x07 = '\x07';x08 = '\x08';x09 = '\x09';x10 = '\x10';x11 = '\x11';x12 = '\x12';x13 = '\x13';x14 = '\x14';x15 = '\x15';x16 = '\x16';x17 = '\x17';x18 = '\x18';x19 = '\x19';x20 = '\x20'
    #this exist because i couldn't find where get this attr from neither how to get this using a string

def tabChanger():
    with keyboard.pressed(Key.alt_l):
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)

def solver(key, pressedKey):

    if(pressedKey == 'Key.shift'):
        if 'Key.' in key:
            with keyboard.pressed(Key.shift):
                key = key.replace("Key.", "")
                contextVAR = getattr(keyboard._Key, key)
                keyboard.press(contextVAR)
                keyboard.release(contextVAR)
        else:
            with keyboard.pressed(Key.shift):
                if '\\' in key:
                    key = key.replace("'", "")
                    key = key.replace("\\", "")
                    keyforcommand = getattr(commandTransform, key)
                    keyboard.press(keyforcommand)
                    keyboard.release(keyforcommand)
                else:
                    key = key.replace("'", "")
                    keyboard.press(key)
                    keyboard.release(key)

    elif(pressedKey == 'Key.alt'):
        if 'Key.' in key:
            with keyboard.pressed(Key.alt):
                key = key.replace("Key.", "")
                contextVAR = getattr(keyboard._Key, key)
                keyboard.press(contextVAR)
                keyboard.release(contextVAR)
        else:
            with keyboard.pressed(Key.alt):
                if '\\' in key:
                    key = key.replace("'", "")
                    key = key.replace("\\", "")
                    keyforcommand = getattr(commandTransform, key)
                    keyboard.press(keyforcommand)
                    keyboard.release(keyforcommand)
                else:
                    key = key.replace("'", "")
                    keyboard.press(key)
                    keyboard.release(key)

    elif (pressedKey == 'Key.alt_l'):
        if 'Key.' in key:
            with keyboard.pressed(Key.alt_l):
                key = key.replace("Key.", "")
                contextVAR = getattr(keyboard._Key, key)
                keyboard.press(contextVAR)
                keyboard.release(contextVAR)
        else:
            with keyboard.pressed(Key.alt_l):
                if '\\' in key:
                    key = key.replace("'", "")
                    key = key.replace("\\", "")
                    keyforcommand = getattr(commandTransform, key)
                    keyboard.press(keyforcommand)
                    keyboard.release(keyforcommand)
                else:
                    key = key.replace("'", "")
                    keyboard.press(key)
                    keyboard.release(key)

    elif (pressedKey == 'Key.alt_r'):
        if 'Key.' in key:
            with keyboard.pressed(Key.alt_r):
                key = key.replace("Key.", "")
                contextVAR = getattr(keyboard._Key, key)
                keyboard.press(contextVAR)
                keyboard.release(contextVAR)
        else:
            with keyboard.pressed(Key.alt_r):
                if '\\' in key:
                    key = key.replace("'", "")
                    key = key.replace("\\", "")
                    keyforcommand = getattr(commandTransform, key)
                    keyboard.press(keyforcommand)
                    keyboard.release(keyforcommand)
                else:
                    key = key.replace("'", "")
                    keyboard.press(key)
                    keyboard.release(key)

    elif (pressedKey == 'Key.alt_gr'):
        if 'Key.' in key:
            with keyboard.pressed(Key.alt_gr):
                key = key.replace("Key.", "")
                contextVAR = getattr(keyboard._Key, key)
                keyboard.press(contextVAR)
                keyboard.release(contextVAR)
        else:
            with keyboard.pressed(Key.alt_gr):
                if '\\' in key:
                    key = key.replace("'", "")
                    key = key.replace("\\", "")
                    keyforcommand = getattr(commandTransform, key)
                    keyboard.press(keyforcommand)
                    keyboard.release(keyforcommand)
                else:
                    key = key.replace("'", "")
                    keyboard.press(key)
                    keyboard.release(key)

    elif (pressedKey == 'Key.caps_lock'):
        if 'Key.' in key:
            with keyboard.pressed(Key.caps_lock):
                key = key.replace("Key.", "")
                contextVAR = getattr(keyboard._Key, key)
                keyboard.press(contextVAR)
                keyboard.release(contextVAR)
        else:
            with keyboard.pressed(Key.caps_lock):
                if '\\' in key:
                    key = key.replace("'", "")
                    key = key.replace("\\", "")
                    keyforcommand = getattr(commandTransform, key)
                    keyboard.press(keyforcommand)
                    keyboard.release(keyforcommand)
                else:
                    key = key.replace("'", "")
                    keyboard.press(key)
                    keyboard.release(key)

    elif (pressedKey == 'Key.cmd_l'):
        if 'Key.' in key:
            with keyboard.pressed(Key.cmd_l):
                key = key.replace("Key.", "")
                contextVAR = getattr(keyboard._Key, key)
                keyboard.press(contextVAR)
                keyboard.release(contextVAR)
        else:
            with keyboard.pressed(Key.cmd_l):
                if '\\' in key:
                    key = key.replace("'", "")
                    key = key.replace("\\", "")
                    keyforcommand = getattr(commandTransform, key)
                    keyboard.press(keyforcommand)
                    keyboard.release(keyforcommand)
                else:
                    key = key.replace("'", "")
                    keyboard.press(key)
                    keyboard.release(key)

    elif (pressedKey == 'Key.cmd'):
        if 'Key.' in key:
            with keyboard.pressed(Key.cmd):
                key = key.replace("Key.", "")
                contextVAR = getattr(keyboard._Key, key)
                keyboard.press(contextVAR)
                keyboard.release(contextVAR)
        else:
            if '\\' in key:
                with keyboard.pressed(Key.cmd):
                    key = key.replace("'", "")
                    key = key.replace("\\", "")
                    keyforcommand = getattr(commandTransform, key)
                    keyboard.press(keyforcommand)
                    keyboard.release(keyforcommand)
            else:
                with keyboard.pressed(Key.cmd):
                    key = key.replace("'", "")
                    keyboard.press(key)
                    keyboard.release(key)

    elif (pressedKey == 'Key.cmd_r'):
        if 'Key.' in key:
            with keyboard.pressed(Key.cmd_r):
                key = key.replace("Key.", "")
                contextVAR = getattr(keyboard._Key, key)
                keyboard.press(contextVAR)
                keyboard.release(contextVAR)
        else:
            with keyboard.pressed(Key.cmd_r):
                if '\\' in key:
                    key = key.replace("'", "")
                    key = key.replace("\\", "")
                    keyforcommand = getattr(commandTransform, key)
                    keyboard.press(keyforcommand)
                    keyboard.release(keyforcommand)
                else:
                    key = key.replace("'", "")
                    keyboard.press(key)
                    keyboard.release(key)

    elif (pressedKey == 'Key.ctrl'):
        if 'Key.' in key:
            with keyboard.pressed(Key.ctrl):
                key = key.replace("Key.", "")
                contextVAR = getattr(keyboard._Key, key)
                keyboard.press(contextVAR)
                keyboard.release(contextVAR)
        else:
            with keyboard.pressed(Key.ctrl):
                if '\\' in key:
                    key = key.replace("'", "")
                    key = key.replace("\\", "")
                    keyforcommand = getattr(commandTransform, key)
                    keyboard.press(keyforcommand)
                    keyboard.release(keyforcommand)
                else:
                    key = key.replace("'", "")
                    keyboard.press(key)
                    keyboard.release(key)

    elif (pressedKey == 'Key.ctrl_l'):
        if 'Key.' in key:
            with keyboard.pressed(Key.ctrl_l):
                key = key.replace("Key.", "")
                contextVAR = getattr(keyboard._Key, key)
                keyboard.press(contextVAR)
                keyboard.release(contextVAR)
        else:
            with keyboard.pressed(Key.ctrl_l):
                if '\\' in key:
                    key = key.replace("'","")
                    key =  key.replace("\\","")
                    keyforcommand = getattr(commandTransform, key)
                    keyboard.press(keyforcommand)
                    keyboard.release(keyforcommand)
                else:
                    key = key.replace("'", "")
                    keyboard.press(key)
                    keyboard.release(key)

    elif (pressedKey == 'Key.ctrl_r'):
        if 'Key.' in key:
            with keyboard.pressed(Key.ctrl_r):
                key = key.replace("Key.", "")
                contextVAR = getattr(keyboard._Key, key)
                keyboard.press(contextVAR)
                keyboard.release(contextVAR)
        else:
            with keyboard.pressed(Key.ctrl_r):
                if '\\' in key:
                    key = key.replace("'", "")
                    key = key.replace("\\", "")
                    keyforcommand = getattr(commandTransform, key)
                    keyboard.press(keyforcommand)
                    keyboard.release(keyforcommand)
                else:
                    key = key.replace("'", "")
                    keyboard.press(key)
                    keyboard.release(key)

    else:
        if "Key." not in key:
            key = key.replace("'", "")
            keyboard.press(key)
            keyboard.release(key)


