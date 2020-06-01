
##############################################
label megaship_multimap1:
    
    call atmo_spaceship_hum
    
    
    
    image mm_bg1:
        imagemapsdir + "/multimap/mm_bg1.png"
        anchor (0.5, 0.5)
        pos (0.5,0.5)
    
    scene mm_bg1 zorder -101
    
    show screen notify("spaceship corridor")
    
    # Set position and path vor special nodes (B,C and D) in specific xy position. 
    # The others (A, AA, BB, CC, DD) are used by the multimap engine.
    $ nodeB = (000,000)
    $ nodeC = (000,000)
    $ nodeD = (000,000)
    
    $ pathB = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)
    $ pathC = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)
    $ pathD = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)
    

    # multimap array
    $ multiarray = [["1E","7S","--","--",  "--","--","--","--"],
                    ["--","1N","--","--",  "--","--","--","--"],
                    ["--","--","--","--",  "--","--","--","--"],
                    ["--","--","--","--",  "--","--","--","--"],
                    ["--","--","--","--",  "--","--","--","--"],
                    ["--","--","--","--",  "--","--","--","--"],
                    ["--","--","--","--",  "--","--","--","--"],
                    ["--","--","--","--",  "--","--","--","--"]]



label loop_megaship_multimap1:
    # draw special objects (doors and items) in special places
    call specialplaces_megaship_multimap1 

    # start enter in animation
    call multimap_startanim
    
    # special nodes
    call specialnodes_megaship_multimap1

    # start "move through the map" loop
    call startpos
    #$ pathA = pathviewall
    

    
    
# do something at node?
    # if at node A
    if exitpos == 1:       
        $ startpos = 1
        jump loop_megaship_multimap1
      
        
    # if at node B
    if exitpos == 2:
        
        #to lift1
        if multiposx == 0 and multiposy == 0:
            call sound_door
            $ liftpos = 3
            jump megaship_lift1
    
        # to lift2
        if multiposx == 1 and multiposy == 1:
            call sound_door
            $ liftpos = 1
            jump megaship_lift2
        
        else:
            jump loop_megaship_multimap1
        
    
    # if at node C
    if exitpos == 3:
        $ startpos = 3
        jump loop_megaship_multimap1
        
    
    # if at node D
    if exitpos == 4:
        $ startpos = 4
        jump loop_megaship_multimap1     



##
    # if at node AA
    if exitpos == 11:
        # go out of the multimap
        if multiposx == 0 and multiposy == 0:
            $ startpos = 1
            jump map4
        
        $ startpos = 33   #if going out at AA
        $ multiposy -= 1
        jump loop_megaship_multimap1
            
    # if at node BB
    if exitpos == 22:
        $ startpos = 44
        $ multiposx += 1
        jump loop_megaship_multimap1
        
    # if at node CC
    if exitpos == 33:
        $ startpos = 11
        $ multiposy += 1
        jump loop_megaship_multimap1
        
    # if at node DD
    if exitpos == 44:
        $ startpos = 22
        $ multiposx -= 1
        jump loop_megaship_multimap1





# special places with special objects
label specialplaces_megaship_multimap1:
    
    # door v1 - to prison
    if multiposx == 0 and multiposy == 0:
        # set nodeB
        if nodeB != multinodeposW:
            $ nodeB = multinodeposW
            if pnc_mode == False:
                show nodeanime as pathnodeB:
                    pos nodeB
                
        show doorv as doorv1 zorder -80:
            pos multiobjectposW
    else:
        hide doorv1
        
        
    # door v2 - to spaceport
    if multiposx == 1 and multiposy == 1:
        # set nodeB
        if nodeB != multinodeposE:
            $ nodeB = multinodeposE
            if pnc_mode == False:
                show nodeanime as pathnodeB:
                    pos nodeB
                
        show doorv as doorv2 zorder -80:
            pos multiobjectposE
    else:
        hide doorv2


    return
    
  
    
# special nodes
label specialnodes_megaship_multimap1:
    
    # node door v1 - to prison
    if multiposx == 0 and multiposy == 0:
        $ nodeB = multinodeposW
        $ pathA = (nodeA, nodeB, (0,0), (0,0), (0,0), nodeBB, (0,0), (0,0))
        $ pathB = (nodeA, nodeB, (0,0), (0,0), (0,0), nodeBB, (0,0), (0,0))
        $ pathBB = (nodeA, nodeB, (0,0), (0,0), (0,0), nodeBB, (0,0), (0,0))
        

                
    # node door v2 - to spaceport
    if multiposx == 1 and multiposy == 1:
        $ nodeB = multinodeposE
        $ pathA = (nodeA, nodeB, (0,0), (0,0), nodeAA, (0,0), (0,0), (0,0))
        $ pathB = (nodeA, nodeB, (0,0), (0,0), nodeAA, (0,0), (0,0), (0,0))
        $ pathAA = (nodeA, nodeB, (0,0), (0,0), nodeAA, (0,0), (0,0), (0,0))
        
 

    return

    



    
    
