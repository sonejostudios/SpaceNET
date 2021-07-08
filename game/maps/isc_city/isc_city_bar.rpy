# MAPS

############################################

init:
    $ isc_bar_client = False
    #$ isc_bar_client = True
    
    $ sam_numpad_mission = 0
    
    default isc_bar_barman_flags = [0, 0, 0, 0]
    default isc_bar_client1_flags = [0, 0, 0, 0]
    default isc_bar_client3_flags = [0, 0, 1, 0]
    
    
    $ isc_sysadmin_move = 0 #0=start at bar, 1=at crane, 2=crane repaired, 3=sun radiation and thanks
    $ isc_sysadmin_sun = 0

    $ spacebar_joke = False
    
    $ isc_bar_music = 2
    

    
    

label isc_city_bar:
    
    stop atmo

    #$ steps_sound = "concrete"
    
    image isc_city_bar = imagemapsdir + "isc_city_bar.png"
    
    scene bgcolor
    show screen notify("ISC Center Bar")
    
    hide screen isc_cardgame_check
    
    show isc_city_bar:
        pos (0,0)
        
        
    show npc as barman:
        pos (400, 55)
        rotate 90
        linear 2 pos (500, 55)
        linear 1 rotate 270
        linear 4 pos (300, 55)
        linear 1 rotate 90
        linear 2 pos (400, 55)
        repeat
        

        
    show npc as client2:
        pos (394, 434)

    show npc as client3:
        pos (614, 403)
        rotate 270
        
        
    show buttonscreen:
        pos (168, 160)
        rotate 90

    
    
    # set all variables for the map (nodes and path)
    $ nodeA = (188, 246)
    $ nodeB = (371, 150)
    $ nodeC = (612, 293)
    $ nodeD = (550, 345)

    $ nodeAA = (398, 345)
    $ nodeBB = (247, 345)
    $ nodeCC = (572, 162)
    $ nodeDD = (190, 159)

    $ pathA = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)
    $ pathB = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)
    $ pathC = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)
    $ pathD = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)
     
    $ pathAA = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)
    $ pathBB = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)
    $ pathCC = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)
    $ pathDD = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)
    



label loop_isc_city_bar:
    
    
    if isc_bar_music == 1:
        call music_bar_village from _call_music_bar_village_1
    
    if isc_bar_music == 2:
        call music_bar_chill from _call_music_bar_chill_1
        
    if isc_bar_music == 3:
        call music_outro_bar from _call_music_outro_bar_1
    
    if isc_bar_music == 4:
        stop music fadeout 1.0
    
    
    
    while True:
        
        if isc_sysadmin_move != 1:
            show npc as client1:
                pos (245, 434)


        # start "move through the map" loop
        call startpos from _call_startpos_26

        # do something at node?
        if exitpos == 1:
            call sound_door from _call_sound_door_62
            $ startpos = 11
            
            $ drunk_level = 0
            jump isc_city_center


        # barman
        if exitpos == 2:
            if startpos == 2:
                call isc_barman from _call_isc_barman
                
            $ startpos = 2

            
        if exitpos == 3:
            if startpos == 3:
                if isc_bar_client == True:
                    $ startpos = 1
                    call sound_door from _call_sound_door_63
                    jump isc_city_bar_toilets
                else:
                    call dialog_closed from _call_dialog_closed_12
            $ startpos = 3
            
        

        # client east
        if exitpos == 4:
            if startpos == 4:
                call isc_bar_client_east from _call_isc_bar_client_east
                
            $ startpos = 4
           


        #player
        if exitpos == 11:
            if startpos == 11:
                call isc_bar_player from _call_isc_bar_player
            $ startpos = 11 


        # sys admin
        if exitpos == 22: #client 1 sys admin
            if startpos == 22:
                call isc_bar_sysadmin from _call_isc_bar_sysadmin 
            $ startpos = 22

            
        if exitpos == 33: # terminal
            if startpos == 33:
                if sam_numpad_mission == 0:
                    $ inbox_new_message = "*"
                    call notify_new_message from _call_notify_new_message
                    
                    $ server_msglist[4] = "5. important meeting"
                
                call terminal from _call_terminal_5
            $ startpos = 33
            

            
        if exitpos == 44: # jukebox
            if startpos == 44:
                #$ pnc_nodes_visible = False
                show screen isc_bar_jukebox
            $ startpos = 44
            



