# terminal

image terminal = "images/terminal.png"

#define termtextpos = Position(xpos = 245, ypos=60, xanchor=0.5, yanchor=0.0)

init:
    transform termtextpos:
        pos (20,30)
        anchor (0,0)
        
    transform termtextpos2:
        pos (47,57)
        anchor (0,0)
    
    $ termtext_align = 0.0
    $ server_itemchoice = 0

init:
    $ termtext = "no entry"
    
    $ termlogin = ""
    $ termpass = ""
    
    $ term_login_done= False





label terminal:
    $ engine = "terminal"
    $ pnc_nodes_visible = False
    
    $ inventory_select = ""
    
    show terminal at topleft
    #show screen notify("terminal")
    call sound_beep from _call_sound_beep_28
    
    if shadow_enable == 1:
        show shadow:
            pos (270, 240)
    
    $ termtext = "help"
    
    hide spacenetsender

    jump term_commands
    

# main menu
label term_menu:
    menu:
        "Terminal":
            call sound_beep from _call_sound_beep_71
            $ showtext = """
    Terminal
    [ascii_line]
    """
            show text Text(showtext,text_align=termtext_align) at termtextpos
            #hide text
            python:
                termtext = renpy.input(_("Type a command:"))
                termtext = termtext.strip().lower()
                if not termtext:
                    termtext = "no entry"

            jump term_commands
            
        "Login" if loginmenu == True:
            $ termtext = "login"
            jump term_login
            #jump term_menu
            
        "Spacenet" if spacenetmenu == True:
            $ termtext = "spacenet"
            jump term_commands
            
        #"missions":
        #    jump term_missions
        
        "Exit":
            $ landing = False
            
            $ pnc_nodes_visible = True
            
            #$ space_terminal = False
            
            call sound_beep from _call_sound_beep_29
            hide terminal
            hide text
            return
            












#################################

# login
label term_login:
    call sound_beep from _call_sound_beep_30
    
    # skip login if already logged in once in game
    if term_login_done == True:
        jump server_start
    
    
    if superdev == 1:
        "Try ID: [playername], Password: freedom"
    
    python:
        termlogin = renpy.input(_("ID:"))
        termlogin = termlogin.strip().lower()
        if not termlogin:
            termlogin = "no entry"
            
    call sound_beep from _call_sound_beep_31
    python:
        termpass = renpy.input(_("Password:"))
        termpass = termpass.strip().lower()
        if not termpass:
            termpass = "no entry"
            
    call sound_beep from _call_sound_beep_32
    if termlogin == playername.lower() and termpass == "freedom":
        #show text "ID: [termlogin] - Password: [termpass]" at termtextpos2
        #m "Now i'm in!"
        $ term_login_done= True
        jump server_start
    
    else:
        $ showtext = """
    Terminal
    [ascii_line]
    
    Login Error! Try again.
    """
        show text Text(showtext,text_align=termtext_align) at termtextpos
        call sound_electroshock from _call_sound_electroshock_27
        with hpunch
        pause 2
        $ termtext = "help"
    
    jump terminal






    




# locate(planet)
label terminal_locate(i):
    
    $ planet2 = planet
    $ planet = i
    
    call planet_info from _call_planet_info_1
    
    $ showtext = """
    Locate
    [ascii_line]
    
    [i] - Object found in universe!
    
    DATA:

    Name: [planet_name]
    Type: [planet_type]
    Size: [planet_size]
    Moon(s): [planet_moons]
    Atmosphere: [planet_atmosphere]
    Temperature: [planet_temperature]
    Radiations: [planet_radiations]
    Habitable: [planet_habitable]
    Inhabited: [planet_inhabited]
    Auth. needed: [planet_auth_needed]
    Required ship: [planet_required_ship]
    """
    

    show text Text(showtext,text_align=termtext_align) at termtextpos
    call sound_beep from _call_sound_beep_33
    

    menu:
        "Add '[planet]' to cockpit map" if space_terminal == True and planet not in planetlist:
            pass
        
        "Exit":
            $ termtext = "help"
            $ planet = planet2
            jump terminal

    $ planet = planet2
    
    #call server_progressbar
    
    call sound_connected from _call_sound_connected_25
    with flash
    
    # planet list
    if i not in planetlist:
        $ planetlist.append(i)

    $ showtext = """
    Locate
    [ascii_line]
    
    Success!
    
    The coordinates of '[i]'
    are copied to your cockpit map.
    """
    show text Text(showtext,text_align=termtext_align) at termtextpos
    
    call sound_connected from _call_sound_connected_26
    #pause 3
    $ termtext = "help"
    
        
    if superdev == True:
        "[planetlist]"
        
        
    
    # delete notes
    if i == "isc":
        call remove_note(note_locate_isc) from _call_remove_note_1
    
    if i == "asteroids":
        call remove_note(note_locate_asteroids) from _call_remove_note_2
        
    if i == "cargo":
        call remove_note(note_locate_cargo) from _call_remove_note_3
    
    
    
    menu:
        "Go to cockpit":
            #scene bgcolor
            #call show_space
            #jump cockpit_map
            jump cockpit
        
        "Exit":
            pass
    
    return



