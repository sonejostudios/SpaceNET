init:
    $ xylo_sea_cabin_door_open = False


###########################################
label xylo_sea_island2:
    
    call atmo_sea from _call_atmo_sea_2
    call atmo_nature from _call_atmo_nature
    
    
    image xylo_sea_island2 = imagemapsdir + "xylo_sea_island2.png"
    
    scene bgcolor
    #show screen notify("Unknown Island")
    
    show xylo_sea_island2
    show waves behind xylo_sea_island2
    
    $ inventory_button = True
    
    
    if xylo_lighthouse_inverted == False:
        show lighthouse:
            pos (675, 229)
            #pos (164, 345)
            rotate 0
            transform_anchor True
            linear 10 rotate 360
            repeat
    else:
        show lighthouse:
            pos (675, 229)
            #pos (164, 345)
            rotate 0
            transform_anchor True
            linear 10 rotate -360
            repeat
        
    show minicircle:
        pos (675, 229)
        #pos (164, 345)
        zoom 0.6

    
    
    # set all variables for the map (nodes and path)
    $ nodeA = (269, 157)
    $ nodeB = (645, 261)
    $ nodeC = (310, 376)
    $ nodeD = (41, 53)
    
    $ nodeAA = (423, 110)
    $ nodeBB = (154, 284)
    $ nodeCC = (400,460)
    $ nodeDD = (40,350)
    
    $ pathA = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, (0,0), (0,0))
    $ pathB = (nodeA, nodeB, (0,0), nodeD, nodeAA, (0,0), (0,0), (0,0))
    $ pathC = (nodeA, (0,0), nodeC, (0,0), nodeAA, nodeBB, (0,0), (0,0))
    $ pathD = (nodeA, nodeB, (0,0), nodeD, nodeAA, (0,0), (0,0), (0,0))
    
    $ pathAA = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, (0,0), (0,0))
    $ pathBB = (nodeA, (0,0), nodeC, (0,0), nodeAA, nodeBB, (0,0), (0,0))
    $ pathCC = ((0,0), (0,0), nodeC, (0,0), (0,0), (0,0), (0,0), (0,0))
    $ pathDD = ((0,0), (0,0), (0,0), nodeD, (0,0), (0,0), (0,0), nodeDD)
    
    
    

