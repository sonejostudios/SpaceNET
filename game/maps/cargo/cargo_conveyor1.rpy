# MAPS

init:
    $ cargo_conveyor_move = False
    



############################################
label cargo_conveyor1:
    
    stop music fadeout 1.0
    # atmo sound
    call atmo_conveyor from _call_atmo_conveyor
    
    
    image cargo_conveyor = imagemapsdir + "cargo_conveyor.png"
    

    scene bgcolor
    show screen notify("cargo conveyor room")
    
    show cargo_conveyor
    
    
    if cargo_conveyor_dir == False:
        show bigdoor behind cargo_conveyor:
            rotate 90
            alpha 0.3
            anchor (0.5,0.5)
            pos (600,100)
            linear 1 pos (600,135)
            repeat
    else:
        show bigdoor behind cargo_conveyor:
            rotate 90
            alpha 0.3
            anchor (0.5,0.5)
            pos (600,135)
            linear 1 pos (600,100)
            repeat
        
        
    #show terminalmap:
    #    anchor (0.5, 0.5)
    #    pos (260,420)
    
    show doorv:
        pos (32, 240)
        
    show doorh:
        pos (400, 35)
        
    show buttonscreen:
        pos (500, 38)
        
    
    #boxes     
    show box:
        pos (100,90)
        
    show box as box2:
        pos (200,90)
        
    show box as box3:
        pos (300,90)
        
    show box as box4:
        pos (300,190)
        
        
    show box as box5:
        pos (100,390)
        
        
    show box as box6:
        pos (440,390)
        
        

        
    
    
    # set all variables for the map (nodes and path)
    $ nodeA = (52, 240)
    $ nodeB = (440, 325)
    $ nodeC = (500, 60)
    $ nodeD = (636, 300)

    $ nodeAA = (636, 227)
    $ nodeBB = (400, 55)
    $ nodeCC = (692, 424)
    $ nodeDD = (632, 427)

    $ pathA = (nodeA, nodeB, (0, 0), nodeD, (0, 0), (0, 0), (0, 0), (0, 0))
    $ pathB = (nodeA, nodeB, nodeC, nodeD, (0, 0), nodeBB, (0, 0), (0, 0))
    $ pathC = ((0, 0), nodeB, nodeC, (0, 0), (0, 0), nodeBB, (0, 0), (0, 0))
    $ pathD = (nodeA, nodeB, (0, 0), nodeD, nodeAA, (0, 0), (0, 0), (0, 0))
     
    $ pathAA = ((0, 0), (0, 0), (0, 0), nodeD, nodeAA, (0, 0), (0, 0), (0, 0))
    $ pathBB = ((0, 0), nodeB, nodeC, (0, 0), (0, 0), nodeBB, (0, 0), (0, 0))
    $ pathCC = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)
    $ pathDD = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)
    
    

    # conveyor animation in
    if cargo_conveyor_move == True:
        show player:
            pos (636,-30)
            linear 8 pos nodeAA
        
        if shadow_enable == 1:
            show shadow:
                pos (636,-30)
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
        


label loop_cargo_conveyor1:
    
    while True:
        # alarm
        call alarm_check from _call_alarm_check_8
        
        # start "move through the map" loop
        call startpos from _call_startpos_24

        # do something at node?
        if exitpos == 1:
            call sound_door from _call_sound_door_53
            $ startpos = 2
            $ multiposx = 3
            $ multiposy = 3
            
            # stop conveyor sound
            stop atmo
            
            jump cargo_multimap1
            
        if exitpos == 2:
            if startpos == 2:
                if inventory_select == "":
                    m "This is a container.{w=2}{nw}"
                    m "What is inside?{w=2}{nw}"
                    if cargo_container_cash > 0:
                        m "Hey, there is something metalic under the container!{w=3}{nw}"
                
                elif inventory_select == "magnet" and cargo_container_cash > 0:
                    call use_and_keep_item from _call_use_and_keep_item_11
                    m "Hey, there are some coins!{w=2}{nw}"
                    call io_cash(cargo_container_cash) from _call_io_cash_3
                    $ cargo_container_cash = 0
                    
                else:
                    call dialog_nosense from _call_dialog_nosense_7
                
            
            $ startpos = 2
            
        if exitpos == 3:
            if startpos == 3:
                show screen cargo_conveyor_panel1
            $ startpos = 3
            
        if exitpos == 4:
            if startpos == 4:
                m "This is a conveyor.{w=2}{nw}"
                m "It transports the goods to the next room.{w=3}{nw}"
            $ startpos = 4
            

        #conveyor animation out
        if exitpos == 11:
            $ startpos = 11
            
            if cargo_conveyor_dir == True:
                show player:
                    pos nodeAA
                    linear 8 ypos -50
                if shadow_enable == 1:
                    show shadow:
                        pos nodeAA
                        linear 8 ypos -50
                else:
                    hide shadow
                        
                pause 7
                $ cargo_conveyor_move = True
                jump cargo_conveyor2
            
            else:
                show player:
                    pos nodeAA
                    linear 0.5 pos nodeD
                pause 0.5
                m "No way I can walk against the conveyor!{w=3}{nw}"
                $ startpos = 4
            
            
        if exitpos == 22:
            if startpos == 22:
                call dialog_closed from _call_dialog_closed_10
                #jump cargo_conveyor2
                
            $ startpos = 22
            
            
        if exitpos == 33: 
            $ startpos = 33

            
        if exitpos == 44:
            $ startpos = 44




#button screen
screen cargo_conveyor_panel1 zorder -999:
    #add "#112119"
    
    on "show" action SetVariable("pnc_nodes_visible", False)
    on "hide" action SetVariable("pnc_nodes_visible", True)
    
    imagebutton: 
        idle "images/maps/bg.png" 
        action [Hide("cargo_conveyor_panel1"), Jump("cargo_conveyor1")]
            
    add "inventory/inventory.png"

    hbox xalign 0.5 yalign 0.5:
        vbox xalign 0.5:
            
            label "Conveyor direction" at center
            null height 10
            
            imagebutton at center:
                auto "images/buttonbig_%s.png" 
                action Jump("cargo_conveyor1_button_broken")
            
            null height 10
            label "Reverse" at center
            
        
            
    if shadow_enable == 1:
        add "images/shadow.png" align (0.5,0.5)



label cargo_conveyor1_button_broken:
    call sound_electroshock from _call_sound_electroshock_7
    with hpunch
    m "This control panel is broken! {w=2.0} {nw}"
    hide screen cargo_conveyor_panel1
    jump loop_cargo_conveyor1
    

