
##############################################

init:
    $ button_cargo_multimap1 = False

label cargo_multimap1:
    
    call music_cargo
    
    image circles_bg:
        imagemapsdir + "/multimap/circlesbg.png"
        anchor (0.5, 0.5)
        pos (0.5,0.5)
        alpha 0.2
        
    $ showcircles = True
    
    scene bgcolor zorder -101
    
    
    if showcircles == True:
        show circles_bg zorder -100
    
    else: 
        hide circles_bg

    #show screen notify("multimap 1")
    
    # Set position and path vor special nodes (B,C and D) in specific xy position. 
    # The others (A, AA, BB, CC, DD) are used by the multimap engine.
    $ nodeB = (-100,000)
    $ nodeC = (-100,000)
    $ nodeD = (-100,000)
    
    $ pathB = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)
    $ pathC = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)
    $ pathD = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)
    

    # multimap array
    $ multiarray = [["1S","1E","7S","1S",  "--","--","--","--"],
                    ["7N","3S","7W","2N",  "--","--","--","--"],
                    ["1E","4N","2E","7W",  "--","--","--","--"],
                    ["1E","3N","2E","1W",  "--","--","--","--"],
                    ["--","--","--","--",  "--","--","--","--"],
                    ["--","--","--","--",  "--","--","--","--"],
                    ["--","--","--","--",  "--","--","--","--"],
                    ["--","--","--","--",  "--","--","--","--"]]



label loop_cargo_multimap1:
    # alarm
    call alarm_check
    
    
    # draw special objects (doors and items) in special places
    call specialplaces_cargo_multimap1 

    # start enter in animation
    call multimap_startanim
    
    # special nodes
    call specialnodes_cargo_multimap1

    # start "move through the map" loop
    call startpos
    #$ pathA = pathviewall
    

    
    
# do something at node?
    # if at node A
    if exitpos == 1:       
        $ startpos = 1
        jump loop_cargo_multimap1
        
    # if at node B
    if exitpos == 2:
        $ startpos = 2
        
        # doorh0 - entrance
        if multiposx == 0 and multiposy == 0:
            call sound_door
            $ multiposx = 0
            $ multiposy = 0
            $ startpos = 33
            jump cargo_movingwalls
        
        # doorh1 - sortcut
        if multiposx == 0 and multiposy == 1:
            call sound_door
            $ multiposx = 0
            $ multiposy = 2
            jump cargo_multimap1
        
        # doorh2 - shortcut
        if multiposx == 0 and multiposy == 2:
            call sound_door
            $ multiposx = 0
            $ multiposy = 1
            jump cargo_multimap1
            
        # info panel
        if multiposx == 0 and multiposy == 3:
            if startpos == 2:
                call cargo_multimap_info
            jump cargo_multimap1
            
        
        #door v1 center right - tube room
        if multiposx == 2 and multiposy == 1:
            
            if inventory_select == "robotcard":
                call use_and_keep_item
                call sound_door
                m "Check!{w=1}{nw}"
                $ startpos = 4
                jump cargo_smallroom_tube
            
            else:
                call dialog_closed

        
        
        # door v2 button bottom right
        if multiposx == 3 and multiposy == 3:
            call sound_door
            #call dialog_closed
            #$ multiposx = 0
            #$ multiposy = 0
            #m "it's open! but nothing interesting there..."
            $ startpos = 1
            jump cargo_conveyor1
            
            $ showcircles = False
            jump cargo_multimap1
        
            
            
        # doorh3 crew card
        if multiposx == 3 and multiposy == 0:
            
            $ startpos = 3
            call sound_door
            jump cargo_smallroom
            
 
        jump loop_cargo_multimap1
        
        
        
    # if at node C
    if exitpos == 3:
        $ startpos = 3
        jump loop_cargo_multimap1
        
    # if at node D
    if exitpos == 4:
        $ startpos = 4
        jump loop_cargo_multimap1     

