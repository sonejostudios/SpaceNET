# MAPS

############################################

init:
    $ cash_isc_rail2 = True


label isc_rail2:
    $ pnc_nodes_visible = True
    
    image isc_rail2 = imagemapsdir + "isc_rail2.png"
    
    #scene bgcolor
    #show screen notify("Industrial Space City")
    
    call show_space from _call_show_space_7
    
    show isc_rail2:
        pos (0,0)
    
    
    #show warningfloor:
    #    anchor (0.5,0.5)
    #    pos (570,240)
    #    rotate 90


    show propeller:
        pos (127,97)
        linear 10 rotate 180.0
        rotate 0
        repeat
    
    
    # set all variables for the map (nodes and path)
    $ nodeA = (395, 42)
    $ nodeB = (463, 139)
    $ nodeC = (682, 139)
    $ nodeD = (660, 25)

    $ nodeAA = (225, 100)
    $ nodeBB = (320, 157)
    $ nodeCC = (770, 70)
    $ nodeDD = (593, 348)

    $ pathA = (nodeA, nodeB, (0, 0), (0, 0), nodeAA, nodeBB, (0, 0), (0, 0))
    $ pathB = (nodeA, nodeB, (0, 0), (0, 0), nodeAA, nodeBB, (0, 0), (0, 0))
    $ pathC = ((0, 0), (0, 0), nodeC, nodeD, (0, 0), (0, 0), nodeCC, (0, 0))
    $ pathD = ((0, 0), (0, 0), nodeC, nodeD, (0, 0), (0, 0), nodeCC, (0, 0))
     
    $ pathAA = (nodeA, nodeB, (0, 0), (0, 0), nodeAA, nodeBB, (0, 0), (0, 0))
    $ pathBB = (nodeA, nodeB, (0, 0), (0, 0), nodeAA, nodeBB, (0, 0), (0, 0))
    $ pathCC = ((0, 0), (0, 0), nodeC, nodeD, (0, 0), (0, 0), nodeCC, (0, 0))
    $ pathDD = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)
    
    
    if playertype == "minidroid":
        show playercross:
            pos nodeB
            
            
    show spaceship2u:
        zoom 0.7
        rotate 90
        pos (-200, 300)
        linear 5 pos (-200, 300)
        linear 30 pos (1000, 300)
        repeat



label loop_isc_rail2:
    
    while True:

        # start "move through the map" loop
        call startpos from _call_startpos_34

        # do something at node?
        if exitpos == 1:
            $ startpos = 4
            call sound_door from _call_sound_door_84
            jump isc_rail1
                
                


        if exitpos == 2:
            if startpos == 2:
                if inventory_select == "":
                    call dialog_notfitting from _call_dialog_notfitting_2
                
                if inventory_select != "minidroid" and inventory_select != "":
                    call dialog_nosense from _call_dialog_nosense_10
                
                if inventory_select == "minidroid":
                    
                    m "I could use the minidroid... let's go! {w=2.5} {nw}"
                    call use_and_keep_item from _call_use_and_keep_item_15
                    call sound_connected from _call_sound_connected_27
                    with flash
                    show minidroid:
                        pos nodeB
                        linear 1 pos nodeC
                    pause 1
                    $ startpos = 3
                    $ playertype = "minidroid"
                    hide minidroid
                    show playercross:
                        pos nodeB
                    jump loop_isc_rail2
                    
            $ startpos = 2

            
        if exitpos == 3:
            if startpos == 3:
                #call sound_connected
                #with flash
                hide player
                show minidroid:
                    pos nodeC
                    linear 1 pos nodeB
                pause 1
                $ startpos = 2
                $ playertype = "player"
                hide minidroid
                hide playercross
                jump loop_isc_rail2
                
            $ startpos = 3
            
        
        if exitpos == 4:

            $ startpos = 11
            jump isc_rail1

            

        #exits routing "got to map and set position for next map"
        if exitpos == 11:
            if startpos == 11:
                if inventory_select == "":
                    m "This is a huge propeller! {w=2.0} {nw}"
                else:
                    call dialog_nosense from _call_dialog_nosense_11
            $ startpos = 11 

            
        if exitpos == 22:
            if startpos == 22:
                m "The view is absolutely amazing... {w=2.0} {nw}"
                if cash_isc_rail2 == True:
                    m "There are some coins!{w=2} {nw}"
                    call io_cash(+10) from _call_io_cash_11
                    $ cash_isc_rail2 = False

            $ startpos = 22

            
        if exitpos == 33:
            $ startpos = 33
            jump isc_rail5

            
        if exitpos == 44:
            $ startpos = 44
            call sound_door from _call_sound_door_85

            





