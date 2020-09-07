# MAPS

############################################

init:
    $ isc_numpad_1 = 0
    $ isc_numpad_2 = 0
    $ isc_numpad_3 = 0
    $ isc_numpad_4 = 0
    $ isc_numpad_5 = 0
    
    $ isc_numpad_6 = 0
    $ isc_numpad_7 = 0
    $ isc_numpad_8 = 0
    $ isc_numpad_9 = 0
    
    
    


label isc_city_bar_toilets:
    
    stop atmo
    
    
    if isc_bar_music == 1:
        call music_bar_village_deep from _call_music_bar_village_deep
    
    if isc_bar_music == 2:
        call music_bar_chill_deep from _call_music_bar_chill_deep
        
    if isc_bar_music == 3:
        call music_outro_deep from _call_music_outro_deep
    
    if isc_bar_music == 4:
        stop music fadeout 1.0
    
    
    #$ steps_sound = "metal"
    
    image isc_city_bar_toilets = imagemapsdir + "isc_city_bar_toilets.png"
    
    scene bgcolor
    show screen notify("Bathroom")
    
    #call show_space
    
    show isc_city_bar_toilets:
        pos (0,0)
    
    
    # set all variables for the map (nodes and path)
    $ nodeA = (84, 239)
    $ nodeB = (150, 172)
    $ nodeC = (317, 172)
    $ nodeD = (482, 172)

    $ nodeAA = (650, 172)
    $ nodeBB = (388, 286)
    $ nodeCC = (379, 428)
    $ nodeDD = (517, 434)
    

    if drunktime > 0:
        $ nodeBB = (287, 286)    


    $ pathA = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, (0, 0), (0, 0))
    $ pathB = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, (0, 0), (0, 0))
    $ pathC = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, (0, 0), (0, 0))
    $ pathD = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, (0, 0), (0, 0))
     
    $ pathAA = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, (0, 0), (0, 0))
    $ pathBB = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, (0, 0), (0, 0))
    $ pathCC = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)
    $ pathDD = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)
    
    
    # reset numpad
    $ isc_numpad_1 = 0
    $ isc_numpad_2 = 0
    $ isc_numpad_3 = 0
    $ isc_numpad_4 = 0
    $ isc_numpad_5 = 0
    
    $ isc_numpad_6 = 0
    $ isc_numpad_7 = 0
    $ isc_numpad_8 = 0
    $ isc_numpad_9 = 0
    
    

    



label loop_isc_city_bar_toilets:
    
    while True:

        # start "move through the map" loop
        call startpos from _call_startpos_13

        # do something at node?
        if exitpos == 1:
            call sound_door from _call_sound_door_27
            $ startpos = 3
            jump isc_city_bar


        if exitpos == 2:
            if startpos == 2:
                call sound_door from _call_sound_door_28
                $ startpos = 3 
                $ isc_wc = 1
                jump isc_city_bar_wcs
            $ startpos = 2

            
        if exitpos == 3:
            if startpos == 3:
                call sound_door from _call_sound_door_29
                $ startpos = 3 
                $ isc_wc = 2
                jump isc_city_bar_wcs
            $ startpos = 3
            
        
        if exitpos == 4:
            if startpos == 4:
                call sound_door from _call_sound_door_30
                $ startpos = 3 
                $ isc_wc = 3
                jump isc_city_bar_wcs
            $ startpos = 4
           

        #exits routing "got to map and set position for next map"
        if exitpos == 11:
            if startpos == 11:
                #call dialog_closed
                
                if drunktime > 0:
                    m "This button panel looks really,{w=1.0} really,{w=1.0} really,{w=1.0} really...{w=1.0} complicated.{w=2.0} {nw}"
                    jump loop_isc_city_bar_toilets

                
                show screen isc_bar_numpad
                
                #call sound_door
                #$ liftpos = 3
                #jump isc_city_bar_lift1 # to lift
            $ startpos = 11 

            
        if exitpos == 22:
            if startpos == 22:
                
                if drunktime > 0:
                    if isc_bar_bathroom_gem== True:
                        m "This sinks looks interesting. {w=2} {nw}"
                        call take_gem from _call_take_gem
                        $ isc_bar_bathroom_gem = False
                    else:
                        call dialog_nothing from _call_dialog_nothing_15
                    
                else:
                    m "There are the sinks. {w=1.5} {nw}"
                    m "I could wash my hands.... {w=1.5} {nw}"
                    menu:
                        "wash your hands":
                            call sound_tap from _call_sound_tap
                            pause 4
                            call sound_connected from _call_sound_connected_4
                            with flash
                            m "Yeah! My hands are clean now!{w=2.5} {nw}"
                        "do nothing":
                            #with hpunch
                            m "I prefer it dirty.{w=1.5} {nw}"
            $ startpos = 22

            
        if exitpos == 33:
            $ startpos = 33
            
            
        if exitpos == 44:
            $ startpos = 44
            

     
    
    
