# MAPS

############################################


init:
    $ isc_containerpos3 = 2
    $ isc_containermoveto3 = 2


label isc_rail3:
    
    image isc_rail3 = imagemapsdir + "isc_rail3.png"
    
    scene bgcolor
    #show screen notify("Industrial Space City")
    
    call show_space from _call_show_space_17
    
    show isc_rail3
    
    
    #show warningfloor:
    #    anchor (0.5,0.5)
    #    pos (570,240)
    #    rotate 90

    
    
    
    show light:
        pos (115,30)
        
    show light as light2:
        pos (115,240)
        
    show light as light3:
        pos (115,430) 

    
    
    
    # set all variables for the map (nodes and path)
    $ nodeA = (338, 438)
    $ nodeB = (340, 360)
    $ nodeC = (645, 459)
    $ nodeD = (657, 368)

    $ nodeAA = (338, 148)
    $ nodeBB = (760, 80)
    $ nodeCC = (524, 72)
    $ nodeDD = (775, 375)

    $ pathA = (nodeA, nodeB, (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0))
    $ pathB = (nodeA, nodeB, (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0))
    $ pathC = ((0, 0), (0, 0), nodeC, nodeD, (0, 0), (0, 0), (0, 0), nodeDD)
    $ pathD = ((0, 0), (0, 0), nodeC, nodeD, (0, 0), (0, 0), (0, 0), nodeDD)
     
    $ pathAA = ((0, 0), (0, 0), (0, 0), (0, 0), nodeAA, nodeBB, nodeCC, (0, 0))
    $ pathBB = ((0, 0), (0, 0), (0, 0), (0, 0), nodeAA, nodeBB, nodeCC, (0, 0))
    $ pathCC = ((0, 0), (0, 0), (0, 0), (0, 0), nodeAA, nodeBB, nodeCC, (0, 0))
    $ pathDD = ((0, 0), (0, 0), nodeC, nodeD, (0, 0), (0, 0), (0, 0), nodeDD)
    
    
    
    # container position
    if isc_containerpos3 == 1:
        show isc_moving_room:
            pos (337,255)
            rotate 90
        #$ pathC = (nodeA, nodeB, nodeC, nodeD, (0, 0), (0, 0), nodeCC, (0, 0))
    
    if isc_containerpos3 == 2:
        show isc_moving_room:
            pos (700,255)
            rotate 90
        #$ pathC = (nodeA, nodeB, nodeC, nodeD, (0, 0), (0, 0), (0, 0), (0, 0))
        
        

    # shadow
    #if shadow_enable == 1:
    #    show shadow zorder 800:
    #        pos nodeA
            
            
            


label loop_isc_rail3:
    
    while True:

        # start "move through the map" loop
        call startpos from _call_startpos_67

        # do something at node?
        if exitpos == 1:
            call sound_door from _call_sound_door_143
            $ startpos = 2
            jump isc_rail1

            
            

            
        if exitpos == 2:
            if startpos == 2 and isc_containerpos3 == 2:
                call dialog_closed from _call_dialog_closed_34
            
            if isc_containerpos3 == 1:
                call sound_door from _call_sound_door_144
                show player:
                    pos (337,250)
                pause 0.7
                call sound_door from _call_sound_door_145
                show player:
                    pos nodeAA
                $ startpos = 11
                jump loop_isc_rail3
            $ startpos = 2
            

            
        if exitpos == 3:
            #call sound_door
            $ startpos = 44
            jump isc_rail1
                
                
                
            
            
        # button screen - demo panel
        if exitpos == 4:
            if startpos == 4:
                
                if demo_version == False:
                    show screen isc_rail3_button1
                
                # demo panel
                else:
                    call demo_panel from _call_demo_panel
            
            $ startpos = 4
            #jump loop_isc_rail3

            

        #exits routing "got to map and set position for next map"
        if exitpos == 11:       #if going out at AA
            if isc_containerpos3 == 1:
                call sound_door from _call_sound_door_146
                show player:
                    pos (337,250)
                pause 0.7
                call sound_door from _call_sound_door_147
                show player:
                    pos nodeB
                $ startpos = 2
                jump loop_isc_rail3
            $ startpos = 11

            
        if exitpos == 22:
            #call dialog_closed
            $ startpos = 1
            call sound_door from _call_sound_door_148
            jump isc_rail4a

            
        if exitpos == 33:
            if startpos == 33:
                if inventory_select == "":
                    call dialog_nothing from _call_dialog_nothing_41
                else:
                    call dialog_nosense from _call_dialog_nosense_15
            $ startpos = 33

            
        if exitpos == 44:
            $ startpos = 33
            jump isc_rail4a

            



screen isc_rail3_button1 zorder -999:
    
    on "show" action SetVariable("pnc_nodes_visible", False)
    on "hide" action SetVariable("pnc_nodes_visible", True)

    #add "#112119"
    
    imagebutton: 
        idle "images/maps/bg.png" 
        action Hide("isc_rail3_button1")
            
    add "images/infopanel.png"
    
    #text "\n [minitrain_button1] - [minitrain_button2] - [minitrain_button3] -- [minitrain_way]"
    

    hbox xalign 0.5 yalign 0.5:
        vbox xalign 0.5:
            label "container 2\nposition 1" at center
            null height 10
            imagebutton: 
                auto "images/buttonbig_%s.png"
                action SetVariable("isc_containermoveto3", 1), Play("sound", "sounds/collect.ogg"), Hide("isc_rail3_button1"), Jump("isc_movingroom_anim3") at center

        null width 100
        
        vbox xalign 0.5:
            label "container 2\nposition 2" at center
            null height 10
            imagebutton: 
                auto "images/buttonbig_%s.png"
                action SetVariable("isc_containermoveto3", 2), Play("sound", "sounds/collect.ogg"), Hide("isc_rail3_button1"), Jump("isc_movingroom_anim3") at center  


    if shadow_enable == 1:
        add "images/shadow.png" align (0.5,0.5)
                
                
    

# demo panel
label demo_panel:

    $ info_panel_symbol = "exit"
    
    $ showtext = """


- End of demo -

You reached the end of the demo version....
Now shut down your computer and go to sleep!

"""

    call info_panel from _call_info_panel_15
    
    #call sound_scan
    #with pixellate
    
    return






label isc_movingroom_anim3:
    
    
    #"move to [isc_containermoveto3] - pos [isc_containerpos3]"
    
    if isc_containermoveto3 < isc_containerpos3 :
        
        show isc_moving_room:
            pos (700,255)
            linear 3 pos (337,255)
        call sound_lift from _call_sound_lift_6
        pause 3
        

    if isc_containermoveto3 > isc_containerpos3:
        
        show isc_moving_room:
            pos (337,255)
            linear 3 pos (700,255)
        call sound_lift from _call_sound_lift_7
        pause 3
        
    
    $ isc_containerpos3 = isc_containermoveto3
    jump loop_isc_rail3
    
    
    

