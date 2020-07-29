# MAPS      
##############################################


init:
    
    default xylo_sea_village_fisher_flags = [0,0,0,0]


label xylo_map4:
    
    stop music fadeout 1.0
    call atmo_ground from _call_atmo_ground_1
    
    image xylo_map4 = imagemapsdir + "xylo_sea_p4.png"
    
    scene bgcolor
    show xylo_map4
    show screen notify("xylo sea village")

  
    show light:
        pos (206,146)
    show light as l2:
        pos (92,272)
    show light as l3:
        pos (740,252)

    
    # set all variables for the map (nodes and path)
    $ nodeA = (-100,-100)
    $ nodeB = (430,230)
    $ nodeC = (620,133)
    $ nodeD = (550,320)
    
    $ nodeAA = (390,33)
    $ nodeBB = (770,350)
    $ nodeCC = (400,460)
    $ nodeDD = (320,275)
    
    $ pathA = (nodeA, nodeB, nodeC, (0,0), nodeAA, nodeBB, (0,0), nodeDD)
    $ pathB = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, (0,0), nodeDD)
    $ pathC = (nodeA, nodeB, nodeC, nodeD, (0,0), (0,0), (0,0), nodeDD)
    $ pathD = ((0,0), nodeB, nodeC, nodeD, (0,0), nodeBB, (0,0), nodeDD)
    
    $ pathAA = (nodeA, nodeB, (0,0), (0,0), nodeAA, (0,0), (0,0), nodeDD)
    $ pathBB = (nodeA, nodeB, (0,0), nodeD, (0,0), nodeBB, (0,0), nodeDD)
    $ pathCC = ((0,0), (0,0), nodeC, (0,0), (0,0), (0,0), (0,0), (0,0))
    $ pathDD = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, (0,0), nodeDD)

label loop_xylo_map4:
    
    if renpy.showing("npc") != True:
        show npc:
            pos (600,360)
            rotate 90
            linear 2 pos (500,360)
            linear 1 rotate 270
            linear 2 pos (600,360)
            linear 1 rotate 90
            repeat

    # start "move through the map" loop
    call startpos from _call_startpos_40
    
    # do something at node?
    if exitpos == 1:        #if at node A
        $ startpos = 11      # stay in A
        $ multiposx = 0
        $ multiposy = 0
        jump multimap1
        
        #jump loop_map4      # map to jump to
        
    if exitpos == 2:
        if startpos == 2:
            m "This is the center of the village. {w=2} {nw}"
        
        $ startpos = 2
        jump loop_xylo_map4
        
    if exitpos == 3:
        
        if startpos == 3:
            call xylo_sea_village_info from _call_xylo_sea_village_info


        $ startpos = 3
        jump loop_xylo_map4
        
    if exitpos == 4: #npc
        
        if startpos == 4:
            jump xylo_sea_village_fisher
        
        $ startpos = 4
        jump loop_xylo_map4     

    #exits routing "got to map"
    if exitpos == 11:       #if going out at AA
        $ startpos = 33     #go to CC
        jump xylo_map1           # map to jump to
        
    if exitpos == 22:
        $ startpos = 44
        jump xylo_map3
        
    if exitpos == 33:
        $ startpos = 11
        jump xylo_map3
        
    if exitpos == 44:
        $ startpos = 22
        call sound_door from _call_sound_door_98
        jump xylo_map5house # go to house

    

label xylo_sea_village_info:
    
    $ info_panel_symbol = ""
    $ showtext = """
- Xylo sea colony -


Welcome to our beautiful sea coast village.

Go north to go to the industrial harbour.

Go east to go to the sea and enjoy the coast road !


    """
    
    call info_panel from _call_info_panel_8 # in animations

    return




label xylo_sea_village_fisher: 
    
    show npc:
        linear 1 pos (550,360) rotate 180
    pause 1.5
    #m "Hello ! {w=1.5} {nw}"
    fisher "Hello. How can I help you? {w=2.5} {nw}"
      
    
    $ questions = ["What is it this the house?{w=2.5} {nw}", 
                    "What about the private property up there?{w=3.0} {nw}", 
                    "What about the sea? {w=2.0} {nw}", 
                    "I would like to rent a boat. {w=2.0} {nw}", 
                    "Nothing, thank you. {w=1.0} {nw}"]
    
    while True:
        menu:
            "[questions[0]]" if xylo_sea_village_fisher_flags[0]  == 0:
                m "[questions[0]]"
                fisher "This is the local bar. {w=2} {nw}"
                $ xylo_sea_village_fisher_flags[0] = 1
                
            "[questions[1]]"if xylo_sea_village_fisher_flags[1]  == 0:
                m "[questions[1]]"
                fisher "Oh, this is a bunker... {w=2} {nw}"
                fisher "It belongs to A.R.K. Corporation. {w=2} {nw}"
                fisher "They just built it a while ago. {w=2} {nw}"
                fisher "I don't knows nothing about, sorry. {w=2.5} {nw}"
                fisher "I just know one thing: {w=2} {nw}"
                fisher "Don't go there, otherwise the guard will kick you out! {w=3} {nw}"
                $ xylo_sea_village_fisher_flags[1] = 1
                
            "[questions[2]]"if xylo_sea_village_fisher_flags[2]  == 0:
                m "[questions[2]]"
                fisher "Oh the sea. {w=2} {nw}"
                fisher "I love it. {w=2} {nw}"
                fisher "But unfortunately I'm not allowed to go there anymore... {w=3.5} {nw}"
                $ xylo_sea_village_fisher_flags[2] = 1
                
            "[questions[3]]"if xylo_sea_village_fisher_flags[3]  == 0:
                m "[questions[3]]"
                fisher "I have no boat to rent, sorry. {w=2} {nw}"
                fisher "I had a boat before, but I sold it to the boat management company. {w=4} {nw}"
                fisher "I don't know if they rent boats, sorry. {w=3} {nw}"
                fisher "Just go to your right, there is an information table I think. {w=3.5} {nw}"
                $ xylo_sea_village_fisher_flags[3] = 1
            
            "[questions[4]]":
                m "[questions[4]]"
                show npc:
                    linear 1 pos (600,360) rotate 270
                    linear 1 rotate 90
                pause 2
                hide npc
                jump loop_xylo_map4
