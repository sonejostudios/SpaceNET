# docking


init:
    $ docking_posx = 5
    $ docking_posy = 5
    $ docking_zoom = 0.2
    $ docking_zoom2 = 40.0
    $ new_docking_pos = [400,240]
    $ new_docking_pos2 = [0,0]
    
    
screen docking_screen():
    imagebutton auto "images/dockup_%s.png" action SetVariable("docking_posy", -5), Play("sound", "sounds/small-propulsion.ogg") align (0.5, 0.0)
    imagebutton auto "images/dockdown_%s.png" action SetVariable("docking_posy", 5), Play("sound", "sounds/small-propulsion.ogg") align (0.5, 1.0)
    imagebutton auto "images/dockleft_%s.png" action SetVariable("docking_posx", -5), Play("sound", "sounds/small-propulsion.ogg") align (0.0, 0.5)
    imagebutton auto "images/dockright_%s.png" action SetVariable("docking_posx", 5), Play("sound", "sounds/small-propulsion.ogg") align (1.0, 0.5)
    
    add "images/dockingtarget.png" align (0.5,0.5)

    
    #text "[docking_posx] [docking_posy]- [new_docking_pos] - [new_docking_pos2] - [docking_zoom]" at truecenter
    
    vbox:
        pos (30,380)
        text "{color=#8dd35f}DATA"
        null height 10
        #text "{color=#8dd35f}Position: [spaceship_pos]"
        text "{color=#8dd35f}Target: [new_docking_pos2] cm"
        text "{color=#8dd35f}Distance: [docking_zoom2] m"
            
    

label docking:
    
    $ pnc_nodes_visible = False
    
    call music_satellite from _call_music_satellite_1
    
    image satellite:
        "images/satellite.png"
        anchor (0.5,0.5)
    
    show bgcolor
    hide orbitmeter
    hide text_planet
    
    $ docking_zoom = 0.2
    $ docking_zoom2 = 40.0
    $ new_docking_pos = [400,240]
    $ new_docking_pos2 = [0,0]
    
    
    show satellite:
        pos (400,550)
        zoom docking_zoom
        ease 4 pos (400,240)
        
    
    if shadow_enable == 1:
        show shadow zorder 999:
            pos (0.5, 1.5)
            easein 4 pos (0.5, 0.5)
            
    pause 4

    show screen notify("Ready for docking")
        
    menu:
        "Start docking":
            if spaceshiptype == "2":
                jump start_docking
            
            else:
                call sound_beep from _call_sound_beep_38
                with hpunch
                m "My spaceship doesn't have a docking hatch!{w=3.0} {nw}"
                jump leave_docking2
            
            
            
        "Leave":
            jump leave_docking2
    
        
    
label start_docking:
    show screen docking_screen
    with Dissolve(1)
    

    # docking loop
    while docking_zoom <= 1.0:
        
        $ new_docking_pos[0] = new_docking_pos[0] + docking_posx
        $ new_docking_pos[1] = new_docking_pos[1] + docking_posy
        
        show satellite:
            linear 1 zoom docking_zoom pos new_docking_pos

        pause 1
        $ docking_zoom += 0.02
        
        # show values
        $ new_docking_pos2 = [new_docking_pos[0]-400 , new_docking_pos[1]-240]
        $ docking_zoom2 = ((1 - docking_zoom) * 100) / 2
        
    
    
    # is docking?
    if -10 <= new_docking_pos2[0] <= 10 and -10 <= new_docking_pos2[1] <= 10 :
        
        show satellite:
            ease 1 pos [400,240]
            
        $ new_docking_pos2 = [0,0]
        $ docking_zoom2 = 0.0
        radio "Docking successful!{w=2.0} {nw}"
        hide screen docking_screen
        
        $ startpos = 1
        call sound_door from _call_sound_door_140
        jump satellite_io11
    
    else:
        jump leave_docking
        
        

    return
    
    

label leave_docking: # anim back from sattelite
    $ pnc_nodes_visible = False
    
    call music_space from _call_music_space_1

    if shadow_enable == 1:
        show shadow zorder 999:
            pos (0.5, 0.5)
            
    call sound_take_off from _call_sound_take_off_6
    hide screen docking_screen
    show satellite:
        pos (400,240)
        ease 5 zoom 0.2 pos (400,240)
    
    pause 5

    show satellite:
        ease 2 pos (400,550)
        
    if shadow_enable == 1:
        show shadow zorder 999:
            pos (0.5, 0.5)
            easein 3 pos (0.5, 1.5)
        
    pause 2
    
    call takeoff_space_anim from _call_takeoff_space_anim_2
    with Dissolve(1)
    jump space
        
     
     
        
label leave_docking2: #leave docking from menu
    $ pnc_nodes_visible = False
    
    call music_space from _call_music_space_2

    call sound_take_off from _call_sound_take_off_7
    hide screen docking_screen


    show satellite:
        ease 3 pos (400,550)
        
    if shadow_enable == 1:
        show shadow zorder 999:
            pos (0.5, 0.5)
            easein 3 pos (0.5, 1.5)
        
    pause 2
    
    call takeoff_space_anim from _call_takeoff_space_anim_3
    with Dissolve(1)
    jump space
    
