# MAPS

init:
    $ megaship_key_open = False


############################################
label megaship_store:
    
    call atmo_spaceship from _call_atmo_spaceship_1
    stop music fadeout 1.0
    
    image megaship_store = imagemapsdir + "megaship_store.png"
    
    scene megaship_store
    show screen notify("staff room")
    
    show bgcolor behind megaship_store
    
    
    show bigdoor behind megaship_store:
        alpha 0.3
        anchor (0.5,0.5)
        pos (500,100)
        linear 8 pos (400,100)
        repeat
        
    show bigdoor as bigdoor2 behind megaship_store:
        alpha 0.3
        anchor (0.5,0.5)
        pos (500,400)
        linear 8 pos (400,400)
        repeat
        
    show terminalmap:
        anchor (0.5, 0.5)
        pos (260,420)
    
    
    # set all variables for the map (nodes and path)
    $ nodeA = (65, 243)
    $ nodeB = (267, 243)
    $ nodeC = (528, 240)
    $ nodeD = (260, 382)

    $ nodeAA = (684, 100)
    $ nodeBB = (684, 200)
    $ nodeCC = (684, 300)
    $ nodeDD = (684, 400)

    $ pathA = (nodeA, nodeB, nodeC, (0, 0), (0, 0), (0, 0), (0, 0), (0, 0))
    $ pathB = (nodeA, nodeB, nodeC, nodeD, (0, 0), (0, 0), (0, 0), (0, 0))
    $ pathC = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)
    $ pathD = ((0, 0), nodeB, nodeC, nodeD, (0, 0), (0, 0), (0, 0), (0, 0))
     
    $ pathAA = ((0, 0), (0, 0), nodeC, (0, 0), nodeAA, nodeBB, nodeCC, nodeDD)
    $ pathBB = ((0, 0), (0, 0), nodeC, (0, 0), nodeAA, nodeBB, nodeCC, nodeDD)
    $ pathCC = ((0, 0), (0, 0), nodeC, (0, 0), nodeAA, nodeBB, nodeCC, nodeDD)
    $ pathDD = ((0, 0), (0, 0), nodeC, (0, 0), nodeAA, nodeBB, nodeCC, nodeDD)


label loop_megaship_store:
    
    while True:
        # start "move through the map" loop
        call startpos from _call_startpos_10

        # do something at node?
        if exitpos == 1:
            call sound_door from _call_sound_door_24
            $ startpos = 1 
            jump megaship_lift2
            
        if exitpos == 2:
            $ startpos = 2
            
        if exitpos == 3:
            if startpos == 3:
                m "There are 4 personal lockers. {w=2.5} {nw}" 
            $ startpos = 3
            
        if exitpos == 4:
            if startpos == 4:
                if "spacesuit" not in inventory:
                    m "This looks like a terminal.{w=2.0} {nw}"
                call terminal from _call_terminal_1
            $ startpos = 4
            

        #exits routing "got to map and set position for next map"
        if exitpos == 11:
            if startpos == 11: # key
                if megaship_key_open == False:
                    if inventory_select == "key":
                        call use_and_keep_item from _call_use_and_keep_item_4
                        call sound_screw from _call_sound_screw
                        m "Now it's open!{w=2.0} {nw}" 
                        $ megaship_key_open = True
                    else:
                        call dialog_closed from _call_dialog_closed_3
                else:
                    if "minidroid" not in inventory: # get minidroid
                        m "There is a small droid there. {w=2.0} {nw}"
                        m "It is written 'minidroid' on it. {w=2.5} {nw}"
                        m "I think this could be really useful to explore narrow places. {w=4.0} {nw}"
                        call take_item("minidroid") from _call_take_item_3
                    else:
                        call dialog_nothing from _call_dialog_nothing_11
            
            $ startpos = 11         
            
        if exitpos == 22: # notebook
            if startpos == 22:
                if "notebook" not in inventory:
                    m "There is a notebook!{w=2.0} {nw}"
                    m "This will be really handy to remember things.{w=3.0} {nw}"
                    call take_item("notebook") from _call_take_item_4
                else:
                    call dialog_nothing from _call_dialog_nothing_12
            $ startpos = 22
            
            
        if exitpos == 33: # spacesuit
            if startpos == 33:
                
                if "spacesuit" not in inventory:
                    m "There is a space suit!{w=2.0} {nw}"
                    call take_item("spacesuit") from _call_take_item_5
                
                else:
                    call dialog_nothing from _call_dialog_nothing_13
                #call dialog_closed  
            $ startpos = 33

            
        if exitpos == 44:
            if startpos == 44:
                call dialog_closed from _call_dialog_closed_4  
            $ startpos = 44


