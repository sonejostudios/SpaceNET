# MAPS

############################################




label xylo_sea_bunker_spacenet:
    
    stop music
    call atmo_spaceship from _call_atmo_spaceship_3
    
    scene bgcolor
    
    image xylo_sea_bunker_spacenet = imagemapsdir + "crossroom.png"
    show xylo_sea_bunker_spacenet at truecenter
    
    image spacenetcomp:
        "images/spacenetcomp.png"
        anchor (0.5,0.5)
    
    show spacenetcomp:
        pos (365,240)
        rotate 270
        rotate_pad True
        
    show terminalmap:
        anchor (0.5,0.5)
        pos (570, 200)
        
        

                
    
    
    show screen notify("server room")
    
    #doors (comment to disable)
    show doorh as doorA:
        pos (400, 55)
    #show doorv as doorB:
    #    pos (587, 240)
    #show doorh as doorC:
    #    pos (400, 427)
    #show doorv as doorD:
    #    pos (215, 240)
    
    
    # set all variables for the map (nodes and path)
    $ nodeA = (400, 75)
    $ nodeB = (530, 200)
    $ nodeC = (400, 337)
    $ nodeD = (313, 240)
    
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


label loop_xylo_sea_bunker_spacenet:
    
    while True:
        # spacenet sender
        if "xylo_sea" in spacenetnodes:
            show spacenetsender:
                pos (480,400)
                

        # start "move through the map" loop
        call startpos from _call_startpos_46

        # do something at node?
        if exitpos == 1:
            $ startpos = 1
            call sound_door from _call_sound_door_107
            jump xylo_sea_bunker_lift1
            
        if exitpos == 2:
            if startpos == 2:
                if "xylo_sea" in spacenetnodes:
                    call terminal from _call_terminal_9
                else:
                    m "This terminal is not working right now. {w=2.5} {nw}"
               
            $ startpos = 2
            
        if exitpos == 3:
            if startpos == 3:
                jump xylo_sea_bunker_spacenet_comp
            $ startpos = 3
            
        if exitpos == 4:
            if startpos == 4:
                m "This one is not working. {w=2} {nw}"
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






label xylo_sea_bunker_spacenet_comp:
    show terminal at topleft
    if shadow_enable == 1:
        show shadow:
            pos (270, 240)
    call sound_beep from _call_sound_beep_35
    
    call spacenet_comp("xylo_sea") from _call_spacenet_comp_1 # install spacenet
    
    jump xylo_sea_bunker_spacenet
    

    


