# MAPS

############################################

init:
    $ spaceship_choice_number = 1
    $ spaceship_choice_info = True
    $ spaceship_choice_infotext = ["sd-2", "1500 km/h", "1 m^2", "0 c", "a basic spaceship"]
    
    

label isc_spaceshipport:
    $ pnc_nodes_visible = True
    
    $ landing = False
    
    image isc_spaceshipport = imagemapsdir + "isc_spaceshipport.png"
    
    scene bgcolor
    
    if startpos == 1:
        show screen notify("Spaceship Hangar")
    
    show isc_spaceshipport
   

    hide spaceship1u
    hide spaceship2u
    hide spaceship3u
        
    # spaceships
    if spaceshiptype != "1":
        show spaceship1u:
            pos (480,380)
            zoom 0.5
        
    if spaceshiptype != "2":
        show spaceship2u:
            pos (480,95)
            rotate 180
            zoom 0.55
        
    if spaceshiptype != "3":
        show spaceship3u:
            pos (326,95)
            rotate 180
            zoom 0.6
            
    if spaceshiptype != "4":
        show spaceship4u:
            pos (326,384)
            zoom 0.6
    

    
    # set all variables for the map (nodes and path)
    $ nodeA = (671, 422)
    $ nodeB = (696, 240)
    $ nodeC = (518, 200)
    $ nodeD = (444, 280)

    $ nodeAA = (370, 200)
    $ nodeBB = (285, 280)
    $ nodeCC = (212, 200)
    $ nodeDD = (132, 280)

    $ pathA = (nodeA, nodeB, (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0))
    $ pathB = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)
    $ pathC = ((0, 0), nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)
    $ pathD = ((0, 0), nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)
     
    $ pathAA = ((0, 0), nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)
    $ pathBB = ((0, 0), nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)
    $ pathCC = ((0, 0), nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)
    $ pathDD = ((0, 0), nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)



    image crane:
        "images/crane.png"
        anchor (0.5,0.5)
    
    show crane:
        pos (62, 240)




label loop_isc_spaceshipport:
    
    while True:

        # start "move through the map" loop
        call startpos from _call_startpos_77

        # do something at node?
        if exitpos == 1:       #if at node A
            $ startpos = 1     # stay in A
            
            call sound_door from _call_sound_door_165
            $ landing = False
            $ isc_spaceship_interchange = True
            jump isc_interchange

            
        if exitpos == 2:
            if startpos == 2:
                jump isc_spaceship_info # to board
            
            $ startpos = 2

            
        if exitpos == 3:
            if startpos == 3:
                if spaceshiptype != "2":
                    m "This spaceship is beautiful!{w=2} {nw}"
                else:
                    call dialog_nothing from _call_dialog_nothing_52
            $ startpos = 3
            
        if exitpos == 4:
            if startpos == 4:
                if spaceshiptype != "1":
                    m "This is a basic spaceship.{w=2} {nw}"
                else:
                    call dialog_nothing from _call_dialog_nothing_53
            $ startpos = 4

            

       
        if exitpos == 11:
            if startpos == 11:
                if spaceshiptype != "3":
                    m "This spaceship looks weird, but it has a lot of space in it!{w=4} {nw}"
                else:
                    call dialog_nothing from _call_dialog_nothing_54 
            $ startpos = 11  

            
        if exitpos == 22:
            if startpos == 22:
                if spaceshiptype != "4":
                    m "This spaceship looks amazing! {w=2.5} {nw}"
                    m "I'd love to fly it one day. {w=2.5} {nw}"
                else:
                    call dialog_nothing from _call_dialog_nothing_55
            $ startpos = 22

            
        if exitpos == 33:
            if startpos ==33:
                call dialog_nothing from _call_dialog_nothing_56
            $ startpos = 33

            
        if exitpos == 44:
            if startpos == 44:
                call dialog_nothing from _call_dialog_nothing_57
            $ startpos = 44



# crane animation



label select_spaceship:
    
    $ pnc_nodes_visible = False
    
    #"spaceshiptype: [spaceshiptype] - spaceship_choice_number : [spaceship_choice_number]"
        
    if int(spaceshiptype) == spaceship_choice_number:
        m "I've got it already! {w=2} {nw}"
        jump isc_spaceship_info
    
    hide bg2
    hide infopanel
    hide spaceship1s
    hide spaceship2s
    hide spaceship3s
    hide spaceship4s
    
    hide text
    
    hide screen isc_hangar_screen
    
    if shadow_enable == 1:
        show shadow zorder 999:
            pos nodeB
            

    call sound_crane from _call_sound_crane
    
    if spaceship_choice_number == 1:
        jump crane_anime1
    
    if spaceship_choice_number == 2:
        jump crane_anime2
        
    if spaceship_choice_number == 3:
        jump crane_anime3
        
    if spaceship_choice_number == 4:
        jump crane_anime4
        

