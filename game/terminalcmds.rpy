
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
    
    $ xylo_sea_boat_company_call_flags = [0,0,0,0]



label term_commands:
    
    call sound_beep from _call_sound_beep_14
    

# command help
    if termtext == "help":
        
        $ showtext = """
    Hello World!
    [ascii_line]
    
    The terminal gives you the access to your 
    entire system.
    Type a command and press Enter.

    Here some useful commands to start:

    Commands:
    locate = search in the databank.
    help = show this help file.
    More: exit, login, cheat, sos...
    
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
        
        
# command help
    if termtext == "locate":
        
        $ showtext = """
    Locate
    [ascii_line]

    locate = search in the databank.
    
    Exemple:
        locate sun
        locate megaship
        locate xylo

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
    Satellite Io-11
    [ascii_line]
    
    Actual Position : [satellite_pos]
    
    Satellite Connected to : [sat_connected_to]
    
    What do you want to do?
    """
            
                show text Text(showtext,text_align=termtext_align) at termtextpos
                menu:
                    "restart Io-11":
                        m "Okay let's do this. {w=1.5} {nw}"
                        call server_progressbar from _call_server_progressbar
                        $ sat_connected_to = "-"

                        
                    "connect to network":
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
                            "exit":
                                pass
                                
                                            
                    "change orbit":
                        m "Okay let's try this... {w=1.5} {nw}"
                        
                        python:
                            io11_new_orbit_x = renpy.input(_("New Orbit X Position:"), allow= "0123456789",  length= 3 )
                            io11_new_orbit_x = io11_new_orbit_x.strip()
                            if not io11_new_orbit_x:
                                io11_new_orbit_x = "-"
                        python:
                            io11_new_orbit_y = renpy.input(_("New Orbit Y Position:"), allow= "0123456789",  length= 3 )
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
    
    Actual Position: ([io11_new_orbit_x],[io11_new_orbit_y])
    """
                            show text Text(showtext,text_align=termtext_align) at termtextpos
                            call sound_connected from _call_sound_connected_11
                            with flash
                            
                            menu:
                                "Exit":
                                    pass
                        
                        else:
                            $ showtext ="""
    Satellite Io-11 
    [ascii_line]
    
    Requested Position: ([io11_new_orbit_x],[io11_new_orbit_y])
        
    Wrong position!
    
    It is not possible to set an orbit at 
    the given position.
    
    Process aborded.
    
    """
                            show text Text(showtext,text_align=termtext_align) at termtextpos
                            call sound_beep from _call_sound_beep_18
                            with hpunch
                            menu:
                                "Exit":
                                    pass
                            
 
                        
                    "exit":
                        $ termtext = "help"
                        jump terminal

        
        else:
         $ showtext ="""
    Satellite Io-11 
    [ascii_line]
    
    Wrong password. 
    
    Remote Connection rejected !
    """
        show text Text(showtext,text_align=termtext_align) at termtextpos
        call sound_beep from _call_sound_beep_19
        with hpunch
        pause 3
        $ termtext = "help"
        jump terminal
            
        
        
    if termtext == "ssh io11" and io11_remote_control == "disabled" :
        $ showtext ="""
    Satellite Io-11 
    [ascii_line]
    
    Remote Connection rejected !
    """
        show text Text(showtext,text_align=termtext_align) at termtextpos
        call sound_beep from _call_sound_beep_20
        with hpunch
        pause 3
        $ termtext = "help"
        jump terminal

    
    
    
    
# command login
    if termtext == "login" :
        jump term_login
        
        
    
        
