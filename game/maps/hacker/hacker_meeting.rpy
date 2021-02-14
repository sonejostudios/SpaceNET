  
    
# hacker meeting
label hacker_meeting:
    $ spaceship_pos = hacker_pos
    
    #"[hacker_in_prison]"
    
    
    if hacker_in_prison >= 1:
        #call dialog_nothing
        return
        
    if hacker_space_meeting_done == True:
        return
    
    show spaceship3s at inspace_idle:
        pos (400, -100)
        linear 5 pos (400, 110)
    
    pause 6

    hacker "Hi...{w=1.5} {nw}"
    
    hacker "Please identify yourself.{w=2} {nw}"
    hacker "How is your name?{w=2} {nw}"
    m "My name is [playername].{w=2} {nw}"
    hacker "Please show me a sign.{w=3} {nw}"
    #hacker "I'm waiting.{w=1}.{w=1}.{w=1}.{w=1}.{w=1}.{w=1}.{w=1} {nw}"
    
    #if inventory_select != "star":
    
    $ x = 0
    while x == 0:
        menu:
            "Here, the star of the rebel alliance." if "star" in inventory:
                
                $ inventory_select = "star"
                call sound_connected from _call_sound_connected
                call use_and_keep_item from _call_use_and_keep_item
                m "Here, the star of the rebel alliance.{w=3} {nw}"
                m "I'm part of the crew.{w=2} {nw}"
                $ inventory_select = ""
                #call sound_connected from _call_sound_connected
                #with flash
                pause 2
                hacker "Good. I was waiting for you.{w=2.5} {nw}"

                hacker "Okay... first, we need to install the new SpaceNET software on all SpaceNet nodes.{w=6} {nw}"
                hacker "I will transfer this software to your private terminal account.{w=4} {nw}"
                hacker "Of course, as an encrypted file!{w=3.5} {nw}"
                hacker "Go to a terminal type 'login'.{w=3} {nw}"
                hacker "Then log in with your name.{w=3} {nw}"
                hacker "The password is 'freedom'.{w=3} {nw}"
                
                $ terminal_login_text = "Login ID: " + playername + ", Password: freedom"
                call add_note(terminal_login_text) from _call_add_note
                #call add_note("Terminal login password: freedom")
                
                hacker "Once you are in, go to your mailbox.{w=2.5} I'll send you more instructions.{w=3}{nw}"
                hacker "Copy it to a disc as soon as you have it.{w=4} {nw}"
                
                hacker "Now, let's go back...{w=3}{nw}"
                
                $ x = 1
                
                #$ inventory_select = ""
            

            
            "I don't know what you are talking about...":
                m "I don't know what you are talking about...{w=2} {nw}"
                hacker "Hm, that's bad.{w=1.5} {nw}"
                hacker "I don't trust you, sorry.{w=2} {nw}"
                $ x = 1
            
            "It was a mistake, sorry....":
                m "It was a mistake, sorry...{w=2} {nw}"
                hacker "Okay, bye.{w=2} {nw}"
                $ x = 1
        
        

      
            
    
    show spaceship3s at inspace_idle:
        pos (400, 110)
        linear 5 pos (400, -110)
    
    pause 5
    
    $ hacker_space_meeting_done = True
    # (this is to False in cockpit)
    
    return



