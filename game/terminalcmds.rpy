
# terminal commands - where the given commands will be analysed

init:
    $ hacker_in_prison = 0
    
    $ intercom_sat = False
    $ sat_connected_to = "A.R.K. Network."
    
    $ spacenet_state = "offline"
    
    $ io11_new_orbit_x = "500"
    $ io11_new_orbit_y = "380"
    
    
    $ isc_crane_pos_x = 0
    $ isc_crane_pos_y = 0
    
    $ crane_pos_name = "stow position"
    
    $ cargo_firedoors = "open"
    
    default xylo_sea_boat_company_call_flags = [0,0,0,0]



label term_commands:
    
    call sound_beep from _call_sound_beep_14
    

# command home
    if termtext == "home":
        
        $ showtext = """
    Hello World!
    [ascii_line]
    
    The terminal gives you the access to the 
    entire system.
    Type a command and press enter.

    Here some useful commands to start:

    Commands:
    locate = search in the space databank.
    home = show this screen.
    More: exit, login, cheat, reboot, sos...
    
    Phone:
    You can also make phone calls. For this,
    just enter the phone number in the terminal.
    """
            
        show text Text(showtext,text_align=termtext_align) at termtextpos
        jump term_menu
    
        
# command exit
    if termtext == "exit":
        
        #$ space_terminal = False
        
        call sound_beep from _call_sound_beep_15
        hide terminal
        hide text
        return
        #jump term_menu
        
        
# command locate
    if termtext == "locate":
        
        $ showtext = """
    Locate
    [ascii_line]

    locate = search in the space databank.
    
    Examples:
        locate sun
        locate megaship
        locate xylo
        
    Important:
        Using this command from your
        spaceship's terminal will allow
        you to copy the coordinates 
        to your cockpit map.

    """
            
        show text Text(showtext,text_align=termtext_align) at termtextpos
        jump term_menu
        
        