#exits routing "go to map"
    # if at node AA
    if exitpos == 11:
        # go out of the multimap
        if multiposx == 0 and multiposy == 0:
            $ startpos = 1
            jump cargo_movingwalls
        
        $ startpos = 33   #if going out at AA
        $ multiposy -= 1
        jump loop_cargo_multimap1
            
    # if at node BB
    if exitpos == 22:
        $ startpos = 44
        $ multiposx += 1
        jump loop_cargo_multimap1
        
    # if at node CC
    if exitpos == 33:
        $ startpos = 11
        $ multiposy += 1
        jump loop_cargo_multimap1
        
    # if at node DD
    if exitpos == 44:
        $ startpos = 22
        $ multiposx -= 1
        jump loop_cargo_multimap1





# special places with special objects
label specialplaces_cargo_multimap1:
    
    
    # door h0 - entrance
    if multiposx == 0 and multiposy == 0:
        
        # set nodeB
        if nodeB != multinodeposN:
            $ nodeB = multinodeposN
            if pnc_mode == False:
                show nodeanime as pathnodeB:
                    pos nodeB

        show doorh as doorh0 zorder -80:
            pos multiobjectposN
            
    else:
        hide doorh0
        hide circle
    
    
    
    # door h1 - shortcut
    if multiposx == 0 and multiposy == 1:
        
        # set nodeB
        if nodeB != multinodeposS:
            $ nodeB = multinodeposS
            if pnc_mode == False:
                show nodeanime as pathnodeB:
                    pos nodeB
        
        show doorh as doorh1 zorder -80:
            pos multiobjectposS
        
        show circle zorder -100:
                pos (140,230)
            
        if renpy.showing("propeller") != True:
            show propeller zorder -99:
                pos (140,230)
                linear 10 rotate -180.0
                rotate 0
                repeat
    else:
        hide doorh1
        hide propeller
        hide circle
        
        
        
    # door h2 - shortcut
    if multiposx == 0 and multiposy == 2:
        
        # set nodeB
        if nodeB != multinodeposN:
            $ nodeB = multinodeposN
            if pnc_mode == False:
                show nodeanime as pathnodeB:
                    pos nodeB
        
        show doorh as doorh2 zorder -80:
            pos multiobjectposN
        
    else:
        hide doorh2
        
        
        
    # door v1 - to tube room
    if multiposx == 2 and multiposy == 1:
        
        # set nodeB
        if nodeB != multinodeposE:
            $ nodeB = multinodeposE
            if pnc_mode == False:
                show nodeanime as pathnodeB:
                    pos nodeB
        
        show doorv as doorv1 zorder -80:
            pos multiobjectposE
    
        if renpy.showing("propeller3") != True:
                show propeller as propeller2 zorder -99:
                    pos (401,401)
                    zoom 0.55
                    alpha 0.2
                show propeller as propeller3 zorder -99:
                    pos (661,81)
                    zoom 0.55
                    alpha 0.2
                    linear 10 rotate -180.0
                    rotate 0
                    repeat
            
    else:
        hide doorv1
        hide propeller3
        hide propeller2
        
        
        
    
    # door v2 door to conveyor1
    if multiposx == 3 and multiposy == 3:
        
        # set nodeB
        if nodeB != multinodeposE:
            $ nodeB = multinodeposE
            if pnc_mode == False:
                show nodeanime as pathnodeB:
                    pos nodeB
        
        #"aa"
        show doorv as doorv2 zorder -80:
            pos multiobjectposE
    else:
        hide doorv2
    
    

        
    
    # button
    if multiposx == 0 and multiposy == 3:
        
        # set nodeB
        if nodeB != multinodeposN:
            $ nodeB = multinodeposN
            if pnc_mode == False:
                show nodeanime as pathnodeB:
                    pos nodeB
        
        show buttonscreen as button1 zorder -80:
            pos multiobjectposN
            
        if renpy.showing("propeller4") != True:
            show propeller as propeller4 zorder -99:
                pos (141,241)
                zoom 0.55
                alpha 0.2
                linear 10 rotate -180.0
                rotate 0
                repeat
            
    else:
        hide button1
        hide propeller4
        
    
    # robot room
    if multiposx == 3 and multiposy == 0:
        
        # set nodeB
        if nodeB != multinodeposN:
            $ nodeB = multinodeposN
            if pnc_mode == False:
                show nodeanime as pathnodeB:
                    pos nodeB
        
        show doorh as doorh3 zorder -80:
            pos multiobjectposN
    else:
        hide doorh3
        



    return
    
  
    
