#cockpit

init:    
    $ target_active = False
    $ in_hyperspace = False
    $ space_distance = 5700
    $ space_velocity = 1750

    
    # planet positions
    $ megaship_pos = (180,200)
    $ xylo_pos = (200,320)
    $ demo_pos = (50,50)
    $ satellite_pos = (380,380)
    $ cargo_pos = (415, 300)
    $ isc_pos = (270, 72)
    $ hacker_pos = (400,200)
    $ sun_pos = (340, 260)
    
    
    
    # starting positions
    $ spaceship_pos = megaship_pos
    $ destination_pos = xylo_pos
    
    
    # input tolerence to planet pos
    $ flight_match = 20
    
    


# screen cockpit
screen cockpit_screen():
    timer 0.2 repeat True action [SetVariable("space_distance", space_distance+1)]
    timer 3 repeat True action [SetVariable("space_velocity", space_velocity+renpy.random.randint(-2, 2))]
    vbox:
        pos (30,380)
        text "{color=#8dd35f}DATA"
        null height 10
        #text "{color=#8dd35f}Position: [spaceship_pos]"
        text "{color=#8dd35f}Distance: [space_distance] km"
        text "{color=#8dd35f}Velocity: [space_velocity] km/h"


# screen cockpit map
screen cockpit_map_screen():
    vbox:
        pos (30,380)
        text "{color=#8dd35f}DATA"
        null height 10
        text "{color=#8dd35f}Position: [spaceship_pos]"
        text "{color=#8dd35f}Destination: [destination_pos]"
        



# screen map mini planets
screen mini_planets():
    if "megaship" in planetlist:
        add "images/planets/miniplanet.png" anchor (0.5,0.5) pos megaship_pos
        text "{color=#8dd35f}{size=12}  megaship" anchor (0,0.5) pos megaship_pos
    
    
    # if planet is known, then show it like this
    if "xylo" in planetlist:
        add "images/planets/miniplanet.png" anchor (0.5,0.5) pos xylo_pos
        text "{color=#8dd35f}{size=12}  xylo" anchor (0,0.5) pos xylo_pos
    
    # demo planet
    #add "images/planets/miniplanet.png" anchor (0.5,0.5) pos demo_pos
    #text "{color=#8dd35f}{size=12}  demo" anchor (0,0.5) pos demo_pos
    
    # satellite
    if "io11" in planetlist:
        add "images/planets/miniplanet.png" anchor (0.5,0.5) pos satellite_pos
        text "{color=#8dd35f}{size=12}  satellite io-11" anchor (0,0.5) pos satellite_pos
    
    # cargo
    if "cargo" in planetlist:
        add "images/planets/miniplanet.png" anchor (0.5,0.5) pos cargo_pos
        text "{color=#8dd35f}{size=12}  space cargo" anchor (0,0.5) pos cargo_pos
    
    # industrial space city
    if "isc" in planetlist:
        add "images/planets/miniplanet.png" anchor (0.5,0.5) pos isc_pos
        text "{color=#8dd35f}{size=12}  industrial space city" anchor (0,0.5) pos isc_pos
        
    # sun
    if "sun" in planetlist:
        add "images/planets/miniplanet.png" anchor (0.5,0.5) pos sun_pos
        text "{color=#8dd35f}{size=12}  sun" anchor (0,0.5) pos sun_pos




# cockpit
label cockpit:
    
    #$ space_terminal = True
    
    $ inventory_select = ""
    
    show screen notify("cockpit")
    
    scene bgcolor
    
    if galaxy_enable == 1:
        show galaxy:
            pause 1
            linear 400 rotate 360.0
            rotate 0
            repeat

    # stars
    show starssmall nomove:
        align (0.5,0.5)
        zoom 1.0
        alpha 0.0
        linear 1 zoom 1.05 alpha 1.0
        easeout 14 zoom 2.0 alpha 0.0
        repeat
        
        
    show starssmall nomove as stars2:
        align (0.5,0.5)
        alpha 0.0
        rotate 90 
        pause 4
        
        block:
            zoom 1.0
            alpha 0.0
            linear 2 zoom 1.1 alpha 1.0
            easeout 14 zoom 2.0 alpha 0.0
            repeat
        
        
    show starssmall nomove as stars3:
        align (0.5,0.5)
        alpha 0.0
        rotate 180   
        pause 8
        
        block:
            zoom 1.0
            alpha 0.0
            linear 2 zoom 1.1 alpha 1.0
            easeout 14 zoom 2.0 alpha 0.0
            repeat
    
    
    show starsmid nomove:
        align (0.5,0.5)
        alpha 0.0
        pause 1

        block:
            zoom 1.0
            alpha 0.0
            linear 2 zoom 1.1 alpha 1.0
            easeout 11 zoom 2.0 alpha 0.0
            repeat
    
    show starsbig nomove:
        align (0.5,0.5)
        alpha 0.0

        block:
            zoom 1.0
            alpha 0.0
            linear 1 zoom 1.05 alpha 1.0
            easeout 8 zoom 2.0 alpha 0.0
            repeat


    if shadow_enable == 1:
        show shadow at truecenter
    else:
        hide shadow
    
    show screen cockpit_screen
    
    jump cockpit_menu
    
    
#cockpit menu
label cockpit_menu:
    
    $ inventory_button = True
    
    #pause
    
    $ target_active = False
    
    show screen cockpit_screen
    hide screen cockpit_map_screen
    hide screen mini_planets
    
    #if planet != "none":
    #    show orbitmeter:
    #        alpha 0
    #        linear 1 alpha 1
    
    menu:
        "navigate":
            call sound_beep from _call_sound_beep_8
            jump cockpit_map
            
        "space view":
            call sound_beep from _call_sound_beep_9
            $ inventory_button = False
            hide orbitmeter
            pause
            call sound_beep from _call_sound_beep_10
            jump cockpit_menu
            
        "exit":
            call sound_beep from _call_sound_beep_11
            jump space
         
         
            