# client east girl
label isc_bar_client_east:
    
    if isc_bar_client3_gem == True and inventory_select == "asteroid":
        call use_item from _call_use_item_11
        m "Here, I brought you a piece of an asteroid. {w=4} {nw}"
        clientisc3 "Oh, thank you!{w=2.5} {nw}"
        clientisc3 "Here, this gem is for you.{w=3} {nw}"
        call take_gem from _call_take_gem_14
        $ isc_bar_client3_gem = False
        m "Thank you very much! {w=2.5} {nw}"
        clientisc3 "Thank you for the asteroid piece!{w=3.5} {nw}"
        return
        
    
    
    if inventory_select != "":
        call npc_dont_need_item(clientisc3) from _call_npc_dont_need_item_7
        return
        

    
    if drunktime > 0:
        call dialog_joke from _call_dialog_joke_3
        if joke == 1:
            clientisc3 "I know it already.{w=2.5} {nw}"
            clientisc3 "Please, stop bothering me with these not-funny-jokes. {w=4.5} {nw}"
            m "Okay, sorry... {w=2} {nw}"
            
        if joke == 2:
            clientisc3 "I don't know... {w=2} {nw}"
            m "There is no difference! {w=2} {nw}"
            clientisc3 "Ha! {w=0.1}ha! {w=0.1}ha! {w=2}{nw}"
            clientisc3 "Nice joke! {w=2} {nw}"
        
        if joke == 3:
            clientisc3 "I don't know... tell me. {w=2.5} {nw}"
            m "The space bar! {w=2} {nw}"
            clientisc3 "Hi! {w=0.1}hi! {w=0.1}hi! {w=0.1}hi! {w=2}{nw}"
            clientisc3 "Very nice joke! {w=2} {nw}"
            clientisc3 "Do you know what? {w=2.5} {nw}"
            clientisc3 "I've seen a gem in the first sink of the bathroom. {w=4} {nw}"
            clientisc3 "But I couldn't manage to get it out! {w=3.5} {nw}"
            clientisc3 "Such a nice gem... {w=2.5} {nw}"
            clientisc3 "If you manage to get it out, you are a happy person!{w=4} {nw}"
            m "Oh... thanks for the hint! {w=2} {nw}"
            clientisc3 "You are welcome. {w=2.5} {nw}"
            clientisc3 "Bye! {w=1.5} {nw}"

        $ joke = 0    
        return
        
    
    clientisc3 "Hi! {w=2}{nw}"
    
    $ questions = ["Hello...{w=2.0} {nw}", 
                    "What are you doing here?{w=3} {nw}", 
                    "What do you think about the gems? {w=3}{nw}", 
                    "Bye! {w=2} {nw}"]
    
    
    
    while True:
        menu:
            "[questions[0]]" if isc_bar_client3_flags[0]  == 0:
                m "[questions[0]]"
                clientisc3 "Yes? {w=2}{nw}"
                m "Hey... {w=1.5}... {w=1}...{w=1}{nw}"
                clientisc3 "? {w=1.5}{nw}"
                $ isc_bar_client3_flags[0] = 1
                
            "[questions[1]]" if isc_bar_client3_flags[1]  == 0:
                m "[questions[1]]"
                clientisc3 "I'm having a drink in the bar. {w=3.5}{nw}"
                clientisc3 "But I'm also thinking about all these gems. {w=4.5}{nw}"
                $ isc_bar_client3_flags[1] = 1
                $ isc_bar_client3_flags[2] = 0
                
            "[questions[2]]" if isc_bar_client3_flags[2]  == 0:
                m "[questions[2]]"
                clientisc3 "Do you know anything about them? {w=3.5}{nw}"
                m "Well, I heard there are powerful. {w=3.5}{nw}"
                clientisc3 "Might be, but they also looks beautiful! {w=4}{nw}"
                clientisc3 "Look at this one! {w=3}{nw}"
                menu:
                    "Yeah, this is a nice one!":
                        m "Yeah, this is a nice one! {w=3}{nw}"
                        clientisc3 "Indeed! {w=2}{nw}"
                    "Actually, I collect them":
                        m "Actually, I collect them. {w=3}{nw}"
                        m "Would you like to give it to me? {w=3}{nw}"
                        clientisc3 "No way! {w=2.5}{nw}"
                        clientisc3 "I might need it one day! {w=3.5}{nw}"
                    "Wow":
                        m "Wow. {w=2}{nw}"
                        clientisc3 "I would say the same. {w=3}{nw}"
                clientisc3 "Do you know where they are coming from? {w=4}{nw}"
                menu:
                    "Well...":
                        m "Well... {w=2}{nw}"
                    "No":
                        m "No. {w=2}{nw}"   
                    "Tell me!":
                        m "Tell me! {w=2}{nw}"
                    
                clientisc3 "I heard they are coming from an asteroid field. {w=4.5}{nw}"
                clientisc3 "Wait... {w=2}{nw}"
                clientisc3 "You look like an adventurer... {w=3.5}{nw}"
                clientisc3 "Listen. {w=2}{nw}"
                clientisc3 "If you want one, then try to locate 'asteroids' in the terminal and have a look by yourself. {w=6.5}{nw}"
                call add_note(note_locate_asteroids) from _call_add_note_14
                clientisc3 "And if you go there... {w=3.5}{nw}"
                clientisc3 "You know what? {w=3.5}{nw}"
                clientisc3 "Actually I would love to have a real asteroid piece. {w=4}{nw}"
                clientisc3 "If you bring me an asteroid piece, I'll give you this gem. {w=4.5}{nw}"
                m "Okay, good to know! {w=2}{nw}"
                $ isc_bar_client3_flags[2] = 1
                
            "[questions[3]]":
                m "[questions[3]]"
                clientisc3 "Bye-bye! {w=1.5}{nw}"
                return
    
    return



