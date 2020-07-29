# MAPS

############################################
label map6:
    
    image map6 = imagemapsdir + "spaceportlift.png"
    
    scene map6
    show screen notify("spaceport")
    
    show bgcolor behind map6
    
    show buttonscreen:
        pos (468, 444) 
    

    
    show light:
        pos (145,130)
        
    show light as light2:
        pos (355,130)
        
    show light as light3:
        pos (145,345)
        
    show light as light4:
        pos (355,345)
        

    # check if spaceship is landing on this map or not
    # $ landing = False
    # $ landing = True
    call landing_anim from _call_landing_anim_5
    
    
    # set all variables for the map (nodes and path)
    $ nodeA = (467,47)
    $ nodeB = (470,240)
    $ nodeC = (470,420)
    $ nodeD = (250,240)
    
    $ nodeAA = (400,25)
    $ nodeBB = (670,240)
    $ nodeCC = (400,460)
    $ nodeDD = (320,235)
    
    $ pathA = (nodeA, nodeB, nodeC, (0,0), (0,0), nodeBB, (0,0), nodeDD)
    $ pathB = (nodeA, nodeB, nodeC, (0,0), (0,0), nodeBB, (0,0), nodeDD)
    $ pathC = (nodeA, nodeB, nodeC, (0,0), (0,0), nodeBB, (0,0), nodeDD)
    $ pathD = ((0,0), nodeB, nodeC, (0,0), (0,0), (0,0), (0,0), nodeDD)
    
    $ pathAA = (nodeA, (0,0), (0,0), (0,0), nodeAA, (0,0), (0,0), (0,0))
    $ pathBB = (nodeA, nodeB, nodeC, (0,0), (0,0), nodeBB, (0,0), nodeDD)
    $ pathCC = ((0,0), (0,0), nodeC, (0,0), (0,0), (0,0), nodeCC, (0,0))
    $ pathDD = (nodeA, nodeB, nodeC, (0,0), (0,0), nodeBB, (0,0), nodeDD)


label loop_map6:

    # start "move through the map" loop
    call startpos from _call_startpos_55

    # do something at node?
    if exitpos == 1:       #if at node A
        $ startpos = 1     # stay in A
        
        jump mapdemos          # map loop to jump to
        
    if exitpos == 2:
        $ startpos = 2
        jump loop_map6
        
    if exitpos == 3: # switch board
        if startpos == 3:
            call shipchoice from _call_shipchoice
        $ startpos = 3
        
        if inventory_select == "cable":
            call use_cable_with_switchboard from _call_use_cable_with_switchboard

        jump loop_map6
        
    if exitpos == 4:
        $ startpos = 4
        jump loop_map6 
        

    #exits routing "got to map and set position for next map"
    if exitpos == 11:       #if going out at AA
        $ startpos = 33     #go to CC
        jump loop_map6          # map to jump to
        
    if exitpos == 22:
        $ startpos = 44
        $ liftpos = 3
        call sound_door from _call_sound_door_123
        jump lift1 # go to lift
        
    if exitpos == 33:
        $ startpos = 11
        jump map6
        
    if exitpos == 44:
        $ startpos = 44
        call sound_door from _call_sound_door_124
        call takeoff_anim from _call_takeoff_anim_7 # go to takeoff
        
        if landing == True:
            $ shippos = (400,0) # set position in surface engine
            jump surface1
        else:
            jump loop_map6



label shipchoice:
    
    #call hidepaths
    
    menu:
        
        "spaceship 1":
            $ spaceshiptype = "1"
            call sound_connected from _call_sound_connected_34
            return
        
        "spaceship 2":
            $ spaceshiptype = "2"
            call sound_connected from _call_sound_connected_35
            return
        
        "spaceship 3":
            $ spaceshiptype = "3"
            call sound_connected from _call_sound_connected_36
            return
            
        "terminal":
            call terminal from _call_terminal_10
            jump map6
        
        "exit":
            return

    
    

label use_cable_with_switchboard:
    
    if inventory_select == "cable":
        call sound_electroshock from _call_sound_electroshock_16
        with hpunch
        m "Wow, I made a short circuit! I hope everything is okay. !!!!! {w=4.0} {nw}"
            
    return
    
    
    
  
    
