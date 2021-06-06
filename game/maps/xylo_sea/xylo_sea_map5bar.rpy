
##############################################

init:
    default xylo_sea_barman_flags = [0, 0]
    default xylo_sea_bar_client1_flags = [0, 0, 0]

    $ xylo_sea_bar_client1_letter = 0
    
    $ xylo_sea_bar_music = 3


label xylo_map5house:
    
    stop atmo fadeout 1.0
    
    image xylo_bar = imagemapsdir + "crossroom.png"
    
    image terminalmap = "images/terminalmap.png"
    
    scene bgcolor
    show screen notify("Sea Settlement Bar")
    
    show xylo_bar at truecenter
    
    show doorv:
        pos (585,240)
        
    show terminalmap:
        anchor (0.5,0.5)
        pos (470,405)
    
    show table:
        pos (320,110)
        
    show npc:
        pos (320,65)
        
    show table as table2:
        pos (490,110)
        
    show table as table3:
        pos (283,330)
        rotate 90
        
    show npc as npc2:
        pos (233,330)
        rotate 90
        
        
    show buttonscreen:
        pos (215, 210)
        rotate 90
        
    
    
    
    # set all variables for the map (nodes and path)
    $ nodeA = (330,330)
    $ nodeB = (400,240)
    $ nodeC = (670,250)
    $ nodeD = (470,366)
    
    $ nodeAA = (321,156)
    $ nodeBB = (560,240)
    $ nodeCC = (400,460)
    $ nodeDD = (238, 208)
    
    $ pathA = (nodeA, nodeB, (0,0), nodeD, nodeAA, nodeBB, (0,0), (0,0))
    $ pathB = (nodeA, nodeB, (0,0), nodeD, nodeAA, nodeBB, (0,0), nodeDD)
    $ pathC = ((0,0), nodeB, (0,0), nodeD, (0,0),(0,0),(0,0), (0,0))
    $ pathD = (nodeA, nodeB, (0,0), nodeD, nodeAA, nodeBB, (0,0), nodeDD)
    
    $ pathAA = (nodeA, nodeB, (0,0), nodeD, nodeAA, nodeBB, (0,0), nodeDD)
    $ pathBB = (nodeA, nodeB, (0,0), nodeD, nodeAA, nodeBB, (0,0), nodeDD)
    $ pathCC = ((0,0), (0,0), nodeC, (0,0), (0,0), (0,0), (0,0), (0,0))
    $ pathDD = ((0,0), nodeB, (0,0), nodeD, nodeAA, nodeBB, (0,0), nodeDD)




label loop_xylo_map5house:
    
    
    if xylo_sea_bar_music == 1:
        call music_bar_village from _call_music_bar_village_2
    
    if xylo_sea_bar_music == 2:
        call music_bar_chill from _call_music_bar_chill_2
        
    if xylo_sea_bar_music == 3:
        call music_outro from _call_music_outro_1
    
    if xylo_sea_bar_music == 4:
        stop music fadeout 1.0
    
    
    
    while True:
        # start "move through the map" loop
        call startpos from _call_startpos_32
        
        # do something at node?
        if exitpos == 1:       #if at node A
            if startpos == 1:
                call xylo_sea_bar_barman from _call_xylo_sea_bar_barman
            
            $ startpos = 1     # stay in A
            
        if exitpos == 2:
            if startpos == 2:
                if inventory_select == "":
                    m "This is the settlement bar.{w=2.5}{nw}"
                else:
                    call dialog_nosense from _call_dialog_nosense_49
            $ startpos = 2
            
        if exitpos == 3:
            $ startpos = 3
            
        if exitpos == 4:
            if startpos == 4:
                call terminal from _call_terminal_6
            
            $ startpos = 4

        
        #exits routing "got to map"
        if exitpos == 11:      
            if startpos == 11:
                call xylo_sea_bar_client1 from _call_xylo_sea_bar_client1
                    
            $ startpos = 11  

            
        if exitpos == 22:
            $ startpos = 44
            call sound_door from _call_sound_door_80
            jump xylo_map4
            
        if exitpos == 33:
            $ startpos = 33


        if exitpos == 44:
            if startpos == 44:
                show screen xylo_sea_bar_jukebox
            $ startpos = 44


    
