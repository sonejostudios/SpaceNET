# MAPS

############################################

init:
    $ xylo_sea_map7_button = False

screen xylo_sea_map7_button() zorder -999:
    
    on "show" action SetVariable("pnc_nodes_visible", False)
    on "hide" action SetVariable("pnc_nodes_visible", True)
    
    add "#112119"
    
    imagebutton: 
        idle "images/maps/bg.png" 
        action Hide("xylo_sea_map7_button")
            
    add "inventory/inventory.png"
    
    hbox xalign 0.5 yalign 0.5:
        vbox xalign 0.5:
            label "bunker door" at center
            null height 10
            imagebutton: 
                auto "images/buttonbig_%s.png"
                action ToggleVariable("xylo_sea_map7_button"), Play("sound", "sounds/collect.ogg") at center
                
    if shadow_enable == 1:
        add "images/shadow.png" align (0.5,0.5)
    


## special guard screen
screen xylo_sea_guard():
    timer 0.1 action [SetVariable("guardpos", 5)]
    
    timer 4 repeat True action [SetVariable("guardpos", guardpos -1)]
    
    #text "aaaaaaaa" at truecenter
    
    if guardpos == 0:
        timer 0.1 repeat True action SetVariable("guardpos", 4)
        
    
    if  startpos == guardpos:
        timer 0.1 repeat True action Hide("guard"), Jump("xylo_map7guard")
    if startpos == 33 and guardpos == 3:
        timer 0.1 repeat True action Hide("guard"), Jump("xylo_map7guard")
    if startpos == 11 and guardpos == 1:
        timer 0.1 repeat True action Hide("guard"), Jump("xylo_map7guard")

        

      
##############################################
label xylo_map7:
    
    #stop atmo fadeout 1.0
    call music_cargo from _call_music_cargo
    
    show screen xylo_sea_guard
    
    image xylo_map7 = imagemapsdir + "xylo_sea_map7.png"
    
    image xylo_sea_guard:
        "images/guard.png"
        pause 0.1
        "images/guard2.png"
        pause 0.1
        repeat
    
    scene xylo_map7
    show screen notify("Xylo's sea bunker")

        
    show xylo_sea_guard:
        transform_anchor True
        anchor (0.5, 0.9)
        rotate 270
        pos (580,130)
        linear 3 pos (260,110)
        linear 1 rotate 180
        linear 3 pos (240,400)
        linear 1 rotate 90
        linear 3 pos (560,400)
        linear 1 rotate 0
        linear 3 pos (580,130)
        linear 1 rotate -90
        repeat
        

    
    # set all variables for the map (nodes and path)
    $ nodeA = (230,100)
    $ nodeB = (550,130)
    $ nodeC = (560,380)
    $ nodeD = (240,380)
    
    $ nodeAA = (405,143)
    $ nodeBB = (750,350)
    $ nodeCC = (400,440)
    $ nodeDD = (320,275)
    
    $ pathA = (nodeA, nodeB, (0,0), nodeD, nodeAA, (0,0), (0,0), (0,0))
    $ pathB = (nodeA, nodeB, nodeC, (0,0), nodeAA, (0,0), (0,0), (0,0))
    $ pathC = ((0,0), nodeB, nodeC, nodeD, (0,0), (0,0), nodeCC, (0,0))
    $ pathD = (nodeA, (0,0), nodeC, nodeD, (0,0), (0,0), nodeCC, (0,0))
    
    $ pathAA = (nodeA, nodeB, (0,0), (0,0), nodeAA, (0,0), (0,0), (0,0))
    $ pathBB = ((0,0), nodeB, (0,0), (0,0), (0,0), nodeBB, (0,0), nodeDD)
    $ pathCC = ((0,0), (0,0), nodeC, nodeD, (0,0), (0,0), nodeCC, (0,0))
    $ pathDD = ((0,0), (0,0), nodeC, nodeD, (0,0), (0,0), nodeCC, (0,0))



label loop_xylo_map7:

    # start "move through the map" loop
    call startpos from _call_startpos_11
    
    # do something at node?
    if exitpos == 1:       #if at node A
        $ startpos = 1     # stay in A
        
        show screen xylo_sea_map7_button
        
        jump loop_xylo_map7          # map to jump to
        
    if exitpos == 2:
        $ startpos = 2
        jump loop_xylo_map7
        
    if exitpos == 3:
        $ startpos = 3

        jump loop_xylo_map7
        
    if exitpos == 4:
        $ startpos = 4
        jump loop_xylo_map7     

    #exits routing "got to map"
    if exitpos == 11:       #if going out at AA
        if xylo_sea_map7_button == True: # button
            $ startpos = 11
            call sound_door from _call_sound_door_25
            #m "The door is open!"
            hide screen xylo_sea_guard
            $ liftpos = 3
            jump xylo_sea_bunker_lift1 # go to bunker
            
        else:
            $ startpos = 11
            call dialog_closed from _call_dialog_closed_5
            jump loop_xylo_map7         # map to jump to
        
    if exitpos == 22:
        $ startpos = 44
        jump xylo_map3
        
    if exitpos == 33:
        $ startpos = 11
        
        hide screen xylo_sea_guard
        $ guardpos = 6
        
        jump xylo_map1
        
    if exitpos == 44:
        $ startpos = 22
        jump xylo_map7guard




label xylo_map7guard:
    hide screen xylo_sea_guard
    hide screen xylo_sea_map7_button
    
    pause 0.3
    call sound_scan from _call_sound_scan_1
    with flash
    
    robotguard "You are not allowed to be here! {w=3.0} {nw}"
    
    $ guardpos = 6
    $ startpos = 11
    

    jump xylo_map1


    
    