# sysadmin
label isc_bar_sysadmin:
    if inventory_select != "" and isc_sysadmin_move != 1:
        call npc_dont_need_item(clientsysadmin) from _call_npc_dont_need_item_8
        return
    
    
    if isc_sysadmin_move == 0:
        clientsysadmin "Hello!{w=2}{nw}"
        
        $ questions = ["Hi!\nMy name is "+ playername +".{w=2.0} {nw}", 
                        "What are you doing here?{w=2.0} {nw}", 
                        "I can help you if you like. {w=2.0} {nw}", 
                        "Work? You are having a drink in the bar! {w=2.0} {nw}", 
                        "Nothing, thank you. {w=1.0} {nw}"]
        
        while True:
            menu:
                "[questions[0]]" if isc_bar_client1_flags[0]  == 0:
                    m "Hi! My name is [playername].{w=3} {nw}"
                    m "Do you know me by chance?{w=3} {nw}"
                    clientsysadmin "No, I've never seen you before.{w=4} {nw}"
                    clientsysadmin "Why are you asking?{w=3} {nw}"
                    m "Well, I lost my memory...{w=3} {nw}"
                    clientsysadmin "Ha ha! {w=1}Nice joke!{w=1} I lost my memory as well.{w=3} {nw}"
                    menu:
                        "Really?":
                            m "Really?{w=2} {nw}"
                        "This is not a joke.":
                            m "This is not a joke.{w=2.5} {nw}"
                        "I'm serious!":
                            m "I'm serious!{w=2.5} {nw}"
                            
                    clientsysadmin "Are you a system administrator?{w=3} {nw}"
                    clientsysadmin "No... {w=1} I'm not.{w=3} {nw}"
                    clientsysadmin "I knew that.w=2} {nw}"
                    clientsysadmin "Stupid job. You are a lucky person!{w=3} {nw}"
                    m "Well...{w=2.5} {nw}"
                    m "I really don't know...{w=2.5} {nw}"
                    clientsysadmin "I'm the system administrator of the Industrial Space City.{w=5} {nw}"
                    clientsysadmin "But this small thingy needs a lot of maintenance!{w=5} {nw}"
                    clientsysadmin "It is just falling apart.{w=5} {nw}"
                    clientsysadmin "If you know a system administrator who could help me, please let me know.{w=5} {nw}"
                    m "Sure.{w=2.5} {nw}"
                    clientsysadmin "Okay, enough for now, I've things to do.{w=3.5} {nw}"
                    clientsysadmin "Please, let me do my work.{w=3} {nw}"
                    $ isc_bar_client1_flags[0] = 1
                
                "[questions[1]]" if isc_bar_client1_flags[1]  == 0:
                    m "[questions[1]]"
                    clientsysadmin "I'm just having a rest before I'll fix the next problem.{w=5} {nw}"
                    clientsysadmin "They are tons of things to do here.{w=3.5} {nw}"
                    clientsysadmin "But I'm tired of fixing problems.{w=3.5} {nw}"
                    clientsysadmin "That's a lot of work!{w=3} {nw}"
                    $ isc_bar_client1_flags[1] = 1
                
                "[questions[2]]" if isc_bar_client1_flags[2] == 0 and isc_bar_client1_flags[1]  == 1:
                    m "[questions[2]]"
                    clientsysadmin "You? helping me? {w=1}Ha {w=1}ha {w=1}ha!{w=2} {nw}"
                    clientsysadmin "If you are not a system administrator, you can't.{w=4} {nw}"
                    clientsysadmin "Just let me do my work.{w=3} {nw}"
                    $ isc_bar_client1_flags[2] = 1
                    
                "[questions[3]]" if isc_bar_client1_flags[3]  == 0 and isc_bar_client1_flags[1]  == 1:
                    m "[questions[3]]"
                    clientsysadmin "What? Of course, I have things to do!{w=3} {nw}"
                    clientsysadmin "For example, I really need to repair the space crane...{w=4} {nw}"
                    clientsysadmin "Usually, it is possible to control the space crane remotely via the terminal.{w=5} {nw}"
                    clientsysadmin "But the controller of the space crane is broken.{w=4}{nw}"
                    clientsysadmin "No access for now!{w=3}{nw}"
                    m "I think you should repair it.{w=3.5} {nw}"
                    m "A lot of engineers need it!{w=3.5} {nw}"
                    clientsysadmin "Well...{w=1} ... {w=1}... {w=1}... {w=1}{nw}"
                    clientsysadmin "You are right.{w=2} I'll have a look now.{w=2}{nw}"
                    $ isc_bar_client1_flags[3] = 1
                    
                    jump isc_bar_client1_out
                    

                "[questions[4]]": #bye
                    m "[questions[4]]"
                    clientsysadmin "Bye!{w=1.5}{nw}"
                    jump loop_isc_city_bar
    

    if isc_sysadmin_move == 1: # sys admin not in bar but at crane screen
        if inventory_select != "":
            call dialog_nosense from _call_dialog_nosense_31
        else:    
            call dialog_nothing from _call_dialog_nothing_24 
    
    
    if isc_sysadmin_move == 2:
        m "Hello again!{w=2} {nw}"
        sysadmin "Hi! Thank you very much for your help.{w=3} {nw}"
        sysadmin "Without you, I couldn't have fixed the crane.{w=3} {nw}"
        sysadmin "I'd like to give you something for your help.{w=3} {nw}"
        sysadmin "Here! [isc_sysadmin_cash]c!{w=2} {nw}"
        call sound_collect from _call_sound_collect_3
        call io_cash(isc_sysadmin_cash) from _call_io_cash_4
        pause 1
        m "Oh, thanks!{w=2.5} {nw}"
        sysadmin "You are welcome. {w=2}{nw}"
        sysadmin "Now that the crane is fixed, I can finally take a break into the bar. {w=5}{nw}"
        sysadmin "I hope nobody will play with it or move it to another location!{w=4}{nw}"
        m "I don't think so, nobody except us knows how to access it remotely.{w=4} {nw}"
        sysadmin "You are right. And I trust you for now.{w=4}{nw}"
        sysadmin "See you around. {w=1} Bye! {w=2.5}{nw}"
        
        $ isc_sysadmin_move = 3
        
    
    if isc_sysadmin_move == 3:
        if isc_bar_sysadmin_gem == True and isc_sysadmin_sun == 1:
            sysadmin "What about the actual direct irradiation of the sun?{w=3} {nw}"
            m "I'm working on it.{w=2} {nw}"
            sysadmin "Okay...{w=1.5} {nw}"
            
        
        if isc_bar_sysadmin_gem == True and isc_sysadmin_sun == 0:
            sysadmin "If you like, I have another job for you.{w=3} {nw}"
            m "Well... why not?{w=2} {nw}"
            sysadmin "I would like to adjust the sun protection shield of the ISC.{w=4} {nw}"
            sysadmin "But for this, I need an actual measurement of the sun's direct irradiation.{w=5} {nw}"
            sysadmin "Could you fly to the sun and make this measurement for me?{w=4} {nw}"
            
            menu:
                "Okay, I'll do it.":
                    m "Okay, I'll do it.{w=2} {nw}"
                    sysadmin "This is great. See you later!{w=3} {nw}"
                    $ isc_sysadmin_sun = 1
                    
                "No, sorry.":
                    m "No, sorry.{w=2} {nw}"
                    sysadmin "Okay, never mind.{w=2} {nw}"
                    
                    
        if isc_bar_sysadmin_gem == True and isc_sysadmin_sun == 2:
            sysadmin "Do you know the actual direct irradiation of the sun?{w=4} {nw}"
            sysadmin "I need it to adjust the sun protection shield of the Industrial Space City.{w=5} {nw}"
            m "Yes, I measured it.{w=2.5} {nw}"
            m "Right now, the amount is 6272 W/m^2.{w=3} {nw}"
            sysadmin "Oh, this is great.{w=3} {nw}"
            sysadmin "Thank you very much.{w=3} {nw}"
            sysadmin "Unfortunately, I don't have any money left for you right now...{w=4.5} {nw}"
            sysadmin "But would you like this gem?{w=3} {nw}"
            m "Sure!{w=1} {nw}"
            call take_gem from _call_take_gem_10
            $ isc_bar_sysadmin_gem = False
            
            

        sysadmin "Thank you for your help.{w=2} {nw}"
        sysadmin "Bye!{w=1.5} {nw}"
                    
            
            
        
        
        

    #else:
    #    call dialog_nothing 
    
    return





