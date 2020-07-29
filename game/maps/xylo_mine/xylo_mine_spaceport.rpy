# MAPS

# xylo mine spaceport

############################################
label xylo_mine:
    
    stop music fadeout 1.0
    call atmo_wind from _call_atmo_wind
    
    
    image xylo_mine = imagemapsdir + "spaceportlift.png"
    
    scene xylo_mine
    show screen notify("abandonned mine")
    
    show bgcolor behind xylo_mine
    
    
    
    show warningfloor:
        anchor (0.5,0.5)
        pos (570,240)
        rotate 90
    
    show light:
        pos (145,130)
        
    show light as light2:
        pos (355,130)
        
    show light as light3:
        pos (145,345)
        
    show light as light4:
        pos (355,345)
        
    hide tube
    show tube:
        pos (523,-430)
        rotate 90
        
    
    show buttonscreen:
        pos (510,445)
        
    show buttonscreen as bs2:
        pos (677,315)
        rotate 90
        

    # check if spaceship is landing on this map or not
    # $ landing = False
    # $ landing = True
    call landing_anim from _call_landing_anim_2
    
    
    # set all variables for the map (nodes and path)
    $ nodeA = (522,87) 
    $ nodeB = (470,240)
    $ nodeC = (512,420)
    $ nodeD = (650,315)
    
    $ nodeAA = (400,25)
    $ nodeBB = (680,240)
    $ nodeCC = (400,460)
    $ nodeDD = (320,235)
    
    $ pathA = (nodeA, nodeB, nodeC, nodeD, (0,0), nodeBB, (0,0), nodeDD)
    $ pathB = (nodeA, nodeB, nodeC, nodeD, (0,0), nodeBB, (0,0), nodeDD)
    $ pathC = (nodeA, nodeB, nodeC, nodeD, (0,0), nodeBB, (0,0), nodeDD)
    $ pathD = (nodeA, nodeB, nodeC, nodeD, (0,0), nodeBB, (0,0), nodeDD)
    
    $ pathAA = (nodeA, (0,0), nodeC, nodeD, nodeAA, (0,0), (0,0), (0,0))
    $ pathBB = (nodeA, nodeB, nodeC, nodeD, (0,0), nodeBB, (0,0), nodeDD)
    $ pathCC = ((0,0), (0,0), nodeC, nodeD, (0,0), (0,0), nodeCC, (0,0))
    $ pathDD = (nodeA, nodeB, nodeC, nodeD, (0,0), nodeBB, (0,0), nodeDD)
    
    
    #if playertype == "minidroid":
    #    show playercross:
    #        pos nodeA
            
    # anim minidroid back
    if startpos == 1:
        show playercross:
            pos nodeA
        
        show minidroid:
            pos (522,-20)
            linear 1 pos nodeA
        pause 1
        $ playertype = "player"
        hide minidroid
        hide playercross
    
    
    


label loop_xylo_mine:

    while True:
        # start "move through the map" loop
        call startpos from _call_startpos_31

        # do something at node?
        if exitpos == 1:       #if at node A
            if startpos == 1:
                #$ startpos = 3
                #jump xylo_mine_tube
                
                if inventory_select == "":
                    m "This is an aeration tube.{w=2} {nw}"
                    call dialog_notfitting from _call_dialog_notfitting_1
                
                if inventory_select != "minidroid" and inventory_select != "":
                    call dialog_nosense from _call_dialog_nosense_8
                
                if inventory_select == "minidroid":
                    
                    m "I can use the minidroid... let's go! {w=2.5} {nw}"
                    call use_and_keep_item from _call_use_and_keep_item_14
                    call sound_connected from _call_sound_connected_24
                    with flash
                    show minidroid:
                        pos nodeA
                        linear 1 ypos 0
                    pause 1
                    $ startpos = 3
                    jump xylo_mine_tube
                    
                
            $ startpos = 1     # stay in A
            

            
        if exitpos == 2:
            if startpos == 2:
                if xylo_mine_spaceport > 0:
                    m "There are [xylo_mine_spaceport]c on the floor... {w=2.5} {nw}"
                    call io_cash(xylo_mine_spaceport) from _call_io_cash_9
                    m "Nice! {w=1.5} {nw}"
                    $ xylo_mine_spaceport = 0
                else:
                    call dialog_nothing
            $ startpos = 2

            
        if exitpos == 3:
            if startpos == 3:
                call xylo_mine_spaceport_isc from _call_xylo_mine_spaceport_isc # advertisement isc
            $ startpos = 3


            
        if exitpos == 4:
            if startpos == 4:
                call xylo_mine_spaceport_info from _call_xylo_mine_spaceport_info # info
            $ startpos = 4

            

        #exits routing "got to map and set position for next map"
        if exitpos == 11:       #if going out at AA
            $ startpos = 11    #go to CC

            
        if exitpos == 22:
            $ startpos = 22
            
            $liftpos = 3
            call sound_door from _call_sound_door_78
            jump xylo_mine_lift1 # go to lift
            
        if exitpos == 33:
            $ startpos = 33

            
        if exitpos == 44:
            $ startpos = 44
            call sound_door from _call_sound_door_79
            call takeoff_anim("withmenu") from _call_takeoff_anim_3 # go to takeoff
            
            
            # straight to space
            if takeoftospace == True:
                $ takeoftospace = False
                $ space_anim = True
                jump space

            
            # to surface
            if landing == True:
                $ shippos = (200,400) # set position in surface engine
                jump surface_xylo
                






label xylo_mine_spaceport_info:
    
    $ info_panel_symbol = "quake"
    $ showtext = """
    
    
    
Because of seismic activity, this mine is
abandonned and absolutely not safe.
Do not enter!

---

This mine is a property of

- General Mining Corporation -
- A.R.K. Corporation -
    """
    
    
    call info_panel from _call_info_panel_5 # in animations

    return
    
   
   
    
label xylo_mine_spaceport_isc:
    
    $ info_panel_symbol = ""
    $ showtext = """
Advertisement:

Are you looking for a new spaceship?
A better - faster - stronger - bigger one?
Just go to Spaceship Interchange at
the Industrial Space City.

Just 'locate isc' in a terminal!
    """
    
    
    
    call info_panel from _call_info_panel_6 # in animations
    call add_note("terminal: locate isc") from _call_add_note_5

    return
