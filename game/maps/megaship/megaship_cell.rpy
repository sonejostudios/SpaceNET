# MAPS

init:
    $ m_megaship_cell_escape = 0
    $ m_megaship_cell_first_talk = 0
    
    $ m_megaship_cell_door = 0
    
    default megaship_cell_door_radio = [0, 0, 0]
    
    
screen dev_puddle():
    text "[m_megaship_cell_escape]" at truecenter


############################################
label megaship_cell:
    
    call atmo_spaceship_hum from _call_atmo_spaceship_hum_2
    
    #show screen dev_puddle
    
    image megaship_cell = imagemapsdir + "megaship_cell.png"
    
    $ pnc_nodes_visible = True
    
    
    if pnc_cursor == True:
        $ change_cursor(type="pnc")
    
    
    if in_intro == True:
        scene megaship_cell
        with pixellate
        $ in_intro = False
    else:
        scene megaship_cell
    
    
    show screen notify("prison cell 1")
    
    show bgcolor behind megaship_cell    
    
    
    image sink = "/images/sink.png"
    show sink:
        anchor (0.5,0.5)
        pos (200, 340)
        
    show wc:
        anchor (0.5,0.5)
        rotate 180
        pos (150,330)
        
    image puddle = "/images/puddle.png"
    
    if m_megaship_cell_escape > 0:
        show puddle behind sink, wc:
            anchor (0.5,0.5)
            pos (200, 325)
            alpha 0.2
    
    
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


