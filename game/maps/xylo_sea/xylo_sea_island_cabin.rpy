# MAPS

############################################

init:
    $ xylo_lighthouse_inverted = False



# island cabin
label xylo_island_cabin:
    
    stop atmo
    # but keep atmo2 playing
   
    image xylo_island_cabin = imagemapsdir + "crossroom.png"
    
    scene bgcolor
    show xylo_island_cabin at truecenter

    show screen notify("Cabin")

    
    show box:
        pos (270, 110)
        
    show box as box2: #down left
        pos (270, 370)
        
    show box as box3: #down right
        pos (530, 325)
    
    
    
    show batterydry:
        pos (440, 67)
        zoom 0.3
        
    show batterydry as bd2:
        pos (460, 67)
        zoom 0.3
        
    show batterydry as bd3:
        pos (480, 67)
        zoom 0.3

    
    
    #doors (comment to disable)
    #show doorh as doorA:
    #    pos (500, 53)
    #show doorv as doorB:
    #    pos (587, 240)
    show doorh as doorC:
        pos (400, 427)
    #show doorv as doorD:
    #    pos (213, 240)
    
   
    
    show buttonscreen: #right
        pos (586, 240)
        rotate 90
        


    # set all variables for the map (nodes and path)
    $ nodeA = (459, 95)
    $ nodeB = (560, 240)
    $ nodeC = (400, 402)
    $ nodeD = (273, 301)
    

    $ nodeAA = (400, 240)
    $ nodeBB = (305, 178)
    $ nodeCC = (-100, -100)
    $ nodeDD = (-100, -100)

    $ pathA = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, (0, 0))
    $ pathB = (nodeA, nodeB, (0, 0), nodeD, nodeAA, nodeBB, nodeCC, (0, 0))
    $ pathC = (nodeA, (0, 0), nodeC, (0, 0), nodeAA, nodeBB, nodeCC, (0, 0))
    $ pathD = (nodeA, nodeB, (0, 0), nodeD, nodeAA, nodeBB, nodeCC, (0, 0))
     
    $ pathAA = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, (0, 0))
    $ pathBB = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, (0, 0))
    $ pathCC = (nodeA, nodeB, nodeC, nodeD, nodeAA, (0, 0), nodeCC, (0, 0))
    $ pathDD = (nodeA, nodeB, (0, 0), nodeD, nodeAA, nodeBB, nodeCC, nodeDD)
    
    




label loop_xylo_island_cabin:
    
    while True:

        # start "move through the map" loop
        call startpos from _call_startpos_93

        # do something at node?
        if exitpos == 1:
            if startpos == 1:
                if inventory_select == "":
                    m "I already fixed the boat.{w=2} {nw}"
                    m "I rather leave these batteries here for the next emergency.{w=4} {nw}"
                else:
                    call dialog_nosense from _call_dialog_nosense_76  
                
            $ startpos = 1
            
        
        if exitpos == 2:
            if startpos == 2:
                show screen xylo_island_cabin_screen
            $ startpos = 2

            
        if exitpos == 3:
            $ startpos = 11
            call sound_door from _call_sound_door_111
            jump xylo_sea_island2
            $ startpos = 3

            
        if exitpos == 4: # gem
            if startpos == 4:
                if inventory_select == "":
                    if xylo_island_cabin_gem == True:
                        call take_gem from _call_take_gem_15
                        $ xylo_island_cabin_gem = False
                    else:
                        m "This is another wooden box.{w=2} {nw}"
                        call dialog_nothing from _call_dialog_nothing_46
                
                elif inventory_select == "lighter":
                    m "One should't play with fire. {w=3} {nw}"
                    
                elif inventory_select == "screwdriver":
                    m "I really have better to do than opening this box! {w=3.5} {nw}"
                
                else:
                    call dialog_nosense from _call_dialog_nosense_77        
                

            $ startpos = 4



        if exitpos == 11:  
            if startpos == 11:
                m "Nice cabin.{w=2} {nw}"
            $ startpos = 11     
 
            
        if exitpos == 22: # coins
            if startpos == 22:
                if inventory_select == "":
                    if cash_xylo_sea_cabin > 0:
                        m "There are some coins on the floor.{w=3} {nw}"
                        call io_cash(cash_xylo_sea_cabin) from _call_io_cash_27
                        $ cash_xylo_sea_cabin = 0
                    else:
                        m "This is wooden box.{w=2} {nw}"
                        call dialog_nothing from _call_dialog_nothing_73
                
                elif inventory_select == "lighter":
                    m "I don't want to set fire! {w=3} {nw}"
                
                elif inventory_select == "screwdriver":
                    m "This box looks empty, this would be a waste of time! {w=3.5} {nw}"
                
                else:
                    call dialog_nosense from _call_dialog_nosense_78  
                
            $ startpos = 22

            
        if exitpos == 33:
            $ startpos = 33

            
        if exitpos == 44:
            $ startpos = 44




#button screen
screen xylo_island_cabin_screen() zorder -999:
    #add "#112119"
    
    on "show" action SetVariable("pnc_nodes_visible", False)
    on "hide" action SetVariable("pnc_nodes_visible", True)
    
    imagebutton: 
        idle "images/maps/bg.png" 
        action [Hide("xylo_island_cabin_screen"), Jump("xylo_island_cabin")]
            
    add "inventory/inventory.png"

    hbox xalign 0.5 yalign 0.5:
        vbox xalign 0.5:
            
            label "Lighthouse rotation" at center
            null height 10
            imagebutton at center:
                auto "images/buttonbig_%s.png" 
                action [ToggleVariable("xylo_lighthouse_inverted"), Play("sound", "sounds/collect.ogg")]
            null height 10
            label "Invert" at center
            
        
            
    if shadow_enable == 1:
        add "images/shadow.png" align (0.5,0.5)
