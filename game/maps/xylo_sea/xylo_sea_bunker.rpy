# MAPS

############################################

# go level -2, get key
# go level -1, use key with lift control
# send lift to -2
# go to lift, lift cabin is not there
# use rope and come to next secret room
# in this room find button "unlock secret level -3"
# go bak to room -2
# call lift
# go to level -3


init:
    $ xylo_bunker_lift_level = 0
    $ xylo_bunker_lift_level0 = False
    $ xylo_bunker_lift_level1 = False
    $ xylo_bunker_lift_level2 = False
    
    $ xylo_bunker_lift_control_broken = True


screen xylo_sea_bunker_lift_control() zorder -999:
    
    on "show" action SetVariable("pnc_nodes_visible", False)
    on "hide" action SetVariable("pnc_nodes_visible", True)
    
    add "#112119"
    
    imagebutton: 
        idle "images/maps/bg.png" 
        action Hide("xylo_sea_bunker_lift_control")
            
    add "inventory/inventory.png"
    
    vbox xalign 0.5 yalign 0.5:
        hbox xalign 0.5:
            imagebutton: 
                auto "images/buttonbig_%s.png"
                action SetVariable("xylo_bunker_lift_level", 0), Jump("xylo_bunker_move_lift") at center
            null width 20
            label "00":
                yanchor 0.5
                ypos 0.5
            
        hbox xalign 0.5:
            imagebutton: 
                auto "images/buttonbig_%s.png"
                action SetVariable("xylo_bunker_lift_level", 1), Jump("xylo_bunker_move_lift") at center
            null width 20
            label "-01":
                yanchor 0.5
                ypos 0.5

        hbox xalign 0.5:
            imagebutton: 
                auto "images/buttonbig_%s.png"
                action SetVariable("xylo_bunker_lift_level", 2), Jump("xylo_bunker_move_lift") at center
            null width 20
            label "-02":
                yanchor 0.5
                ypos 0.5
    
    if shadow_enable == 1:
        add "images/shadow.png" align (0.5,0.5)



label xylo_bunker_move_lift:
    
    if xylo_bunker_lift_control_broken == True and liftpos == 2:
        call sound_electroshock from _call_sound_electroshock_3
        $ xylo_bunker_lift_level = 1
        with hpunch
        hide screen xylo_sea_bunker_lift_control
        m "I looks like this control panel is not working! {w=2.0} {nw}"
        m "I see a broken cable outside the panel... {w=2.0} {nw}"
        if "cable" not in inventory:
            m "If I could find a piece of cable somewhere, I could fix it easily! {w=3.5} {nw}"
        jump loop_xylo_sea_bunker
    
    
    else:
        call sound_lift from _call_sound_lift
        pause 3.75
        
        hide screen xylo_sea_bunker_lift_control
        jump loop_xylo_sea_bunker
    
    
    

# bunker map

