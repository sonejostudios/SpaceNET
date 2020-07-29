# MAPS

init:
    $ megaship_key_open = False #?
    
    $ cargo_conveyor_dir = False


############################################
label cargo_conveyor2:
    
    call atmo_conveyor from _call_atmo_conveyor_1
    
    scene bgcolor
    show screen notify("cargo conveyor room")
    
    show cargo_conveyor:
        yzoom -1
        
    
    if cargo_conveyor_dir == False:
        show bigdoor behind cargo_conveyor:
            rotate 90
            alpha 0.3
            anchor (0.5,0.5)
            pos (600,330)
            linear 1 pos (600,365)
            repeat
    else:
        show bigdoor behind cargo_conveyor:
            rotate 90
            alpha 0.3
            anchor (0.5,0.5)
            pos (600,365)
            linear 1 pos (600,330)
            repeat
        
        
    #show terminalmap:
    #    anchor (0.5, 0.5)
    #    pos (260,420)
    
    show doorh:
        pos (350, 37)
        
    show doorh as doorh2:
        pos (400, 443)
        
    show buttonscreen:
        pos (500, 440)
        
        
    show tube:
        pos (-440, 240)
    
    
    #boxes     
    show box:
        pos (200,390)
        
    show box as box2:
        pos (300,390)
        
    show box as box3:
        pos (300,290)
        
    show box as box4:
        pos (710,90)
        
    show box as box5:
        pos (100,90)
        
        
    #show warningfloor:
    #    anchor (0.5,0.5)
    #    pos (510,240)
    #    rotate 90

        
    if countdown_sec <= 0:
        $ alarm_on = False
        $ cargo_reactor_state = "working"
        
        
    # atmo sound
    if renpy.music.is_playing(channel='atmo') == False:
        call sound_conveyor from _call_sound_conveyor
    
    
    
    # set all variables for the map (nodes and path)
    $ nodeA = (80, 240)
    $ nodeB = (500, 160)
    $ nodeC = (500, 415)
    $ nodeD = (635, 180)

    $ nodeAA = (635, 255)
    $ nodeBB = (400, 418)
    $ nodeCC = (351, 58)
    $ nodeDD = (632, 427)

    $ pathA = (nodeA, nodeB, (0, 0), nodeD, (0, 0), (0, 0), nodeCC, (0, 0))
    $ pathB = (nodeA, nodeB, nodeC, nodeD, (0, 0), nodeBB, nodeCC, (0, 0))
    $ pathC = ((0, 0), nodeB, nodeC, (0, 0), (0, 0), nodeBB, nodeCC, (0, 0))
    $ pathD = (nodeA, nodeB, (0, 0), nodeD, nodeAA, (0, 0), nodeCC, (0, 0))
     
    $ pathAA = ((0, 0), (0, 0), (0, 0), nodeD, nodeAA, (0, 0), (0, 0), (0, 0))
    $ pathBB = ((0, 0), nodeB, nodeC, (0, 0), (0, 0), nodeBB, nodeCC, (0, 0))
    $ pathCC = (nodeA, nodeB, nodeC, nodeD, (0, 0), nodeBB, nodeCC, (0, 0))
    $ pathDD = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)
    
    if playertype == "minidroid":
        $ pathD = (nodeA, nodeB, (0, 0), nodeD, (0, 0), (0, 0), nodeCC, (0, 0))
    
    
    # conveyor animation in
    if cargo_conveyor_move == True:
        show player:
            pos (636,530)
            linear 8 pos nodeAA
        
        if shadow_enable == 1:
            show shadow:
                pos (636,530)
                linear 8 pos nodeAA
            
        pause 8
        show player:
            linear 0.5 pos nodeD
            
        if shadow_enable == 1:
            show shadow:
                linear 0.5 pos nodeD
        pause 0.5
        
        $ startpos = 4
        
        $ cargo_conveyor_move = False
        
        
    if playertype == "minidroid" and startpos == 1:
        show minidroid:
            pos (0, 240)
            linear 0.5 pos nodeA
            
        if shadow_enable == 1:
            show shadow:
                pos nodeA
        
        pause 0.5
        hide minidroid
        


