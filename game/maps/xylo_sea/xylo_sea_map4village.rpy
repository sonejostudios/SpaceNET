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
    show screen notify("Settlement Center")

  
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
            if inventory_select == "":
                m "This is the center of the settlement. {w=3} {nw}"
            else:
                call dialog_nosense from _call_dialog_nosense_51
        
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
- Sea Settlement -


Welcome to this beautiful place.

Go north to go to the industrial harbor.
Go east to go to the sea and enjoy the coastal road.

If it is the right season, 
we also recommand to take a boat trip on the sea!
Just call the boat rental company for more information.


    """
    
    call info_panel from _call_info_panel_8 # in animations

    return




label xylo_sea_village_fisher:
    show npc:
        linear 1 pos (550,360) rotate 180
    pause 1.5
    
    if inventory_select != "":
        call npc_dont_need_item(fisher) from _call_npc_dont_need_item_6
        show npc:
            linear 1 pos (600,360) rotate 270
            linear 1 rotate 90
        pause 2
        hide npc
        jump loop_xylo_map4
    
    
    fisher "Hello. How can I help you? {w=3.5} {nw}"
      
    
    $ questions = ["What is inside this house?{w=3.5} {nw}", 
                    "What about the private property up there?{w=4} {nw}", 
                    "What about the sea? {w=3.0} {nw}", 
                    "I would like to rent a boat. {w=3.0} {nw}", 
                    "I'm fine, thanks. {w=2.0} {nw}"]
    
    while True:
        menu:
            "[questions[0]]" if xylo_sea_village_fisher_flags[0]  == 0:
                m "[questions[0]]"
                fisher "This is the local bar. {w=2.5} {nw}"
                fisher "It is okay, but the barman is grumpy. {w=3} {nw}"
                fisher "When I was younger, I enjoyed it a lot. {w=3} {nw}"
                menu:
                    "And now?":
                        m "And now?{w=2.5} {nw}"
                        
                    "You don't like it anymore?":
                        m "You don't like it anymore?{w=3.5} {nw}"
                        
                fisher "I'm too old now for that kind of stuff. {w=3.5} {nw}"
                fisher "I prefer the fresh air from the sea.{w=3} {nw}"
                fisher "And I'm tired of arguing around with the grumpy barman.{w=5} {nw}"
                        
                $ xylo_sea_village_fisher_flags[0] = 1
                
            "[questions[1]]"if xylo_sea_village_fisher_flags[1]  == 0:
                m "[questions[1]]"
                fisher "Oh, this is a bunker... {w=3} {nw}"
                fisher "It belongs to A.R.K. Corporation. {w=3} {nw}"
                fisher "They just built it a while ago. {w=3} {nw}"
                fisher "I don't know anyhing about it, sorry. {w=3.5} {nw}"
                fisher "I just know one thing: {w=3} {nw}"
                fisher "Don't go there, otherwise the robot guard will kick you out! {w=4.5} {nw}"
                menu:
                    "Who?":
                        m "Who?{w=2.5} {nw}"
                        fisher "Are you deaf? {w=2.5} {nw}"
                        fisher "The robot guard! {w=2.5} {nw}"
                        
                    "Why?":
                        m "Why?{w=2.5} {nw}"
                        fisher "I really don't know... {w=2.5} {nw}"
                        fisher "Just don't do it.{w=2.5} {nw}"
                
                m "Okay, thanks for the hint.{w=3.5} {nw}"
                $ xylo_sea_village_fisher_flags[1] = 1
                
            "[questions[2]]"if xylo_sea_village_fisher_flags[2]  == 0:
                m "[questions[2]]"
                fisher "Oh, the sea. {w=3} {nw}"
                fisher "I love it. {w=2.5} {nw}"
                fisher "But unfortunately, I'm not allowed to go there anymore... {w=4.5} {nw}"
                menu:
                    "Why not?":
                        m "Why not?{w=2.5} {nw}"
                        
                    "Who says that?":
                        m "Who says that?{w=3.5} {nw}"
                        
                    "Tell me.":
                        m "Tell me.{w=2.5} {nw}"
                        
                fisher "The government took away my fishing license. {w=4.5} {nw}"
                fisher "A couple of weeks ago, a guy came to me. {w=4.5} {nw}"
                fisher "He asked a lot of questions.{w=4.5} {nw}"
                fisher "And then he said, I'm too old for fishing!{w=4.5} {nw}"
                fisher "This small insolent jerk!{w=4.5} {nw}"
                fisher "They are working for the government and they think they are kings!{w=5} {nw}"
                fisher "At his age, I was one of the first who colonized this planet. {w=5} {nw}"
                fisher "There was nothing here!{w=3.5} {nw}"
                fisher "We built everything by hands!{w=3.5} {nw}"
                fisher "And now, they are just coming around and think they can decide everything? {w=5} {nw}"
                fisher "I don't think so!{w=2.5} {nw}"
                fisher "I will never do what they want.{w=3.5} {nw}"
                fisher "I don't care, I have nothing to lose anymore.{w=3.5} {nw}"
                
                $ xylo_sea_village_fisher_flags[2] = 1
                
            "[questions[3]]"if xylo_sea_village_fisher_flags[3]  == 0:
                m "[questions[3]]"
                fisher "I have no boat for rent, sorry. {w=3} {nw}"
                fisher "I had a boat before, but since I lost my fishing license, I sold it to the Boat Rental Company. {w=6} {nw}"
                fisher "And I don't know if they rent boats in that season. {w=4.5} {nw}"
                fisher "You should ask them by yourself. {w=3.5} {nw}"
                fisher "Just go to your right, I think there is an information table. {w=4.5} {nw}"
                $ xylo_sea_village_fisher_flags[3] = 1
            
            "[questions[4]]":
                m "[questions[4]]"
                show npc:
                    linear 1 pos (600,360) rotate 270
                    linear 1 rotate 90
                pause 2
                hide npc
                jump loop_xylo_map4