label xylo_sea_bunker:
    
    image xylo_sea_bunker = imagemapsdir + "crossroom.png"
    
    scene bgcolor
    show xylo_sea_bunker at truecenter
    
    $ liftlevelname = liftlevel[liftpos]
    
    #$ xylo_bunker_lift_level = liftlevel[liftpos]
    
    show screen notify("Bunker level [liftlevelname]")
    
    
    #doors (comment to disable)
    show doorh as doorA:
        pos (400, 55)
    #show doorv as doorB:
    #    pos (587, 240)
    #show doorh as doorC:
    #    pos (400, 427)
    #show doorv as doorD:
    #    pos (215, 240)
    
    show warningfloor:
        anchor (0.5,0.5)
        pos (400,140)
    
    show buttonscreen:
        pos (300,55)
        
    show buttonscreen as buttonscreen2:
        pos (500,55)
        
    
    show text "{color=#8dd35f}{size=+140}[liftlevelname]{/size}{/color}" as text2:
        anchor (0.0,0.0)
        pos (220,230)
        alpha 0.05
        
        
    if liftpos == 1:  # level -2
        show box:
            pos (260,240)
            

    
    
    # set all variables for the map (nodes and path)
    $ nodeA = (400, 78)
    $ nodeB = (500, 78)
    $ nodeC = (400, 410)
    $ nodeD = (300, 78)
    

    $ nodeAA = (400, 200)
    $ nodeBB = (-100, -100)
    $ nodeCC = (-100, -100)
    $ nodeDD = (-100, -100)

    $ pathA = (nodeA, nodeB, (0, 0), nodeD, nodeAA, (0, 0), (0, 0), (0, 0))
    $ pathB = (nodeA, nodeB, (0, 0), nodeD, nodeAA, (0, 0), (0, 0), (0, 0))
    $ pathC = (nodeA, nodeB, (0, 0), nodeD, nodeAA, (0, 0), (0, 0), (0, 0))
    $ pathD = (nodeA, nodeB, (0, 0), nodeD, nodeAA, (0, 0), (0, 0), (0, 0))
     
    $ pathAA = (nodeA, nodeB, (0, 0), nodeD, nodeAA, (0, 0), (0, 0), (0, 0))
    $ pathBB = (nodeA, nodeB, (0, 0), nodeD, nodeAA, nodeBB, nodeCC, nodeDD)
    $ pathCC = (nodeA, nodeB, (0, 0), nodeD, nodeAA, nodeBB, nodeCC, nodeDD)
    $ pathDD = (nodeA, nodeB, (0, 0), nodeD, nodeAA, nodeBB, nodeCC, nodeDD)
    
    


label loop_xylo_sea_bunker:
    
    while True:

        # start "move through the map" loop
        call startpos from _call_startpos_12

        # do something at node?
        if exitpos == 1:
            $ startpos = 1
            
            hide text2
            call sound_door from _call_sound_door_26
            
            if liftpos == 2:                        # -01
                if xylo_bunker_lift_level == 1:
                    jump xylo_sea_bunker_lift1
                else:
                    $ startpos = 44
                    jump xylo_sea_bunker_liftmap

            if liftpos == 1:                        # -02
                if xylo_bunker_lift_level == 2:
                    jump xylo_sea_bunker_lift1
                else:
                    $ startpos = 44
                    jump xylo_sea_bunker_liftmap

            
        
        
        if exitpos == 2:
            if startpos == 2:
                if xylo_bunker_lift_control_broken == True and inventory_select == "cable":
                    
                    call sound_electroshock from _call_sound_electroshock_4
                    call use_item from _call_use_item
                    m "I can try to fix it with this cable. {w=2} {nw}"
                    
                    #with flash
                    $ xylo_bunker_lift_control_broken = False
                    show screen xylo_sea_bunker_lift_control
                    m "Yes, it works! {w=2} {nw}"
                
                show screen xylo_sea_bunker_lift_control # lift control
            
            $ startpos = 2

            
        if exitpos == 3:
            $ startpos = 3

            
        if exitpos == 4:
            if startpos == 4:
               call xylo_sea_bunker_level_info from _call_xylo_sea_bunker_level_info
            $ startpos = 4


        #exits routing "got to map and set position for next map"
        if exitpos == 11:  
            
            if startpos == 11:
                m "I'm at level [liftlevelname]. {w=2} {nw}"
                if liftpos == 2:
                    m "Except a lift control panel and an info board, there is absolutely nothing in this room! {w=6} {nw}"
                    m "This is quite strange... {w=1.5} {nw}"
                    
                if liftpos == 1:
                    call dialog_nothing from _call_dialog_nothing_14

             
            $ startpos = 11     
 
            
        if exitpos == 22:
            $ startpos = 22

            
        if exitpos == 33:
            $ startpos = 33

            
        if exitpos == 44:
            $ startpos = 44



label xylo_sea_bunker_level_info:
    
    $ info_panel_symbol = "exit"
    $ showtext = """
    
    
- A.R.K. Corporation -


Level [liftlevelname]

Emergency Exit
    """
    
    call info_panel from _call_info_panel # in animations

    return