label loop_megaship_cell:
    
    
    while True:
        # start "move through the map" loop
        call startpos from _call_startpos_19

        # do something at node?
        if exitpos == 1:
            if startpos == 1:
                if m_megaship_cell_escape < 4 and m_megaship_cell_first_talk == 0:
                    m "I'm in prison! {w=2.0} {nw}"
                    m "And I don't remember anything... {w=2.5} {nw}"
                    m "Except my name, [playername]... {w=2.5} {nw}"
                    m "And another name: SpaceNET... {w=3.5} {nw}"
                    m "But what does it mean?... {w=2.5} {nw}"
                    m "SpaceNET... {w=2.5} {nw}"
                    m "And what to do now? {w=2.5} {nw}"
                    $ m_megaship_cell_first_talk = 1
                else:
                    m "I'm in cell number 1. {w=2.0} {nw}"
                    
            $ startpos = 1   

            
        if exitpos == 2:
            if startpos == 2:
                if inventory_select == "newspaper":
                    m "I just took this newspaper from the table.{w=2.5} {nw}"
                    m "Why should I put it back?{w=2.5} {nw}"
                    #call dialog_nosense
                    
                elif inventory_select == "screwdriver":
                    call dialog_nosense from _call_dialog_nosense_26
                
                else:
                    m "This is a table.{w=2.0} {nw}"
                    
                    if "newspaper" not in inventory:
                        m "There is a newspaper.{w=2.0} {nw}"
                        call take_item("newspaper") from _call_take_item_10
                
            $ startpos = 2

            
        if exitpos == 3: 
            if startpos == 3:
                if inventory_select == "newspaper":
                    m "I don't think it's a good idea to lie down and read a newspaper now.{w=4} {nw}"
                    #call dialog_nosense
                    
                elif inventory_select == "screwdriver":
                    call dialog_nosense from _call_dialog_nosense_27
                    
                else:
                    m "This is a bed.{w=2.0} {nw}"
            $ startpos = 3

            
        if exitpos == 4:
            if startpos == 4:
                
                if inventory_select != "newspaper":
                    if inventory_select == "screwdriver":
                        m "I don't want to repair it now.{w=2.0} {nw}"
                    else:
                        m "This is the sink and the toilet.{w=2.0} {nw}"
                    
                if m_megaship_cell_escape == 1:
                    m "It is completely flooded and doesn't work anymore.{w=3.0} {nw}"
                
                if inventory_select == "newspaper" and m_megaship_cell_escape == 0:
                    
                    menu:
                        "Use newspaper with sink":
                            call use_and_keep_item from _call_use_and_keep_item_7
                            call sound_paper from _call_sound_paper
                            #with flash
                            m "Now the sink is blocked.{w=2.0} {nw}"
                            m "What will happen if I open the tap?{w=2.0} {nw}"
                            
                            call sound_tap from _call_sound_tap_1
                            show puddle behind sink:
                                anchor (0.5,0.5)
                                alpha 0.0
                                pos (200, 325)
                                linear 2 alpha 0.2
                            
                            $ m_megaship_cell_escape = 1
                            

                            pass
                        
                        "Back":
                            pass
                            
                if m_megaship_cell_escape == 2:
                    m "The repair-robot is working.{w=2.0} {nw}"
                    m "There is a screw driver...{w=2.0} {nw}"
                    m "I could take it... {w=2.0} {nw}"
                    
                    call take_item("screwdriver") from _call_take_item_11
                    
                    if "screwdriver" in inventory:
                        $ m_megaship_cell_escape = 3
                        call megaship_cell_robot_back from _call_megaship_cell_robot_back
                        pass
                        
                if inventory_select == "newspaper" and m_megaship_cell_escape >= 2:
                    m "The sink is already blocked.{w=2.0} {nw}"

            $ startpos = 4

            

        #exits routing "got to map and set position for next map"
        if exitpos == 11:       
            $ startpos = 11        
 
            
        if exitpos == 22:
            if startpos == 22:
                if inventory_select == "newspaper":
                    #call dialog_nosense
                    m "This idea is useless.{w=2} {nw}"
                    m "I can't open a door with a newspaper!{w=3.5} {nw}"
                
                elif inventory_select == "screwdriver":
                    call dialog_nosense from _call_dialog_nosense_28
                
                else:
                    if m_megaship_cell_door == 0:
                        m "This is the prison cell door.{w=3} {nw}"
                        call dialog_closed from _call_dialog_closed_8
                        m "But there is an intercom device.{w=3} {nw}"
                        $ m_megaship_cell_door = 1
                    
                    radio "What do you want, prisoner?{w=3.0} {nw}"
                    
                    menu:
                        "The sink is broken" if m_megaship_cell_escape == 1:
                            m "The sink is broken.{w=2.0} {nw}"
                            radio "Okay, i'll send a repair-robot to your cell.{w=3.0} {nw}"
                            call megaship_cell_robot from _call_megaship_cell_robot
                        
                        "I've found a newspaper" if "newspaper" in inventory and megaship_cell_door_radio != [1,1,1]:
                            m "I've found a newspaper.{w=2} {nw}"
                            radio "Good for you.{w=2.0} {nw}"
                            radio "I hope it's interesting!{w=2.0} {nw}"
                            menu:
                                "Not really" if megaship_cell_door_radio[0] == 0:
                                    m "Not really.{w=2} {nw}"
                                    radio "Well... then try to build a paper plane with it!{w=3.0} {nw}"
                                    $ megaship_cell_door_radio[0] = 1
                                    
                                "It is really old" if megaship_cell_door_radio[1] == 0:
                                    m "It is really old.{w=2} {nw}"
                                    radio "Well... then read about history!{w=3.0} {nw}"
                                    $ megaship_cell_door_radio[1] = 1
                                    
                                "There is nothing interesting inside" if megaship_cell_door_radio[2] == 0:
                                    m "There is nothing interesting inside.{w=3} {nw}"
                                    radio "Well... then read it backwards!{w=3.0} {nw}"
                                    $ megaship_cell_door_radio[2] = 1
                            
                            radio "Ha{w=0.2} ha{w=0.2} ha{w=0.2} ha{w=0.2} ha! {w=2.0}{nw}"
                                
                        
                        "Nothing":
                            #m "nothing.{w=1.0} {nw}"
                            pass
                    
            $ startpos = 22

            
        if exitpos == 33:
            
            if m_megaship_cell_escape == 4: # exit
                call sound_screw from _call_sound_screw_4
                $ startpos = 1
                jump megaship_aeration
            
            
            if startpos == 33:
                if inventory_select == "newspaper":
                    m "This is a stupid idea.{w=2} {nw}"
                    m "I can't open a metal grid with a newspaper!{w=3.5} {nw}"
                    
                if inventory_select != "screwdriver" and inventory_select != "newspaper":
                    m "This is an aeration shaft.{w=3.0} {nw}"
                    m "It is sealed by a metal grid.{w=3.0} {nw}"
                
                if inventory_select == "screwdriver" and m_megaship_cell_escape == 3:
                    call use_and_keep_item from _call_use_and_keep_item_8
                    call sound_screw from _call_sound_screw_5
                    $ m_megaship_cell_escape = 4
                    pause 2
                    call sound_connected from _call_sound_connected_6
                    with flash
                    m "The aeration shaft is open now!{w=2.0} {nw}"

                
            $ startpos = 33

            
        if exitpos == 44:
            $ startpos = 44





label megaship_cell_robot:
    
    image megaship_cell_robot = "images/guard2.png"
    hide megaship_cell_robot
    
    call sound_door from _call_sound_door_38
    

    show megaship_cell_robot:
        transform_anchor True
        anchor  (0.5,0.9)
        pos (635, 240)
        rotate 270
        linear 4 pos (240,240)
        linear 1 rotate 180
        linear 2 pos (240,310)
        
    robot "I will repair your sink.{w=2.0} {nw}"
    robot "Don't try to get out, the door will remain closed.{w=3.0} {nw}"
    
    $ m_megaship_cell_escape = 2
    
    return
    
    
label megaship_cell_robot_back:
    
    pause 2
    robot "I can't find my screw driver.{w=2.0} {nw}"
    robot "I can't repair your sink right now.{w=3.0} {nw}"
    robot "I'll be back.{w=2.0} {nw}"
    

    show megaship_cell_robot:
        transform_anchor True
        anchor  (0.5,0.9)
        pos (240,310)
        linear 2 pos (240,240)
        linear 1 rotate 270
        linear 4 pos (635, 240)

    pause 7
    call sound_door from _call_sound_door_39
    hide megaship_cell_robot
    
    return
