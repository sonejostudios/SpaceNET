# MAPS

############################################

init:
    $ xylo_spaceport_hall_term = False
    
    default xylo_village_oldman_flags = [0, 0, 0, 0]



label xylo_spaceport_hall:
    
    
    stop music fadeout 1.0
    call atmo_village from _call_atmo_village_1
    
    
    image xylo_spaceport_hall = imagemapsdir + "xylo_spaceport_hall.png"
    
    scene xylo_spaceport_hall
    show screen notify("Xylo spaceport hall")
    
    show bgcolor behind xylo_spaceport_hall    
    

    # check if spaceship is landing on this map or not
    # $ landing = False
    # $ landing = True
    #call landing_anim
    
    
    # set all variables for the map (nodes and path)
    $ nodeA = (628, 58)
    $ nodeB = (403, 238)
    $ nodeC = (101, 422)
    $ nodeD = (178, 243)

    $ nodeAA = (617, 242)
    $ nodeBB = (234, 426)
    $ nodeCC = (400, 380)
    $ nodeDD = (58, 391)

    $ pathA = (nodeA, nodeB, nodeC, (0, 0), nodeAA, nodeBB, (0, 0), (0, 0))
    $ pathB = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, (0, 0))
    $ pathC = (nodeA, nodeB, nodeC, nodeD, (0, 0), nodeBB, nodeCC, (0, 0))
    $ pathD = ((0, 0), nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, (0, 0))
     
    $ pathAA = (nodeA, nodeB, (0, 0), nodeD, nodeAA, (0, 0), (0, 0), (0, 0))
    $ pathBB = (nodeA, nodeB, nodeC, nodeD, (0, 0), nodeBB, nodeCC, (0, 0))
    $ pathCC = ((0, 0), nodeB, nodeC, nodeD,  (0, 0), nodeBB, nodeCC, (0, 0))
    $ pathDD = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)


label loop_xylo_spaceport_hall:
    
    while True:
    
        if renpy.showing("npc") != True:
            show npc:
                pos (440,360)
                linear 2 pos (440,400)
                linear 1 rotate 180
                linear 2 pos (440,360)
                linear 1 rotate 0
                repeat

        # start "move through the map" loop
        call startpos from _call_startpos_23

        # do something at node?
        if exitpos == 1:     
            if drunktime > 0:
                if startpos == 1:
                    m "Flying around is not a good idea right now...{w=3.0} {nw}"
                $ startpos = 1
                jump loop_xylo_spaceport_hall
            
            
            $ startpos = 3  
            call sound_door from _call_sound_door_49
            $ landing = False
            jump xylo_spaceport         
            
        if exitpos == 2:
            if startpos == 2:
                m "I'm in the hall of the spaceport.{w=3.0} {nw}"
            $ startpos = 2

            
        if exitpos == 3:
            
            if startpos == 3 and xylo_spaceport_hall_term == True:
                call terminal from _call_terminal_4
            
            if startpos == 3 and xylo_spaceport_hall_term == False:
                if inventory_select != "screwdriver":
                    call sound_electroshock from _call_sound_electroshock_25
                    with hpunch
                    m "This terminal is broken... {w=1.5} {nw}"
                
                if inventory_select == "screwdriver":
                    call use_and_keep_item from _call_use_and_keep_item_10
                    m "Let's see if I can repaire it... {w=2.0} {nw}"
                    $ xylo_spaceport_hall_term = True
                    call sound_screw from _call_sound_screw_6
                    pause 1
                    call sound_electroshock from _call_sound_electroshock_6
                    pause 1
                    call sound_connected from _call_sound_connected_8
                    #with flash
                    m "Yeah, I fixed it! Now it seems to work again. {w=2.0} {nw}"
                
            $ startpos = 3

            
            
            
        if exitpos == 4:
            if drunktime > 0:
                if startpos == 4:
                    m "I'm not in a shopping mood right now... {w=3.0} {nw}"
                $ startpos = 4
                jump loop_xylo_spaceport_hall
            
            $ startpos = 3
            call sound_door from _call_sound_door_50
            jump xylo_spaceport_hall_store # to store
            

        #exits routing "got to map and set position for next map"
        if exitpos == 11:       #if going out at AA
            call sound_door from _call_sound_door_51
            $ startpos = 1    #go to CC
            jump xylo_spaceport_hall_bar          # map to jump to
            
        if exitpos == 22:
            call sound_door from _call_sound_door_52
            $ startpos = 1
            jump xylo_village1 # to village1
            
       
        if exitpos == 33:
            if startpos == 33:
                call xylo_spaceport_hall_oldman from _call_xylo_spaceport_hall_oldman #npc
            
            $ startpos = 33

            
        if exitpos == 44:
            $ startpos = 44






