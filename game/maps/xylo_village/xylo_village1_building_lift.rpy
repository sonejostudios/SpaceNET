# Lift

label xylo_village1_building_lift:

    
    
    # define the name of the 4 levels of this lift, None if there is no level
    #$ liftlevel = ("- 01", None, None, "00")
    
    $ liftlevel = ("00", "01", "02", "03")
    
    call liftengine from _call_liftengine_2
    
    
    #define what to do at level when arrived
    if liftpos == 0:
        $ startpos = 2
        call sound_door from _call_sound_door_86
        jump xylo_village1_building
        
    if liftpos == 1:
        $ startpos = 2
        call sound_door from _call_sound_door_87
        jump xylo_village1_building

    if liftpos == 2:
        $ startpos = 2
        call sound_door from _call_sound_door_88
        jump xylo_village1_building
        
    if liftpos == 3:
        $ startpos = 2
        call sound_door from _call_sound_door_89
        jump xylo_village1_building
