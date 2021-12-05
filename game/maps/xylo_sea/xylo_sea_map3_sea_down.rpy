


###########################################
label xylo_map3:
    
    call atmo_sea from _call_atmo_sea
    stop atmo2
    
    image xylo_map3 = imagemapsdir + "xylo_sea_p3.png"
    
    scene bgcolor
    show screen notify("Pier")
    
    show xylo_map3
    show waves behind xylo_map3
    
    $ inventory_button = True
    


    if xylo_boat_trip == True:
        if planet == "xylo":
            show boat:
                pos (546,420)
                rotate 90
        else:
            if shadow_enable == 1:
                show shadow:
                    pos (546,420)
            
            show boat:
                pos (300,550)
                rotate 0
                easein 3 pos (546,420) rotate 90
            
            call sound_propulsion from _call_sound_propulsion_1
            pause 3
            call sound_door from _call_sound_door_79
            show boat:
                pos (546,420) 
                rotate 90
            
    
    # reset planet and spaceship to xylo
    $ planet = "xylo"
    $ spaceshiptype = spaceshiptype_bak
    #"[spaceshiptype]"

    
    
    
    # set all variables for the map (nodes and path)
    $ nodeA = (300,150)
    $ nodeB = (520,130)
    $ nodeC = (662,250)
    $ nodeD = (540,360)
    
    $ nodeAA = (260,40)
    $ nodeBB = (538, 417)
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
        if startpos == 1:
            m "Somehow, I like this coastal road. {w=3} {nw}"
        $ startpos = 1     # stay in A
        jump loop_xylo_map3          # map to jump to
        
    if exitpos == 2:
        if startpos == 2:
            m "This way is very interesting... {w=3.0} {nw}"
            m "Why is it like this? {w=3.0} {nw}"
        $ startpos = 2
        jump loop_xylo_map3
        
    if exitpos == 3:
        if startpos == 3:
            if inventory_select == "":
                #m "There is an info board. {w=2.0} {nw}"
                call xylo_sea_map3_info from _call_xylo_sea_map3_info
            else:
                call dialog_nosense from _call_dialog_nosense_44
            

        $ startpos = 3
        jump loop_xylo_map3
        
    if exitpos == 4:
        if startpos == 4:
            
            
            
            if xylo_boat_trip == False:
                m "The view is quite nice here. {w=3} {nw}"
            
            
            
            else:
                $ planet = "xylo_sea"
                $ shippos = (0,800)
                $ spaceshiptype_bak = spaceshiptype
                $ spaceshiptype = "boat"
                
                call sound_door from _call_sound_door_104
                hide player
                pause 0.5
                
                #call sound_propulsion
                call sound_boat_start from _call_sound_boat_start
                pause 1
                show boat:
                    pos (546,420)
                    rotate 90
                    easeout 3 pos (1000,420)
                
                pause 3
                
                $ direction = 90
                jump surface_xylo_sea
                
                m "This boat looks great. {w=3} {nw}"
                m "I'd love to use it! {w=3} {nw}"
           
            
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
    
    $ info_panel_symbol = "boat"
    $ showtext = """
    
    
- Sea View Boat Rental Company -


If you are interested in a boat trip, 
please call 05060708.

Just type our phone number in the terminal,
we will be happy to give you more information.

    """
    
    call info_panel from _call_info_panel_9
    
    call add_note("Boat Rental Company number: 05060708") from _call_add_note_9
    
    return
