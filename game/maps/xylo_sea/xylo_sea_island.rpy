
init:
    $ xylo_island_name = "Unknown Island"
    
    $ bonfire_wood = False
    $ bonfire_paper = False
    $ bonfire_fire = False
    $ battery_full = False
    
    $ boat_broken = "check" #(check -> takebattery -> batteryout -> no)


###########################################
label xylo_sea_island:

    
    call atmo_sea from _call_atmo_sea_4
    call atmo_nature from _call_atmo_nature_1
    

    image xylo_sea_island = imagemapsdir + "xylo_sea_island.png"
    
    scene bgcolor
    
    if planet == "xylo_sea":
        show screen notify(xylo_island_name)
    
    
    show xylo_sea_island
    show waves behind xylo_sea_island
    
    $ inventory_button = True
    
    
    
    # bonfire
    if bonfire_wood == True:
        show bonfire:
            pos (544, 280)
            alpha 0.5
        
    if bonfire_fire == True:
        if renpy.showing("smoking1") != True:
            show smoking1:
                pos (544, 280)
        if renpy.showing("smoking2") != True:
            show smoking2:
                pos (544, 280)
        if renpy.showing("smoking3") != True:
            show smoking3:
                pos (544, 280)
    
    

    
    if planet == "xylo":
        show boat:
            pos (300, 380)
            rotate 0


    # berth anim
    if planet == "xylo_sea":
        if shadow_enable == 1:
            show shadow:
                pos (130, 250)
        
        
        show boat:
            pos (-200, 400)
            rotate direction
            easein 4 pos (300, 380) rotate 0
        
        
        call sound_propulsion from _call_sound_propulsion_2
        pause 4
        call sound_door from _call_sound_door_125
        $ planet = "xylo"
        show boat:
            pos (300, 380)
            rotate 0
        

        
    
    
    
    
    # set all variables for the map (nodes and path)
    $ nodeA = (571, 102)
    $ nodeB = (579, 293)
    $ nodeC = (767, 362)
    $ nodeD = (390, 384)
    
    $ nodeAA = (497, 132)
    $ nodeBB = (538, 417)
    $ nodeCC = (400,460)
    $ nodeDD = (40,350)
    
    $ pathA = (nodeA, nodeB, nodeC, nodeD, nodeAA, (0,0), (0,0), (0,0))
    $ pathB = (nodeA, nodeB, nodeC, nodeD, nodeAA, (0,0), (0,0), (0,0))
    $ pathC = (nodeA, nodeB, nodeC, nodeD, nodeAA, (0,0), (0,0), (0,0))
    $ pathD = (nodeA, nodeB, nodeC, nodeD, nodeAA, (0,0), (0,0), (0,0))
    
    $ pathAA = (nodeA, nodeB, nodeC, nodeD, nodeAA, (0,0), (0,0), (0,0))
    $ pathBB = ((0,0), nodeB, (0,0), (0,0), (0,0), (0,0), (0,0), (0,0))
    $ pathCC = ((0,0), (0,0), nodeC, (0,0), (0,0), (0,0), (0,0), (0,0))
    $ pathDD = ((0,0), (0,0), (0,0), nodeD, (0,0), (0,0), (0,0), nodeDD)
    
    
    

