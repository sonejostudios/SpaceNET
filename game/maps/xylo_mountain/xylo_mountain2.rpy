# MAPS

############################################


label xylo_mountain2:
    
    #call atmo_nature
    
    image xylo_mountain2 = imagemapsdir + "xylo_mountain2.png"
    
    scene bgcolor
    show screen notify("Sacred lake of the mountains")
    
    image waves2 = SnowBlossom("images/wave.png", count=200, border=50, xspeed=(5), yspeed=(1), start=0, fast=True, horizontal=True)
    show waves2
    show xylo_mountain2
    
    
    show buttonscreen:
        pos (645, 200)
        rotate 90
        

    # check if spaceship is landing on this map or not
    # $ landing = False
    # $ landing = True
    #call landing_anim
    
    
    if sam_meeting_mountains == True:
        show npc:
            pos (65, 205)
            rotate 180
    
    
    # set all variables for the map (nodes and path)
    $ nodeA = (655, 447)
    $ nodeB = (619, 200)
    $ nodeC = (200, 88)
    $ nodeD = (64, 246)

    $ nodeAA = (190, 419)
    $ nodeBB = (518, 370)
    $ nodeCC = (765, 155)
    $ nodeDD = (768, 197)

    $ pathA = (nodeA, nodeB, (0, 0), (0, 0), (0, 0), nodeBB, (0, 0), (0, 0))
    $ pathB = (nodeA, nodeB, nodeC, (0, 0), (0, 0), nodeBB, (0, 0), (0, 0))
    $ pathC = ((0, 0), nodeB, nodeC, nodeD, (0, 0), (0, 0), (0, 0), (0, 0))
    $ pathD = ((0, 0), (0, 0), nodeC, nodeD, nodeAA, (0, 0), (0, 0), (0, 0))
     
    $ pathAA = ((0, 0), (0, 0), (0, 0), nodeD, nodeAA, nodeBB, (0, 0), (0, 0))
    $ pathBB = (nodeA, nodeB, (0, 0), (0, 0), nodeAA, nodeBB, (0, 0), (0, 0))
    $ pathCC = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)
    $ pathDD = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)


label loop_xylo_mountain2:

    while True:
        # start "move through the map" loop
        call startpos from _call_startpos_68

        # do something at node?
        if exitpos == 1: #if at node A
            
            $ landing = False
            $ startpos = 1     # stay in A
            
            #this needs to be here so it is set up even if playeralready in map
            if countdown_sec <= 0:
                $ countdown = False
                $ sam_meeting_mountains = False
            
            jump xylo_mountain1          # map loop to jump to
            
        if exitpos == 2:
            if startpos == 2:
                if inventory_select == "":
                    call xylo_mountain2_info from _call_xylo_mountain2_info
                elif inventory_select == "pick" or inventory_select == "shovel":
                    call sound_dig from _call_sound_dig_2
                    call use_and_keep_item from _call_use_and_keep_item_33
                    pause 1.5
                    call dialog_nothing from _call_dialog_nothing_62
                    $ inventory_select = ""
                else:
                    call dialog_nosense from _call_dialog_nosense_20
                
            $ startpos = 2

            
        if exitpos == 3:
            if startpos == 3: # cash
                if inventory_select == "":
                    if cash_xylo_mountain1 > 0:
                        m "There are some coins!{w=2} {nw}"
                        call io_cash(cash_xylo_mountain1) from _call_io_cash_18
                        $ cash_xylo_mountain1 = 0
                    else:
                        call dialog_nothing from _call_dialog_nothing_42
                    
                elif inventory_select == "pick" or inventory_select == "shovel":
                    call sound_dig from _call_sound_dig_3
                    call use_and_keep_item from _call_use_and_keep_item_34
                    pause 1.5
                    call dialog_nothing from _call_dialog_nothing_63
                    $ inventory_select = ""
                else:
                    call dialog_nosense from _call_dialog_nosense_21
                
            $ startpos = 3


            
        if exitpos == 4: # spacnet guy meeting
            
            if startpos == 4:
                if inventory_select == "":
                    if sam_meeting_mountains == True:
                        call xylo_mountain2_spacenet_guy from _call_xylo_mountain2_spacenet_guy
                    else:
                        call dialog_nothing from _call_dialog_nothing_43
                    
                elif inventory_select == "pick" or inventory_select == "shovel":
                    call sound_dig from _call_sound_dig_4
                    call use_and_keep_item from _call_use_and_keep_item_35
                    pause 1.5
                    call dialog_nothing from _call_dialog_nothing_64
                    $ inventory_select = ""
                
                else:
                    call dialog_nosense from _call_dialog_nosense_22
            
            $ startpos = 4

            

        #exits routing "got to map and set position for next map"
        if exitpos == 11:
            if startpos == 11:
                if inventory_select == "":
                    call dialog_nothing from _call_dialog_nothing_44       #if going out at AA
                
                elif inventory_select == "pick" or inventory_select == "shovel":
                    call sound_dig from _call_sound_dig_5
                    call use_and_keep_item from _call_use_and_keep_item_36
                    pause 1.5
                    $ inventory_select = ""
                    
                    if xylo_mountain_gem == True:
                        call take_gem from _call_take_gem_11
                        $ xylo_mountain_gem = False
                    else:
                        call dialog_nothing from _call_dialog_nothing_65
                    
                else:
                    call dialog_nosense from _call_dialog_nosense_23  
                
            $ startpos = 11    #go to CC

            
        if exitpos == 22:
            if startpos == 22:
                if inventory_select == "":
                    m "There is a lake. {w=2.5} {nw}"
                    m "It seems to be really deep. {w=2.5} {nw}"     
                
                elif inventory_select == "pick" or inventory_select == "shovel":
                    call sound_dig from _call_sound_dig_6
                    call use_and_keep_item from _call_use_and_keep_item_37
                    pause 1.5
                    call dialog_nothing from _call_dialog_nothing_66
                    $ inventory_select = ""
                    
                else:
                    call dialog_nosense from _call_dialog_nosense_24  
                
                
                
            $ startpos = 22

            
        if exitpos == 33:
            $ startpos = 33

            
        if exitpos == 44:
            $ startpos = 44






