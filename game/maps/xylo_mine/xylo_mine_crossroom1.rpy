# MAPS

############################################
label xylo_mine_crossroom1:
    
    
    call atmo_cave
    
    image crossroom = imagemapsdir + "crossroom.png"
    
    scene bgcolor
    show crossroom at truecenter
    show screen notify("maintenance room")
    
    show bgcolor behind crossroom
    
    # set darkroom to True
    #$ darkroom = True
    
    show warningfloor:
        anchor (0.5,0.5)
        pos (470,240)
        rotate 90
        
    show warningfloor as warningfloor2:
        anchor (0.5,0.5)
        pos (400,340)
    
    #doors (comment to disable)
    #show doorh as doorA:
    #    pos (400, 55)
    show doorv as doorB:
        pos (587, 240)
    show doorh as doorC:
        pos (400, 427)
    show doorv as doorD:
        pos (215, 240)
        
    
    # set all variables for the map (nodes and path)
    $ nodeA = (-100,-100) #(400, 75)
    $ nodeB = (565, 240)
    $ nodeC = (400, 405)
    $ nodeD = (235, 240)
    

    $ nodeAA = (400, 240)
    $ nodeBB = (-100, -100)
    $ nodeCC = (-100, -100)
    $ nodeDD = (-100, -100)

    $ pathA = ((0, 0), nodeB, nodeC, nodeD, nodeAA, (0, 0), (0, 0), (0, 0))
    $ pathB = ((0, 0), nodeB, nodeC, nodeD, nodeAA, (0, 0), (0, 0), (0, 0))
    $ pathC = ((0, 0), nodeB, nodeC, nodeD, nodeAA, (0, 0), (0, 0), (0, 0))
    $ pathD = ((0, 0), nodeB, nodeC, nodeD, nodeAA, (0, 0), (0, 0), (0, 0))
     
    $ pathAA = ((0, 0), nodeB, nodeC, nodeD, nodeAA, (0, 0), (0, 0), (0, 0))
    $ pathBB = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)
    $ pathCC = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)
    $ pathDD = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)
    
    




label loop_xylo_mine_crossroom1:
    
    
    #darkroom (in moveengine)
    if darkroom == True:
        call darkroom
    else:
        hide  darkroombg
        #reset paths
        $ pathB = (nodeA, nodeB, nodeC, nodeD, nodeAA, (0, 0), (0, 0), (0, 0))
        $ pathC = (nodeA, nodeB, nodeC, nodeD, nodeAA, (0, 0), (0, 0), (0, 0))
        $ pathD = (nodeA, nodeB, nodeC, nodeD, nodeAA, (0, 0), (0, 0), (0, 0))
        
        $ inventory_select = "lamp"
        call use_and_keep_item
        
        


    # start "move through the map" loop
    call startpos
    

    # do something at node?
    if exitpos == 1:
        
        $ startpos = 1 
        jump loop_xylo_mine_crossroom1 
        
    if exitpos == 2:

        $ startpos = 2
        
        # special use of node B with darkroom
        if inventory_select == "lamp":
            call use_and_keep_item
            call sound_connected
            #with flash
            $ darkroom = False
            jump loop_xylo_mine_crossroom1
        else:
            call sound_door
            $ liftpos = 0
            #stop music
            jump xylo_mine_lift1
            
            

    if exitpos == 3: # jump to xylo mine multimap
        
        # special use of node D with darkroom
        if inventory_select == "lamp":
            $ startpos = 3
            $ darkroom = False
            jump loop_xylo_mine_crossroom1
            
        else:
            call sound_door
            $ startpos = 2
            $ multiposx = 2
            $ multiposy = 0
            jump xylo_mine_multimap1
        
        
    if exitpos == 4:
        $ startpos = 4

        # special use of node D with darkroom
        if inventory_select == "lamp":
            $ darkroom = False
            jump loop_xylo_mine_crossroom1
        else:
            call sound_door
            $ liftpos = 3
            jump xylo_mine_lift2

        

    #exits routing "got to map and set position for next map"
    if exitpos == 11:
        if startpos == 11:
            call dialog_nothing
        $ startpos = 11     
        jump loop_xylo_mine_crossroom1   
        
    if exitpos == 22:
        $ startpos = 22
        jump loop_xylo_mine_crossroom1 
        
    if exitpos == 33:
        $ startpos = 33
        jump loop_xylo_mine_crossroom1
        
    if exitpos == 44:
        $ startpos = 44
        jump loop_xylo_mine_crossroom1








