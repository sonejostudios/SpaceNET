# MAPS



############################################
label cargo_aeration:
    
    call atmo_base from _call_atmo_base_5
    
    
    scene bgcolor
    show screen notify("cargo reactor")
    
    image cargo_aeration = imagemapsdir + "cargo_aeration.png"
    show cargo_aeration
    


    # set all variables for the map (nodes and path)
    $ nodeA = (25, 107)
    $ nodeB = (414, 107)
    $ nodeC = (414, 403)
    $ nodeD = (770, 403)

    $ nodeAA = (744, 425)
    $ nodeBB = (704, 427)
    $ nodeCC = (661, 427)
    $ nodeDD = (614, 429)

    $ pathA = (nodeA, nodeB, (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0))
    $ pathB = (nodeA, nodeB, nodeC, (0, 0), (0, 0), (0, 0), (0, 0), (0, 0))
    $ pathC = ((0, 0), nodeB, nodeC, nodeD, (0, 0), (0, 0), (0, 0), (0, 0))
    $ pathD = ((0, 0), (0, 0), nodeC, nodeD, (0, 0), (0, 0), (0, 0), (0, 0))
     
    $ pathAA = ((0, 0), (0, 0), (0, 0), nodeD, nodeAA, (0, 0), (0, 0), (0, 0))
    $ pathBB = ((0, 0), nodeB, nodeC, (0, 0), (0, 0), nodeBB, nodeCC, (0, 0))
    $ pathCC = (nodeA, nodeB, nodeC, nodeD, (0, 0), nodeBB, nodeCC, (0, 0))
    $ pathDD = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)
    
    


label loop_cargo_aeration:

    while True:
        
        # alarm
        call alarm_check from _call_alarm_check_11
        
        # start "move through the map" loop
        call startpos from _call_startpos_44

        # do something at node?
        if exitpos == 1:
            $ startpos = 11
            jump cargo_smallroom_tube


            
        if exitpos == 2:
            $ startpos = 2
            
        if exitpos == 3:
            $ startpos = 3
            
        if exitpos == 4:
            
            $ startpos = 1
            jump cargo_conveyor2
            

        #conveyor animation out
        if exitpos == 11:
            $ startpos = 11
              
            
            
        if exitpos == 22:
            $ startpos = 22
            
            
        if exitpos == 33:
            $ startpos = 33

            
        if exitpos == 44:
            $ startpos = 44


