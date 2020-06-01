# MAPS

############################################


init:
    $ xylo_mine_used_dynamite = False
    $ xylo_mine_used_dynamite_dialog = False



screen xylo_mine_earthquake:
    
    timer 7 repeat True action Jump("xylo_mine_level1_earthquake")


label xylo_mine_level1:
    
    stop music
    
    #call music_xylo_mine
    
    call atmo_deep_ambiance
    
    
    image xylo_mine_level1 = imagemapsdir + "xylo_mine1.png"
    image xylo_mine_level2 = imagemapsdir + "xylo_mine2.png"
    
    scene bgcolor
    show screen notify("high security area")
    
    show xylo_mine_level1
    
    
    $ showtext = ""

            

    # check if spaceship is landing on this map or not
    #$ landing = False
    # $ landing = True
    #call landing_anim
    
    
    # set all variables for the map (nodes and path)
    $ nodeA = (407, 53)
    $ nodeB = (421, 193)
    $ nodeC = (130, 79)
    $ nodeD = (718, 59)

    $ nodeAA = (100, 338)
    $ nodeBB = (470, 410)
    $ nodeCC = (656, 292)
    $ nodeDD = (704, 295)

    $ pathA = (nodeA, nodeB, (0, 0), (0, 0), nodeAA, (0, 0), (0, 0), (0, 0))
    $ pathB = (nodeA, nodeB, nodeC, nodeD, nodeAA, (0, 0), (0, 0), (0, 0))
    $ pathC = ((0, 0), nodeB, nodeC, (0, 0), (0, 0), (0, 0), (0, 0), (0, 0))
    $ pathD = ((0, 0), nodeB, (0, 0), nodeD, nodeAA, (0, 0), (0, 0), (0, 0))
     
    $ pathAA = (nodeA, nodeB, (0, 0), nodeD, nodeAA, (0, 0), (0, 0), (0, 0))
    $ pathBB = (nodeA, nodeB, (0, 0), (0, 0), (0, 0), nodeBB, (0, 0), (0, 0))
    $ pathCC = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)
    $ pathDD = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)
    


label loop_xylo_mine_level1:
    
    if xylo_mine_used_dynamite == True:
        $ pathA = (nodeA, nodeB, (0, 0), (0, 0), nodeAA, nodeBB, (0, 0), (0, 0))
        $ pathB = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, (0, 0), (0, 0))
        
        
        
    if xylo_mine_used_dynamite == True:
        show xylo_mine_level2:
            align (1.0,1.0)
     
    if xylo_mine_used_dynamite == True:
        show screen xylo_mine_earthquake
    
    if xylo_mine_used_dynamite == False:
        hide screen xylo_mine_earthquake
        
    
    while True:

        # start "move through the map" loop
        call startpos

        # do something at node?
        if exitpos == 1:
            $ startpos = 2
            $ xylo_mine_used_dynamite_dialog = False
            
            $ xylo_mine_level1_button1 = False
            $ xylo_mine_level1_button2 = False
            $ xylo_mine_level1_button3 = False
            
            hide screen xylo_mine_earthquake
            $ multiposx = 0
            $ multiposy = 2
            call sound_door
            jump xylo_mine_multimap1
            
            

        if exitpos == 2:
            if startpos == 2:
                if xylo_mine_used_dynamite == False and inventory_select == "dynamite":
                    m "Okay, let's go! {w=2} {nw}"
                    call sound_ignition
                    show player:
                        linear 0.5 pos nodeC
                    if shadow_enable == 1:
                        show shadow:
                            linear 0.5 pos nodeC
                    $ startpos = 3
                    call use_item
                    m "3... {w=1} 2... {w=1} 1... {w=1}{nw}"
                    #pause 3
                    call sound_explosion
                    $ xylo_mine_used_dynamite = True
                    with flash
                    jump xylo_mine_level1
                    
                
                if xylo_mine_used_dynamite == False and inventory_select == "":
                    m "There is a lot of stones... {w=2} {nw}"
                    m "It looks like they have fallen from the ceiling... {w=3} {nw}"
                    m "Now the way is blocked! {w=2} {nw}"
                    
                if xylo_mine_used_dynamite == False and inventory_select == "pick":
                    m "There are to many stones, this is just to much work now! {w=3} {nw}"
                    jump loop_xylo_mine_level1
                    
                if xylo_mine_used_dynamite == False and inventory_select != "":
                    call dialog_nosense
                
                
            $ startpos = 2
            

        if exitpos == 3:
            if startpos == 3:
                call dialog_nothing
            $ startpos = 3

        if exitpos == 4:
            if startpos == 4:
                if "pick" not in inventory:
                    m "There is a pick! {w=2} {nw}"
                    call take_item("pick")
                else:    
                    call dialog_nothing
                
            $ startpos = 4

        #exits
        if exitpos == 11: 
            if startpos == 11:
                call xylo_mine_level1_info     
            $ startpos = 11    

        if exitpos == 22:
            hide screen xylo_mine_earthquake
            $ startpos = 1
            call sound_door
            jump xylo_mine_spacenet
                
            $ startpos = 22


        if exitpos == 33:
            $ startpos = 33

            
        if exitpos == 44:
            $ startpos = 44




label xylo_mine_level1_info:
    
    $ info_panel_symbol = "quake"
    $ showtext = """
    
    
Danger! Seismic Activity!
    
This mine is abandonned and really dangerous.

Do not mine here, 
this could trigger small earthquakes!

You stay at your own risk.
    """
    
    call info_panel # in animations

    return




label xylo_mine_level1_earthquake:
            
    call sound_earthquake
    with hpunch
    
    if xylo_mine_used_dynamite_dialog == False:
        $ xylo_mine_used_dynamite_dialog = True
        m "I think the explosion was too loud... {w=2} {nw}"
        m "And it has triggered seismic activity! {w=2} {nw}"
        m "I definitely should't stay here longer... {w=2} {nw}"
        
    
    
    if showtext != "":
        call xylo_mine_level1_info

    jump loop_xylo_mine_level1
    
