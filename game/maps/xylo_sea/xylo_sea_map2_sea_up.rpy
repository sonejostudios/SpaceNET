  
##################################


label xylo_map2:
    
    call atmo_sea from _call_atmo_sea_1

    image xylo_map2 = imagemapsdir + "xylo_sea_p2.png"
    
    scene bgcolor
    show screen notify("Xylo sea coast")
    
    show xylo_map2

    image waves = SnowBlossom("images/wave.png", count=100, border=50, xspeed=(5), yspeed=(5), start=0, fast=True, horizontal=True)
    show waves behind xylo_map2
    
    
    image rope_sea = "inventory/rope_idle.png"
    
    if "rope" not in inventory and xylo_sea_bunker_rope == False:
        show rope_sea:
            pos (270, 316)
            zoom 0.4
    
    
    
    
    
    # set all variables for the map (nodes and path)
    $ nodeA = (400,150)
    $ nodeB = (550,240)
    $ nodeC = (260,330)
    $ nodeD = (170,170)
    
    $ nodeAA = (400,25)
    $ nodeBB = (780,240)
    $ nodeCC = (270,440)
    $ nodeDD = (40,140)
    
    $ pathA = ((0,0), (0,0), (0,0), (0,0), nodeAA, (0,0), (0,0), (0,0))
    $ pathB = (nodeA, (0,0), nodeC, nodeD, (0,0), nodeBB, (0,0), (0,0))
    $ pathC = ((0,0), (0,0), nodeC, nodeD, (0,0),(0,0),nodeCC, (0,0))
    $ pathD = ((0,0), (0,0), nodeC, nodeD, (0,0), (0,0), (0,0), nodeDD)
    
    $ pathAA = (nodeA, (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0))
    $ pathBB = ((0,0), nodeB, (0,0), (0,0), (0,0), (0,0), (0,0), (0,0))
    $ pathCC = ((0,0), (0,0), nodeC, (0,0), (0,0), (0,0), nodeCC, (0,0))
    $ pathDD = ((0,0), (0,0), (0,0), nodeD, (0,0), (0,0), (0,0), nodeDD)


label loop_xylo_map2:

    
    while True:
        # start "move through the map" loop
        call startpos from _call_startpos_70
        
        # do something at node?
        if exitpos == 1:       #if at node A
            $ startpos = 1     # stay in A

            
        if exitpos == 2:
            $ startpos = 2

            
        if exitpos == 3: # rope
            if startpos == 3:
                if "rope" not in inventory and xylo_sea_bunker_rope == False:
                    
                    if inventory_select == "knife":
                        call use_and_keep_item from _call_use_and_keep_item_26
                        m "Let's take a piece of this rope.{w=3.0} {nw}"
                        call take_item("rope") from _call_take_item_17
                        
                        if inventory_notify == "rope":
                            hide rope_sea
                    
                    elif inventory_select == "":
                        m "There is a rope on the floor.{w=2.0} {nw}"
                        m "It is tied to the pier.{w=2.0} {nw}"
                        
                    else:
                        call dialog_nosense from _call_dialog_nosense_16
                        
                    
                    
                else:
                    call dialog_nothing from _call_dialog_nothing_45
                
            $ startpos = 3

            
        if exitpos == 4:
            
            if startpos == 4:
                if cash_xylo_sea_map2 > 0:
                    m "There is some money on the ground... {w=2.0} {nw}"
                    call io_cash(cash_xylo_sea_map2) from _call_io_cash_19
                    $ cash_xylo_sea_map2 = 0
                    
                else:
                    call dialog_nothing from _call_dialog_nothing_46
            
            $ startpos = 4

        
        #exits routing "got to map"
        if exitpos == 11:       #if going out at AA
            $ startpos = 11     #go to CC

            
        if exitpos == 22:
            $ startpos = 22

            
        if exitpos == 33:
            $ startpos = 11
            jump xylo_map3
            
        if exitpos == 44:
            $ startpos = 22
            jump xylo_map1
    


