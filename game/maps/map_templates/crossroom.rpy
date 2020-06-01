# MAPS

############################################
label crossroom:
    
    image crossroom = imagemapsdir + "crossroom.png"
    
    scene bgcolor
    show crossroom at truecenter
    show screen notify("crossroom")
    
    show bgcolor behind crossroom
    
    #doors (comment to disable)
    show doorh as doorA:
        pos (400, 55)
    show doorv as doorB:
        pos (587, 240)
    show doorh as doorC:
        pos (400, 427)
    show doorv as doorD:
        pos (215, 240)
    
    
    # set all variables for the map (nodes and path)
    $ nodeA = (400, 75)
    $ nodeB = (570, 240)
    $ nodeC = (400, 410)
    $ nodeD = (235, 240)
    

    $ nodeAA = (400, 240)
    $ nodeBB = (-100, -100)
    $ nodeCC = (-100, -100)
    $ nodeDD = (-100, -100)

    $ pathA = (nodeA, nodeB, nodeC, nodeD, nodeAA, (0, 0), (0, 0), (0, 0))
    $ pathB = (nodeA, nodeB, nodeC, nodeD, nodeAA, (0, 0), (0, 0), (0, 0))
    $ pathC = (nodeA, nodeB, nodeC, nodeD, nodeAA, (0, 0), (0, 0), (0, 0))
    $ pathD = (nodeA, nodeB, nodeC, nodeD, nodeAA, (0, 0), (0, 0), (0, 0))
     
    $ pathAA = (nodeA, nodeB, nodeC, nodeD, nodeAA, (0, 0), (0, 0), (0, 0))
    $ pathBB = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)
    $ pathCC = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)
    $ pathDD = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)


label loop_crossroom:

    # start "move through the map" loop
    call startpos

    # do something at node?
    if exitpos == 1:
        $ startpos = 1 
        jump mapdemos 
        
    if exitpos == 2:
        $ startpos = 2
        jump loop_crossroom
        
    if exitpos == 3:
        $ startpos = 3
        jump loop_crossroom
        
    if exitpos == 4:
        $ startpos = 4
        jump loop_crossroom 
        

    #exits routing "got to map and set position for next map"
    if exitpos == 11:   
        $ startpos = 11     
        jump loop_crossroom   
        
    if exitpos == 22:
        $ startpos = 22
        jump loop_crossroom 
        
    if exitpos == 33:
        $ startpos = 33
        jump loop_crossroom
        
    if exitpos == 44:
        $ startpos = 44
        jump loop_crossroom


