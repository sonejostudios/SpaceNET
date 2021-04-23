init:
    $ takeoftospace = False
    
    # multiplicator for stars amount. 0 for none, 1 (min) to 4.
    # this as to set at compile time
    $ starsamount = 2
    
    #stars flight R2L
    image starssmall r2l= SnowBlossom("images/starsmall.png", count=starsamount*50, border=50, xspeed=(-1, -10), yspeed=(0, 0), start=0, fast=True, horizontal=True)
    image starsmid r2l= SnowBlossom("images/star.png", count=starsamount*25, border=50, xspeed=(-10, -50), yspeed=(0, 0), start=0, fast=True, horizontal=True)
    image starsbig r2l= SnowBlossom("images/starbig.png", count=starsamount*6, border=50, xspeed=(-50, -200), yspeed=(0, 0), start=0, fast=True, horizontal=True)


    #stars flight L2R
    image starssmall l2r= SnowBlossom("images/starsmall.png", count=starsamount*50, border=50, xspeed=(1, 10), yspeed=(0, 0), start=0, fast=True, horizontal=True)
    image starsmid l2r= SnowBlossom("images/star.png", count=starsamount*25, border=50, xspeed=(10, 50), yspeed=(0, 0), start=0, fast=True, horizontal=True)
    image starsbig l2r= SnowBlossom("images/starbig.png", count=starsamount*6, border=50, xspeed=(50, 200), yspeed=(0, 0), start=0, fast=True, horizontal=True)


    #orbit
    image starssmall orbit = SnowBlossom("images/starsmall.png", count=starsamount*50, border=50, xspeed=(10, 50), yspeed=(0, 0), start=0, fast=True, horizontal=True)
    image starsmid orbit = SnowBlossom("images/star.png", count=starsamount*25, border=50, xspeed=(50, -50), yspeed=(0, 0), start=0, fast=True, horizontal=True)
    image starsbig orbit = SnowBlossom("images/starbig.png", count=starsamount*6, border=50, xspeed=(-50, -300), yspeed=(0, 0), start=0, fast=True, horizontal=True)

    #up2down
    image starssmall u2d = SnowBlossom("images/starsmall.png", count=starsamount*50, border=50, xspeed=(0, 0), yspeed=(1, 10), start=0, fast=True, horizontal=False)
    image starsmid u2d = SnowBlossom("images/star.png", count=starsamount*25, border=50, xspeed=(0, 0), yspeed=(10, 50), start=0, fast=True, horizontal=False)
    image starsbig u2d = SnowBlossom("images/starbig.png", count=starsamount*6, border=50, xspeed=(0, 0), yspeed=(50, 200), start=0, fast=True, horizontal=False)

    #down2up
    image starssmall d2u = SnowBlossom("images/starsmall.png", count=starsamount*50, border=50, xspeed=(0, 0), yspeed=(-1, -10), start=0, fast=True, horizontal=False)
    image starsmid d2u = SnowBlossom("images/star.png", count=starsamount*25, border=50, xspeed=(0, 0), yspeed=(-10, -50), start=0, fast=True, horizontal=False)
    image starsbig d2u = SnowBlossom("images/starbig.png", count=starsamount*6, border=50, xspeed=(0, 0), yspeed=(-50, -200), start=0, fast=True, horizontal=False)

    #nomove
    image starssmall nomove = SnowBlossom("images/starsmall.png", count=starsamount*50, border=50, xspeed=(0), yspeed=(0), start=0, fast=True, horizontal=True)
    image starsmid nomove = SnowBlossom("images/star.png", count=starsamount*25, border=50, xspeed=(0), yspeed=(0), start=0, fast=True, horizontal=True)
    image starsbig nomove = SnowBlossom("images/starbig.png", count=starsamount*6, border=50, xspeed=(0), yspeed=(0), start=0, fast=True, horizontal=True)



    #R2L Hyperspace
    image starssmall hsr2l= SnowBlossom("images/hssmall.png", count=starsamount*50, border=50, xspeed=(-10, -100), yspeed=(0, 0), start=0, fast=True, horizontal=True)
    image starsmid hsr2l= SnowBlossom("images/hsmid.png", count=starsamount*25, border=50, xspeed=(-100, -500), yspeed=(0, 0), start=0, fast=True, horizontal=True)
    image starsbig hsr2l= SnowBlossom("images/hsbig.png", count=starsamount*6, border=50, xspeed=(-500, -1000), yspeed=(0, 0), start=0, fast=True, horizontal=True)

    #L2R Hyperspace
    image starssmall hsl2r= SnowBlossom("images/hssmall.png", count=starsamount*50, border=50, xspeed=(00, 100), yspeed=(0, 0), start=0, fast=True, horizontal=True)
    image starsmid hsl2r= SnowBlossom("images/hsmid.png", count=starsamount*25, border=50, xspeed=(100, 500), yspeed=(0, 0), start=0, fast=True, horizontal=True)
    image starsbig hsl2r= SnowBlossom("images/hsbig.png", count=starsamount*6, border=50, xspeed=(500, 1000), yspeed=(0, 0), start=0, fast=True, horizontal=True)

    #U2D Hyperspace
    image starssmall hsu2d= SnowBlossom("images/hs2small.png", count=starsamount*50, border=50, xspeed=(0, 0), yspeed=(00, 100), start=0, fast=True, horizontal=False)
    image starsmid hsu2d= SnowBlossom("images/hs2mid.png", count=starsamount*25, border=50, xspeed=(0, 0), yspeed=(100, 500), start=0, fast=True, horizontal=False)
    image starsbig hsu2d= SnowBlossom("images/hs2big.png", count=starsamount*6, border=50, xspeed=(0, 0), yspeed=(500, 1000), start=0, fast=True, horizontal=False)

    #D2U Hyperspace
    image starssmall hsd2u= SnowBlossom("images/hs2small.png", count=starsamount*50, border=50, xspeed=(0, 0), yspeed=(-10, -100), start=0, fast=True, horizontal=False)
    image starsmid hsd2u= SnowBlossom("images/hs2mid.png", count=starsamount*25, border=50, xspeed=(0, 0), yspeed=(-100, -500), start=0, fast=True, horizontal=False)
    image starsbig hsd2u= SnowBlossom("images/hs2big.png", count=starsamount*6, border=50, xspeed=(0, 0), yspeed=(-500, -1000), start=0, fast=True, horizontal=False)


    $ game_percents = 0
    


