# MAPS

############################################



# spaceport GEM
label isc_gateway_crane_to_spacenet:
    
    call atmo_spaceship_station 
    
    scene bgcolor
    
    call show_space
    
    
    show crane as crane2:
        anchor (0.5, 0.5)
        pos (700, 240)
        rotate 90
        
    show crane as crane3:
        anchor (0.5, 0.5)
        pos (600, 240)
        
    show crane as crane3:
        anchor (0.5, 0.5)
        pos (370, 240)
    
    show crossroomsmall:
        anchor (0.5, 0.5)
        pos (400, 200)
    
    
    show crossroomsmall as crossroomsmall2:
        anchor (0.5, 0.5)
        pos (535, 240)
    
    show crane:
        anchor (0.5, 0.5)
        pos (100, 240)
        rotate 90
        
    show doorv:
        pos (422, 240)
        


    
    # set all variables for the map (nodes and path)
    $ nodeA = (50,240) #(467,47)
    $ nodeB = (400,240)
    $ nodeC = (330,130) #(470,420)
    $ nodeD = (249,240)
    
    $ nodeAA = (400,25)
    $ nodeBB = (605,240)
    $ nodeCC = (400,460)
    $ nodeDD = (320,240)
    
    
    $ pathA = (nodeA, nodeB, (0,0), (0,0), (0,0), (0,0), (0,0), (0,0))
    $ pathB = (nodeA, nodeB, nodeC, (0,0), (0,0), (0,0), (0,0), (0,0))
    $ pathC = ((0,0), nodeB, nodeC, (0,0), (0,0), (0,0), (0,0), (0,0))
    $ pathD = ((0,0), (0,0), nodeC, (0,0), (0,0), (0,0), (0,0), nodeDD)
    
    $ pathAA = (nodeA, (0,0), (0,0), (0,0), nodeAA, (0,0), (0,0), (0,0))
    $ pathBB = (nodeA, (0,0), (0,0), (0,0), (0,0), nodeBB, (0,0), nodeDD)
    $ pathCC = ((0,0), (0,0), nodeC, (0,0), (0,0), (0,0), nodeCC, (0,0))
    $ pathDD = ((0,0), (0,0), (0,0), (0,0), (0,0), nodeBB, (0,0), nodeDD)
    


label loop_isc_gateway_crane_to_spacenet:
    
    while True:

        # start "move through the map" loop
        call startpos

        # do something at node?
        if exitpos == 1:       #if at node A
            $ inventory_select = "hook"
            call use_and_keep_item
            m "Let's go! {w=2} {nw}"
            
            $ startpos = 4
            jump isc_city_gateway_crane

            
        if exitpos == 2:
            if startpos == 2:
                $ startpos = 1
                call sound_door
                jump isc_city_spacenet
            $ startpos = 2

            
        if exitpos == 3:
            if startpos == 3:
                if isc_gateway_spacenet_cash > 0:
                    m "There are some coins! {w=1.5} {nw}"
                    call io_cash(isc_gateway_spacenet_cash)
                    $ isc_gateway_spacenet_cash = 0
                else:
                    call dialog_nothing
                
            $ startpos = 3

            
        if exitpos == 4:
            $ startpos = 4

            

        #exits routing "got to map and set position for next map"
        if exitpos == 11:       #if going out at AA
            $ startpos = 11    #go to CC

            
        if exitpos == 22:
            $ startpos = 22
            

            
        if exitpos == 33:
            $ startpos = 33

            
        if exitpos == 44:
            $ startpos = 44

                