label crane_anime1:
    show crane zorder 910:
        pos (62, 240)
        ease 3 xpos 479
    #pause 4
    $ renpy.pause(4, hard='True')
    
    show crane zorder 910:
        ease 3 xpos 62
    show spaceship1u zorder 900:
        ease 3 xpos 62
    #pause 4
    $ renpy.pause(4, hard='True')
    
    show spaceship1u:
        ease 4 ypos 550
    #pause 4
    $ renpy.pause(4, hard='True')
    
    $ spaceshiptype = "1"
    
    #pause 1
    show player:
        ease 0.5 pos nodeA
    pause 0.5
    
    call sound_door from _call_sound_door_166
    $ startpos = 1
    jump isc_interchange

    
label crane_anime2:
    show crane zorder 910:
        pos (62, 240)
        ease 3 xpos 479
    #pause 4
    $ renpy.pause(4, hard='True')
    
    show crane zorder 910:
        ease 3 xpos 62
    show spaceship2u zorder 900:
        ease 3 xpos 62
    #pause 4
    $ renpy.pause(4, hard='True')
    
    show spaceship2u:
        ease 4 ypos 550
    #pause 4
    $ renpy.pause(4, hard='True')
    
    $ spaceshiptype = "2"
    
    #pause 1
    show player:
        ease 0.5 pos nodeA
    pause 0.5
    
    call sound_door from _call_sound_door_167
    $ startpos = 1
    jump isc_interchange



label crane_anime3:
    show crane zorder 910:
        pos (62, 240)
        ease 3 xpos 325
    #pause 4
    $ renpy.pause(4, hard='True')
    
    show crane zorder 910:
        ease 3 xpos 62
    show spaceship3u zorder 900:
        ease 3 xpos 62
    #pause 4
    $ renpy.pause(4, hard='True')
    
    show spaceship3u:
        ease 4 ypos 550
    #pause 4
    $ renpy.pause(4, hard='True')
    
    $ spaceshiptype = "3"
    
    #pause 1
    show player:
        ease 0.5 pos nodeA
    pause 0.5
    
    call sound_door from _call_sound_door_168
    $ startpos = 1
    jump isc_interchange
    
    
    
label crane_anime4:
    show crane zorder 910:
        pos (62, 240)
        ease 3 xpos 325
    #pause 4
    $ renpy.pause(4, hard='True')
    
    show crane zorder 910:
        ease 3 xpos 62
    show spaceship4u zorder 900:
        ease 3 xpos 62
    #pause 4
    $ renpy.pause(4, hard='True')
    
    show spaceship4u:
        ease 4 ypos 550
    #pause 4
    $ renpy.pause(4, hard='True')
    
    $ spaceshiptype = "4"
    
    #pause 1
    show player:
        ease 0.5 pos nodeA
    pause 0.5
    
    call sound_door from _call_sound_door_177
    $ startpos = 1
    jump isc_interchange






###################################################################################################
# spaceship interchange display

screen isc_hangar_screen() zorder -999:
    
    on "show" action SetVariable("pnc_nodes_visible", False)
    on "hide" action SetVariable("pnc_nodes_visible", True)

    #if spaceship_choice_number > 1:
    imagebutton auto "images/dockleft_%s.png" action Play("sound", "sounds/beep.ogg"), Jump("spaceship_choice_previous") align (0.0, 0.5)
    
    #if spaceship_choice_number < 3:
    imagebutton auto "images/dockright_%s.png" action Play("sound", "sounds/beep.ogg"), Jump("spaceship_choice_next") align (1.0, 0.5)

    if spaceship_choice_info == True:
        vbox:
            pos (70,70)
            #text "{color=#8dd35f}DATA"
            #null height 10
            text "{color=#8dd35f}ID: [spaceship_choice_number]"
            text "{color=#8dd35f}Name: [spaceship_choice_infotext[0]]"
            text "{color=#8dd35f}Speed: [spaceship_choice_infotext[1]]"
            text "{color=#8dd35f}Container: [spaceship_choice_infotext[2]]"
            #text "{color=#8dd35f}Price : [spaceship_choice_infotext[3]]"

    
    hbox xalign 0.5 yalign 0.8:
        
        vbox xalign 0.5:
            #label "select" at center
            #null height 10
            imagebutton: 
                auto "images/buttonbig_%s.png"
                action Play("sound", "sounds/collect.ogg"), Jump("select_spaceship") at center
            label "select" at center
                
        null width 100
        
        vbox xalign 0.5:
            #label "exit" at center
            #null height 10
            imagebutton: 
                auto "images/buttonbig_%s.png"
                action Hide("isc_hangar_screen"), Jump("isc_spaceshipport") at center
            label "exit" at center
    
    
    if shadow_enable == 1:
        add "images/shadow.png" align (0.5,0.5)
                
                
    