# command sos
    if termtext == "sos" :
        $ showtext = """
    SOS
    [ascii_line]
    
    Do you really want to send a sos message?
    """
        show text Text(showtext,text_align=termtext_align) at termtextpos
        call sound_beep from _call_sound_beep_21
        
        menu:
            "send sos":
                pass
            "exit":
                $ termtext = "help"
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
        $ termtext = "help"
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
        
        radio "Welcome to sea view boat company.{w=3.0} {nw}"
        
        
        $ questions = ["Hello!{w=1} {nw}", 
                        "Have you heard about SpaceNET? {w=2.0} {nw}", 
                        "I'd like to have some info about the boat trips on the xylo sea.{w=4.0} {nw}", 
                        "Bye bye.{w=2.0} {nw}"]
        
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
                    radio "We are a boat rental company, not a tourist information!{w=4} {nw}"
                    m "Okay, bye!{w=1.5} {nw}"
                    $ xylo_sea_boat_company_call_flags[1] = 1
                    
                    
                "[questions[2]]" if xylo_sea_boat_company_call_flags[0] == 1:
                    m "[questions[2]]"
                    radio "Oh yes, for sure!{w=2.0} {nw}"
                    radio "Unfortunatly we have no free boat for rent right now.{w=3.0} {nw}"
                    radio "Please call us later, thanks!{w=3.0} {nw}"
                
                "[questions[3]]":
                    m "[questions[3]]"
                    radio "Bye!{w=1.0} {nw}"
                    
                    $ termtext = "help"
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
        
        radio "Hello, welcome to a.r.k. corporation. {w=2.5} {nw}"
        radio "How can I help you? {w=2} {nw}"
        
        
        $ questions = ["Hi, I would like to visit your company. {w=2} {nw}",
                        "I'm fine, thanks. {w=2.0} {nw}"]
        
        while True:
            menu:
                "[questions[0]]":
                    m "[questions[0]]"
                    radio "Yes, no problem. {w=1.5} {nw}"
                    radio "We can make an appointment. {w=2} {nw}"
                    radio "How is your name? {w=1.5} {nw}"
                    m "My name is [playername]. {w=1.5} {nw}"
                    radio "Alright!{w=1} Your are registered now. {w=2.5} {nw}"
                    radio "Just come to our building, our guard at the reception will let you in. {w=4} {nw}"
                    m "Okay, thanks! {w=1.5} {nw}"
                    radio "See you soon, bye!{w=2} {nw}"
                    $ xylo_village1_building_reception = 2
                    
                    $ termtext = "help"
                    jump terminal
                
                "[questions[1]]":
                    m "[questions[1]]"
                    radio "No problem, bye!{w=2.0} {nw}"
                    
                    $ termtext = "help"
                    jump terminal
    

# command cheat
    if termtext == "cheat" :
        $ showtext = """
    Cheat
    [ascii_line]
    
    """
        show text Text(showtext,text_align=termtext_align) at termtextpos
        call sound_beep from _call_sound_beep_22
        with hpunch
        m "Cheating is not a good idea right now... {w=2.5} {nw}"
        $ termtext = "help"
        jump terminal
        