# special nodes
label specialnodes_cargo_multimap1:
    
    
    
    # node door h0 - entrance
    if multiposx == 0 and multiposy == 0:
        $ nodeB = multinodeposN
        $ pathA = (nodeA, nodeB, (0,0), (0,0), (0,0), (0,0), nodeCC, (0,0))
        $ pathB = (nodeA, nodeB, (0,0), (0,0), (0,0), (0,0), nodeCC, (0,0))
        $ pathCC = (nodeA, nodeB, (0,0), (0,0), (0,0), (0,0), nodeCC, (0,0))
        

    
    # node door h1 - shortcut
    if multiposx == 0 and multiposy == 1:
        $ nodeB = multinodeposS
        $ pathA = (nodeA, nodeB, (0,0), (0,0), nodeAA, nodeBB, (0,0), (0,0))
        $ pathB = (nodeA, nodeB, (0,0), (0,0), nodeAA, nodeBB, (0,0), (0,0))
        $ pathAA = (nodeA, nodeB, (0,0), (0,0), nodeAA, (0,0), (0,0), (0,0))
        $ pathBB = (nodeA, nodeB, (0,0), (0,0), (0,0), nodeBB, (0,0), (0,0))
        


    # node door h2 - shortcut
    if multiposx == 0 and multiposy == 2:
        $ nodeB = multinodeposN
        $ pathA = (nodeA, nodeB, (0,0), (0,0), (0,0), nodeBB, (0,0), (0,0))
        $ pathB = (nodeA, nodeB, (0,0), (0,0), (0,0), nodeBB, (0,0), (0,0))
        $ pathBB = (nodeA, nodeB, (0,0), (0,0), (0,0), nodeBB, (0,0), (0,0))
        

                
    # node door v1 - door to tube
    if multiposx == 2 and multiposy == 1:
        $ nodeB = multinodeposE
        $ pathA = (nodeA, nodeB, (0,0), (0,0), nodeAA, (0,0), (0,0), nodeDD)
        $ pathB = (nodeA, nodeB, (0,0), (0,0), nodeAA, (0,0), (0,0), nodeDD)
        $ pathAA = (nodeA, nodeB, (0,0), (0,0), nodeAA, (0,0), (0,0), (0,0))
        $ pathDD = (nodeA, nodeB, (0,0), (0,0), (0,0), (0,0), (0,0), nodeDD)
        

                
    # node door v2 to conveyor1
    if multiposx == 3 and multiposy == 3:
        $ nodeB = multinodeposE
        $ pathA = (nodeA, nodeB, (0,0), (0,0), (0,0), (0,0), (0,0), nodeDD)
        $ pathB = (nodeA, nodeB, (0,0), (0,0), (0,0), (0,0), (0,0), nodeDD)
        $ pathDD = (nodeA, nodeB, (0,0), (0,0), (0,0), (0,0), (0,0), nodeDD)
        


                
    # node button1
    if multiposx == 0 and multiposy == 3:
        $ nodeB = multinodeposN
        $ pathA = (nodeA, nodeB, (0,0), (0,0), (0,0), nodeBB, (0,0), (0,0))
        $ pathB = (nodeA, nodeB, (0,0), (0,0), (0,0), nodeBB, (0,0), (0,0))
        $ pathBB = (nodeA, nodeB, (0,0), (0,0), (0,0), nodeBB, (0,0), (0,0))
        

                
    # node door h crew card
    if multiposx == 3 and multiposy == 0:
        $ nodeB = multinodeposN
        $ pathA = (nodeA, nodeB, (0,0), (0,0), (0,0), (0,0), nodeCC, (0,0))
        $ pathB = (nodeA, nodeB, (0,0), (0,0), (0,0), (0,0), nodeCC, (0,0))
        $ pathCC = (nodeA, nodeB, (0,0), (0,0), (0,0), (0,0), nodeCC, (0,0))
        


    return





label cargo_multimap_info:
    
    $ info_panel_symbol = "noentry"

    $ showtext = """
    
    
- A.R.K. Cargo Spaceship -


This area is for crew robots only.

    """
    
    # {font=marvosym.ttf}{size=70}haj{/size}{/font}
    # {font=symbolx.ttf}{size=70}bpr{/size}{/font}
    
    call info_panel # in animations
    
    
    return
    
    



    
    
