# MAPS

############################################


label isc_city_center:
    
    stop music fadeout 1.0
    call atmo_spaceship_station from _call_atmo_spaceship_station_6
    
    
    image isc_city_center = imagemapsdir + "isc_city_center.png"
    
    #scene bgcolor
    show screen notify("Industrial Space City Center")
    
    call show_space from _call_show_space_16
    
    show isc_city_center:
        pos (0,0)
    
    
    show light:
        pos (742,84)
        
    show light as light2:
        pos (742,255)
        
    
    $ landing = False
    
    
    # set all variables for the map (nodes and path)
    $ nodeA = (39, 204)
    $ nodeB = (148, 100)
    $ nodeC = (450, 44)
    $ nodeD = (585, 80)

    $ nodeAA = (630, 176)
    $ nodeBB = (537, 302)
    $ nodeCC = (355, 302)
    $ nodeDD = (140, 302)

    $ pathA = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)
    $ pathB = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)
    $ pathC = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)
    $ pathD = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)
     
    $ pathAA = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)
    $ pathBB = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)
    $ pathCC = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)
    $ pathDD = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)
    
    

label loop_isc_city_center:
    
    while True:

        # start "move through the map" loop
        call startpos from _call_startpos_61

        # do something at node?
        if exitpos == 1:
            if drunktime > 0:
                if startpos == 1:
                    m "Why going so far? {w=2.0} {nw}"
                $ startpos = 1
                jump loop_isc_city_center
            
            call sound_door from _call_sound_door_130
            $ startpos = 11
            jump isc_rail4b


        if exitpos == 2:
            if drunktime > 0:
                if startpos == 2:
                    m "I'm not in a shopping mood right now... {w=3.0} {nw}"
                $ startpos = 2
                jump loop_isc_city_center

            $ startpos = 3
            call sound_door from _call_sound_door_131
            jump isc_city_shop


            
        if exitpos == 3:
            if drunktime > 0:
                if startpos == 3:
                    m "Flying around is not a good idea right now...{w=3.0} {nw}"
                $ startpos = 3
                jump loop_isc_city_center
            
            #if startpos == 3:
            if isc_spaceport_auth == True:
                call sound_door from _call_sound_door_132
                $ startpos = 1
                jump isc_city_spaceport
            else:
                call sound_electroshock from _call_sound_electroshock_17
                with hpunch
                radio "You are not allowed to go there, go away! {w=2.5} {nw}"
                call dialog_closed from _call_dialog_closed_28
            $ startpos = 3
            
        
        if exitpos == 4:
            if startpos == 4:
                call isc_city_center_info from _call_isc_city_center_info
            $ startpos = 4
           

        #exits routing "got to map and set position for next map"
        if exitpos == 11:
            call sound_door from _call_sound_door_133
            $ startpos = 1
            jump isc_city_bar


            
        if exitpos == 22:
            if startpos == 22:
                call dialog_closed from _call_dialog_closed_29
            $ startpos = 22

            
        if exitpos == 33:
            if startpos == 33:
                call isc_city_center_info_admin from _call_isc_city_center_info_admin
            $ startpos = 33
            

            
        if exitpos == 44:
            if startpos == 44:
                call dialog_closed from _call_dialog_closed_30
            $ startpos = 44
            

            




label isc_city_center_info:
    
    $ showtext = """
- Industrial Space City Center -


Welcome to the city center of the

Industrial Space City.

Enjoy the bar, the shop, and many more!

---

To access the spaceport, 

you'll need a landing authorisation.

    """
    
    if drunktime > 0:
        $ showtext = """
- Advertisement -


Do you know the Space Adventure Game SF-IO?

You should play it!

"""

    call info_panel from _call_info_panel_12
    
    return
    
    
    
label isc_city_center_info_admin:
    
    $ showtext = """
- Industrial Space City Administration -


If you have any question concerning

the Industrial Space City,

please call the administration under 007008.

The next terminal is in the bar.

"""

    if drunktime > 0:
        $ showtext = """
- Underground News -


Some time ago, 
there was a huge knowledge network called 
IOnet.

The people were free and the life was good.
But unfortunately the time changed and
a new military governemt took the power.

They shut down the IOnet and since then,
we can't educate ourselves and we can't know the truth.

"""

    call info_panel from _call_info_panel_13
    
    if drunktime <= 0:
        call add_note("ISC administration number: 007008") from _call_add_note_10
    

    
    return