# command cheat missions
    if termtext == "cheat missions" :
        $ showtext = """
    Cheat missions
    [ascii_line]
    
    You finished all missions!
    """
        show text Text(showtext,text_align=termtext_align) at termtextpos
        call sound_connected from _call_sound_connected_15
        with flash
        
        call cheat_missions from _call_cheat_missions
        
        pause 3
        $ termtext = "help"
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
            "launch SpaceNET" if intercom_sat == True and sat_connected_to == "SpaceNET" and active_nodes_amount == max_nodes_amount and spacenet_state == "offline":
                m "Yes, finally! Let's launch it!! {w=2.5}{nw}"
                call server_progressbar from _call_server_progressbar_7
                call sound_collect from _call_sound_collect_2
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
                
                
            
            "info":
                $ showtext = """
    SpaceNET
    [ascii_line]
    
    Welcome to SpaceNET!
    
    SpaceNET is a free knowledge network.
    
    All nodes need to be activated and connected
    to each other to allow SpaceNet to work.

    A node can be everywhere.
    A nodes is just a SpaceNET server with
    the SpaceNET software.

    SpaceNET also needs an intercom satellite 
    to work properly.

    """
                show text Text(showtext,text_align=termtext_align) at termtextpos
                menu:
                    "back":
                        $ termtext = "spacenet"
                        jump term_commands
        
            
            "exit":
                pass
                
        $ termtext = "help"
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
        
        
        $ questions = ["I need a landing authorisation. {w=2} {nw}",
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
                    radio "Call anytime if you need something else.{w=2.5} {nw}"
                    radio "Bye!{w=1} {nw}"
                    

                    $ termtext = "help"
                    jump terminal
                
                "[questions[1]]":
                    m "[questions[1]]"
                    radio "Okay, bye.{w=2.0} {nw}"
                    
                    $ termtext = "help"
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
            hacker "Well done [playername]! Now all the weapons are destroyed.{w=4} {nw}"
            hacker "This is great! {w=2} {nw}"
            hacker "Please go to Sam and talk to him. {w=3} {nw}"
            hacker "I think he will know what we can do now. {w=3} {nw}"
            hacker "Bye! {w=1.5} {nw}"
            jump terminal
            
    
        if hacker_in_prison == 0:
            
            call sound_connected from _call_sound_connected_19
            pause 1
            
            hacker "Hello [playername]. Thank you for calling.{w=2.5} {nw}"
            hacker "Please, be careful with the satellite mission. {w=3} {nw}"
            hacker "Before you flight to the satellite, you need to know a couple of important things... {w=4.5} {nw}"
            hacker "First, thank you for the help. {w=2} {nw}"
            hacker "Without you we would not be able to accomplish our mission! {w=3} {nw}"
            hacker "Second, wait... {w=2} {nw}"
            
            call music_intro from _call_music_intro
            
            hacker "... {w=2} {nw}"
            
            $ questions = ["Are you okay? {w=2} {nw}",
                            "What's wrong? {w=2.0} {nw}",
                            "I think I know what's happening! {w=2.0} {nw}",
                            "I think I know where you are. {w=2.0} {nw}",
                            "Please, keep calm and listen. {w=2.0} {nw}"]

            menu:
                "[questions[0]]":
                    m "[questions[0]]"
                    
                "[questions[1]]":
                    m "[questions[1]]"
            
            
            hacker "Something strange is happening... {w=2.5} {nw}"
            hacker "I can't move my spaceship anymore... {w=2.5} {nw}"
            hacker "And it is moving by itself! {w=2.5} {nw}"

            menu:
                "[questions[2]]":
                    m "[questions[2]]"
                    
            m "Is there a huge spaceship close to you? {w=3} {nw}"
            hacker "Yes... {w=1} And it is controlling my spaceship!{w=2} They are getting me!{w=2}{nw}"
            hacker "Help!{w=2}{nw}"
            hacker "I'm coming closer to the spaceship...{w=3}{nw}"
            hacker "A huge door is opening right now... {w=3}{nw}"
            hacker "My spaceship is going straight into it!{w=3}{nw}"
            
            menu:
                "[questions[3]]":
                    m "[questions[3]]"
                    
                "[questions[4]]":
                    m "[questions[4]]"
                    
            
            m "You are capturated by the prison megaship of the governement. {w=4}{nw}"
            m "They will put you into a prison cell. {w=3}{nw}"
            m "But there is a way out! {w=3}{nw}"
            m "I could try to get there, but I'll need some tools. {w=3.5}{nw}"   
            hacker "If you need anything, go to Sam.{w=3.5}{nw}"
            hacker "He can certainly help you.{w=3}{nw}"
            hacker "Please help me out!{w=3}{nw}"
            hacker "...{w=2}{nw}"
            
            stop music fadeout 3.0
            
            m "4n0nym0u5?{w=1} 4n0nym0u5?{w=1} 4n0nym0u5...{w=1}{nw}"
            
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
        
        #python:
        #    io11_pass_entry = renpy.input(_("ssh isc Password:"))
        #    io11_pass_entry = io11_pass_entry.strip()
        #    if not io11_pass_entry:
        #        io11_pass_entry = ""
                
        
        #if io11_pass_entry == "isccrane":
            
        call sound_connected from _call_sound_connected_20
        $ showtext = """
    ssh isc
    [ascii_line]
    
    Welcome to isc remote control.
    
    Crane position : x[isc_crane_pos_x], y[isc_crane_pos_y]
    
    Position name : [crane_pos_name]
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
                        $ isc_sysadmin_move = 2
                        
                    
                    elif isc_crane_pos_x == 1 and isc_crane_pos_y == 0:
                        $ crane_pos_name = "space gateway"
                    
                    else:
                        $ crane_pos_name = ""
                    
                    show text Text(showtext,text_align=termtext_align) at termtextpos
                
            "Exit":
                pass
                $ termtext = "help"
                jump terminal
    
        $ termtext = "help"
        jump terminal





# command ssh cargo
    if termtext == "ssh cargo" and cargo_remote_control != "none":
        
        python:
            cargo_pass_entry = renpy.input(_("ssh cargo Password:"))
            cargo_pass_entry = cargo_pass_entry.strip()
            if not cargo_pass_entry:
                cargo_pass_entry = ""
                
        
        if cargo_pass_entry == "convoy":
            
            if cargo_remote_control == "enabled":
            
                call sound_connected from _call_sound_connected_21
                $ showtext = """
    ssh cargo
    [ascii_line]
    
    Welcome to space cargo remote control.
    
    
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
                            m "Nobody can enter it and restart the reactor!{w=3.5}{nw}"
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
    
    Remote Connection rejected !
    """
                            show text Text(showtext,text_align=termtext_align) at termtextpos
                            call sound_beep from _call_sound_beep_25
                            $ cargo_remote_control = "disabled"
                            m "Oh no! I think the crew restarted the reactor and disabled the remote control!{w=5}{nw}"
                            #pause 3
                            $ termtext = "help"
                            jump terminal
                            
                    
                    "Exit":
                        $ termtext = "help"
                        jump terminal
                        
            if cargo_remote_control == "enabled":
                $ showtext ="""
    ssh cargo 
    [ascii_line]
    
    Remote Connection rejected !
    """
                show text Text(showtext,text_align=termtext_align) at termtextpos
                call sound_beep from _call_sound_beep_26
                pause 3
                $ termtext = "help"
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
        




######################################

#if nothing happens, then
    show text (_("Command: [termtext] - command not found.")) at termtextpos2
    pause 2
    $ termtext = "help"
    jump terminal
    #jump term_menu