label xylo_spaceport_hall_oldman: 
    
    if inventory_select != "":
        call npc_dont_need_item(oldman) from _call_npc_dont_need_item_4
        return
        
    show npc:
        linear 1 pos (440,380) rotate 90
    pause 1.5
    
    
    m "Hello! {w=1.5} {nw}"
    oldman "What do you want? {w=2.0} {nw}"
    
    
    if drunktime > 0:
        call dialog_joke from _call_dialog_joke_2
        if joke == 1:
            oldman "Oh, I know this joke already.  {w=3} {nw}"
            oldman "It is not funny at all!  {w=2} {nw}"
            oldman "Come back if you have a better one.  {w=3} {nw}"

        if joke == 2:
            oldman "Well... {w=1} I don't know! {w=2}{nw}"
            m "There is no difference! {w=2} {nw}"
            oldman "Ha! {w=0.1}ha! {w=0.1}ha! {w=0.1}ha! {w=2}{nw}"
            oldman "This was a really good one! {w=3}{nw}"
            oldman "I haven't lough so much since a long time! {w=3.5}{nw}"
            oldman "Thank you very much. {w=3}{nw}"
            if xylo_village_oldman_gem == True:
                oldman "Here. {w=1}That's for you.{w=3}{nw}"
                $ xylo_village_oldman_gem = False
                call take_gem from _call_take_gem_4

        if joke == 3:
            oldman "The space bar! {w=2}{nw}"
            m "Okay okay.. bye. {w=2}{nw}"
        
        $ joke = 0
        return
    
    
    #m "{a=jump:xylo_spaceport_hall}I'm just looking around.{/a} \n\n{a=jump:xylo_spaceport_hall}What are you doing here ?{/a}"
        
    
    $ questions = ["I'm just looking around.{w=2.0} {nw}", 
                    "What are you doing here?{w=2.0} {nw}", 
                    "What a nice weather, isn't it? {w=2.0} {nw}", 
                    "Have you heard about SpaceNET? {w=2.0} {nw}", 
                    "Nothing, thank you. {w=1.0} {nw}"]
    
    while True:
        menu:
            "[questions[0]]" if xylo_village_oldman_flags[0]  == 0:
                m "[questions[0]]"
                oldman "Okay, then look around, hopefully you'll see something, hahaha! {w=4} {nw}"
                $ xylo_village_oldman_flags[0] = 1
                
            "[questions[1]]" if xylo_village_oldman_flags[1]  == 0:
                m "[questions[1]]"
                oldman "Did I ask you any question about you? {w=3} {nw}"
                oldman "No. {w=1} {nw}"
                oldman "So don't ask me stupid questions! {w=3} {nw}"
                $ xylo_village_oldman_flags[1] = 1
                
            "[questions[2]]" if xylo_village_oldman_flags[2]  == 0:
                m "[questions[2]]"
                oldman "Yeah, it is. {w=2} {nw}"
                $ xylo_village_oldman_flags[2] = 1
                
            "[questions[3]]" if xylo_village_oldman_flags[3]  == 0:
                m "[questions[3]]"
                oldman "No, I don't know what are you talking about. {w=3} {nw}"
                $ xylo_village_oldman_flags[3] = 1
            
            "[questions[4]]": #bye
                m "[questions[4]]"
                show npc:
                    linear 1 pos (440,360) rotate 180
                    linear 1 rotate 0
                pause 2
                hide npc
                return
    return
            
    
