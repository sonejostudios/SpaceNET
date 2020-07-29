
##############################################
label multimap1:
    
    image walls_mm1:
        imagemapsdir + "/multimap/multimap1.png"
        anchor (0.5, 0.5)
        pos (0.5,0.5)
        
    #image circles_bg:
    #    imagemapsdir + "/multimap/circlesbg.png"
    #    anchor (0.5, 0.5)
    #    pos (0.5,0.5)
        
    $ showcircles = True
    
    scene walls_mm1 zorder -101
    
    if showcircles == True:
        show circles_bg zorder -100
    else: 
        hide circles_bg

    #show screen notify("multimap 1")
    
    # Set position and path vor special nodes (B,C and D) in specific xy position. 
    # The others (A, AA, BB, CC, DD) are used by the multimap engine.
    $ nodeB = (000,000)
    $ nodeC = (000,000)
    $ nodeD = (000,000)
    
    $ pathB = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)
    $ pathC = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)
    $ pathD = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)
    

    # multimap array
    $ multiarray = [["3E","2E","7S","1S",  "7E","2E","7S","--"],
                    ["7N","3S","7W","2N",  "7N","3S","7W","--"],
                    ["1E","4N","2E","7W",  "--","3E","1W","--"],
                    ["1E","3N","2E","1W",  "1E","7W","--","--"],
                    ["--","--","--","--",  "--","--","--","--"],
                    ["--","--","--","--",  "--","--","--","--"],
                    ["--","--","--","--",  "--","--","--","--"],
                    ["--","--","--","--",  "--","--","--","--"]]



label loop_multimap1:
    # draw special objects (doors and items) in special places
    call specialplaces_multimap1 from _call_specialplaces_multimap1 

    # start enter in animation
    call multimap_startanim from _call_multimap_startanim_3
    
    # special nodes
    call specialnodes_multimap1 from _call_specialnodes_multimap1

    # start "move through the map" loop
    call startpos from _call_startpos_72
    #$ pathA = pathviewall
    

    
    
# do something at node?
    # if at node A
    if exitpos == 1:       
        $ startpos = 1
        jump loop_multimap1
        
    # if at node B
    if exitpos == 2:
        $ startpos = 2
        
        # doorh1
        if multiposx == 0 and multiposy == 1:
            call sound_door from _call_sound_door_149
            $ multiposx = 0
            $ multiposy = 2
            jump multimap1
        
        # doorh2
        if multiposx == 0 and multiposy == 2:
            call sound_door from _call_sound_door_150
            $ multiposx = 0
            $ multiposy = 1
            jump multimap1
            
        #door v1
        if multiposx == 2 and multiposy == 1:
            call dialog_closed from _call_dialog_closed_36
        
        # door button
        if multiposx == 3 and multiposy == 3 and button_multimap1 == True:
            call sound_door from _call_sound_door_151
            $ multiposx = 4
            $ multiposy = 3
            
            $ showcircles = False
            jump multimap1
        if multiposx == 3 and multiposy == 3 and button_multimap1 == False:
            call dialog_closed from _call_dialog_closed_37
            jump multimap1
        
        # door button back
        if multiposx == 4 and multiposy == 3:
            call sound_door from _call_sound_door_152
            $ multiposx = 3
            $ multiposy = 3
            
            $ showcircles = True
            jump multimap1
            
        # door locked
        if multiposx == 0 and multiposy == 3:
            call button_multimap1 from _call_button_multimap1
            
        jump loop_multimap1
        
    # if at node C
    if exitpos == 3:
        $ startpos = 3
        jump loop_multimap1
        
    # if at node D
    if exitpos == 4:
        $ startpos = 4
        jump loop_multimap1     

#exits routing "go to map"
    # if at node AA
    if exitpos == 11:
        # go out of the multimap
        if multiposx == 0 and multiposy == 0:
            $ startpos = 1
            jump map4
        
        $ startpos = 33   #if going out at AA
        $ multiposy -= 1
        jump loop_multimap1
            
    # if at node BB
    if exitpos == 22:
        $ startpos = 44
        $ multiposx += 1
        jump loop_multimap1
        
    # if at node CC
    if exitpos == 33:
        $ startpos = 11
        $ multiposy += 1
        jump loop_multimap1
        
    # if at node DD
    if exitpos == 44:
        $ startpos = 22
        $ multiposx -= 1
        jump loop_multimap1





