# Enter script code
# wrap_selection 
# get keys 
wrap_glob = store.get_global_value("wrap")
wrap_open = min(wrap_glob)
wrap_close = max(wrap_glob)
# below needed to get working in some apps, otherwise 
# clipboard.get_selection() quicker/better 
# get clipboard/selection 
#try: 
    #clip_board = clipboard.get_clipboard() 
#except: 
    #clip_board = "" 
#keyboard.send_keys("<ctrl>+x") 
#time.sleep(0.01) 
#try: 
    #selection = clipboard.get_clipboard() 
#except: 
    #selection = "" 

# clipboard won't update if selection empty so set 
#if clip_board == selection: 
    #selection = "" # problem if clipboard and selection are the same 

#clipboard.fill_clipboard(clip_board) # <- replace this
#keyboard.send_keys(clip_board)
#for c in clip_board:
   #keyboard.send_keys("<shift>+<left>")
#keyboard.send_keys("<ctrl>+x") 
    
# output
#keyboard.send_keys(wrap_open+selection+wrap_close+"<left>")
keyboard.send_keys(wrap_open+wrap_close+"<left>")
#for s in selection:
#   keyboard.send_keys("<shift>+<left>")

#del selection, clip_board
 
