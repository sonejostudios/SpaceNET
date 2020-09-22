# MAPS

init:
    $ megaship_cell2 = False
    $ megaship_cell3 = False


############################################
label megaship_aeration:
    
    call atmo_spaceship_hum from _call_atmo_spaceship_hum_4
    
    image megaship_aeration = imagemapsdir + "megaship_aeration.png"
    
    scene megaship_aeration
    show screen notify("prison aeration")
    
    show bgcolor behind megaship_aeration    
    
    
    # set all variables for the map (nodes and path)
    $ nodeA = (293, 38)
    $ nodeB = (293, 173)
    $ nodeC = (293, 313)
    $ nodeD = (293, 445)

    $ nodeAA = (556, 450)
    $ nodeBB = (49, 72)
    $ nodeCC = (100, 100)
    $ nodeDD = (74, 152)

    $ pathA = (nodeA, nodeB, nodeC, nodeD, (0, 0), (0, 0), (0, 0), (0, 0))
    $ pathB = (nodeA, nodeB, nodeC, nodeD, (0, 0), (0, 0), (0, 0), (0, 0))
    $ pathC = (nodeA, nodeB, nodeC, nodeD, (0, 0), (0, 0), (0, 0), (0, 0))
    $ pathD = (nodeA, nodeB, nodeC, nodeD, nodeAA, (0, 0), (0, 0), (0, 0))
     
    $ pathAA = ((0, 0), (0, 0), (0, 0), nodeD, nodeAA, (0, 0), (0, 0), (0, 0))
    $ pathBB = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)
    $ pathCC = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)
    $ pathDD = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)


label loop_megaship_aeration:
    
    while True:
        # start "move through the map" loop
        call startpos from _call_startpos_64

        # do something at node?
        if exitpos == 1:
            if startpos == 1:
                call sound_screw from _call_sound_screw_8
                $ startpos = 33 
                jump megaship_cell 
            $ startpos = 1
            
        if exitpos == 2:
            if startpos == 2:
                if megaship_cell2 == False:
                    if inventory_select == "laser":
                        
                        m "I can cut the areation grid with this laser tool. {w=3.0} {nw}"
                        m "Let's do it! {w=1.5} {nw}"
                        call use_and_keep_item from _call_use_and_keep_item_24
                        call sound_electroshock from _call_sound_electroshock_18
                        with flash
                        $ megaship_cell2 = True
                
                    else:
                        if inventory_select == "screwdriver":
                            call dialog_nosense from _call_dialog_nosense_29
                        else:
                            call dialog_closed from _call_dialog_closed_31
                        m "How to cut this metal grid? {w=3} {nw}"
                else:
                    call sound_screw from _call_sound_screw_9
                    $ startpos = 33 
                    jump megaship_cell2
                    
                
            $ startpos = 2

            
        if exitpos == 3:
            if startpos == 3:
                if megaship_cell3 == False:
                    if inventory_select == "laser":
                        
                        call use_and_keep_item from _call_use_and_keep_item_25
                        call sound_electroshock from _call_sound_electroshock_19
                        with flash
                        $ megaship_cell3 = True
                        m "Great tool, this laser. {w=2.0} {nw}"
                
                    else:
                        if inventory_select == "screwdriver":
                            call dialog_nosense from _call_dialog_nosense_30
                        else:
                            call dialog_closed from _call_dialog_closed_32
                        m "I'll need a metal cutting tool to open this. {w=3} {nw}"
                else:
                    call sound_screw from _call_sound_screw_10
                    $ startpos = 33 
                    jump megaship_cell3
                    
            $ startpos = 3

            
        if exitpos == 4:
            $ startpos = 4

            

        #exits routing "got to map and set position for next map"
        if exitpos == 11:
            call sound_screw from _call_sound_screw_11    
            $ startpos = 1       
            jump megaship_prison   
            
        if exitpos == 22:
            if startpos == 22:
                call dialog_closed from _call_dialog_closed_33
            $ startpos = 22
            

            
        if exitpos == 33:
            $ startpos = 33

            
        if exitpos == 44:
            $ startpos = 44



