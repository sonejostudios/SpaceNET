# MAPS

############################################
label asteroid4:
    $ pnc_nodes_visible = True
    
    stop music fadeout 1.0
    
    call atmo_spaceship_station from _call_atmo_spaceship_station_9
    
    image asteroid4 = imagemapsdir + "asteroid4.png"
    
    scene bgcolor
    call show_space from _call_show_space_28
    show screen notify("Asteroid 4")
    
    show asteroid4 at inspace_idle
    
    show asteroid_small:
        rotate 0
        anchor (0.5, 0.5)
        zoom 0.6
        around (380, 240)
        radius 360
        angle 0
        linear 20 clockwise circles 1 rotate -360*4
        repeat


    if module_in_orbit == False and "magnetcord" not in inventory:
        show cord_throw2:
            pos (450, 170)
            
    if module_in_orbit == False and "module" not in inventory and spaceship_broken == True:
        show hyperspace_module:
            pos (450, 170)
            zoom 0.3
        


    # check if spaceship is landing on this map or not
    # $ landing = False
    # $ landing = True
    call landing_anim from _call_landing_anim_10
    
    
    # set all variables for the map (nodes and path)
    $ nodeA = (290, 68)
    $ nodeB = (450, 200)
    $ nodeC = (612, 164)
    $ nodeD = (344, 386)
    
    $ nodeAA = (400,25)
    $ nodeBB = (670,240)
    $ nodeCC = (400,460)
    $ nodeDD = (315,240)
    
    $ pathA = (nodeA, nodeB, (0,0), nodeD, (0,0), (0,0), (0,0), nodeDD)
    $ pathB = (nodeA, nodeB, nodeC, nodeD, (0,0), (0,0), (0,0), nodeDD)
    $ pathC = ((0,0), nodeB, nodeC, nodeD, (0,0), (0,0), (0,0), nodeDD)
    $ pathD = (nodeA, nodeB, nodeC, nodeD, (0,0), (0,0), (0,0), nodeDD)
    
    $ pathAA = (nodeA, nodeB, nodeC, nodeD, (0,0), (0,0), (0,0), nodeDD)
    $ pathBB = (nodeA, nodeB, nodeC, nodeD, (0,0), (0,0), (0,0), nodeDD)
    $ pathCC = (nodeA, nodeB, nodeC, nodeD, (0,0), (0,0), (0,0), nodeDD)
    $ pathDD = (nodeA, nodeB, nodeC, nodeD, (0,0), (0,0), (0,0), nodeDD)
    
    if landing == True:
        $ inventory_select = "spacesuit"
        call inventory_notify from _call_inventory_notify_12





label loop_asteroid4:
    
    while True:
        # start "move through the map" loop
        call startpos from _call_startpos_86 


        # do something at node?
        if exitpos == 1:
            if startpos == 1:
                if inventory_select == "":
                    m "The view is beautiful. {w=2.5} {nw}"
                else:
                    call asteroid_dig(0) from _call_asteroid_dig_13
            $ startpos = 1   
            
            
            
        if exitpos == 2:
            if startpos == 2:
                if inventory_select == "":
                    if module_in_orbit == False and "magnetcord" not in inventory:
                        m "There is my cord with the magnet! {w=2.5} {nw}"
                        call take_item("magnetcord") from _call_take_item_20
                        if inventory_notify == "magnetcord":
                            hide cord_throw2
                    
                    elif module_in_orbit == False and "module" not in inventory and spaceship_broken == True:
                        m "And the hyperspace module! {w=2.5} {nw}"
                        call take_item("module") from _call_take_item_21
                        if inventory_notify == "module":
                            hide hyperspace_module
                        
                    else:    
                        m "This is a quite small asteroid. {w=2.5} {nw}"
                
                else:
                    call asteroid_dig(0) from _call_asteroid_dig_14
            
            $ startpos = 2
            
            
        if exitpos == 3:
            if startpos == 3:
                if inventory_select == "":
                    m "A small asteroid is in orbit around us. {w=3.5} {nw}"
                    m "Beautiful! {w=2.5} {nw}"
                else:
                    call asteroid_dig(0) from _call_asteroid_dig_15
            $ startpos = 3

            
        if exitpos == 4:
            if startpos == 4:
                if inventory_select == "":
                    call dialog_nothing from _call_dialog_nothing_74
                elif inventory_select == "pick" or inventory_select == "shovel":
                    call asteroid_dig(1) from _call_asteroid_dig_16
                    if asteroid4_gem == True:
                        call take_gem from _call_take_gem_13
                        $ asteroid4_gem = False
                    else:
                        call dialog_nothing from _call_dialog_nothing_75
                else:
                    call dialog_nosense from _call_dialog_nosense_36
            $ startpos = 4

            

        if exitpos == 11:     
            $ startpos = 11   

            
        if exitpos == 22:
            $ startpos = 22

            
        if exitpos == 33:
            $ startpos = 33

            
        # spaceship
        if exitpos == 44:
            $ startpos = 44
            #call sound_door
            call takeoff_anim("withmenu") from _call_takeoff_anim_12 # go to takeoff
            $ pnc_nodes_visible = True
            
            # straight to space
            if takeoftospace == True:
                $ takeoftospace = False
                $ space_anim = True
                $ pnc_nodes_visible = False
                jump space

            
            # to surface
            if landing == True:
                $ shippos = (1200,1200) # set position in surface engine
                jump surface
                





