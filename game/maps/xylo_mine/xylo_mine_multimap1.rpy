
##############################################

init:
    $ xylo_mine_level1_button1 = True
    $ xylo_mine_level1_button2 = True
    $ xylo_mine_level1_button3 = True
    
    

screen xylo_mine_level1_buttons zorder -999:
    
    on "show" action SetVariable("pnc_nodes_visible", False)
    on "hide" action SetVariable("pnc_nodes_visible", True)
    
    add "#112119"
    imagebutton: 
        idle "images/maps/bg.png" 
        action Hide("xylo_mine_level1_buttons")
    add "inventory/inventory.png"
    
    #text "{color=#8dd35f} lock 1 : [xylo_mine_level1_button1] \n lock 2 : [xylo_mine_level1_button2] \n lock 3 : [xylo_mine_level1_button3] {/color}":
    #    pos (0.1,0.2)
    
    hbox xalign 0.5 yalign 0.5:
        vbox xalign 0.5:
            if multiposx == 1 and multiposy == 3: 
                imagebutton: 
                    auto "images/buttonbig_%s.png"
                    action ToggleVariable("xylo_mine_level1_button1"), Play("sound", "sounds/collect.ogg") at center
                null height 10
                label "high security area lock 1" at center
            
            if multiposx == 2 and multiposy == 3: 
                imagebutton: 
                    auto "images/buttonbig_%s.png"
                    action ToggleVariable("xylo_mine_level1_button2"), Play("sound", "sounds/collect.ogg") at center
                null height 10
                label "high security area lock 2" at center
            
            if multiposx == 3 and multiposy == 3: 
                imagebutton: 
                    auto "images/buttonbig_%s.png"
                    action ToggleVariable("xylo_mine_level1_button3"), Play("sound", "sounds/collect.ogg") at center
                null height 10
                label "high security area lock 3" at center
            
            
    if shadow_enable == 1:
        add "images/shadow.png" align (0.5,0.5)
                
                
    





label xylo_mine_multimap1:
    
    call music_xylo_mine from _call_music_xylo_mine
    call atmo_cave from _call_atmo_cave
    
    image walls_mm1:
        imagemapsdir + "/multimap/multimap1.png"
        anchor (0.5, 0.5)
        pos (0.5,0.5)
        alpha 0.1
        
    scene bgcolor zorder -999
    
    show walls_mm1 zorder -101
    

    #show screen notify("multimap 1")
    
    # Set position and path vor special nodes (B,C and D) in specific xy position. 
    # The others (A, AA, BB, CC, DD) are used by the multimap engine.
    $ nodeB = (000,000)
    $ nodeC = (000,000)
    $ nodeD = (000,000)
    
    $ pathB = (nodeA, nodeB, (0, 0), (0, 0), nodeAA, nodeBB, nodeCC, nodeDD)
    $ pathC = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)
    $ pathD = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)
    

    # multimap array
    $ multiarray = [["--","--","1S","--",  "--","--","--","--"],
                    ["7E","3S","3N","7S",  "--","--","--","--"],
                    ["1N","3E","3S","3W",  "--","--","--","--"],
                    ["--","1N","1N","1N",  "--","--","--","--"],
                    ["--","--","--","--",  "--","--","--","--"],
                    ["--","--","--","--",  "--","--","--","--"],
                    ["--","--","--","--",  "--","--","--","--"],
                    ["--","--","--","--",  "--","--","--","--"]]



label loop_xylo_mine_multimap1:
    # draw special objects (doors and items) in special places
    call specialplaces_xylo_mines_multimap1 from _call_specialplaces_xylo_mines_multimap1 

    # start enter in animation
    call multimap_startanim from _call_multimap_startanim_1
    
    # special nodes
    call specialnodes_xylo_mine_multimap1 from _call_specialnodes_xylo_mine_multimap1

    # start "move through the map" loop
    call startpos from _call_startpos_9
    #$ pathA = pathviewall
    

    
    
# do something at node?
    # if at node A
    if exitpos == 1:       
        $ startpos = 1
        jump loop_xylo_mine_multimap1
        
    
    
    
    # if at node B
    if exitpos == 2:
        $ startpos = 2
        
        # doorh0 - entrance
        if multiposx == 2 and multiposy == 0:
            call sound_door from _call_sound_door_22
            $ startpos = 3
            jump xylo_mine_crossroom1
            
        # doorh1 - to mine
        if multiposx == 0 and multiposy == 2:
            
            if xylo_mine_level1_button1 == False and xylo_mine_level1_button2 == False and xylo_mine_level1_button3 == False:
                call sound_door from _call_sound_door_23
                $ startpos = 1
                jump xylo_mine_level1
            else:
                call dialog_closed from _call_dialog_closed_2
                m "There is a digital display on the door. {w=3} {nw}"
                m "Lock 1: [xylo_mine_level1_button1] \nLock 2: [xylo_mine_level1_button2] \nLock 3: [xylo_mine_level1_button3] {w=4} {nw}"
            
        # button 1
        if multiposx == 1 and multiposy == 3:
            show screen xylo_mine_level1_buttons
            jump loop_xylo_mine_multimap1
            
        # button 2
        if multiposx == 2 and multiposy == 3:
            show screen xylo_mine_level1_buttons
            jump loop_xylo_mine_multimap1
            
        # button 3
        if multiposx == 3 and multiposy == 3:
            show screen xylo_mine_level1_buttons
            jump loop_xylo_mine_multimap1
        
            
        jump loop_xylo_mine_multimap1
        
    
    
    
    
    # if at node C
    if exitpos == 3:
        $ startpos = 3
        jump loop_xylo_mine_multimap1
        
    # if at node D
    if exitpos == 4:
        $ startpos = 4
        jump loop_xylo_mine_multimap1     