# surface to spaceport
label takeoff_anim(x):
    
    #$ spaceship_broken = True 
    
    # spaceship repair (asteroids)
    if spaceshiptype == "4b" and inventory_select == "screwdriver":
        m "Let's try to repair the wing. {w=3} {nw}"
        call use_and_keep_item from _call_use_and_keep_item_40
        call sound_screw from _call_sound_screw_13
        pause 3
        call sound_connected from _call_sound_connected_30
        
        $ spaceshiptype = "4"
        with flash

        $ landing = False
        $ pnc_nodes_visible = True
        
        m "Yes, it worked! {w=2} {nw}"
        if spaceship_broken == True:
            m "But I still need to replace the hyperspace module. {w=4} {nw}"
        
        return
        
        
    if spaceship_broken == True and inventory_select == "module":
        m "Let's try to replace the hyperspace module. {w=3} {nw}"
        call use_item from _call_use_item_10
        call sound_screw from _call_sound_screw_14
        pause 3
        call sound_connected from _call_sound_connected_31
        
        hide smoking1
        hide smoking2
        hide smoking3
        
        $ spaceship_broken = False
        with flash

        $ landing = False
        $ pnc_nodes_visible = True
        
        m "Yes, it worked! {w=2} {nw}"
        
        return
    
    
    
    # take off menu + anim
    $ pnc_nodes_visible = False
    
    $ inventory_select = ""
    call sound_door from _call_sound_door_179
    call hidepaths from _call_hidepaths
    hide player

    if x != "nomenu":
        menu:
            "Take off to space":
                $ takeoftospace = True
                $ ingame = False
                $ isc_spaceship_interchange = False
                pass
                
            "Take off to surface":
                $ isc_spaceship_interchange = False
                pass
                
            "Exit":
                $ landing = False
                call sound_door from _call_sound_door_82
                $ pnc_nodes_visible = True
                return
    
    #pause 1
    if spaceship_broken == True:
        hide smoking1
        hide smoking2
        hide smoking3
        with dissolve
    
    show spaceship:
        pos (250, 240)
        easeout 4 pos (-300, 240) zoom 2.0 rotate direction
        
    if shadow_enable == 1:
        show shadow:
            pos (250, 240)
            easeout 4 pos (-300, 240)
            
    
    call sound_take_off from _call_sound_take_off_2
    pause 4
    
    show spaceship:
        rotate 0
        zoom 1.0
    
    $ landing = True
    
    return


    

