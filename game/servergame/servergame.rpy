init:
    #$ server_fileitems = 2
    #$ server_msgitems = 2
    $ ascii_line = "---------------------------------------------"



label server_menu:
    $ inventory_select = ""
    
    $ server_itemchoice = 0
    
    if inbox_new_message == "*":
        call notify_new_message from _call_notify_new_message_1
    
    menu:
        #"start":
        #    call sound_beep
        #    jump server_start
        "files":
            call sound_beep from _call_sound_beep_58
            jump server_files
        "[inbox_new_message]inbox[inbox_new_message]":
            call sound_beep from _call_sound_beep_59
            $ inbox_new_message = ""
            jump server_inbox
        "exit":
            call sound_beep from _call_sound_beep_60
            jump terminal
        
    return
    

label server_fileitems:
    $ inventory_select = ""
    
    $ server_itemchoice = 0
    menu:
        "1":
            call sound_beep from _call_sound_beep_61
            $ server_itemchoice = 1
        "2":
            call sound_beep from _call_sound_beep_62
            $ server_itemchoice = 2
        
        "3" if server_filelist[2] !="":
            call sound_beep from _call_sound_beep_63
            $ server_itemchoice = 3
        
        "back":
            call sound_beep from _call_sound_beep_64
            $ server_itemchoice = 0
            return
            #jump server_start
            
    return
    
    
    
label server_msgitems:
    $ inventory_select = ""
    
    $ server_itemchoice = 0
    menu:
        "1":
            call sound_beep from _call_sound_beep_65
            $ server_itemchoice = 1
        "2":
            call sound_beep from _call_sound_beep_66
            $ server_itemchoice = 2
        
        "3" if server_msglist[2] != "":
            call sound_beep from _call_sound_beep_67
            $ server_itemchoice = 3
        
        "4" if server_msglist[3] != "":
            call sound_beep from _call_sound_beep_68
            $ server_itemchoice = 4
            
        "5" if server_msglist[4] != "":
            call sound_beep from _call_sound_beep_69
            $ server_itemchoice = 5
        
        "back":
            call sound_beep from _call_sound_beep_70
            $ server_itemchoice = 0
            return
            #jump server_start
            
    return    


label server_start:
    
    $ showtext = """
    Welcome
    [ascii_line]
    
    Welcome to your private terminal, [playername].
    
    What do you want to do?
    """
    
    show text Text(showtext,text_align=termtext_align) at termtextpos

    jump server_menu
    
    
    
label server_progressbar:
    
    $ server_progress = 0
    
    while server_progress <= 100:
        
        $ showtext = "Progress: [server_progress] %"
        show text showtext: #at termtextpos2
            pos (274,240)
        pause 0.01
        $ server_progress += 1
    
    pause 1
    call sound_connected from _call_sound_connected_41
        
    return
    