# player
label isc_bar_player:
    
    if drunktime > 0:
        m "What about a joke? {w=2} {nw}"
        clientplayer "Okay, if you insist... {w=2.5} {nw}"
        
        clientplayer "What is the spaceship pilot's favorite place on a computer?{w=5} {nw}"
        m "Well... {w=2} {nw}"
        clientplayer "The space bar! {w=2.5} {nw}"
        m "Hihi.... that's funny! {w=2.5} {nw}"
        
        $ spacebar_joke = True
        
        return
    
    
    if inventory_select == "":
        clientplayer "Hello!{w=2}{nw}"
        m "Hi! {w=1}{nw}"
        clientplayer "I know a really nice space card game.{w=3.5}{nw}"
        clientplayer "Do you want to try?{w=3}{nw}"
        clientplayer "Unfortunately, I don't have any card games...{w=4}{nw}"
        clientplayer "Do you have one?{w=2}{nw}"
        

    # game
    elif inventory_select == "cards":

        call use_and_keep_item from _call_use_and_keep_item_12
        call sound_connected from _call_sound_connected_23

        m "Here, a card game. {w=2}{nw}"
        clientplayer "You've got a card game!{w=3}{nw}"
        clientplayer "Very nice...{w=3}{nw}"
        
        if cardgame_gem == True:
            clientplayer "If you win the game, I'll give you something!{w=4}{nw}"
        
        menu:
            "Let's play!":
                clientplayer "Alright, try to get the same cards.{w=4}{nw}"
                clientplayer "You have one minute, let's go!{w=3}{nw}"
                
                $ countdown = True
                $ countdown_sec = 60
                
                #client "Okay, let's go!{w=3}{nw}"
                #show screen notify("Card Game")
                jump isc_city_bar_cardgame

            
            
            "No, thanks":
                m "No, thanks... bye! {w=2}{nw}"
                clientplayer "Okay, bye.{w=1.5}{nw}"
                
    
    else:
        call npc_dont_need_item(clientplayer) from _call_npc_dont_need_item_9
                
                
    return
            




