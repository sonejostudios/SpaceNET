# MAPS

############################################

init:
    $ xylo_village1_building_alarm = 0
    $ xylo_village1_building_reception = 0
    $ alarm_on = False

    default xylo_building_reception_flags = [0, 0, 0, 0]
    
    default xylo_building_level1_flages = [0, 0, 0, 0]
    default xylo_building_level3_flages = [0, 0, 0, 0]
    
    
    
screen xylo_village1_building_alarm_button() zorder -999:
    #add "#112119"
    
    on "show" action SetVariable("pnc_nodes_visible", False)
    on "hide" action SetVariable("pnc_nodes_visible", True)
    
    imagebutton at topleft: 
        idle "images/maps/bg.png" 
        action [Hide("xylo_village1_building_alarm_button")]
        
      
    add "inventory/inventory.png"
    
    hbox xalign 0.5 yalign 0.5:
        vbox xalign 0.5:
            label "Fire Alarm" at center
            null height 10
            imagebutton: 
                auto "images/buttonbig_%s.png"
                action ToggleVariable("alarm_on", True), Play("sound", "sounds/collect.ogg"), Hide("xylo_village1_building_alarm_button"), Jump("loop_xylo_village1_building") at center
                
    if shadow_enable == 1:
        add "images/shadow.png" align (0.5,0.5)
    

