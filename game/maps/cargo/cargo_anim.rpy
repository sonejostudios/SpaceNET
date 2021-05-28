# cargo anim

init:
    $ cargo_exploded = 0


image cargo_animbg = imagemapsdir + "cargo_animbg.png"
    

label cargo_anim_down:
    
    $ pnc_nodes_visible = False
    
    stop music fadeout 0.1
    call music_cargo from _call_music_cargo_4
    
    call atmo_spaceport from _call_atmo_spaceport_3
    
    
    # stop alarm
    $ alarm_on = False
    
    call show_space from _call_show_space_19
    
    show cargo_animbg
    
    #call sound_take_off
    
    
    show light:
        pos (102,120)
        
    show light as light2:
        pos (241,162)
        
    show light as light3:
        pos (580,65)
        
    show light as light4:
        pos (725,170)
        
        
    
    show spaceshipside:
        zoom 0.7
        pos (390, -50)
        linear 4 pos (400, 320) rotate 90
        linear 4 pos (430, 450) rotate 0
        linear 2 pos (430, 520)
        
    if shadow_enable == 1:
        show shadow:
            pos (400, 0)
            linear 10 pos (400, 480)

    
    pause 10
    #centered "cargo anim down"
    
    $ pnc_nodes_visible = True
    jump cargo_spaceport
    



label cargo_anim_up:
    $ pnc_nodes_visible = False
    
    call atmo_spaceport from _call_atmo_spaceport_4
    
    # stop alarm
    $ alarm_on = False
    
    call show_space from _call_show_space_20

    show cargo_animbg
    
    #call sound_take_off
    
    
    show light:
        pos (102,120)
        
    show light as light2:
        pos (241,162)
        
    show light as light3:
        pos (580,65)
        
    show light as light4:
        pos (725,170)
    
    
    show spaceshipside:
        zoom 0.7
        pos (370, 520)#(400, -50)
        linear 1.5 pos (370, 450)
        linear 2.5 pos (400, 320) rotate -90
        linear 5 pos (430, -50) rotate 0
        

    if shadow_enable == 1:
        show shadow:
            pos (400, 480)
            linear 9 pos (400, 0)

    
    pause 9
    #centered "cargo anim up"
    
    $ shippos = (800,1200)
    
    jump surface_cargo
    
    
    


    
# cargo explosion
label cargo_explosion_anim:
    $ pnc_nodes_visible = False
    # stop alarm
    $ alarm_on = False
    call alarm_check from _call_alarm_check_15
    
    call show_space from _call_show_space_21
    with pixellate
    
    image cargoship_anim:
        "images/planets/cargo_small.png"
        anchor (0.5,0.5)
        
    show cargoship_anim at truecenter
    pause 2
    
    

    image explosion:
        "images/explosion.png"
        anchor (0.5,0.5)
        
    call sound_explosion from _call_sound_explosion_1
    with hpunch
    show white:
        alpha 0.0
        linear 0.5 alpha 1
        linear 0.5 alpha 0
    show explosion:
        alpha 0.5
        pos (400,240)
        zoom 0.5
        linear 1.5 zoom 3 alpha 0

   
    pause 0.5
    
    call sound_explosion from _call_sound_explosion_2
    with hpunch
    show white:
        alpha 0.0
        linear 0.5 alpha 1
        linear 0.5 alpha 0
    show explosion as explosion2:
        rotate 25
        alpha 0.5
        pos (400,240)
        zoom 0.5
        linear 1.5 zoom 3 alpha 0

        
    pause 0.5
    
    hide cargoship_anim
    
    call sound_explosion from _call_sound_explosion_3
    with hpunch
    show white:
        alpha 0.0
        linear 0.5 alpha 1
        linear 0.5 alpha 0
    show explosion as explosion3:
        rotate 40
        alpha 0.5
        pos (400,240)
        zoom 0.5
        linear 1.5 zoom 3 alpha 0

    
    
    $ cargo_pos = (-100,-100)
    $ cargo_remote_control = "none"
    $ cargo_exploded = 1 # will be set to 2 (final state) in space
    $ planet = "none"
    
    pause 4
    m "Mission accomplished!{w=2}{nw}"
    m "All the weapons are destroyed.{w=2}{nw}"
    m "They won't hurt anybody anymore.{w=2}{nw}"
    m "I think I should call 4n0nym0u5 now.{w=3}{nw}"
    
    
    
    $ startpos = 3
    jump space
    
    
    
    
    
    

