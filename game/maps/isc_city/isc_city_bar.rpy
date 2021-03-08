# MAPS

############################################

init:
    $ isc_bar_client = False
    #$ isc_bar_client = True
    
    $ sam_numpad_mission = 0
    
    default isc_bar_client1_flags = [0, 0, 0, 0]
    default isc_bar_barman_flags = [0, 0, 0, 0]
    
    $ isc_sysadmin_move = 0
    $ isc_sysadmin_sun = 0

    $ spacebar_joke = False
    
    $ isc_bar_music = 2
    

    
    

label isc_city_bar:
    
    stop atmo
    
    #"sam_numpad_mission : [sam_numpad_mission]"
    
    #$ steps_sound = "concrete"
    
    image isc_city_bar = imagemapsdir + "isc_city_bar.png"
    
    scene bgcolor
    show screen notify("ISC City Bar")
    
    hide screen isc_cardgame_check
    
    #call show_space
    
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
            



# client east
label isc_bar_client_east:
    if inventory_select != "":
        $ inventory_select = ""
        clientisc3 "[text_i_dont_need_anything]"
        return
        
    clientisc3 "hi! {w=2}{nw}"
    
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
            clientisc3 "You are really welcome. {w=2.5} {nw}"
            clientisc3 "Bye! {w=1.5} {nw}"

        $ joke = 0    
        return
        
    
    m "hello... {w=1.5}{nw}"
    m "hey... {w=1.5}... {w=1}...{w=1}{nw}"
    clientisc3 "? {w=1.5}{nw}"
    m "...Have you heard about SpaceNET? {w=3}{nw}"
    clientisc3 "No, sorry. {w=1.5}{nw}"
    
    m "okay, bye... {w=1.5}{nw}"
    clientisc3 "Bye bye! {w=1.5}{nw}"
    
    return