# command ssh io11
    if termtext == "ssh io11" and io11_remote_control == "enabled" :
        
        python:
            io11_pass_entry = renpy.input(_("Satellite Remote Control Password:"))
            io11_pass_entry = io11_pass_entry.strip()
            if not io11_pass_entry:
                io11_pass_entry = ""
                
        
        
        
        if io11_pass_entry == io11_pass:
            while True:
                $ showtext = """
    Satellite io-11
    [ascii_line]
    
    Actual Position : [satellite_pos]
    
    Satellite connected to : [sat_connected_to]
    
    What do you want to do?
    """
            
                show text Text(showtext,text_align=termtext_align) at termtextpos
                menu:
                    "Restart IO-11":
                        m "Okay, let's do this. {w=1.5} {nw}"
                        call server_progressbar from _call_server_progressbar
                        $ sat_connected_to = "-"

                        
                    "Connect to network":
                        menu:
                            "A.R.K. Network":
                                if intercom_sat == False:
                                    call server_progressbar from _call_server_progressbar_1
                                    call sound_connected from _call_sound_connected_9
                                    with flash
                                    $ sat_connected_to = "A.R.K. Network."
                                else:
                                    call server_progressbar from _call_server_progressbar_2
                                    $ sat_connected_to = "-"
                                    call sound_beep from _call_sound_beep_16
                                    with hpunch
                                    
                            
                            "SpaceNET":
                                if intercom_sat == True:
                                    call server_progressbar from _call_server_progressbar_3
                                    call sound_connected from _call_sound_connected_10
                                    with flash
                                    $ sat_connected_to = "SpaceNET"
                                else:
                                    call server_progressbar from _call_server_progressbar_4
                                    $ sat_connected_to = "-"
                                    call sound_beep from _call_sound_beep_17
                                    with hpunch
                            "Exit":
                                pass
                                
                                            
                    "Change orbit":
                        m "Okay, let's try this... {w=1.5} {nw}"
                        
                        python:
                            io11_new_orbit_x = renpy.input(_("New orbit X position:"), allow= "0123456789",  length= 3 )
                            io11_new_orbit_x = io11_new_orbit_x.strip()
                            if not io11_new_orbit_x:
                                io11_new_orbit_x = "-"
                        python:
                            io11_new_orbit_y = renpy.input(_("New orbit Y position:"), allow= "0123456789",  length= 3 )
                            io11_new_orbit_y = io11_new_orbit_y.strip()
                            if not io11_new_orbit_y:
                                io11_new_orbit_y = "-"
                        
                        call server_progressbar from _call_server_progressbar_5
                        
                        #"[io11_new_orbit_x], [io11_new_orbit_y]"
                        
                        if io11_new_orbit_x == "350" and io11_new_orbit_y == "150":
                            
                            $ intercom_sat = True
                            $ planet = "none"
                            
                            $ satellite_pos = (int(io11_new_orbit_x), int(io11_new_orbit_y))
                            
                            $ showtext ="""
    Satellite Io-11 
    [ascii_line]
    
    New orbit validated!
    
    Actual position: ([io11_new_orbit_x],[io11_new_orbit_y])
    """
                            show text Text(showtext,text_align=termtext_align) at termtextpos
                            call sound_connected from _call_sound_connected_11
                            with flash
                            
                            menu:
                                "Exit":
                                    pass
                        
                        else:
                            $ showtext ="""
    Satellite io-11 
    [ascii_line]
    
    Requested position: ([io11_new_orbit_x],[io11_new_orbit_y])
        
    Wrong position!
    
    It is not possible to move the satellite to 
    the given position.
    
    Process aborded.
    
    """
                            show text Text(showtext,text_align=termtext_align) at termtextpos
                            call sound_beep from _call_sound_beep_18
                            with hpunch
                            menu:
                                "Exit":
                                    pass
                            
 
                        
                    "Exit":
                        $ termtext = "home"
                        jump terminal

        
        else:
         $ showtext ="""
    Satellite io-11 
    [ascii_line]
    
    Wrong password. 
    
    Remote connection rejected !
    """
        show text Text(showtext,text_align=termtext_align) at termtextpos
        call sound_beep from _call_sound_beep_19
        with hpunch
        pause 3
        $ termtext = "home"
        jump terminal
            
        
        
    if termtext == "ssh io11" and io11_remote_control == "disabled" :
        $ showtext ="""
    Satellite io-11 
    [ascii_line]
    
    Remote connection rejected !
    """
        show text Text(showtext,text_align=termtext_align) at termtextpos
        call sound_beep from _call_sound_beep_20
        with hpunch
        pause 3
        $ termtext = "home"
        jump terminal

    
    
    
    
# command login
    if termtext == "login" :
        $ loginmenu = True
        jump term_login
        
        
    
        
# command sos
    if termtext == "sos" :
        $ showtext = """
    SOS
    [ascii_line]
    
    Do you really want to send a SOS message?
    """
        show text Text(showtext,text_align=termtext_align) at termtextpos
        call sound_beep from _call_sound_beep_21
        
        menu:
            "Send SOS":
                pass
            "Exit":
                $ termtext = "home"
                jump terminal
    
        
        
        call server_progressbar from _call_server_progressbar_6
        #show text "Sos sent!" at termtextpos2
        $ showtext = """
    SOS
    [ascii_line]
    
    Sos sent!
    """
        show text Text(showtext,text_align=termtext_align) at termtextpos
        
        call sound_connected from _call_sound_connected_12

        pause 2.5
        $ termtext = "home"
        jump terminal
   
   

