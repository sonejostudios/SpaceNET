# MAPS

init:
    $ asteroid_brokenwall1 = False
    
    $ asteroid_cord_at_box = True


############################################
label asteroid2_spaceship:
    
    $ pnc_nodes_visible = True
    
    #stop music fadeout 1.0
    #stop atmo fadeout 1.0
    call atmo_deep_ambiance from _call_atmo_deep_ambiance_5
    call music_xylo_building from _call_music_xylo_building_1
    
    
    image broken_spaceship = imagemapsdir + "broken_spaceship.png"
    
    scene bgcolor

    show screen notify("Spaceship Wreck")
    
    show broken_spaceship

    

    
    # check if spaceship is landing on this map or not
    #$ landing = False
    # $ landing = True
    #call landing_anim
    
    
    # set all variables for the map (nodes and path)
    $ nodeA = (368, 140)
    $ nodeB = (327, 231)
    $ nodeC = (513, 306)
    $ nodeD = (431, 268)
    
    $ nodeAA = (633, 286)
    $ nodeBB = (211, 168)
    $ nodeCC = (179, 245)
    $ nodeDD = (236, 321)
    
    $ pathA = (nodeA, nodeB, nodeC, nodeD, (0,0), (0,0), (0,0), (0,0))
    $ pathB = (nodeA, nodeB, nodeC, nodeD, (0,0), (0,0), (0,0), (0,0))
    $ pathC = (nodeA, nodeB, nodeC, nodeD, nodeAA, (0,0), (0,0), (0,0))
    $ pathD = (nodeA, nodeB, nodeC, nodeD, (0,0), (0,0), (0,0), (0,0))
    
    $ pathAA = ((0,0), (0,0), nodeC, (0,0), nodeAA, (0,0), (0,0), (0,0))
    $ pathBB = ((0,0), nodeB, (0,0), (0,0), (0,0), nodeBB, nodeCC, nodeDD)
    $ pathCC = ((0,0), nodeB, (0,0), (0,0), (0,0), nodeBB, nodeCC, nodeDD)
    $ pathDD = ((0,0), (0,0), (0,0), (0,0), (0,0), nodeBB, nodeCC, nodeDD)





label loop_asteroid2_spaceship:
    
    while True:
        
        #broken wall
        if asteroid_brokenwall1 == False:
            show brokenwall closed behind shadow:
                pos (306, 229)
                rotate 90
        if asteroid_brokenwall1 == True:
            show brokenwall open behind shadow:
                pos (306, 229)
                rotate 90
            $ pathB = (nodeA, nodeB, nodeC, nodeD, (0,0), nodeBB, nodeCC, (0,0))
            
        
        
        
        
        # start "move through the map" loop
        call startpos from _call_startpos_89 


        # do something at node?
        if exitpos == 1:
            $ startpos = 4
            jump asteroid2_rightdown

            
            
            
        if exitpos == 2:
            if asteroid_brokenwall1 == False:
                if inventory_select == "":
                    m "The metal wall is broken. {w=3.5} {nw}"
                    m "I can see through.\nThere is the spaceship's cockpit.{w=4} {nw}"
                
                elif inventory_select == "laser":
                    m "I could use the laser to widen the hole. \nLet's go!{w=3.5} {nw}"
                    call use_and_keep_item from _call_use_and_keep_item_42
                    call sound_electroshock from _call_sound_electroshock_15
                    pause 1.5
                    call sound_connected from _call_sound_connected_32
                    with flash
                    $ asteroid_brokenwall1 = True
                    
                    $ pathB = (nodeA, nodeB, nodeC, nodeD, (0,0), nodeBB, nodeCC, nodeDD)
                
                else:
                    call dialog_nosense from _call_dialog_nosense_38
                
            $ startpos = 2
            
            
        if exitpos == 3:
            if startpos == 3:
                m "This spaceship is wrecked. {w=2.5} {nw}"
            $ startpos = 3


            
        if exitpos == 4:
            if startpos == 4:
                if inventory_select == "":
                    m "These boxes block the door to the cockpit. {w=3.5} {nw}"
                    m "I can't go through. {w=3} {nw}"
                    if asteroid_cord_at_box == True:
                        m "There is a cord tighten around this box. {w=3.5} {nw}"
                
                elif inventory_select == "knife":
                    if asteroid_cord_at_box == True:
                        call use_and_keep_item from _call_use_and_keep_item_43
                        m "Let's try to cut this cord. {w=2.5} {nw}"
                        call take_item("cord") from _call_take_item_23
                        if inventory_notify == "cord":
                            $ asteroid_cord_at_box = False
                    else:
                        call dialog_nosense from _call_dialog_nosense_39
                else:
                    call dialog_nosense from _call_dialog_nosense_40
            
            $ startpos = 4

            

        if exitpos == 11:    
            if startpos == 11:
                if inventory_select == "module":
                    m "This spaceship is totally broken. {w=3} {nw}"
                    m "I can't repaire it, even with this hyperspace module. {w=4} {nw}"
                
                else:
                    m "There should be the hyperspace module. {w=3} {nw}"
                    m "But it is missing! {w=2} {nw}"
                    m "I guess it flew away during the accident... {w=3.5} {nw}"
                
            $ startpos = 11   

            
        if exitpos == 22:
            if startpos == 22:
                call dialog_nothing from _call_dialog_nothing_77
            $ startpos = 22

            
        if exitpos == 33:
            if startpos == 33:
                m "This is the cockpit. {w=2} {nw}"
                m "Everything is broken... {w=2} {nw}"
            $ startpos = 33

            
        # spaceship
        if exitpos == 44:
            if startpos == 44:
                if "shovel" not in inventory:
                    m "Hey, there is a shovel! {w=2} {nw}"
                    call take_item("shovel") from _call_take_item_24
                else:
                    call dialog_nothing from _call_dialog_nothing_78
            $ startpos = 44

                