#exits routing "go to map"
    # if at node AA
    if exitpos == 11:
        # go out of the multimap
        if multiposx == 0 and multiposy == 0:
            $ startpos = 1
            jump xylo_mine_crossroom1
        
        $ startpos = 33   #if going out at AA
        $ multiposy -= 1
        jump loop_xylo_mine_multimap1
            
    # if at node BB
    if exitpos == 22:
        $ startpos = 44
        $ multiposx += 1
        jump loop_xylo_mine_multimap1
        
    # if at node CC
    if exitpos == 33:
        $ startpos = 11
        $ multiposy += 1
        jump loop_xylo_mine_multimap1
        
    # if at node DD
    if exitpos == 44:
        $ startpos = 22
        $ multiposx -= 1
        jump loop_xylo_mine_multimap1





# special places with special objects
label specialplaces_xylo_mines_multimap1:
    
    
    # door h0 - entrance
    if multiposx == 2 and multiposy == 0:
        # set nodeB
        if nodeB != multinodeposN:
            $ nodeB = multinodeposN
            if pnc_mode == False:
                show nodeanime as pathnodeB:
                    pos nodeB
        
        show doorh as doorh0 zorder -80:
            pos multiobjectposN
        return
            
            
            
    # door h1 - to mine
    if multiposx == 0 and multiposy == 2:
        # set nodeB
        if nodeB != multinodeposS:
            $ nodeB = multinodeposS
            if pnc_mode == False:
                show nodeanime as pathnodeB:
                    pos nodeB
        
        show doorh as doorh1 zorder -80:
            pos multiobjectposS
        return
        
        
        
        
    # button 1
    if multiposx == 1 and multiposy == 3:
        # set nodeB
        if nodeB != multinodeposS:
            $ nodeB = multinodeposS
            if pnc_mode == False:
                show nodeanime as pathnodeB:
                    pos nodeB
        
        
        show buttonscreen as buttonscreen zorder -80:
            pos multiobjectposS
        return
        
        
        
    # button 2
    if multiposx == 2 and multiposy == 3:
        # set nodeB
        if nodeB != multinodeposS:
            $ nodeB = multinodeposS
            if pnc_mode == False:
                show nodeanime as pathnodeB:
                    pos nodeB
        
        
        show buttonscreen as buttonscreen zorder -80:
            pos multiobjectposS
        return
        
        
        
    # button 3
    if multiposx == 3 and multiposy == 3:
        # set nodeB
        if nodeB != multinodeposS:
            $ nodeB = multinodeposS
            if pnc_mode == False:
                show nodeanime as pathnodeB:
                    pos nodeB
        
        
        show buttonscreen as buttonscreen zorder -80:
            pos multiobjectposS
        return
          
            
    else:
        hide doorh0
        hide doorh1
        hide circle
        hide buttonscreen
        
    


    return
    
  
    
# special nodes
label specialnodes_xylo_mine_multimap1:
    
    # node door h0 - entrance
    if multiposx == 2 and multiposy == 0:
        $ nodeB = multinodeposN
        $ pathA = (nodeA, nodeB, (0,0), (0,0), (0,0), (0,0), nodeCC, (0,0))
        $ pathB = (nodeA, nodeB, (0,0), (0,0), (0,0), (0,0), nodeCC, (0,0))
        $ pathCC = (nodeA, nodeB, (0,0), (0,0), (0,0), (0,0), nodeCC, (0,0))
        

    
    # node door h1 - to mine
    if multiposx == 0 and multiposy == 2:
        $ nodeB = multinodeposS
        $ pathA = (nodeA, nodeB, (0,0), (0,0), nodeAA, (0,0), (0,0), (0,0))
        $ pathB = (nodeA, nodeB, (0,0), (0,0), nodeAA, (0,0), (0,0), (0,0))
        $ pathAA = (nodeA, nodeB, (0,0), (0,0), nodeAA, (0,0), (0,0), (0,0))
        

                
    # button 1
    if multiposx == 1 and multiposy == 3:
        $ nodeB = multinodeposS
        $ pathA = (nodeA, nodeB, (0,0), (0,0), nodeAA, (0,0), (0,0), (0,0))
        $ pathB = (nodeA, nodeB, (0,0), (0,0), nodeAA, (0,0), (0,0), (0,0))
        $ pathAA = (nodeA, nodeB, (0,0), (0,0), nodeAA, (0,0), (0,0), (0,0))
        

                
    # button 2
    if multiposx == 2 and multiposy == 3:
        $ nodeB = multinodeposS
        $ pathA = (nodeA, nodeB, (0,0), (0,0), nodeAA, (0,0), (0,0), (0,0))
        $ pathB = (nodeA, nodeB, (0,0), (0,0), nodeAA, (0,0), (0,0), (0,0))
        $ pathAA = (nodeA, nodeB, (0,0), (0,0), nodeAA, (0,0), (0,0), (0,0))
        

                
    # button 3
    if multiposx == 3 and multiposy == 3:
        $ nodeB = multinodeposS
        $ pathA = (nodeA, nodeB, (0,0), (0,0), nodeAA, (0,0), (0,0), (0,0))
        $ pathB = (nodeA, nodeB, (0,0), (0,0), nodeAA, (0,0), (0,0), (0,0))
        $ pathAA = (nodeA, nodeB, (0,0), (0,0), nodeAA, (0,0), (0,0), (0,0))
        

                

    return




    
    