label xylo_village1_building:
    
    stop atmo fadeout 1.0
    
    call music_xylo_building from _call_music_xylo_building
    
    
    image xylo_village1_building = imagemapsdir + "crossroom.png"
    
    scene bgcolor
    show xylo_village1_building at truecenter
    
    if liftpos == 0:
        show screen notify("A.R.K. Corp. building")
    
    show bgcolor behind xylo_village1_building
    
    #doors (comment to disable)
    #show doorh as doorA:
    #    pos (400, 55)
    show doorv as doorB:
        pos (587, 240)
    
    if liftpos == 0:
        show doorh as doorC:
            pos (400, 427)
    #show doorv as doorD:
    #    pos (215, 240)
    


    show text "{color=#8dd35f}{size=+140}[liftpos]{/size}{/color}":
        anchor (0.0,0.0)
        pos (220,50)
        alpha 0.1
    
    
    
    image desk = "images/desk.png"
    
    if liftpos == 0:
        show desk:
            anchor (0.5,0.5)
            pos (400, 190)
        show warningfloor:
            anchor (0.5,0.5)
            pos (400,320)
        
        if alarm_on != True:
            show npc:
                pos (400, 160)
            
    if liftpos == 1:
        show desk:
            anchor (0.5,0.5)
            pos (480, 120)
        
        if xylo_village1_building_alarm < 2:
            show npc:
                pos (480, 90)
                
        show box:
            pos (260,380)
            
        show box as box2:
            pos (400,380)
            
        show box as box3:
            pos (540,380)

            
    if liftpos == 2:
        show desk:
            anchor (0.5,0.5)
            pos (480, 370)
            rotate 180
        show desk as desk2:
            anchor (0.5,0.5)
            pos (480, 120)
        
        if alarm_on != True:
            show npc:
                pos (480, 400)
                
        show box:
            pos (260,380)
            
            
    if liftpos == 3:
        show desk:
            anchor (0.5,0.5)
            pos (280, 300)
            rotate 270
            
        if alarm_on != True:
            show npc:
                pos (240, 300)
                rotate 90
                
        show box:
            pos (440,100)
            
        show box as box2:
            pos (540,100)
        
        show box as box3:
            pos (540,380)

    
    
    # set all variables for the map (nodes and path)
    $ nodeA = (400, 75)
    $ nodeB = (566, 240)
    $ nodeC = (400, 405)
    $ nodeD = (235, 240)
    

    $ nodeAA = (400, 240)
    
    $ nodeBB = (480, 170)
    $ nodeCC = (480, 318)
    $ nodeDD = (330, 300)

    $ pathA = (nodeA, nodeB, nodeC, nodeD, nodeAA, (0, 0), (0, 0), (0, 0))
    $ pathB = ((0, 0), nodeB, nodeC, (0, 0), nodeAA, (0, 0), (0, 0), (0, 0))
    $ pathC = ((0, 0), nodeB, nodeC, (0, 0), nodeAA, (0, 0), (0, 0), (0, 0))
    $ pathD = (nodeA, nodeB, nodeC, nodeD, nodeAA, (0, 0), (0, 0), (0, 0))
    $ pathAA = ((0, 0), nodeB, nodeC, (0, 0), nodeAA, (0, 0), (0, 0), (0, 0))
    $ pathBB = ((0, 0), nodeB, (0, 0), (0, 0), nodeAA, nodeBB, (0, 0), (0, 0))
    $ pathCC = ((0, 0), nodeB, (0, 0), (0, 0), nodeAA, nodeBB, nodeCC, (0, 0))
    $ pathDD = ((0, 0), nodeB, (0, 0), (0, 0), nodeAA, (0, 0), (0, 0), nodeDD)
    
    
    if liftpos == 0:
        $ pathB = ((0, 0), nodeB, nodeC, (0, 0), nodeAA, (0, 0), (0, 0), (0, 0))
        $ pathC = ((0, 0), nodeB, nodeC, (0, 0), nodeAA, (0, 0), (0, 0), (0, 0))
        $ pathAA = ((0, 0), nodeB, nodeC, (0, 0), nodeAA, (0, 0), (0, 0), (0, 0))
    if liftpos == 1:
        $ pathB = ((0, 0), nodeB, (0, 0), (0, 0), nodeAA, nodeBB, (0, 0), (0, 0))
        $ pathAA = ((0, 0), nodeB, (0, 0), (0, 0), nodeAA, nodeBB, (0, 0), (0, 0))
        $ pathBB = ((0, 0), nodeB, (0, 0), (0, 0), nodeAA, nodeBB, (0, 0), (0, 0))
        
    if liftpos == 2:
        $ pathB = ((0, 0), nodeB, (0, 0), (0, 0), nodeAA, nodeBB, nodeCC, (0, 0))
        $ pathAA = ((0, 0), nodeB, (0, 0), (0, 0), nodeAA, nodeBB, nodeCC, (0, 0))
        $ pathBB = ((0, 0), nodeB, (0, 0), (0, 0), nodeAA, nodeBB, nodeCC, (0, 0))
        $ pathCC = ((0, 0), nodeB, (0, 0), (0, 0), nodeAA, nodeBB, nodeCC, (0, 0))
        
    if liftpos == 3:
        $ pathB = ((0, 0), nodeB, (0, 0), (0, 0), nodeAA, (0, 0), (0, 0), nodeDD)
        $ pathAA = ((0, 0), nodeB, (0, 0), (0, 0), nodeAA, (0, 0), (0, 0), nodeDD)
        $ pathDD = ((0, 0), nodeB, (0, 0), (0, 0), nodeAA, (0, 0), (0, 0), nodeDD)
    

     



