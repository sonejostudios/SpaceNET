# MAPS

############################################

label xylo_minitrain2:
    $ pnc_nodes_visible = True
    
    stop sound fadeout 1.0
    call atmo_base
    
    call music_xylo_mine
    
    image xylo_minitrain = imagemapsdir + "xylo_minitrain.png"
    
    #show screen notify("other side")
    
    scene bgcolor
    
    show xylo_minitrain:
        anchor (1400,840)
        pos (400,240)

    
    show circle:
        anchor (0.5,0.5)
        pos (400,260)
        zoom 0.3
    
    
    
    # set all variables for the map (nodes and path)
    $ nodeA = (550, 280)
    $ nodeB = (406, 85)
    $ nodeC = (400, 260)
    $ nodeD = (644, 443)

    $ nodeAA = (684, 445)
    $ nodeBB = (715, 444)
    $ nodeCC = (743, 445)
    $ nodeDD = (771, 417)

    $ pathA = (nodeA, (0, 0), nodeC, (0, 0), (0, 0), (0, 0), (0, 0), (0, 0))
    $ pathB = ((0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0))
    $ pathC = (nodeA, (0, 0), nodeC, (0, 0), (0, 0), (0, 0), (0, 0), (0, 0))
    $ pathD = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)
     
    $ pathAA = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)
    $ pathBB = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)
    $ pathCC = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)
    $ pathDD = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)


label loop_xylo_minitrain2:

    # start "move through the map" loop
    call startpos

    # do something at node?
    if exitpos == 1:      
        call sound_door
        $ startpos = 1   
        jump xylo_mine_minitrain_room
        
    if exitpos == 2:
        $ startpos = 2
        jump loop_xylo_minitrain2
        
    if exitpos == 3: 
        $ startpos = 3
        $ pnc_nodes_visible = False
        jump minitrain_cross10
        
    if exitpos == 4:
        $ startpos = 4
        jump loop_xylo_minitrain2 
        

    #exits routing "got to map and set position for next map"
    if exitpos == 11:       #if going out at AA
        $ startpos = 11    #go to CC
        jump loop_xylo_minitrain2          # map to jump to
        
    if exitpos == 22:
        $ startpos = 22
        
        $liftpos = 3
        call sound_door
        jump loop_xylo_minitrain2 # go to lift
        
    if exitpos == 33:
        $ startpos = 33
        jump loop_xylo_minitrain2
        
    if exitpos == 44:
        $ startpos = 44

        jump loop_xylo_minitrain2




label minitrain_cross10:
    #"10"
    
    call sound_minitrain_loop
    
    $ path = ((0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0))
    call hidepaths
    
    show xylo_minitrain:
        easeout 2 anchor (1400,640)
        linear 5 anchor (700, 640)
    pause 7

    jump minitrain_loopback
    
    

