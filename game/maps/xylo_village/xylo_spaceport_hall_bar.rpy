# MAPS

############################################



init:
    $ xylo_spaceport_hall_bar_client = False
    
    $ questions_client = ["Hello, how are you doing? {w=3}{nw}", 
                            "What are you doing here?{w=3} {nw}", 
                            "Have you heard about SpaceNET? {w=3} {nw}", 
                            "Bye bye. {w=1.5} {nw}"]
                            
    $ sam_known = False
    $ sam_meeting_mountains = False
    
    $ sam_numpad_mission = 0
    
    default xylo_bar_client1_flags = [0, 0, 0, 1, 1]
    default xylo_bar_client1_flags2 = [0, 0, 0, 0]
    default xylo_bar_client2_flags = [0, 0, 0]
    default xylo_bar_client4_flags = [0, 0, 0]
    default xylo_bar_barman_flags = [0, 0, 0, 0]

    $ game_end = False
    
    $ xylo_village_bar_music = 1
    
    
    
    
    
    

label xylo_spaceport_hall_bar:
    
    stop atmo
    
    image xylo_spaceport_hall_bar = imagemapsdir + "xylo_spaceport_hall_bar.png"
    
    scene bgcolor
    show screen notify("Xylo village bar")
    
    show xylo_spaceport_hall_bar
    
    
    show buttonscreen:
        pos (524, 337) #(632, 207)
        #rotate 90
        
        
    show npc as barman:
        pos (400, 423)
        rotate 90
        linear 2 pos (500, 423)
        linear 1 rotate -90
        linear 4 pos (300, 423)
        linear 1 rotate 90
        linear 2 pos (400, 423)
        repeat
        
    show npc as client1:
        pos (208, 77)
        rotate -50
        
    show npc as client2:
        pos (585, 75)
        rotate 40
        
    if countdown == False:
        show npc as client4:
            pos (182, 237)
            rotate 90
            
    if game_end == True and spacenet_state == "online":
        hide client4
    
    
    # set all variables for the map (nodes and path)
    $ nodeA = (400, 55)
    $ nodeB = (400, 328)
    $ nodeC = (524, 314)#(606, 205)
    $ nodeD = (-100, -100)

    $ nodeAA = (290, 126)
    $ nodeBB = (521, 140)
    $ nodeCC = (613, 283)
    $ nodeDD = (276, 238)

    $ pathA = (nodeA, nodeB, nodeC, (0, 0), nodeAA, nodeBB, nodeCC, nodeDD)
    $ pathB = (nodeA, nodeB, nodeC, (0, 0), nodeAA, nodeBB, nodeCC, nodeDD)
    $ pathC = (nodeA, nodeB, nodeC, (0, 0), nodeAA, nodeBB, nodeCC, nodeDD)
    $ pathD = (nodeA, nodeB, nodeC, (0, 0), nodeAA, nodeBB, nodeCC, nodeDD)
     
    $ pathAA = (nodeA, nodeB, nodeC, (0, 0), nodeAA, nodeBB, nodeCC, nodeDD)
    $ pathBB = (nodeA, nodeB, nodeC, (0, 0), nodeAA, nodeBB, nodeCC, nodeDD)
    $ pathCC = (nodeA, nodeB, nodeC, (0, 0), nodeAA, nodeBB, nodeCC, nodeDD)
    $ pathDD = (nodeA, nodeB, nodeC, (0, 0), nodeAA, nodeBB, nodeCC, nodeDD)
    


    if countdown_sec <= 0:
        $ countdown = False
        $ sam_meeting_mountains = False