label loop_xylo_village1_building:
    
    # alarm
    call alarm_check from _call_alarm_check

    # start "move through the map" loop
    call startpos from _call_startpos_3

    # do something at node?
    if exitpos == 1:
        $ startpos = 1 
        jump loop_xylo_village1_building 
        
    if exitpos == 2: # Lift
        $ startpos = 2
        
        if xylo_village1_building_reception >=3:
            call sound_door from _call_sound_door_8
            jump xylo_village1_building_lift
            
        else:
            show npc:
                linear 0.5 rotate -55
            #call sound_scan
            #with flash
            
            guardxylo "Hey! {w=1} {nw}" 
            guardxylo "You are not allowed to go into this building. {w=3} {nw}"
            guardxylo "Go out! {w=1.5} {nw}" 
            m "Okay, okay... {w=1.5} {nw}" 
            show player:
                linear 1 pos nodeC
            pause 1
            call sound_door from _call_sound_door_9
            $ startpos = 33
            jump xylo_village1
            
        
    if exitpos == 3:
        
        # reset alarm
        $ alarm_on = False
        if xylo_village1_building_alarm >= 1:
            $ xylo_village1_building_alarm = 1
        
        call alarm_check from _call_alarm_check_1
        
        $ startpos = 33
        call sound_door from _call_sound_door_10
        stop music fadeout 1.0
        jump xylo_village1
        
    if exitpos == 4:
        $ startpos = 4
        jump loop_xylo_village1_building 
        

    #exits routing "got to map and set position for next map"
    if exitpos == 11:
        if startpos == 11:
            if liftpos == 0:
                if alarm_on != True:
                    jump xylo_village1_building_reception # reception
                else:
                    call dialog_nothing from _call_dialog_nothing_5
                    
            else:
                m "I'm on floor number [liftpos]. {w=2} {nw}"
        $ startpos = 11     
        jump loop_xylo_village1_building   
        
    
    if exitpos == 22:
        if startpos == 22 and liftpos == 1 and xylo_village1_building_alarm < 2: # level 1 worker
            
            if inventory_select != "":
                call npc_dont_need_item(worker1) from _call_npc_dont_need_item_11
                jump loop_xylo_village1_building   
            
            worker1 "What do you want? {w=1.5} {nw}"
                
            $ questions = ["I'm just looking around. {w=2.0} {nw}", 
                            "Your colleague on level 3 needs help with the fire alarm I think... {w=3} {nw}", 
                            "Nothing, thank you. {w=1.0} {nw}"]
                            
            menu:
                "[questions[0]]" if xylo_building_level3_flages[0] == 0:
                    m "[questions[0]]"
                    worker1 "I don't have time to have a talk with you, sorry! {w=3.0} {nw}"
                    $ xylo_building_level3_flages[0] = 1
                    
                "[questions[1]]" if xylo_village1_building_alarm == 1:
                    m "[questions[1]]"
                    worker1 "Okay, thank you, I'll go up straight away. {w=2.5} {nw}"
                    
                    show npc:
                        linear 0.5 rotate 180
                        linear 0.5 ypos 70
                        linear 0.5 rotate 90
                        linear 1 xpos 400
                        linear 0.5 rotate 0
                        linear 1 ypos 240
                        linear 0.5 rotate -90
                        linear 1 pos nodeB
                        
                    pause 5.5
                    $xylo_village1_building_alarm = 2
                    hide npc
                    call sound_door from _call_sound_door_11
                    jump loop_xylo_village1_building
                    
                "[questions[2]]":
                    m "[questions[2]]"
                    worker1 "Okay, bye. {w=1} {nw}"
                        
            
        if startpos == 22 and liftpos == 1 and xylo_village1_building_alarm == 2:   # level 1 no worker set alarm!
            if alarm_on != True:
                m "There is the fire alarm...{w=2.0} {nw}"
            
            if inventory_select != "":
                call dialog_nosense from _call_dialog_nosense_32
            else:
                show screen xylo_village1_building_alarm_button
            
            

            
            
        if startpos == 22 and liftpos == 2 and alarm_on != True: # empty desk level 2
            worker2 "Hey! {w=1} {nw}"
            worker2 "What are you looking for? {w=2.5} {nw}"
            worker2 "You are not allowed to be here! {w=2.5} {nw}"
            worker2 "I'll call the guard now! {w=2.0} {nw}"
            worker2 "Guaaaard! {w=1} {nw}"
            jump xylo_village1_building_kickout
            
        if startpos == 22 and liftpos == 2 and alarm_on == True:
            call dialog_nothing from _call_dialog_nothing_6
        
        $ startpos = 22
        jump loop_xylo_village1_building 
        
    if exitpos == 33:

        if startpos == 33 and liftpos == 2 and alarm_on != True: # level 2
            
            if inventory_select != "":
                call npc_dont_need_item(worker2) from _call_npc_dont_need_item_12
                jump loop_xylo_village1_building  
            
            worker2 "Hmm? {w=1} {nw}"
            worker2 "What are you doing here? {w=2.0} {nw}"
            worker2 "Please don't bother me and let me do my work. {w=2.5} {nw}"
            
        if alarm_on == True: # get AccessCard
            if "accesscard" not in inventory:
                m "Oh, there is an access card on the desk! {w=2.5} {nw}"
                call take_item("accesscard") from _call_take_item
            else:
                call dialog_nothing from _call_dialog_nothing_7
            
        
        $ startpos = 33
        jump loop_xylo_village1_building
        
        
    if exitpos == 44:
        
        if startpos == 44 and liftpos == 3 and alarm_on != True: # level 3
            jump xylo_village1_building_level3
            
        
        if startpos == 44 and liftpos == 3 and alarm_on == True and cash_xylo_building > 0:
            m "There is some money on the desk. Oh nice, I'm rich!{w=3} {nw}"
            call io_cash(cash_xylo_building) from _call_io_cash
            $ cash_xylo_building = 0
            
        if startpos == 44 and liftpos == 3 and alarm_on == True and cash_xylo_building == False:
            call dialog_nothing from _call_dialog_nothing_8
            
        $ startpos = 44
        
        jump loop_xylo_village1_building




