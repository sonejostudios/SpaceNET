# MAPS

############################################

init:
    $ xylo_mine_minitrain_room_pick = False
    
    $ xylo_mine_minitrain_room_earthquake_dialog = False
    
    
    
screen xylo_mine_minitrain_room_earthquake():
    
    if moving == False:
        timer 5 repeat True action Jump("xylo_mine_minitrain_room_earthquake")




label xylo_mine_minitrain_room:
    
    stop music
    call atmo_cave from _call_atmo_cave_3
    
    image xylo_mine_minitrain_room = imagemapsdir + "xylo_mine_minitrain_room.png"
    image xylo_mine_minitrain_room2 = imagemapsdir + "xylo_mine_minitrain_room2.png"
    
    scene bgcolor
    show screen notify("abandonned mine")
    
    show xylo_mine_minitrain_room
    
    
    show screen xylo_mine_minitrain_room_earthquake
    

    # check if spaceship is landing on this map or not
    #$ landing = False
    # $ landing = True
    #call landing_anim
    
    
    # set all variables for the map (nodes and path)
    $ nodeA = (50, 236)
    $ nodeB = (238, 220)
    $ nodeC = (288, 73)
    $ nodeD = (212, 401)

    $ nodeAA = (490, 210)
    $ nodeBB = (729, 73)
    $ nodeCC = (676, 414)
    $ nodeDD = (728, 225)

    $ pathA = (nodeA, nodeB, (0, 0), (0, 0), nodeAA, (0, 0), (0, 0), (0, 0))
    $ pathB = (nodeA, nodeB, nodeC, nodeD, nodeAA, (0, 0), (0, 0), (0, 0))
    $ pathC = ((0, 0), nodeB, nodeC, nodeD, (0, 0), (0, 0), (0, 0), (0, 0))
    $ pathD = ((0, 0), nodeB, nodeC, nodeD, (0, 0), (0, 0), (0, 0), (0, 0))
     
    $ pathAA = (nodeA, nodeB, (0, 0), (0, 0), nodeAA, (0, 0), nodeCC, (0, 0))
    $ pathBB = ((0, 0), (0, 0), (0, 0), (0, 0), nodeAA, nodeBB, (0, 0), (0, 0))
    $ pathCC = ((0, 0), (0, 0), (0, 0), (0, 0), nodeAA, (0, 0), nodeCC, (0, 0))
    $ pathDD = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)
    
    

label loop_xylo_mine_minitrain_room:


    if xylo_mine_minitrain_room_pick == True:
        $ pathAA = (nodeA, nodeB, (0, 0), (0, 0), nodeAA, nodeBB, nodeCC, (0, 0))
        show xylo_mine_minitrain_room2:
            align (1.0,0.0)
        
    
    while True:

        # start "move through the map" loop
        call startpos from _call_startpos_54

        # do something at node?
        if exitpos == 1:
            $ startpos = 1
            call sound_door from _call_sound_door_120
            hide screen xylo_mine_minitrain_room_earthquake
            jump xylo_minitrain2


        if exitpos == 2:
            if startpos == 2:
                m "I'm at level -2 of the mine. {w=2} {nw}"
            $ startpos = 2
            

        if exitpos == 3:
            if startpos == 3:
                call xylo_mine_level1_info from _call_xylo_mine_level1_info_2
            $ startpos = 3

        if exitpos == 4:
            if startpos == 4:
                call dialog_nothing from _call_dialog_nothing_34
            $ startpos = 4

        #exits
        if exitpos == 11: 
            if startpos == 11:
                if inventory_select == "pick" and xylo_mine_minitrain_room_pick == False:
                    hide screen xylo_mine_minitrain_room_earthquake
                    
                    m "Let's dig and free the way!{w=2} {nw}"
                    call use_and_keep_item from _call_use_and_keep_item_23
                    call sound_dig from _call_sound_dig_1
                    
                    pause 1
                    call sound_collect from _call_sound_collect_8
                    with flash
                    $ xylo_mine_minitrain_room_pick = True
                    show screen xylo_mine_minitrain_room_earthquake
                    jump xylo_mine_minitrain_room
                
                if xylo_mine_minitrain_room_pick == False:
                    m "There are a lot of stones there.{w=2} {nw}"
                    m "These stones looks not stable...{w=2} {nw}"
                    m "Tey looks like they just have fallen down from the ceiling.{w=3} {nw}"
                    m "Maybe there is a way behind?{w=2} {nw}"
                #call dialog_nothing 
            $ startpos = 11
            
             

        if exitpos == 22:
            if startpos == 22:
                hide screen xylo_mine_minitrain_room_earthquake
                m "There is some old dynamite... {w=2} {nw}"
                if "dynamite" not in inventory:
                    call take_item ("dynamite") from _call_take_item_15
                else:
                    m "I have already one, this is enough for now. {w=2} {nw}"
                show screen xylo_mine_minitrain_room_earthquake
                
            $ startpos = 22


        if exitpos == 33:
            if startpos == 33:
                m "Stones, stones, stones... {w=2} {nw}"
            $ startpos = 33

            
        if exitpos == 44:
            $ startpos = 44





label xylo_mine_minitrain_room_earthquake:
    
            
    call sound_earthquake from _call_sound_earthquake_1
    with hpunch
    
    if xylo_mine_minitrain_room_earthquake_dialog == False:
        $ xylo_mine_minitrain_room_earthquake_dialog = True
        m "Wow! This feels like seismic actvity! {w=2} {nw}"
        m "I think it would be better not to stay longer! {w=3} {nw}"
        
    
    
    if showtext != "":
        call xylo_mine_level1_info from _call_xylo_mine_level1_info_3

    jump loop_xylo_mine_minitrain_room


