
init:
    default server_filelist = ["1. help.txt", "2. SpaceNET.xxx", "", ""]


label server_files:

    $ showtext = """
    Files
    [ascii_line]
    
    """ + server_filelist[0] + """
    """ + server_filelist[1] + """
    """ + server_filelist[2] + """
    """ + server_filelist[3]
    
    
    show text Text(showtext,text_align=termtext_align) at termtextpos
    
    call server_fileitems
    
    if server_itemchoice == 0:
        jump server_start
    if server_itemchoice == 1:
        jump server_helpfile
    if server_itemchoice == 2:
        jump server_file2
    if server_itemchoice == 3:
        if server_filelist[2] == "3. uncrypter_install":
            call server_install
            $ server_filelist[2] = "3. uncrypter"
            jump server_start
        else:
            jump server_uncrypter
    
    
    jump server_menu


label server_helpfile:
    $ showtext = """
    Help File
    [ascii_line]
    
    You have a file folder and an inbox folder.
    
    In the file folder are all files saved
    on your server.
    
    In the inbox folder are all messages
    sent to your private messaging system.
    """
    show text Text(showtext,text_align=termtext_align) at termtextpos
    
    menu:
        "back":
            call sound_beep
            jump server_files
                
                
                
label server_file2:
    if server_filelist[1] == "2. SpaceNET.xxx":
    
        $ showtext = """
    Encrypted File
    [ascii_line]
    
    You need an encryption tool to decrypt it."""
        show text Text(showtext,text_align=termtext_align) at termtextpos
        
        menu:
            "decrypt with uncrypter" if server_filelist[2] == "3. uncrypter":
                $ server_filelist[1] = "2. SpaceNET"

                call sound_beep
                pause 1
                call sound_connected
                
                $ server_msglist[2] = "3. well done!"
                
                #call notify_new_message
                $ inbox_new_message = "*"
                
                jump server_files
                
            "back":
                call sound_beep
                jump server_files
                
    else:
        $ showtext = """
    SpaceNET Readme
    [ascii_line]
    
    TOP SECRET.
    
    Copy this software to a disc. 
    This will also create an  autostart for the 
    installer. As soon as the disc is ready, just 
    insert it to a computer. SpaceNET will 
    automatically install and configure itself.
    
    Keep in mind, this is a top secret software, 
    keep it always by yourself.
    
    Once the software is installed on a computer
    node, it will show informations about the 
    SpaceNET network. It will also create a bridge
    to the terminal, type 'spacenet' in a terminal 
    to access it.
    
    Good luck.
    """
    
        show text Text(showtext,text_align=termtext_align) at termtextpos
        
        #"[server_filelist]"

        while True:
            menu:
                "copy to disc" if spacenet_copied == False:
                    call sound_beep
                    if inventory_select == "spacenet":
                        call use_and_keep_item
                        call server_progressbar
                        $ inventory_select = ""
                        call sound_connected
                        with flash
                        $ spacenet_copied = True
                        m "Yes, it works!{w=2.5} {nw}"
                        m "Now the SpaceNET software is on the disc.{w=3} {nw}"
                        m "I can't wait to install it everywhere! {w=3} {nw}"
                        
                        $ inbox_new_message = "*"
                        $ server_msglist[3] = "4. satellite"
                    else:
                        m "I need to insert a disc first.{w=3} {nw}"
                    
                    
                    
                "back":
                    call sound_beep

                    jump server_files
        

label server_install:
    show text "Do you want to install it?" at termtextpos2
    menu:
        "install":
            call sound_beep
            pass
        "back":
            call sound_beep
            jump server_start
                
    
    show text "Installing..." at termtextpos2
    pause 1
    call server_progressbar
    show text "Install completed." at termtextpos2
    pause 1
    
    return
    
    
    
label server_uncrypter:
    $ showtext = """
    Uncrypter
    [ascii_line]
    
    With uncrypter, you can decrypt files.
    """
    
    show text Text(showtext,text_align=termtext_align) at termtextpos
    
    menu:
        "back":
            call sound_beep
            jump server_files


