# MAPS

############################################
init:
    $ isc_flight = False
    $ isc_gateway_usehook = False


label isc_city_gateway:
    
    call atmo_spaceship_station 
    
    image isc_city_gateway = imagemapsdir + "isc_city_gateway.png"
    
    #scene bgcolor
    show screen notify("ISC Gateway")
    
    call show_space
    
    show crane:
        anchor (0.5,0.5)
        rotate 90
        pos (200,240)
    
    show isc_city_gateway:
        anchor (0.5,0.5)
        pos (0.5,0.5)
    
    
    show light:
        pos (400,133)
        
    show light as light2:
        pos (400,350)
        
        

    
    # set all variables for the map (nodes and path)
    $ nodeA = (370, 240)
    $ nodeB = (480, 240)
    $ nodeC = (755, 240)
    $ nodeD = (589, 80)

    $ nodeAA = (630, 176)
    $ nodeBB = (537, 302)
    $ nodeCC = (350, 302)
    $ nodeDD = (140, 302)

    $ pathA = (nodeA, nodeB, (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0))
    $ pathB = (nodeA, nodeB, (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0))
    $ pathC = (nodeA, nodeB, nodeC, (0, 0), (0, 0), (0, 0), (0, 0), (0, 0))
    $ pathD = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)
     
    $ pathAA = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)
    $ pathBB = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)
    $ pathCC = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)
    $ pathDD = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)
    

    if isc_flight == True:
        call isc_city_gateway_spaceship_back
        
        
    #if waiting for hacker, move crane away
    if sam_numpad_mission == 2 and countdown_sec > 0:
        $ isc_crane_pos_x = 0
        $ isc_crane_pos_y = 0
        $ crane_pos_name = "stow position"
        
        
        
    #if crane in place, show it
    if isc_crane_pos_x == 1 and isc_crane_pos_y == 0:
        show crane as crane2:
            pos (755, 240)
            rotate 90
        $ pathA = (nodeA, nodeB, nodeC, (0, 0), (0, 0), (0, 0), (0, 0), (0, 0))
        $ pathB = (nodeA, nodeB, nodeC, (0, 0), (0, 0), (0, 0), (0, 0), (0, 0))
        
        

    
    


label loop_isc_city_gateway:
    
    while True:

        # start "move through the map" loop
        call startpos

        # do something at node?
        if exitpos == 1:
            
            $ countdown = False
            
            call sound_door
            $liftpos = 0
            jump isc_city_bar_lift2
            $ startpos = 1



        if exitpos == 2:
            
            if startpos == 2:

                if sam_numpad_mission == 2 and countdown_sec > 0:
                    m "I think this is the place I should wait for 4n0nym0us.{w=2.5} {nw}"
                    pause countdown_sec
                    jump isc_city_gateway_spaceship
                    
                if isc_crane_pos_x == 1 and isc_crane_pos_y == 0:
                    if inventory_select == "hook":
                        $ isc_gateway_usehook = True
                        m "Let's climb on the crane!{w=2} {nw}"
                    else:
                        m "The crane... {w=1} I could walk on it... {w=2.5} {nw}"
                        m "I this it is very dangerous... {w=2}  Should I? {w=1} {nw}"
                
                else:
                    m "Wow... {w=1.5} {nw}"
                    m "The view is absolutely amazing! {w=2} {nw}"
                    m "But... {w=1} {nw}"
                    m "Nothing to do here... {w=2} {nw}"
                
            $ startpos = 2

            

            
        if exitpos == 3: # go onto crane
            if "hook" not in inventory:
                m "Are you crazy?{w=1.5} {nw}"
                show player:
                    pos nodeC
                    ease 0.5 pos nodeB
                pause 0.5
                m "No way I'll climb there without safety equiment!{w=3} {nw}"
                $ startpos = 2
                
            else:
                $ inventory_select = "hook"
                call use_and_keep_item
                m "Let's go! {w=2} {nw}"
                $ startpos = 1
                jump isc_city_gateway_crane
            
            
            
        
        if exitpos == 4:
            $ startpos = 4
           

        #exits routing "got to map and set position for next map"
        if exitpos == 11:
            $ startpos = 11 

            
        if exitpos == 22:
            $ startpos = 22

            
        if exitpos == 33:
            $ startpos = 33
            

            
        if exitpos == 44:
            $ startpos = 44
            

            

