# MAPS

############################################

init:
    $ isc_spaceport_auth = False
    #$ isc_spaceport_auth = True # set to false before release

    $ isc_spaceport_usehook = False
    $ walk_on_crane_idea = False


label isc_city_spaceport:
    
    #call atmo_spaceport
    stop music fadeout 1.0
    call atmo_spaceship_station from _call_atmo_spaceship_station_4

    
    #$ isc_spaceport_usehook = False
    
    image isc_city_spaceport = imagemapsdir + "isc_city_spaceport.png"
    
    scene bgcolor
    
    call show_space from _call_show_space_13
    
    show screen notify("ISC City Spaceport")
    
    show isc_city_spaceport
    
    
    #show warningfloor:
    #    anchor (0.5,0.5)
    #    pos (540,370)
    #    rotate 90
    
    show light:
        pos (145,130)
        
    show light as light2:
        pos (355,130)
        
    show light as light3:
        pos (145,345)
        
    show light as light4:
        pos (355,345)
        
    show light as light5:
        pos (605,75)
        


    if isc_crane_pos_x == 0 and isc_crane_pos_y == 1:
        show crane behind shadow:
            anchor (0, 0.5)
            pos (640, 240)
            rotate 90
            

    # check if spaceship is landing on this map or not
    # $ landing = False
    # $ landing = True

            

    if isc_spaceship_interchange == False:
        call landing_anim from _call_landing_anim_4
        
        if isc_spaceport_auth == False:
            radio "You are not allowed to land here, go away! {w=2.5} {nw}"
            m "Okay, okay... {w=2} {nw}"
            $ landing = True
            call takeoff_anim("nomenu") from _call_takeoff_anim_5 # go to takeoff
            $ shippos = (1000,800) # set position in surface engine
            jump surface_isc
    
    
    # set all variables for the map (nodes and path)
    $ nodeA = (605,430) #(467,47)
    $ nodeB = (743,240)
    $ nodeC = (-100,-100) #(470,420)
    $ nodeD = (249,240)
    
    $ nodeAA = (400,25)
    $ nodeBB = (605,240)
    $ nodeCC = (400,460)
    $ nodeDD = (320,240)
    
    
    $ pathA = (nodeA, (0,0), (0,0), (0,0), (0,0), nodeBB, (0,0), (0,0))
    $ pathB = ((0,0), nodeB, (0,0), (0,0), (0,0), nodeBB, (0,0), nodeDD)
    $ pathC = (nodeA, (0,0), nodeC, (0,0), (0,0), nodeBB, (0,0), nodeDD)
    $ pathD = ((0,0), (0,0), nodeC, (0,0), (0,0), (0,0), (0,0), nodeDD)
    
    $ pathAA = (nodeA, (0,0), (0,0), (0,0), nodeAA, (0,0), (0,0), (0,0))
    $ pathBB = (nodeA, (0,0), (0,0), (0,0), (0,0), nodeBB, (0,0), nodeDD)
    $ pathCC = ((0,0), (0,0), nodeC, (0,0), (0,0), (0,0), nodeCC, (0,0))
    $ pathDD = ((0,0), (0,0), (0,0), (0,0), (0,0), nodeBB, (0,0), nodeDD)
    
    
    if isc_spaceship_interchange == True:
        $ pathBB = (nodeA, (0,0), (0,0), nodeD, (0,0), nodeBB, (0,0), nodeDD)
        $ pathDD = ((0,0), (0,0), (0,0), nodeD, (0,0), nodeBB, (0,0), nodeDD)
        $ pathD = ((0,0), (0,0), (0,0), nodeD, (0,0), nodeBB, (0,0), nodeDD)

            
    if isc_crane_pos_x == 0 and isc_crane_pos_y == 1:
        $ pathBB = (nodeA, nodeB, (0,0), (0,0), (0,0), nodeBB, (0,0), nodeDD)
        