# command 05060708 - boat trip
    if termtext == "05060708" :
        $ showtext = """
    Calling 
    [ascii_line]
    
    Calling [termtext]...
    """
        show text Text(showtext,text_align=termtext_align) at termtextpos
        
        call sound_connected from _call_sound_connected_13
        pause 1
        
        radio "Welcome to the Sea View Boat Company.{w=3.5} {nw}"
        radio "What can I do for you?{w=3.0} {nw}"
        
        
        $ questions = ["Hello!{w=1} {nw}", 
                        "Have you heard about SpaceNET? {w=2.5} {nw}", 
                        "I'd like to rent a boat.{w=2.5} {nw}", 
                        "I'm fine, thanks.{w=2.0} {nw}"]
        
        while True:
            menu:
                "[questions[0]]" if xylo_sea_boat_company_call_flags[0] == 0:
                    m "[questions[0]]"
                    radio "What can I do for you?{w=2.5} {nw}"
                    m "Are you a boat rental company? {w=3} {nw}"
                    radio "Yes, we are. How can I help? {w=3} {nw}"
                    $ xylo_sea_boat_company_call_flags[0] = 1
                    
                    
                "[questions[1]]" if xylo_sea_boat_company_call_flags[1] == 0:
                    m "[questions[1]]"
                    radio "No, I don't know what you are talking about.{w=3} {nw}"
                    radio "We are a boat rental company, not a tourist information center!{w=4.5} {nw}"
                    $ xylo_sea_boat_company_call_flags[1] = 1
                    
                    
                "[questions[2]]" if xylo_boat_trip == False:
                    m "[questions[2]]"

                    radio "Oh yes, for sure.{w=2.5} {nw}"
                    radio "You can rent a boat for one, two or three days.{w=4} {nw}"
                    radio "Which offer do you want?{w=3} {nw}"
                    
                    menu:
                        "1 day = 49c":
                            $ cash_xylo_sea_cabin = 49
                        "2 days = 89c":
                            $ cash_xylo_sea_cabin = 89
                        "3 days = 119c":
                            $ cash_xylo_sea_cabin = 119
                        
                        "Nothing, thanks.":
                            m "Nothing, thanks.{w=2.0} {nw}"
                            $ termtext = "home"
                            jump terminal
                            
                    if coins >= cash_xylo_sea_cabin:
                        call io_cash(-cash_xylo_sea_cabin) from _call_io_cash_26

                        # set amount (rounded) for island cabin
                        $ cash_xylo_sea_cabin = cash_xylo_sea_cabin + 1
                        
                        radio "Alright!{w=2.0} {nw}"
                        radio "A boat will wait for you at the pier.{w=3.5} {nw}"
                        radio "Enjoy the trip!{w=2.0} {nw}"
                        $ xylo_boat_trip = True
                        
                    else:
                        m "I don't have enough money!{w=3.5} {nw}"

                
                "[questions[3]]":
                    m "[questions[3]]"
                    radio "Bye!{w=1.0} {nw}"
                    
                    $ termtext = "home"
                    jump terminal




# command 00003477 - Paradise Island Company
    if termtext == "003477" :
        $ showtext = """
    Calling 
    [ascii_line]
    
    Calling [termtext]...
    """
        show text Text(showtext,text_align=termtext_align) at termtextpos
        
        call sound_connected from _call_sound_connected_44
        pause 1
        
        radio "Welcome to the Paradise Island Company!{w=3.5} {nw}"
        
        if xylo_sea_cabin_door_open == False:
            menu:
                "Help!":
                    m "Help!{w=1.5} {nw}"
                "I have to tell you something.":
                    m "I have to tell you something.{w=3} {nw}"
                "Do you know what?":
                    m "Do you know what?{w=2} {nw}"
                    
            m "I was on Paradise Island, but my boat ran out of power.{w=4} {nw}"
            m "I was trapped on the island!{w=3.5} {nw}"
            radio "Well... there is a cabin with some emergency battery packs.{w=4.0} {nw}"
            radio "You didn't find them, did you?{w=3} {nw}"
            m "Well, the cabin was closed...{w=3} {nw}"
            radio "Really? Let me see...{w=2.5} {nw}"
            m "But don't worry, I managed to...{w=3} {nw}"
            menu:
                "...escape the island!":
                    m "...escape the island!{w=2.5}{nw}"
                "...recharge my battery pack!":
                    m "...recharge my battery pack!{w=2.5}{nw}"
                "...make a bonfire!":
                    m "...make a bonfire!{w=2.5}{nw}"
                "...electrocute myself!":
                    m "...electrocute myself!{w=2.5}{nw}"
                
            radio "Wait. Well, you are right. The cabin's door is closed. This is strange.{w=4.5} {nw}"
            m "...as I said, I figured out a way...{w=3} {nw}"
            radio "I'm really sorry. Somebody closed the door and didn't tell me.{w=4} {nw}"
            m "...as I said, this...{w=2} {nw}"
            radio "I will open it remotely.{w=3} {nw}"
            m "...I mean, I don't need...{w=3} {nw}"
            radio "Wait...{w=1.5} {nw}"
            m "...but...{w=1.5} {nw}"
            radio "Okay! Now it is open again.{w=3} {nw}"
            radio "Good.{w=1.5} {nw}"
            radio "What do you want to say?{w=3} {nw}"
            $ xylo_sea_cabin_door_open = True
            
        m "...{w=1.5} {nw}"
        m "Never mind.{w=2} {nw}"
        radio "Alright. If you need anything, just call again.{w=3.5} {nw}"
        radio "Bye!{w=1.5} {nw}"

        $ termtext = "home"
        jump terminal




