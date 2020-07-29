# MAPS

############################################
label xylo_map6spaceport:
    
    stop music fadeout 1.0
    call atmo_ground from _call_atmo_ground_2
    
    image xylo_map6spaceport = imagemapsdir + "spaceportlift.png"
    
    scene bgcolor
    show screen notify("xylo sea colony spaceport")
    
    show xylo_map6spaceport
    
    #show buttonscreen:
    #    pos (468, 444) 

    show terminalmap:
        anchor (0.5, 0.5)
        pos (468, 425) 
    

    
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
    call landing_anim from _call_landing_anim_3
    
    
    # set all variables for the map (nodes and path)
    $ nodeA = (-100,-100) #(467,47)
    $ nodeB = (470,240)
    $ nodeC = (468,386)
    $ nodeD = (250,240)
    
    $ nodeAA = (400,25)
    $ nodeBB = (685,240)
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


label loop_xylo_map6spaceport:
    
    while True:

        # start "move through the map" loop
        call startpos from _call_startpos_43

        # do something at node?
        if exitpos == 1:       #if at node A
            $ startpos = 1     # stay in A
            jump mapdemos          # map loop to jump to
            
        
        if exitpos == 2:
            if startpos == 2:
                m "This spaceport is on the top of the building. {w=3.5} {nw}"
            $ startpos = 2

            
        if exitpos == 3: # switch board
            if startpos == 3:
                
                if inventory_select == "cable":
                    call xylo_use_cable_with_switchboard from _call_xylo_use_cable_with_switchboard
                
                if superdev == True:
                    call xylo_shipchoice from _call_xylo_shipchoice
                if superdev == False:
                    call terminal from _call_terminal_7
            
            $ startpos = 3
            

            
        if exitpos == 4:
            $ startpos = 4

            

        #exits routing "got to map and set position for next map"
        if exitpos == 11:       #if going out at AA
            $ startpos = 33     #go to CC

            
        if exitpos == 22:
            $ startpos = 44
            $ liftpos = 3
            call sound_door from _call_sound_door_103
            jump xylo_lift1 # go to lift
            
        if exitpos == 33:
            $ startpos = 11

            
        if exitpos == 44:
            $ startpos = 44
            call sound_door from _call_sound_door_104
            call takeoff_anim("withmenu") from _call_takeoff_anim_4 # go to takeoff
            
            
            # straight to space
            if takeoftospace == True:
                $ takeoftospace = False
                $ space_anim = True
                jump space
            
            # to surface
            if landing == True:
                $ shippos = (1200,1400) # set position in surface engine
                jump surface_xylo




label xylo_shipchoice:
    
    #call hidepaths
    
    menu:
        
        "spaceship 1":
            $ spaceshiptype = "1"
            call sound_connected from _call_sound_connected_30
            return
        
        "spaceship 2":
            $ spaceshiptype = "2"
            call sound_connected from _call_sound_connected_31
            return
        
        "spaceship 3":
            $ spaceshiptype = "3"
            call sound_connected from _call_sound_connected_32
            return
            
        "terminal":
            call terminal from _call_terminal_8
            jump loop_xylo_map6spaceport
        
        "exit":
            return

    
    

label xylo_use_cable_with_switchboard:
    
    if inventory_select == "cable":
        call sound_electroshock from _call_sound_electroshock_15
        with hpunch
        m "Wow, I made a short circuit! I hope everything is okay! {w=4.0} {nw}"
            
    return
    
    
    
  
    
