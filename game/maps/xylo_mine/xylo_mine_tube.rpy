# MAPS

############################################

    

label xylo_mine_tube:
    
    image crossroomsmall = imagemapsdir + "crossroomsmall.png"
    
    scene bgcolor
    show crossroomsmall at truecenter
    show screen notify("aeration")
    

    hide tube
    show tube:
        rotate 90
        pos (400, 832)
        

    $ landing = False
     
        
    #show buttonscreen:
    #    pos (400, 147)
    
    
    # set all variables for the map (nodes and path)
    $ nodeA = (400, 160)
    $ nodeB = (480, 240)
    $ nodeC = (400, 320)
    $ nodeD = (320, 240)
    

    $ nodeAA = (400, 240)
    $ nodeBB = (-100, -100)
    $ nodeCC = (-100, -100)
    $ nodeDD = (-100, -100)

    $ pathA = (nodeA, nodeB, nodeC, nodeD, (0, 0), (0, 0), (0, 0), (0, 0))
    $ pathB = (nodeA, nodeB, nodeC, nodeD, (0, 0), (0, 0), (0, 0), (0, 0))
    $ pathC = (nodeA, nodeB, nodeC, nodeD, (0, 0), (0, 0), (0, 0), (0, 0))
    $ pathD = (nodeA, nodeB, nodeC, nodeD, (0, 0), (0, 0), (0, 0), (0, 0))
     
    $ pathAA = (nodeA, nodeB, nodeC, nodeD, (0, 0), (0, 0), (0, 0), (0, 0))
    $ pathBB = (nodeA, nodeB, nodeC, nodeD, (0, 0), (0, 0), (0, 0), (0, 0))
    $ pathCC = (nodeA, nodeB, nodeC, nodeD, (0, 0), (0, 0), (0, 0), (0, 0))
    $ pathDD = (nodeA, nodeB, nodeC, nodeD, (0, 0), (0, 0), (0, 0), (0, 0))
    
    
    show minidroid:
        pos (400,450)
        linear 2 pos nodeC
    
    if shadow_enable == 1:
        show shadow:
            pos (400,450)
            linear 2 pos nodeC
            
    pause 2
    
    hide minidroid
    
    $ playertype = "minidroid"
    



label loop_xylo_mine_tube:

    while True:

        # start "move through the map" loop
        call startpos from _call_startpos_59
        

        # do something at node?
        if exitpos == 1:
            if startpos == 1:
                if xylo_mine_tube_gem == True:
                    #md "Analyzing.{w=1}.{w=1}.{w=1}.{w=1}.{w=1}.{w=1} {nw}"
                    #md "Gem found. {w=2} {nw}"
                    call take_gem from _call_take_gem_6
                    $ xylo_mine_tube_gem = False
                else:
                    call dialog_nothing from _call_dialog_nothing_36
                    
            $ startpos = 1 

            
        if exitpos == 2:
            if startpos == 2:
                if xylo_mine_tube_cash2 > 0:
                    md "There are some coins. {w=2} {nw}"
                    call io_cash(xylo_mine_tube_cash2) from _call_io_cash_15
                    $ xylo_mine_tube_cash2 = 0
                else:
                    call dialog_nothing from _call_dialog_nothing_37
            $ startpos = 2
            

        if exitpos == 3:
            if startpos == 3:
                hide player
                show minidroid:
                    pos nodeC
                    linear 2 pos (400, 480)
                pause 2
                $ playertype = "player"
                #hide minidroid
                #hide playercross
                
                $ startpos = 1
                jump xylo_mine
            
            $ startpos = 3

            
            
            
        if exitpos == 4:
            if startpos == 4:
                if xylo_mine_tube_cash > 0:
                    md "There are some coins. {w=2} {nw}"
                    call io_cash(xylo_mine_tube_cash) from _call_io_cash_16
                    $ xylo_mine_tube_cash = 0
                else:
                    call dialog_nothing from _call_dialog_nothing_38
            $ startpos = 4


        #######
        
        if exitpos == 11:
            $ startpos = 11
 
            
        if exitpos == 22:
            $ startpos = 22

            
        if exitpos == 33:
            $ startpos = 33

            
        if exitpos == 44:
            $ startpos = 44