label loop_xylo_spaceport_hall_bar:
    
    if xylo_village_bar_music == 1:
        call music_bar_village from _call_music_bar_village
    
    if xylo_village_bar_music == 2:
        call music_bar_chill from _call_music_bar_chill
        
    if xylo_village_bar_music == 3:
        call music_outro_bar from _call_music_outro_bar
    
    if xylo_village_bar_music == 4:
        stop music fadeout 1.0
        
    
    
    while True:
        


        # start "move through the map" loop
        call startpos from _call_startpos_14

        # do something at node?
        if exitpos == 1:
            $ startpos = 11
            call sound_door from _call_sound_door_32
            
            if countdown_sec <= 0:
                $ countdown = False
                
            $ drunk_level = 0    
            jump xylo_spaceport_hall
            

        # barman
        if exitpos == 2:
            if startpos == 2:
                call xylo_village_barman from _call_xylo_village_barman
                
            $ startpos = 2

            
        if exitpos == 3:
            if startpos == 3:
                #$ pnc_nodes_visible = False
                show screen xylo_village_bar_jukebox
                
            $ startpos = 3
            
        
        if exitpos == 4:
            $ startpos = 4
           

        #exits routing "got to map and set position for next map"
        if exitpos == 11:
            if startpos == 11:
                call xylo_village_client1 from _call_xylo_village_client1 # packet client
            $ startpos = 11 

            
        if exitpos == 22:
            if startpos == 22:
                call xylo_village_client2 from _call_xylo_village_client2 # gem client
            $ startpos = 22

            
        if exitpos == 33:
            if startpos == 33:
                if xylo_spaceport_hall_bar_client == True:
                    call sound_door from _call_sound_door_33
                    $ startpos = 4
                    jump xylo_spaceport_hall_bar_wcs
                    
                else:
                    #m "This are the toilets of the bar. {w=2.5}{nw}"
                    call dialog_closed from _call_dialog_closed_6
            $ startpos = 33
            

            
        if exitpos == 44:
            if startpos == 44:
                if countdown == False:
                    call xylo_village_client4 from _call_xylo_village_client4 # spacenet client
                else:
                    call dialog_nothing from _call_dialog_nothing_16
            $ startpos = 44
            

            
