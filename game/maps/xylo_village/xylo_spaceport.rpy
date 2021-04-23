# MAPS

############################################


init:
    $ xylo_spaceport_brokenwall = False


label xylo_spaceport:
    $ pnc_nodes_visible = True
    
    
    stop music
    call atmo_village from _call_atmo_village
    
    
    $ planet = "xylo"
    
    $ planetxy_first = True
    

    image xylo_spaceport = imagemapsdir + "xylo_spaceport.png"
    
    scene xylo_spaceport
    show screen notify("Xylo village spaceport")
    
    show bgcolor behind xylo_spaceport
    
    show doorh:
        pos (600,445)

    
    show light:
        pos (145,130)
        
    show light as light2:
        pos (355,130)
        
    show light as light3:
        pos (145,345)
        
    show light as light4:
        pos (355,345)
        

    
    if game_end == True and spacenet_state == "online":
        show npc:
            pos (387, 420)
            rotate 45
        
        
    #broken wall boilerplate only because of landing animation (see loop_xylo_spaceport)
    if xylo_spaceport_brokenwall == False:
        show brokenwall closed behind shadow:
            pos (468,25)
    if xylo_spaceport_brokenwall == True:
        show brokenwall open behind shadow:
            pos (468,25)
        
        

    # check if spaceship is landing on this map or not
    # $ landing = False
    # $ landing = True
    call landing_anim from _call_landing_anim
    
    
    # set all variables for the map (nodes and path)
    $ nodeA = (419, 395)
    $ nodeB = (470,240)
    $ nodeC = (600,423)
    $ nodeD = (470,48)
    
    $ nodeAA = (400,25)
    $ nodeBB = (632,168)
    $ nodeCC = (400,460)
    $ nodeDD = (320,235)
    
    $ pathA = ((0,0), nodeB, nodeC, nodeD, (0,0), nodeBB, (0,0), nodeDD)
    $ pathB = ((0,0), nodeB, nodeC, nodeD, (0,0), nodeBB, (0,0), nodeDD)
    $ pathC = ((0,0), nodeB, nodeC, nodeD, (0,0), nodeBB, (0,0), nodeDD)
    $ pathD = ((0,0), nodeB, nodeC, nodeD, (0,0), nodeBB, (0,0), nodeDD)
    
    $ pathAA = ((0,0), (0,0), (0,0), (0,0), nodeAA, (0,0), (0,0), (0,0))
    $ pathBB = ((0,0), nodeB, nodeC, nodeD, (0,0), nodeBB, (0,0), nodeDD)
    $ pathCC = ((0,0), (0,0), nodeC, (0,0), (0,0), (0,0), nodeCC, (0,0))
    $ pathDD = ((0,0), nodeB, nodeC, nodeD, (0,0), nodeBB, (0,0), nodeDD)
    
    
    if game_end == True and spacenet_state == "online":
        
        $ pathA = (nodeA, nodeB, nodeC, nodeD, (0,0), nodeBB, (0,0), nodeDD)
        $ pathB = (nodeA, nodeB, nodeC, nodeD, (0,0), nodeBB, (0,0), nodeDD)
        $ pathC = (nodeA, nodeB, nodeC, nodeD, (0,0), nodeBB, (0,0), nodeDD)
        $ pathD = (nodeA, nodeB, nodeC, nodeD, (0,0), nodeBB, (0,0), nodeDD)
        
        $ pathAA = (nodeA, (0,0), (0,0), (0,0), nodeAA, (0,0), (0,0), (0,0))
        $ pathBB = (nodeA, nodeB, nodeC, nodeD, (0,0), nodeBB, (0,0), nodeDD)
        $ pathCC = (nodeA, (0,0), nodeC, (0,0), (0,0), (0,0), nodeCC, (0,0))
        $ pathDD = (nodeA, nodeB, nodeC, nodeD, (0,0), nodeBB, (0,0), nodeDD)