# command 01020304 - a.r.k corporation
    if termtext == "01020304" :
        $ showtext = """
    Calling 
    [ascii_line]
    
    Calling [termtext]...
    """
        show text Text(showtext,text_align=termtext_align) at termtextpos
        
        call sound_connected from _call_sound_connected_14
        pause 1
        
        radio "Hello, welcome to A.R.K. Corporation. {w=3} {nw}"
        radio "How can I help you? {w=2} {nw}"
        
        
        $ questions = ["Hi, I would like to visit your company. {w=3} {nw}",
                        "I'm fine, thanks. {w=2.0} {nw}"]
        
        while True:
            menu:
                "[questions[0]]":
                    m "[questions[0]]"
                    radio "Yes, no problem. {w=2.5} {nw}"
                    radio "We can make an appointment. {w=3} {nw}"
                    radio "What is your name? {w=2.5} {nw}"
                    m "My name is [playername]. {w=2.5} {nw}"
                    radio "Alright!{w=1} You are registered now. {w=2.5} {nw}"
                    radio "Just come to our building, our guard at the reception will let you in. {w=5} {nw}"
                    m "Okay, thanks! {w=2.5} {nw}"
                    radio "See you soon, bye!{w=2.5} {nw}"
                    $ xylo_village1_building_reception = 2
                    
                    $ termtext = "home"
                    jump terminal
                
                "[questions[1]]":
                    m "[questions[1]]"
                    radio "No problem, bye!{w=2.0} {nw}"
                    
                    $ termtext = "home"
                    jump terminal
    

# command cheat
    if termtext == "cheat" :
        $ showtext = """
    Cheat
    [ascii_line]
    
    """
        show text Text(showtext,text_align=termtext_align) at termtextpos
        call sound_electroshock from _call_sound_electroshock_28
        with hpunch
        m "Cheating is not a good idea right now... {w=3} {nw}"
        call sound_beep from _call_sound_beep_22
        $ termtext = "home"
        jump terminal
        

        
       
        
# command SpaceNET
    if termtext == "spacenet" :
        
        call nodes_list_update from _call_nodes_list_update
        
        $ showtext = """
    SpaceNET
    [ascii_line]
    
    SpaceNET: [spacenet_state]
    
    Intercom satellite in orbit: [intercom_sat]
    Intercom satellite network: [sat_connected_to]
    
    Nodes:
    Needed: [max_nodes_amount]
    Active: [active_nodes_amount]
    
    Active Nodes:
    [spacenetnodes_text]


    """
        show text Text(showtext,text_align=termtext_align) at termtextpos
        call sound_beep from _call_sound_beep_23
        
        $ spacenetmenu = True
         
        menu:
            #"reset spacenet state":
            #    $ spacenet_state = "offline"
            
            "Launch SpaceNET" if intercom_sat == True and sat_connected_to == "SpaceNET" and active_nodes_amount == max_nodes_amount and spacenet_state == "offline":
                m "Yes, finally! Let's launch it! {w=2.5}{nw}"
                call sound_modem from _call_sound_modem_2
                call server_progressbar from _call_server_progressbar_7
                call sound_connected from _call_sound_connected_15
                with flash
                
                
                $ spacenet_state = "online"
                
                $ showtext = """
    SpaceNET
    [ascii_line]
    
    SpaceNET is now connected!
    
    SpaceNET state: [spacenet_state]
 

    """
                show text Text(showtext,text_align=termtext_align) at termtextpos
                
                pause 4
                
                $ termtext = "spacenet"
                jump terminal
                
                
            
            "Info":
                $ showtext = """
    SpaceNET
    [ascii_line]
    
    Welcome to SpaceNET!
    
    SpaceNET is a free knowledge network.
    
    All nodes need to be activated and connected
    to each other to allow SpaceNet to work.

    A node can be everywhere.
    A node is just a SpaceNET server with
    the SpaceNET software.

    SpaceNET also needs an intercom satellite 
    to work properly.

    """
                show text Text(showtext,text_align=termtext_align) at termtextpos
                menu:
                    "Back":
                        $ termtext = "spacenet"
                        jump term_commands
        
            
            "Exit":
                pass
                
        $ termtext = "home"
        jump terminal






