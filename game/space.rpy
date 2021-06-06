# space

init:
    $ planetxy_auth = False
    $ planetxy_register = False
    
    $ planetxy_first = False
    
    $ planetxy_scan = False
    
    $ hacker_space_meeting_done = False
    
    $ space_terminal = False

 
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
        pos (54,110)
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
    
    $ spacemenu_text = ""
    $ spacemenu_visible = False



# show menu hover text if not touch screen
screen spacemenu_text():
    if not renpy.variant("touch") and inventory_visible == False:
        if spacemenu_visible == True:
            if 310 < mousepos[0] < 490 and 210 < mousepos[1] < 270:
                $ spacemenu_text = "Spaceship"
            
            
            elif 155 < mousepos[0] < 240 and 68 < mousepos[1] < 154:
                $ spacemenu_text = "Terminal"
                
            elif 557 < mousepos[0] < 642 and 68 < mousepos[1] < 154:
                $ spacemenu_text = "Cockpit"
                
            elif 155 < mousepos[0] < 240 and 320 < mousepos[1] < 408:
                $ spacemenu_text = "Orbital View"
                
            elif 557 < mousepos[0] < 642 and 320 < mousepos[1] < 408:
                if planet == "asteroids":
                    $ spacemenu_text = "Fly through the Asteroid Field"
                elif planet == "io11":
                    $ spacemenu_text = "Dock to the Satellite"
                elif planet == "sun":
                    $ spacemenu_text = "Try to land on the Sun"
                elif planet == "cargo":
                    $ spacemenu_text = "Fly to the Space Cargo"
                    
                elif planet == "megaship":
                    $ spacemenu_text = "Fly into the Megaship"
                
                elif planet == "isc":
                    $ spacemenu_text = "Fly to the Industrial Space City"
                    
                elif planet == "xylo":
                    $ spacemenu_text = "Land on Xylo"
                
                else:
                    $ spacemenu_text = "Fly to " + planet
                
            
            else:
                $ spacemenu_text = ""
                
        else:
            if 310 < mousepos[0] < 490 and 210 < mousepos[1] < 270:
                $ spacemenu_text = "Spaceship"
            else:
                $ spacemenu_text = ""
            
        text "{color=#8dd35f}[spacemenu_text]":
            anchor (0.5, 1.0)
            pos (400,472)
        



# main space label
label space:
    $ engine = "space"
    $ pnc_nodes_visible = False
    $ space_terminal = True
    
    
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
    
    
    if spaceship_broken == True:
        if renpy.showing("smoking1") != True:
            show smoking1:
                pos (400,220)
        if renpy.showing("smoking2") != True:
            show smoking2:
                pos (400,220)
        if renpy.showing("smoking3") != True:
            show smoking3:
                pos (400,220)
    
        
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
            pos (54,150)
            alpha 0.7
            linear 1 pos (54,148)
            linear 1 pos (54,150)
            repeat 
        
        if planet == "sun":
            show screen notify("In orbit of the sun")
            
        elif planet == "asteroids":
            show screen notify("Near the asteroid field")    
        
        else:
            show screen notify("In orbit of [planet]")
        
    
    if planet == "none" or planet == "hacker":
        hide orbitmeter
        hide text_planet
        show screen notify("Free in space")
        
    if planet == "hacker":
        call hacker_meeting from _call_hacker_meeting
        $ planet = "none"
        


    if planet == "asteroids":
        $ asteroidzoom = renpy.random.random()*0.9 + 0.1
        show asteroid_small behind orbitmeter, text_planet, spaceshipside:
            zoom asteroidzoom
            rotate 0
            ypos 100
            xpos 900
            linear 10 xpos -200 rotate -560
            repeat
            
        $ asteroidzoom2 = renpy.random.random()*0.9 + 0.1
        show asteroid_small as asteroid_small2 behind orbitmeter, text_planet, spaceshipside:
            zoom asteroidzoom2
            rotate 0
            ypos 350
            xpos 1200
            linear 13 xpos -200 rotate -460
            repeat
            
        

        
    jump space_loop