# barman
label xylo_village_barman:
    
    if inventory_select != "":
        call npc_dont_need_item(barman_xvil) from _call_npc_dont_need_item_15
        return
    
    
    barman_xvil "Hello! {w=2}{nw}"
    show npc as barman:
        linear 2 pos (370, 423)
        linear 1 rotate 0
    #pause 2
    if xylo_bar_barman_flags[0] == 0:
        barman_xvil "Hi, welcome to the official bar of xylo village. {w=2}{nw}"
        barman_xvil "How can I help you? {w=2}{nw}"
    
    $ questions = ["I want a drink... {w=2.5} {nw}", 
                    "You have weird clients, I have to say.{w=2.5} {nw}", 
                    "May I use the bathroom?{w=2.0} {nw}", 
                    "Have you heard about SpaceNET? {w=2.0} {nw}", 
                    "I'm fine, thank you. {w=1.0} {nw}"]
                    
    $ drinks = ["Recycled Water", 
                "Galactic Beer"]
    
    
    

    while True:
        menu:
            "[questions[0]]":
                m "[questions[0]]"
                if xylo_bar_barman_flags[0] == 0:
                    barman_xvil "Oh yeah, we've got plenty of drinks.\nEverything you need!{w=3}{nw}"
                    barman_xvil "We offer:\n1. [drinks[0]] (1c)\n2. [drinks[1]] (10c)\nAnd many more... {w=6} {nw}"
                
                $ xylo_bar_barman_flags[0] = 1

                menu:
                    "[drinks[0]]\n1c" if coins >= 1:
                        m "A [drinks[0]]. {w=1.5}{nw}"
                        m "This realy doesn't sound good, but I will try.{w=2.5}{nw}"
                        barman_xvil "1c, please. {w=1.5}{nw}"
                        call io_cash(-1) from _call_io_cash_1
                        m "Beark! {w=1.5}{nw}"
                        m "This is horrible! {w=2}{nw}"
                        $ xylo_spaceport_hall_bar_client = True
                        $ xylo_spaceport_hall_wc_cash_wc += 1
                        
                        jump loop_xylo_spaceport_hall_bar
                        
                        
                        
                    "[drinks[1]]\n10c" if coins >= 10 and demo_version == False:
                        m "A [drinks[1]]. {w=1.5}{nw}"
                        barman_xvil "10c, please. {w=1.5}{nw}"
                        call io_cash(-10) from _call_io_cash_2
                        
                        $ xylo_spaceport_hall_bar_client = True
                        $ xylo_spaceport_hall_wc_cash_wc += 10
                        
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
                            jump loop_xylo_spaceport_hall_bar
                            
                        $ drunk_level += 1
                        
                        jump loop_xylo_spaceport_hall_bar
                        
                        
                    "Nothing, thanks":
                        jump loop_xylo_spaceport_hall_bar
                            
        
            "[questions[1]]" if xylo_bar_barman_flags[1] == 0:
                m "[questions[1]]"
                barman_xvil "Please don't say that, nobody is weird here. {w=3} {nw}"
                barman_xvil "What do you want?{w=2} {nw}"
                $ xylo_bar_barman_flags[1] = 1
            
            "[questions[2]]"if xylo_bar_barman_flags[2] == 0:
                m "[questions[2]]"
                if xylo_spaceport_hall_bar_client == False:
                    barman_xvil "The bathroom is only for the clients. {w=2.5} {nw}"
                    barman_xvil "I'm sorry. {w=1} {nw}"
                else:
                    barman_xvil "Sure. {w=1} {nw}"
                    $ xylo_bar_barman_flags[2] = 1
                    
                    
            "[questions[3]]" if xylo_bar_barman_flags[3] == 0:
                m "[questions[3]]"
                barman_xvil "About what? {w=2} {nw}"
                barman_xvil "I don't know what are you talking about. {w=3} {nw}"
                barman_xvil "Please don't bother me anymore. {w=2} {nw}"
                barman_xvil "If you continue asking stupid things, I'll kick you out! {w=3.5} {nw}"
                $ xylo_bar_barman_flags[3] = 1
            
            "[questions[4]]":
                m "[questions[4]]"
                barman_xvil "Okay, bye! {w=1} {nw}"
                return
    
    return




