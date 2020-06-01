# MAPS

############################################


init:
    $ isc_containerpos4 = 2
    $ isc_containermoveto4 = 2


label isc_rail4b:
    
    call music_isc
    call atmo_spaceship_station
    
    
    scene bgcolor
    #show screen notify("B")
    
    call show_space
    
    show isc_rail4
    

    
    
    #show warningfloor:
    #    anchor (0.5,0.5)
    #    pos (570,240)
    #    rotate 90

    
    
    
    #show light:
    #    pos (115,30)
    #    
    #show light as light2:
    #    pos (115,240)
    #    
    #show light as light3:
    #    pos (115,430) 

    
    
    
    # set all variables for the map (nodes and path)
    $ nodeA = (537, 253)
    $ nodeB = (480, 134)
    $ nodeC = (495,42)
    $ nodeD = (480, 408)

    $ nodeAA = (760, 252)
    $ nodeBB = (544, 460)
    $ nodeCC = (385, 216)
    $ nodeDD = (385, 325)

    $ pathA = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, (0, 0), (0, 0))
    $ pathB = (nodeA, nodeB, nodeC, nodeD, (0, 0), nodeBB, (0, 0), (0, 0))
    $ pathC = (nodeA, nodeB, nodeC, nodeD, (0, 0), nodeBB, (0, 0), (0, 0))
    $ pathD = (nodeA, nodeB, nodeC, nodeD, (0, 0), nodeBB, (0, 0), (0, 0))
     
    $ pathAA = (nodeA, (0, 0), (0, 0), (0, 0), nodeAA, (0, 0), (0, 0), (0, 0))
    $ pathBB = (nodeA, nodeB, nodeC, nodeD, (0, 0), nodeBB, (0, 0), (0, 0))
    $ pathCC = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)
    $ pathDD = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)
    
    
    if playertype == "minidroid":
        show playercross:
            pos (255, 42)
    
    
    # container position
    if isc_containerpos4 == 1:
        show isc_moving_room:
            pos (376,138)
        #$ pathC = (nodeA, nodeB, nodeC, nodeD, (0, 0), (0, 0), nodeCC, (0, 0))
    
    if isc_containerpos4 == 2:
        show isc_moving_room:
            pos (376,408)
        #$ pathC = (nodeA, nodeB, nodeC, nodeD, (0, 0), (0, 0), (0, 0), (0, 0))
        
        

    # shadow
    #if shadow_enable == 1:
    #    show shadow zorder 800:
    #        pos nodeA
            
            
            


label loop_isc_rail4b:
    
    while True:

        # start "move through the map" loop
        call startpos

        # do something at node?
        if exitpos == 1:
            $ startpos = 1

        
            
        if exitpos == 2:
            if startpos == 2 and isc_containerpos4 == 2:
                call dialog_closed
                
            if playertype == "minidroid":
                call dialog_ndd
                $ startpos = 2
                jump loop_isc_rail4b
                
            
            if isc_containerpos4 == 1:
                call sound_door
                show player:
                    pos (373,136)
                pause 0.7
                call sound_door
                $ startpos = 2
                jump isc_rail4a
            $ startpos = 2
            

            
        if exitpos == 3:
            if startpos == 3 and playertype == "minidroid": 
                hide player
                show minidroid:
                    pos nodeC
                    linear 2 pos (255, 42)
                pause 2
                $ startpos = 3
                $ playertype = "player"
                hide minidroid
                hide playercross

                #"next scene!"
                jump isc_rail4a
            
            if startpos == 3 and playertype == "player": 
                call dialog_nosense
            
            $ startpos = 3
                
                
                
            
            
        if exitpos == 4:
            if startpos == 4 and isc_containerpos4 == 1:
                
                if playertype == "minidroid":
                    call sound_door_locked
                    md "It is locked!{w=1.5} {nw}"
                else:
                    call dialog_closed
                
                
            
            if isc_containerpos4 == 2:
                call sound_door
                show player:
                    pos (376,408)
                pause 0.7
                call sound_door
                $ startpos = 4
                jump isc_rail4a
            
            $ startpos = 4

            

        #exits routing "got to map and set position for next map"
        if exitpos == 11:
            if playertype == "minidroid":
                call dialog_ndd
            else:
                call sound_door
                $ startpos = 1
                jump isc_city_center
            $ startpos = 11

            
        if exitpos == 22:
            $ startpos = 11
            jump isc_rail5

            
        if exitpos == 33:
            $ startpos = 33

            
        if exitpos == 44:
            m "I can see on the other side....  but...{w=2} {nw}"
            call dialog_nothing
            $ startpos = 44
            #jump isc_rail3

            


                



