# asteroid anim


label asteroid_collision_anim:
    $ pnc_nodes_visible = False
    
    #stop music fadeout 0.1


    #call show_space
    

    $ asteroidzoom = renpy.random.random()*0.9 + 0.1
    show asteroid_small behind orbitmeter, text_planet, spaceshipside:
        zoom asteroidzoom
        rotate 0
        ypos 100
        xpos 900
        linear 10 xpos -200 rotate -560
        repeat
        
    $ asteroidzoom2 = renpy.random.random()*0.9 + 0.1
    show asteroid_small as asteroid_small3 behind orbitmeter, text_planet, spaceshipside:
        zoom asteroidzoom2
        rotate 0
        ypos 350
        xpos 1200
        linear 13 xpos -200 rotate -460
        repeat


    
    show spaceshipside:
        pos (400, -50)
        linear 3 pos (400, 240)
        linear 3 pos (400, 560) rotate -600
        

        
    show asteroid_small2 zorder 500:
        rotate 0
        zoom 1.0
        pos (900, -100)
        linear 3 pos (400, 190) rotate -360
        linear 3 pos (-100, -100) rotate -360*2
        
        
        
    if shadow_enable == 1:
        show shadow:
            pos (400, 0)
            linear 10 pos (400, 480)

    
    pause 3
    call sound_explosion from _call_sound_explosion_4
    with hpunch
    #with flash
    pause 3
    $ pnc_nodes_visible = True
    
    
    
    # set spaceship broken state
    $ spaceship_broken = True
    $ spaceshiptype = "4b"
    
    
    
    
    $ direction = 600
    $ shippos = (200,1600)
    jump asteroid3
    

