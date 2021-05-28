
init:
    $ clientcards = ["1", "2"]
    $ playercards = ["2", "3"]
    
    



label isc_city_bar_cardgame:
    
    
    image cards:
        "cards.png"
        anchor (0.5,0)
        
    image card1:
        "card1.png"
        anchor (0.5,0.5)
        
    image card2:
        "card2.png"
        anchor (0.5,0.5)
        
    image card3:
        "card3.png"
        anchor (0.5,0.5)
        
        
        
        
        
    
    scene bgcolor
    #show screen notify("Card Game")
    
    
    show screen isc_cardgame_check

    
    
    
    #client cards
    

    $ clientcards = (renpy.random.choice(["1", "2", "3"]), renpy.random.choice(["1", "2", "3"]))
    
    $ playercards = (renpy.random.choice(["1", "2", "3"]), renpy.random.choice(["1", "2", "3"]))
    
    #show text "[clientcards]\n\n\n[playercards]" at truecenter
    with Dissolve(0.5) 
    
    show cards as cards1:
        pos (300,30)

    if clientcards[0] == "1":
        show card1 as card1a:
            pos (300,130)
    if clientcards[0]  == "2":
        show card2 as card1b:
            pos (300,130)
    if clientcards[0]  == "3":
        show card3 as card1c:
            pos (300,130)
    
    with Dissolve(0.5)    
        
    show cards as cards2:
        pos (500,30)
        
    if clientcards[1] == "1":
        show card1 as card2a:
            pos (500,130)
    if clientcards[1]  == "2":
        show card2 as card2b:
            pos (500,130)
    if clientcards[1]  == "3":
        show card3 as card2c:
            pos (500,130)
    
    with Dissolve(0.5)    
    
    #with pixellate
    pause
    
    #player cards
    
    show cards as cards3:
        pos (300,250)
    
    if playercards[0] == "1":
        show card1 as card3a:
            pos (300,350)
    if playercards[0]  == "2":
        show card2 as card3b:
            pos (300,350)
    if playercards[0]  == "3":
        show card3 as card3c:
            pos (300,350)
        
    with Dissolve(0.5)    
    #pause 
    
    show cards as cards4:
        pos (500,250)
        
    if playercards[1] == "1":
        show card1 as card4a:
            pos (500,350)
    if playercards[1]  == "2":
        show card2 as card4b:
            pos (500,350)
    if playercards[1]  == "3":
        show card3 as card4c:
            pos (500,350)


    with Dissolve(0.5)
    #pause
    
    if clientcards != playercards:
        #client "You lost!{w=1.5}{nw}"
        
        call sound_beep from _call_sound_beep_2
        #with hpunch
        #clientplayer "You lost the game! {w=2.5}{nw}"
        
        menu:
            "Try again":
                jump isc_city_bar_cardgame
            "Back":
                hide screen isc_cardgame_check
                $ countdown = False
                $ countdown_sec = 0
                m "Okay, enough, bye!{w=2.5}{nw}"
                clientplayer "Bye.{w=2}{nw}"
                jump isc_city_bar
                
    else:
        hide screen isc_cardgame_check
        $ countdown = False
        $ countdown_sec = 0
        
        call sound_collect from _call_sound_collect_1
        with flash
        
        clientplayer "You won the game!{w=3}{nw}"
        
        if cardgame_gem == True:
            clientplayer "Here, my gift for you.{w=3}{nw}"
            $ cardgame_gem = False
            call take_gem from _call_take_gem_2
            
        clientplayer "Really well played!{w=2.5}{nw}"
        clientplayer "You look like a treasure hunter...{w=3}{nw}"
        clientplayer "I'll tell you something...{w=3}{nw}"
        clientplayer "I lost another gem somewhere around the spaceport interchange of the ISC.{w=5}{nw}"
        clientplayer "But I'm so rich and I don't need it.{w=3}{nw}"
        clientplayer "Maybe you'd like to find it?{w=3}{nw}"
        clientplayer "It's up to you!{w=2.5}{nw}"
        
    clientplayer "Thank you for playing.{w=3}{nw}"
    clientplayer "Bye.{w=2}{nw}"
    
    #pause
    
    
    
    
    #jump isc_city_bar_cardgame
    jump isc_city_bar
    
    
    
label isc_city_bar_cardgame_lost:
    
    hide screen isc_cardgame_check
    
    clientplayer "You lost the game!{w=3}{nw}"
    clientplayer "Bye-bye...{w=2}{nw}"
    jump isc_city_bar
    
    

screen isc_cardgame_check():
    
    if countdown_sec < 2:
        timer 1.0 repeat True action [Jump("isc_city_bar_cardgame_lost")]
    

    
