label isc_city_bar_lift1:
    
    #"sea colony lift"
    
    # define the name of the 4 levels of this lift, None if there is no level
    #$ liftlevel = ("- 01", None, None, "00")
    # (down, middle-down, middle-up, up)
    
    $ liftlevel = ("-01", None, None, "00")
    
    while True:
        call liftengine
        
        #define what to do at level when arrived
        
        #down
        if liftpos == 0:
            #call dialog_closed
            $ startpos = 4
            call sound_door
            jump isc_bar_lift_room
            
            
        #middle-down
        if liftpos == 1:
            call dialog_closed

        #middle-up
        if liftpos == 2:
            call dialog_closed
            
        #up
        if liftpos == 3:
            $ startpos = 11
            call sound_door
            jump isc_city_bar_toilets

    
    
