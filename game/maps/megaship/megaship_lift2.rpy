# Lift

label megaship_lift2:
    
    call music_drops from _call_music_drops
    
    
    # define the name of the 4 levels of this lift, None if there is no level
    #$ liftlevel = ("- 01", None, None, "00")
    
    $ liftlevel = ("-01", "00", "01", "02")
    
    call liftengine from _call_liftengine_1
    
    #define what to do at level when arrived
    if liftpos == 0:
        $ startpos = 1
        #m "...that looks like a spaceport ! {w=2.5} {nw}"
        call sound_door from _call_sound_door_72
        jump megaship_spaceport
        
    if liftpos == 1:
        call sound_door from _call_sound_door_73
        $ startpos = 2
        $ multiposx = 1 
        $ multiposy = 1
        jump megaship_multimap1

    if liftpos == 2:
        $ startpos = 1
        call sound_door from _call_sound_door_74
        jump megaship_store
        
    if liftpos == 3:
        m "There are lots of people out there...{w=2.0} {nw}"
        m "Too many for my taste. {w=2.0} {nw}"
        #call sound_door_locked
        jump megaship_lift2
