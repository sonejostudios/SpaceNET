# Lift

label xylo_mine_lift1:
    
    call music_xylo_mine
    
    
    # define the name of the 4 levels of this lift, None if there is no level
    #$ liftlevel = ("- 01", None, None, "00")
    
    $ liftlevel = ("-01", None, None, "00")
    
    call liftengine
    
    #define what to do at level when arrived
    if liftpos == 0:
        $ startpos = 2
        call sound_door
        
        
        #$ darkroom = True
        
        jump xylo_mine_crossroom1
        
    if liftpos == 1:
        call sound_door_locked
        jump xylo_mine_lift1

    if liftpos == 2:
        call sound_door_locked
        jump xylo_mine_lift1
        
    if liftpos == 3:
        call sound_door
        $ startpos = 22
        $ landing = False
        jump xylo_mine