label xylo_mountain2_info:
    
    $ info_panel_symbol = ""
    $ showtext = """
- Sacred Lake -


This lake was an ancient sacred place.

A long time ago, a temple was built here, 
but it was abandonned and destroyed by winds and storms.

The legend says, there is a treasure. 
But nobody has found it until now. 
Does it really exist?

    """
    
    call info_panel from _call_info_panel_16 # in animations
    
    return



label xylo_mountain2_spacenet_guy:
    
    $ countdown_sec = -1
    
    if "star" in inventory:
        sam "Please go to 4n0nym0u5! {w=2}{nw}"
        return
    
    sam "Welcome back, [playername]! {w=2.5} {nw}"
    m "Welcome to what? {w=2.} {nw}"
    sam "You don't remember? The Rebel Alliance! {w=3} {nw}"
    m "Nope... {w=2.} {nw}"
    
    sam "Do you remember the IOnet?{w=1} No? {w=1}Okay...{w=1} {nw}"
    sam "The IOnet was a free knowledge network. {w=3} {nw}"
    sam "We are a group of scientists and we are close to figure out a new energy source. {w=5} {nw}"
    sam "Really powerful.{w=1} We wanted to use this free energy to create a new world.{w=4} A better one... {w=2}{nw}"
    sam "But the corrupt government stopped us and put in jail almost all of us. {w=5} {nw}"
    sam "And you were the guy who helped us restarting the network! {w=4} {nw}"
    m "I'm sorry, but I can't remember anything! {w=3} {nw}"
    sam "Okay...{w=1} maybe they gave you some serum to erase your memory... {w=4.5} {nw}"
    sam "...{w=1} {nw}"
    sam "Okay...{w=1} {nw}"
    sam "...{w=1} {nw}"
    
    sam "We are the Rebel Alliance, and we want to rebuild a new knowledge network. {w=5} {nw}"
    sam "It is called... {w=2} {nw}"
    sam "- SpaceNET -{w=2} {nw}"
    sam "...{w=2} {nw}"
    sam "And we need your help. {w=3} {nw}"
    sam "Please, accept! {w=3} {nw}"
    sam "This new free energy will help us all... {w=3} {nw}"
    sam "I'm sure, with it, we will achieve to bring your memory back. {w=4} {nw}"
    m "That sounds like a good deal... {w=3} {nw}"
    m "I accept.{w=1.5}{nw}"
    sam "This is great! {w=1.5} {nw}"
    
    
    if "star" not in inventory:
        sam "Here, I give you an official sign, the Star of the Rebel Alliance. {w=3.5} {nw}"
        $ inventory_select = "star"
        $ inventory.append("star")
        call sound_collect from _call_sound_collect_9
        call inventory_notify from _call_inventory_notify_7
        with flash
        m "Thank you very much.{w=1.5}{nw}"
        
    m "What can I do?{w=1.5}{nw}"
    
    sam "Please, go to 4n0nym0u5, our main hacker.{w=3} {nw}"
    sam "She will inform you about the software side of SpaceNET.{w=3} {nw}"
    sam "And how to install it on the SpaceNET nodes.{w=3} {nw}"
    sam "...{w=1} {nw}"
    sam "I will organize a secret meeting for you.{w=3} {nw}"
    sam "Wait...{w=1} {nw}"
    sam ".{w=0.5}.{w=0.5}.{w=0.5}.{w=0.5}.{w=0.5}.{w=0.5}.{w=0.5}.{w=0.5}.{w=0.5}.{w=0.5} {nw}"
    sam "Okay...{w=1} {nw}"
    
    sam "The meeting is set in space around [hacker_pos].{w=4} {nw}"
    
    sam "Go to space and flight to this location.{w=3} {nw}"
    sam "You will meet her there.{w=2} {nw}"
    sam "Good luck!{w=1.5} {nw}"
    
    #$ sam_hacker_meeting_text_workaround = "Meet 4n0nym0u5 in space around " + str(hacker_pos)
    call add_note(sam_hacker_meeting_text_workaround) from _call_add_note_11
    
    
    return
