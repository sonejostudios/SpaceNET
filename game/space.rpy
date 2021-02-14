# space

init:
    $ planetxy_auth = False
    $ planetxy_register = False
    
    $ planetxy_first = False
    
    $ planetxy_scan = False
    
    $ hacker_space_meeting_done = False
    
    $ space_terminal = False


init:    
    image galaxy: 
        "images/galaxy.png"
        alpha 0.1
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        #linear 240 pos (-0.7, 0.5)
    
    image orbitmeter:
        transform_anchor True
        "images/orbitmeter.png"
        anchor (24,26)
        pos (50,110)
        #pos (50,430)
        linear 10 rotate 360.0
        rotate 0
        repeat
        
    image spacemenu = "images/spacemenu.png"
        
    
    transform inspace_idle:
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        linear 1 pos (0.5, 0.49)
        linear 1 pos (0.5, 0.5)
        repeat
        

    $ space_anim = True




# main space label
label space:
    $ pnc_nodes_visible = False
    
    $ space_terminal = True
    
    
    # dev only
    if superdev == True:
        show screen _performance
    else:
        hide screen _performance


    #stop music
    stop atmo
    
    #call atmo_spaceship
    #
    
    call music_space from _call_music_space
    
    
    hide screen cockpit_screen
    
    # stop alarm
    $ alarm_on = False
    call alarm_check from _call_alarm_check_5

    
    
    
    # hide inventory button
    $ inventory_button = True
        
    show screen superdev

    
    call show_space from _call_show_space_2
    
    $ inventory_select = ""
    
    

    
    
    if space_anim == True:
        call takeoff_space_anim from _call_takeoff_space_anim
    
    
    # show spaceship with transform
    show spaceshipside at inspace_idle
        
    if shadow_enable == 1:
        show shadow at truecenter
    
    
    # coming from hyperspace
    if in_hyperspace == True:
        with Dissolve(2.0)
        $ in_hyperspace = False
        
        
    # come back from cargo explosion, pixellate
    if cargo_exploded == 1:
        $ cargo_exploded = 2
        with pixellate
        
        
    # planets conditions
    if planet != "none":
        show orbitmeter:
            alpha 0
            linear 1 alpha 1
        
        show text "{color=#8dd35f}[planet]" as text_planet:
            pos (50,150)
            alpha 0.5
            linear 1 pos (50,148)
            linear 1 pos (50,150)
            repeat 
        
        if planet == "sun":
            show screen notify("in orbit of the [planet]")
        else:
            show screen notify("in orbit of [planet]")
        
    
    if planet == "none" or planet == "hacker":
        hide orbitmeter
        hide text_planet
        show screen notify("free in space")
        
    if planet == "hacker":
        call hacker_meeting from _call_hacker_meeting
        $ planet = "none"

        
    jump space_loop


# show space background with background color, galaxy and stars
label show_space:

    
    $ inventory_select = ""
        
    scene bgcolor
    
    if galaxy_enable == 1:
        show galaxy

    # stars
    show starssmall r2l behind ship
    show starsmid r2l behind ship
    show starsbig r2l behind ship
    

    return



#space loop
label space_loop:
    
    $ inventory_select = ""

    #wait for action
    pause
    
    
    #show screen spacemenu
    #with irisout
    
    # open space menu with transform
    call sound_scan from _call_sound_scan_2
    show spacemenu at inspace_idle with irisout
    
    #wait for action
    pause
    $ clickpos = mousepos
    
    # close space menu
    call sound_scan from _call_sound_scan_3
    hide spacemenu with irisin
    
    
    #space menu
    
    # cockpit
    #if (570,80) < mousepos < (640,140) : # this doesn't work properly!
    if 570 < clickpos[0] < 640 and 80 < clickpos[1] < 140:
        #m "the cockpit is not implemented yet!"
        jump cockpit
    
    
    # landing
    if 570 < clickpos[0] < 640 and 330 < clickpos[1] < 400:
        
        $ space_terminal = False
        
        jump land_to_planet
        
    
    # terminal
    if 165 < clickpos[0] < 230 and 80 < clickpos[1] < 140:
        
        #$ space_terminal = True
        
        call terminal from _call_terminal_2
        jump space
        
    
    
    # orbital view
    if 165 < clickpos[0] < 230 and 330 < clickpos[1] < 390:
        jump orbital_view
    

    jump space_loop 
    
    return
    
    
label land_to_planet:
    
    $ pnc_nodes_visible = False
    
    if planet == "none" or planet == "hacker":
        with hpunch
        call sound_beep from _call_sound_beep_3
        m "I'm free in space, there is nothing for landing!"
        jump space_loop
    
    if planet == "megaship":
        call landing_space_anim from _call_landing_space_anim
        
        $ startpos = 22
        jump megaship_landing
        
    
    # the future idea is to land every time randomly on the surface
    if planet == "xylo":
        if planetxy_auth == True:
            call landing_space_anim from _call_landing_space_anim_1
            $ landing = True
            
            if planetxy_first == False:
                $ startpos = 44
                $ shippos = (400,0)
                jump xylo_spaceport
            else:
                jump surface_xylo
                
        else:
            call sound_beep from _call_sound_beep_4
            with hpunch
            radio "Landing autorization denied. {w=2.5} {nw}"
            jump space_loop
            
    
    #if planet == "demo":
    #    call landing_space_anim
    #    $ landing = True
    #    jump surface1
    
        
    if planet == "io11":
        call landing_space_anim from _call_landing_space_anim_2
        
        jump docking
        #$ startpos = 1
        #jump satellite_io11
        
    if planet == "cargo" and cargo_exploded == 0:
        call landing_space_anim from _call_landing_space_anim_3
        $ landing = True
        jump surface_cargo
        

        
    if planet == "isc":
        call landing_space_anim from _call_landing_space_anim_4
        $ landing = True
        jump surface_isc
        
    
    if planet == "sun":
        #call landing_space_anim
        #$ landing = True
        call sound_beep from _call_sound_beep_5
        with hpunch
        m "No way I will land on the sun! {w=3.0}{nw}"
        jump space_loop
        