# landing to ground
label landing_anim:
    $ pnc_nodes_visible = True
    
        
    if landing == False:
        show spaceship:
            pos (250, 240)
            zoom 0.75
            

    else:
        
        hide smoking1
        hide smoking2
        hide smoking3
    
        show spaceship:
            rotate direction
            zoom 2.0
            pos (-300, 240)
            easein 4 pos (250, 240) zoom 0.75  rotate 0
            
        if shadow_enable == 1:
            show shadow:
                pos (-300, 240)
                easein 4 pos (250, 240)
        call sound_take_off from _call_sound_take_off_3
        
        pause 4

        # force final pos if pause is skipped
        show spaceship:
            pos (250, 240)
            zoom 0.75
            rotate 0
        
        call sound_door from _call_sound_door_83
        
        # show inventory button
        $ inventory_button = True
        
    
    # smoking
    if spaceship_broken == True:
        show smoking1:
            pos (250,240)
        show smoking2:
            pos (250,240)
        show smoking3:
            pos (250,240)
    
    return



# surface to space transition animation
label takeoff_tospace_anime:
    $ pnc_nodes_visible = False
    
    if spaceship_broken == True:
        hide smoking1
        hide smoking2
        hide smoking3
        with dissolve
    
    show spaceship:
        pos (0.5, 0.5)
        easeout 3 pos (0.5, -0.5) zoom 2.0 rotate 90
        
    if shadow_enable == 1:
        show shadow:
            pos (0.5, 0.5)
            easeout 3 pos (0.5, -0.5)
    
    call sound_take_off from _call_sound_take_off_4
    pause 3
    
    $ space_anim = True
    $ takeoftospace = False
    

    jump space


# from space to surface
label landing_fromspace_anim:
    $ pnc_nodes_visible = False
    
    show spaceship:
        rotate 90
        zoom 2.0
        pos (0.5, -0.5)
        easein 3 pos (0.5, 0.5) zoom 0.5  rotate 0
    
    if shadow_enable == 1:
        show shadow:
            pos (0.5, -0.5)
            easein 3 pos (0.5, 0.5)
    
    $ direction = 0
    #call sound_take_off
    pause 3
    
    $ space_anim = False
    
    return


# space to surface called from space label
label takeoff_space_anim:
    $ pnc_nodes_visible = False
    
    #call sound_take_off
    
    show spaceshipside:
        pos (0.5, 1.5)
        easein 2 pos (0.5, 0.5)
        
    if shadow_enable == 1:
        show shadow:
            pos (0.5, 1.5)
            easein 2 pos (0.5, 0.5)
        
    pause 2
    
    $ space_anim = False
    
    return
    


# in space go down to surface
label landing_space_anim:
    
    call sound_take_off from _call_sound_take_off_5
    
    if spaceship_broken == True:
        hide smoking1
        hide smoking2
        hide smoking3
        with dissolve
    
    show spaceshipside:
        pos (0.5, 0.5)
        easeout 2 pos (0.5, 1.5)
        
    if shadow_enable == 1:
        show shadow:
            pos (0.5, 0.5)
            easeout 2 pos (0.5, 1.5)
        
    pause 2
    
    $ space_anim = True
    
    return
    
    


label hyperspace_anim:
    $ pnc_nodes_visible = False
    
    $ inventory_select = ""
    
    call sound_hyperspace from _call_sound_hyperspace_5
    
    hide screen cockpit_map_screen
    hide screen mini_planets
    
    show screen notify("Hyperspace")
    
    scene bgcolor
    
    if galaxy_enable == 1:
        show galaxy

    # stars
    show starssmall hsr2l behind ship
    show starsmid hsr2l behind ship
    show starsbig hsr2l behind ship
    
    # show spaceship with transform
    show spaceshipside at inspace_idle
        
    if shadow_enable == 1:
        show shadow at truecenter
    with flash
    
    pause 3
    
    $ in_hyperspace = True
    
    return
    
    


# alarm
label alarm_check:
    if alarm_on == True:
        if renpy.music.is_playing(channel='alarm_channel') == False:
            call sound_alarm from _call_sound_alarm
        
        if renpy.showing("white") != True:
            show white zorder 999:
                alpha 0.5
                linear 1 alpha 0
                linear 1 alpha 0.5
                repeat
    else:
        stop alarm_channel
        hide white
        
    return