#space loop
label space_loop:
    
    show screen spacemenu_text
    
    $ inventory_select = ""

    #wait for action
    pause
    
    
    #show screen spacemenu
    #with irisout
    
    # open space menu with transform
    call sound_scan from _call_sound_scan_2
    show spacemenu at inspace_idle with irisout
    
    $ spacemenu_visible = True
    
    

    
    #wait for action
    pause
    $ clickpos = mousepos
    

    # close space menu
    call sound_scan from _call_sound_scan_3
    hide spacemenu with irisin
    
    
    hide screen spacemenu_text
    $ spacemenu_visible = False
    
    
    
    
    
    #space menu
    # terminal
    if 155 < clickpos[0] < 240 and 68 < clickpos[1] < 154:
        call terminal from _call_terminal_2
        jump space
    
    
    # cockpit
    if 557 < clickpos[0] < 642 and 68 < clickpos[1] < 154:
        jump cockpit
    
    
    # orbital view
    if 155 < clickpos[0] < 240 and 320 < clickpos[1] < 408:
        jump orbital_view
        
        
    # landing
    if 557 < clickpos[0] < 642 and 320 < clickpos[1] < 408:
        $ space_terminal = False
        jump land_to_planet
        
    

        
    

    

    jump space_loop 
    
    return
    


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




    
    
label land_to_planet:
    
    $ pnc_nodes_visible = False
    
    if planet == "none" or planet == "hacker":
        with hpunch
        call sound_beep from _call_sound_beep_3
        m "I'm free in space, there is nothing to land on!{w=3.5} {nw}"
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
                $ direction = 180
                jump xylo_spaceport
            else:
                jump surface_xylo
                
        else:
            call sound_beep from _call_sound_beep_4
            with hpunch
            radio "Landing authorization denied. {w=2.5} {nw}"
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
        m "Are you crazy?{w=2.0}{nw}"
        m "No way I will land on the sun! {w=3.0}{nw}"
        jump space_loop
        
        
    if planet == "asteroids":

        if spaceshiptype not in ["4", "4b"]:
            call sound_beep from _call_sound_beep_74
            with hpunch
            m "No way I will do it! {w=2.5}{nw}"
            m "My spaceship is way too slow... {w=3.0}{nw}"
            m "Entering an asteroid field with it is just too dangerous! {w=4.0}{nw}"
            m "I definitely need a faster spaceship if I want to fly through this asteroid field. {w=5.0}{nw}"
            jump space_loop
        
        else:
            if "pick" in inventory and "laser" in inventory:
                call landing_space_anim from _call_landing_space_anim_5
                $ landing = True

                if asteroid_collision == False:
                    jump asteroid_collision_anim
                else:
                    jump surface_asteroids
                
            else:    
                call sound_beep from _call_sound_beep_75
                with hpunch
                m "Right now, I really have better to do than shooting a sci-fi movie scene inside these asteroids! {w=6.0}{nw}"
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
    image asteroids_small = "images/planets/asteroids_small.png"

    image sunbig = "images/planets/sunbig.png"
    
    
    show screen notify("Orbital View")
    
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
            
    if planet == "asteroids":
        show asteroids_small at truecenter, inspace_idle
    
    
    pause 0.1
    show orbitfocus at truecenter, inspace_idle #with wipedown
    
    
    #$ planet = "none"
    
    call planet_info from _call_planet_info
    
    show screen planet_info 
    with wipedown
    #with flash
    
    
    
    menu:

        "Map" if planet != "none":
            call sound_beep from _call_sound_beep_6
            jump map_view
            
        "Ask for landing authorization" if planet_auth_needed == "Yes" and planetxy_auth == False:
            call sound_modem from _call_sound_modem
            radio "Authorization request.{w=1.0}.{w=1.0}.{w=1.0}.{w=1.0}.{w=1.0} {nw}"
            call sound_connected from _call_sound_connected_7
            radio "Authorization granted! {w=2.0} {nw}"
            
            
            if planet == "xylo":
                
                radio "Please register your ship at [xylo_village_name]. {w=3.5} {nw}"
                radio "It is the main settlement of the planet. {w=3} {nw}"
                m "Alright. I think I should go there first. {w=3} {nw}"
                m "Let's go! {w=2} {nw}"
                
                $ planetxy_auth = True
                $ planetxy_register = False

            jump orbital_view
            
            
        "Measure direct irradiation" if spaceshiptype == "3" and planet == "sun":
            call sound_scan from _call_sound_scan_8
            with flash
            radio "Measured direct irradiation: 6272 W/m^2{w=3.0} {nw}"
        
            call add_note("Direct irradiation of the sun: 6272 W/m^2") from _call_add_note_13
            $ isc_sysadmin_sun = 2
        
        
        "Exit":
            
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
    hide asteroids_small
    
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
            
            
    if planet == "asteroids":
        show surface:
            zoom 0.24
            align (0.5,0.5)
            alpha 0.5



    show mapgrid
    
    pause 
    
    jump orbital_view
    
    
    


  