label loop_xylo_sea_island:
    
    while True:

        # start "move through the map" loop
        call startpos from _call_startpos_94
        
        # do something at node?
        if exitpos == 1:
            if startpos == 1:
                if inventory_select == "wood":
                    call dialog_nobonfire from _call_dialog_nobonfire_4
                else:
                    call xylo_sea_island_info from _call_xylo_sea_island_info   
            $ startpos = 1
            
        
        if exitpos == 2: # at bonfire
            if startpos == 2:
                if bonfire_wood == False and bonfire_fire == False:
                    if inventory_select == "":
                        m "Wow...{w=1} I'm on a abandonned island! {w=3.5} {nw}"
                        m "I should find a hammock and have a nap... {w=3.5} {nw}"
                    elif inventory_select == "wood":
                        m "I think this is a good place for a bonfire.{w=3.5} {nw}"
                        
                        $ bonfire_wood = True
                        call use_item from _call_use_item_13
                        show bonfire:
                            pos (544, 280)
                            alpha 0.5
                    else:
                        call dialog_nosense from _call_dialog_nosense_79
                        

                if bonfire_wood == True:
                    if bonfire_fire == False:
                        if inventory_select == "":
                            m "My bonfire is almost ready! {w=3} {nw}"
                            
                        elif inventory_select == "newspaper":
                            m "Let's put some newspaper on the bonfire. {w=3.5} {nw}"
                            $ bonfire_paper = True
                            call use_item from _call_use_item_14
                            pause 0.5
                            call sound_paper from _call_sound_paper_1
                            
                            
                            
                            
                            
                        elif inventory_select == "lighter" and bonfire_paper == False:
                            m "The wood is too thick for this small lighter.{w=4} {nw}"
                            m "No chance to make a fire like this!{w=3.5} {nw}"

                        
                        elif inventory_select == "lighter" and bonfire_paper == True:
                            m "Let's make a fire!{w=3.5} {nw}"
                            
                            
                            $ bonfire_fire = True
                            call use_and_keep_item from _call_use_and_keep_item_46
                            call sound_ignition from _call_sound_ignition_1
                            pause 3
                            call sound_connected from _call_sound_connected_45
                            with flash
                            if renpy.showing("smoking1") != True:
                                show smoking1:
                                    pos (544, 280)
                            if renpy.showing("smoking2") != True:
                                show smoking2:
                                    pos (544, 280)
                            if renpy.showing("smoking3") != True:
                                show smoking3:
                                    pos (544, 280)
                                    
                        else:
                            call dialog_nosense from _call_dialog_nosense_80
                                    

                    # bonfire burning
                    else:
                        if inventory_select == "":
                            if xylo_sea_cabin_door_open == False:
                                m "The fire is burning. {w=3} {nw}"
                            else:
                                m "Wow, my bonfire is still burning... {w=3} {nw}"
                            
                            m "And it is really hot! {w=3} {nw}"
                            
                        elif inventory_select == "wood":
                            m "Here, more wood for the bonfire! {w=3.5} {nw}"
                            call use_item from _call_use_item_15
                            
                        elif inventory_select == "batterywet":
                            m "I don't think it is a good idea to throw this battery pack into the bonfire! {w=5} {nw}"
                            m "But at least, I could use the heat to dry it. {w=3.5} {nw}"
                            m "Let's try this. {w=2.5} {nw}"
                            call use_item from _call_use_item_16
                            show batterywet behind shadow:
                                pos (577, 252)
                                zoom 0.3
                            pause 2
                            
                            call xylo_island_waiting from _call_xylo_island_waiting_1
                            
                            hide batterywet
                            call get_item("batterydry") from _call_get_item_3
                        else:
                            call dialog_nosense from _call_dialog_nosense_81
                
                
            $ startpos = 2

            
        if exitpos == 3: # go to island2
            $ startpos = 4
            jump xylo_sea_island2

            
        if exitpos == 4: # at boat

            if startpos == 4:
                if inventory_select == "":
                    
                    if boat_broken == "no":
                        $ planet = "xylo_sea"
                        
                        $ shippos = (1400,0)
                        call sound_door from _call_sound_door_172
                        hide player
                        pause 0.5
                        
                        #call sound_propulsion
                        call sound_boat_start from _call_sound_boat_start_1
                        pause 1
                        show boat:
                            pos (300, 380)
                            easeout 4 pos (-200,400) rotate -90
                        
                        pause 4
                        $ direction = 270
                        jump surface_xylo_sea
                        
                    elif boat_broken == "check":
                        call sound_door from _call_sound_door_184
                        hide player
                        pause 0.5
                        call sound_motor_broken from _call_sound_motor_broken
                        pause 4
                        call sound_electroshock from _call_sound_electroshock_36
                        with hpunch
                        m "Oh no! The boat doesn't want to start... {w=3} {nw}"
                        m "Now I'm stuck on this unknown island! {w=3} {nw}"
                        m "Help! {w=1.5} {nw}"
                        call sound_door from _call_sound_door_185
                        show player
                        $ boat_broken = "takebattery"
                    
                    elif boat_broken == "takebattery":
                        call sound_door from _call_sound_door_186
                        hide player
                        pause 0.5
                        m "The battery seems to be empty. {w=3} {nw}"
                        m "I could try to take it out. {w=3} {nw}"
                        m "Let's go! {w=3} {nw}"
                        m ".{w=1}.{w=1}.{w=1} {nw}"
                        call sound_waterstone from _call_sound_waterstone
                        pause 1
                        call get_item("batterywet") from _call_get_item_4
                        m "Oh no! the battery pack is full of water. {w=3} {nw}"
                        m "I can't use it like this. {w=3} {nw}"
                        
                        call sound_door from _call_sound_door_187
                        show player
                        $ boat_broken = "batteryout"
                        
                    elif boat_broken == "batteryout":
                        m "I can't use the boat right now. {w=3} {nw}"
                        m "I need to fix its battery first. {w=3} {nw}"
                        
                        
                elif inventory_select == "wood":
                    call dialog_nobonfire from _call_dialog_nobonfire_5
                    
                elif inventory_select == "screwdriver":
                    if boat_broken != "no":
                        m "I need to repair the battery, not the boat. {w=3.5} {nw}"
                        $ inventory_select = ""
                    else:
                        call dialog_nosense
                    
                elif inventory_select == "batterywet":
                    m "The battery is empty... and wet. {w=3} {nw}"
                    call dialog_nosense from _call_dialog_nosense_82
                    
                elif inventory_select == "batterydry":
                    if battery_full == False:
                        m "The battery is dry but still empty... {w=3} {nw}"
                        call dialog_nosense from _call_dialog_nosense_83
                    else:
                        call use_item from _call_use_item_17
                        pause 1
                        call sound_electroshock from _call_sound_electroshock_37
                        with hpunch
                        m "Okay, it seems to work!  {w=3} {nw}"
                        m "Yay!  {w=3} {nw}"
                        $ boat_broken = "no"
                    
                
                else:
                    call dialog_nosense from _call_dialog_nosense_84
              
                    
                
            $ startpos = 4

        
        
        if exitpos == 11:
            if startpos == 11:
                if inventory_select == "":
                    m "I can see the coast at the horizon.{w=3} {nw}"
                    m "And some boats sailing around.{w=3} {nw}"
                    m "Nice view!{w=2} {nw}"
                
                elif inventory_select == "wood":
                    call dialog_nobonfire from _call_dialog_nobonfire_6
                
            $ startpos = 11   

            
        if exitpos == 22:
            $ startpos = 22

            
        if exitpos == 33:
            $ startpos = 33

            
        if exitpos == 44:
            $ startpos = 44

        







label xylo_sea_island_info:
    
    $ info_panel_symbol = "island"
    $ showtext = """
    
    
    
- Welcome to Paradise Island -


We wish y.. a plea..nt stay .. this natural island.
Enjoy ... beaches and a rom..tic ...ing at the lighthou...
In case .. emergency, 
plea.. contact ... Par..ise Island Comp..y:
Ju.. type 0034.7 in a termi..l.

Enj.. your stay!

    """
    
    call info_panel from _call_info_panel_21
    
    
    if xylo_island_name != "Paradise Island":
        
        m "This sign is really old and difficult to read.{w=3.5} {nw}"
        m "It is good to have an emergency call number... but one figure is missing!{w=4.5} {nw}"
        m "And there is no terminal here around...{w=3.5} {nw}"
        m "Anyway... {w=1.5} {nw}"
        $ xylo_island_name = "Paradise Island"
        
    call add_note("Paradise Island Company: 0034.7") from _call_add_note_16
    
    
    
    
    
    return
