# MAPS

init:
    $ megaship_cell2 = False
    $ megaship_cell3 = False


############################################
label megaship_aeration:
    
    call atmo_spaceship_hum
    
    image megaship_aeration = imagemapsdir + "megaship_aeration.png"
    
    scene megaship_aeration
    show screen notify("prison aeration")
    
    show bgcolor behind megaship_aeration    
    
    
    # set all variables for the map (nodes and path)
    $ nodeA = (293, 38)
    $ nodeB = (293, 173)
    $ nodeC = (293, 313)
    $ nodeD = (293, 445)

    $ nodeAA = (556, 450)
    $ nodeBB = (49, 72)
    $ nodeCC = (100, 100)
    $ nodeDD = (74, 152)

    $ pathA = (nodeA, nodeB, nodeC, nodeD, (0, 0), (0, 0), (0, 0), (0, 0))
    $ pathB = (nodeA, nodeB, nodeC, nodeD, (0, 0), (0, 0), (0, 0), (0, 0))
    $ pathC = (nodeA, nodeB, nodeC, nodeD, (0, 0), (0, 0), (0, 0), (0, 0))
    $ pathD = (nodeA, nodeB, nodeC, nodeD, nodeAA, (0, 0), (0, 0), (0, 0))
     
    $ pathAA = ((0, 0), (0, 0), (0, 0), nodeD, nodeAA, (0, 0), (0, 0), (0, 0))
    $ pathBB = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)
    $ pathCC = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)
    $ pathDD = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)


label loop_megaship_aeration:
    
    while True:
        # start "move through the map" loop
        call startpos

        # do something at node?
        if exitpos == 1:
            if startpos == 1:
                call sound_screw
                $ startpos = 33 
                jump megaship_cell 
            $ startpos = 1
            
        if exitpos == 2:
            if startpos == 2:
                if megaship_cell2 == False:
                    if inventory_select == "laser":
                        
                        m "I can cut the areation grid with this laser tool. {w=3.0} {nw}"
                        m "Let's do it! {w=1.5} {nw}"
                        call use_and_keep_item
                        call sound_electroshock
                        with flash
                        $ megaship_cell2 = True
                
                    else:
                        call dialog_closed
                        m "How to cut this metal grid? {w=3} {nw}"
                else:
                    call sound_screw
                    $ startpos = 33 
                    jump megaship_cell2
                    
                
            $ startpos = 2

            
        if exitpos == 3:
            if startpos == 3:
                if megaship_cell3 == False:
                    if inventory_select == "laser":
                        
                        call use_and_keep_item
                        call sound_electroshock
                        with flash
                        $ megaship_cell3 = True
                        m "Great tool, this laser. {w=2.0} {nw}"
                
                    else:
                        call dialog_closed
                        m "I'll need a metal cutting tool to open this. {w=3} {nw}"
                else:
                    call sound_screw
                    $ startpos = 33 
                    jump megaship_cell3
                    
            $ startpos = 3

            
        if exitpos == 4:
            $ startpos = 4

            

        #exits routing "got to map and set position for next map"
        if exitpos == 11:
            call sound_screw    
            $ startpos = 1       
            jump megaship_prison   
            
        if exitpos == 22:
            if startpos == 22:
                call dialog_closed
            $ startpos = 22
            

            
        if exitpos == 33:
            $ startpos = 33

            
        if exitpos == 44:
            $ startpos = 44



