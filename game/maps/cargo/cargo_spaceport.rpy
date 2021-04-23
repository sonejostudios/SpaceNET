# MAPS

############################################
label cargo_spaceport:
    $ pnc_nodes_visible = True
    
    call atmo_spaceport from _call_atmo_spaceport_1
    
    
    image cargo_spaceport = imagemapsdir + "cargo_spaceport.png"
    
    scene bgcolor
    show screen notify("maintenance shaft")
    
    show cargo_spaceport
    
    
    #show warningfloor:
    #    anchor (0.5,0.5)
    #    pos (570,240)
    #    rotate 90
    
    #show light:
    #    pos (145,130)
        
    #show light as light2:
    #    pos (355,130)
        
    #show light as light3:
    #    pos (145,345)
        
    #show light as light4:
    #    pos (355,345)
        

    # check if spaceship is landing on this map or not
    # $ landing = False
    # $ landing = True
    call landing_anim from _call_landing_anim_1
    
    
    # set all variables for the map (nodes and path)
    $ nodeA = (-100,-100) #(467,47)
    $ nodeB = (388,240)
    $ nodeC = (-100,-100) #(470,420)
    $ nodeD = (250,240)
    
    $ nodeAA = (400,25)
    $ nodeBB = (670,240)
    $ nodeCC = (400,460)
    $ nodeDD = (315,240)
    
    $ pathA = (nodeA, nodeB, nodeC, (0,0), (0,0), nodeBB, (0,0), nodeDD)
    $ pathB = ((0,0), nodeB, nodeC, (0,0), (0,0), (0,0), (0,0), nodeDD)
    $ pathC = (nodeA, nodeB, nodeC, (0,0), (0,0), nodeBB, (0,0), nodeDD)
    $ pathD = ((0,0), nodeB, nodeC, (0,0), (0,0), (0,0), (0,0), nodeDD)
    
    $ pathAA = (nodeA, (0,0), (0,0), (0,0), nodeAA, (0,0), (0,0), (0,0))
    $ pathBB = (nodeA, nodeB, nodeC, (0,0), (0,0), nodeBB, (0,0), nodeDD)
    $ pathCC = ((0,0), (0,0), nodeC, (0,0), (0,0), (0,0), nodeCC, (0,0))
    $ pathDD = ((0,0), nodeB, nodeC, (0,0), (0,0), (0,0), (0,0), nodeDD)


label loop_cargo_spaceport:
    
    # alarm
    call alarm_check from _call_alarm_check_7

    # start "move through the map" loop
    call startpos from _call_startpos_22

    # do something at node?
    if exitpos == 1:       #if at node A
        $ startpos = 1     # stay in A
        
        jump loop_cargo_spaceport          # map loop to jump to
        
    if exitpos == 2:
        $ startpos = 1
        
        #call dialog_closed # door
        call sound_door from _call_sound_door_46
        
        #jump cargo_multimap1
        jump cargo_movingwalls # to movingwalls
        
    if exitpos == 3: # switch board
        $ startpos = 3

        jump loop_cargo_spaceport
        
    if exitpos == 4:
        $ startpos = 4
        jump loop_cargo_spaceport 
        

    #exits routing "got to map and set position for next map"
    if exitpos == 11:       #if going out at AA
        $ startpos = 11    #go to CC
        jump loop_cargo_spaceport          # map to jump to
        
    if exitpos == 22:
        $ startpos = 22
        
        $liftpos = 3
        call sound_door from _call_sound_door_47
        jump loop_cargo_spaceport # go to lift
        
    if exitpos == 33:
        $ startpos = 33
        jump loop_cargo_spaceport
        
    if exitpos == 44:
        $ startpos = 44
        call sound_door from _call_sound_door_48
        call takeoff_anim("withmenu") from _call_takeoff_anim_2 # go to takeoff
        $ pnc_nodes_visible = True
        
        
        # straight to space
        if takeoftospace == True:
            $ takeoftospace = False
            $ space_anim = True
            
            $ alarm_on = False
            
            $ pnc_nodes_visible = False
            
            jump space

        
        # to surface
        if landing == True:
            $ shippos = (200,400) # set position in surface engine
            jump cargo_anim_up
            
        jump loop_cargo_spaceport