# sysadmin
label isc_bar_sysadmin:
    if isc_sysadmin_move == 0:
        clientsysadmin "hello!{w=2}{nw}"
        
        $ questions = ["I'm just looking around.{w=2.0} {nw}", 
                        "What are you doing here?{w=2.0} {nw}", 
                        "I can help you if you like. {w=2.0} {nw}", 
                        "Work? You are having a drink in the bar! {w=2.0} {nw}", 
                        "Nothing, thank you. {w=1.0} {nw}"]
        
        while True:
            menu:
                "[questions[0]]" if isc_bar_client1_flags[0]  == 0:
                    m "[questions[0]]"
                    clientsysadmin "Nice for you! Please let me do my work.{w=4} {nw}"
                    $ isc_bar_client1_flags[0] = 1
                
                "[questions[1]]" if isc_bar_client1_flags[1]  == 0:
                    m "[questions[1]]"
                    clientsysadmin "I'm the system administrator of the industrial space station.{w=4} {nw}"
                    clientsysadmin "I'm just having a rest before I'll fix the next problem here.{w=4} {nw}"
                    clientsysadmin "They are tons of things to do here!{w=2} {nw}"
                    $ isc_bar_client1_flags[1] = 1
                
                "[questions[2]]" if isc_bar_client1_flags[2] == 0 and isc_bar_client1_flags[1]  == 1:
                    m "[questions[2]]"
                    clientsysadmin "You? helping me? I don't think so you can help me.{w=4} {nw}"
                    clientsysadmin "Please let me do my work.{w=3} {nw}"
                    $ isc_bar_client1_flags[2] = 1
                    
                "[questions[3]]" if isc_bar_client1_flags[3]  == 0 and isc_bar_client1_flags[1]  == 1:
                    m "[questions[3]]"
                    clientsysadmin "What?? Of course I have things to do!{w=3} {nw}"
                    clientsysadmin "For example, I really need to repaire the space crane...{w=4} {nw}"
                    clientsysadmin "Usually it is possible to control the space crane remotely via the terminal.{w=4} {nw}"
                    clientsysadmin "But the controller of the space crane is broken.{w=3}{nw}"
                    clientsysadmin "No access for now!{w=3}{nw}"
                    m "I thing you should repair it.{w=2} {nw}"
                    m "A lot of engineers need it!{w=2} {nw}"
                    clientsysadmin "Well.{w=1} ... {w=1}... {w=1}... {w=1}{nw}"
                    clientsysadmin "You are right.{w=2} I'll have a look now.{w=2}{nw}"
                    $ isc_bar_client1_flags[3] = 1
                    
                    jump isc_bar_client1_out
                    

                "[questions[4]]": #bye
                    m "[questions[4]]"
                    clientsysadmin "Bye!{w=1.5}{nw}"
                    jump loop_isc_city_bar
    

    if isc_sysadmin_move == 1: # sys admin not in bar but at crane screen
        call dialog_nothing from _call_dialog_nothing_24 
    
    if isc_sysadmin_move == 2:
        m "Hello again!{w=2} {nw}"
        sysadmin "Hi! Thank you very much for your help.{w=3} {nw}"
        sysadmin "Without you I couldn't fix the crane.{w=3} {nw}"
        sysadmin "I'd like to give you something for your help.{w=3} {nw}"
        sysadmin "Here! [isc_sysadmin_cash]c!{w=2} {nw}"
        call sound_collect from _call_sound_collect_3
        call io_cash(isc_sysadmin_cash) from _call_io_cash_4
        pause 1
        m "Wow...{w=1} thank you!{w=2} {nw}"
        sysadmin "You are welcome! {w=3}{nw}"
        $ isc_sysadmin_move = 3
        
    if isc_sysadmin_move == 3:
        
        if isc_bar_sysadmin_gem == True and isc_sysadmin_sun == 1:
            sysadmin "What about the actual direct radiation of the sun?{w=3} {nw}"
            m "I'm working on it.{w=2} {nw}"
            sysadmin "Okay...{w=1.5} {nw}"
            
        
        if isc_bar_sysadmin_gem == True and isc_sysadmin_sun == 0:
            sysadmin "If you like, I have another job for you.{w=3} {nw}"
            m "Well... why not?{w=2} {nw}"
            sysadmin "I would like to adjust the sun protection shield of the ISC.{w=4} {nw}"
            sysadmin "But for this, I need an actual measurement of the sun's direct radiation.{w=5} {nw}"
            sysadmin "Could you fly to the sun and make this measurement for me?{w=4} {nw}"
            
            menu:
                "Okay, I'll do it.":
                    m "Okay, I'll do it.{w=2} {nw}"
                    sysadmin "This is great! see you later.{w=3} {nw}"
                    $ isc_sysadmin_sun = 1
                    
                "No, sorry.":
                    m "No, sorry.{w=2} {nw}"
                    sysadmin "Okay, never mind.{w=2} {nw}"
                    
                    
        if isc_bar_sysadmin_gem == True and isc_sysadmin_sun == 2:
            sysadmin "Do you know the actual direct radiation of the sun?{w=4} {nw}"
            sysadmin "I need it to adjust the sun protection shield of the Industrial Space City.{w=5} {nw}"
            m "Yes, I measured it.{w=2} {nw}"
            m "Right now, the amount is 6272 W/m^2.{w=3} {nw}"
            sysadmin "Oh, this is great!{w=3} {nw}"
            sysadmin "Thank you very much.{w=3} {nw}"
            sysadmin "Unfortunately I don't have any money left for you right now...{w=4} {nw}"
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
        
        clientplayer "What is an spaceship pilote's favourite place on a computer?{w=5} {nw}"
        m "Well... {w=2} {nw}"
        clientplayer "The space bar! {w=2.5} {nw}"
        m "Hihi.... that's funny! {w=2.5} {nw}"
        
        $ spacebar_joke = True
        
        return
    
    
    if inventory_select == "":
        clientplayer "hello!{w=2}{nw}"
        m "hi! {w=1}{nw}"
        clientplayer "I know a really nice space card game.{w=3.5}{nw}"
        clientplayer "Do you want to try?{w=3}{nw}"
        clientplayer "Unfortunately I don't have any card game...{w=4}{nw}"
        clientplayer "Do you have one?{w=2}{nw}"
        

    # game
    if inventory_select == "cards":

        call use_and_keep_item from _call_use_and_keep_item_12
        call sound_connected from _call_sound_connected_23

        m "Here, a card game. {w=2}{nw}"
        clientplayer "You've got a card game!{w=3}{nw}"
        clientplayer "Very nice...{w=3}{nw}"
        clientplayer "If you win the game, I'll give you something!{w=4}{nw}"
        menu:
            "let's play!":
                clientplayer "Alright, try to get the same cards.{w=4}{nw}"
                clientplayer "You have one minute, let's go!{w=3}{nw}"
                
                $ countdown = True
                $ countdown_sec = 60
                
                #client "Okay, let's go!{w=3}{nw}"
                #show screen notify("Card Game")
                jump isc_city_bar_cardgame

            
            
            "no, thanks":
                m "no, thanks... bye! {w=2}{nw}"
                clientplayer "okay, bye.{w=1.5}{nw}"
                
    
    if inventory_select != "cards" and inventory_select != "":
        clientplayer "I don't need that, thanks.{w=3}{nw}"
                
                
    return
            




# barman
label isc_barman:
    if inventory_select != "":
        $ inventory_select = ""
        barman_isc "[text_i_dont_need_anything]"
        return
    
    barman_isc "hello! {w=1}{nw}"
    show npc as barman:
        linear 2 pos (370, 55)
        linear 1 rotate 180
    #pause 2
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
                    barman_isc "Oh yeah, we have plenty of drinks.\nEverything you need!{w=3}{nw}"
                    barman_isc "We have:\n1. [drinks[0]] (2c)\n2. [drinks[1]] (15c)\n3. [drinks[2]] (23c)\n4. [drinks[3]] (?c)\nAnd many more... {w=6} {nw}"
                
                    $ isc_bar_barman_flags[0] = 1
                
                menu:
                    "[drinks[0]]\n2c"if coins >= 2:
                        m "A [drinks[0]]. {w=1.5}{nw}"
                        m "This realy doesn't sound good, but I will try.{w=2.5}{nw}"
                        barman_isc "2c, please. {w=1.5}{nw}"
                        call io_cash(-2) from _call_io_cash_5
                        m "Beark! {w=1.5}{nw}"
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
                        barman_isc "...with its 2 suns and its never ending sunset! {w=3}{nw}"
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

                        
                    "nothing, thanks":
                        pass
                            
        
                
            "[questions[1]]" if isc_bar_client == False:
                m "[questions[1]]"
                barman_isc "The bathroom is only for the clients. {w=2.5} {nw}"
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




