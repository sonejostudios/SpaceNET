# MAPS

############################################

init:
    $ xylo_sea_bunker_info = False


label xylo_map1:
    
    stop music fadeout 1.0
    call atmo_ground from _call_atmo_ground
    
    image xylo_map1 = imagemapsdir + "xylo_sea_map1.png"
    
    scene bgcolor
    show screen notify("Xylo sea colony")
    
    show xylo_map1

    show propeller:
        pos (663,86)
        linear 10 rotate 180.0
        rotate 0
        repeat
        
    
    if xylo_sea_bunker_info == 0:
        show buttonscreen:
            pos (400,130)

    
    # set all variables for the map (nodes and path)
    $ nodeA = (400,240)
    $ nodeB = (400,155)
    $ nodeC = (400,350)
    $ nodeD = (250,240)
    
    $ nodeAA = (400,25)
    $ nodeBB = (780,240)
    $ nodeCC = (400,455)
    $ nodeDD = (95,235)
    
    $ pathA = (nodeA, nodeB, (0,0), (0,0), (0,0), nodeBB, nodeCC, nodeDD)
    $ pathB = (nodeA, nodeB, (0,0), (0,0), (0,0), (0,0), nodeCC, (0,0))
    $ pathC = (nodeA, nodeB, nodeC, nodeD, nodeAA, (0,0), nodeCC, (0,0))
    $ pathD = (nodeA, nodeB, nodeC, nodeD, (0,0), nodeBB, (0,0), nodeDD)
    
    $ pathAA = (nodeA, (0,0), (0,0), (0,0), nodeAA, (0,0), nodeCC, (0,0))
    $ pathBB = (nodeA, (0,0), (0,0), (0,0), (0,0), nodeBB, (0,0), nodeDD)
    $ pathCC = (nodeA, nodeB, (0,0), (0,0), (0,0), (0,0), nodeCC, (0,0))
    $ pathDD = (nodeA, (0,0), (0,0), (0,0), (0,0), nodeBB, (0,0), nodeDD)
    
    
    if xylo_sea_bunker_info == True:
        $ pathA = (nodeA, (0,0), (0,0), (0,0), nodeAA, nodeBB, nodeCC, nodeDD)
        $ pathB = (nodeA, (0,0), (0,0), (0,0), nodeAA, (0,0), nodeCC, (0,0))
        $ pathAA = (nodeA, (0,0), (0,0), (0,0), nodeAA, (0,0), nodeCC, (0,0))
        $ pathCC = (nodeA, (0,0), (0,0), (0,0), nodeAA, (0,0), nodeCC, (0,0))


label loop_xylo_map1:

    # start "move through the map" loop
    call startpos from _call_startpos_17

    # do something at node?
    if exitpos == 1:   
        if startpos == 1:
            m "This is the xylo sea colony. {w=2} {nw}"
            m "It looks like an industrial harbour. {w=2} {nw}"
          
        $ startpos = 1   
        jump loop_xylo_map1        
        
    if exitpos == 2: # bunker info
        
        if startpos == 2:
            
            if inventory_select == "screwdriver":
                m "I could remove the screws...{w=2} {nw}"
                m "Remove the board...{w=1.5} {nw}"
                m "And go through!{w=1.5} {nw}"
                
                call use_and_keep_item from _call_use_and_keep_item_6
                call sound_screw from _call_sound_screw_3
                
                $ xylo_sea_bunker_info = True
                
                $ pathB = (nodeA, nodeB, (0,0), (0,0), nodeAA, (0,0), nodeCC, nodeDD)
            
            if xylo_sea_bunker_info == False:
                call xylo_sea_bunker_info from _call_xylo_sea_bunker_info
            
            else:
                hide buttonscreen
                
                
            
        
            
        
        $ startpos = 2
        jump loop_xylo_map1
        
    if exitpos == 3:
        $ startpos = 3
        jump loop_xylo_map1
        
    if exitpos == 4:
        $ startpos = 4
        jump loop_xylo_map1 
        

    #exits routing "got to map and set position for next map"
    if exitpos == 11:       #if going out at AA
        $ startpos = 33     #go to CC
        jump xylo_map7         # map to jump to
        
    if exitpos == 22:
        $ startpos = 44
        jump xylo_map2
        
    if exitpos == 33:
        $ startpos = 11
        jump xylo_map4
        
    if exitpos == 44:
        #$ startpos = 22
        $ liftpos = 0
        call sound_door from _call_sound_door_37
        jump xylo_lift1



label xylo_sea_bunker_info:
    
    $ info_panel_symbol = "biohazard"
    $ showtext = """
    
    
    
- A.R.K. Corporation -


Private property
You shall not pass


    """
    
    call info_panel from _call_info_panel_2 # in animations

    return
