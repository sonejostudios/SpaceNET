# MAPS

############################################


label isc_city_spacenet:
    
    stop music
    
    call atmo_spaceship from _call_atmo_spaceship
    
    scene bgcolor
    
    #call show_space
    
    image isc_gateway_spacenet = imagemapsdir + "crossroom.png"
    show isc_gateway_spacenet at truecenter
    
    image spacenetcomp:
        "images/spacenetcomp.png"
        anchor (0.5,0.5)
    
    show spacenetcomp:
        anchor (0.5,0.5)
        pos (400,280)
        rotate 180
        rotate_pad True
        
    show terminalmap:
        anchor (0.5,0.5)
        pos (235, 70)
        
        
    
    show screen notify("server room")
    
    #doors (comment to disable)
    #show doorh as doorA:
    #    pos (400, 55)
    #show doorv as doorB:
    #    pos (587, 240)
    #show doorh as doorC:
    #    pos (400, 427)
    show doorv as doorD:
        pos (215, 240)
    
    
    # set all variables for the map (nodes and path)
    $ nodeA = (240, 240)
    $ nodeB = (237, 110)
    $ nodeC = (495, 200)
    $ nodeD = (430, 325)
    
    $ nodeAA = (400, 240)
    
    $ nodeBB = (400, 140)
    $ nodeCC = (490, 180)
    $ nodeDD = (-100, -100)

    $ pathA = (nodeA, nodeB, nodeC, nodeD, nodeAA, (0, 0), (0, 0), (0, 0))
    $ pathB = (nodeA, nodeB, nodeC, nodeD, nodeAA, (0, 0), (0, 0), (0, 0))
    $ pathC = (nodeA, nodeB, nodeC, nodeD, nodeAA, (0, 0), (0, 0), (0, 0))
    $ pathD = (nodeA, nodeB, nodeC, nodeD, nodeAA, (0, 0), (0, 0), (0, 0))
     
    $ pathAA = (nodeA, nodeB, nodeC, nodeD, nodeAA, (0, 0), (0, 0), (0, 0))
    
    $ pathBB = ((0, 0), (0, 0), nodeC, nodeD, nodeAA, nodeBB, nodeCC, (0, 0))
    $ pathCC = ((0, 0), (0, 0), nodeC, nodeD, nodeAA, nodeBB, nodeCC, (0, 0))
    $ pathDD = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)


label loop_isc_city_spacenet:


    while True:
        # spacenet sender
        if "isc_city" in spacenetnodes:
            show spacenetsender:
                pos (250,390)
                

        # start "move through the map" loop
        call startpos from _call_startpos_1

        # do something at node?
        if exitpos == 1:
            $ startpos = 2
            call sound_door from _call_sound_door_5
            jump isc_gateway_crane_to_spacenet
            
            
        if exitpos == 2:
            if startpos == 2:
                call terminal from _call_terminal
            $ startpos = 2
            
            
        if exitpos == 3: # terminal
            if startpos == 3:
                m "This computer doesn't seem to work. {w=2} {nw}"
                m "Is it broken? {w=2} {nw}"
            $ startpos = 3
            
        if exitpos == 4:
            if startpos == 4:
                jump isc_city_spacenet_comp
            $ startpos = 4

            

        #exits routing "got to map and set position for next map"
        if exitpos == 11:
            if startpos == 11:
                m "This room is full of computers. {w=2} {nw}"
            $ startpos = 11      
            
        if exitpos == 22:
            $ startpos = 22

            
        if exitpos == 33:
            $ startpos = 33
            
        if exitpos == 44:
            $ startpos = 44






label isc_city_spacenet_comp:
    show terminal at topleft
    if shadow_enable == 1:
        show shadow:
            pos (270, 240)
    call sound_beep from _call_sound_beep
    
    call spacenet_comp("isc_city") from _call_spacenet_comp # install spacenet
    
    jump isc_city_spacenet
    

    

