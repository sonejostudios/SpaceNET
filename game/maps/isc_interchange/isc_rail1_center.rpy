# MAPS

############################################


init:
    $ isctrain_anim = False
    $ isc_containerpos = 2
    $ isc_containermoveto = 2


label isc_rail1:

    call music_isc from _call_music_isc
    call atmo_spaceship_station from _call_atmo_spaceship_station_2
    
    
    image isc_rail1 = imagemapsdir + "isc_rail1.png"
    
    scene bgcolor
    show screen notify("Industrial Space City")
    
    call show_space from _call_show_space_3
    
    show isc_rail1
    
    
    #show warningfloor:
    #    anchor (0.5,0.5)
    #    pos (570,240)
    #    rotate 90

 
    #call sound_door
        
        
    image isc_moving_room:
        "/images/isc_moving_room.png"
        anchor (0.5,0.5)

    
    
    # set all variables for the map (nodes and path)
    $ nodeA = (290, 220)
    $ nodeB = (344, 50)
    $ nodeC = (421, 112)
    $ nodeD = (344, 430)

    $ nodeAA = (640, 455)
    $ nodeBB = (675, 360)
    $ nodeCC = (630, 115)
    $ nodeDD = (650, 20)

    $ pathA = (nodeA, nodeB, nodeC, nodeD, (0, 0), (0, 0), (0, 0), (0, 0))
    $ pathB = (nodeA, nodeB, nodeC, nodeD, (0, 0), (0, 0), (0, 0), (0, 0))
    $ pathC = (nodeA, nodeB, nodeC, nodeD, (0, 0), (0, 0), (0, 0), (0, 0))
    $ pathD = (nodeA, nodeB, nodeC, nodeD, (0, 0), (0, 0), (0, 0), (0, 0))
     
    $ pathAA = ((0, 0), (0, 0), (0, 0), (0, 0), nodeAA, nodeBB, (0, 0), (0, 0))
    $ pathBB = ((0, 0), (0, 0), (0, 0), (0, 0), nodeAA, nodeBB, (0, 0), (0, 0))
    $ pathCC = ((0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), nodeCC, nodeDD)
    $ pathDD = ((0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), nodeCC, nodeDD)
    
    
    
    # container position
    if isc_containerpos == 1:
        show isc_moving_room:
            pos (525,116)
        #$ pathC = (nodeA, nodeB, nodeC, nodeD, (0, 0), (0, 0), nodeCC, (0, 0))
    
    if isc_containerpos == 2:
        show isc_moving_room:
            pos (525,400)
        #$ pathC = (nodeA, nodeB, nodeC, nodeD, (0, 0), (0, 0), (0, 0), (0, 0))
        
        

    

    # shadow
    if shadow_enable == 1:
        show shadow zorder 800:
            pos nodeA
            
            
    # train entry anim
    if isctrain_anim == True:
        show isctrain:
            transform_anchor True
            pos (-100,220)
            anchor (0.35,0.5)
            easein 2 pos (190,220)
        pause 2
        show isctrain:
            transform_anchor True
            anchor (0.35,0.5)
            pos (190,220)
        
        $ startpos = 1
        $ isctrain_anim = False
        call sound_door from _call_sound_door_54
        
    else:
        show isctrain:
            transform_anchor True
            anchor (0.35,0.5)
            pos (190,220)
            



    # coming from trip
    if triptime == True:
        $ triptime = False
        $ startpos = 1
        call sound_scan from _call_sound_scan_4
        #with Dissolve(0.5)
        with pixellate




label loop_isc_rail1:
    $ pnc_nodes_visible = True
    
    while True:

        # start "move through the map" loop
        call startpos from _call_startpos_25

        # do something at node?
        if exitpos == 1:
            
            if startpos == 1:
                #call dialog_closed
                call sound_door from _call_sound_door_55
                hide player
                show isctrain:
                    rotate 180
                    easeout 2 xpos -200
                pause 0.5
                call sound_train from _call_sound_train
                pause 1.5
                $ startpos = 2  
                jump isc_wagon_anim_toleft
            
            else:
                $ startpos = 1
                jump loop_isc_rail1
            
            

            
        if exitpos == 2:
            call sound_door from _call_sound_door_56
            $ startpos = 1
            jump isc_rail3

            
        if exitpos == 3:
            if startpos == 3 and isc_containerpos == 2:
                call dialog_closed from _call_dialog_closed_11
            
            if isc_containerpos == 1:
                call sound_door from _call_sound_door_57
                show player:
                    pos (520,115)
                pause 0.7
                call sound_door from _call_sound_door_58
                show player:
                    pos nodeCC
                $ startpos = 33
                jump loop_isc_rail1
            $ startpos = 3
                
                
                
            
            
        if exitpos == 4:
            $ startpos = 1
            call sound_door from _call_sound_door_59
            jump isc_rail2

            

        #exits routing "got to map and set position for next map"
        if exitpos == 11:       #if going out at AA
            $ startpos = 4    #go to CC
            jump isc_rail2

            
        if exitpos == 22:
            if startpos == 22:
                show screen isc_rail1_button1
            $ startpos = 22
            jump loop_isc_rail1

            
        if exitpos == 33:
            #if startpos == 33:
            call sound_door from _call_sound_door_60
            show player:
                pos (520,115)
            pause 0.7
            call sound_door from _call_sound_door_61
            show player:
                pos nodeC
            $ startpos = 3
            jump loop_isc_rail1
            
            #$ startpos = 33

            
        if exitpos == 44:
            $ startpos = 3
            jump isc_rail3

            



screen isc_rail1_button1() zorder -999:
    
    on "show" action SetVariable("pnc_nodes_visible", False)
    on "hide" action SetVariable("pnc_nodes_visible", True)

    #add "#112119"
    
    imagebutton: 
        idle "images/maps/bg.png" 
        action Hide("isc_rail1_button1")
            
    add "images/infopanel.png"
    
    #text "\n [minitrain_button1] - [minitrain_button2] - [minitrain_button3] -- [minitrain_way]"
    

    hbox xalign 0.5 yalign 0.5:
        vbox xalign 0.5:
            label "container\nposition 1" at center
            null height 10
            imagebutton: 
                auto "images/buttonbig_%s.png"
                action SetVariable("isc_containermoveto", 1), Play("sound", "sounds/collect.ogg"), Hide("isc_rail1_button1"), Jump("isc_movingroom_anim") at center

        null width 100
        
        vbox xalign 0.5:
            label "container\nposition 2" at center
            null height 10
            imagebutton: 
                auto "images/buttonbig_%s.png"
                action SetVariable("isc_containermoveto", 2), Play("sound", "sounds/collect.ogg"), Hide("isc_rail1_button1"), Jump("isc_movingroom_anim") at center
                

    
    if shadow_enable == 1:
        add "images/shadow.png" align (0.5,0.5)
                
                
    


label isc_movingroom_anim:
    
    
    
    if isc_containermoveto < isc_containerpos :
        
        show isc_moving_room:
            pos (525,400)
            linear 3 pos (525,116)
        call sound_lift from _call_sound_lift_1
        pause 3
        

    if isc_containermoveto > isc_containerpos:
        
        show isc_moving_room:
            pos (525,116)
            linear 3 pos (525,400)
        call sound_lift from _call_sound_lift_2
        pause 3
        
    
    $ isc_containerpos = isc_containermoveto
    jump loop_isc_rail1
    
    
    

