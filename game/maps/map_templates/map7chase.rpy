
## special guard screen
screen guard():
    timer 0.1 action [SetVariable("guardpos", 5)]
    
    timer 4 repeat True action [SetVariable("guardpos", guardpos -1)]
    
    #text "aaaaaaaa" at truecenter
    
    if guardpos == 0:
        timer 0.1 repeat True action SetVariable("guardpos", 4)
        
    
    if  startpos == guardpos:
        timer 0.1 repeat True action Hide("guard"), Jump("map7guard")

    if startpos == 33 and guardpos == 3:
        timer 0.1 repeat True action Hide("guard"), Jump("map7guard")
    if startpos == 11 and guardpos == 1:
        timer 0.1 repeat True action Hide("guard"), Jump("map7guard")

        

      
##############################################
label map7:
    
    show screen guard
    
    image map7 = imagemapsdir + "xylo_sea_map7.png"
    
    scene map7
    show screen notify("map7 chase")

    #button. set buttons like button_house
    #$ buttons = button_chase
    #show buttons:
    #    pos (220,105)
        
    show guard:
        transform_anchor True
        anchor (0.5, 0.9)
        rotate 270
        pos (600,130)
        linear 3 pos (260,110)
        linear 1 rotate 180
        linear 3 pos (240,400)
        linear 1 rotate 90
        linear 3 pos (560,400)
        linear 1 rotate 0
        linear 3 pos (600,130)
        linear 1 rotate -90

        repeat
        

    
    # set all variables for the map (nodes and path)
    $ nodeA = (260,110)
    $ nodeB = (600,130)
    $ nodeC = (560,400)
    $ nodeD = (240,400)
    
    $ nodeAA = (400,140)
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



label loop_map7:

    # start "move through the map" loop
    call startpos from _call_startpos_51
    
    # do something at node?
    if exitpos == 1:       #if at node A
        $ startpos = 1     # stay in A
        
        call map7button from _call_map7button # button
        
        jump loop_map7          # map to jump to
        
    if exitpos == 2:
        $ startpos = 2
        jump loop_map7
        
    if exitpos == 3:
        $ startpos = 3

        jump loop_map7
        
    if exitpos == 4:
        $ startpos = 4
        jump loop_map7     

    #exits routing "got to map"
    if exitpos == 11:       #if going out at AA
        if button_chase == True: # button
            $ startpos = 11
            call sound_door from _call_sound_door_117
            m "The door is open!"
            jump loop_map7 # go to house
            
        else:
            $ startpos = 11
            call dialog_closed from _call_dialog_closed_26
            jump loop_map7         # map to jump to
        
    if exitpos == 22:
        $ startpos = 44
        jump map3
        
    if exitpos == 33:
        $ startpos = 11
        
        hide screen guard
        $ guardpos = 6
        
        jump map1
        
    if exitpos == 44:
        $ startpos = 22
        jump map7guard





label map7button:
    
    #call buttons from _call_buttons
    # set button_house like buttons
    $ button_chase = buttons
    
    return
    


label map7guard:
    hide screen guard
    
    call sound_scan from _call_sound_scan_6
    with flash
    
    guard "You are not allowed to be here!! {w=3.0} {nw}"
    
    $ guardpos = 6
    $ startpos = 11
    

    jump map1


    
    
