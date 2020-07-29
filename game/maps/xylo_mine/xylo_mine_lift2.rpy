# Lift

label xylo_mine_lift2:
    
    # define the name of the 4 levels of this lift, None if there is no level
    #$ liftlevel = ("- 01", None, None, "00")
    
    $ liftlevel = ("-01", None, None, "00")
    
    call liftengine from _call_liftengine_6
    
    #define what to do at level when arrived
    if liftpos == 0:
        #call dialog_closed
        call sound_door from _call_sound_door_115
        $ startpos = 1
        jump xylo_minitrain
        
    if liftpos == 1:
        jump xylo_mine_lift2

    if liftpos == 2:
        jump xylo_mine_lift2
        
    if liftpos == 3:
        call sound_door from _call_sound_door_116
        $ startpos = 4
        jump xylo_mine_crossroom1
