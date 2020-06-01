  
##################################
label map2:

    image map2 = imagemapsdir + "xylo_sea_p2.png"
    
    scene map2
    show screen notify("map2")
    
    show bgcolor behind map2

    image waves = SnowBlossom("images/wave.png", count=100, border=50, xspeed=(5), yspeed=(5), start=0, fast=True, horizontal=True)
    show waves behind map2
    

    
    # set all variables for the map (nodes and path)
    $ nodeA = (400,150)
    $ nodeB = (550,240)
    $ nodeC = (260,330)
    $ nodeD = (170,170)
    
    $ nodeAA = (400,25)
    $ nodeBB = (780,240)
    $ nodeCC = (270,440)
    $ nodeDD = (40,140)
    
    $ pathA = ((0,0), (0,0), (0,0), (0,0), nodeAA, (0,0), (0,0), (0,0))
    $ pathB = (nodeA, (0,0), nodeC, nodeD, (0,0), nodeBB, (0,0), (0,0))
    $ pathC = ((0,0), (0,0), nodeC, nodeD, (0,0),(0,0),nodeCC, (0,0))
    $ pathD = ((0,0), (0,0), nodeC, nodeD, (0,0), (0,0), (0,0), nodeDD)
    
    $ pathAA = (nodeA, (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0))
    $ pathBB = ((0,0), nodeB, (0,0), (0,0), (0,0), (0,0), (0,0), (0,0))
    $ pathCC = ((0,0), (0,0), nodeC, (0,0), (0,0), (0,0), nodeCC, (0,0))
    $ pathDD = ((0,0), (0,0), (0,0), nodeD, (0,0), (0,0), (0,0), nodeDD)


label loop_map2:

    # start "move through the map" loop
    call startpos
    
    # do something at node?
    if exitpos == 1:       #if at node A
        $ startpos = 1     # stay in A
        jump loop_map2          # map to jump to
        
    if exitpos == 2:
        $ startpos = 2
        jump loop_map2
        
    if exitpos == 3:
        $ startpos = 3
        jump loop_map2
        
    if exitpos == 4:
        $ startpos = 4
        
        call find_bulb
        
        jump loop_map2 
    
    #exits routing "got to map"
    if exitpos == 11:       #if going out at AA
        $ startpos = 33     #go to CC
        jump map1           # map to jump to
        
    if exitpos == 22:
        $ startpos = 44
        jump map1
        
    if exitpos == 33:
        $ startpos = 11
        jump map3
        
    if exitpos == 44:
        $ startpos = 22
        jump map1
    




label find_bulb:
    if "bulb" not in inventory:
        
        #call hidepaths
        
        m "There is a light bulb! {w=3.0} {nw}"

        call take_item("bulb")
                
    
    
    return
