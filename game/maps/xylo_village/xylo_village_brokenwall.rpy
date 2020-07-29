# MAPS

############################################


label xylo_village_brokenwall:
    
    image crossroomsmall = imagemapsdir + "crossroomsmall.png"
    
    scene bgcolor
    show crossroomsmall at truecenter
    show screen notify("secret room")


    show brokenwall open:
        pos (397,344)
        
    #show tube behind crossroomsmall at truecenter
    
    
    $ landing = False
    
    
    # set all variables for the map (nodes and path)
    $ nodeA = (400, 160)
    $ nodeB = (480, 240)
    $ nodeC = (400, 320)
    $ nodeD = (320, 240)
    

    $ nodeAA = (400, 240)
    $ nodeBB = (-100, -100)
    $ nodeCC = (-100, -100)
    $ nodeDD = (-100, -100)

    $ pathA = (nodeA, nodeB, nodeC, nodeD, (0, 0), (0, 0), (0, 0), (0, 0))
    $ pathB = (nodeA, nodeB, nodeC, nodeD, (0, 0), (0, 0), (0, 0), (0, 0))
    $ pathC = ((0, 0), (0, 0), nodeC, (0, 0), nodeAA, (0, 0), (0, 0), (0, 0))
    $ pathD = (nodeA, nodeB, nodeC, nodeD, (0, 0), (0, 0), (0, 0), (0, 0))
     
    $ pathAA = ((0, 0), (0, 0), nodeC, (0, 0), nodeAA, (0, 0), (0, 0), (0, 0))
    $ pathBB = (nodeA, nodeB, nodeC, nodeD, (0, 0), (0, 0), (0, 0), (0, 0))
    $ pathCC = (nodeA, nodeB, nodeC, nodeD, (0, 0), (0, 0), (0, 0), (0, 0))
    $ pathDD = (nodeA, nodeB, nodeC, nodeD, (0, 0), (0, 0), (0, 0), (0, 0))
    


label loop_xylo_village_brokenwall:

    while True:

        # start "move through the map" loop
        call startpos from _call_startpos_21
        

        # do something at node?
        if exitpos == 1:
            $ startpos = 1 

            
        if exitpos == 2:
            $ startpos = 2
            

        if exitpos == 3:
            $ startpos = 4
            jump xylo_spaceport

            
            
        if exitpos == 4:
            $ startpos = 4


        #######
        
        if exitpos == 11:
            if startpos == 11:
                if xylo_village_brokenwall_gem == True:
                    call take_gem from _call_take_gem_3
                    $ xylo_village_brokenwall_gem = False
                else:
                    call dialog_nothing from _call_dialog_nothing_23
            $ startpos = 11
 
            
        if exitpos == 22:
            $ startpos = 22

            
        if exitpos == 33:
            $ startpos = 33

            
        if exitpos == 44:
            $ startpos = 44









