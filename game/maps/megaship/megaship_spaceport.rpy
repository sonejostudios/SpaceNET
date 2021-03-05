# MAPS

# prison cell start of game

############################################
label megaship_spaceport:
    $ pnc_nodes_visible = True
    
    call atmo_spaceport from _call_atmo_spaceport
    stop music fadeout 1.0
    
    image megaship_spaceport = imagemapsdir + "megaship_spaceport.png"
    
    #scene megaship_spaceport
    show screen notify("spaceport")
    
    #show bgcolor behind megaship_spaceport
    
    scene bgcolor
    
    
##
    if galaxy_enable == 1:
        show galaxy

    # stars
    show starssmall r2l behind ship
    show starsmid r2l behind ship
    show starsbig r2l behind ship
    
    
    image megaship_spaceport = imagemapsdir + "megaship_spaceport.png"
    image megaship_spaceport2 = imagemapsdir + "megaship_spaceport2.png"
    image megaship_bigdoor = "/images/bigdoor.png"
    image spaceship_deco = "images/spaceship/spaceship2u.png"
    
    
    #call sound_crane
    $ renpy.music.play("sounds/crane.ogg", channel="music", fadein=1, fadeout=1, tight=True, if_changed=True, loop=True)
    
    
    #show megaship_bigdoor(tag="megaship_bigdoor") zorder 1000:
    show megaship_bigdoor:
        anchor (1.0,1.0)
        pos (800, 240)
        linear 5 pos (800, 240)
        linear 5 pos (800, 120) #open
        linear 5 pos (800, 120)
        linear 5 pos (800, 240) #close
        repeat
        
    show megaship_bigdoor as megaship_bigdoor2:
        anchor (1.0,0.0)
        pos (800, 240)
        linear 5 pos (800, 240)
        linear 5 pos (800, 360) #open
        linear 5 pos (800, 360)
        linear 5 pos (800, 240) #close
        repeat
        
    show megaship_spaceport
    
    #show spaceship_deco(tag="spaceship_deco") zorder 900:
    show spaceship_deco zorder 900:
        anchor (0.5,0.5)
        zoom 0.5
        rotate 180
        pos (330, 88)
        ease 5 pos (330, 88)
        ease 5 pos (330, 240) rotate 90
        ease 5 pos (800, 240)
        rotate 270
        ease 15 pos (800, 240) 
        ease 5 pos (330, 240) 
        ease 5 pos (330, 88) rotate 180
        repeat
    
    
    if hacker_in_prison == 1:
        show spaceship3u :
            zoom 0.5
            pos (330,390)
    
    
    show light:
        pos (72,96)
    show light as light2:
        pos (72,386)
    show light as light3:
        pos (654,55)
    show light as light4:
        pos (654,424)
        
    show spaceship zorder 950:
        zoom 0.5
        pos (194,390)
        

    show shadow zorder 1000:
        pos nodeA
    
    show megaship_spaceport2 zorder 999:
        align (1.0,0.5)
        
        

        

##
    
    
    # set all variables for the map (nodes and path)
    $ nodeA = (54, 240)
    $ nodeB = (150, 156)
    $ nodeC = (299, 157)
    $ nodeD = (428, 157)

    $ nodeAA = (527, 240)
    $ nodeBB = (151, 322)
    $ nodeCC = (301, 321)
    $ nodeDD = (431, 323)

    $ pathA = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)
    $ pathB = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)
    $ pathC = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)
    $ pathD = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)
     
    $ pathAA = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)
    $ pathBB = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)
    $ pathCC = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)
    $ pathDD = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)
    
    
    # space suit?
    if "spacesuit" not in inventory:
        show player:
            pos nodeA
        show nodeanime as pathnodeA:
            pos nodeA
        
        with flash
        m "haaa! there is no air to breathe!{w=3.0} {nw}"
        call sound_door from _call_sound_door
        jump megaship_lift2
    
    else:
        $ inventory_select = "spacesuit"
        call inventory_notify from _call_inventory_notify
    
    
    