label isc_spaceship_info:
    
    $ pnc_nodes_visible = False
    
    show bgcolor as bg2
    show infopanel zorder 900
    
    hide shadow
    
    hide spaceship1s
    hide spaceship2s
    hide spaceship3s
    
    hide crane
    
    if spaceship_choice_number == 1:
        show spaceship1s zorder 100:
            ypos 0.3
            xpos 400
        $ spaceship_choice_infotext = ["SD-2", "1500 km/h", "1 m^2", "0 c", "a basic spaceship"]
            
            
    if spaceship_choice_number == 2:
        show spaceship2s zorder 100:
            ypos 0.3
            xpos 400
        $ spaceship_choice_infotext = ["IO-1", "2000 km/h", "6 m^2", "1000 c", "an advanced spaceship with a docking hatch"]
            
            
    if spaceship_choice_number == 3:
        show spaceship3s zorder 100:
            ypos 0.3
            xpos 400
        $ spaceship_choice_infotext = ["SF-3", "700 km/h", "20 m^2", "2000 c", "a scientific spaceship"]
        
        
    if spaceship_choice_number == 4:
        show spaceship4s zorder 100:
            ypos 0.3
            xpos 400
        $ spaceship_choice_infotext = ["IO-4", "3500 km/h", "5 m^2", "3000 c", "a really fast spaceship"]
        
    
    show screen isc_hangar_screen
    
    show text "[spaceship_choice_infotext[4]]":
    #show text "{color=#8dd35f}[spaceship_choice_infotext[4]]":
        pos (0.5,0.5)
    
    pause
    
    hide screen isc_hangar_screen


#label info_panel_hide:

    # hide
    hide bg2
    hide infopanel

    
    hide spaceship1s
    hide spaceship1u
    
    
    $ info_panel_symbol = ""
    $ showtext = ""
    
    
    jump isc_spaceshipport
    
    
    

label spaceship_choice_next:
    if spaceship_choice_number < 4:

        $ spaceship_choice_info = False
        hide text
        
        # 1
        if spaceship_choice_number == 1:
            show spaceship1s:
                ypos 0.3
                xpos 400
                ease 1 xpos -200
            
            show spaceship2s:
                ypos 0.3
                xpos 1000
                ease 1 xpos 400
                
        # 2
        if spaceship_choice_number == 2:
            show spaceship2s:
                ypos 0.3
                xpos 400
                ease 1 xpos -200
            
            show spaceship3s:
                ypos 0.3
                xpos 1000
                ease 1 xpos 400
                
        # 3
        if spaceship_choice_number == 3:
            show spaceship3s:
                ypos 0.3
                xpos 400
                ease 1 xpos -200
            
            show spaceship4s:
                ypos 0.3
                xpos 1000
                ease 1 xpos 400
              
        
        pause 1
        $ spaceship_choice_number += 1
        $ spaceship_choice_info = True
        
        
    jump isc_spaceship_info


    
label spaceship_choice_previous:
    if spaceship_choice_number > 1:
        
        $ spaceship_choice_info = False
        hide text
        
        
        # 4
        if spaceship_choice_number == 4:
            show spaceship4s:
                ypos 0.3
                xpos 400
                ease 1 xpos 1000
            
            show spaceship3s:
                ypos 0.3
                xpos -200
                ease 1 xpos 400
                
        
        # 3
        if spaceship_choice_number == 3:
            show spaceship3s:
                ypos 0.3
                xpos 400
                ease 1 xpos 1000
            
            show spaceship2s:
                ypos 0.3
                xpos -200
                ease 1 xpos 400
                
                
        # 2
        if spaceship_choice_number == 2:
            show spaceship2s:
                ypos 0.3
                xpos 400
                ease 1 xpos 1000
            
            show spaceship1s:
                ypos 0.3
                xpos -200
                ease 1 xpos 400
                
              
        
        pause 1
        
        
        $ spaceship_choice_number -= 1
        $ spaceship_choice_info = True
        
        show text "[spaceship_choice_infotext[4]]" at truecenter
        #show text "{color=#8dd35f}[spaceship_choice_infotext[4]]" at truecenter
        
    jump isc_spaceship_info
    
    
    
    
    
