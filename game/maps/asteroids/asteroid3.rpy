# MAPS

############################################
label asteroid3:
    $ pnc_nodes_visible = True
    
    stop music fadeout 1.0
    
    call atmo_deep_ambiance from _call_atmo_deep_ambiance_4
    
    image asteroid3 = imagemapsdir + "asteroid3.png"
    
    scene bgcolor
    call show_space from _call_show_space_29
    show screen notify("Asteroid 3")
    
    show asteroid3: #at inspace_idle
        pos (-100,-410)
        

    $ asteroidzoom = renpy.random.random()*0.7 + 0.1
    show asteroid_small behind orbitmeter, text_planet, spaceshipside, asteroid3:
        zoom asteroidzoom
        rotate 0
        ypos 200
        xpos 900
        linear 10 xpos -200 rotate -560
        repeat
        
    $ asteroidzoom2 = renpy.random.random()*0.7 + 0.1
    show asteroid_small2 as asteroid_small2 behind orbitmeter, text_planet, spaceshipside, asteroid3:
        zoom asteroidzoom2
        rotate 0
        ypos 400
        xpos 1200
        linear 13 xpos -200 rotate -460
        repeat
        
        
    show asteroid_small as asteroid_small3:
        pos (495, 110)
        rotate -45

    

    # check if spaceship is landing on this map or not
    # $ landing = False
    # $ landing = True
    call landing_anim from _call_landing_anim_11
    
    
    # set all variables for the map (nodes and path)
    $ nodeA = (287, 28)
    $ nodeB = (443, 237)
    $ nodeC = (538, 152)
    $ nodeD = (468, 378)
    
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
    

    #"spaceship_broken [spaceship_broken]\nasteroid_collision [asteroid_collision]\nspaceshiptype [spaceshiptype]"
    
    if asteroid_collision == False:
        #call sound_earthquake
        call sound_explosion from _call_sound_explosion_5
        with hpunch
        m "Wow. That was an emergency landing! {w=3.5} {nw}"
        m "That was such a crash! {w=2.5} {nw}"
        m "Just because of this stupid asteroid. {w=3.5} {nw}"
        m "I hope my spaceship is okay.{w=3.5} {nw}"
        m "Let's have a look.{w=1}.{w=1}.{w=1}.{w=1}.{w=1} {nw}"
        m "Oh no! My spaceship is broken. {w=2.5} {nw}"
        m "One wing looks really bad. {w=2.5} {nw}"
        m "And the hyperspace module is smoking... {w=3.5} {nw}"
        m "I think I'm trap on this asteroid field! {w=3.5} {nw}"
        $ asteroid_collision = True
        $ startpos = 44
    

    if landing == True:
        $ inventory_select = "spacesuit"
        call inventory_notify from _call_inventory_notify_13
        call sound_door from _call_sound_door_180
        



label loop_asteroid3:
    
    while True:
        # start "move through the map" loop
        call startpos from _call_startpos_87 


        # do something at node?
        if exitpos == 1:
            $ startpos = 1
            jump asteroid3_up 
            
            
            
        if exitpos == 2:
            if startpos == 2:
                if inventory_select == "":
                    m "This is a middle range asteroid. {w=2.5} {nw}"
                else:
                    call asteroid_dig(0) from _call_asteroid_dig_17
                
            $ startpos = 2
            
            
        if exitpos == 3:
            if startpos == 3:
                if inventory_select == "":
                    m "Rocks...{w=2} {nw}"
                    m "Now I'm hidden behind it.{w=3} {nw}"
                    m "But hey! There is nobody around to find me anyway...{w=4} {nw}"
                    m "Well...{w=1.5} {nw}"
                    m "What's the point?{w=2.5} {nw}"
                    m "I really have better to do now!{w=3} {nw}"
                else:
                    call asteroid_dig(0) from _call_asteroid_dig_18
            $ startpos = 3

            
        if exitpos == 4:
            if startpos == 4:
                call asteroid_dig(0) from _call_asteroid_dig_19
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
            $ direction = 0
            #call sound_door
            call takeoff_anim("withmenu") from _call_takeoff_anim_13 # go to takeoff
            $ pnc_nodes_visible = True
            
            # straight to space
            if takeoftospace == True:
                $ takeoftospace = False
                $ space_anim = True
                $ pnc_nodes_visible = False
                jump space

            
            # to surface
            if landing == True:
                $ shippos = (200,1600) # set position in surface engine
                $ space_anim = False
                jump surface_asteroids
                
        jump loop_asteroid3
                