label loop_megaship_spaceport:

    
    while True:
        # start "move through the map" loop
        call startpos from _call_startpos

        # do something at node?
        if exitpos == 1:
            $ startpos = 1
            $ liftpos = 0
            call sound_door from _call_sound_door_1
            jump megaship_lift2
            
        if exitpos == 2:
            if startpos == 2:
                call dialog_nothing from _call_dialog_nothing
            $ startpos = 2
            
            
        if exitpos == 3:
            
            # get spaceship_deco bound position
            $ spaceship_deco_bounds = renpy.get_image_bounds("spaceship_deco")
            $ spaceship_deco_bounds = (int(spaceship_deco_bounds[0]), int(spaceship_deco_bounds[1]))
            #"[spaceship_deco_bounds]"
            
            if startpos == 3:
                if spaceship_deco_bounds == (276,34):
                    m "This spaceship is quite nice... {w=3.0} {nw}"
                    m "Somehow better than mine! {w=3.0} {nw}"
                else:
                    call dialog_nothing from _call_dialog_nothing_1
                
            $ startpos = 3
            
            
        if exitpos == 4:
            if startpos == 4:
                call dialog_nothing from _call_dialog_nothing_2
            $ startpos = 4
            
            

        #exits routing "got to map and set position for next map"
        if exitpos == 11:
            if startpos == 11:
                m "This is a huge door! {w=2.0} {nw}"
            $ startpos = 11      
            
            
        if exitpos == 22:
            #if startpos == 22:
            #m "This is my spaceship! {w=2.0} {nw}"
            
            call sound_door from _call_sound_door_2
            hide player
            
            menu:
                "take off":
                    # get bigdoor bound position
                    $ bigdoor_bounds = renpy.get_image_bounds("megaship_bigdoor")
                    $ bigdoor_bounds = (int(bigdoor_bounds[0]), int(bigdoor_bounds[1]))
                    #"[bigdoor_bounds]"
                    
                    if bigdoor_bounds[1] == -120:
                    
                        
                        m "Let's go! {w=0.7} {nw}"
                        hide player
                        show spaceship zorder 950:
                            zoom 0.5
                            rotate 0
                            pos (194,390)
                            ease 1 pos (194,240) rotate 90
                            ease 2 pos (800, 240)
                        
                        #pause 1
                        call sound_take_off from _call_sound_take_off
                        pause 3
                        stop music
                        jump space
                    else:
                        m "I don't want to start now if the door is closed! {w=3.0} {nw}"
                    
                "leave":
                    call sound_door from _call_sound_door_3
                    show player
                    pass
                    
                
            $ startpos = 22
            
            
        if exitpos == 33:
            if startpos == 33 and hacker_in_prison == 1:
                m "This is the spaceship of 4n0nym0us. {w=2.5} {nw}"
            else:
                call dialog_nothing from _call_dialog_nothing_3
            $ startpos = 33
            
            
            
        if exitpos == 44:
            if startpos == 44:
                call dialog_nothing from _call_dialog_nothing_4
            $ startpos = 44
            




label megaship_landing:

    hide megaspaceship
    hide spaceshipside
    hide spaceship
    
    image megaship_spaceport = imagemapsdir + "megaship_spaceport.png"
    image megaship_spaceport2 = imagemapsdir + "megaship_spaceport2.png"
    image megaship_bigdoor = "/images/bigdoor.png"
    image spaceship_deco = "images/spaceship/spaceship2u.png"
    
    
    show megaship_bigdoor:
        anchor (1.0,1.0)
        pos (800, 240)
        #linear 2 pos (800, 240)
        linear 5 pos (800, 120)
    show megaship_bigdoor as megaship_bigdoor2:
        anchor (1.0,0.0)
        pos (800, 240)
        #linear 2 pos (800, 240)
        linear 5 pos (800, 360)
        
    show megaship_spaceport
    
    show spaceship_deco:
        anchor (0.5,0.5)
        zoom 0.5
        pos (330, 88)
        rotate 180
        
    if hacker_in_prison == 1:
        show spaceship3u :
            zoom 0.5
            pos (330,390)
    
    
    show light:
        pos (72,96)
    show light as light2:
        pos (72,386)
    show light as light3:
        pos (654,55)
    show light as light4:
        pos (654,424)
        
    show shadow at truecenter zorder 1000
        
    pause 4
    
    show spaceship zorder 950:
        rotate -90
        zoom 0.5
        pos (800, 240)
        ease 4 pos (194,240)
        #ease 3 rotate 0
        ease 2 pos (194,390) rotate 0
        
    
    show megaship_spaceport2 zorder 999:
        align (1.0,0.5)
        
    
    pause 6
    
    show megaship_bigdoor:
        linear 5 pos (800, 240)
    show megaship_bigdoor as megaship_bigdoor2:
        linear 5 pos (800, 240)
        
    pause 5

    call sound_door from _call_sound_door_4
    jump megaship_spaceport