label xylo_village1_building_reception:
    
    if inventory_select != "":
        
        if inventory_select == "accesscard":
            guardxylo "Hey! Where have you found this access card? {w=3} {nw}"
            guardxylo "Give it to me! {w=2} {nw}"
            m "No!{w=2} {nw}"
            $ inventory_select = ""
            show player:
                linear 0.5 pos nodeC
            pause 0.5
            call sound_door from _call_sound_door_176
            $ startpos = 33
            jump xylo_village1
        
        call npc_dont_need_item(guardxylo) from _call_npc_dont_need_item_13
        jump loop_xylo_village1_building   
        
    
    guardxylo "Hi.{w=2} {nw}"
    guardxylo "What do you want? {w=2} {nw}"

    $ questions = ["I'm just looking around...{w=2.0} {nw}", 
                        "What is inside this building? {w=2.0} {nw}",
                        "Is it possible to visit this building? {w=2.0} {nw}",
                        "I have an appointment. {w=2.0} {nw}",
                        "Nothing, thank you. {w=1.0} {nw}"]
    
    while True:
        menu:
            "[questions[0]]" if xylo_building_reception_flags[0] == 0:
                m "[questions[0]]"
                guardxylo "There is nothing to see here. {w=2.0} {nw}"
                guardxylo "Bye! {w=1.0} {nw}"
                $ xylo_building_reception_flags[0] = 1
            
            "[questions[1]]" if xylo_building_reception_flags[1] == 0:
                m "[questions[1]]"
                guardxylo "This is the building of A.R.K. Corporation. {w=2.5} {nw}"
                guardxylo "We are a universal company with the goal, {w=2.5} {nw}"
                guardxylo "doing as much as possible to help the government. {w=2.5} {nw}"
                guardxylo "If you have any questions, just ask me. {w=2.5} {nw}"
                $ xylo_village1_building_reception = 1
                $ xylo_building_reception_flags[1] = 1
                
            "[questions[2]]" if xylo_village1_building_reception >= 1:
                m "[questions[2]]"
                guardxylo "It is not possible to visit the building right now, sorry... {w=3.5} {nw}"
                guardxylo "Please call the A.R.K. central to make an appointment if you want to visit... {w=5} {nw}"
                guardxylo "Our phone number is 01020304. {w=3} {nw}"
                guardxylo "Just type it in the terminal to call us. {w=3} {nw}"
                guardxylo "See you. {w=1.5} {nw}"
                call add_note("A.R.K. Corporation Office number: 01020304") from _call_add_note_1
                
            "[questions[3]]" if xylo_village1_building_reception >= 2:
                m "[questions[3]]"
                guardxylo "What is your name? {w=2.5} {nw}"
                m "My name is [playername]. {w=2.5} {nw}"
                guardxylo "Wait... {w=1.5} {nw}"
                guardxylo "... {w=1.5} {nw}"
                guardxylo "Okay, no problem, I'll let you in. {w=2.5} {nw}"
                call sound_collect from _call_sound_collect
                with flash
                guardxylo "Welcome to A.R.K. Corporation! {w=3} {nw}"
                $ xylo_village1_building_reception = 3
                jump loop_xylo_village1_building 
                
                 
            "[questions[4]]":
                m "[questions[4]]"
                guardxylo "Okay bye! {w=2} {nw}"
                jump loop_xylo_village1_building 
    
  
    
    