# command 007008 - isc administration
    if termtext == "007008" :
        $ showtext = """
    Calling 
    [ascii_line]
    
    Calling [termtext]...
    """
        show text Text(showtext,text_align=termtext_align) at termtextpos
        
        call sound_connected from _call_sound_connected_16
        pause 1
        
        radio "Hello, welcome to the administration of the Industrial Space City. {w=3.5} {nw}"
        radio "How can I help you? {w=2} {nw}"
        
        
        $ questions = ["I need a landing authorization. {w=2} {nw}",
                        "I'm fine, thanks. {w=2.0} {nw}"]
        
        while True:
            menu:
                "[questions[0]]":
                    m "[questions[0]]"
                    radio "Yes, no problem. {w=1.5} {nw}"
                    call sound_connected from _call_sound_connected_17
                    with flash
                    $ isc_spaceport_auth = True
                    
                    radio "You are now allowed to land on the main Industrial Space City Spaceport! {w=3} {nw}"
                    radio "Call anytime if you need anything else.{w=2.5} {nw}"
                    radio "Bye!{w=1} {nw}"
                    

                    $ termtext = "home"
                    jump terminal
                
                "[questions[1]]":
                    m "[questions[1]]"
                    radio "Okay, bye.{w=2.0} {nw}"
                    
                    $ termtext = "home"
                    jump terminal

    
    




# command locate megaship
    if termtext == "locate megaship" :
        call terminal_locate("megaship") from _call_terminal_locate
        jump terminal

# command locate xylo
    if termtext == "locate xylo" :
        call terminal_locate("xylo") from _call_terminal_locate_1
        jump terminal
        

# command locate sun
    if termtext == "locate sun" :
        call terminal_locate("sun") from _call_terminal_locate_2
        jump terminal


# command locate satellite io11
    if termtext == "locate io11" :
        call terminal_locate("io11") from _call_terminal_locate_3
        jump terminal
        
# command locate cargo
    if termtext == "locate cargo" and cargo_remote_control != "none":
        call terminal_locate("cargo") from _call_terminal_locate_4
        jump terminal
        
# command locate isc
    if termtext == "locate isc" :
        call terminal_locate("isc") from _call_terminal_locate_5
        jump terminal
        
        
# command locate asteroids
    if termtext == "locate asteroids" :
        call terminal_locate("asteroids") from _call_terminal_locate_6
        jump terminal
        

        
    
    