# barman
label isc_barman:
    show npc as barman:
        linear 2 pos (370, 55)
        linear 1 rotate 180
    #pause 2
    if inventory_select != "":
        call npc_dont_need_item(barman_isc) from _call_npc_dont_need_item_10
        return
    
    barman_isc "Hello! {w=1}{nw}"

    if isc_bar_barman_flags[0] == 0:
        barman_isc "Hi, welcome to my humble bar. {w=2}{nw}"
        barman_isc "How can I help you? {w=2}{nw}"
    
    $ questions = ["I want a drink... {w=2.5} {nw}", 
                    "May I use the bathroom?{w=2.0} {nw}", 
                    "I'm fine, thank you. {w=1.0} {nw}"]
                    
    $ drinks = ["Recycled Water", 
                "Galactic Beer", 
                "Cocktail with exotic fruits from different planets", 
                "Forbidden Alien Shot"]
    

    
    while True:
        menu:
            "[questions[0]]":
                m "[questions[0]]"
                if isc_bar_barman_flags[0] == 0:
                    barman_isc "Oh yeah, we've got plenty of drinks.\nEverything you need!{w=3}{nw}"
                    barman_isc "We've got:\n1. [drinks[0]] (2c)\n2. [drinks[1]] (15c)\n3. [drinks[2]] (23c)\n4. [drinks[3]] (?c)\nAnd many more... {w=6} {nw}"
                
                    $ isc_bar_barman_flags[0] = 1
                
                menu:
                    "[drinks[0]]\n2c"if coins >= 2:
                        m "A [drinks[0]]. {w=1.5}{nw}"
                        m "This really doesn't sound good, but I will try.{w=2.5}{nw}"
                        barman_isc "2c, please. {w=1.5}{nw}"
                        call io_cash(-2) from _call_io_cash_5
                        m "Ugh! {w=1.5}{nw}"
                        m "This is horrible! {w=2}{nw}"
                        $ isc_bar_client = True
                        $ isc_bar_wc_cash += 2
                        
                        jump loop_isc_city_bar
                        
                        
                        
                    "[drinks[1]]\n15c"if coins >= 15:
                        m "A [drinks[1]]. {w=1.5}{nw}"
                        barman_isc "15c, please. {w=1.5}{nw}"
                        call io_cash(-15) from _call_io_cash_6
                        
                        $ isc_bar_client = True
                        $ isc_bar_wc_cash += 15
                        
                        m "Cheers! {w=1.5}{nw}"
                        
                        if drunk_level == 0:
                            m "This tastes like a great galactic beer, amazing! {w=4}{nw}"
                        if drunk_level == 1:
                            m "This one tastes even better than the first one! {w=4}{nw}"
                        if drunk_level >= 2:
                            m "Yihaaaaaaa! The galactic beer tastes better and better!{w=4}{nw}"
                            $ drunktime = 120 #=60sec
                            with Dissolve(2)
                            $ drunk_level = 0
                            m "Wow... {w=1}I feel so good...{w=2}{nw}"
                            jump loop_isc_city_bar
                            
                        $ drunk_level += 1
                        
                        jump loop_isc_city_bar
                        
                        
                        
                    "[drinks[2]]\n23c"if coins >= 23:
                        m "A [drinks[2]]. {w=2.5}{nw}"
                        barman_isc "23c, please. {w=1.5}{nw}"
                        call io_cash(-23) from _call_io_cash_7
                        
                        $ isc_bar_client = True
                        $ isc_bar_wc_cash += 23
                        
                        m "Cheers! {w=1.5}{nw}"
                        
                        m "Nice taste... {w=2}{nw}"
                        barman_isc "Oh yes... like on an island of the planet Erion... {w=3}{nw}"
                        barman_isc "...with its 2 suns and its never-ending sunset! {w=3}{nw}"
                        #call add_note("Terminal: locate erion")
                        
                        m "Hmmmmm... it just tastes amazing...{w=3}{nw}"
                        $ drunktime = 120 #=60sec
                        with Dissolve(2)
                        $ drunk_level = 0
                        m "Yeah... {w=1}I feel so amazing...{w=2}{nw}"
                        jump loop_isc_city_bar
                            

                        
                        
                    "[drinks[3]]\n?c":
                        m "A [drinks[3]]. {w=1.5}{nw}"
                        barman_isc "Hmm... how much you would pay? {w=2.5}{nw}"
                        
                        menu:
                            "0c":
                                m "0c.{w=1}{nw}"
                                barman_isc "Haha.{w=1}{nw}"
                                barman_isc "You are really funny.{w=2}{nw}"
                                barman_isc "Bye.{w=1}{nw}"
                            "10c" if coins >= 10:
                                m "10c.{w=1}{nw}"
                                barman_isc "Are you kidding? {w=1.5}{nw}"
                            "20c" if coins >= 20:
                                m "20c.{w=1}{nw}"
                                barman_isc "Better, but still not enough, my friend! {w=2.5}{nw}"
                            "50c" if coins >= 50:
                                m "50c.{w=1}{nw}"
                                barman_isc "Okay for now... have fun! {w=1.5}{nw}"
                                call io_cash(-50) from _call_io_cash_8
                                m "Hmm, this is toooooooo tasty!{w=2}{nw}"
                                $ isc_bar_client = True
                                $ isc_bar_wc_cash += 50
                                
                                jump alienshot_trip

                        
                    "Nothing, thanks":
                        pass
                            
        
                
            "[questions[1]]" if isc_bar_client == False:
                m "[questions[1]]"
                barman_isc "The bathroom is only for clients. {w=2.5} {nw}"
                barman_isc "I'm sorry. {w=1} {nw}"

                    

            "[questions[2]]":
                m "[questions[2]]"
                barman_isc "Okay, bye! {w=1} {nw}"
                return
    
    return
    
    
    
    
