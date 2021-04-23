# MAPS

############################################

init:
    $ asteroid_magnet_at_box = True


label asteroid_spacenet:
    
    stop music
    #call atmo_spaceship
    call atmo_base from _call_atmo_base_4
    #call atmo_reactor
    
    scene bgcolor
    
    image asteroid_spacenet = imagemapsdir + "crossroom.png"
    show asteroid_spacenet at truecenter
    
    
    show warningfloor:
        anchor (0.5,0.5)
        pos (400, 163)
        rotate 0
    
    
    image spacenetcomp:
        "images/spacenetcomp.png"
        anchor (0.5,0.5)
    
    show spacenetcomp:
        anchor (0.5,0.5)
        pos (440,240)
        rotate 90
        rotate_pad True
        xzoom -1

        

    
    
    #show terminalmap:
    #    anchor (0.5,0.5)
    #    pos (233, 152)
        
        
        
    show box:
        pos (259, 98)
        
    show buttonscreen:
        pos (216, 276)
        rotate 90
        

    show screen notify("Abandonned base")
    
    #doors (comment to disable)
    show doorh as doorA:
        pos (400, 55)
    #show doorv as doorB:
    #    pos (587, 240)
    #show doorh as doorC:
    #    pos (400, 427)
    #show doorv as doorD:
    #    pos (215, 240)
    
    
    

    
    
    
    # set all variables for the map (nodes and path)
    $ nodeA = (400, 75)
    $ nodeB = (238, 276)
    $ nodeC = (400, 337)
    $ nodeD = (490, 261)
    
    $ nodeAA = (369, 211)
    $ nodeBB = (260, 162)
    
    $ nodeCC = (490, 180)
    $ nodeDD = (-100, -100)

    $ pathA = (nodeA, nodeB, nodeC, nodeD, nodeAA, (0, 0), (0, 0), (0, 0))
    $ pathB = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, (0, 0), (0, 0))
    $ pathC = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, (0, 0), (0, 0))
    $ pathD = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, (0, 0), (0, 0))
     
    $ pathAA = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, (0, 0), (0, 0))
    
    $ pathBB = ((0, 0), nodeB, nodeC, nodeD, nodeAA, nodeBB, (0, 0), (0, 0))
    $ pathCC = ((0, 0), (0, 0), nodeC, nodeD, nodeAA, nodeBB, nodeCC, (0, 0))
    $ pathDD = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)


label loop_asteroid_spacenet:
    
    while True:
        # spacenet sender
        if "asteroid_base" in spacenetnodes:
            show spacenetsender:
                pos (464, 390)
                #pos (329, 400)
                

        # start "move through the map" loop
        call startpos from _call_startpos_88

        # do something at node?
        if exitpos == 1:
            $ startpos = 11
            $ liftpos = 0
            call sound_door from _call_sound_door_183
            jump asteroid_lift1
            
        if exitpos == 2:
            if startpos == 2:
                call asteroid_spacenet_info from _call_asteroid_spacenet_info
            $ startpos = 2
            
        if exitpos == 3:
            if startpos == 3:
                jump asteroid_spacenet_spacenet_comp
                
                
            $ startpos = 3
            
        if exitpos == 4:
            if startpos == 4:
                m "This computer is off. {w=2} {nw}"
                if asteroid2_cash > 0:
                    m "Hey, there is some money on the desk! {w=3.0} {nw}"
                    call io_cash(asteroid2_cash) from _call_io_cash_25
                    $ asteroid2_cash = 0
            $ startpos = 4

            

        #exits routing "got to map and set position for next map"
        if exitpos == 11:
            if startpos == 11:
                m "This room is full of computers. {w=2} {nw}"
            $ startpos = 11      
            
        if exitpos == 22:
            #"asteroid_magnet_at_box [asteroid_magnet_at_box]"
            
            if "magnet" in inventory or "magnetcord" in inventory or module_in_orbit == False:
                $ asteroid_magnet_at_box = False
            
            if startpos == 22:
                if inventory_select == "":
                    m "This is a big metal box. {w=2} {nw}"
                    m "What is inside?{w=2} {nw}"
                    m "Maybe some weird experiments?{w=2.5} {nw}"
                    m "I don't know, and I will probably never know.{w=3.5} {nw}"
                
                
                    if asteroid_magnet_at_box == True:
                        call use_and_keep_item from _call_use_and_keep_item_41
                        m "At least, there is a magnet on it.{w=3.5} {nw}"
                        call take_item("magnet") from _call_take_item_22
                        
                        if inventory_notify == "magnet":
                            $ asteroid_magnet_at_box = False
                        
                else:
                    call dialog_nosense from _call_dialog_nosense_37
                

            $ startpos = 22

            
        if exitpos == 33:
            $ startpos = 33
            
        if exitpos == 44:
            $ startpos = 44






label asteroid_spacenet_spacenet_comp:
    show terminal at topleft
    if shadow_enable == 1:
        show shadow:
            pos (270, 240)
    call sound_beep from _call_sound_beep_76 
    
    call spacenet_comp("asteroid_base") from _call_spacenet_comp_4 # install spacenet
    
    jump asteroid_spacenet
    

    

label asteroid_spacenet_info:

    $ info_panel_symbol = ""
    $ showtext = """
- Asteroid Scientific Research Base -


This is a scientific research base.
The main goal is to study the asteroid field,
but also the stars around.

Two solar panels are providing electricity for the base.
They need to be maintened on a regular basis.


    """

    call info_panel from _call_info_panel_15

    return
