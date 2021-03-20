# MAPS

############################################

# go level -2, get key
# go level -1, use key with lift control
# send lift to -2
# go to lift, lift cabin is not there
# use rope and come to next secret room
# in this room find button "unlock secret level -3"
# go back to room -2
# call lift
# go to level -3

init:
    $ xylo_sea_bunker_liftroom_lock1 = False
    $ xylo_sea_bunker_liftroom_lock3 = True


 
# bunker map

label xylo_sea_bunker_liftroom:
    $ pnc_nodes_visible = True
    
    stop music
    call atmo_base from _call_atmo_base_3
    
    image xylo_sea_bunker_liftroom = imagemapsdir + "crossroom.png"
    
    scene bgcolor
    show xylo_sea_bunker_liftroom at truecenter
    

    show screen notify("Lift maintenance room")
    
    
    #doors (comment to disable)
    #show doorh as doorA:
    #    pos (400, 55)
    show doorv as doorB:
        pos (587, 240)
    #show doorh as doorC:
    #    pos (400, 427)
    #show doorv as doorD:
    #    pos (215, 240)
    
    show warningfloor:
        rotate 90
        anchor (0.5,0.5)
        pos (500,240)
        
    
    show spacenetcomp:
        anchor (0.5,0.5)
        pos (360,310)
        crop (0, 80, 300, 300)
    
    #show buttonscreen:
    #    pos (300,55)

    
    
    # set all variables for the map (nodes and path)
    $ nodeA = (400, 75)
    $ nodeB = (565, 240)
    $ nodeC = (300, 340)
    $ nodeD = (300, 240)
    

    $ nodeAA = (400, 240)
    $ nodeBB = (-100, -100)
    $ nodeCC = (-100, -100)
    $ nodeDD = (-100, -100)

    $ pathA = (nodeA, nodeB, (0, 0), nodeD, nodeAA, (0, 0), (0, 0), (0, 0))
    $ pathB = ((0, 0), nodeB, nodeC, nodeD, nodeAA, (0, 0), (0, 0), (0, 0))
    $ pathC = ((0, 0), nodeB, nodeC, nodeD, nodeAA, (0, 0), (0, 0), (0, 0))
    $ pathD = ((0, 0), nodeB, nodeC, nodeD, nodeAA, (0, 0), (0, 0), (0, 0))
     
    $ pathAA = ((0, 0), nodeB, nodeC, nodeD, nodeAA, (0, 0), (0, 0), (0, 0))
    $ pathBB = (nodeA, nodeB, (0, 0), nodeD, nodeAA, nodeBB, nodeCC, nodeDD)
    $ pathCC = (nodeA, nodeB, (0, 0), nodeD, nodeAA, nodeBB, nodeCC, nodeDD)
    $ pathDD = (nodeA, nodeB, (0, 0), nodeD, nodeAA, nodeBB, nodeCC, nodeDD)
    
    


label loop_xylo_sea_bunker_liftroom:
    
    while True:

        # start "move through the map" loop
        call startpos from _call_startpos_8

        # do something at node?
        if exitpos == 1:
            $ startpos = 1
            
        if exitpos == 2:
            
            if xylo_sea_bunker_liftroom_lock1 == False:
                $ startpos = 33
                call sound_door from _call_sound_door_21
                jump xylo_sea_bunker_liftmap
            else:
                $ startpos = 2
                call dialog_closed from _call_dialog_closed_1

            
        if exitpos == 3: # software disk
            if startpos == 3:
                if "spacenet" not in inventory:
                    m "There is a computer disk on the desk. {w=2.5} {nw}"
                    m "It seems to be empty. {w=2} {nw}"
                    call take_item("spacenet") from _call_take_item_2
                else:
                    call dialog_nothing from _call_dialog_nothing_10
                    
            $ startpos = 3

            
        if exitpos == 4:
            if startpos == 4:
                m "This computer is really old, but it is still working! {w=3} {nw}"
                jump xylo_sea_bunker_liftroom_computer
            $ startpos = 4


        #exits routing "got to map and set position for next map"
        if exitpos == 11:
            if startpos == 11:
                m "This looks like a maintenance room. {w=2} {nw}"
            $ startpos = 11     
 
            
        if exitpos == 22:
            $ startpos = 22

            
        if exitpos == 33:
            $ startpos = 33

            
        if exitpos == 44:
            $ startpos = 44



label xylo_sea_bunker_liftroom_computer:
    $ pnc_nodes_visible = False
    
    scene terminal at topleft
    call sound_beep from _call_sound_beep_1
    
    $ unlock_text1 = "unlocked"
    $ unlock_text3 = "unlocked"
    
    if xylo_sea_bunker_liftroom_lock1 == True:
        $ unlock_text1 = "locked"
    if xylo_sea_bunker_liftroom_lock3 == True:
        $ unlock_text3 = "locked"
    
    $ showtext = """
    Welcome to 
    A.R.K. Bunker Lift Control
    [ascii_line]
    
    Level  00 : unlocked
    
    Level -01 : [unlock_text1] 
    
    Level -02 : unlocked
    
    Level -03 : [unlock_text3] 
    """
    
    show text Text(showtext,text_align=termtext_align) at termtextpos
    
    menu:
        "Lock 00":
            m "If I do that, I can't go out of the bunker anymore! {w=3.5} {nw}"
            call dialog_nosense from _call_dialog_nosense_3
            
        "Lock -01" if xylo_sea_bunker_liftroom_lock1 == False:
            m "Why should I actally do that? {w=2} {nw}"
            m "Okay... let's have a try. {w=2} {nw}"
            $ xylo_sea_bunker_liftroom_lock1 = True
            #call server_progressbar
            #call sound_scan
            #with flash

            
        "Unlock -01" if xylo_sea_bunker_liftroom_lock1 == True:
            $ xylo_sea_bunker_liftroom_lock1 = False

            
        "Lock -02":
            call dialog_nosense from _call_dialog_nosense_4
            
        "Lock -03" if xylo_sea_bunker_liftroom_lock3 == False:
            $ xylo_sea_bunker_liftroom_lock3 = True

            
        "Unlock -03" if xylo_sea_bunker_liftroom_lock3 == True:
            m "This looks like there is a secret level in this bunker... {w=3.5} {nw}"
            m "Interesting! {w=1} {nw}"
            $ xylo_sea_bunker_liftroom_lock3 = False

            
        "Exit":
            jump xylo_sea_bunker_liftroom
            
    #pause 2
            
    jump xylo_sea_bunker_liftroom_computer
