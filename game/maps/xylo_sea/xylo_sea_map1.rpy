# MAPS

############################################

init:
    $ xylo_sea_bunker_info = False


label xylo_map1:
    
    stop music fadeout 1.0
    call atmo_ground from _call_atmo_ground
    
    image xylo_map1 = imagemapsdir + "xylo_sea_map1.png"
    
    scene bgcolor
    show screen notify("Sea Settlement")
    
    show xylo_map1

    show propeller:
        pos (663,86)
        linear 10 rotate 180.0
        rotate 0
        repeat
        
        
    
    if xylo_sea_bunker_info == 0:
        show buttonscreen:
            pos (400,130)
            
          
    show minicircle:
        pos (276, 409)
        zoom 0.6
    if renpy.showing("smoking1") != True:
        show smoking1:
            pos (277, 410)
    if renpy.showing("smoking2") != True:
        show smoking2:
            pos (277, 410)
    if renpy.showing("smoking3") != True:
        show smoking3:
            pos (277, 410)
            
            
    show minicircle as minicircle2:
        pos (481, 93)
        zoom 0.6

    
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
            if inventory_select == "":
                m "This is the sea settlement. {w=3} {nw}"
                m "This part really looks like... {w=3}a dirty industrial harbor. {w=3} {nw}"
                m "I can see a smoking chimney and a huge propeller... {w=4} {nw}"
                m "This is not so nice like they said in the advertisement! {w=4.5} {nw}"
            else:
                call dialog_nosense from _call_dialog_nosense_54
          
        $ startpos = 1   
        jump loop_xylo_map1        
        
    if exitpos == 2: # bunker info
        
        if startpos == 2:
            
            if inventory_select == "screwdriver":
                m "I could remove the screws...{w=2.5} {nw}"
                m "Remove the sign...{w=2} {nw}"
                m "And go through!{w=2} {nw}"
                
                call use_and_keep_item from _call_use_and_keep_item_6
                call sound_screw from _call_sound_screw_3
                
                $ xylo_sea_bunker_info = True
                
                $ pathB = (nodeA, nodeB, (0,0), (0,0), nodeAA, (0,0), nodeCC, (0,0))
            
            if xylo_sea_bunker_info == False:
                if inventory_select == "":
                    call xylo_sea_bunker_info from _call_xylo_sea_bunker_info
                    m "This sign is blocking the way to the north!{w=3.5} {nw}"
                    m "I need to find a way to remove it if I want to go there.{w=3.5} {nw}"
                else:
                    call dialog_nosense from _call_dialog_nosense_46
            
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


Private property.
You shall not pass.


    """
    
    call info_panel from _call_info_panel_2 # in animations

    return
