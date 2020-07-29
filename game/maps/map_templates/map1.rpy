# MAPS

############################################
label map1:
    
    image map1 = imagemapsdir + "xylo_sea_map1.png"
    
    scene map1
    show screen notify("map1")
    

    show propeller:
        pos (663,86)
        linear 10 rotate 180.0
        rotate 0
        repeat
    

    
    # set all variables for the map (nodes and path)
    $ nodeA = (400,150)
    $ nodeB = (550,240)
    $ nodeC = (400,350)
    $ nodeD = (250,240)
    
    $ nodeAA = (400,25)
    $ nodeBB = (780,240)
    $ nodeCC = (400,460)
    $ nodeDD = (110,235)
    
    $ pathA = (nodeA, nodeB, (0,0), (0,0), nodeAA, (0,0), (0,0), (0,0))
    $ pathB = (nodeA, nodeB, nodeC, nodeD, (0,0), nodeBB, (0,0), nodeDD)
    $ pathC = ((0,0), nodeB, nodeC, nodeD, (0,0), (0,0), nodeCC, (0,0))
    $ pathD = ((0,0), nodeB, nodeC, nodeD, (0,0), nodeBB, (0,0), nodeDD)
    
    $ pathAA = (nodeA, (0,0), (0,0), (0,0), nodeAA, (0,0), (0,0), (0,0))
    $ pathBB = ((0,0), nodeB, (0,0), nodeD, (0,0), nodeBB, (0,0), nodeDD)
    $ pathCC = ((0,0), (0,0), nodeC, (0,0), (0,0), (0,0), nodeCC, (0,0))
    $ pathDD = ((0,0), nodeB, (0,0), nodeD, (0,0), nodeBB, (0,0), nodeDD)


label loop_map1:

    # start "move through the map" loop
    call startpos from _call_startpos_63

    # do something at node?
    if exitpos == 1:       #if at node A
        $ startpos = 1     # stay in A
        jump loop_map1          # map to jump to
        
    if exitpos == 2:
        $ startpos = 2
        jump loop_map1
        
    if exitpos == 3:
        $ startpos = 3
        jump loop_map1
        
    if exitpos == 4:
        $ startpos = 4
        jump loop_map1 
        

    #exits routing "got to map and set position for next map"
    if exitpos == 11:       #if going out at AA
        $ startpos = 33     #go to CC
        jump map7         # map to jump to
        
    if exitpos == 22:
        $ startpos = 44
        jump map2
        
    if exitpos == 33:
        $ startpos = 11
        jump map4
        
    if exitpos == 44:
        #$ startpos = 22
        call sound_door from _call_sound_door_139
        jump lift1
