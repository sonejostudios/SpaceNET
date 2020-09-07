
##############################################
label map5:
    
    image map5 = imagemapsdir + "xylo_sea_phouse.png"
    
    scene map5
    show screen notify("house")
    
    # set all variables for the map (nodes and path)
    $ nodeA = (465,365)
    $ nodeB = (540,240)
    $ nodeC = (670,250)
    $ nodeD = (540,360)
    
    $ nodeAA = (473,125)
    $ nodeBB = (740,240)
    $ nodeCC = (400,460)
    $ nodeDD = (310,270)
    
    $ pathA = ((0,0), nodeB, nodeC, (0,0), nodeAA, (0,0), (0,0), nodeDD)
    $ pathB = ((0,0), nodeB, (0,0), (0,0), nodeAA, nodeBB, (0,0), (0,0))
    $ pathC = ((0,0), nodeB, (0,0), nodeD, (0,0),(0,0),(0,0), (0,0))
    $ pathD = ((0,0), nodeB, nodeC, (0,0), (0,0), (0,0), (0,0), nodeDD)
    
    $ pathAA = ((0,0), nodeB, (0,0), (0,0), nodeAA, nodeBB, (0,0), (0,0))
    $ pathBB = ((0,0), nodeB, (0,0), (0,0), nodeAA, nodeBB, (0,0), (0,0))
    $ pathCC = ((0,0), (0,0), nodeC, (0,0), (0,0), (0,0), (0,0), (0,0))
    $ pathDD = ((0,0), (0,0), (0,0), nodeD, (0,0), (0,0), (0,0), (0,0))

label loop_map5:

    # start "move through the map" loop
    call startpos from _call_startpos_35
    
    # do something at node?
    if exitpos == 1:       #if at node A
        $ startpos = 1     # stay in A
        jump loop_map5          # map to jump to
        
    if exitpos == 2:
        $ startpos = 2
        
        
        call map5_bulb from _call_map5_bulb
        
        jump loop_map5
        
    if exitpos == 3:
        $ startpos = 3
        jump loop_map5
        
    if exitpos == 4:
        $ startpos = 4
        jump loop_map5 
    
    #exits routing "got to map"
    if exitpos == 11:       #if going out at AA
        #$ exitpos = 44       
        $ startpos = 11     #go to CC
        
        call map5_talk1 from _call_map5_talk1  #go to map5_talk1
        
        jump map5           # map to jump to
        
    if exitpos == 22:
        $ startpos = 44
        call sound_door from _call_sound_door_90
        jump map4
        
    if exitpos == 33:
        $ startpos = 11
        jump map2
        
        
    if exitpos == 44:
        $ startpos = 22
        jump map2

    else :
        pause 3
        jump map5



label map5_talk1:
    
    if m_step_eileen1 == 2:
        sam "Thank you for your help, I'm happy now.{w=3.0} {nw}"
    
    if inventory_select == "bulb":
        call use_item from _call_use_item_4
        sam "Thank you for the light bulb!!{w=3.0} {nw}"
        $ m_step_eileen1 = 2
    
    if m_step_eileen1 == 1:
        sam "Have you found a light bulb? I'm still waiting!{w=3.0} {nw}"
    
    if m_step_eileen1 == 0:
        #call new_mission from _call_new_mission
        sam "I'm looking for a light bulb, do you have one?{w=3.0} {nw}"
        $ m_step_eileen1 = 1
    

    return
    
    

label map5_bulb:
    if "bulb" not in inventory:
        
        #call hidepaths
        
        m "There is a light bulb!{w=2.0} {nw}"
        
        call take_item("bulb") from _call_take_item_13

    return
    
