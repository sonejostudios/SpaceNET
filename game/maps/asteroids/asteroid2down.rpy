# MAPS

init:
    $ asteroid2down_solarpanel = False
    $ asteroid2down_lift = False


############################################
label asteroid2_down:
    $ pnc_nodes_visible = True
    
    call atmo_deep_ambiance from _call_atmo_deep_ambiance_2
    
    
    image asteroid2 = imagemapsdir + "asteroid2.png"
    
    scene bgcolor
    call show_space from _call_show_space_24
    #show screen notify("Asteroid 2")
    
    show asteroid2: #at inspace_idle
        pos (60,-460)
        
        
        
    $ asteroidzoom = renpy.random.random()*0.7 + 0.1
    show asteroid_small behind orbitmeter, text_planet, spaceshipside, asteroid2:
        zoom asteroidzoom
        rotate 0
        ypos 300
        xpos 900
        linear 10 xpos -200 rotate -560
        repeat
        
    $ asteroidzoom2 = renpy.random.random()*0.7 + 0.1
    show asteroid_small2 as asteroid_small2 behind orbitmeter, text_planet, spaceshipside, asteroid2:
        zoom asteroidzoom2
        rotate 0
        ypos 400
        xpos 1200
        linear 13 xpos -200 rotate -460
        repeat
        


        
    show asteroid_small as asteroid_small3:
        pos (227, 164)
        rotate 0
        
    # hidden lift
    if asteroid2down_lift == True:
        show lift_top:
            pos (571, 200)
            zoom 0.8
        show asteroid_small2b:
            pos (562, 230)
    else:
        show asteroid_small2 as asteroid_lift:
            pos (581, 210)
            rotate 180
        
        
    if asteroid2down_solarpanel == True:
        show solarpanel:
            pos (367, 75)
            rotate -45
    
    
    # check if spaceship is landing on this map or not
    $ landing = False
    # $ landing = True
    #call landing_anim
    
    
    # set all variables for the map (nodes and path)
    $ nodeA = (550, 31)
    $ nodeB = (400, 100)
    $ nodeC = (271, 185)
    $ nodeD = (773, 90)
    
    $ nodeAA = (570, 160)
    $ nodeBB = (670,240)
    $ nodeCC = (400,460)
    $ nodeDD = (315,240)
    
    $ pathA = (nodeA, nodeB, nodeC, nodeD, nodeAA, (0,0), (0,0), (0,0))
    $ pathB = (nodeA, nodeB, nodeC, nodeD, nodeAA, (0,0), (0,0), (0,0))
    $ pathC = (nodeA, nodeB, nodeC, nodeD, nodeAA, (0,0), (0,0), (0,0))
    $ pathD = (nodeA, nodeB, nodeC, nodeD, nodeAA, (0,0), (0,0), (0,0))
    
    $ pathAA = (nodeA, nodeB, nodeC, nodeD, nodeAA, (0,0), (0,0), (0,0))
    $ pathBB = (nodeA, nodeB, nodeC, nodeD, (0,0), (0,0), (0,0), (0,0))
    $ pathCC = (nodeA, nodeB, nodeC, nodeD, (0,0), (0,0), (0,0), (0,0))
    $ pathDD = (nodeA, nodeB, nodeC, nodeD, (0,0), (0,0), (0,0), (0,0))
    
    
    if startpos == 11:
        $ inventory_select = "spacesuit"
        call inventory_notify from _call_inventory_notify_9





label loop_asteroid2_down:
    
    while True:
        
        # start "move through the map" loop
        call startpos from _call_startpos_82 


        # do something at node?
        if exitpos == 1:
            $ startpos = 3
            jump asteroid2
            
            
            
        if exitpos == 2: # asteroid2 down
            if startpos == 2:
                if asteroid2down_solarpanel == False:
                    $ inventory_notify = ""
                    call asteroid_dig(1) from _call_asteroid_dig
                    if inventory_notify == "pick":
                        m "There is something. {w=3.5} {nw}"
                        m "But the pick is useless against this asteroid dust. {w=3.5} {nw}"
                    
                    elif inventory_notify == "shovel":
                        show solarpanel behind pathnodeB:
                            pos (367, 75)
                            rotate -45
                            alpha 0
                            linear 3 alpha 1
                        pause 2
                        $ asteroid2down_solarpanel = True
                        
                        m "There is a solar panel under the dust! {w=3.5} {nw}"
                        m "Something is using power here. But what? {w=3.5} {nw}"
                        
                    else:
                        pass
                else:
                    if inventory_select == "":
                        m "This is a solar panel. {w=2.5} {nw}"
                        m "It seems to be working. {w=2.5} {nw}"
                    else:
                        call dialog_nosense from _call_dialog_nosense_33
                
            $ startpos = 2
            
            
        if exitpos == 3:
            if startpos == 3:
                if inventory_select == "":
                    m "Rocks, rocks, rocks... {w=2.5} {nw}"
                    m "Everywhere rocks... {w=2.5} {nw}"
                else:
                    call asteroid_dig(0) from _call_asteroid_dig_1
            $ startpos = 3

            
        if exitpos == 4:
            $ startpos = 1
            jump asteroid2_rightdown

            

        if exitpos == 11:
            if startpos == 11:
                #"asteroid2down_lift [asteroid2down_lift]"
                if asteroid2down_lift == False:
                    $ inventory_notify = ""
                    call asteroid_dig(1) from _call_asteroid_dig_2
                    if inventory_notify == "pick":
                        with hpunch
                        call sound_earthquake from _call_sound_earthquake_3
                        
                        hide asteroid_lift
                        show lift_top:
                            pos (571, 200)
                            zoom 0.8
                        
                        show asteroid_small2b:
                            pos (562, 230)
                        
                        $ asteroid2down_lift = True
                            
                    elif inventory_notify == "shovel":
                        call dialog_nothing from _call_dialog_nothing_67
                    
                    else:
                        m "Except rocks. {w=2.5} {nw}"
                        
                else:
                    if asteroid2down_solarpanel == True and asteroid2right_solarpanel == True:
                        $ startpos = 1
                        $ liftpos = 3
                        call sound_door from _call_sound_door_178
                        jump asteroid_lift1
                    
                    else:
                        m "There is a small cabin! {w=3} {nw}"
                        m "What is it doing here on this lost asteroid? {w=4} {nw}"
                        m "That's really weird! {w=2.5} {nw}"
                        call dialog_closed from _call_dialog_closed_51
           
            
            $ startpos = 11   

            
        if exitpos == 22:
            $ startpos = 22

            
        if exitpos == 33:
            $ startpos = 33

            
        # spaceship
        if exitpos == 44:
            $ startpos = 44

                