label loop_xylo_spaceport:
    
    
    #broken wall
    if xylo_spaceport_brokenwall == False:
        show brokenwall closed behind shadow:
            pos (468,25)
    if xylo_spaceport_brokenwall == True:
        show brokenwall open behind shadow:
            pos (468,25)
            
            
    
    # if GAME END
    if game_end == True and startpos == 1:
        with pixellate

        
            
    
    while True:
        # start "move through the map" loop
        call startpos from _call_startpos_7

        
        # GAME END
        if exitpos == 1:  
            if startpos == 1 and game_end == True and spacenet_state == "online":
                $ inventory_select = ""
                sam "You've done a great job, thank you!{w=3}{nw}"
                sam "Now we can live a normal life...{w=3}{nw}"
                sam "With the SpaceNET network, anybody has now access to information.{w=4}{nw}"
                sam "This will be a great step toward peace.{w=3}{nw}"
                m "This is great!{w=2}{nw}"
                sam "Thank you very...{w=1} very...{w=1} very much!{w=2}{nw}"
                sam "Now we can start a new life!{w=3}{nw}"
                m "Yeah!{w=2}{nw}"
                sam "I wish you all the best.{w=2.5}{nw}"
                sam "...{w=1}{nw}"
                sam "We are done now.{w=2}{nw}"
                
                menu:
                    "Alright, see you soon!":
                        m "Alright, see you soon!{w=2}{nw}"
                        sam "Bye!{w=2}{nw}"
                        
                        show player:
                            pos nodeA
                            ease 1 pos nodeDD
                        if shadow_enable == 1:
                            show shadow:
                                pos nodeA
                                ease 1 pos nodeDD
                            
                        pause 1
                        
                       
                        call sound_door from _call_sound_door_18
                        hide player
                        
                        pause 0.7
                        
                        call takeoff_anim("nomenu") from _call_takeoff_anim # go to takeoff
                        
                        $ takeoftospace = True
                        # straight to space
                        if takeoftospace == True:
                            $ takeoftospace = False
                            $ space_anim = True
                            #jump space
                            jump game_end_anim
                        
                    
                    "Wait, I'll be back":
                        pass

 
            $ startpos = 1
        

            

        if exitpos == 2:
            if startpos == 2:
                call dialog_nothing from _call_dialog_nothing_9
            $ startpos = 2
         

            
        if exitpos == 3:
            if planetxy_register == True:
                $ startpos = 1
                call sound_door from _call_sound_door_19
                jump xylo_spaceport_hall
            else:
                $ startpos = 3
                call dialog_closed from _call_dialog_closed
                
            
            
            
        if exitpos == 4:
            
            if xylo_spaceport_brokenwall == True:
                $ startpos = 3
                jump xylo_village_brokenwall
            
            if startpos == 4:
                if inventory_select == "":
                    m "This wall seems to be broken...  {w=2} {nw}"
                    
                elif inventory_select == "dynamite":
                    m "This is overkill... no way! {w=2.5} {nw}"
                    
                elif inventory_select == "pick":
                    m "I could use the pick and open it completely. \nLet's go!{w=3.5} {nw}"
                    call use_and_keep_item from _call_use_and_keep_item_3
                    call sound_dig from _call_sound_dig
                    pause 1.5
                    call sound_connected from _call_sound_connected_2
                    with flash
                    $ xylo_spaceport_brokenwall = True
                    jump loop_xylo_spaceport
                    
                else:
                    call dialog_nosense from _call_dialog_nosense_2
                    
                
            $ startpos = 4

            

        #exits routing "got to map and set position for next map"
        if exitpos == 11:       #if going out at AA
            $ startpos = 33     #go to CC

            
        if exitpos == 22:
            if startpos == 22:
                m "There is a service screen.{w=2.5}{nw}"
                m "Hello?{w=1.5}{nw}"
                radio "Welcome to Xylo Village! What can I do for you?{w=3.5}{nw}"
                
                $ questions = ["Hi. Where I am? {w=1.5} {nw}",
                                "I need to register my spaceship. {w=2.5} {nw}",
                                "I'm fine, thank you. {w=1.0} {nw}"]
                
                menu:
                    "[questions[0]]":
                        m "[questions[0]]"
                        radio "You are at Xylo Village Spaceport. {w=2.5}{nw}"
                        radio "Go south and you'll find the hall with a shop and a bar. {w=3.5}{nw}"
                        radio "Further, you'll find the village. {w=3.5}{nw}"
                        radio "Enjoy! {w=1.5}{nw}"
                        
                    "[questions[1]]" if planetxy_register == False:
                        m "[questions[1]]"
                        radio "Sure.{w=1} No problem.{w=1} {nw}"
                        radio "Wait...{w=2} {nw}"
                        call sound_connected from _call_sound_connected_3
                        with flash
                        $ planetxy_register = True
                        radio "Your spaceship and you are now registered.{w=3} {nw}"
                        radio "You are now allowed to land everywhere on Xylo.{w=3} {nw}"
                        radio "Thank you for the registration.{w=2.5} {nw}"
                        radio "Bye.{w=1} {nw}"
                        #m "Oh, that's nice, thanks!{w=2.5} {nw}"
                        
                    "[questions[2]]":
                        m "[questions[2]]"
                        pass
                
                
            $ startpos = 22

            
        if exitpos == 33:
            $ startpos = 33

            
        if exitpos == 44:
            $ startpos = 44
            call sound_door from _call_sound_door_20
            call takeoff_anim("withmenu") from _call_takeoff_anim_1 # go to takeoff
            
            
            # straight to space
            if takeoftospace == True:
                $ takeoftospace = False
                $ space_anim = True
                jump space
                
            # to surface
            if landing == True:
                $ shippos = (400,0) # set position in surface engine
                $ space_anim = False
                jump surface_xylo
            
            jump loop_xylo_spaceport