label cockpit2space:
    hide destx
    hide desty
    hide target
    hide mapgrid
    hide player
    jump cockpit_menu
    #call sound_beep
    #jump space
            
            

#cockpit map
label cockpit_map:
    
    #$ space_terminal = True
    
    
    # reset new satellite position
    if intercom_sat == True:
        $ satellite_pos = (350,150)
    
    
    image destx:
        "images/destx.png"
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        
    image desty:
        "images/desty.png"
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        
    image target:
        anchor (0.5,0.5)
        "target.png"
        


    
    hide orbitmeter
    
    #screen cockpit map
    show screen cockpit_map_screen
    
    show screen mini_planets
    
    hide screen cockpit_screen
    
    show mapgrid
    show player:
        pos spaceship_pos
    
    
    
    # show lines at spaceship position
    if target_active == False:
        show destx:
            ypos spaceship_pos[1]
        show desty:
            xpos spaceship_pos[0]
    
    
    
    #pause
    hide target
    
    $ destination_pos = mousepos
    
   
    # set new destination
    if target_active == True:
        
        call planet_match from _call_planet_match
        
        show destx:
            easein 1 ypos destination_pos[1]
        
        show desty:
            easein 1 xpos destination_pos[0]
            
        pause 1
        show target:
            pos destination_pos
            alpha 0.0
            linear 0.5 alpha 0.9
            
        
        # jump to menu after moving
        jump cockpit_map_menu
        
    
    $ target_active = True
    
    #pause 1
    $ destination_pos = spaceship_pos
    jump cockpit_map_menu
    #jump cockpit_map2
    
    

label cockpit_map2:  

    #wait for player input
    pause
    
    call sound_beep from _call_sound_beep_12
    
    # jump to menu if click on destination
    if (destination_pos[0]-20) < mousepos[0] < (destination_pos[0]+20) and (destination_pos[1]-20) < mousepos[1] < (destination_pos[1]+20):
        jump cockpit_map_menu
        

    jump cockpit_map
    



# go to planet position if matched
label planet_match:
    
    # megaship
    if megaship_pos[0]-flight_match < destination_pos[0] < megaship_pos[0]+flight_match and megaship_pos[1]-flight_match < destination_pos[1] < megaship_pos[1]+flight_match :
        $ destination_pos = megaship_pos
    
    # xylo
    if xylo_pos[0]-flight_match < destination_pos[0] < xylo_pos[0]+flight_match and xylo_pos[1]-flight_match < destination_pos[1] < xylo_pos[1]+flight_match :
        $ destination_pos = xylo_pos
        
    # sattelite io11
    if satellite_pos[0]-flight_match < destination_pos[0] < satellite_pos[0]+flight_match and satellite_pos[1]-flight_match < destination_pos[1] < satellite_pos[1]+flight_match :
        $ destination_pos = satellite_pos
    
    # cargo
    if cargo_pos[0]-flight_match < destination_pos[0] < cargo_pos[0]+flight_match and cargo_pos[1]-flight_match < destination_pos[1] < cargo_pos[1]+flight_match :
        $ destination_pos = cargo_pos

    # isc
    if isc_pos[0]-flight_match < destination_pos[0] < isc_pos[0]+flight_match and isc_pos[1]-flight_match < destination_pos[1] < isc_pos[1]+flight_match :
        $ destination_pos = isc_pos
    
    # hacker
    if hacker_pos[0]-flight_match < destination_pos[0] < hacker_pos[0]+flight_match and hacker_pos[1]-flight_match < destination_pos[1] < hacker_pos[1]+flight_match :
        $ destination_pos = hacker_pos
    
    # sun
    if sun_pos[0]-flight_match < destination_pos[0] < sun_pos[0]+flight_match and sun_pos[1]-flight_match < destination_pos[1] < sun_pos[1]+flight_match :
        $ destination_pos = sun_pos
        
        
    return





label cockpit_map_menu:
    #call planet_match

    menu:
        
        "fly to" if destination_pos != spaceship_pos:
            $ hacker_space_meeting_done = False
            call flight from _call_flight
            jump space
        
        "set destination":
            jump cockpit_map2

            
        "terminal":
            #$ space_terminal = True
            scene bgcolor
            hide screen mini_planets
            hide screen cockpit_map_screen
            call terminal from _call_terminal_3
            jump cockpit
            
        "exit":
            hide destx
            hide desty
            hide target
            hide mapgrid
            hide player

            
            call sound_beep from _call_sound_beep_13
            
            jump cockpit_menu
        
    
    jump cockpit_menu





#flight through hyperspace
label flight:
    
    # destination check and set planets
    if destination_pos == megaship_pos:
        $ planet = "megaship"
        
    elif destination_pos == xylo_pos:
        $ planet = "xylo"
    
    elif destination_pos == satellite_pos:
        $ planet = "io11"
        
    elif destination_pos == cargo_pos:
        $ planet = "cargo"
        
    elif destination_pos == isc_pos:
        $ planet = "isc"
        
    elif destination_pos == hacker_pos:
        $ planet = "hacker"

    elif destination_pos == sun_pos:
        $ planet = "sun"
    
    
    
    else:
        $ planet = "none"
        
    
    
    $ spaceship_pos = destination_pos
    
    call hyperspace_anim from _call_hyperspace_anim
    
    $ target_active = False
    
    
    # demo end
    if demo_version == True:
        if planet in ["hacker", "io11", "cargo", "isc"]:
            jump end_demo
    
    
    return
    



