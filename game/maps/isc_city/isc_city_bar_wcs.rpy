# MAPS

############################################


init:
    $ isc_wc = 1
    




    

label isc_city_bar_wcs:
    
    image crossroomsmall = imagemapsdir + "crossroomsmall.png"
    
    scene bgcolor
    show crossroomsmall at truecenter
    show screen notify("wc")
    
    image wc = "/images/wc.png"
    
    
    if isc_wc == 2:
        show puddle:
            anchor (0.5,0.5)
            pos (460, 260)
            rotate 270
            alpha 0.2
            
    
    if isc_wc == 3:
        show puddle:
            anchor (0.5,0.5)
            pos (400, 190)
            rotate 180
            alpha 0.2
            

        
        
    show wc:
        anchor (0.5,0.5)
        pos (400, 170)
        
        
    show doorh:
        pos (400,334)
        

    # set all variables for the map (nodes and path)
    $ nodeA = (400, 210)
    $ nodeB = (460, 265)
    $ nodeC = (400, 312)
    $ nodeD = (320, 240)
    

    $ nodeAA = (400, 240)
    $ nodeBB = (-100, -100)
    $ nodeCC = (-100, -100)
    $ nodeDD = (-100, -100)

    $ pathA = (nodeA, (0, 0), nodeC, (0, 0), (0, 0), (0, 0), (0, 0), (0, 0))
    $ pathB = (nodeA, (0, 0), nodeC, (0, 0), (0, 0), (0, 0), (0, 0), (0, 0))
    $ pathC = (nodeA, (0, 0), nodeC, (0, 0), (0, 0), (0, 0), (0, 0), (0, 0))
    $ pathD = (nodeA, nodeB, nodeC, nodeD, (0, 0), (0, 0), (0, 0), (0, 0))
     
    $ pathAA = (nodeA, nodeB, nodeC, nodeD, (0, 0), (0, 0), (0, 0), (0, 0))
    $ pathBB = (nodeA, nodeB, nodeC, nodeD, (0, 0), (0, 0), (0, 0), (0, 0))
    $ pathCC = (nodeA, nodeB, nodeC, nodeD, (0, 0), (0, 0), (0, 0), (0, 0))
    $ pathDD = (nodeA, nodeB, nodeC, nodeD, (0, 0), (0, 0), (0, 0), (0, 0))
    
    if isc_wc == 2:
        $ pathA = (nodeA, nodeB, nodeC, (0, 0), (0, 0), (0, 0), (0, 0), (0, 0))
        $ pathB = (nodeA, nodeB, nodeC, (0, 0), (0, 0), (0, 0), (0, 0), (0, 0))
        $ pathC = (nodeA, nodeB, nodeC, (0, 0), (0, 0), (0, 0), (0, 0), (0, 0))
    
    
    #"wc no: [isc_wc]"
    

label loop_isc_city_bar_wcs:

    while True:

        # start "move through the map" loop
        call startpos from _call_startpos_65
        

        # do something at node?
        if exitpos == 1:
            if startpos == 1:
                if isc_wc == 1:
                    menu:
                        "flush":
                            call sound_flush from _call_sound_flush
                            pause 5
                            m "It looks better now! {w=2} {nw}"
                            if isc_bar_wc_cash > 0:
                                m "There are some coins! {w=2} {nw}"
                                call io_cash(isc_bar_wc_cash) from _call_io_cash_17
                                $ isc_bar_wc_cash = 0
                            #else:
                            #    call dialog_nothing
                        "do nothing":
                            pass
                if isc_wc == 2:
                    menu:
                        "flush":
                            call sound_flush from _call_sound_flush_1
                            pause 5
                            m "It looks better now! {w=2} {nw}"
                            call dialog_nothing from _call_dialog_nothing_39
                        "do nothing":
                            pass
                if isc_wc == 3:
                    menu:
                        "flush":
                            call sound_flush from _call_sound_flush_2
                            pause 5
                            m "It looks better now! {w=2} {nw}"
                            if isc_bar_wc_gem== True:
                                call take_gem from _call_take_gem_7
                                $ isc_bar_wc_gem = False
                            else:
                                call dialog_nothing from _call_dialog_nothing_40
                        "do nothing":
                            pass
                    
                            
            $ startpos = 1 

            
        if exitpos == 2:
            if startpos == 2:
                m "There is some liquid on the floor... {w=2.5} {nw}"
                m "This is disgusting! {w=1.5} {nw}"
            $ startpos = 2
            

        # wc door out
        if exitpos == 3:
            
            if isc_wc == 1:
                #"[isc_wc]"
                $ startpos = 2
            
            if isc_wc == 2:
                #"[isc_wc]"
                $ startpos = 3
            
            if isc_wc == 3:
                #"[isc_wc]"
                $ startpos = 4
            
            call sound_door from _call_sound_door_141
            jump isc_city_bar_toilets
            


            
        if exitpos == 4:
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









