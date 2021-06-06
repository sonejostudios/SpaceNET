# MAPS

############################################

init:
    $ isc_crane_repared = False


label isc_rail5:
    
    image isc_rail5 = imagemapsdir + "isc_rail5.png"
    
    #scene bgcolor
    #show screen notify("Industrial Space City")
    
    call show_space from _call_show_space_10
    
    show isc_rail5:
        pos (0,0)
        
        
    show buttonscreen:
        pos (588, 259)
        rotate 90
    
    if isc_sysadmin_move == 1:
        show npc as sysadmin:
            pos (570, 290)
            rotate 40
            linear 1 rotate 50
            linear 1 rotate 40
            repeat
            

    
    if isc_crane_pos_x == 0 and isc_crane_pos_y == 0:
        if isc_sysadmin_move < 2:
            show crane:
                pos (700, 420)
                pause 1
                ease 0.2 pos (705, 420)
                ease 0.2 pos (700, 420)
                repeat
            
            # smoking
            show smoking1:
                pos (700, 243)
            show smoking2:
                pos (700, 243)
            show smoking3:
                pos (700, 243)
        
        else:
            show crane:
                pos (700, 420)
            

    
    
    #show warningfloor:
    #    anchor (0.5,0.5)
    #    pos (570,240)
    #    rotate 90

    show light:
        pos (76,121)
        
    show light as light2:
        pos (324,256)
        
    show light as light3:
        pos (712,85) 
    
    # set all variables for the map (nodes and path)
    $ nodeA = (125, 28)
    $ nodeB = (171, 131)
    $ nodeC = (171, 410)
    $ nodeD = (488, 410)

    $ nodeAA = (501, 21)
    $ nodeBB = (562, 259)
    $ nodeCC = (25, 411)
    $ nodeDD = (737, 189)

    $ pathA = (nodeA, nodeB, (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0))
    $ pathB = (nodeA, nodeB, nodeC, (0, 0), (0, 0), (0, 0), (0, 0), (0, 0))
    $ pathC = ((0, 0), nodeB, nodeC, nodeD, (0, 0), (0, 0), (0, 0), (0, 0))
    $ pathD = ((0, 0), (0, 0), nodeC, nodeD, nodeAA, nodeBB, (0, 0), (0, 0))
     
    $ pathAA = ((0, 0), (0, 0), (0, 0), nodeD, nodeAA, nodeBB, (0, 0), (0, 0))
    $ pathBB = ((0, 0), (0, 0), (0, 0), nodeD, nodeAA, nodeBB, (0, 0), (0, 0))
    $ pathCC = ((0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), nodeCC, (0, 0))
    $ pathDD = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)
    
    


label loop_isc_rail5:
    
    while True:
        
        
        if playertype == "player":
            $ pathD = ((0, 0), (0, 0), (0, 0), nodeD, nodeAA, nodeBB, (0, 0), (0, 0))
            $ pathB = (nodeA, nodeB, (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0))
        

        # start "move through the map" loop
        call startpos from _call_startpos_39

        # do something at node?
        if exitpos == 1:
            $ startpos = 22
            jump isc_rail4a

        if exitpos == 2:
            $ startpos = 2

            
        if exitpos == 3:
            $ startpos = 3
            
        
        if exitpos == 4:
            if startpos == 4:
                if inventory_select != "":
                    call dialog_nosense from _call_dialog_nosense_14
                    $ startpos = 4
                    jump loop_isc_rail5
                    
                if playertype == "player":
                    call dialog_notfitting from _call_dialog_notfitting_4
                
                
            $ startpos = 4

            

        #exits routing "got to map and set position for next map"
        if exitpos == 11: 
            $ startpos = 22
            jump isc_rail4b

            
        if exitpos == 22:
            if startpos == 22:
                if isc_sysadmin_move == 1:
                    if inventory_select == "":
                        if isc_crane_repared == False:
                            m "Hi! It's me again. {w=2.5} {nw}"
                            sysadmin "Hi. You again? {w=2.5} {nw}"
                            sysadmin "What do you want? {w=2.5} {nw}"
                            m "May I give you a hand? {w=2.5} {nw}"
                            sysadmin "Well... {w=1.5}Yes. {w=2.5} {nw}"
                            sysadmin "I'm trying to repair the controller of the space crane. {w=3.5} {nw}"
                            sysadmin "The light bulb of the light pipe seems to be broken. {w=3.5} {nw}"
                            sysadmin "Do you have an idea how to fix it? {w=3} {nw}"
                        else:
                            sysadmin "The light pipe is working again, but the crane is still blocked... {w=4.5} {nw}"
                            sysadmin "Please log in to the ISC remote control and move the crane to the city center. {w=5} {nw}"
                            sysadmin "I hope this will solve our problem! {w=3.5} {nw}"
                        
                    elif inventory_select == "bulb":
                        call use_item from _call_use_item_5
                        $ isc_crane_repared = True
                        
                        m "Here's a light bulb. {w=2.5} {nw}"
                        sysadmin "Great. Thanks! {w=2} {nw}"
                        sysadmin "Okay... could you help me more? {w=3} {nw}"
                        m "Sure. {w=1} {nw}"
                        sysadmin "Please, go to the terminal and log into the ISC system. {w=4} {nw}"
                        sysadmin "The command is: ssh isc{w=3} {nw}"
                        sysadmin "Please, set the crane position to the city center, at (x1, y1). {w=5} {nw}"
                        
                        call add_note("ISC remote access: ssh isc") from _call_add_note_6
                        
                        sysadmin "Thank you.{w=2} {nw}"
                        
                    elif inventory_select == "screwdriver":
                        sysadmin "I have my own screwdriver, thanks. {w=3} {nw}"
                        
                    elif inventory_select == "laser" or inventory_select == "dynamite" or inventory_select == "pick":
                        sysadmin "Are you crazy? I want to fix it, not destroy it completely! {w=4} {nw}"
                        
                    else:
                        call npc_dont_need_item(sysadmin) from _call_npc_dont_need_item_5
                        
                
                
                else:
                    call isc_crane_screen from _call_isc_crane_screen
                    
                    
            $ startpos = 22
            jump loop_isc_rail5

            
        if exitpos == 33:
            $ startpos = 33
            jump isc_rail2

            
        if exitpos == 44:
            $ startpos = 44


            


label isc_crane_screen:
     
    if isc_sysadmin_move <= 1:
        $ showtext = """
- ISC Space Crane Control -



! Crane Error !

---

Please contact the system administrator.


    """
    
    else:
        $ showtext = """
- ISC Space Crane Control -



The Space crane is operational.
Remote control only.

---

Crane position: [crane_pos_name] (x[isc_crane_pos_x], y[isc_crane_pos_y])

    """

    call info_panel from _call_info_panel_7
    
    return


