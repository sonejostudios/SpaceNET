# MAPS

init:
    $ m_megaship_cell_escape = 0
    
    
screen dev_puddle:
    text "[m_megaship_cell_escape]" at truecenter


############################################
label megaship_cell:
    
    call atmo_spaceship_hum
    
    #show screen dev_puddle
    
    image megaship_cell = imagemapsdir + "megaship_cell.png"
    
    
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
        call startpos

        # do something at node?
        if exitpos == 1:
            if startpos == 1:
                if m_megaship_cell_escape < 4:
                    m "I'm in prison! {w=2.0} {nw}"
                    m "And I don't remember anything... {w=2.5} {nw}"
                    m "Except my name, [playername]... {w=2.5} {nw}"
                    m "And an other name: SpaceNET... {w=3.5} {nw}"
                    m "But what does it mean?... {w=2.5} {nw}"
                    m "SpaceNET... {w=2.5} {nw}"
                    m "And what to do now? {w=2.5} {nw}"
                else:
                    m "I'm in cell number 1. {w=2.0} {nw}"
            $ startpos = 1   

            
        if exitpos == 2:
            if startpos == 2:
                m "This is a table.{w=2.0} {nw}"
                
                if "newspaper" not in inventory:
                    m "There is a newspaper.{w=2.0} {nw}"
                    call take_item("newspaper")
                
            $ startpos = 2

            
        if exitpos == 3: 
            if startpos == 3:
                m "This is a bed.{w=2.0} {nw}"
            $ startpos = 3

            
        if exitpos == 4:
            if startpos == 4:
                
                if inventory_select != "newspaper":
                    m "This is the sink and the wc.{w=2.0} {nw}"
                    
                if m_megaship_cell_escape == 1:
                    m "It is completely flooded and doesn't work anymore.{w=3.0} {nw}"
                
                if inventory_select == "newspaper" and m_megaship_cell_escape == 0:
                    
                    menu:
                        "use newspaper with sink":
                            call use_and_keep_item
                            call sound_paper
                            #with flash
                            m "now the sink is blocked.{w=2.0} {nw}"
                            m "what will happen if I open the tap?{w=2.0} {nw}"
                            
                            call sound_tap
                            show puddle behind sink:
                                anchor (0.5,0.5)
                                alpha 0.0
                                pos (200, 325)
                                linear 2 alpha 0.2
                            
                            $ m_megaship_cell_escape = 1
                            

                            pass
                        
                        "back":
                            pass
                            
                if m_megaship_cell_escape == 2:
                    m "the repair-robot is working.{w=2.0} {nw}"
                    m "there is a screw driver...{w=2.0} {nw}"
                    m "I could take it... {w=2.0} {nw}"
                    
                    call take_item("screwdriver")
                    
                    if "screwdriver" in inventory:
                        $ m_megaship_cell_escape = 3
                        call megaship_cell_robot_back
                        pass

            $ startpos = 4

            

        #exits routing "got to map and set position for next map"
        if exitpos == 11:       
            $ startpos = 11        
 
            
        if exitpos == 22:
            $ startpos = 22
            call dialog_closed
            
            radio "what do you want, prisoner?{w=3.0} {nw}"
            
            menu:
                "the sink is broken" if m_megaship_cell_escape == 1:
                    m "the sink is broken.{w=2.0} {nw}"
                    radio "okay, i'll send a repair-robot to your cell.{w=3.0} {nw}"
                    call megaship_cell_robot
                
                "nothing":
                    #m "nothing.{w=1.0} {nw}"
                    pass

            
        if exitpos == 33:
            
            if m_megaship_cell_escape == 4: # exit
                call sound_screw
                $ startpos = 1
                jump megaship_aeration
            
            
            if startpos == 33:
                    
                if inventory_select != "screwdriver":
                    m "This is an aeration shaft.{w=3.0} {nw}"
                
                if inventory_select == "screwdriver" and m_megaship_cell_escape == 3:
                    call use_and_keep_item
                    call sound_screw
                    $ m_megaship_cell_escape = 4
                    pause 2
                    call sound_connected
                    with flash
                    m "The grid is open now!{w=2.0} {nw}"

                
            $ startpos = 33

            
        if exitpos == 44:
            $ startpos = 44





label megaship_cell_robot:
    
    image megaship_cell_robot = "images/guard2.png"
    hide megaship_cell_robot
    
    call sound_door
    

    show megaship_cell_robot:
        transform_anchor True
        anchor  (0.5,0.9)
        pos (635, 240)
        rotate 270
        linear 4 pos (240,240)
        linear 1 rotate 180
        linear 2 pos (240,310)
        
    robot "I will repair your sink.{w=2.0} {nw}"
    robot "Don't try to go out, the door will remain closed.{w=3.0} {nw}"
    
    $ m_megaship_cell_escape = 2
    
    return
    
    
label megaship_cell_robot_back:
    
    pause 2
    robot "I don't find my screw driver.{w=2.0} {nw}"
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
    call sound_door
    hide megaship_cell_robot
    
    return
