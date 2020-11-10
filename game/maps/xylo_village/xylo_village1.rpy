# MAPS

init:
    $ gov_joke = False


############################################

label xylo_village1:
    
    stop music
    
    call atmo_village from _call_atmo_village_2
    
    image xylo_village1 = imagemapsdir + "xylo_village1.png"
    
    scene bgcolor
    show screen notify("xylo's colony village")
    
    image waves3 = SnowBlossom("images/wave.png", count=400, border=50, xspeed=(0), yspeed=(10), start=0, fast=True, horizontal=False)
    show waves3
    
    show xylo_village1
    
    

    # check if spaceship is landing on this map or not
    # $ landing = False
    # $ landing = True
    #call landing_anim
    
    
    # set all variables for the map (nodes and path)
    $ nodeA = (180, 75)
    $ nodeB = (244, 239)
    $ nodeC = (132, 322)
    $ nodeD = (370, 130)

    $ nodeAA = (80, 104)
    $ nodeBB = (660, 240)
    $ nodeCC = (737, 157)
    $ nodeDD = (772, 240)

    $ pathA = (nodeA, nodeB, nodeC, nodeD, nodeAA, (0, 0), (0, 0), (0, 0))
    $ pathB = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, (0, 0), nodeDD)
    $ pathC = (nodeA, nodeB, nodeC, nodeD, nodeAA, (0, 0), (0, 0), (0, 0))
    $ pathD = (nodeA, nodeB, nodeC, nodeD, nodeAA, (0, 0), (0, 0), (0, 0))
     
    $ pathAA = (nodeA, nodeB, nodeC, nodeD, nodeAA, (0, 0), (0, 0), (0, 0))
    $ pathBB = ((0, 0), nodeB, (0, 0), (0, 0), (0, 0), nodeBB, nodeCC, nodeDD)
    $ pathCC = ((0, 0), (0, 0), (0, 0), (0, 0), (0, 0), nodeBB, nodeCC, nodeDD)
    $ pathDD = ((0, 0), nodeB, (0, 0), (0, 0), (0, 0), nodeBB, nodeCC, nodeDD)


label loop_xylo_village1:
    
    while True:

        # start "move through the map" loop
        call startpos from _call_startpos_75

        # do something at node?
        if exitpos == 1:       #if at node A
            $ startpos = 22    # stay in A
            call sound_door from _call_sound_door_159
            jump xylo_spaceport_hall        # map loop to jump to
            
        if exitpos == 2:
            if startpos == 2:
                m "I'm in the middle of the village. {w=2.0} {nw}"
                m "What a beautiful place! {w=2.0} {nw}"
            $ startpos = 2
            
            
        if exitpos == 3: 
            if startpos == 3:
                call dialog_closed from _call_dialog_closed_41
                
            $ startpos = 3
            
        if exitpos == 4:
            if startpos == 4:
                call dialog_closed from _call_dialog_closed_42

            $ startpos = 4
            

        #exits routing "got to map and set position for next map"
        if exitpos == 11:
            if startpos == 11:    #if going out at AA
                call xylo_village1_info from _call_xylo_village1_info
            
            $ startpos = 11     #go to CC

            
        if exitpos == 22:
            if startpos == 22:
                m "Nice river. {w=1.0} {nw}"
                if xylo_village1_cash > 0:
                    m "There is something on the floor... {w=2} {nw}"
                    m "This is one coin! {w=2} {nw}"
                    m "I'm rich! {w=1.5} {nw}"
                    call io_cash(xylo_village1_cash) from _call_io_cash_20
                    $ xylo_village1_cash = 0
                    
            $ startpos = 22

            
        if exitpos == 33:
            $ startpos = 3
            call sound_door from _call_sound_door_160
            $ liftpos = 0
            jump xylo_village1_building

        
        if exitpos == 44:
            $ startpos = 1
            jump xylo_village2




label xylo_village1_info:
    
    $ info_panel_symbol = "" #"exit"
    
    $ showtext = """
- Xylo's Colony Village -


Welcome to xylo's colony village!
We hope you'll have fun there.

Enjoy!

"""


    if drunktime > 0:
        $ gov_joke = True
        $ showtext = """
- Best Joke Ever -


What is the difference between the government
and A.R.K Corporation?

Answer:
There is no difference!

"""


    call info_panel from _call_info_panel_17
    
    return
