# MAPS

############################################

init:
    $ cargo_grate = True


# room with cleaning robot
label cargo_smallroom: 
    
    stop music fadeout 1.0
    call atmo_base from _call_atmo_base_1
    
    
    image crossroomsmall = imagemapsdir + "crossroomsmall.png"
    
    scene bgcolor
    
    show crossroomsmall at truecenter
    show screen notify("cargo room")

        
    #show tube behind crossroomsmall at truecenter
    
    
    $ landing = False
    
    
    show doorh:
        pos (400, 335)
        
        
    show puddle:
        anchor (0.5,0.5)
        pos (352, 190)
        alpha 0.2
        
    show robot:
        anchor (0.5,0.5)
        pos (375, 218)
        rotate 25
        
    
    
    
    # set all variables for the map (nodes and path)
    $ nodeA = (400, 160)
    $ nodeB = (480, 240)
    $ nodeC = (400, 315)
    $ nodeD = (320, 240)
    

    $ nodeAA = (400, 240)
    $ nodeBB = (-100, -100)
    $ nodeCC = (-100, -100)
    $ nodeDD = (-100, -100)

    $ pathA = (nodeA, nodeB, nodeC, nodeD, (0, 0), (0, 0), (0, 0), (0, 0))
    $ pathB = (nodeA, nodeB, nodeC, nodeD, (0, 0), (0, 0), (0, 0), (0, 0))
    $ pathC = ((0, 0), (0, 0), nodeC, (0, 0), nodeAA, (0, 0), (0, 0), (0, 0))
    $ pathD = (nodeA, nodeB, nodeC, nodeD, (0, 0), (0, 0), (0, 0), (0, 0))
     
    $ pathAA = ((0, 0), (0, 0), nodeC, (0, 0), nodeAA, (0, 0), (0, 0), (0, 0))
    $ pathBB = (nodeA, nodeB, nodeC, nodeD, (0, 0), (0, 0), (0, 0), (0, 0))
    $ pathCC = (nodeA, nodeB, nodeC, nodeD, (0, 0), (0, 0), (0, 0), (0, 0))
    $ pathDD = (nodeA, nodeB, nodeC, nodeD, (0, 0), (0, 0), (0, 0), (0, 0))
    


label loop_cargo_smallroom:

    while True:
        
        # alarm
        call alarm_check from _call_alarm_check_3

        # start "move through the map" loop
        call startpos from _call_startpos_5
        

        # do something at node?
        if exitpos == 1:
            $ startpos = 1 

            
        if exitpos == 2:
            $ startpos = 2
            

        if exitpos == 3:
            $ startpos = 2
            call sound_door from _call_sound_door_16
            jump cargo_multimap1
            


            
            
        if exitpos == 4:
            $ startpos = 4


        #######
        
        if exitpos == 11:
            if startpos == 11:
                m "There is a cleaning robot on the floor.{w=3}{nw}"
                m "It seems to be broken.{w=2}{nw}"
                
                if "robotcard" not in inventory:
                    m "Hey! There is something there.{w=3}{nw}"
                    m "It looks like an id card.{w=3}{nw}"
                    
                    call take_item("robotcard") from _call_take_item_1

                    
            $ startpos = 11
 
            
        if exitpos == 22:
            $ startpos = 22

            
        if exitpos == 33:
            $ startpos = 33

            
        if exitpos == 44:
            $ startpos = 44