# drink to forget, talk about abanndonned mine. letter to sea coast bar client
label xylo_village_client1:
    
    if inventory_select != "":
        call npc_dont_need_item(client1) from _call_npc_dont_need_item_16
        return
        
    
    client1 "Hello...{w=2} {nw}"
    
    if drunktime > 0:
        call dialog_joke from _call_dialog_joke
        if joke == 1:
            client1 "Ha. {w=1}Ha. {w=1}Ha. {w=2} {nw}"

        if joke == 2:
            client1 "I don't know... {w=2} {nw}"
            m "There is no difference! {w=2} {nw}"
            client1 "Ha! {w=0.1}ha! {w=0.1}ha! {w=0.1}ha! {w=2}{nw}"
            client1 "Nice one. {w=2} {nw}"
        
        if joke == 3:
            client1 "Well... {w=2} {nw}"
            m "The space bar! {w=2} {nw}"
            client1 "Ha! {w=0.1}ha! {w=0.1}ha! {w=0.1}ha! {w=2}{nw}"
            client1 "Nice joke! {w=2} {nw}"
        
        $ joke = 0
        return
        
        
                    
    while True:
        
        menu:
            "[questions_client[0]]" if xylo_bar_client1_flags[0] == 0: #how are you
                m "[questions_client[0]]"
                client1 "Hi. I'm fine, thanks. {w=2} {nw}"
                $ xylo_bar_client1_flags[0] = 1
                
            "[questions_client[1]]" if xylo_bar_client1_flags2 != [1, 1, 1, 1]: # doing?
                m "[questions_client[1]]"
                client1 "What am I doing? {w=2} {nw}"
                client1 "I'm drinking to forget... {w=2} {nw}"
                m "To forget what? {w=2} {nw}"
                client1 "Well... {w=1} I'm really unhappy... {w=1}{nw}"
                client1 "Because they just closed the mine where I was working.{w=3.5} {nw}"
                client1 "So I don't have a job anymore! {w=2} {nw}"
                client1 "What to do now? {w=2} {nw}"
                $ xylo_bar_client1_flags[3] = 0
                
                $ x = 0
                
                while x == 0:
                    menu:
                        "What kind of mine was it?" if xylo_bar_client1_flags2[0] == 0:
                            m "What kind of mine was it?{w=2} {nw}"
                            client1 "It was a silver mine. {w=2} {nw}"
                            client1 "It was really nice to work there! {w=2} {nw}"
                            $ xylo_bar_client1_flags2[0] = 1
                            
                        "Where is it?"if xylo_bar_client1_flags2[1] == 0:
                            m "Where is it?{w=2} {nw}"
                            client1 "It is just south-west of this colony village. {w=3.5} {nw}"
                            client1 "But it is abandonned. {w=2} {nw}"
                            client1 "Going there is now just useless... {w=3} {nw}"
                            client1 "Don't think about this. {w=2} {nw}"
                            $ xylo_bar_client1_flags2[1] = 1
                            
                            
                        "Who is the owner?"if xylo_bar_client1_flags2[2] == 0:
                            m "Who is the owner? {w=2} {nw}"
                            client1 "The owner? It is General Mining Corporation.{w=4} {nw}"
                            client1 "But there is no office there.{w=3} {nw}"
                            $ xylo_bar_client1_flags2[2] = 1
                            
                        "Why did they close it?"if xylo_bar_client1_flags2[3] == 0:
                            m "Why did they close it? {w=2} {nw}"
                            client1 "They said, it is because of seismic activity.{w=4} {nw}"
                            client1 "It is now too dangerous to work there.{w=3} {nw}"
                            client1 "But rumours are saying, they found something special there.{w=3} {nw}"
                            client1 "...{w=2} {nw}"
                            client1 "I don't know if it is related, but the company was bought by A.R.K. Corporation.{w=4} {nw}"
                            client1 "And all of the sudden, they closed the mine!{w=3} {nw}"
                            $ xylo_bar_client1_flags2[3] = 1
                            
                            
                        
                        "Okay, thanks!":
                            m "Okay, thanks!{w=2} {nw}"
                            $ x = 1
                            
                            
                            
                    
                        
                
            "[questions_client[2]]" if xylo_bar_client1_flags[2] == 0: # spacenet?
                m "[questions_client[2]]"
                client1 "SpaceNET?... {w=0.5} No idea, sorry. {w=1.5}{nw}"
                $ xylo_bar_client1_flags[2] = 1
                
                
            "Can I help you somehow?" if "letter" not in inventory and xylo_sea_bar_client1_letter != 1 and xylo_bar_client1_flags[3] == 0:
                m "Can I help you somehow?{w=2} {nw}"
                client1 "Maybe... {w=1}Look. {w=1}As I left, I found this letter.{w=3} {nw}"
                client1 "There are some personal documents of a friend of mine.{w=3} {nw}"
                client1 "I'm sure, he would love to have them back.{w=3} {nw}"
                client1 "But unfortunately I can't go to him because I don't own any spaceship!{w=4} {nw}"
                client1 "He is now living on the sea coast, in the really south-east. {w=4} {nw}"
                client1 "Would you like to help and bring him the documents? {w=4} {nw}"
                client1 "I'm sure he will be grateful.{w=3} {nw}"
                menu:
                    "Okay, I'll do it.":
                        m "Okay, I'll do it.{w=2} {nw}"
                        client1 "That's really nice, thanks!{w=3} {nw}"
                        client1 "Here is the letter.{w=2} {nw}"
                        
                        call take_item("letter") from _call_take_item_6
                        
                        $ xylo_bar_client1_flags[4] = 0

                    
                    "No, thanks.":
                        m "No, thanks.{w=2} {nw}"
                return
                                
            
            "What should I do?" if "letter" in inventory and xylo_bar_client1_flags[4] == 0:
                m "What should I do?{w=2} {nw}"
                client1 "Please, bring the documents to my friend at the sea coast village.{w=4} {nw}"
                client1 "Thanks!{w=2} {nw}"
            
                
            
            "[questions_client[3]]": # bye
                m "[questions_client[3]]"
                client1 "Bye!{w=1.5} {nw}"
                return
    
    return




