# Lift

label xylo_mine_lift1:
    
    call music_xylo_mine from _call_music_xylo_mine_2
    
    
    # define the name of the 4 levels of this lift, None if there is no level
    #$ liftlevel = ("- 01", None, None, "00")
    
    $ liftlevel = ("-01", None, None, "00")
    
    call liftengine from _call_liftengine_7
    
    #define what to do at level when arrived
    if liftpos == 0:
        $ startpos = 2
        call sound_door from _call_sound_door_121
        
        
        #$ darkroom = True
        
        jump xylo_mine_crossroom1
        
    if liftpos == 1:
        call sound_door_locked from _call_sound_door_locked_4
        jump xylo_mine_lift1

    if liftpos == 2:
        call sound_door_locked from _call_sound_door_locked_5
        jump xylo_mine_lift1
        
    if liftpos == 3:
        call sound_door from _call_sound_door_122
        $ startpos = 22
        $ landing = False
        jump xylo_mine
