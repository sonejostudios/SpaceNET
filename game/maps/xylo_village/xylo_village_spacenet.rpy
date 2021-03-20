# MAPS

############################################

init:

    $ xylo_village_spacenet_button = False
    $ xylo_village_spacenet_button_start = False
    $ xylo_village_spacenet_button_lock = True


screen xylo_village_spacenet_button() zorder -999:
    
    on "show" action SetVariable("pnc_nodes_visible", False)
    on "hide" action SetVariable("pnc_nodes_visible", True)
    
    add "#112119"
    
    imagebutton: 
        idle "images/maps/bg.png" 
        action Hide("xylo_village_spacenet_button")
            
    add "inventory/inventory.png"
    
    hbox xalign 0.5 yalign 0.5:
        vbox xalign 0.5:
            label "Power" at center
            null height 10
            imagebutton: 
                auto "images/buttonbig_%s.png"
                action ToggleVariable("xylo_village_spacenet_button"), Play("sound", "sounds/collect.ogg") at center
                
        null width 50
        
        vbox xalign 0.5:
            label "Start" at center
            null height 10
            imagebutton: 
                auto "images/buttonbig_%s.png"
                action ToggleVariable("xylo_village_spacenet_button_start"), Play("sound", "sounds/collect.ogg") at center
                
        null width 50
        
        vbox xalign 0.5:
            label "Lock" at center
            null height 10
            imagebutton: 
                auto "images/buttonbig_%s.png"
                action ToggleVariable("xylo_village_spacenet_button_lock"), Play("sound", "sounds/collect.ogg") at center
                
    if shadow_enable == 1:
        add "images/shadow.png" align (0.5,0.5)
               






label xylo_village_spacenet:
    
    call atmo_spaceship from _call_atmo_spaceship_6
    
    scene bgcolor
    
    image xylo_village_spacenet = imagemapsdir + "crossroom.png"
    show xylo_village_spacenet at truecenter
    
    image spacenetcomp:
        "images/spacenetcomp.png"
        anchor (0.5,0.5)
    
    show spacenetcomp:
        pos (440,240)
        rotate 90
        rotate_pad True
        
    show terminalmap:
        anchor (0.5,0.5)
        pos (440, 410)
        
        

                
    
    
    show screen notify("Server room")
    
    #doors (comment to disable)
    #show doorh as doorA:
    #    pos (400, 55)
    #show doorv as doorB:
    #    pos (587, 240)
    #show doorh as doorC:
    #    pos (400, 427)
    show doorv as doorD:
        pos (215, 240)
    
    
    # set all variables for the map (nodes and path)
    $ nodeA = (400, 75)
    $ nodeB = (570, 240)
    $ nodeC = (440, 370)
    $ nodeD = (235, 240)
    
    $ nodeAA = (400, 240)
    
    $ nodeBB = (400, 142)
    $ nodeCC = (490, 180)
    $ nodeDD = (-100, -100)

    $ pathA = (nodeA, nodeB, nodeC, nodeD, nodeAA, (0, 0), (0, 0), (0, 0))
    $ pathB = (nodeA, nodeB, nodeC, nodeD, nodeAA, (0, 0), (0, 0), (0, 0))
    $ pathC = ((0, 0), (0, 0), nodeC, nodeD, nodeAA, nodeBB, nodeCC, (0, 0))
    $ pathD = ((0, 0), (0, 0), nodeC, nodeD, nodeAA, nodeBB, nodeCC, (0, 0))
     
    $ pathAA = ((0, 0), (0, 0), nodeC, nodeD, nodeAA, nodeBB, nodeCC, (0, 0))
    
    $ pathBB = ((0, 0), (0, 0), nodeC, nodeD, nodeAA, nodeBB, nodeCC, (0, 0))
    $ pathCC = ((0, 0), (0, 0), nodeC, nodeD, nodeAA, nodeBB, nodeCC, (0, 0))
    $ pathDD = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)


label loop_xylo_village_spacenet:
    
    
    # spacenet sender
    if "xylo_village" in spacenetnodes:
        show spacenetsender:
            pos (547,390)
            

    # start "move through the map" loop
    call startpos from _call_startpos_62

    # do something at node?
    if exitpos == 1:
        $ startpos = 1 
        jump loop_xylo_village_spacenet 
        
    if exitpos == 2:
        $ startpos = 2
        jump loop_xylo_village_spacenet
        
    if exitpos == 3: # terminal
        if startpos == 3:
            call terminal from _call_terminal_12
        
        $ startpos = 3
        
        jump loop_xylo_village_spacenet
        
    if exitpos == 4:
        $ startpos = 11
        call sound_door from _call_sound_door_138
        jump xylo_village2 # out 
        

    #exits routing "got to map and set position for next map"
    if exitpos == 11:
        if startpos == 11:
            m "This room is full of computers. {w=2} {nw}"
            m "And I thought this is a dangerous area? {w=2} {nw}"
            m "Something is weird here... {w=2} {nw}"
        $ startpos = 11     
        jump loop_xylo_village_spacenet   
        
    if exitpos == 22:
        if startpos == 22:
            show screen xylo_village_spacenet_button # power button
        
        $ startpos = 22

        jump loop_xylo_village_spacenet 
        
    if exitpos == 33:
        if startpos == 33:
            jump xylo_village_spacenet_comp
        $ startpos = 33
        jump loop_xylo_village_spacenet
        
    if exitpos == 44:
        $ startpos = 44
        jump loop_xylo_village_spacenet





label xylo_village_spacenet_comp:
    show terminal at topleft
    if shadow_enable == 1:
        show shadow:
            pos (270, 240)
    call sound_beep from _call_sound_beep_37
    
    if xylo_village_spacenet_button == False or xylo_village_spacenet_button_start == False :
        m "The computer interface is not running... {w=2} {nw}"
        jump xylo_village_spacenet
        
    if xylo_village_spacenet_button_lock == True:
        m "This computer is locked... {w=2} {nw}"
        jump xylo_village_spacenet
    
    
    call spacenet_comp("xylo_village") from _call_spacenet_comp_3 # install spacenet
    
    jump xylo_village_spacenet
    

    


