# MAPS



# prison cell with gem

############################################
label megaship_cell2:
    
    call atmo_spaceship_hum
    
    show screen notify("prison cell 2")
    
    scene bgcolor 
    show megaship_cell    
    
    show sink:
        anchor (0.5,0.5)
        pos (200, 340)
    show wc:
        anchor (0.5,0.5)
        rotate 180
        pos (150,330)

    
    # set all variables for the map (nodes and path)
    $ nodeA = (401, 330)
    $ nodeB = (520, 260)
    $ nodeC = (288, 230)
    $ nodeD = (200, 305)

    $ nodeAA = (11, 12)
    $ nodeBB = (640, 240)
    $ nodeCC = (159, 240)
    $ nodeDD = (47, 13)

    $ pathA = (nodeA, nodeB, nodeC, (0, 0), (0, 0), (0, 0), (0, 0), (0, 0))
    $ pathB = (nodeA, nodeB, nodeC, (0, 0), (0, 0), nodeBB, nodeCC, (0, 0))
    $ pathC = (nodeA, nodeB, nodeC, nodeD, (0, 0), nodeBB, nodeCC, (0, 0))
    $ pathD = ((0, 0), (0, 0), nodeC, nodeD, (0, 0), (0, 0), nodeCC, (0, 0))
     
    $ pathAA = ((0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0))
    $ pathBB = ((0, 0), nodeB, nodeC, (0, 0), (0, 0), nodeBB, nodeCC, (0, 0))
    $ pathCC = ((0, 0), nodeB, nodeC, nodeD, (0, 0), nodeBB, nodeCC, (0, 0))
    $ pathDD = ((0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0))


label loop_megaship_cell2:
    
    
    while True:
        # start "move through the map" loop
        call startpos

        # do something at node?
        if exitpos == 1:
            if startpos == 1:
                if megaship_cell2_gem == True:
                    call take_gem
                    $ megaship_cell2_gem = False
                else:
                    m "I'm in cell number 2. {w=2.0} {nw}"
            $ startpos = 1   

            
        if exitpos == 2: # gem
            if startpos == 2:
                m "This is a table.{w=2.0} {nw}"
                call dialog_nothing
                
            $ startpos = 2

            
        if exitpos == 3: 
            if startpos == 3:
                m "This is a bed.{w=2.0} {nw}"
                call dialog_nothing
            $ startpos = 3

            
        if exitpos == 4:
            if startpos == 4:
                m "This is the sink and the wc.{w=2.0} {nw}"
                call dialog_nothing
            $ startpos = 4

            

        #exits routing "got to map and set position for next map"
        if exitpos == 11:       
            $ startpos = 11        
 
            
        if exitpos == 22:
            $ startpos = 22
            call dialog_closed
            

            
        if exitpos == 33:
            call sound_screw
            $ startpos = 2
            jump megaship_aeration
            $ startpos = 33

            
        if exitpos == 44:
            $ startpos = 44

