# Lift

label megaship_lift1:
    
    call music_drops from _call_music_drops_1
    
    
    # define the name of the 4 levels of this lift, None if there is no level
    #$ liftlevel = ("- 01", None, None, "00")
    
    $ liftlevel = ("-01", None, None, "00")
    
    call liftengine from _call_liftengine_5
    
    #define what to do at level when arrived
    if liftpos == 0:
        $ startpos = 33
        call sound_door from _call_sound_door_113
        jump megaship_prison
        
    if liftpos == 1:
        call sound_door_locked from _call_sound_door_locked_2
        jump megaship_lift1

    if liftpos == 2:
        call sound_door_locked from _call_sound_door_locked_3
        jump megaship_lift1
        
    if liftpos == 3:
        call sound_door from _call_sound_door_114
        $ startpos = 2
        $ multiposx = 0 
        $ multiposy = 0
        jump megaship_multimap1
