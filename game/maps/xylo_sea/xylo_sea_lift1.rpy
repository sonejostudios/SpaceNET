label xylo_lift1:
    
    
    
    #"sea colony lift"
    
    # define the name of the 4 levels of this lift, None if there is no level
    #$ liftlevel = ("- 01", None, None, "00")
    
    $ liftlevel = ("00", "01", "02", "03")
    
    call liftengine from _call_liftengine_4
    
    #define what to do at level when arrived
    if liftpos == 0:
        $ startpos = 44
        call sound_door from _call_sound_door_108
        jump xylo_map1
        
    if liftpos == 1:
        call dialog_closed from _call_dialog_closed_20
        jump xylo_lift1

    if liftpos == 2:
        call dialog_closed from _call_dialog_closed_21
        jump xylo_lift1
        
    if liftpos == 3:
        $ startpos = 22
        $ landing = False
        call sound_door from _call_sound_door_109
        jump xylo_map6spaceport