# spaceship
label isc_city_gateway_spaceship:
    
    
    call sound_hyperspace
    
    $ countdown = False
    $ countdown_sec = 0
    show spaceship3u:
        pos (535,600)
        easein 7 pos (535,240)
    pause 7

    hacker "Come in! {w=2.5} {nw}"
    
    call music_satellite
    
    
    $ isc_flight = False

    menu:
        "Let's go!":
            call sound_door
            hide player
            hide pathnodeA
            hide pathnodeB
            $ isc_flight = True
            $ sam_numpad_mission = 3
            
        "No, thanks":
            m "no, thanks! {w=1.5} {nw}"
            stop music fadeout 1.0
    
    
    call sound_hyperspace
    
    show spaceship3u:
        pos (535,240)
        easeout 5 pos (535,-200)
    pause 5
    if isc_flight == True:
        jump isc_spaceflight
    
    else:
        jump loop_isc_city_gateway
    
    
    
    
label isc_city_gateway_spaceship_back:
    
    call sound_hyperspace
    
    if shadow_enable == 1:
        show shadow at truecenter
        

    show spaceship3u zorder 900:
        pos (535,700)
        easein 7 pos (535,240)
    with pixellate
    
    stop music fadeout 10.0
    
    pause 7
    
    $ isc_flight = False
    
    call sound_door
    
    pause 0.5
    call sound_hyperspace
    
    show spaceship3u zorder 900:
        pos (535,240)
        easeout 5 pos (535,-200)
    
    return 
    
    
    
    
    
    
label isc_spaceflight:
    
    #call music_satellite
    
    scene bgcolor
    call show_space
    show spaceship3s at inspace_idle
    with pixellate
    pause 1
    
    hacker "Hey... nice to see you again.{w=3} {nw}"
    hacker "I've just got a really bad information.{w=3} {nw}"
    
    while True:
        
        call isc_spaceflight_cargo_mission

        hacker "...{w=2} {nw}"
        hacker "Are you ready?{w=2} {nw}"

        menu:
            "okay, let's go!":
                m "okay, let's go!{w=2} {nw}"
                
                hacker "I'll archive a voice message for you.{w=3} {nw}"
                hacker "Just call 111999 in the terminal.{w=3} {nw}"

                call add_note("cargo mission voice message : 111999")
                
                hacker "Okay... {w=2} {nw}"
                hacker "I'll bring you back to the gateway.{w=3} {nw}"
                hacker "Good luck!{w=2} {nw}"
                
                jump isc_city_gateway
            
            "no, please explain me again":
                m "no, please explain me again.{w=2} {nw}"
                pass
            

    jump isc_city_gateway
    
    
    
    
label isc_spaceflight_cargo_mission:
    
    hacker "The A.R.K. Corporation is going to deliver weapons to the government.{w=5} {nw}"
    hacker "They want to start a civil war!{w=3} {nw}"
    hacker "We need to stop them.{w=2} {nw}"
    hacker "...{w=2} {nw}"
    hacker "Here is your mission:{w=2} {nw}"
    hacker "Infiltrate the space cargo of A.R.K. Corporation.{w=4} {nw}"
    hacker "You'll find it in the terminal.\nJust 'locate cargo' in the terminal.{w=5} {nw}"
    
    # add note?
    
    hacker "Then go there and find a way to go to the main reactor.{w=4} {nw}"
    hacker "Once there, activate the remote control.{w=4} {nw}"
    hacker "Then stop the reactor.{w=3} {nw}"
    hacker "Hurry up! The crew robots will try to come to the reactor and restart it.{w=5} {nw}"
    hacker "Go back to your spaceship as fast as possible...{w=4} {nw}"
    hacker "... and connect to the cargo remotely.{w=4} {nw}"
    hacker "Close the fire doors, so the crew robots won't come into the reactor room.{w=5} {nw}"
    hacker "So they won't restart it...{w=3} {nw}"
    hacker "The cooling system is powered by the reactor, so the whole system will overheat.{w=5} {nw}"
    hacker "If we are lucky, this will destroy the cargo ship!{w=4} {nw}"
    
    return
    
    
    
    