label loop_xylo_sea_island2:
    
    while True:

        # start "move through the map" loop
        call startpos from _call_startpos_92
        
        # do something at node?
        if exitpos == 1:
            if startpos == 1:
                if inventory_select == "wood":
                    call dialog_nobonfire from _call_dialog_nobonfire
                else:
                    m "This island is beautiful. {w=3.5} {nw}"   
            
            $ startpos = 1
            
            
            
            
        if exitpos == 2: # lighthouse
            if startpos == 2:
                if inventory_select == "":
                    if "lighter" not in inventory:
                        m "This is a tiny lighthouse. {w=3} {nw}"
                        m "Sweet! {w=1.5} {nw}"
                        m "Wait... {w=1.5} {nw}"
                        m "There is an old lighter on the ground. {w=4} {nw}"
                        call take_item("lighter") from _call_take_item_26
                        
                    else:
                        m "There are some crazy looking cables coming out the lighthouse... {w=5} {nw}"
                        menu:
                            "Look at the crazy looking cables" if xylo_lighthouse_inverted == False:
                                m "They look dangerous.{w=2}{nw}"
                                m "I rather be careful. {w=2}{nw}"
                                
                            "Touch the crazy looking cables":
                                call sound_electroshock from _call_sound_electroshock_31
                                with hpunch
                                m "Wow!{w=1.5}{nw}"
                                m "I should'nt play around with electricity. {w=2}{nw}"
                            
                            "Connect the crazy looking cables" if xylo_lighthouse_inverted == False:
                                call sound_electroshock from _call_sound_electroshock_32
                                with hpunch
                                call sound_explosion from _call_sound_explosion_6
                                with flash
                                m "Boom!{w=1.5}{nw}"
                                m "This was not a good idea. {w=2.5}{nw}"
                                m "I hope I didn't break anything. {w=2.5}{nw}"
                                
                            "Lick the crazy looking cables" if xylo_lighthouse_inverted == True:
                                m "Are you kidding?{w=2}{nw}"
                                m "No way! {w=1.5}{nw}"
                                m "Well... {w=1.5}{nw}"
                                m "It is really a stupid idea! {w=3}{nw}"
                                m "But I heard, one can not die in some adventure games. {w=3.5}{nw}"
                                m "So... {w=1.5}{nw}"
                                m "Let's try it. {w=2}{nw}"
                                call sound_explosion from _call_sound_explosion_7
                                with flash
                                $ drunktime = 30 #=15sec
                                with Dissolve(2)
                                m "Oh.. I'm feeling dizzy...{w=2.5}{nw}"

                                
                            "Do nothing":
                                m "This is boring! {w=2} {nw}"
                
                
                elif inventory_select == "wood":
                    call dialog_nobonfire from _call_dialog_nobonfire_1
                    
                elif inventory_select == "screwdriver":
                    call sound_electroshock from _call_sound_electroshock_33
                    call use_and_keep_item from _call_use_and_keep_item_47
                    with hpunch
                    m "Ouch! {w=2} {nw}"
                    
                elif inventory_select == "cable":
                    call sound_electroshock from _call_sound_electroshock_34
                    call use_and_keep_item from _call_use_and_keep_item_48
                    with hpunch
                    call sound_explosion from _call_sound_explosion_8
                    with flash
                    m "Boom!{w=1.5}{nw}"
                    m "That was loud. {w=2.5}{nw}"
                
                elif inventory_select == "batterywet":
                    call use_and_keep_item from _call_use_and_keep_item_45
                    call sound_electroshock from _call_sound_electroshock_35
                    with hpunch
                    m "This was a bad idea! {w=2}{nw}"
                    
                elif inventory_select == "batterydry":
                    if battery_full == False:
                        m "Let's charge that battery pack! {w=3} {nw}"
                        call use_item from _call_use_item_12
                        
                        show batterydry behind lighthouse, shadow:
                            pos (650, 220)
                            zoom 0.3
                        
                        call xylo_island_waiting from _call_xylo_island_waiting
                        
                        hide batterydry
                        call get_item("batterydry") from _call_get_item_2
                        $ battery_full = True
                    else:
                        m "The battery pack is already charged. {w=3} {nw}"
                        $ inventory_select = ""
                    
                else:
                    call dialog_nosense from _call_dialog_nosense_75

                
            $ startpos = 2

            
        if exitpos == 3:
            if startpos == 3:
                if inventory_select == "":
                    m "I can see a small island on the other side.{w=3.5} {nw}"
                    m "I'd love to go there!{w=3} {nw}"
                
                elif inventory_select == "wood":
                    call dialog_nobonfire from _call_dialog_nobonfire_2
            $ startpos = 3

            
        if exitpos == 4:
            $ startpos = 3
            jump xylo_sea_island

        
        
        if exitpos == 11: # cabin
            
            if xylo_sea_cabin_door_open == True:
                $ startpos = 3
                call sound_door from _call_sound_door_48
                jump xylo_island_cabin
            
            if startpos == 11:
                call dialog_closed from _call_dialog_closed_54
            
            $ startpos = 11   

            
        if exitpos == 22:
            if startpos == 22:
                if inventory_select == "wood":
                    call dialog_nobonfire from _call_dialog_nobonfire_3
                else:
                    if "wood" not in inventory:
                        m "There is some driftwood on the beach. {w=3.5} {nw}"
                        call take_item("wood") from _call_take_item_27
                    else:
                        m "The sand of this beach is white and thin... {w=3.5} {nw}"
                        m "Nice beach! {w=2.5} {nw}"
                        m "But I don't think is is the right time to think about lying around at the beach. {w=4} {nw}"
                        m "No. {w=1} {nw}"
                        m "Not yet! {w=1.5} {nw}"
                        
            $ startpos = 22

            
        if exitpos == 33:
            $ startpos = 33

            
        if exitpos == 44:
            $ startpos = 44

        