# info panel
label info_panel:
    $ pnc_nodes_visible = False
    
    if inventory_select != "":
        call dialog_nosense from _call_dialog_nosense_9
        $ pnc_nodes_visible = True
        return
    
    show bgcolor as bg2
    show infopanel
    
    # screws
    show screw:
        pos (60,60)
        rotate renpy.random.randint(0, 360)
    show screw as screw2:
        pos (740,60)
        rotate renpy.random.randint(0, 360)
    show screw as screw3:
        pos (60,420)
        rotate renpy.random.randint(0, 360)
    show screw as screw4:
        pos (740,420)
        rotate renpy.random.randint(0, 360)
        
    
    
    image symlaser:
        "images/symbols/symlaser.png"
        anchor (0.5,0.5)
        
    image symbiohazard:
        "images/symbols/symbiohazard.png"
        anchor (0.5,0.5)
        
    image symatom:
        "images/symbols/symatom.png"
        anchor (0.5,0.5)
        
    image symdanger:
        "images/symbols/symdanger.png"
        anchor (0.5,0.5)
        
    image symexit:
        "images/symbols/symexit.png"
        anchor (0.5,0.5)
        
    image symquake:
        "images/symbols/symquake.png"
        anchor (0.5,0.5)
        
    image symnoentry:
        "images/symbols/symnoentry.png"
        anchor (0.5,0.5)
    
    
    
    
    # symbols    
    if info_panel_symbol == "laser":
        show symlaser:
            ypos 0.3
            xpos 0.5
            
    if info_panel_symbol == "biohazard":
        show symbiohazard: 
            ypos 0.3
            xpos 0.5
            
    if info_panel_symbol == "atom":
        show symatom: 
            ypos 0.3
            xpos 0.5
            
    if info_panel_symbol == "exit":
        show symexit: 
            ypos 0.3
            xpos 0.5
            
    if info_panel_symbol == "danger":
        show symdanger: 
            ypos 0.3
            xpos 0.5
            
    if info_panel_symbol == "quake":
        show symquake:
            ypos 0.25
            #xpos 0.5
            xalign 0.5
            
    if info_panel_symbol == "noentry":
        show symnoentry: 
            ypos 0.3
            xpos 0.5  
            
    if info_panel_symbol == "node":
        show node2 as sysnode: 
            ypos 0.17
            xpos 0.5
            anchor (0.5, 0.5)
            
                   
        
    #shadow
    if shadow_enable == 1:
        show shadow:
            pos (0.5,0.5)
    else:
        hide shadow

    show text showtext:
        pos (0.5,0.5)
        #alpha 1
        #pause 1
        #alpha 0.5
        #pause 0.2
        #repeat
    
    $ inventory_select = ""
    
    pause
    


#label info_panel_hide:

    # hide
    hide bg2
    hide infopanel
    hide text showtext
    
    hide screw
    hide screw2
    hide screw3
    hide screw4
    
    hide symlaser
    hide symbiohazard
    hide symatom
    hide symexit
    hide symdanger
    hide symquake
    hide symnoentry
    hide sysnode
    
    $ info_panel_symbol = ""
    $ showtext = ""
    
    $ pnc_nodes_visible = True
    
    return
    







# GAME END
    
label game_end_anim:
    $ pnc_nodes_visible = False
    
    call music_outro from _call_music_outro_2

    call show_space from _call_show_space_6
    
    hide screen buttons
    hide screen notify

    if space_anim == True:
        call takeoff_space_anim from _call_takeoff_space_anim_1
    
    # show spaceship with transform
    show spaceshipside at inspace_idle
        
    if shadow_enable == 1:
        show shadow at truecenter
    #m "Yeah!{w=2}{nw}"
    show spaceshipside:
        pos (400,240)
        linear 10 zoom 0 pos (700, 240)
        
    pause 10
    #"YOU WON THE GAME!"
    call end_background from _call_end_background_1
    
    jump end_finished
  
  
  
  
  
    
    
label end_background:
    $ pnc_nodes_visible = False
    
    show screen termfx

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
        
    
    return
        



label end_finished:
    $ pnc_nodes_visible = False
        
    # SpaceNET
    
    #set percents - gems
    $ game_percents = 100 - maxgems + gems
 
    
    with dissolve

    #call music_bar_village
    
    call sound_hyperspace from _call_sound_hyperspace_6
    
    show spacenet_logo
    
    show text "{color=#8dd35f}[game_percents]% finished":
        pos (400,360)
        alpha 0.5
        
    
    with Dissolve(2)
    
    pause
    
    #hide spacenet_logo
    #with Dissolve(2)
    
    hide spacenet_logo
    hide text
    with Dissolve(2)

    jump credits
        
    
    
label end_demo:
    call sound_scan from _call_sound_scan_9
    call show_space from _call_show_space_23
    with flash
    centered "{color=#8dd35f}End of the demo.\n\nBut you still have to save the universe!{/color}"
    hide screen buttons
    jump credits
    
    
    

