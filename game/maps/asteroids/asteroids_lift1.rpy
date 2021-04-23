label asteroid_lift1:
    
    
    # define the name of the 4 levels of this lift, None if there is no level
    #$ liftlevel = ("- 01", None, None, "00")
    # (down, middle-down, middle-up, up)
    
    $ liftlevel = ("-01", None, None, "00")
    
    while True:
        call liftengine from _call_liftengine_10 
        
        #define what to do at level when arrived
        
        #down
        if liftpos == 0:
            #call dialog_closed
            $ startpos = 1
            call sound_door from _call_sound_door_181 
            jump asteroid_spacenet
            
            
        #middle-down
        if liftpos == 1:
            call dialog_closed from _call_dialog_closed_52

        #middle-up
        if liftpos == 2:
            call dialog_closed from _call_dialog_closed_53 
            
        #up
        if liftpos == 3:
            $ startpos = 11
            call sound_door from _call_sound_door_182
            jump asteroid2_down

    
    
