# MAPS

############################################



label xylo_mountain1:
    
    stop music fadeout 1.0
    call atmo_wind from _call_atmo_wind_1
    
    
    image xylo_mountain1 = imagemapsdir + "xylo_mountain1.png"
    
    scene bgcolor
    show screen notify("top of the mountain")
    
 
    show xylo_mountain1
    
    show buttonscreen:
        pos (630, 375)
        
        

    # check if spaceship is landing on this map or not
    # $ landing = False
    # $ landing = True
    call landing_anim from _call_landing_anim_6
    
    
    # set all variables for the map (nodes and path)
    $ nodeA = (670,30) #(467,47)
    $ nodeB = (470,240)
    $ nodeC = (-100,-100) #(470,420)
    $ nodeD = (250,240)
    
    $ nodeAA = (400,25)
    $ nodeBB = (630,350)
    $ nodeCC = (400,460)
    $ nodeDD = (320,235)
    
    $ pathA = (nodeA, nodeB, nodeC, (0,0), (0,0), nodeBB, (0,0), (0,0))
    $ pathB = (nodeA, nodeB, nodeC, (0,0), (0,0), nodeBB, (0,0), nodeDD)
    $ pathC = (nodeA, nodeB, nodeC, (0,0), (0,0), nodeBB, (0,0), nodeDD)
    $ pathD = ((0,0), nodeB, nodeC, (0,0), (0,0), (0,0), (0,0), nodeDD)
    
    $ pathAA = (nodeA, (0,0), (0,0), (0,0), nodeAA, (0,0), (0,0), (0,0))
    $ pathBB = (nodeA, nodeB, nodeC, (0,0), (0,0), nodeBB, (0,0), nodeDD)
    $ pathCC = ((0,0), (0,0), nodeC, (0,0), (0,0), (0,0), nodeCC, (0,0))
    $ pathDD = ((0,0), nodeB, (0,0), (0,0), (0,0), nodeBB, (0,0), nodeDD)


label loop_xylo_mountain1:

    # start "move through the map" loop
    call startpos from _call_startpos_56

    # do something at node?
    if exitpos == 1:       #if at node A
        $ startpos = 1     # stay in A
        
        jump xylo_mountain2
        
        
    if exitpos == 2:
        if startpos == 2:
            m "I'm on the top of the mountain. {w=2.5} {nw}"
            m "The view here is amazing! {w=2.5} {nw}"
        $ startpos = 2
        jump loop_xylo_mountain1
        
    if exitpos == 3: # switch board
        $ startpos = 3

        jump loop_xylo_mountain1
        
    if exitpos == 4:
        $ startpos = 4
        jump loop_xylo_mountain1 
        

    #exits routing "got to map and set position for next map"
    if exitpos == 11:       #if going out at AA
        $ startpos = 11    #go to CC
        jump loop_xylo_mountain1          # map to jump to
        
    if exitpos == 22:
        if startpos == 22:
            #if inventory_select == "":
            #    m "There is an information table at the tree. {w=2.5} {nw}"
            call xylo_mountain1_info from _call_xylo_mountain1_info

        
        $ startpos = 22
        jump loop_xylo_mountain1 # go to lift
        
    if exitpos == 33:
        $ startpos = 33
        jump loop_xylo_mountain1
        
    if exitpos == 44:
        $ startpos = 44
        call sound_door from _call_sound_door_125
        call takeoff_anim("withmenu") from _call_takeoff_anim_8 # go to takeoff
        
        
        # straight to space
        if takeoftospace == True:
            $ takeoftospace = False
            $ space_anim = True
            jump space
        
        # to surface
        if landing == True:
            $ shippos = (200,1200) # set position in surface engine
            jump surface_xylo
        
        jump loop_xylo_mountain1




label xylo_mountain1_info:

    $ info_panel_symbol = ""
    $ showtext = """
- Montain view -


This is a ancient sacred place.
This tree was planted to remember this place.

At night, it is possible to see the two moons of xylo 
at the same time, in a sky full of stars.


    """

    call info_panel from _call_info_panel_10

    return