# GEMS client
label xylo_village_client2:
    
    if inventory_select == "gem":
        call use_and_keep_item from _call_use_and_keep_item_5
        
        client2gem "Beautiful!{w=2}{nw}"
        if gems != maxgems:
            client2gem "But it is not enough...{w=2.5}{nw}"
            client2gem "Please find the [maxgems] gems before it is too late.{w=4}{nw}"
            m "Okay, let's go!{w=2}{nw}"
            return
        
        else:
            client2gem "You collected all the [maxgems] gems, this is great, thanks! {w=4}{nw}"
            client2gem "Now the government can't find them.{w=2.5}{nw}"
            client2gem "Thank you very much!{w=2}{nw}"
            client2gem "As a zen master, I don't need them.{w=2}{nw}"
            client2gem "I don't need any precious stones to be happy.{w=3}{nw}"
            client2gem "But...{w=2}{nw}"
            client2gem "I feel you are a good person.{w=2}{nw}"
            client2gem "Would you like to keep them for a while?{w=3}{nw}"
            client2gem "At least until the peace is back here.{w=3}{nw}"
            client2gem "Maybe one day, good people will know how to use them for good things.{w=5}{nw}"
            m "No problem.{w=2}{nw}"
            client2gem "Thank you very much!{w=3}{nw}"
            m "You are really welcome.{w=2}{nw}"
            client2gem "Bye!{w=1.5}{nw}"
            
            #$ inventory_select = ""

            
            return
            
    
    
    if inventory_select != "" and inventory_select != "gem":
        call npc_dont_need_item(client2gem) from _call_npc_dont_need_item_17
        return
    
    
    client2gem "Hi!{w=1.5} {nw}"
    
    
    if drunktime > 0:
        call dialog_joke from _call_dialog_joke_1
        if joke >= 1:
            client2gem "Please, let me meditate.  {w=3} {nw}"
            client2gem "Ask somebody else.  {w=2} {nw}"
        $ joke = 0
        return
    
    
    
    if xylo_bar_client2_flags[1] == 1 and gems != maxgems:
        client2gem "What about the gems?{w=2.5} {nw}"
        m "I've got [gems].{w=2}{nw}"
        client2gem "When you'll find all the [maxgems] gems, come back to me.{w=4} {nw}"
        
                    
    while True:
        
        menu:
                 
            "[questions_client[0]]" if gems != maxgems and xylo_bar_client2_flags[0] == 0:#how are you
                m "[questions_client[0]]"
                client2gem "Hi. I'm fine, thanks. {w=2} {nw}"
                $ xylo_bar_client2_flags[0] = 1
                #return
                
            "[questions_client[1]]" if gems != maxgems and xylo_bar_client2_flags[1] == 0: # doing?
                m "[questions_client[1]]"
                client2gem "I am a zen master.{w=2} {nw}"
                client2gem "There are many things disturbing the peace of our world...{w=4} {nw}"
                client2gem "Of course, bad people and their need for power.{w=4} {nw}"
                client2gem "There are many precious gems full of energy in this world.{w=4} {nw}"
                client2gem "If the government find them, this could be a disaster...{w=4} {nw}"
                client2gem "Somebody has to collect them before they now their existance.{w=4} {nw}"
                client2gem "To say it exactly, I know about [maxgems] gems.{w=4} {nw}"
                client2gem "Could you collect them before it is too late?{w=4} {nw}"
                m "Well... why not?{w=2.5} {nw}"
                client2gem "Great!{w=2} {nw}"
                
                if xylo_bar_gem == True:
                    client2gem "Here, I give you one sample. It is for you.{w=4} {nw}"
                    call take_gem from _call_take_gem_1
                    $ xylo_bar_gem = False
                    
                    
                
                client2gem "Come back to me when you have all [maxgems] gems.{w=4} {nw}"
                m "Okay!{w=2} {nw}"
                client2gem "Then we'll see what we can do.{w=3} {nw}"
                client2gem "Thank you!{w=2} {nw}"
                $ xylo_bar_client2_flags[1] = 1
                #return
                
            "[questions_client[2]]" if gems != maxgems and xylo_bar_client2_flags[2] == 0: # spacenet?
                m "[questions_client[2]]"
                client2gem "SpaceNET?... {w=1} No, I don't know. {w=1}{nw}"
                $ xylo_bar_client2_flags[2] = 1
                #return
                
            
            
            "I found all the gems!" if gems == maxgems:
                $ inventory_select = "gem"
                m "I found all the gems!{w=2} {nw}"
                jump xylo_village_client2
            
            "[questions_client[3]]":
                m "[questions_client[3]]"
                client2gem "See you soon.{w=2} {nw}"
                return

                
    return




