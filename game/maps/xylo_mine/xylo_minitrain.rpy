# MAPS

############################################

    
init:
    $ minitrain_way = [False,False,False]
    
    $ minitrain_button1 = False
    $ minitrain_button2 = False
    $ minitrain_button3 = False



screen xylo_minitrain_button1 zorder -999:
    
    on "show" action SetVariable("pnc_nodes_visible", False)
    on "hide" action SetVariable("pnc_nodes_visible", True)
    
    #add "#112119"
    
    imagebutton: 
        idle "images/maps/bg.png" 
        action Hide("xylo_minitrain_button1")
            
    add "inventory/inventory.png"
    
    #text "\n [minitrain_button1] - [minitrain_button2] - [minitrain_button3] -- [minitrain_way]"
    
    hbox xalign 0.5 yalign 0.5:
        vbox xalign 0.5:
            label "1" at center
            null height 10
            imagebutton: 
                auto "images/buttonbig_%s.png"
                action ToggleVariable("minitrain_button1"), Play("sound", "sounds/collect.ogg") at center
                
        null width 100
        
        vbox xalign 0.5:
            label "2" at center
            null height 10
            imagebutton: 
                auto "images/buttonbig_%s.png"
                action ToggleVariable("minitrain_button2"), Play("sound", "sounds/collect.ogg") at center
                
        null width 100
        
        vbox xalign 0.5:
            label "3" at center
            null height 10
            imagebutton: 
                auto "images/buttonbig_%s.png"
                action ToggleVariable("minitrain_button3"), Play("sound", "sounds/collect.ogg") at center
    
    if shadow_enable == 1:
        add "images/shadow.png" align (0.5,0.5)
                
                
    
             
    
        

# minitrain

label xylo_minitrain:
    $ pnc_nodes_visible = True
    
    stop sound fadeout 1.0
    call atmo_base
    
    call music_xylo_mine
    
    image xylo_minitrain = imagemapsdir + "xylo_minitrain.png"
    
    scene bgcolor
    show screen notify("mine train")
    
    show xylo_minitrain:
        anchor (400,240)
        pos (400,240)

    
    show circle:
        anchor (0.5,0.5)
        pos (400,260)
        zoom 0.3
    
    
    
    # set all variables for the map (nodes and path)
    $ nodeA = (53, 132)
    $ nodeB = (406, 85)
    $ nodeC = (400, 260)
    $ nodeD = (644, 443)

    $ nodeAA = (684, 445)
    $ nodeBB = (715, 444)
    $ nodeCC = (743, 445)
    $ nodeDD = (771, 417)

    $ pathA = (nodeA, nodeB, (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0))
    $ pathB = (nodeA, nodeB, nodeC, (0, 0), (0, 0), (0, 0), (0, 0), (0, 0))
    $ pathC = ((0, 0), nodeB, nodeC, (0, 0), (0, 0), (0, 0), (0, 0), (0, 0))
    $ pathD = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)
     
    $ pathAA = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)
    $ pathBB = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)
    $ pathCC = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)
    $ pathDD = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)


label loop_xylo_minitrain:

    # start "move through the map" loop
    call startpos

    # do something at node?
    if exitpos == 1:       #if at node A
        call sound_door
        $ liftpos == 0
        $ startpos = 1     # stay in A
        jump xylo_mine_lift2          # map loop to jump to
        
    if exitpos == 2:
        if startpos == 2:
            show screen xylo_minitrain_button1
        $ startpos = 2
        jump loop_xylo_minitrain
        
    
    if exitpos == 3: # go to minitrain
        
        $ minitrain_way = [minitrain_button1, minitrain_button2, minitrain_button3]

        $ startpos = 3
        jump minitrain_start
        
    if exitpos == 4:
        $ startpos = 4
        jump loop_xylo_minitrain 
        

    #exits routing "got to map and set position for next map"
    if exitpos == 11:       #if going out at AA
        $ startpos = 11    #go to CC
        jump loop_xylo_minitrain          # map to jump to
        
    if exitpos == 22:
        $ startpos = 22
        
        $liftpos = 3
        call sound_door
        jump loop_xylo_minitrain # go to lift
        
    if exitpos == 33:
        $ startpos = 33
        jump loop_xylo_minitrain
        
    if exitpos == 44:
        $ startpos = 44

        jump loop_xylo_minitrain



# minitrain animations

label minitrain_start:
    $ pnc_nodes_visible = False
    
    call sound_minitrain_loop
    
    
    $ path = ((0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0))
    call hidepaths

    
    show xylo_minitrain:
        pos (400,240)
        easeout 2 anchor (700,240)
    pause 2  
    
    if minitrain_way[0] == False:  
        jump minitrain_cross1
    if minitrain_way[0] == True:  
        jump minitrain_cross5
    
    
label minitrain_cross1:
    #"1"
    show xylo_minitrain:
        linear 1 anchor (700,140)
        linear 4 anchor (1400,140)
        linear 3 anchor (1400,640)
    
    pause 8
    
    jump minitrain_cross2
    
    
label minitrain_cross2:
    #"2"
    show xylo_minitrain:
        linear 2 anchor (1000,640)
    pause 2
    
    jump minitrain_cross3


label minitrain_cross3:
    #"3"
    show xylo_minitrain:
        linear 2 anchor (700,640)
    pause 2
    
    jump minitrain_loopback
    
    
label minitrain_loopback:
    #"loopback"
    show xylo_minitrain:
        linear 3 anchor (200,640)
        linear 2 anchor (200,340)
        linear 2 anchor (400,340)
        easein 2 anchor (400,240)
    pause 9
    
    
    jump xylo_minitrain
    
    

label minitrain_cross5:
    #"5"
    show xylo_minitrain:
        linear 1 anchor (700,340)
        linear 2 anchor (1000,340)
    pause 3
    
    if minitrain_way[1] == True:
        jump minitrain_cross6
    if minitrain_way[1] == False:
        jump minitrain_cross7
    

label minitrain_cross6:
    #"6"
    show xylo_minitrain:
        linear 2 anchor (1000,640)
    pause 2
    
    jump minitrain_cross3
    
    
label minitrain_cross7:
    #"7"
    show xylo_minitrain:
        linear 2 anchor (1200,340)
        linear 3 anchor (1200,740)
        linear 3 anchor (700,740)
    pause 8
    
    if minitrain_way[2] == False:
        jump minitrain_cross8
    
    if minitrain_way[2] == True:
        jump minitrain_cross9
        
        
    
label minitrain_cross8:
    #"8"
    show xylo_minitrain:
        linear 1 anchor (700,640)
    pause 1
    jump minitrain_loopback


label minitrain_cross9:
    # "9"
    show xylo_minitrain:
        linear 4 anchor (100,740)
        linear 1 anchor (100,840)
        linear 7 anchor (1400,840)
    pause 12
    
    stop sound fadeout 1.0
    
    jump xylo_minitrain2
    
    

