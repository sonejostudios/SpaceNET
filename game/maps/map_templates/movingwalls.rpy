# MAPS
############################################

init:
    # moving wall positions
    $ movingwall1 = 1
    $ movingwall2 = 2
    $ movingwall3 = 3


screen dev:
    text "[movingwall1] - [movingwall2] - [movingwall3]" at truecenter


label movingwalls:
    
    image movingwallsbg = imagemapsdir + "mwbg.png"
    
    image movingwall:
        "images/movingwall.png"
        anchor (0.5,0.5)
    
    scene movingwallsbg
    show screen notify("moving walls")
    
    #show screen dev
    
    show bgcolor behind movingwallsbg
    
    
    # set all variables for the map (nodes and path)
    $ nodeA = (46, 93)
    $ nodeB = (146, 130)
    $ nodeC = (700, 90)
    $ nodeD = (750, 240)

    $ nodeAA = (700, 390)
    $ nodeBB = (146, 350)
    $ nodeCC = (99, 430)
    $ nodeDD = (546, 352)

    $ pathA = (nodeA, nodeB, (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0))
    $ pathB = (nodeA, nodeB, (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0))
    $ pathC = ((0, 0), (0, 0), nodeC, nodeD, nodeAA, (0, 0), (0, 0), (0, 0))
    $ pathD = ((0, 0), (0, 0), nodeC, nodeD, nodeAA, (0, 0), (0, 0), (0, 0))
     
    $ pathAA = ((0, 0), (0, 0), nodeC, nodeD, nodeAA, (0, 0), (0, 0), (0, 0))
    $ pathBB = ((0, 0), (0, 0), (0, 0), (0, 0), (0, 0), nodeBB, nodeCC, (0, 0))
    $ pathCC = ((0, 0), (0, 0), (0, 0), (0, 0), (0, 0), nodeBB, nodeCC, (0, 0))
    $ pathDD = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)


    # show walls first
    show movingwall as mwall1 behind movingwallsbg:
        xpos 300
        ypos 80
        
    show movingwall as mwall2 behind movingwallsbg:
        xpos 430
        ypos 240
        
    show movingwall as mwall3 behind movingwallsbg:
        xpos 560
        ypos 400




label loop_movingwalls:
    
    #reset path
    $ pathA = (nodeA, nodeB, (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0))
    $ pathB = (nodeA, nodeB, (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0))
    $ pathC = ((0, 0), (0, 0), nodeC, nodeD, nodeAA, (0, 0), (0, 0), (0, 0))
     
    $ pathAA = ((0, 0), (0, 0), nodeC, nodeD, nodeAA, (0, 0), (0, 0), (0, 0))
    $ pathBB = ((0, 0), (0, 0), (0, 0), (0, 0), (0, 0), nodeBB, nodeCC, (0, 0))
    $ pathCC = ((0, 0), (0, 0), (0, 0), (0, 0), (0, 0), nodeBB, nodeCC, (0, 0))
    
    #redraw path
    if movingwall1 == 1 and movingwall2 == 1 and movingwall3 == 1:
        $ pathA = (nodeA, nodeB, nodeC, (0, 0), (0, 0), (0, 0), (0, 0), (0, 0))
        $ pathB = (nodeA, nodeB, nodeC, (0, 0), (0, 0), (0, 0), (0, 0), (0, 0))
        $ pathC = (nodeA, nodeB, nodeC, nodeD, nodeAA, (0, 0), (0, 0), (0, 0))
        
    if movingwall1 == 3 and movingwall2 == 3 and movingwall3 == 3:
        $ pathAA = ((0, 0), (0, 0), nodeC, nodeD, nodeAA, nodeBB, nodeCC, (0, 0))
        $ pathBB = ((0, 0), (0, 0), (0, 0), (0, 0), nodeAA, nodeBB, nodeCC, (0, 0))
        $ pathCC = ((0, 0), (0, 0), (0, 0), (0, 0), nodeAA, nodeBB, nodeCC, (0, 0))
    
    

    # start "move through the map" loop
    call startpos

    # do something at node?
    if exitpos == 1:
        call sound_door
        $ startpos = 1
        jump mapdemos
        
    if exitpos == 2:
        if startpos == 2:
            jump movingwall_buttons
            
        $ startpos = 2
        jump loop_movingwalls
        
    if exitpos == 3:
        $ startpos = 3
        jump loop_movingwalls
        
    if exitpos == 4:
        if startpos == 4:
            jump movingwall_buttons
            
        $ startpos = 4
        jump loop_movingwalls 
        

    #exits routing "got to map and set position for next map"
    if exitpos == 11:  
        $ startpos = 11     
        jump loop_movingwalls   
        
    if exitpos == 22:
        if startpos == 22:
            jump movingwall_buttons
        
        $ startpos = 22
        jump loop_movingwalls 
        
    if exitpos == 33:
        call sound_door
        $ startpos = 1
        jump mapdemos
        
    if exitpos == 44:
        $ startpos = 44
        jump loop_movingwalls