# command 003007 - 4n0nymu5 phone proxy 
    if termtext == "003007" :
        $ showtext = """
    Calling 
    [ascii_line]
    
    Calling [termtext]...
    """
        show text Text(showtext,text_align=termtext_align) at termtextpos
        
        if cargo_exploded == 2:
            call sound_connected from _call_sound_connected_18
            pause 1
            
            hacker "Hello! {w=1.5} {nw}"
            hacker "Well done [playername]! Now all the weapons are destroyed.{w=4.5} {nw}"
            hacker "This is great! {w=2.5} {nw}"
            hacker "Please go to Sam and talk to him. {w=3.5} {nw}"
            hacker "I think he will know what we can do now. {w=4} {nw}"
            hacker "Bye! {w=1.5} {nw}"
            jump terminal
            
    
        if hacker_in_prison == 0:
            
            call sound_connected from _call_sound_connected_19
            pause 1
            
            hacker "Hello [playername]. Thank you for calling.{w=3.5} {nw}"
            hacker "I need to tell you a couple of important things... {w=4} {nw}"
            hacker "First, thank you for the help. {w=3} {nw}"
            hacker "Without you, we would not be able to accomplish our mission! {w=5} {nw}"
            hacker "Second, wait... {w=2.5} {nw}"
            
            call music_intro from _call_music_intro
            
            hacker "... {w=2} {nw}"
            
            $ questions = ["Are you okay? {w=2} {nw}",
                            "What's wrong? {w=2.0} {nw}",
                            "I think I know what's happening! {w=2.5} {nw}",
                            "I experienced something similar. {w=2.5} {nw}",
                            "I think I know where you are. {w=2.5} {nw}",
                            "Please, keep calm and listen. {w=2.5} {nw}"]

            menu:
                "[questions[0]]":
                    m "[questions[0]]"
                    
                "[questions[1]]":
                    m "[questions[1]]"
            
            
            hacker "Something strange is happening... {w=3} {nw}"
            hacker "I can't move my spaceship anymore... {w=3} {nw}"
            hacker "And it is moving by itself! {w=3} {nw}"

            menu:
                "[questions[2]]":
                    m "[questions[2]]"
                    
                "[questions[3]]":
                    m "[questions[3]]"
                    
            m "Is there a huge spaceship close to you? {w=3.5} {nw}"
            hacker "Yes... {w=1} And it is controlling my spaceship!{w=2} They are catching me!{w=3}{nw}"
            hacker "Help!{w=2}{nw}"
            hacker "I'm coming closer to the spaceship...{w=3.5}{nw}"
            hacker "A huge door is opening right now... {w=3.5}{nw}"
            hacker "My spaceship is going straight into it!{w=3.5}{nw}"
            
            menu:
                "[questions[4]]":
                    m "[questions[4]]"
                    
                "[questions[5]]":
                    m "[questions[5]]"
                    
            
            m "You are captured by the prison megaship of the government. {w=4}{nw}"
            m "They will put you into a prison cell. {w=3.5}{nw}"
            m "But there is a way out! {w=3}{nw}"
            m "I could try to get there, but I'll need some tools. {w=4}{nw}"   
            hacker "If you need anything, go to Sam.{w=3.5}{nw}"
            hacker "He might help you.{w=2.5}{nw}"
            hacker "Please help me out!{w=2.5}{nw}"
            hacker "...{w=2}{nw}"
            
            stop music fadeout 3.0
            
            m "4n0nym0u5?{w=1} 4n0nym0u5?{w=1} 4n0nym0u5...{w=2}{nw}"
            
            m "...{w=1}{nw}"
            m "Okay, let see what I can do. {w=3}{nw}"
            
            #stop music fadeout 1.0

            $ hacker_in_prison = 1
            
        else:
            #"[hacker_in_prison]"
            pause 2
            m "Nobody is there... {w=2}{nw}"
            
        jump terminal
        
        
        


