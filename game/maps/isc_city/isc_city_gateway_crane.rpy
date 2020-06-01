# MAPS

############################################


label isc_city_gateway_crane:
    
    #$ inventory = ["newspaper", "screwdriver", "spacesuit", "lamp", "bulb", "mirror", "spacenet", "accesscard", "rope", 
    #                "cable", "pick", "dynamite", "minidroid", "gem", "star", "notebook", "laser", "key", "letter", "hook", "magnet"]
    
    #$ inventory = []
    
    $ inventory_select = "spacesuit"
    call use_and_keep_item
    
    
    scene bgcolor
    
    call show_space
    
    show crane as crane2:
        anchor (0.5, 0.5)
        pos (399, 240)
    

    
    show crane:
        anchor (0.5, 0.5)
        pos (201, 240)
        rotate 90
        
        
    show crane as crane3:
        anchor (0.5, 0.5)
        pos (600, 141)
        rotate 90
        
    show crane as crane4:
        anchor (0.5, 0.5)
        pos (500, 341)
        rotate 90
        
        


    
    # set all variables for the map (nodes and path)
    $ nodeA = (50,240) #(467,47)
    $ nodeB = (400,240)
    $ nodeC = (400,141) #(470,420)
    $ nodeD = (748,141) 
    
    $ nodeAA = (400,341)
    $ nodeBB = (700,341)
    $ nodeCC = (400,460)
    $ nodeDD = (320,240)
    
    
    $ pathA = (nodeA, nodeB, (0,0), (0,0), (0,0), (0,0), (0,0), (0,0))
    $ pathB = (nodeA, nodeB, nodeC, (0,0), nodeAA, (0,0), (0,0), (0,0))
    $ pathC = ((0,0), nodeB, nodeC, nodeD, nodeAA, (0,0), (0,0), (0,0))
    $ pathD = ((0,0), (0,0), nodeC, nodeD, (0,0), (0,0), (0,0), (0,0))
    
    $ pathAA = ((0,0), nodeB, nodeC, (0,0), nodeAA, nodeBB, (0,0), (0,0))
    $ pathBB = ((0,0), (0,0), (0,0), (0,0), nodeAA, nodeBB, (0,0), (0,0))
    $ pathCC = ((0,0), (0,0), nodeC, (0,0), (0,0), (0,0), nodeCC, (0,0))
    $ pathDD = ((0,0), (0,0), (0,0), (0,0), (0,0), nodeBB, (0,0), nodeDD)
    
    

    show hexagon:
        #anchor (0.5, 0.5)
        pos (nodeC[0]-1, nodeC[1])
        
    show hexagon as hexagon2:
        #anchor (0.5, 0.5)
        pos (nodeB[0]-1, nodeB[1])
        
    show hexagon as hexagon3:
        #anchor (0.5, 0.5)
        pos (nodeAA[0]-1, nodeAA[1])
        
        
        


label loop_isc_city_gateway_crane:
    
    while True:

        # start "move through the map" loop
        call startpos

        # do something at node?
        if exitpos == 1:       #if at node A
            $ startpos = 3
            jump isc_city_gateway

            
        if exitpos == 2:
            if startpos == 2:
                call dialog_nothing
            
            $ startpos = 2

            
        if exitpos == 3:
            if startpos == 3:
                call dialog_nothing
            $ startpos = 3

            
        if exitpos == 4: # go to spacenet
            $ startpos = 1
            jump isc_gateway_crane_to_spacenet
            

            

        #exits routing "got to map and set position for next map"
        if exitpos == 11:       #if going out at AA
            if startpos == 11:
                call dialog_nothing
            $ startpos = 11    #go to CC

            
        if exitpos == 22:
            if startpos == 22:
                if "magnet" not in inventory:
                    m "There is something glueing to the crane...{w=2} {nw}"
                    m "Wait... {w=1}this is a magnet! {w=2} {nw}"
                    call take_item("magnet")
                else:
                    m "The view is unbelievable!{w=2} {nw}"
                    
            $ startpos = 22
            

            
        if exitpos == 33:
            $ startpos = 33

            
        if exitpos == 44:
            $ startpos = 44

                

