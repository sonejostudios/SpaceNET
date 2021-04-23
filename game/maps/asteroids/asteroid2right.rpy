# MAPS

init:
    $ asteroid2right_solarpanel = False
    
    $ rock_asteroid2right = False


############################################
label asteroid2_right:
    $ pnc_nodes_visible = True
    
    call atmo_deep_ambiance from _call_atmo_deep_ambiance_7
    
    
    image asteroid2 = imagemapsdir + "asteroid2.png"
    
    scene bgcolor
    call show_space from _call_show_space_31
    #show screen notify("Asteroid 2")
    
    show asteroid2: #at inspace_idle
        pos (-740,20)
        
        
    $ asteroidzoom = renpy.random.random()*0.7 + 0.2
    show asteroid_small behind orbitmeter, text_planet, spaceshipside, asteroid2:
        zoom asteroidzoom
        rotate 0
        ypos 100
        xpos 900
        linear 10 xpos -200 rotate -560
        repeat
        
    $ asteroidzoom2 = renpy.random.random()*0.7 + 0.2
    show asteroid_small as asteroid_small2 behind orbitmeter, text_planet, spaceshipside, asteroid2:
        zoom asteroidzoom2
        rotate 0
        ypos 240
        xpos 1200
        linear 13 xpos -200 rotate -460
        repeat
        

    # breakable rock
    if rock_asteroid2right == True:
        show asteroid_small2b:
            pos (400, 294)
            rotate -65
    else:
        show asteroid_small as asteroid_small3_breakable:
            pos (421, 274)
            rotate 90
        
        
    show asteroid_small2 as asteroid_small4:
        pos (422, 394)
        rotate 100
        zoom 0.8
        
    show asteroid_small as asteroid_small5:
        pos (100, 240)
        rotate 200
        zoom 0.7
        
    
    
    if asteroid2right_solarpanel == True:
        show solarpanel:
            pos (206, 290)

    
    
    # check if spaceship is landing on this map or not
    $ landing = False
    # $ landing = True
    #call landing_anim
    
    
    # set all variables for the map (nodes and path)
    $ nodeA = (30, 380)
    $ nodeB = (207, 332)
    $ nodeC = (362, 276)
    $ nodeD = (300, 450)
    
    $ nodeAA = (400,25)
    $ nodeBB = (670,240)
    $ nodeCC = (400,460)
    $ nodeDD = (315,240)
    
    $ pathA = (nodeA, nodeB, nodeC, nodeD, (0,0), (0,0), (0,0), (0,0))
    $ pathB = (nodeA, nodeB, nodeC, nodeD, (0,0), (0,0), (0,0), (0,0))
    $ pathC = (nodeA, nodeB, nodeC, nodeD, (0,0), (0,0), (0,0), (0,0))
    $ pathD = (nodeA, nodeB, nodeC, nodeD, (0,0), (0,0), (0,0), (0,0))
    
    $ pathAA = (nodeA, nodeB, nodeC, nodeD, (0,0), (0,0), (0,0), (0,0))
    $ pathBB = (nodeA, nodeB, nodeC, nodeD, (0,0), (0,0), (0,0), (0,0))
    $ pathCC = (nodeA, nodeB, nodeC, nodeD, (0,0), (0,0), (0,0), (0,0))
    $ pathDD = (nodeA, nodeB, nodeC, nodeD, (0,0), (0,0), (0,0), (0,0))





label loop_asteroid2_right:
    
    while True:
        
        # start "move through the map" loop
        call startpos from _call_startpos_91 


        # do something at node?
        if exitpos == 1:
            $ startpos = 4
            jump asteroid2
            
            
            
        if exitpos == 2: # asteroid2 right
            if startpos == 2:
                if asteroid2right_solarpanel == False:
                    $ inventory_notify = ""
                    call asteroid_dig(1) from _call_asteroid_dig_21
                    if inventory_notify == "pick":
                        m "There is something inside the ground. {w=3.5} {nw}"
                        m "But I need another tool to get rid of this asteroid dust! {w=4.5} {nw}"
                    
                    elif inventory_notify == "shovel":
                        show solarpanel behind pathnodeB:
                            pos (206, 290)
                            alpha 0
                            linear 3 alpha 1
                        pause 2
                        $ asteroid2right_solarpanel = True
                        
                        m "Hey, there is a solar panel! {w=3.5} {nw}"
                        m "For what is it used? {w=2.5} {nw}"
                        
                    else:
                        pass
                else:
                    if inventory_select == "":
                        m "This is a solar panel. {w=2.5} {nw}"
                        m "But I have no clue for what it is for. {w=3.5} {nw}"
                    else:
                        call dialog_nosense from _call_dialog_nosense_42
                
            $ startpos = 2
            
            
        if exitpos == 3:
            if startpos == 3:
                #"rock_asteroid2right [rock_asteroid2right]"
                if rock_asteroid2right == False:
                    if inventory_select == "":
                        m "Rocks everywhere... {w=2.5} {nw}"
                        m "This one looks slightly different than the others. {w=4.0} {nw}"

                    else:
                        call asteroid_dig(1) from _call_asteroid_dig_22
                        if inventory_notify == "pick":
                            with hpunch
                            call sound_earthquake from _call_sound_earthquake_5
                            
                            hide asteroid_small3_breakable
                            show asteroid_small2b:
                                pos (400, 294)
                                rotate -65
                            
                            $ rock_asteroid2right = True
                                
                        elif inventory_notify == "shovel":
                            call dialog_nothing from _call_dialog_nothing_79
                        
                        else:
                            call dialog_nothing from _call_dialog_nothing_80
                else:
                    
                    if "asteroid" not in inventory:
                        m "I could take one of these rocks. {w=3} {nw}"
                        call take_item("asteroid") from _call_take_item_25
                    
                    else:
                        call asteroid_dig(0) from _call_asteroid_dig_23
            
            $ startpos = 3

            
        if exitpos == 4:
            $ startpos = 3
            jump asteroid2_rightdown

            

        if exitpos == 11:     
            $ startpos = 11   

            
        if exitpos == 22:
            $ startpos = 22

            
        if exitpos == 33:
            $ startpos = 33

            
        # spaceship
        if exitpos == 44:
            $ startpos = 44

                





