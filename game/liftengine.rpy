

label liftengine:
    $ pnc_nodes_visible = False
    
    #stop atmo fadeout 1.0
    
    #stop music
    
    call atmo_spaceship_hum from _call_atmo_spaceship_hum_3
    
    #call music_lift
    
    scene bgcolor
    
    image liftcabin = "images/lift/liftcabin.png"
    image lift = "images/lift/lift.png"
    
    show lift:
        xpos 0.5
        ypos 0.5
        xanchor 0.5
    
    
    if liftpos == 0:
        show screen notify("Level [liftlevel[0]]") 
        show lift:
            yanchor 938
            
    if liftpos == 1:
        show screen notify("Level [liftlevel[1]]") 
        show lift:
            yanchor 600
            
    if liftpos == 2:
        show screen notify("Level [liftlevel[2]]") 
        show lift:
            yanchor 300
            
    if liftpos == 3:
        show screen notify("Level [liftlevel[3]]") 
        show lift:
            yanchor 56
    
    
    show liftcabin at truecenter
    
    show player:
        pos (400, 258)

    
    if shadow_enable == 1:
        show shadow:
            pos (400, 258)
            
            
    # alarm
    call alarm_check from _call_alarm_check_10
    

    
    menu:
        "[liftlevel[3]]" if liftpos != 3 and liftlevel[3] != None:
            $ liftpos = 3
            show lift:
                ease 3 yanchor 56
            pass
            
        "[liftlevel[3]]\nExit" if liftpos == 3 :
            #call sound_door
            #stop music
            $ pnc_nodes_visible = True
            return
        
        
        "[liftlevel[2]]" if liftpos != 2 and liftlevel[2] != None:
            $ liftpos = 2
            show lift:
                ease 3 yanchor 300
            pass
            
        "[liftlevel[2]]\nExit" if liftpos == 2 :
            #call sound_door
            #stop music
            $ pnc_nodes_visible = True
            return
            
        
        "[liftlevel[1]]" if liftpos != 1 and liftlevel[1] != None:
            $ liftpos = 1
            show lift:
                ease 3 yanchor 600
            pass
            
        "[liftlevel[1]]\nExit" if liftpos == 1 :
            #call sound_door
            #stop music
            $ pnc_nodes_visible = True
            return
        
        
        "[liftlevel[0]]" if liftpos != 0 and liftlevel[0] != None:
            $ liftpos = 0
            show lift:
                ease 3 yanchor 938 
            pass
            
        "[liftlevel[0]]\nExit" if liftpos == 0 :
            #call sound_door
            #stop music
            $ pnc_nodes_visible = True
            return

    call sound_lift from _call_sound_lift_3       
    pause 3   # animation time
    
    jump liftengine
    
    
    

    

    
