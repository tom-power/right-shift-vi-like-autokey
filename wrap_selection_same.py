def select(string):
    for s in string:
        keyboard.send_keys("<shift>+<left>")
        if False: # work out start of line prob
            return False
    return True

def remove_wrap(string):
    keyboard.send_keys("<delete>")
    keyboard.send_keys("<delete>")
    keyboard.send_keys("<backspace>")
    keyboard.send_keys(string)    
    
# find out what's selected is empty by reselecting acccording to what's on the clipboard
def selection_empty(string):
    oc = False
    # get clipboard
    try:
        cb = clipboard.get_clipboard()
    except:
        cb = ""
    # unselect the select back same number a argument                 
    keyboard.send_keys("<right>")
    if select(string) == False: # todo: doesn't work at start of line
        oc = True
    keyboard.send_keys("<ctrl>+c")    
    time.sleep(0.01)
    # get new selection
    try:
        sl = clipboard.get_clipboard()
    except:
        sl = ""

    if cb != sl:        
        oc = True        
        keyboard.send_keys("<right>")        
    # restore clipboard and return
    clipboard.fill_clipboard(cb)
    del cb, sl    
    return oc