label xylo_village1_building_level3: # level 3
    
    if inventory_select != "":
        call npc_dont_need_item(worker3) from _call_npc_dont_need_item_14
        jump loop_xylo_village1_building  
    
    worker3 "Hello... {w=1} {nw}"
    worker3 "what can I do for you? {w=2.5} {nw}"
       
 
    
    $ questions = ["Nothing, I'm just looking around. {w=2.0} {nw}", 
                    "What are you doing here?{w=2.0} {nw}", 
                    "I'm from the bureau of safety inspections. {w=2.0} {nw}", 
                    "Nothing, thank you. {w=1.0} {nw}"]
    
    while True:
        menu:
            "[questions[0]]" if xylo_building_level3_flages[0] == 0:
                m "[questions[0]]"
                worker3 "This is a restricted area... {w=2} {nw}"
                worker3 "There is nothing to see here! {w=2} {nw}"
                worker3 "If you continue asking I'll call the guard! {w=3} {nw}"
                $ xylo_building_level3_flages[0] = 1
                
            "[questions[1]]" if xylo_building_level3_flages[1] == 0:
                m "[questions[1]]"
                worker3 "Hey, that's my business, not yours. {w=2} {nw}"
                worker3 "Go out!{w=1.5} {nw}"
                worker3 "You don't want to go out? {w=2} {nw}"
                worker3 "I'll call the guard now! {w=2} {nw}"
                $ xylo_building_level3_flages[1] = 1
                
                
                $ questions = ["Please don't! I will go...{w=2} {nw}", 
                                "Pff, I don't mind. {w=2} {nw}"]
                menu:
                    "[questions[0]]":
                        m "[questions[0]]"
                        show player:
                            linear 1 pos nodeB
                        pause 1
                        call sound_door from _call_sound_door_12
                        jump xylo_village1_building_lift
                        
                    "[questions[1]]":
                        m "[questions[1]]"
                        worker3 "Whaaaaaat? {w=1} {nw}"
                        worker3 "Okay... I'll kick you out! {w=2} {nw}"
                        worker3 "Guaaaard! {w=1} {nw}"
                        jump xylo_village1_building_kickout
                
                
            "[questions[2]]" if xylo_building_level3_flages[2] == 0:
                m "[questions[2]]"
                worker3 "Oh... Hello inspector. {w=2} {nw}"
                worker3 "I'm so sorry I thought you were an annoying guy. {w=3} {nw}"
                worker3 "Here is nothing you need to worry about! {w=3} {nw}"
                worker3 "What can I do for you? {w=2} {nw}"
                m "Do you have a functional fire alarm in your building? {w=3} {nw}"
                worker3 "Yes, of course, it is here at the desk. {w=3} {nw}"
                
                $ xylo_village1_building_alarm = 1
                
                m "Okay, thank you for the information, bye! {w=3} {nw}"
                
                $ xylo_building_level3_flages[2] = 1
                
            
            "[questions[3]]":
                m "[questions[3]]"
                worker3 "Okay, bye! {w=2} {nw}"
                jump loop_xylo_village1_building
                
                
                
                
label xylo_village1_building_kickout:
    call sound_scan from _call_sound_scan
    with flash
    show npc as guard:
        rotate 90
        pos nodeB
        linear 1 pos position
    pause 1
    
    show npc as guard:
        linear 0.5 rotate 270
        linear 1 pos nodeB
    pause 0.5
    
    show player:
        linear 1 pos nodeB
    pause 1
    
    call sound_door from _call_sound_door_13

    $ startpos = 33
    jump xylo_village1