# command ssh isc
    if termtext == "ssh isc" : 
        call sound_connected from _call_sound_connected_20
        $ showtext = """
    ssh isc
    [ascii_line]
    
    Welcome to ISC remote control.
    
    Crane position: x[isc_crane_pos_x], y[isc_crane_pos_y]
    
    Position name: [crane_pos_name]
    """
        show text Text(showtext,text_align=termtext_align) at termtextpos
        
        menu:
            "Move crane":
                call sound_beep from _call_sound_beep_24
                
                while True:
                    menu:
                        "North":
                            if isc_crane_pos_y < 1:
                                call sound_movingwall from _call_sound_movingwall_1
                                $ crane_pos_name = "moving..."
                                show text Text(showtext,text_align=termtext_align) at termtextpos
                                pause 1
                                $ isc_crane_pos_y += 1
                            else:
                                call sound_electroshock from _call_sound_electroshock_8
                                with hpunch
                        "South":
                            if isc_crane_pos_y > 0:
                                call sound_movingwall from _call_sound_movingwall_2
                                $ crane_pos_name = "moving..."
                                show text Text(showtext,text_align=termtext_align) at termtextpos
                                pause 1
                                $ isc_crane_pos_y -= 1
                            else:
                                call sound_electroshock from _call_sound_electroshock_9
                                with hpunch
                        "East":
                            if isc_crane_pos_x < 1:
                                call sound_movingwall from _call_sound_movingwall_3
                                $ crane_pos_name = "moving..."
                                show text Text(showtext,text_align=termtext_align) at termtextpos
                                pause 1
                                $ isc_crane_pos_x += 1
                            else:
                                call sound_electroshock from _call_sound_electroshock_10
                                with hpunch
                        "West":
                            if isc_crane_pos_x > 0:
                                call sound_movingwall from _call_sound_movingwall_4
                                $ crane_pos_name = "moving..."
                                show text Text(showtext,text_align=termtext_align) at termtextpos
                                pause 1
                                $ isc_crane_pos_x -= 1
                            else:
                                call sound_electroshock from _call_sound_electroshock_11
                                with hpunch
                        "Stow":
                            if isc_crane_pos_x == 1 or isc_crane_pos_y == 1:
                                call sound_movingwall from _call_sound_movingwall_5
                                $ crane_pos_name = "moving..."
                                show text Text(showtext,text_align=termtext_align) at termtextpos
                                pause 1
                                $ isc_crane_pos_x = 0
                                $ isc_crane_pos_y = 0
                            else:
                                call sound_electroshock from _call_sound_electroshock_12
                                with hpunch
                            
                        "Exit":
                            jump terminal


                    
                            
                    if isc_crane_pos_x == 0 and isc_crane_pos_y == 0:
                        $ crane_pos_name = "stow position"
                        
                    elif isc_crane_pos_x == 0 and isc_crane_pos_y == 1:
                        $ crane_pos_name = "spaceport"
                        
                    elif isc_crane_pos_x == 1 and isc_crane_pos_y == 1:
                        $ crane_pos_name = "city center"
                        if isc_sysadmin_move == 1:
                            $ isc_sysadmin_move = 2
                        
                    
                    elif isc_crane_pos_x == 1 and isc_crane_pos_y == 0:
                        $ crane_pos_name = "space gateway"
                    
                    else:
                        $ crane_pos_name = ""
                    
                    show text Text(showtext,text_align=termtext_align) at termtextpos
                
            "Exit":
                pass
                $ termtext = "home"
                jump terminal
    
        $ termtext = "home"
        jump terminal





# command ssh cargo
    if termtext == "ssh cargo" and cargo_remote_control != "none":
        
        python:
            cargo_pass_entry = renpy.input(_("ssh cargo password:"))
            cargo_pass_entry = cargo_pass_entry.strip()
            if not cargo_pass_entry:
                cargo_pass_entry = ""
                
        
        if cargo_pass_entry == "convoy":
            
            if cargo_remote_control == "enabled":
            
                call sound_connected from _call_sound_connected_21
                $ showtext = """
    ssh cargo
    [ascii_line]
    
    Welcome to Space Cargo remote control.
    
    
    Cargo reactor state: [cargo_reactor_state]
    
    Fire doors: [cargo_firedoors]
    """
                show text Text(showtext,text_align=termtext_align) at termtextpos
                
                menu:
                    "Close fire doors":
                        if countdown_sec > 0:
                            
                            $ cargo_firedoors = "closed"
                            
                            show text Text(showtext,text_align=termtext_align) at termtextpos
                            
                            $ countdown_sec = 0
                            $ countdown = False
                            
                            call sound_connected from _call_sound_connected_22
                            
                            m "Okay... Now the reactor room is closed...{w=3.5}{nw}"
                            m "Now, nobody can enter it and restart the reactor.{w=3.5}{nw}"
                            m "The cooling systems are also down.{w=3}{nw}"
                            m "The reactor will overheat!{w=3}{nw}"
                            m "Let's see...{w=2}{nw}"
 
                            
                            jump cargo_explosion_anim
                            
                            
                        
                        else:
                            $ countdown_sec = 0
                            $ countdown = False
                            $ alarm_on = False
                            with hpunch
                            $ showtext ="""
    ssh cargo 
    [ascii_line]
    
    Remote connection rejected!
    """
                            show text Text(showtext,text_align=termtext_align) at termtextpos
                            call sound_beep from _call_sound_beep_25
                            $ cargo_remote_control = "disabled"
                            m "Oh no! I think the crew restarted the reactor and disabled the remote control!{w=5}{nw}"
                            #pause 3
                            $ termtext = "home"
                            jump terminal
                            
                    
                    "Exit":
                        $ termtext = "home"
                        jump terminal
                        
            if cargo_remote_control == "enabled":
                $ showtext ="""
    ssh cargo 
    [ascii_line]
    
    Remote connection rejected!
    """
                show text Text(showtext,text_align=termtext_align) at termtextpos
                call sound_beep from _call_sound_beep_26
                pause 3
                $ termtext = "home"
                jump terminal
            