# moving buttons   
label movingwall_buttons:
    
    
    show screen movingwall_buttons_panel
    
    pause 
    #menu:
    #    "button 1":
    #        $ movingwall1 += 1
    #    "button 2":
    #        $ movingwall1 += 1
    #        $ movingwall3 += 1
    #    "button 3":
    #        $ movingwall2 += 1
    #        $ movingwall3 += 1
    #    "exit":
    #        return
    
    jump loop_movingwalls




# move the walls
label movethewalls:

                
    if movingwall1 > 4:
        $ movingwall1 = 1
    if movingwall2 > 4:
        $ movingwall2 = 1
    if movingwall3 > 4:
        $ movingwall3 = 1
        
        
    # move wall1
    if movingwall1 == 1:
        show movingwall as mwall1:
            linear 1 ypos 80
    if movingwall1 == 2 or movingwall1 == 4:
        show movingwall as mwall1:
            linear 1 ypos 240
    if movingwall1 == 3:
        show movingwall as mwall1:
            linear 1 ypos 400
            
    # move wall2
    if movingwall2 == 1:
        show movingwall as mwall2:
            linear 1 ypos 80
    if movingwall2 == 2 or movingwall2 == 4:
        show movingwall as mwall2:
            linear 1 ypos 240
    if movingwall2 == 3:
        show movingwall as mwall2:
            linear 1 ypos 400
            
    # move wall3
    if movingwall3 == 1:
        show movingwall as mwall3:
            linear 1 ypos 80
    if movingwall3 == 2 or movingwall3 == 4:
        show movingwall as mwall3:
            linear 1 ypos 240
    if movingwall3 == 3:
        show movingwall as mwall3:
            linear 1 ypos 400
            
    
    call sound_movingwall
    pause 1

    jump loop_movingwalls
    
    





#button screen
screen movingwall_buttons_panel zorder -999:
    #add "#112119"
    
    imagebutton: 
        idle "images/maps/bg.png" 
        action Hide("movingwall_buttons_panel") at topleft
            
    add "inventory/inventory.png"

    hbox xalign 0.5 yalign 0.5:
        vbox xalign 0.5:
            label "1" at center
            null height 10
            imagebutton:
                auto "images/buttonbig_%s.png" 
                action SetVariable("movingwall1", movingwall1 +1), Hide("movingwall_buttons_panel"), Jump("movethewalls") at center
            
        null width 100
        
        vbox xalign 0.5:
            label "2" at center
            null height 10
            imagebutton:
                auto "images/buttonbig_%s.png" 
                action SetVariable("movingwall1", movingwall1 +1), SetVariable("movingwall3", movingwall3 +1), Hide("movingwall_buttons_panel"), Jump("movethewalls") at center
            
        null width 100
        
        vbox xalign 0.5:
            label "3" at center
            null height 10
            imagebutton: 
                auto "images/buttonbig_%s.png" 
                action SetVariable("movingwall3", movingwall3 +1), SetVariable("movingwall2", movingwall2 +1), Hide("movingwall_buttons_panel"), Jump("movethewalls") at center
            
