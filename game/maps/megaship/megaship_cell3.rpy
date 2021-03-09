# MAPS


# prison cell with hacker and key

############################################
label megaship_cell3:
    
    call atmo_spaceship_hum from _call_atmo_spaceship_hum_1
    
    show screen notify("prison cell 3")
    
    scene bgcolor 
    show megaship_cell    
    
    show sink:
        anchor (0.5,0.5)
        pos (200, 340)
    show wc:
        anchor (0.5,0.5)
        rotate 180
        pos (150,330)
        
        
    if hacker_in_prison == 1:
        show npc:
            pos (440,340)
            rotate -90    


    
    # set all variables for the map (nodes and path)
    $ nodeA = (401, 330)
    $ nodeB = (520, 260)
    $ nodeC = (288, 230)
    $ nodeD = (200, 305)

    $ nodeAA = (11, 12)
    $ nodeBB = (640, 240)
    $ nodeCC = (159, 240)
    $ nodeDD = (47, 13)

    $ pathA = (nodeA, nodeB, nodeC, (0, 0), (0, 0), (0, 0), (0, 0), (0, 0))
    $ pathB = (nodeA, nodeB, nodeC, (0, 0), (0, 0), nodeBB, nodeCC, (0, 0))
    $ pathC = (nodeA, nodeB, nodeC, nodeD, (0, 0), nodeBB, nodeCC, (0, 0))
    $ pathD = ((0, 0), (0, 0), nodeC, nodeD, (0, 0), (0, 0), nodeCC, (0, 0))
     
    $ pathAA = ((0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0))
    $ pathBB = ((0, 0), nodeB, nodeC, (0, 0), (0, 0), nodeBB, nodeCC, (0, 0))
    $ pathCC = ((0, 0), nodeB, nodeC, nodeD, (0, 0), nodeBB, nodeCC, (0, 0))
    $ pathDD = ((0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0))


label loop_megaship_cell3:
    
    
    while True:
        # start "move through the map" loop
        call startpos from _call_startpos_16

        # do something at node?
        if exitpos == 1:
            if startpos == 1:
                if hacker_in_prison == 1:
                    
                    if "key" not in inventory:
                        hacker "Hello [playername]! {w=2.0} {nw}"
                        hacker "Thank you for coming. {w=1.0}I'm really happy you made it!{w=2.0}{nw}"
                        hacker "Listen... {w=2.0} {nw}"
                        hacker "I really need to leave for my next mission. {w=3.5} {nw}"
                        hacker "While the guards were trying to put me in this cell, I managed to steal their key. {w=4.5} {nw}"
                        hacker "But I have no clue as where to use it. {w=2.5} {nw}"
                        hacker "Maybe you'll find the place? {w=2.5} {nw}"

                        call take_item("key") from _call_take_item_9
                        
                        if "key" in inventory:
                            m "Okay, thanks! I'll see what I can do. {w=3} {nw}"
                            hacker "Okay I will leave now. {w=1}Bye!{w=2.5} {nw}"
                            
                            $ hacker_in_prison = 2
                            
                            show npc:
                                pos (440,340)
                                rotate -90
                                linear 1 rotate -45
                                linear 2 pos nodeC rotate -90
                                linear 1 pos nodeCC
                                linear 1 pos nodeCC
                            
                            pause 4
                            call sound_screw from _call_sound_screw_1
                            pause 1
                            hide npc
                            #m "hacker_in_prison [hacker_in_prison]"
                    else:
                        pass
          
                
                else:
                    m "I'm in cell number 3. {w=2.0} {nw}"
            
            $ startpos = 1   

            
        if exitpos == 2:
            if startpos == 2:
                m "This is a table.{w=2.0} {nw}"
                call dialog_nothing from _call_dialog_nothing_20
            $ startpos = 2

            
        if exitpos == 3: 
            if startpos == 3:
                m "This is a bed.{w=2.0} {nw}"
                call dialog_nothing from _call_dialog_nothing_21
            $ startpos = 3

            
        if exitpos == 4:
            if startpos == 4:
                m "This is the sink and the toilet.{w=2.0} {nw}"
                call dialog_nothing from _call_dialog_nothing_22
            $ startpos = 4

            

        #exits routing "got to map and set position for next map"
        if exitpos == 11:       
            $ startpos = 11        
 
            
        if exitpos == 22:
            $ startpos = 22
            call dialog_closed from _call_dialog_closed_7
            


            
        if exitpos == 33:
            call sound_screw from _call_sound_screw_2
            $ startpos = 3
            jump megaship_aeration
            $ startpos = 33

            
        if exitpos == 44:
            $ startpos = 44