label xylo_sea_bar_barman:
    
    if inventory_select == "":
        #if xylo_sea_barman_flags[0] == 0:
        barman_xsea "Hello, can I see your membership card? {w=3}{nw}"
        
        menu:
            "I don't have one." if xylo_sea_barman_flags[0] == 0:
                m "I don't have one.{w=2}{nw}"
                barman_xsea "No card, nothing.{w=2}{nw}"
                barman_xsea "Bye.{w=1}{nw}"
                $ xylo_sea_barman_flags[0] = 1
            
            "Is this the bar?" if xylo_sea_barman_flags[1] == 0:
                m "Is this the bar?{w=2}{nw}"
                barman_xsea "This is a private bar, yes.{w=2}{nw}"
                m "Do you know where I can buy a drink?{w=2}{nw}"
                barman_xsea "If you are not a member, you can't, I'm sorry.{w=3}{nw}"
                m "What?{w=2}{nw}"
                barman_xsea "Yes, it is like this, only members are allowed to buy drinks here.{w=4}{nw}"
                barman_xsea "Now, let me do my work.{w=3}{nw}"
                barman_xsea "Bye.{w=1}{nw}"
                $ xylo_sea_barman_flags[1] = 1
            
            "I'll go, bye.":
                m "I'll go, bye.{w=1.5}{nw}"

        return
    
    
    elif inventory_select == "accesscard" or inventory_select == "robotcard":
        #barman "This is the wrong card, sorry. {w=3}{nw}"
        $ inventory_select = ""
        barman_xsea "What? Are you from A.R.K. Corporation? {w=3.5}{nw}"
        barman_xsea "Go out of this room, right now! {w=3}{nw}"
        m "Okay, okay...{w=2}{nw}"
        
        show player:
            pos nodeA
            linear 0.5 pos nodeBB
        pause 0.5
        
        call sound_door from _call_sound_door_81
        $ startpos = 44
        jump xylo_map4
        #return
    
    else:
        call npc_dont_need_item(barman_xsea) from _call_npc_dont_need_item_2
        return
    
    






label xylo_sea_bar_client1:
    
    if inventory_select == "":
        
        clientsea "Hey. {w=2} {nw}"
        
        $ questions_client = ["Hi! My name is...{w=3} {nw}", 
                                "What are you doing here?{w=3} {nw}", 
                                "Have you heard about SpaceNET? {w=3} {nw}", 
                                "Okay, bye. {w=1.5} {nw}"]

        while True:
            menu:
                "[questions_client[0]]" if xylo_sea_bar_client1_flags[0] == 0: #how are you
                    m "Hi! My name is [playername].{w=3.5} {nw}"
                    clientsea "Hi [playername]. {w=3} {nw}"
                    m "Do we know each other? {w=3.5} {nw}"
                    clientsea "No, sorry, I've never seen you around. {w=3.5} {nw}"
                    clientsea "Why are you asking? {w=2.5} {nw}"
                    m "Oh, I was just wondering if somebody knows me. {w=3.5} {nw}"
                    clientsea "... {w=2} {nw}"
                    clientsea "Well, you don't need to know who knows you, if you already know the people, right? {w=6} {nw}"
                    clientsea "I really don't understand why you are asking around... if somebody knows you or not. {w=6} {nw}"
                    clientsea "Are you okay?{w=2.5} {nw}"
                    m "... {w=2} {nw}"
                    m "Listen, this is a weird story. {w=3.5} {nw}"
                    m "I woke up this morning with no memory.{w=3.5} {nw}"
                    m "I just forgot everything!{w=2.5} {nw}"
                    m "... {w=2} {nw}"
                    clientsea "You are a lucky person. {w=3} {nw}"
                    clientsea "... {w=2} {nw}"
                    m "I really don't think so. {w=3} {nw}"
                    clientsea "I would like to forget everything. {w=3.5} {nw}"
                    clientsea "I need a drink. {w=3} {nw}"
                    m "What do you want to forget?{w=3.5} {nw}"
                    clientsea "Nothing, that's private. {w=3.5} {nw}"
                    clientsea "I don't want to talk about it. {w=3.5} {nw}"
                    
                    $ xylo_sea_bar_client1_flags[0] = 1
                    
                "[questions_client[1]]" if xylo_sea_bar_client1_flags[1] == 0: #how are you
                    m "[questions_client[1]]"
                    clientsea "What I'm doing here? Drinking to forget! {w=4} {nw}"
                    clientsea "I worked in the silver mine in the northwest. {w=4} {nw}"
                    clientsea "But they closed it, so now I don't know what to do! {w=4} {nw}"
                    clientsea "The worse, they didn't give me back my personal documents. {w=5} {nw}"
                    clientsea "So I can't apply for a new job anywhere... {w=3.5} {nw}"
                    clientsea "And if I want to renew all my documents, I need to pay...{w=5} {nw}"
                    clientsea "Guess. {w=2} {nw}"
                    
                    menu:
                        "10c?":
                            m "10c?{w=2} {nw}"
                            clientsea "Are you kidding?{w=3} {nw}"
                        "50c?":
                            m "50c?{w=2} {nw}"
                            clientsea "That would be nice!{w=3} {nw}"
                        "100c?":
                            m "100c?{w=2} {nw}"
                            clientsea "Way more!{w=3} {nw}"
                        "I don't know.":
                            m "I don't know.{w=2} {nw}"
                            $ x=1
                            
                    clientsea "... {w=2} {nw}"
                    clientsea "If I want to renew all my documents, I need to pay...{w=4} {nw}"
                    clientsea "1000c! {w=2.5} {nw}"
                    clientsea "This is just crazy! {w=2.5} {nw}"
                    m "Oh yes, that's a lot of money.{w=3.5} {nw}"
                    $ xylo_sea_bar_client1_flags[1] = 1
                    
                 
                "[questions_client[2]]" if xylo_sea_bar_client1_flags[2] == 0: # spacenet?
                    m "[questions_client[2]]"
                    clientsea "SpaceNET?... {w=2}{nw}"
                    clientsea "I heard, it is a new project by the.... {w=4}{nw}"
                    clientsea "...by the... {w=2.5}{nw}"
                    clientsea "That's all I know. {w=3}{nw}"
                    clientsea "Sorry. {w=2}{nw}"
                    $ xylo_sea_bar_client1_flags[2] = 1
                        
                
                "[questions_client[3]]": # bye
                    m "[questions_client[3]]"
                    clientsea "Bye. {w=1}{nw}"
                    return

        return
        
        
    elif inventory_select == "letter":
        call use_item from _call_use_item_3
        m "I think this belongs to you.{w=3}{nw}"
        m "I met a miner in the bar in [xylo_village_name]. He gave me this letter for you.{w=5}{nw}"
        
        clientsea "Oh, that's amazing!{w=2.5}{nw}"
        clientsea "These are my personal documents.{w=3}{nw}"
        clientsea "Thank you very much.{w=2.5}{nw}"
        clientsea "...{w=2}{nw}"
        clientsea "You know what?{w=2.5}{nw}"
        clientsea "I think I'm a bit drunk.{w=2.5}{nw}"
        clientsea "But I don't care!{w=2.5}{nw}"
        clientsea "I'll give you 100c for this favor.{w=3}{nw}"
        clientsea "It's worth it to me.{w=2.5}{nw}"
        clientsea "Now I have all I need!{w=2.5}{nw}"
        clientsea "And I can start a new life!{w=2.5}{nw}"
        clientsea "That's the best thing ever.{w=2.5}{nw}"
        
        call io_cash(100) from _call_io_cash_10

        m "Nice, thank you!{w=2.5}{nw}"
        clientsea "You are really welcome.{w=2.5}{nw}"
        clientsea "Bye!{w=2.5}{nw}"
        
        
        $ xylo_sea_bar_client1_letter = 1
        
        return
        
    
    else:
        call npc_dont_need_item(clientsea) from _call_npc_dont_need_item_3
        return

    
    
 
 
