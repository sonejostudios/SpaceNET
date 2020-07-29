
###########################################
label map3:
    
    image map3 = imagemapsdir + "xylo_sea_p3.png"
    
    scene map3
    show screen notify("map3")
    
    show bgcolor behind map3
    show waves behind map3


    
    # set all variables for the map (nodes and path)
    $ nodeA = (300,150)
    $ nodeB = (520,130)
    $ nodeC = (670,250)
    $ nodeD = (540,360)
    
    $ nodeAA = (260,40)
    $ nodeBB = (780,240)
    $ nodeCC = (400,460)
    $ nodeDD = (40,350)
    
    $ pathA = (nodeA, nodeB, (0,0), (0,0), nodeAA, (0,0), (0,0), (0,0))
    $ pathB = (nodeA, nodeB, nodeC, (0,0), (0,0), (0,0), (0,0), (0,0))
    $ pathC = ((0,0), nodeB, nodeC, nodeD, (0,0),(0,0),(0,0), (0,0))
    $ pathD = ((0,0), (0,0), nodeC, nodeD, (0,0), (0,0), (0,0), nodeDD)
    
    $ pathAA = (nodeA, (0,0), (0,0), (0,0), nodeAA, (0,0), (0,0), (0,0))
    $ pathBB = ((0,0), nodeB, (0,0), (0,0), (0,0), (0,0), (0,0), (0,0))
    $ pathCC = ((0,0), (0,0), nodeC, (0,0), (0,0), (0,0), (0,0), (0,0))
    $ pathDD = ((0,0), (0,0), (0,0), nodeD, (0,0), (0,0), (0,0), nodeDD)

label loop_map3:

    # start "move through the map" loop
    call startpos from _call_startpos_45
    
    # do something at node?
    if exitpos == 1:       #if at node A
        $ startpos = 1     # stay in A
        jump loop_map3          # map to jump to
        
    if exitpos == 2:
        $ startpos = 2
        m "This way is very interesting! {w=3.0} {nw}"
        jump loop_map3
        
    if exitpos == 3:
        $ startpos = 3
        jump loop_map3
        
    if exitpos == 4:
        $ startpos = 4
        jump loop_map3 
    
    #exits routing "got to map"
    if exitpos == 11:    #if going out at AA
        $ startpos = 33    #go to CC
        jump map2           # map to jump to
        
    if exitpos == 22:
        $ startpos = 44
        jump map2
        
    if exitpos == 33:
        $ startpos = 11
        jump map2
        
    if exitpos == 44:
        $ startpos = 22
        jump map4
        
  
