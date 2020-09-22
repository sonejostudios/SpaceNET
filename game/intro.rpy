# intro


init:    
    image galaxy: 
        "images/galaxy.png"
        alpha 0.1
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        #linear 240 pos (-0.7, 0.5)
        
        
    image megaspaceship:
        "images/spaceship/megaspaceship.png"
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        
    image spacenet_logo:
        "images/spacenet_logo.png"
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
    

    
    transform inspace_idle:
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        linear 1 pos (0.5, 0.49)
        linear 1 pos (0.5, 0.5)
        repeat
        

# start intro
label intro:
    $ pnc_nodes_visible = False
    
    $ superdev = False
    
    $ planet = "megaship"
    
    $ planetlist = ["megaship", "xylo"]
    
    $ planet1_auth = True
    $ ingame = False
    $ landing = True
    $ space_anim = False
    
    $ inventory = []
    
    $ coins = 0
    
    
    if pnc_cursor == True:
        $ change_cursor(type="default")
    
    jump intro_logo


#logo
label intro_logo:
    
    #sound
    #call sound_hyperspace
    call sound_title from _call_sound_title
    
    stop music fadeout 1.0
    
    #atmo
    #call atmo_spaceship
    
    
    $ renpy.music.play("sounds/spaceship.ogg", channel="atmo", fadein=5, fadeout=0, tight=True, if_changed=True)


    
    scene bgcolor
    with pixellate
    
    show screen termfx
    
    if galaxy_enable == 1:
        show galaxy
    
    if shadow_enable == 1:
        show shadow at truecenter zorder 1000

# stars
    #show starssmall u2d
    #show starsmid u2d
    #show starsbig u2d
    
    call end_background from _call_end_background_2
    
    window hide
    with Dissolve(2)
    


    show spacenet_logo
    with Dissolve(2)
    
    pause 4
    
    hide spacenet_logo
    with Dissolve(2)
    
    #call atmo_spaceship
    #call sound_beep
    
    # ask for player name
    python:
        playername = renpy.input(_("Enter your name:"))
        playername = playername.strip()
        if not playername:
            playername = "noname"

    
    jump intro1



# intro1
label intro1:
    
    call music_intro from _call_music_intro_1
    
    scene bgcolor
    with Dissolve(2)


    
    
    
    show screen notify("Somewhere in space")

    show screen termfx
    
    show screen setpos
    #show screen buttons
    show screen superdev
    show screen selected_item
    
    if galaxy_enable == 1:
        show galaxy

    # stars
    show starssmall r2l
    show starsmid r2l
    show starsbig r2l
    
    
    # show spaceship with transform
    show spaceshipside at inspace_idle
        
    if shadow_enable == 1:
        show shadow at truecenter zorder 1000
    
    
    with Dissolve(2)
    
    
    #wait for action
    pause 2
    
    #"[playername]"
    
    window hide
    
    
    show spaceshipside at inspace_idle:
        ease 3 rotate -10 pos (0.5,0.45)
        ease 3 rotate 10 pos (0.5,0.5)
        repeat
        
    pause 2
        
    m "That's strange...{w=2.0} {nw}"
    m "I can't move the spaceship anymore...{w=2.0} {nw}"
    
    
    
    jump intro2
    
    
    
    
label intro2: 
    
    
    show megaspaceship:
        zoom 1
        pos (-1400,-200)
        ease 10 pos (-900,-100)
        
    pause 10

    show megaspaceship:
        ease 10 zoom 0.18 pos (400,200)
        
    show spaceshipside at inspace_idle:
        ease 10 zoom 0.18 pos (0.79,0.55) rotate 0
        
    pause 12    
    
    jump intro3
    
    
label intro3: # spaceport

    
    show screen setpos
    #show screen buttons
    show screen superdev
    
    
    hide megaspaceship
    hide spaceshipside
    hide spaceship
    
    image megaship_spaceport = imagemapsdir + "megaship_spaceport.png"
    image megaship_spaceport2 = imagemapsdir + "megaship_spaceport2.png"
    image megaship_bigdoor = "/images/bigdoor.png"
    image spaceship_deco = "images/spaceship/spaceship2u.png"
    
    
    
    call atmo_spaceport from _call_atmo_spaceport_2
    
    
    show megaship_bigdoor:
        anchor (1.0,1.0)
        pos (800, 240)
        linear 2 pos (800, 240)
        linear 5 pos (800, 120)
    show megaship_bigdoor as megaship_bigdoor2:
        anchor (1.0,0.0)
        pos (800, 240)
        linear 2 pos (800, 240)
        linear 5 pos (800, 360)
        
    show megaship_spaceport
    
    show spaceship_deco:
        anchor (0.5,0.5)
        zoom 0.5
        pos (330, 88)
        rotate 180
    
    
    show light:
        pos (72,96)
    show light as light2:
        pos (72,386)
    show light as light3:
        pos (654,55)
    show light as light4:
        pos (654,424)
        
        
        
    call sound_crane_sound from _call_sound_crane_sound
    pause 7
    stop sound fadeout 1.0
    
    
    show spaceship:
        rotate 90
        zoom 0.5
        pos (800, 240)
        ease 10 pos (194,240)
        ease 3 rotate 0
        ease 4 pos (194,390)
        
    
    show megaship_spaceport2 zorder 900:
        align (1.0,0.5)
        
    pause 17
    
    # alarm
    $ alarm_on = True
    call alarm_check from _call_alarm_check_12
    
    show megaship_bigdoor:
        linear 5 pos (800, 240)
    show megaship_bigdoor as megaship_bigdoor2:
        linear 5 pos (800, 240)
        
    call sound_crane_sound from _call_sound_crane_sound_1
    pause 5
    stop sound fadeout 1.0
    
    
    
    
    window hide
    robotguard "You are under arrest! {w=3.5} {nw}"
    #pause 2
    
    $ alarm_on = False
    call alarm_check from _call_alarm_check_13

    jump intro4


label intro4:
    $ startpos = 1
    $ in_intro = True
    
    show screen buttons
    
    
    stop music fadeout 1.0
    
    stop atmo fadeout 1.0
    
    call sound_scan from _call_sound_scan_7
    
    jump megaship_cell



    