label loop_isc_city_spaceport:
    
    
    while True:

        # start "move through the map" loop
        call startpos from _call_startpos_48

        # do something at node?
        if exitpos == 1:       #if at node A
            $ startpos = 3
            call sound_door from _call_sound_door_110
            jump isc_city_center 

            
        if exitpos == 2:
            if "hook" not in inventory:
                m "Are you crazy?{w=1.5} {nw}"
                show player:
                    pos nodeB
                    ease 0.5 pos nodeBB
                pause 0.5
                m "No way I'll climb there without safety equipment!{w=3} {nw}"

                $ startpos = 22
            
            else:
                $ inventory_select = "hook"
                call use_and_keep_item from _call_use_and_keep_item_20
                m "Let's go! {w=2} {nw}"
                $ startpos = 1
                jump isc_city_spaceport_gem

            
        if exitpos == 3:
            $ startpos = 3

            
        if exitpos == 4:
            if startpos == 4:
                if isc_spaceport_cash > 0:
                    m "There are some coins! {w=2} {nw}"
                    call io_cash(isc_spaceport_cash) from _call_io_cash_12
                    $ isc_spaceport_cash = 0
                else:
                    call dialog_nothing from _call_dialog_nothing_31
            $ startpos = 4

            

        #exits routing "got to map and set position for next map"
        if exitpos == 11:       #if going out at AA
            $ startpos = 11    #go to CC

            
        if exitpos == 22:
            if startpos == 22:
                if isc_crane_pos_x == 0 and isc_crane_pos_y == 1:

                    if inventory_select == "hook":
                        $ isc_spaceport_usehook = True
                        m "Let's climb on the crane!{w=2} {nw}"
                    else:
                        if walk_on_crane_idea == False:
                            m "Wow... {w=1} I could walk on the crane...{w=2} {nw}"
                            m "Dangerous idea... {w=2} {nw}"
                            $ walk_on_crane_idea = True
                        pass

                        
            
            $ startpos = 22
            

            
        if exitpos == 33:
            $ startpos = 33

            
        if exitpos == 44:
            $ startpos = 44
            
            if isc_spaceship_interchange == False:
                call sound_door from _call_sound_door_111
                call takeoff_anim("withmenu") from _call_takeoff_anim_6 # go to takeoff
                
                
                # straight to space
                if takeoftospace == True:
                    $ takeoftospace = False
                    $ space_anim = True
                    jump space

                
                # to surface
                if landing == True:
                    $ shippos = (1000,800) # set position in surface engine
                    jump surface_isc
            
            else:
                pass
            
            




# spaceport GEM
label isc_city_spaceport_gem:
    
    $ inventory_select = "spacesuit"
    call use_and_keep_item from _call_use_and_keep_item_21
    
    scene bgcolor
    
    call show_space from _call_show_space_14
    
    show crane as crane2:
        anchor (0.5, 0.5)
        pos (400, 240)
    
    show crossroomsmall at truecenter
    
    show crane:
        anchor (0.5, 0.5)
        pos (100, 240)
        rotate 90

    
    # set all variables for the map (nodes and path)
    $ nodeA = (50,240) #(467,47)
    $ nodeB = (400,240)
    $ nodeC = (-100,-100) #(470,420)
    $ nodeD = (249,240)
    
    $ nodeAA = (400,25)
    $ nodeBB = (605,240)
    $ nodeCC = (400,460)
    $ nodeDD = (320,240)
    
    
    $ pathA = (nodeA, nodeB, (0,0), (0,0), (0,0), (0,0), (0,0), (0,0))
    $ pathB = (nodeA, nodeB, (0,0), (0,0), (0,0), (0,0), (0,0), (0,0))
    $ pathC = (nodeA, (0,0), nodeC, (0,0), (0,0), nodeBB, (0,0), nodeDD)
    $ pathD = ((0,0), (0,0), nodeC, (0,0), (0,0), (0,0), (0,0), nodeDD)
    
    $ pathAA = (nodeA, (0,0), (0,0), (0,0), nodeAA, (0,0), (0,0), (0,0))
    $ pathBB = (nodeA, (0,0), (0,0), (0,0), (0,0), nodeBB, (0,0), nodeDD)
    $ pathCC = ((0,0), (0,0), nodeC, (0,0), (0,0), (0,0), nodeCC, (0,0))
    $ pathDD = ((0,0), (0,0), (0,0), (0,0), (0,0), nodeBB, (0,0), nodeDD)
    


label loop_isc_city_spaceport_gem:
    
    while True:

        # start "move through the map" loop
        call startpos from _call_startpos_49

        # do something at node?
        if exitpos == 1:       #if at node A
            $ startpos = 2
            $ landing = False
            jump isc_city_spaceport

            
        if exitpos == 2:
            if startpos == 2:
                if isc_spaceport_gem == True:
                    $ isc_spaceport_gem = False
                    call take_gem from _call_take_gem_5
                    
                else:
                    call dialog_nothing from _call_dialog_nothing_32
                    m "But the view is amazing!{w=2} {nw}"
            
            $ startpos = 2

            
        if exitpos == 3:
            $ startpos = 3

            
        if exitpos == 4:
            $ startpos = 4

            

        #exits routing "got to map and set position for next map"
        if exitpos == 11:       #if going out at AA
            $ startpos = 11    #go to CC

            
        if exitpos == 22:
            $ startpos = 22
            

            
        if exitpos == 33:
            $ startpos = 33

            
        if exitpos == 44:
            $ startpos = 44

                