# SpaceNET info client - SAM
label xylo_village_client4:


    # show/hide sam
    if countdown == False:
        show npc as client4:
            pos (182, 237)
            rotate 90
            
    if game_end == True and spacenet_state == "online":
        hide client4
        
    
    if game_end == True:
        call dialog_nothing from _call_dialog_nothing_17
        return
        
    if drunktime > 0:
        samclient "Please, don't bother me. {w=2} {nw}"
        return
        
        
    if inventory_select != "":
        if sam_meeting_mountains == False or game_end == False:
            call npc_dont_need_item(samclient) from _call_npc_dont_need_item_18
        return
        

    while True:
        if "star" not in inventory:
            menu:
                "[questions_client[0]]" if sam_known == False and xylo_bar_client4_flags[0] == 0: #how are you
                    m "[questions_client[0]]"
                    samclient "Please, let me alone. {w=2} {nw}"
                    $ xylo_bar_client4_flags[0] = 1
                    
                "[questions_client[1]]"if sam_known == False and xylo_bar_client4_flags[1] == 0: # doing?
                    m "[questions_client[1]]"
                    samclient "What am I doing? {w=2} {nw}"
                    samclient "Nothing special, just having a nice galactic beer. {w=2} {nw}"
                    $ xylo_bar_client4_flags[1] = 1
                    
                "[questions_client[2]]": # spacenet?
                    m "[questions_client[2]]"
                    samclient "Hmm. {w=1}{nw}"
                    samclient "Please, don't talk about this in public. {w=2.5}{nw}"
                    samclient "Okay? {w=1.5}{nw}"
                    samclient "... {w=1.5}{nw}"
                    samclient "If you really want to know more... {w=3}{nw}"
                    samclient "... {w=1.5}{nw}"
                    samclient "Wait... {w=1} Who are you? {w=2} {nw}"
                    m "I'm [playername].{w=2}{nw}"
                    m "I just escaped from a huge spaceship...{w=2.5}{nw}"
                    m "And I can't remember nothing except the name SpaceNET!{w=3.5}{nw}"
                    samclient "Did you say, you are [playername]? {w=2.5}{nw}"
                    m "Hmm... yes, that's my name.{w=2}{nw}"
                    samclient "Okay. My name is Sam. {w=2}{nw}"
                    
                    $ sam_known = True
                    
                    sam "We need to have a talk. {w=2}{nw}"
                    sam "Please meet me in 2 minutes at the mountain's lake. {w=4}{nw}"
                    sam "I won't wait, so hurry up! {w=2}{nw}"
                    sam "See you there.{w=1.5}{nw}"
                   
                    show npc as client4:
                        linear 0.5 rotate 180
                        linear 1 pos (185,311) 
                        linear 0.5 rotate 90
                        linear 1.5 pos nodeB
                        linear 0.5 rotate 0
                        linear 2 pos nodeA
                    
                    pause 6
                    call sound_door from _call_sound_door_34
                    hide client4
                    
                    $ countdown = True
                    $ countdown_sec = 120 # mountain meeting
                    
                    $ sam_meeting_mountains = True
                    
                    
                    return
                    
                    
                "[questions_client[3]]":
                    m "[questions_client[3]]"
                    return
                    
        #return

    
        elif hacker_in_prison == 1:
            menu:
                "Hey Sam. We need help!" if "laser" not in inventory:
                    m "Hey Sam! We need help!{w=2}{nw}"
                    sam "What happened?{w=2}{nw}"
                    m "I was talking with 4n0nym0us as she got cought!{w=3.5}{nw}"
                    m "I think I know where she is, but I'll need a metal cutting tool to get there.{w=4}{nw}"
                    sam "Hm... I see.{w=2}{nw}"
                    sam "I have this small laser here, do you think it is strong enough for that task?{w=4}{nw}"
                    m "I don't know...{w=2} But I could try.{w=2}{nw}"
                    sam "Okay, just take this laser.{w=2}{nw}"
                    call take_item("laser") from _call_take_item_7
                    if "laser" in inventory:
                        sam "Okay, please go now and free 4n0nym0us!{w=3}{nw}"
                        sam "Good luck.{w=2}{nw}"
                    
                    return
                    

                "[questions_client[3]]":
                    m "[questions_client[3]]"
                    sam "bye.{w=1}{nw}"
                    return
                    
        
        elif cargo_exploded == 0 and (sam_numpad_mission == 1 or sam_numpad_mission == 2):
            #if sam_numpad_mission == 1 or sam_numpad_mission == 2 :
            sam "Hey [playername]!{w=1.5}{nw}"
            sam "I'm happy you've seen my message in your inbox.{w=2.5}{nw}"
            sam "I just met 4n0nym0us.{w=2}{nw}"
            sam "She told me she just figured out a very important information about A.R.K. Corporation.{w=3}{nw}"
            sam "They sent a big cargo ship full of weapons to the government.{w=3}{nw}"
            sam "They propably want to start a civil war!{w=2}{nw}"
            sam "We really need to stop this before it is too late!{w=2.5}{nw}"
            sam "I will organize a meeting with 4n0nym0us for you.{w=2.5}{nw}"
            sam "She has a good idea how to stop this cargo ship and how you could help us.{w=3.5}{nw}"
            sam "4n0nym0us is close to the industrial space city right now...{w=3.5}{nw}"
            sam "She will pick you up there at the space gateway.{w=2.5}{nw}"
            sam "It is a prohibided area, but I'll tell you how to get there.{w=3}{nw}"
            sam "The secret entrance is located in the bar, it is door number 4 in the bathroom.{w=3.5}{nw}"
            sam "But you will need a pin to access it.{w=2}{nw}"
            sam "The pin is 12458.{w=2}{nw}"
            sam "It doesn't matter in which order you enter the numbers.{w=3}{nw}"
            
            call add_note("isc space gateway pin : 12458") from _call_add_note_2
            
            sam "When you are done, just open the door.{w=2.5}{nw}"
            sam "Now let me see when you could meet 4n0nym0us there.{w=3}{nw}"
            sam "... {w=1}... {w=1}... {w=1}... {w=1}... {w=1}... {w=1}{nw}"
            sam "Okay. She will pass by now!{w=2.5}{nw}"
            sam "Are you ready?{w=2}{nw}"
            menu:
                "Okay, let's go!":
                    m "Okay, let's go!{w=2}{nw}"
                    sam "Hurry up!{w=2}{nw}"
                    $ sam_numpad_mission = 2
                    $ countdown = True
                    $ countdown_sec = 180
                    
                "Not yet, sorry":
                    m "Not yet, sorry{w=2}{nw}"
                    pass
                    

            
            
        elif cargo_exploded == 2:
            m "Hello!{w=1}{nw}"
            sam "Hi [playername]! {w=2}{nw}"

            if  active_nodes_amount != max_nodes_amount:
                sam "Well done with the space cargo! {w=2.5}{nw}"
                sam "But we still need to activate all the spacenet nodes!{w=3}{nw}"
                sam "[active_nodes_amount] of [max_nodes_amount] nodes are activated right now.{w=3}{nw}"
                sam "When you are done, please start the SpaceNET network!{w=3}{nw}"
                sam "Then come back to me.{w=2.5}{nw}"
                
            
            if  active_nodes_amount == max_nodes_amount and spacenet_state == "offline":
                sam "We are still not done with our tasks....{w=3}{nw}"
                sam "Please launch SpaceNET and come back to me.{w=3}{nw}"
            
            
            # GAME END
            if  active_nodes_amount == max_nodes_amount and spacenet_state == "online":
                sam "All SpaceNET nodes are activated.{w=3}{nw}"
                sam "And SpaceNET is online again!{w=2}{nw}"
                sam "This is great!{w=2}{nw}"
                sam "With the power of SpaceNET's information network, the corrupted government has no influence anymore...{w=6.5}{nw}"
                sam "Now we can start a new life in peace...{w=3}{nw}"
                sam "Thank you very much!{w=2}{nw}"
                sam "...{w=1}{nw}"
                
                $ startpos = 1
                
                $ game_end = True
                $ landing = False
                jump xylo_spaceport
                
            
        
        
        
        else:
            m "Hello!{w=1}{nw}"
            sam "Hi. I'm busy right now, sorry... {w=3}{nw}"
            sam "See you soon, bye! {w=2}{nw}"
            
            
            
            
        return
    return
    
    
    
    
    

    
