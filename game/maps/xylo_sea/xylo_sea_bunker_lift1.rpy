label xylo_sea_bunker_lift1:
    
    call music_cargo from _call_music_cargo_3
    
    #"sea colony lift"
    
    # define the name of the 4 levels of this lift, None if there is no level
    #$ liftlevel = ("- 01", None, None, "00")
    
    $ liftlevel = (None, "-02", "-01", "00")
    
    if xylo_sea_bunker_liftroom_lock3 == False:
        $ liftlevel = ("-03", "-02", "-01", "00")
    
    call liftengine from _call_liftengine_8
    
    
    # force liftpos = lift_level
    if liftpos == 0:
        $ xylo_bunker_lift_level = 3
    if liftpos == 1:
        $ xylo_bunker_lift_level = 2
    if liftpos == 2:
        $ xylo_bunker_lift_level = 1
    if liftpos == 3:
        $ xylo_bunker_lift_level = 0
    
    
    
    #define what to do at level when arrived
    if liftpos == 0:
        call sound_door from _call_sound_door_134
        $ startpos = 1
        jump xylo_sea_bunker_spacenet
        
    if liftpos == 1:
        call sound_door from _call_sound_door_135
        $ startpos = 1
        jump xylo_sea_bunker

    if liftpos == 2:
        call sound_door from _call_sound_door_136
        $ startpos = 1
        jump xylo_sea_bunker
        
    if liftpos == 3:
        $ startpos = 11
        $ landing = False
        $ guardpos = 1
        call sound_door from _call_sound_door_137
        jump xylo_map7