label alienshot_trip:
    
    call sound_scan from _call_sound_scan_5
    stop music fadeout 0.5
    
    $ drunktime = 0
    
    $ triptime = True
    with Dissolve(0.5)
    #with pixellate

    pause 2
        
    #jump isc_city_center
    #jump isc_interchange
    jump isc_rail1





# client 1 sys admin move out the bar
label isc_bar_client1_out:
    
    show npc as client1:
        pos (245, 434)
        linear 1 rotate 90
        linear 1 pos (317, 434)
        linear 1 rotate 0
        linear 1 pos (317, 240)
        linear 1 rotate -90
        linear 1 pos nodeA
                            
    pause 6
    call sound_door from _call_sound_door_64
    hide client1
    $ isc_sysadmin_move = 1
    
    jump loop_isc_city_bar
    
    
    
    

#button screen
screen isc_bar_jukebox() zorder -999:
    #add "#112119"
    on "show" action SetVariable("pnc_nodes_visible", False)
    on "hide" action SetVariable("pnc_nodes_visible", True)
    
    imagebutton at topleft: 
        idle "images/maps/bg.png" 
        action [Hide("isc_bar_jukebox")]
        
            
    
    add "inventory/inventory.png"

    label "Jukebox":
        align (0.5, 0.25)
        
    
    hbox xalign 0.5 yalign 0.6:
        
        vbox xalign 0.5:
            imagebutton:
                auto "images/buttonbig_%s.png" 
                action SetVariable("isc_bar_music", 1), Jump("loop_isc_city_bar")#, Hide("xylo_village_bar_jukebox") at center
            null height 10
            label "1" at center
            
        null width 50
        
        vbox xalign 0.5:
            imagebutton:
                auto "images/buttonbig_%s.png" 
                action SetVariable("isc_bar_music", 2), Jump("loop_isc_city_bar")#, Hide("xylo_village_bar_jukebox") at center
            null height 10
            label "2" at center
                
        null width 50
        
        vbox xalign 0.5:
            imagebutton: 
                auto "images/buttonbig_%s.png" 
                action SetVariable("isc_bar_music", 3), Jump("loop_isc_city_bar")#, Hide("xylo_village_bar_jukebox") at center
            null height 10
            label "3" at center
            
            
        null width 50
        
        vbox xalign 0.5:
            imagebutton: 
                auto "images/buttonbig_%s.png" 
                action SetVariable("isc_bar_music", 4), Jump("loop_isc_city_bar")#, Hide("xylo_village_bar_jukebox") at center
            null height 10
            label "None" at center
            
                
                
    if shadow_enable == 1:
        add "images/shadow.png" align (0.5,0.5)




