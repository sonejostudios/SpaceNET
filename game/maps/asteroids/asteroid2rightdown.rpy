# MAPS

init:
    $ asteroid2_spaceship_entrance = False

############################################
label asteroid2_rightdown:
    $ pnc_nodes_visible = True
    
    stop music fadeout 1.0
    call atmo_deep_ambiance from _call_atmo_deep_ambiance_6
    
    
    image asteroid2 = imagemapsdir + "asteroid2.png"
    
    scene bgcolor
    call show_space from _call_show_space_30
    #show screen notify("Asteroid 2")
    
    show asteroid2: #at inspace_idle
        pos (-740,-460)
        
        
    show spaceship3s:
        pos (400, 200)
        rotate 150
        
    
    # big asteroid on spaceship
    show asteroid_small2 as asteroid_small3:
        pos (370, 260)
        rotate 20
        
    
    show asteroid_small as asteroid_small4:
        pos (231, 192)
        rotate 115
        zoom 0.75
        
      
    # door asteroid
    if asteroid2_spaceship_entrance == False:
        show asteroid_small as asteroid_small_door:
            pos (380, 196)
            rotate 40
            zoom 0.5
    
        
        
    $ asteroidzoom = renpy.random.random()*0.7 + 0.1
    show asteroid_small behind orbitmeter, text_planet, spaceshipside, asteroid2:
        zoom asteroidzoom
        rotate 0
        ypos 240
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
        

    
    
    
    # check if spaceship is landing on this map or not
    $ landing = False
    # $ landing = True
    #call landing_anim
    
    
    # set all variables for the map (nodes and path)
    $ nodeA = (30, 90)
    $ nodeB = (235, 150)
    $ nodeC = (300, 30)
    $ nodeD = (364, 170)
    
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





label loop_asteroid2_rightdown:
    
    while True:
        # start "move through the map" loop
        call startpos from _call_startpos_90 


        # do something at node?
        if exitpos == 1:
            $ startpos = 4
            jump asteroid2_down
            
            
            
        if exitpos == 2:
            if startpos == 2:
                if inventory_select == "":
                    m "Rocks on rocks... {w=2} {nw}"
                else:
                    call asteroid_dig(0) from _call_asteroid_dig_20
            $ startpos = 2
            
            
        if exitpos == 3:
            $ startpos = 4
            jump asteroid2_right

            
        if exitpos == 4:
            if startpos == 4:

                if asteroid2_spaceship_entrance == False:
                    if inventory_select == "":
                        m "It is an old spaceship. It looks totally broken. {w=4} {nw}"
                        m "I guess it was an accident. {w=3} {nw}"
                        m "What happened? {w=2.5} {nw}"
                        m "The door is broken, but also covered by a big rock. {w=4} {nw}"
                        m "I can't go through. {w=2.5} {nw}"
                    
                    elif inventory_select == "pick":
                        call sound_dig from _call_sound_dig_8
                        call use_and_keep_item from _call_use_and_keep_item_44
                        pause 1.5
                        hide asteroid_small_door
                        call sound_connected from _call_sound_connected_42
                        with flash
                        m "The door is free now! {w=2} {nw}"
                        
                        $ asteroid2_spaceship_entrance = True
                        
                    else:
                        call dialog_nosense from _call_dialog_nosense_41
                
                else:
                    $ startpos = 1
                    jump asteroid2_spaceship
            
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

                





