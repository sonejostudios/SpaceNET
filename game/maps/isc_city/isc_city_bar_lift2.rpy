label isc_city_bar_lift2:
    
    #"sea colony lift"
    
    # define the name of the 4 levels of this lift, None if there is no level
    #$ liftlevel = ("- 01", None, None, "00")
    # (down, middle-down, middle-up, up)
    
    $ liftlevel = ("-02", None, None, "-01")
    
    while True:
        call liftengine from _call_liftengine_9
        
        #define what to do at level when arrived
        
        #down
        if liftpos == 0:
            call sound_door from _call_sound_door_161
            $ startpos = 1
            jump isc_city_gateway
            
        #middle-down
        if liftpos == 1:
            call dialog_closed from _call_dialog_closed_43

        #middle-up
        if liftpos == 2:
            call dialog_closed from _call_dialog_closed_44
            
        #up
        if liftpos == 3:
            $ startpos = 2
            call sound_door from _call_sound_door_162
            jump isc_bar_lift_room
