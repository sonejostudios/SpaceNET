# MAPS

############################################


label isc_city_center:
    
    stop music fadeout 1.0
    call atmo_spaceship_station
    
    
    image isc_city_center = imagemapsdir + "isc_city_center.png"
    
    #scene bgcolor
    show screen notify("Industrial Space City Center")
    
    call show_space
    
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
    
    

    # coming from trip
    #if triptime == True:
    #    $ triptime = False
    #    $ startpos = 2
    #    call sound_scan
    #    #with Dissolve(0.5)
    #    with pixellate



label loop_isc_city_center:
    
    while True:

        # start "move through the map" loop
        call startpos

        # do something at node?
        if exitpos == 1:
            call sound_door
            $ startpos = 11
            jump isc_rail4b


        if exitpos == 2:
            if startpos == 2:
                #m "this is the shop.{w=1} {nw}"
                $ startpos = 3
                call sound_door
                jump isc_city_shop
            $ startpos = 2

            
        if exitpos == 3:
            #if startpos == 3:
            if isc_spaceport_auth == True:
                call sound_door
                $ startpos = 1
                jump isc_city_spaceport
            else:
                call sound_electroshock
                with hpunch
                radio "You are not allowed to go there, go away! {w=2.5} {nw}"
                call dialog_closed
            $ startpos = 3
            
        
        if exitpos == 4:
            if startpos == 4:
                call isc_city_center_info
            $ startpos = 4
           

        #exits routing "got to map and set position for next map"
        if exitpos == 11:
            call sound_door
            $ startpos = 1
            jump isc_city_bar


            
        if exitpos == 22:
            if startpos == 22:
                call dialog_closed
            $ startpos = 22

            
        if exitpos == 33:
            if startpos == 33:
                call isc_city_center_info_admin
            $ startpos = 33
            

            
        if exitpos == 44:
            if startpos == 44:
                call dialog_closed
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

    call info_panel
    
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
This is horrible!

"""

    call info_panel
    
    if drunktime <= 0:
        call add_note("ISC administration number: 007008")
    

    
    return