#button screen
screen xylo_village_bar_jukebox() zorder -999:
    #add "#112119"
    
    on "show" action SetVariable("pnc_nodes_visible", False)
    on "hide" action SetVariable("pnc_nodes_visible", True)

    imagebutton at topleft: 
        idle "images/maps/bg.png" 
        action [Hide("xylo_village_bar_jukebox")]
      
    
    add "inventory/inventory.png"

    label "Jukebox":
        align (0.5, 0.25)
        
    
    hbox xalign 0.5 yalign 0.6:
        
        vbox xalign 0.5:
            imagebutton:
                auto "images/buttonbig_%s.png" 
                action SetVariable("xylo_village_bar_music", 1), Jump("loop_xylo_spaceport_hall_bar")#, Hide("xylo_village_bar_jukebox") at center
            null height 10
            label "1" at center
            
        null width 50
        
        vbox xalign 0.5:
            imagebutton:
                auto "images/buttonbig_%s.png" 
                action SetVariable("xylo_village_bar_music", 2), Jump("loop_xylo_spaceport_hall_bar")#, Hide("xylo_village_bar_jukebox") at center
            null height 10
            label "2" at center
                
        null width 50
        
        vbox xalign 0.5:
            imagebutton: 
                auto "images/buttonbig_%s.png" 
                action SetVariable("xylo_village_bar_music", 3), Jump("loop_xylo_spaceport_hall_bar")#, Hide("xylo_village_bar_jukebox") at center
            null height 10
            label "3" at center
            
            
        null width 50
        
        vbox xalign 0.5:
            imagebutton: 
                auto "images/buttonbig_%s.png" 
                action SetVariable("xylo_village_bar_music", 4), Jump("loop_xylo_spaceport_hall_bar")#, Hide("xylo_village_bar_jukebox") at center
            null height 10
            label "None" at center
            
                
                
    if shadow_enable == 1:
        add "images/shadow.png" align (0.5,0.5)
    

