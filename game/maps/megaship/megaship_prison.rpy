# MAPS

############################################

init:
    $ megaship_prisondoor_button = False


screen megaship_buttons1() zorder -999:
    #add "#112119"
    
    on "show" action SetVariable("pnc_nodes_visible", False)
    on "hide" action SetVariable("pnc_nodes_visible", True)

    imagebutton at topleft: 
        idle "images/maps/bg.png" 
        action [Hide("megaship_buttons1")]
        
            
    
    add "inventory/inventory.png"
    
    hbox xalign 0.5 yalign 0.5:
        vbox xalign 0.5:
            label "main door" at center
            null height 10
            imagebutton: 
                auto "images/buttonbig_%s.png"
                action ToggleVariable("megaship_prisondoor_button"), Play("sound", "sounds/collect.ogg") at center
            
        #null width 100
        
        #vbox xalign 0.5:
        #    label "exit" at center
        #    null height 10
        #    imagebutton auto "images/buttonbig_%s.png" action Hide("megaship_buttons1"), Play("sound", "sounds/beep.ogg") at center
        
            
    if shadow_enable == 1:
        add "images/shadow.png" align (0.5,0.5)


label megaship_prison:
    
    call atmo_spaceship from _call_atmo_spaceship_4
    stop music fadeout 1.0
    
    image megaship_prison = imagemapsdir + "megaship_prison.png"
    
    scene megaship_prison
    show screen notify("prison hall")
    
    show bgcolor behind megaship_prison
    
    show propeller:
        pos (427,167)
        linear 10 rotate 180.0
        rotate 0
        repeat
        
    show buttonscreen:
        pos (545, 70)
        rotate 90
    
    
    # set all variables for the map (nodes and path)
    $ nodeA = (347, 406)
    $ nodeB = (370, 298)
    $ nodeC = (277, 299)
    $ nodeD = (277, 192)

    $ nodeAA = (277, 83)
    $ nodeBB = (520, 70)
    $ nodeCC = (523, 294)
    $ nodeDD = (57, 82)

    $ pathA = (nodeA, nodeB, (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0))
    $ pathB = (nodeA, nodeB, nodeC, nodeD, nodeAA, (0, 0), nodeCC, (0, 0))
    $ pathC = ((0, 0), nodeB, nodeC, nodeD, nodeAA, (0, 0), nodeCC, (0, 0))
    $ pathD = ((0, 0), nodeB, nodeC, nodeD, nodeAA, (0, 0), nodeCC, (0, 0))
     
    $ pathAA = ((0, 0), nodeB, nodeC, nodeD, nodeAA, nodeBB, (0, 0), (0, 0))
    $ pathBB = ((0, 0), (0, 0), (0, 0), (0, 0), nodeAA, nodeBB, nodeCC, (0, 0))
    $ pathCC = ((0, 0), nodeB, nodeC, nodeD, (0, 0), nodeBB, nodeCC, (0, 0))
    $ pathDD = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)


label loop_megaship_prison:

    while True:
        # start "move through the map" loop
        call startpos from _call_startpos_50

        # do something at node?
        if exitpos == 1:
            call sound_screw from _call_sound_screw_7
            $ startpos = 11
            jump megaship_aeration 
            
        if exitpos == 2:
            if startpos == 2:
                m "This is the prison main hall. {w=2.0} {nw}"
                if megaship_prisondoor_button == False:
                    m "Maybe I can find the way out of the prison? {w=4.0} {nw}"
            $ startpos = 2

            
        if exitpos == 3:
            if startpos == 3:
                call dialog_closed from _call_dialog_closed_22
            $ startpos = 3

            
        if exitpos == 4:
            if startpos == 4:
                call dialog_closed from _call_dialog_closed_23
            $ startpos = 4

            

        if exitpos == 11:
            if startpos ==11:
                call dialog_closed from _call_dialog_closed_24    
            $ startpos = 11        

            
        if exitpos == 22:
            if startpos == 22:
                show screen megaship_buttons1 # show button screen
            $ startpos = 22

            
        if exitpos == 33:
            if startpos == 33:
                if megaship_prisondoor_button == False:
                    call dialog_closed from _call_dialog_closed_25

                else:
                    call sound_door from _call_sound_door_112
                    $ liftpos = 0
                    jump megaship_lift1
            
            $ startpos = 33
                
            
        if exitpos == 44:
            $ startpos = 44