label loop_cargo_conveyor2:

    while True:
        # alarm
        call alarm_check from _call_alarm_check_14
        
        # start "move through the map" loop
        call startpos from _call_startpos_73

        # do something at node?
        if exitpos == 1:
            if startpos == 1:
                if playertype == "minidroid":
                    $ startpos = 4
                    
                    hide player
                    show minidroid:
                        pos nodeA
                        linear 0.5 pos (0, 240)
                    pause 0.5
                    
                    # stop conveyor sound
                    stop atmo
                    
                    jump cargo_aeration
                else:
                    if inventory_select == "":
                        call dialog_notfitting from _call_dialog_notfitting_5
                    
                    elif inventory_select == "minidroid":
                        m "Why going that way if I can walk normally?{w=3}{nw}"
                        m "I should focus on the mission!{w=3}{nw}"
                    else:
                        call dialog_nosense from _call_dialog_nosense_17
            $ startpos = 1

            
        if exitpos == 2:
            if startpos == 2:
                call dialog_nothing from _call_dialog_nothing_50
            
            $ startpos = 2
            
            
        if exitpos == 3:
            if startpos == 3:
                show screen cargo_conveyor_panel2
            $ startpos = 3
            
        if exitpos == 4:
            if startpos == 4:
                if playertype == "player":
                    m "This is a conveyor.{w=2}{nw}"
                    m "It transports the goods to the next room.{w=3}{nw}"
                else:
                    m "Bad idea... {w=1}I don't want to destroy the minidroid!{w=3}{nw}"
                    
            $ startpos = 4
            

        #conveyor animation out
        if exitpos == 11:
            $ startpos = 11
            
            if cargo_conveyor_dir == False:
                show player:
                    pos nodeAA
                    linear 8 ypos 530
                if shadow_enable == 1:
                    show shadow:
                        pos nodeAA
                        linear 8 ypos 530
                else:
                    hide shadow
                        
                pause 7
                $ cargo_conveyor_move = True
                jump cargo_conveyor1
                
            else:
                show player:
                    pos nodeAA
                    linear 0.5 pos nodeD
                pause 0.5
                m "No way I can walk against the conveyor!{w=3}{nw}"
                $ startpos = 4
                
                
            
            
        if exitpos == 22:
            if startpos == 22:
                call dialog_closed from _call_dialog_closed_38
                #jump cargo_conveyor1
                
            $ startpos = 22
            
            
        if exitpos == 33:
            if playertype == "minidroid":
                call dialog_ndd from _call_dialog_ndd
            else:
                if startpos == 33:
                    call sound_door from _call_sound_door_153
                    $ startpos = 1
                    
                    # stop conveyor sound
                    stop atmo
                    
                    jump cargo_reactor
            
            $ startpos = 33

            
        if exitpos == 44:
            $ startpos = 44



### button screen



#button screen
screen cargo_conveyor_panel2 zorder -999:
    #add "#112119"
    
    on "show" action SetVariable("pnc_nodes_visible", False)
    on "hide" action SetVariable("pnc_nodes_visible", True)
    
    imagebutton: 
        idle "images/maps/bg.png" 
        action [Hide("cargo_conveyor_panel2"), Jump("cargo_conveyor2")]
            
    add "inventory/inventory.png"

    hbox xalign 0.5 yalign 0.5:
        vbox xalign 0.5:
            
            label "Conveyor direction" at center
            null height 10
            imagebutton at center:
                auto "images/buttonbig_%s.png" 
                action [ToggleVariable("cargo_conveyor_dir"), Play("sound", "sounds/movingwall.ogg")]
            null height 10
            label "Reverse" at center
            
        
            
    if shadow_enable == 1:
        add "images/shadow.png" align (0.5,0.5)
    

