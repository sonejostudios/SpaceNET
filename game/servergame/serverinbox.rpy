
init:
    default server_msglist = ["1. hello!", "2. a decryption tool for you", "", "", "", ""]
    
    $ inbox_new_message = ""
    
    $ server_mail_page = 1
    
label server_inbox:
    
    # for testing only
    #$ server_msglist = ["1. hello!", "2. a decryption tool for you", "", "", "", ""]
    
    
    $ showtext = """
    Inbox
    [ascii_line]
    
    """ + server_msglist[0] + """
    """ + server_msglist[1] + """
    """ + server_msglist[2] + """
    """ + server_msglist[3] + """
    """ + server_msglist[4]
    
    show text Text(showtext,text_align=termtext_align) at termtextpos
    
    call server_msgitems from _call_server_msgitems
    
    if server_itemchoice == 0:
        jump server_start
    
    if server_itemchoice == 1:
        jump server_hellomsg
    
    if server_itemchoice == 2:
        jump server_uncrypttoolmsg
    
    if server_itemchoice == 3:
        jump server_welldonemsg
    
    if server_itemchoice == 4:
        $ server_mail_page = 1 
        jump server_satellitemsg
    
    if server_itemchoice == 5:
        jump server_numpad_sam_msg

    jump server_menu
    
    


label notify_new_message:
    #pause 1
    #show screen notify("Inbox: new message received!")
    show screen notify("{image=images/inventory/letter_idle.png}")
    #"Inbox: new message received!"
    $ inbox_new_message = "*"
    call sound_connected from _call_sound_connected_40
    return




label server_hellomsg:
    $ showtext = """
    Hello!
    [ascii_line]
    
    How are you doing?
    
    Here is your inbox, you'll find all messages 
    sent to your private messaging system.
    
    - 4n0nym0u5 -
    """
    show text Text(showtext,text_align=termtext_align) at termtextpos
    
    menu:
        "back":
            call sound_beep from _call_sound_beep_48
            jump server_inbox
                
                
label server_uncrypttoolmsg:
    $ showtext = """
    Hello again!
    [ascii_line]
    
    I just sent you a decryption tool. 
    It is called uncrypter.
    You'll need to download and install it 
    properly to use it.
    
    I hope it will be useful to you!...
    Bye
    
    - 4n0nym0u5 -
    """
    show text Text(showtext,text_align=termtext_align) at termtextpos
    
    menu:
        "Download" if server_filelist[2] == "":
            call sound_beep from _call_sound_beep_49
            call server_download from _call_server_download
            $ server_filelist[2] = "3. uncrypter_install"
            $ server_fileitems = 3
            
            jump server_start
        "Back":
            call sound_beep from _call_sound_beep_50
            jump server_inbox
            
            
            
            
            
label server_download:
    show text "Do you want to download it?" at termtextpos2
    menu:
        "Download":
            call sound_beep from _call_sound_beep_51
            pass
        "Back":
            call sound_beep from _call_sound_beep_52
            jump server_start
                
    
    show text "Downloading...":
        pos (274,240)
    pause 1
    call server_progressbar from _call_server_progressbar_16
    show text "Download completed.":
        pos (274,240)
    pause 1

    
    return
    #jump server_start
    
    
    
label server_welldonemsg:
    $ showtext = """
    Well done!
    [ascii_line]
    
    I've seen you decrypted the file 
    sucessfully, that's great!
    
    Now insert a disk in the terminal and
    copy the SpaceNET software to the disk.
    
    Then, try to find the secret SpaceNET nodes
    and install the SpaceNET software on them.
    
    - 4n0nym0u5 -
    """
    show text Text(showtext,text_align=termtext_align) at termtextpos
    
    menu:
        "Back":
            #call notify_new_message
            #$ inbox_new_message = "*"
            #"Add new message with instructions about satellite"
            
            call sound_beep from _call_sound_beep_53
            jump server_inbox
            
            
            
            
label server_satellitemsg:
    
    if server_mail_page == 1:
        $ showtext = """
    Satellite io-11
    [ascii_line]
    
    Hello [playername],
    
    I have an important mission for you.
    In order to accelerate the speed of SpaceNET,
    we will need to have our own satellite.
    
    I figured out a satellite from the A.R.K Corp.,
    which could help us with this task. But first,
    we need to hack it and send it into a new 
    orbit. The satellite is named io11.
    You'll find your mission schedule on page 2.
    
    Important: Call me first on a proxy line.
    Here is the number: 003007
     
    Good luck.
    
    - 4n0nym0u5 -
    """
    
        
    
    if server_mail_page == 2:
        $ showtext = """
    Satellite io-11
    [ascii_line]
    
    You mission: 
    
    1. Locate the statellite named io11 
       (use 'locate io11' in the terminal).
    2. Dock on the satellite. You'll need 
       a spaceship with a docking hatch.
    3. Hack the computer, set a new password 
       and enable remote control.
    4. Go out the satellite and log into the 
       stellite's remote control via a terminal.
    5. Restart the satellite to disconnect it.
    6. Set a new orbit. Set it to X=350 and Y=150.
    7. Send the satellite to new orbit.
    8. Connect to the SpaceNET Network.

    """    
    
    show text Text(showtext,text_align=termtext_align) at termtextpos
    

    
    menu:
        "Page 1":
            $ server_mail_page = 1
            call sound_beep from _call_sound_beep_54
            jump server_satellitemsg
        "Page 2":
            $ server_mail_page = 2  
            
            call sound_beep from _call_sound_beep_55
            jump server_satellitemsg 
        "Back":
            call add_note("Terminal: locate io11\nio11 set new orbit to: X=350, Y=150\n4n0nym0u5 proxy phone number: 003007") from _call_add_note_12
            
            call sound_beep from _call_sound_beep_56
            jump server_inbox





label server_numpad_sam_msg:
    $ showtext = """
    Important meeting
    [ascii_line]
    
    Hi!
    
    Here is Sam. 
    I have an secret information for you.
    It is too dangerous to send it to you 
    via the terminal.
    
    Please meet me at the bar of Xylo village.
    See you there,
        
    - Sam -
    """
    show text Text(showtext,text_align=termtext_align) at termtextpos
    
    # set sam numpad mission to "sam will tell you the numpad code"
    $ sam_numpad_mission = 1
    
    menu:
        "Back":
            #call notify_new_message
            #$ inbox_new_message = "*"
            #"Add new message with instructions about satellite"
            
            call sound_beep from _call_sound_beep_57
            jump server_inbox