screen isc_bar_numpad() zorder -999:
    
    on "show" action SetVariable("pnc_nodes_visible", False)
    on "hide" action SetVariable("pnc_nodes_visible", True)

    #add "#112119"
    
    imagebutton: 
        idle "images/maps/bg.png" 
        action Hide("isc_bar_numpad")
            
    add "images/infopanel.png"
    
    #text "\n [minitrain_button1] - [minitrain_button2] - [minitrain_button3] -- [minitrain_way]"
    
    hbox xalign 0.5 yalign 0.2:
        vbox xalign 0.5:
            imagebutton: 
                auto "images/buttonbig_%s.png"
                action ToggleVariable("isc_numpad_1"), Play("sound", "sounds/collect.ogg") at center
            label "1" at center

        null width 10
        
        vbox xalign 0.5:
            imagebutton: 
                auto "images/buttonbig_%s.png"
                action ToggleVariable("isc_numpad_2"), Play("sound", "sounds/collect.ogg") at center
            label "2" at center
            
        null width 10
        
        vbox xalign 0.5:
            imagebutton: 
                auto "images/buttonbig_%s.png"
                action ToggleVariable("isc_numpad_3"), Play("sound", "sounds/collect.ogg") at center
            label "3" at center
            
        null width 10
        
        vbox xalign 0.5:
            imagebutton: 
                auto "images/buttonbig_%s.png"
                action ToggleVariable("isc_numpad_4"), Play("sound", "sounds/collect.ogg") at center
            label "4" at center
        
        null width 10
        
        vbox xalign 0.5:
            imagebutton: 
                auto "images/buttonbig_%s.png"
                action ToggleVariable("isc_numpad_5"), Play("sound", "sounds/collect.ogg") at center
            label "5" at center
            
            
          
    hbox xalign 0.5 yalign 0.8:
        vbox xalign 0.5:
            imagebutton: 
                auto "images/buttonbig_%s.png"
                action ToggleVariable("isc_numpad_6"), Play("sound", "sounds/collect.ogg") at center
            label "6" at center

        null width 10
    
        vbox xalign 0.5:
            imagebutton: 
                auto "images/buttonbig_%s.png"
                action ToggleVariable("isc_numpad_7"), Play("sound", "sounds/collect.ogg") at center
            label "7" at center

        null width 10
        
        vbox xalign 0.5:
            imagebutton: 
                auto "images/buttonbig_%s.png"
                action ToggleVariable("isc_numpad_8"), Play("sound", "sounds/collect.ogg") at center
            label "8" at center
            
        null width 10
        
        vbox xalign 0.5:
            imagebutton: 
                auto "images/buttonbig_%s.png"
                action ToggleVariable("isc_numpad_9"), Play("sound", "sounds/collect.ogg") at center
            label "9" at center
            
        null width 10
        
        vbox xalign 0.5:
            imagebutton: 
                auto "images/buttonbig_%s.png"
                action Jump("isc_numpad_open") at center
            label "open door" at center
          
            
            
    
    if shadow_enable == 1:
        add "images/shadow.png" align (0.5,0.5)
        
        
        

label isc_numpad_open:
    
    if isc_numpad_1 == 1 and isc_numpad_2 == 1 and isc_numpad_4 == 1 and isc_numpad_5 == 1 and isc_numpad_8 == 1 and isc_numpad_3 == 0 and isc_numpad_6 == 0 and isc_numpad_7 == 0 and isc_numpad_9 == 0:
        call sound_connected from _call_sound_connected_5
        with flash
        hide screen isc_bar_numpad
        call sound_door from _call_sound_door_31
        $ liftpos = 3
        
        stop music fadeout 1.0
        
        jump isc_city_bar_lift1 # to lift
        
    else:
        #hide screen isc_bar_numpad
        call sound_electroshock from _call_sound_electroshock_5
        with hpunch
        jump loop_isc_city_bar_toilets
        
        
        
        
        
        
