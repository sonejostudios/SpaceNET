# isc wagon anim


label isc_wagon_anim_toright:
    
    $ pnc_nodes_visible = False
    
    stop music fadeout 1.0
    call atmo_spaceship_station from _call_atmo_spaceship_station
    
    call show_space from _call_show_space
    

        
    show tube:
        pos (400,206)
        
    show tube as tube2:
        pos (400,276)
    
    show rails2:
        pos (400,240)
        linear 0.1 pos (370,240)
        repeat
        
    show isctrain:
        anchor (0.35,0.5)
        pos (-100,240)
        linear 6 pos (900,240)
        
        
    if shadow_enable == 1:
        show shadow:
            pos (0, 240)
            linear 6 pos (800, 240)
            
    pause 6
    
    $ landing = False
    
    
    $ isctrain_anim = True
    
    $ pnc_nodes_visible = True
    jump isc_rail1
    


label isc_wagon_anim_toleft:
    $ pnc_nodes_visible = False
    
    stop music fadeout 1.0
    call atmo_spaceship_station from _call_atmo_spaceship_station_1
    
    call show_space from _call_show_space_1
    
        
    show tube:
        pos (400,206)
        
    show tube as tube2:
        pos (400,276)
    
    show rails2:
        pos (400,240)
        linear 0.1 pos (430,240)
        repeat
        
    show isctrain:
        rotate 180
        anchor (0.35,0.5)
        pos (900,240)
        linear 6 pos (-100,240)
        
        
    if shadow_enable == 1:
        show shadow:
            pos (800, 240)
            linear 6 pos (0, 240)
            
    pause 6
    
    $ landing = False
    
    $ startpos = 22
    $ isctrain_anim = True
    
    $ pnc_nodes_visible = True
    jump isc_interchange