# cargo mission reminder
    if termtext == "111999" :
        $ showtext = """
    Calling 
    [ascii_line]
    
    Calling [termtext]...
    """
        show text Text(showtext,text_align=termtext_align) at termtextpos
        
        hacker "Hello [playername]!{w=3} {nw}"
        hacker "This is your cargo infiltration mission:{w=4} {nw}"
        
        call isc_spaceflight_cargo_mission from _call_isc_spaceflight_cargo_mission
        
        hacker "Good luck!{w=2} {nw}"
        
        jump terminal
        






# access game menu from terminal
    if termtext == "save" :
        $ ShowMenu("save")() # extra () needed
        jump terminal
        
    if termtext == "load" :
        $ ShowMenu("load")() 
        jump terminal
        
    if termtext == "preferences" :
        $ ShowMenu("preferences")() 
        jump terminal
        
    if termtext == "prefs" :
        $ ShowMenu("preferences")() 
        jump terminal
        
    if termtext == "help" :
        $ ShowMenu("help")() 
        jump terminal
        
    if termtext == "history" :
        $ ShowMenu("history")() 
        jump terminal
        
        
        
# reboot
    if termtext == "reboot" :
        call server_progressbar from _call_server_progressbar_17
        call sound_scan from _call_sound_scan_10
        with flash
        jump terminal
        
        
        
# player's name
    if termtext == playername:
        call sound_connected from _call_sound_connected_43
        $ showtext = """
    [playername]
    [ascii_line]
    
    That's you!
    """
        show text Text(showtext,text_align=termtext_align) at termtextpos
        menu:
            "Exit":
                pass
        jump terminal



    
#~     if termtext == "sarah" : 
#~         call sound_connected
#~         $ showtext = """
#~     identify [termtext]
#~     [ascii_line]
    
#~     Name: Sarah C.
#~     Age: 28
#~     Height: 1.60m
#~     Weight: 65kg
#~     Hair: Brown
#~     Eyes: Blue
#~     Married: No
#~     Children: None
#~     Profession: Vendor
#~     Works at: [xylo_village_name]
#~     Registered at: [xylo_village_name], Xylo Sea
#~     Spaceship Driving License: No
#~     Located at: [xylo_village_name]

#~     """
#~         show text Text(showtext,text_align=termtext_align) at termtextpos
        
#~         image vendor_xylo = "sides/vendor.png"
#~         show vendor_xylo:
#~             anchor (1.0,0.0)
#~             pos (500, 105)
        
#~         menu:
#~             "Delete":
#~                 call sound_electroshock
#~                 with hpunch
#~                 "Error!{w=2} {nw}"
#~                 jump term_commands
#~             "Back":
#~                 hide vendor_xylo
#~                 jump terminal
        







######################################

#if nothing happens, then
    $ showtext = """
    Terminal
    [ascii_line]
    
    Command: [termtext] - command not found.
    """
    show text Text(showtext,text_align=termtext_align) at termtextpos
    #show text (_("Command: [termtext] - command not found.")) at termtextpos2
    pause 2
    $ termtext = "home"
    jump terminal
    #jump term_menu