# orbital view    
label orbital_view:
    
    $ inventory_select = ""
    
    #$ inventory_button = False
    
    image orbitfocus = "images/orbitfocus.png"
    image xylo_small = "images/planets/xylo_small.png"
    
    image megaspaceship_small = "images/planets/megaspaceship_small.png"
    image cargo_small = "images/planets/cargo_small.png"
    image isc_small = "images/planets/isc_small.png"

    image sunbig = "images/planets/sunbig.png"
    
    
    show screen notify("orbital view")
    
    scene bgcolor
    
    if galaxy_enable == 1:
        show galaxy

    # stars
    show starssmall orbit behind ship
    show starsmid orbit behind ship
    show starsbig orbit behind ship
    
    if shadow_enable == 1:
        show shadow at truecenter
    
    
    # planet pics
    if planet == "none" or planet == "hacker":
        show text "{color=#8dd35f}Not in orbit" at truecenter:
    
    if planet == "megaship":
        show megaspaceship_small at truecenter, inspace_idle:
    
    if planet == "xylo":
        show xylo_small at truecenter, inspace_idle
            #rotate -25
        
    if planet == "demo":
        show xylo_small at truecenter, inspace_idle
        
    if planet == "io11":
        show satellite at truecenter, inspace_idle:
            zoom 0.2
            
    if planet == "cargo":
        show cargo_small at truecenter, inspace_idle
        
    if planet == "isc":
        show isc_small at truecenter, inspace_idle
        
    if planet == "sun":
        show sunbig at truecenter, inspace_idle:
            zoom 0.35
    
    
    pause 0.1
    show orbitfocus at truecenter, inspace_idle #with wipedown
    
    
    #$ planet = "none"
    
    call planet_info from _call_planet_info
    
    show screen planet_info 
    with wipedown
    #with flash
    
    
    
    menu:

        "map" if planet != "none":
            call sound_beep from _call_sound_beep_6
            jump map_view
            
        "ask for landing authorization" if planet_auth_needed == "Yes" and planetxy_auth == False:
            call sound_modem from _call_sound_modem
            radio "Authorisation request.{w=1.0}.{w=1.0}.{w=1.0}.{w=1.0}.{w=1.0} {nw}"
            call sound_connected from _call_sound_connected_7
            radio "Authorisation granted! {w=2.0} {nw}"
            
            
            if planet == "xylo":
                
                radio "Please register your ship at Xylo Village. {w=3.0} {nw}"
                m "Hmm... I think I should go there first. {w=2.0} Let's go! {w=1.0} {nw}"
                
                $ planetxy_auth = True
                $ planetxy_register = False

            jump orbital_view
            
            
        "measure direct radiation" if spaceshiptype == "3" and planet == "sun":
            call sound_scan from _call_sound_scan_8
            with flash
            radio "Measured direct radiation: 6272 W/m^2{w=3.0} {nw}"
        
            call add_note("Direct radiation of the sun: 6272 W/m^2") from _call_add_note_13
            $ isc_sysadmin_sun = 2
        
        
        "exit":
            
            hide screen planet_info
            call sound_beep from _call_sound_beep_7
            jump space
            
    
    
    jump orbital_view
    





# view map in orbit view    
label map_view:
    
    $ inventory_select = ""
    
    image mapgrid:
        "images/mapgrid.png"
        alpha 0.2
    
    hide screen planet_info
    hide satellite
    hide orbitfocus
    hide megaspaceship_small
    hide cargo_small
    hide isc_small
    hide sunbig
    hide xylo_small
    
    if planet == "megaship":
        show megaspaceship:
            zoom 0.18
            align (0.5,0.5)
            alpha 0.5

    if planet == "xylo":
        show surface:
            zoom 0.24
            align (0.5,0.5)
            alpha 0.5
            
    if planet == "demo":
        show surface:
            zoom 0.24
            align (0.5,0.5)
            alpha 0.5
                
    if planet == "io11":
        show satellite_io11:
            zoom 0.8
            align (0.5,0.5)
            alpha 0.5
                
    if planet == "cargo":
        show surface:
            zoom 0.3
            align (0.5,0.5)
            alpha 0.5
    
    if planet == "isc":
        show surface:
            zoom 0.22
            align (0.5,0.5)
            alpha 0.5
            
    if planet == "sun":
        show sunbig:
            anchor (0.5,0.5)
            pos (0.5,0.5)
            alpha 0.8



    show mapgrid
    
    pause 
    
    jump orbital_view
    
    
    


  