# special places with special objects
label specialplaces_multimap1:
    
    # door h1
    if multiposx == 0 and multiposy == 1:
        show doorh as doorh1 zorder -80:
            pos multiobjectposS
            
        if renpy.showing("propeller") != True:
            show circle zorder -99:
                pos (140,230)
            show propeller zorder -99:
                pos (140,230)
                linear 10 rotate -180.0
                rotate 0
                repeat
    else:
        hide doorh1
        hide propeller
        hide circle
        
    # door h2
    if multiposx == 0 and multiposy == 2:
        show doorh as doorh2 zorder -80:
            pos multiobjectposN
        
        
    else:
        hide doorh2
        
    # door v1
    if multiposx == 2 and multiposy == 1:
        show doorv as doorv1 zorder -80:
            pos multiobjectposE
    
        if renpy.showing("propeller3") != True:
                show propeller as propeller2 zorder -99:
                    pos (401,401)
                    zoom 0.55
                show propeller as propeller3 zorder -99:
                    pos (661,81)
                    zoom 0.55
                    linear 10 rotate -180.0
                    rotate 0
                    repeat
            
    else:
        hide doorv1
        hide propeller3
        hide propeller2
        
    # door v2 door with button
    if multiposx == 3 and multiposy == 3:
        #"aa"
        show doorv as doorv2 zorder -80:
            pos multiobjectposE
    else:
        hide doorv2
    
    # door v3
    if multiposx == 4 and multiposy == 3:
        show doorv as doorv3 zorder -80:
            pos multiobjectposW
            
    else:
        hide doorv3
        
    # button
    if multiposx == 0 and multiposy == 3:
        show buttons as button1 zorder -80:
            pos multiobjectposN
            
        if renpy.showing("propeller4") != True:
            show propeller as propeller4 zorder -99:
                pos (141,241)
                zoom 0.55
                linear 10 rotate -180.0
                rotate 0
                repeat
            
    else:
        hide button1
        hide propeller4
        


    return
    
  
    
# special nodes
label specialnodes_multimap1:
    
    # node door h1
    if multiposx == 0 and multiposy == 1:
        $ nodeB = multinodeposS
        $ pathA = (nodeA, nodeB, (0,0), (0,0), nodeAA, nodeBB, (0,0), (0,0))
        $ pathB = (nodeA, nodeB, (0,0), (0,0), nodeAA, nodeBB, (0,0), (0,0))
        
        if renpy.showing("pathnodeB") != True:
            show nodeanime as pathnodeB:
                pos nodeB
                
    # node door h2
    if multiposx == 0 and multiposy == 2:
        $ nodeB = multinodeposN
        $ pathA = (nodeA, nodeB, (0,0), (0,0), (0,0), nodeBB, (0,0), (0,0))
        $ pathB = (nodeA, nodeB, (0,0), (0,0), (0,0), nodeBB, (0,0), (0,0))
        
        if renpy.showing("pathnodeB") != True:
            show nodeanime as pathnodeB:
                pos nodeB
                
    # node door v1
    if multiposx == 2 and multiposy == 1:
        $ nodeB = multinodeposE
        $ pathA = (nodeA, nodeB, (0,0), (0,0), nodeAA, (0,0), (0,0), nodeDD)
        $ pathB = (nodeA, nodeB, (0,0), (0,0), nodeAA, (0,0), (0,0), nodeDD)
        
        if renpy.showing("pathnodeB") != True:
            show nodeanime as pathnodeB:
                pos nodeB
                
    # node door v2 with button
    if multiposx == 3 and multiposy == 3:
        $ nodeB = multinodeposE
        $ pathA = (nodeA, nodeB, (0,0), (0,0), (0,0), (0,0), (0,0), nodeDD)
        $ pathB = (nodeA, nodeB, (0,0), (0,0), (0,0), (0,0), (0,0), nodeDD)
        
        if renpy.showing("pathnodeB") != True:
            show nodeanime as pathnodeB:
                pos nodeB
                
    # node door v3
    if multiposx == 4 and multiposy == 3:
        $ nodeB = multinodeposW
        $ pathA = (nodeA, nodeB, (0,0), (0,0), (0,0), nodeBB, (0,0), (0,0))
        $ pathB = (nodeA, nodeB, (0,0), (0,0), (0,0), nodeBB, (0,0), (0,0))
        
        if renpy.showing("pathnodeB") != True:
            show nodeanime as pathnodeB:
                pos nodeB
                
    # node button1
    if multiposx == 0 and multiposy == 3:
        $ nodeB = multinodeposN
        $ pathA = (nodeA, nodeB, (0,0), (0,0), (0,0), nodeBB, (0,0), (0,0))
        $ pathB = (nodeA, nodeB, (0,0), (0,0), (0,0), nodeBB, (0,0), (0,0))
        
        if renpy.showing("pathnodeB") != True:
            show nodeanime as pathnodeB:
                pos nodeB

    return





label button_multimap1:
    
    call buttons from _call_buttons_2
    # set button_multimap1 like buttons
    $ button_multimap1 = buttons
    
    return
    



    
    
