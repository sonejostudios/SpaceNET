# MAPS

init:
    $ rock_asteroid3up = False


############################################
label asteroid3_up:
    $ pnc_nodes_visible = True
    
    
    image asteroid3 = imagemapsdir + "asteroid3.png"
    
    scene bgcolor
    call show_space from _call_show_space_26
    #show screen notify("Asteroid 3")
    
    show asteroid3: #at inspace_idle
        pos (20, 0)
        
        
    $ asteroidzoom = renpy.random.random()*0.7 + 0.2
    show asteroid_small behind orbitmeter, text_planet, spaceshipside, asteroid3:
        zoom asteroidzoom
        rotate 0
        ypos 120
        xpos 900
        linear 10 xpos -200 rotate -560
        repeat
        
    $ asteroidzoom2 = renpy.random.random()*0.7 + 0.2
    show asteroid_small as asteroid_small2 behind orbitmeter, text_planet, spaceshipside, asteroid3:
        zoom asteroidzoom2
        rotate 0
        ypos 260
        xpos 1200
        linear 13 xpos -200 rotate -460
        repeat
        
        
    
    show asteroid_small as asteroid_small3:
        pos (130, 280)
        rotate 180
        zoom 0.8
    
    # breakable rock
    if rock_asteroid3up == True:
        show asteroid_small2b:
            pos (500, 390)
            rotate -55
    else:
        show asteroid_small2 as asteroid_small4:
            pos (532, 380)
    
    
    
        

    # check if spaceship is landing on this map or not
    $ landing = False
    # $ landing = True
    #call landing_anim
    
    
    # set all variables for the map (nodes and path)
    $ nodeA = (350, 450)
    $ nodeB = (165, 299)
    $ nodeC = (291, 55)
    $ nodeD = (480, 370)
    
    $ nodeAA = (400,25)
    $ nodeBB = (670,240)
    $ nodeCC = (400,460)
    $ nodeDD = (315,240)
    
    $ pathA = (nodeA, nodeB, nodeC, nodeD, (0,0), (0,0), (0,0), nodeDD)
    $ pathB = (nodeA, nodeB, nodeC, nodeD, (0,0), (0,0), (0,0), nodeDD)
    $ pathC = (nodeA, nodeB, nodeC, (0,0), (0,0), (0,0), (0,0), nodeDD)
    $ pathD = (nodeA, nodeB, (0,0), nodeD, (0,0), (0,0), (0,0), nodeDD)
    
    $ pathAA = (nodeA, nodeB, nodeC, nodeD, (0,0), (0,0), (0,0), nodeDD)
    $ pathBB = (nodeA, nodeB, nodeC, nodeD, (0,0), (0,0), (0,0), nodeDD)
    $ pathCC = (nodeA, nodeB, nodeC, nodeD, (0,0), (0,0), (0,0), nodeDD)
    $ pathDD = (nodeA, nodeB, nodeC, nodeD, (0,0), (0,0), (0,0), nodeDD)





label loop_asteroid3_up:
    
    while True:
        # start "move through the map" loop
        call startpos from _call_startpos_84 


        # do something at node?
        if exitpos == 1:
            $ startpos = 1
            jump asteroid3
            
            
            
        if exitpos == 2:
            if startpos == 2:
                if inventory_select == "":
                    m "More rocks... {w=2} {nw}"
                else:
                    call asteroid_dig(0) from _call_asteroid_dig_6
            $ startpos = 2
            
            
        if exitpos == 3:
            if startpos == 3:
                if inventory_select == "":
                    if asteroid3_gem == True:
                        m "There is something shiny inside the ground. {w=3.5} {nw}"
                        m "But the ground is too hard to take it out. {w=3} {nw}"
                    else:
                        call dialog_nothing from _call_dialog_nothing_70
                
                elif inventory_select == "pick" or inventory_select == "shovel":
                    call asteroid_dig(1) from _call_asteroid_dig_7
                    if asteroid3_gem == True:
                        call take_gem from _call_take_gem_12
                        $ asteroid3_gem = False
                    else:
                        call dialog_nothing from _call_dialog_nothing_71
                else:
                    call dialog_nosense from _call_dialog_nosense_35
                    
            $ startpos = 3

            
        if exitpos == 4:
            if startpos == 4:
                #"rock_asteroid3up [rock_asteroid3up]"
                if rock_asteroid3up == False:
                    if inventory_select == "":
                        m "Rocks, rocks, rocks... {w=3} {nw}"
                        m "Well... this one looks different than the others... {w=4} {nw}"
                        m "Maybe another kind of asteroid? {w=3} {nw}"
                        m "This is interesting! {w=3} {nw}"
                    else:
                        $ inventory_select2 = ""
                        call asteroid_dig(1) from _call_asteroid_dig_8
                        
                        if inventory_select2 == "pick":
                            with hpunch
                            call sound_earthquake from _call_sound_earthquake_4
                            
                            hide asteroid_small4
                            show asteroid_small2b:
                                pos (500, 390)
                                rotate -55
                            
                            $ rock_asteroid3up = True
                                
                        elif inventory_select2 == "shovel":
                            call dialog_nothing from _call_dialog_nothing_72
                        
                        else:
                            pass
                            
                            
                        $ inventory_select2 = ""
                
                else:
                    if "asteroid" not in inventory:
                        m "Now, this rock is broken. {w=2.5} {nw}"
                        m "I could take one piece. {w=2.5} {nw}"
                        call take_item("asteroid") from _call_take_item_19
                    
                    else:
                        call asteroid_dig(0) from _call_asteroid_dig_9
                    
            $ startpos = 4

            

        if exitpos == 11:     
            $ startpos = 11   

            
        if exitpos == 22:
            $ startpos = 22

            
        if exitpos == 33:
            $ startpos = 33

            
        if exitpos == 44:
            if startpos == 44:
                call asteroid_dig(0) from _call_asteroid_dig_10
            $ startpos = 44

                





