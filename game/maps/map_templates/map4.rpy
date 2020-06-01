      
##############################################
label map4:
    
    image map4 = imagemapsdir + "xylo_sea_p4.png"
    
    scene map4
    show screen notify("map4")

    #button. set buttons like button_house
    $ buttons = button_house
    show buttons:
        pos (630,140)
        
    #show light:
    #    pos (630,140)

    
    # set all variables for the map (nodes and path)
    $ nodeA = (465,350)
    $ nodeB = (400,155)
    $ nodeC = (600,130)
    $ nodeD = (540,360)
    
    $ nodeAA = (390,40)
    $ nodeBB = (750,350)
    $ nodeCC = (400,460)
    $ nodeDD = (320,275)
    
    $ pathA = (nodeA, nodeB, nodeC, (0,0), nodeAA, nodeBB, (0,0), nodeDD)
    $ pathB = (nodeA, nodeB, nodeC, (0,0), nodeAA, nodeBB, (0,0), nodeDD)
    $ pathC = (nodeA, nodeB, nodeC, (0,0), (0,0), (0,0), (0,0), nodeDD)
    $ pathD = ((0,0), nodeB, nodeC, (0,0), (0,0), (0,0), (0,0), nodeDD)
    
    $ pathAA = (nodeA, nodeB, (0,0), (0,0), nodeAA, (0,0), (0,0), nodeDD)
    $ pathBB = (nodeA, nodeB, (0,0), (0,0), (0,0), nodeBB, (0,0), nodeDD)
    $ pathCC = ((0,0), (0,0), nodeC, (0,0), (0,0), (0,0), (0,0), (0,0))
    $ pathDD = (nodeA, nodeB, nodeC, (0,0), nodeAA, nodeBB, (0,0), nodeDD)

label loop_map4:

    # start "move through the map" loop
    call startpos
    
    # do something at node?
    if exitpos == 1:        #if at node A
        $ startpos = 11      # stay in A
        $ multiposx = 0
        $ multiposy = 0
        jump multimap1
        
        #jump loop_map4      # map to jump to
        
    if exitpos == 2:
        $ startpos = 2
        jump loop_map4
        
    if exitpos == 3:
        $ startpos = 3
        
        call map4button # button
        
        jump loop_map4
        
    if exitpos == 4:
        $ startpos = 4
        jump loop_map4     

    #exits routing "got to map"
    if exitpos == 11:       #if going out at AA
        $ startpos = 33     #go to CC
        jump map1           # map to jump to
        
    if exitpos == 22:
        $ startpos = 44
        jump map3
        
    if exitpos == 33:
        $ startpos = 11
        jump map3
        
    if exitpos == 44:
        if button_house == True:
            $ startpos = 22
            call sound_door
            jump map5 # go to house
            
        else:
            $ startpos = 44
            call dialog_closed
            jump loop_map4




label map4button:
    
    call buttons
    # set button_house like buttons
    $ button_house = buttons
    
    return
    



    
    
