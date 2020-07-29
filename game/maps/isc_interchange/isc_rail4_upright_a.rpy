# MAPS

############################################


init:
    $ isc_containerpos4 = 2
    $ isc_containermoveto4 = 2


label isc_rail4a:
    
    image isc_rail4 = imagemapsdir + "isc_rail4.png"
    
    scene bgcolor
    #show screen notify("A")
    
    call show_space from _call_show_space_9
    
    
    show isc_rail4
    
    
    #show warningfloor:
    #    anchor (0.5,0.5)
    #    pos (570,240)
    #    rotate 90

    
    
    
    #show light:
    #    pos (115,30)
    #    
    #show light as light2:
    #    pos (115,240)
    #    
    #show light as light3:
    #    pos (115,430) 

    
    
    
    # set all variables for the map (nodes and path)
    $ nodeA = (40, 161)
    $ nodeB = (268, 133)
    $ nodeC = (255, 42)
    $ nodeD = (269, 406)

    $ nodeAA = (200, 368)
    $ nodeBB = (196, 456)
    $ nodeCC = (30, 400)
    $ nodeDD = (385, 284)

    $ pathA = (nodeA, nodeB, nodeC, (0, 0), (0, 0), (0, 0), (0, 0), (0, 0))
    $ pathB = (nodeA, nodeB, nodeC, (0, 0), (0, 0), (0, 0), (0, 0), (0, 0))
    $ pathC = (nodeA, nodeB, nodeC, (0, 0), (0, 0), (0, 0), (0, 0), (0, 0))
    $ pathD = ((0, 0), (0, 0), (0, 0), nodeD, nodeAA, nodeBB, (0, 0), (0, 0))
     
    $ pathAA = ((0, 0), (0, 0), (0, 0), nodeD, nodeAA, nodeBB, (0, 0), (0, 0))
    $ pathBB = ((0, 0), (0, 0), (0, 0), nodeD, nodeAA, nodeBB, (0, 0), (0, 0))
    $ pathCC = ((0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), nodeCC, (0, 0))
    $ pathDD = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)
    
    
    if playertype == "minidroid":
        show playercross:
            pos nodeC
    
    
    # container position
    if isc_containerpos4 == 1:
        show isc_moving_room:
            pos (376,138)
        #$ pathC = (nodeA, nodeB, nodeC, nodeD, (0, 0), (0, 0), nodeCC, (0, 0))
    
    if isc_containerpos4 == 2:
        show isc_moving_room:
            pos (376,408)
        #$ pathC = (nodeA, nodeB, nodeC, nodeD, (0, 0), (0, 0), (0, 0), (0, 0))
        
        

    # shadow
    #if shadow_enable == 1:
    #    show shadow zorder 800:
    #        pos nodeA
            
            
            


label loop_isc_rail4a:
    
    while True:

        # start "move through the map" loop
        call startpos from _call_startpos_38

        # do something at node?
        if exitpos == 1:
            call sound_door from _call_sound_door_93
            $ startpos = 22
            jump isc_rail3

            
            

            
        if exitpos == 2:
            if startpos == 2 and isc_containerpos4 == 2:
                call dialog_closed from _call_dialog_closed_16
            
            if isc_containerpos4 == 1:
                call sound_door from _call_sound_door_94
                show player:
                    pos (373,136)
                pause 0.7
                call sound_door from _call_sound_door_95
                $ startpos = 2
                jump isc_rail4b
            $ startpos = 2
            

            
        if exitpos == 3:
            if isc_containerpos4 == 2:
                if inventory_select == "":
                    call dialog_notfitting from _call_dialog_notfitting_3
                
                if inventory_select != "minidroid" and inventory_select != "":
                    call dialog_nosense from _call_dialog_nosense_12
                
                if inventory_select == "minidroid":
                    
                    m "I can use the mini droid... let's go ! {w=2.5} {nw}"
                    call use_and_keep_item from _call_use_and_keep_item_17
                    call sound_connected from _call_sound_connected_28
                    with flash
                    show minidroid:
                        pos nodeC
                        linear 2 pos (500,42)
                    pause 2
                    $ startpos = 3
                    $ playertype = "minidroid"
                    hide minidroid
                    show playercross:
                        pos nodeC
                    
                    #"next scene!"
                    jump isc_rail4b
                
            else:
                call dialog_nosense from _call_dialog_nosense_13
                    
            
            $ startpos = 3
                
                
                
            
            
        if exitpos == 4:
            if startpos == 4 and isc_containerpos4 == 1:
                #call dialog_closed
                call sound_door_locked from _call_sound_door_locked_1
                md "It is locked!{w=1.5} {nw}"
            
            if isc_containerpos4 == 2:
                call sound_door from _call_sound_door_96
                show player:
                    pos (376,406)
                pause 0.7
                call sound_door from _call_sound_door_97
                $ startpos = 4
                jump isc_rail4b
            $ startpos = 4

            

        #exits routing "got to map and set position for next map"
        if exitpos == 11:       #if going out at AA
            if startpos == 11:
                show screen isc_rail4_button1
            $ startpos = 11

            
        if exitpos == 22:
            $ startpos = 1
            jump isc_rail5

            
        if exitpos == 33:
            $ startpos = 44
            jump isc_rail3

            
        if exitpos == 44:
            m "I can see on the other side....  but...{w=2} {nw}"
            call dialog_nothing from _call_dialog_nothing_29
            $ startpos = 44
            #jump isc_rail3

            



screen isc_rail4_button1 zorder -999:
    
    on "show" action SetVariable("pnc_nodes_visible", False)
    on "hide" action SetVariable("pnc_nodes_visible", True)

    #add "#112119"
    
    imagebutton: 
        idle "images/maps/bg.png" 
        action Hide("isc_rail4_button1")
            
    add "images/infopanel.png"
    
    #text "\n [minitrain_button1] - [minitrain_button2] - [minitrain_button3] -- [minitrain_way]"
    
    hbox xalign 0.5 yalign 0.5:
        vbox xalign 0.5:
            label "container 3\nposition 1" at center
            null height 10
            imagebutton: 
                auto "images/buttonbig_%s.png"
                action SetVariable("isc_containermoveto4", 1), Play("sound", "sounds/collect.ogg"), Hide("isc_rail4_button1"), Jump("isc_movingroom_anim4") at center

        null width 100
        
        vbox xalign 0.5:
            label "container 3\nposition 2" at center
            null height 10
            imagebutton: 
                auto "images/buttonbig_%s.png"
                action SetVariable("isc_containermoveto4", 2), Play("sound", "sounds/collect.ogg"), Hide("isc_rail4_button1"), Jump("isc_movingroom_anim4") at center  
    
    if shadow_enable == 1:
        add "images/shadow.png" align (0.5,0.5)
                
                
    


label isc_movingroom_anim4:
    
    
    #"move to [isc_containermoveto4] - pos [isc_containerpos4]"
    
    if isc_containermoveto4 < isc_containerpos4 :
        
        show isc_moving_room:
            pos (376,408)
            linear 3 pos (376,138)
        call sound_lift from _call_sound_lift_4
        pause 3
        

    if isc_containermoveto4 > isc_containerpos4:
        
        show isc_moving_room:
            pos (376,138)
            linear 3 pos (376,408)
        call sound_lift from _call_sound_lift_5
        pause 3
        
    
    $ isc_containerpos4 = isc_containermoveto4
    jump loop_isc_rail4a
    
    
    

