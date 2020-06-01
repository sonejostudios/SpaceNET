# MAPS

############################################

# go level -2, get key
# go level -1, use key with lift control
# send lift to -2
# go to lift, lift cabin is not there
# use rope and come to next secret room
# in this room find button "unlock secret level -3"
# go bak to room -2
# call lift
# go to level -3


init:
    $ xylo_sea_bunker_rope = False



# bunker map

label xylo_sea_bunker_liftmap:
    
    call music_cargo
    

    scene bgcolor
    
    show lift:
        anchor (0.5,0.5)
        pos (0.5,0.5)
        zoom 1
    
    
    #if xylo_sea_bunker_rope == False:
    #    show screen notify("lift shaft")
    
    
    # set all variables for the map (nodes and path)
    $ nodeA = (30, 30)
    $ nodeB = (40, 40)
    $ nodeC = (50, 50)
    $ nodeD = (60, 60)
    

    $ nodeAA = (70, 70)
    $ nodeBB = (80, 80)
    $ nodeCC = (345, 200)
    $ nodeDD = (455, 200)

    $ pathA = (nodeA, nodeB, (0, 0), nodeD, nodeAA, (0, 0), (0, 0), (0, 0))
    $ pathB = ((0, 0), nodeB, (0, 0), nodeD, (0, 0), (0, 0), (0, 0), (0, 0))
    $ pathC = (nodeA, nodeB, (0, 0), nodeD, nodeAA, (0, 0), (0, 0), (0, 0))
    $ pathD = ((0, 0), nodeB, (0, 0), nodeD, (0, 0), (0, 0), (0, 0), (0, 0))
     
    $ pathAA = (nodeA, nodeB, (0, 0), nodeD, nodeAA, (0, 0), nodeCC, nodeDD)
    $ pathBB = (nodeA, nodeB, (0, 0), nodeD, nodeAA, nodeBB, nodeCC, nodeDD)
    
    $ pathCC = ((0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), nodeCC, nodeDD)
    $ pathDD = ((0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), nodeCC, nodeDD)
    

    show player:
        pos nodeDD
        
    if pnc_mode == False:
        show nodeanime as pathnodeDD:
            pos nodeDD
        
    
    image side_door = "images/side_door.png"
    
    show side_door behind player, pathnodeDD:
            anchor (0.0,0.5)
            pos (448, 190)
    
    
    if liftpos == 1: #-02
        $ pathDD = ((0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), nodeDD)
        
        m "Wow! {w=1} {nw}"
        m "This is very high! {w=2} {nw}"
        m "But... {w=1} {nw}"
        
        if "cable" not in inventory:
            m "There is a cable... {w=2} {nw}"
            call take_item("cable")
        
        else:
            call dialog_nothing
        
        
    if liftpos == 2: #-01
        show side_door as sidedoor2 behind player, pathnodeDD:
            anchor (0.1,0.5)
            rotate 180
            pos (306, 190)
            
            
        if xylo_sea_bunker_rope == False:
            $ pathDD = ((0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), nodeDD)
            m "Wow! {w=1} {nw}"
            m "This is very high! {w=2} {nw}"
            m "Interesting... There is a door on the other side. {w=3.5} {nw}"
            
        if xylo_sea_bunker_rope == True:
            $ pathDD = ((0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), nodeCC, nodeDD)
            image xylo_sea_bunker_rope = "images/xylo_sea_bunker_rope.png"
            show xylo_sea_bunker_rope:
                anchor (0.5,0.5)
                pos (400,175)
            

       
       
       
        

label loop_xylo_sea_bunker_liftmap:
    
    
    while True:

        
        call startpos

        #m " I can't go there, it is to dangerous! {w=3} {nw}"
        

        # do something at node?
        if exitpos == 1:
            $ startpos = 1

        if exitpos == 2:

            $ startpos = 2

            
        if exitpos == 3:
            $ startpos = 3

            
        if exitpos == 4:
            $ startpos = 4


        #exits routing "got to map and set position for next map"
        if exitpos == 11:   
            $ startpos = 11     
 
            
        if exitpos == 22:
            $ startpos = 22

            
        if exitpos == 33:
            $ startpos = 2
            call sound_door
            jump xylo_sea_bunker_liftroom

            
        if exitpos == 44:
            if startpos == 44:
                if inventory_select == "rope":
                    m "It is quite dangerous, but why not? {w=2} {nw}"
                    $ xylo_sea_bunker_rope = True
                    call sound_electroshock
                    with flash
                    
                    call use_item
                    
                    jump xylo_sea_bunker_liftmap
            

            $ startpos = 1
            call sound_door
            jump xylo_sea_bunker
            




