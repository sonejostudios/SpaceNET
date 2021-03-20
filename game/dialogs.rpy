#dialogs

init:
    $ joke = 0
    
    $ text_i_dont_need_anything = "I don't need anything, thanks. {w=2.5}{nw}"

label surface_borders:
    $ say_surfaceborder = renpy.random.choice(  ["I should not fly too far away...", 
                                                "This seems interesting, but it is too far away.", 
                                                "Why going so far?", 
                                                "No no, I don't want to fly there.", 
                                                "I don't have time to fly around..."])
    m "[say_surfaceborder] {w=2.0} {nw}"
    return
    



label dialog_idontknow:
    $ say_idontknow = renpy.random.choice(  ["I don't have a clue what it is.", 
                                            "What's that?", 
                                            "What is this?",
                                            "No comment.",
                                            "I don't know what it is."])
    m "[say_idontknow] {w=2.0} {nw}"
    return

label dialog_nothing:
    #call sound_search
    $ say_nothing = renpy.random.choice(    ["There is nothing.", 
                                            "I can't see anything.", 
                                            "Nothing there.",
                                            "Hmm... there is nothing.",
                                            "Nothing to see, nothing to do.",
                                            "Nothing special there..."])
    m "[say_nothing] {w=2.0} {nw}"
    return


label dialog_closed:
    
    if inventory_select == "screwdriver":
        m "Unscrewing this door is definitely a bad idea, forget it! {w=3.0} {nw}"
    elif inventory_select == "accesscard" or inventory_select == "robotcard":
        m "This access card doesn't fit to this door! {w=3.0} {nw}"
    elif inventory_select == "cable":
        m "I could make a short circuit... {w=1.5} {nw}"
        call sound_electroshock from _call_sound_electroshock_1
        with hpunch
        m "Haaa... bad idea! {w=1.5} {nw}"
        m "Nothing happens... {w=1.5} {nw}"
    elif inventory_select == "pick":
        m "I don't want to destroy this door. {w=2} {nw}"
    elif inventory_select == "dynamite":
        m "I really - really - really - don't want to destroy this door! {w=3.5} {nw}"
    elif inventory_select == "laser":
        m "This laser is not strong enough to cut this door. {w=3.5} {nw}"
    elif inventory_select == "key":
        m "This key is useless with this door, forget it! {w=3.5} {nw}"
    
    elif inventory_select != "":
        call dialog_nosense from _call_dialog_nosense_5
        
    else:
        call sound_door_locked from _call_sound_door_locked
        $ say_closed = renpy.random.choice( ["It's locked.", 
                                            "I can't open it.", 
                                            "It's not open.",
                                            "It seems to be locked.",
                                            "It is locked."])
        m "[say_closed] {w=2.0} {nw}"
        
    $ inventory_select = ""
    
    return


label dialog_nosense:
    $ say_nosense = renpy.random.choice( ["This doesn't make sense!", 
                                        "Why should I do that?", 
                                        "Why would I do that?",
                                        "I think this doesn't makes sense.",
                                        "I don't know why I should do this.",
                                        "This is not the solution.",
                                        "Very bad idea!",
                                        "No way I will do this.",
                                        "Why?",
                                        "This won't do anything.",
                                        "Someday, I may be able to do that, but not today.",
                                        "Useless idea..."])
    
    
    #call use_and_keep_item
    m "[say_nosense] {w=2.0} {nw}"
    $ inventory_select = ""
    
    return



label dialog_notfitting:
    m "There's no way I'm fitting into this!{w=2} {nw}"
    return
     
     
label dialog_ndd:
    call sound_electroshock from _call_sound_electroshock_2
    with hpunch
    md "This is a ndd, a non-droid door...{w=2} {nw}" 
    md "I can't go through there! {w=2} {nw}"
    return
    
    
    
label dialog_joke:
    m "What about a joke? {w=2} {nw}"
    menu:
        
        "What is a spaceships' pilote's favourite place on a computer?" if spacebar_joke == True:
            m "What is a spaceships' pilote's favourite place on a computer?{w=5} {nw}"
            $ joke = 3
        
        "What is the difference between the government and the A.R.K Corporation?" if gov_joke == True:
            m "What is the difference between the government and the A.R.K Corporation? {w=5} {nw}"
            $ joke = 2
            
        
        "This is the story of a guy...":
            m "This is the story of a guy... {w=2} {nw}"
            $ joke = 1 
        
        "Forget it.":
            $ joke = 0 
    
    return



label npc_dont_need_item(npc):
    
    if inventory_select in ["accesscard", "spacenet", "robotcard", "bulb"]:
        $ npc_noneed_say = renpy.random.randint(1, 3)
    else:
        $ npc_noneed_say = renpy.random.randint(1, 9)
    
    
    # unspecific items
    if npc_noneed_say == 1:
        npc "I don't need anything, thanks. {w=2.5}{nw}"
    if npc_noneed_say == 2:
        npc "I don't need that, thanks. {w=2.5}{nw}"
    if npc_noneed_say == 3:
        npc "I'm not interested, sorry. {w=3.5}{nw}"
    
        
    # talk about item
    if npc_noneed_say == 4:
        npc "I don't need any [inventory_select], thanks. {w=3}{nw}"
    if npc_noneed_say == 5:
        npc "Do I look like I would really need any [inventory_select]? {w=4}{nw}"
    if npc_noneed_say == 6:
        npc "Please, don't bother me with your [inventory_select]. {w=3.5}{nw}"
    if npc_noneed_say == 7:
        npc "What do your want with your [inventory_select]? {w=3.5}{nw}"
    if npc_noneed_say == 8:
        npc "What's the thing with this [inventory_select]? {w=3}{nw}"
        npc "Please don't bother me with it. {w=3.5}{nw}"
    if npc_noneed_say == 9:
        npc "If I need your [inventory_select], I'll let you know. {w=4}{nw}"
        
    
    $ inventory_select = ""
    
    return



