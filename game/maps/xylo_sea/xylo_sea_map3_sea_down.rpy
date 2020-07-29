
###########################################
label xylo_map3:
    
    call atmo_sea from _call_atmo_sea
    
    image xylo_map3 = imagemapsdir + "xylo_sea_p3.png"
    
    scene bgcolor
    show screen notify("sea colony coast")
    
    show xylo_map3
    show waves behind xylo_map3


    
    # set all variables for the map (nodes and path)
    $ nodeA = (300,150)
    $ nodeB = (520,130)
    $ nodeC = (662,250)
    $ nodeD = (540,360)
    
    $ nodeAA = (260,40)
    $ nodeBB = (780,240)
    $ nodeCC = (400,460)
    $ nodeDD = (40,350)
    
    $ pathA = (nodeA, nodeB, (0,0), (0,0), nodeAA, (0,0), (0,0), (0,0))
    $ pathB = (nodeA, nodeB, nodeC, (0,0), (0,0), (0,0), (0,0), (0,0))
    $ pathC = ((0,0), nodeB, nodeC, nodeD, (0,0),(0,0),(0,0), (0,0))
    $ pathD = ((0,0), (0,0), nodeC, nodeD, (0,0), (0,0), (0,0), nodeDD)
    
    $ pathAA = (nodeA, (0,0), (0,0), (0,0), nodeAA, (0,0), (0,0), (0,0))
    $ pathBB = ((0,0), nodeB, (0,0), (0,0), (0,0), (0,0), (0,0), (0,0))
    $ pathCC = ((0,0), (0,0), nodeC, (0,0), (0,0), (0,0), (0,0), (0,0))
    $ pathDD = ((0,0), (0,0), (0,0), nodeD, (0,0), (0,0), (0,0), nodeDD)

label loop_xylo_map3:

    # start "move through the map" loop
    call startpos from _call_startpos_47
    
    # do something at node?
    if exitpos == 1:       #if at node A
        $ startpos = 1     # stay in A
        jump loop_xylo_map3          # map to jump to
        
    if exitpos == 2:
        if startpos == 2:
            m "This way is very interesting! {w=3.0} {nw}"
        $ startpos = 2
        jump loop_xylo_map3
        
    if exitpos == 3:
        if startpos == 3:
            if inventory_select == "":
                m "There is an info board. {w=2.0} {nw}"
            call xylo_sea_map3_info from _call_xylo_sea_map3_info

        $ startpos = 3
        jump loop_xylo_map3
        
    if exitpos == 4:
        $ startpos = 4
        jump loop_xylo_map3 
    
    #exits routing "got to map"
    if exitpos == 11:    #if going out at AA
        $ startpos = 33    #go to CC
        jump xylo_map2           # map to jump to
        
    if exitpos == 22:
        $ startpos = 44
        jump xylo_map2
        
    if exitpos == 33:
        $ startpos = 11
        jump xylo_map2
        
    if exitpos == 44:
        $ startpos = 22
        jump xylo_map4
        



label xylo_sea_map3_info:
    
    $ info_panel_symbol = ""
    $ showtext = """
- Sea View Boat Company -


If you are interested for a boat trip, 

please call 05060708.

Just type our phone number in the terminal,

we will be happy to give you more info.


    """
    
    call info_panel from _call_info_panel_9
    
    call add_note("xylo sea boat company number: 05060708") from _call_add_note_9
    
    return
