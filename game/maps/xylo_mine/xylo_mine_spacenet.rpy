# MAPS

############################################


screen xylo_mine_spacenet_earthquake:
    
    timer 7 repeat True action Jump("xylo_mine_spacenet_earthquake")


label xylo_mine_spacenet:
    
    stop music
    call atmo_spaceship from _call_atmo_spaceship_5
    
    scene bgcolor
    
    image xylo_mine_spacenet = imagemapsdir + "crossroom.png"
    show xylo_mine_spacenet at truecenter
    
    image spacenetcomp:
        "images/spacenetcomp.png"
        anchor (0.5,0.5)
    
    show spacenetcomp:
        pos (365,240)
        rotate 270
        rotate_pad True
        
    show terminalmap:
        anchor (0.5,0.5)
        pos (570, 278)
        
        
    
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
    $ nodeB = (530, 278)
    $ nodeC = (400, 337)
    $ nodeD = (312, 240)
    
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


label loop_xylo_mine_spacenet:
    
    show screen xylo_mine_spacenet_earthquake
    
    $ xylo_mine_spacenet_earthquake_position = ""
    
    while True:
        # spacenet sender
        if "xylo_mine" in spacenetnodes:
            show spacenetsender:
                pos (256,95)
                

        # start "move through the map" loop
        call startpos from _call_startpos_57

        # do something at node?
        if exitpos == 1:
            $ startpos = 22
            hide screen xylo_mine_spacenet_earthquake
            call sound_door from _call_sound_door_126
            jump xylo_mine_level1
            
        if exitpos == 2:
            if startpos == 2:
                hide screen xylo_mine_spacenet_earthquake
                call terminal from _call_terminal_11
            $ startpos = 2
            jump loop_xylo_mine_spacenet
            
        if exitpos == 3: # terminal
            if startpos == 3:
                m "This computer seems to work automatically. {w=2} {nw}"
                m "I can't do anything with it. {w=2} {nw}"
            $ startpos = 3
            
        if exitpos == 4:
            if startpos == 4:
                hide screen xylo_mine_spacenet_earthquake
                jump xylo_mine_spacenet_comp
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






label xylo_mine_spacenet_comp:
    show terminal at topleft
    if shadow_enable == 1:
        show shadow:
            pos (270, 240)
    call sound_beep from _call_sound_beep_36
    
    call spacenet_comp("xylo_mine") from _call_spacenet_comp_2 # install spacenet
    
    jump xylo_mine_spacenet
    

    



label xylo_mine_spacenet_earthquake:
            
    call sound_earthquake from _call_sound_earthquake_2
    with hpunch
    
    if xylo_mine_used_dynamite_dialog == False:
        $ xylo_mine_used_dynamite_dialog = True
        m "I think the explosion was too loud... {w=2} {nw}"
        m "I just triggered sismic activity ! {w=2} {nw}"
        m "I definitely should't stay here longer... {w=2} {nw}"
        

    jump loop_xylo_mine_spacenet