# tube room
label cargo_smallroom_tube: 
    
    stop music fadeout 1.0
    call atmo_base from _call_atmo_base_2
    
    image crossroomsmall = imagemapsdir + "crossroomsmall.png"
    
    scene bgcolor
    
    show crossroomsmall at truecenter
    show screen notify("cargo room")

        
    show tube:
        pos (955,240)
    
    
    $ landing = False
    
    
    show doorv:
        pos (308, 240)


    # grate
    if cargo_grate == True:
        show doorv as grate:
            pos (465, 240)
            zoom 0.5
            

    # set all variables for the map (nodes and path)
    $ nodeA = (400, 160)
    $ nodeB = (-100, -100)#(480, 240)
    $ nodeC = (400, 315)
    $ nodeD = (330, 240)
    

    $ nodeAA = (440, 240)
    $ nodeBB = (-100, -100)
    $ nodeCC = (-100, -100)
    $ nodeDD = (-100, -100)

    $ pathA = (nodeA, nodeB, nodeC, nodeD, (0, 0), (0, 0), (0, 0), (0, 0))
    $ pathB = (nodeA, nodeB, nodeC, nodeD, (0, 0), (0, 0), (0, 0), (0, 0))
    $ pathC = ((0, 0), (0, 0), nodeC, (0, 0), nodeAA, (0, 0), (0, 0), (0, 0))
    $ pathD = ((0, 0), (0, 0), (0, 0), nodeD, nodeAA, (0, 0), (0, 0), (0, 0))
     
    $ pathAA = ((0, 0), (0, 0), (0, 0), nodeD, nodeAA, (0, 0), (0, 0), (0, 0))
    $ pathBB = (nodeA, nodeB, nodeC, nodeD, (0, 0), (0, 0), (0, 0), (0, 0))
    $ pathCC = (nodeA, nodeB, nodeC, nodeD, (0, 0), (0, 0), (0, 0), (0, 0))
    $ pathDD = ((0, 0), (0, 0), (0, 0), nodeD, nodeAA, (0, 0), (0, 0), (0, 0))
    
    
    if playertype == "minidroid":
        show playercross:
            pos nodeAA
            
    # anim minidroid back
    if startpos == 11:
        show minidroid:
            pos (800,240)
            ease 1 pos nodeAA
        pause 1
        $ playertype = "player"
        hide minidroid
        hide playercross
        
    


label loop_cargo_smallroom_tube:

    while True:
        
        # alarm
        call alarm_check from _call_alarm_check_4

        # start "move through the map" loop
        call startpos from _call_startpos_6
        

        # do something at node?
        if exitpos == 1:
            $ startpos = 1 

            
        if exitpos == 2:
            $ startpos = 2
            

        if exitpos == 3:
            $ startpos = 2

            
            
        if exitpos == 4:
            $ startpos = 2
            stop atmo fadeout 1.0
            call sound_door from _call_sound_door_17
            jump cargo_multimap1
            $ startpos = 4


        #######
        
        if exitpos == 11:
            if startpos == 11:
                if cargo_grate == False:
                
                    if inventory_select == "minidroid":
                        m "I can use the minidroid to enter it...{w=2} Let's try! {w=2}{nw}"
                        call use_and_keep_item from _call_use_and_keep_item_1
                        call sound_connected from _call_sound_connected_1
                        with flash
                        show minidroid:
                            pos nodeAA
                            linear 2 pos (800,240)
                        pause 2
                        $ startpos = 1
                        $ playertype = "minidroid"
                        hide minidroid
                        show playercross behind shadow:
                            pos nodeAA
                        
                        $ startpos = 1
                        jump cargo_aeration 
                        
                        
                        
                    elif inventory_select == "" :
                        call dialog_notfitting from _call_dialog_notfitting
                    
                    else:
                        call dialog_nosense from _call_dialog_nosense
                
                
                if cargo_grate == True:
                    if inventory_select == "":
                        m "This is a thin aeration shaft.{w=2}{nw}"
                        m "There is a grate to close it.{w=2}{nw}"
                    
                    if inventory_select == "laser":
                        m "Let's see if I can open it.{w=2}{nw}"
                        call use_and_keep_item from _call_use_and_keep_item_2
                        call sound_electroshock from _call_sound_electroshock
                        with flash
                        $ cargo_grate = False
                        hide grate
                        m "Now it is open!{w=2}{nw}"
                    
                    if inventory_select != "laser" and inventory_select != "":
                        call dialog_nosense from _call_dialog_nosense_1
                        
                        
                    
            
            $ startpos = 11
 
 
 
            
        if exitpos == 22:
            $ startpos = 22

            
        if exitpos == 33:
            $ startpos = 33

            
        if exitpos == 44:
            $ startpos = 44




