# MAPS

############################################
label asteroid2:
    $ pnc_nodes_visible = True
    
    if landing == True:
        stop music fadeout 1.0
        
    call atmo_deep_ambiance from _call_atmo_deep_ambiance_3

    
    image asteroid2 = imagemapsdir + "asteroid2.png"
    
    scene bgcolor
    call show_space from _call_show_space_27
    show screen notify("Asteroid 2")
    
    show asteroid2: #at inspace_idle
        pos (60,20)
        
        
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
        

    show asteroid_small as asteroid_small3:
        pos (484, 172)
        rotate 90
        
    show asteroid_small2 as asteroid_small4:
        pos (231, 421)
        zoom 0.8
    
    
    # check if spaceship is landing on this map or not
    # $ landing = False
    # $ landing = True
    call landing_anim from _call_landing_anim_9
    
    

    
    
    # set all variables for the map (nodes and path)
    $ nodeA = (472, 216)
    $ nodeB = (420, 370)
    $ nodeC = (550, 450)
    $ nodeD = (770, 380)
    
    $ nodeAA = (400,25)
    $ nodeBB = (670,240)
    $ nodeCC = (400,460)
    $ nodeDD = (315,240)
    
    $ pathA = (nodeA, nodeB, nodeC, (0,0), (0,0), (0,0), (0,0), nodeDD)
    $ pathB = (nodeA, nodeB, nodeC, nodeD, (0,0), (0,0), (0,0), nodeDD)
    $ pathC = (nodeA, nodeB, nodeC, nodeD, (0,0), (0,0), (0,0), nodeDD)
    $ pathD = ((0,0), nodeB, nodeC, nodeD, (0,0), (0,0), (0,0), (0,0))
    
    $ pathAA = (nodeA, nodeB, nodeC, nodeD, (0,0), (0,0), (0,0), nodeDD)
    $ pathBB = (nodeA, nodeB, nodeC, nodeD, (0,0), (0,0), (0,0), nodeDD)
    $ pathCC = (nodeA, nodeB, nodeC, nodeD, (0,0), (0,0), (0,0), nodeDD)
    $ pathDD = (nodeA, nodeB, nodeC, (0,0), (0,0), (0,0), (0,0), nodeDD)

    if landing == True:
        $ inventory_select = "spacesuit"
        call inventory_notify from _call_inventory_notify_11



label loop_asteroid2_landing:
    
    while True:
        # start "move through the map" loop
        call startpos from _call_startpos_85 


        # do something at node?
        if exitpos == 1:
            if startpos == 1:
                if inventory_select == "":
                    m "This was probably an asteroid. {w=2.5} {nw}"
                else:
                    call asteroid_dig(0) from _call_asteroid_dig_11
            $ startpos = 1   
            
            
            
        if exitpos == 2:
            if startpos == 2:
                if inventory_select == "":
                    m "This is the biggest asteroid. {w=2.5} {nw}"
                else:
                    call asteroid_dig(0) from _call_asteroid_dig_12
            $ startpos = 2
            
            
        if exitpos == 3:
            $ startpos = 1
            jump asteroid2_down

            
        if exitpos == 4:
            $ startpos = 1
            jump asteroid2_right

            

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
            call takeoff_anim("withmenu") from _call_takeoff_anim_11 # go to takeoff
            $ pnc_nodes_visible = True
            
            # straight to space
            if takeoftospace == True:
                $ takeoftospace = False
                $ space_anim = True
                $ pnc_nodes_visible = False
                jump space

            
            # to surface
            if landing == True:
                $ shippos = (1000,200) # set position in surface engine
                jump surface
                