#button screen
screen xylo_sea_bar_jukebox() zorder -999:
    #add "#112119"
    
    on "show" action SetVariable("pnc_nodes_visible", False)
    on "hide" action SetVariable("pnc_nodes_visible", True)
    
    imagebutton: 
        idle "images/maps/bg.png" 
        action Hide("xylo_sea_bar_jukebox") at topleft
            
    add "inventory/inventory.png"

    
    label "Jukebox":
        align (0.5, 0.25)
        
    
    hbox xalign 0.5 yalign 0.6:
        
        vbox xalign 0.5:
            imagebutton:
                auto "images/buttonbig_%s.png" 
                action SetVariable("xylo_sea_bar_music", 1), Jump("loop_xylo_map5house")#, Hide("xylo_village_bar_jukebox") at center
            null height 10
            label "1" at center
            
        null width 50
        
        vbox xalign 0.5:
            imagebutton:
                auto "images/buttonbig_%s.png" 
                action SetVariable("xylo_sea_bar_music", 2), Jump("loop_xylo_map5house")#, Hide("xylo_village_bar_jukebox") at center
            null height 10
            label "2" at center
                
        null width 50
        
        vbox xalign 0.5:
            imagebutton: 
                auto "images/buttonbig_%s.png" 
                action SetVariable("xylo_sea_bar_music", 3), Jump("loop_xylo_map5house")#, Hide("xylo_village_bar_jukebox") at center
            null height 10
            label "3" at center
            
            
        null width 50
        
        vbox xalign 0.5:
            imagebutton: 
                auto "images/buttonbig_%s.png" 
                action SetVariable("xylo_sea_bar_music", 4), Jump("loop_xylo_map5house")#, Hide("xylo_village_bar_jukebox") at center
            null height 10
            label "None" at center
            
                
                
    if shadow_enable == 1:
        add "images/shadow.png" align (0.5,0.5)
