# MAPS

############################################

image hyperspace_module:
    "images/inventory/module_idle.png"
    anchor (0.5, 0.5)
    
image cord_throw:
    "images/cord_throw.png"
    anchor (0.0, 0.5)
    
image cord_throw2:
    "images/cord_throw2.png"
    anchor (1.0, 1.0)

init:
    $ module_orbit_pos_x = 0 # needes to be defined first
    $ module_orbit_pos_y = 0 # needes to be defined first
    
    $ asteroid_cord_on_ground = False
    
    $ module_in_orbit = True


screen asteroid1_orbitpos():
    # get orbit position
    $ asteroidsmall1_orbit_box = renpy.get_image_bounds("asteroid_small")
    $ asteroidsmall1_orbit_pos = (int(asteroidsmall1_orbit_box[0]), int(asteroidsmall1_orbit_box[1]))

    $ asteroidsmall2_orbit_box = renpy.get_image_bounds("asteroid_small2")
    $ asteroidsmall2_orbit_pos = (int(asteroidsmall2_orbit_box[0]), int(asteroidsmall2_orbit_box[1]))
    
    $ module_orbit_box = renpy.get_image_bounds("hyperspace_module")
    $ module_orbit_pos = (int(module_orbit_box[0]), int(module_orbit_box[1]))
    
    timer 0.1 repeat True action [SetVariable("module_orbit_pos_x", int(module_orbit_box[0])), SetVariable("module_orbit_pos_y", int(module_orbit_box[1]))]
    
#~     if superdev == True:
#~         text " asteroidsmall1 [asteroidsmall1_orbit_pos]\n\n asteroidsmall2 [asteroidsmall2_orbit_pos]\n\n module_orbit [module_orbit_pos]":
#~             ypos 80
            
#~         if module_orbit_pos_x > 580 and 50 < module_orbit_pos_y < 190:
#~             text "NOW!" as text2:
#~                 ypos 240
                


label asteroid1:
    $ pnc_nodes_visible = True

    stop music fadeout 1.0
    
    #call atmo_deep_ambiance
    call atmo_spaceship_station from _call_atmo_spaceship_station_8
    
    show screen asteroid1_orbitpos
    
    image asteroid1 = imagemapsdir + "asteroid1.png"
    
    scene bgcolor
    call show_space from _call_show_space_25
    show screen notify("Asteroid 1")
    
    show asteroid1 at inspace_idle
    
    show asteroid_small:
        rotate 0
        anchor (0.5, 0.5)
        zoom 0.5
        around (330, 240)
        radius 262
        angle 180
        linear 20 clockwise circles 1 rotate -360*4
        repeat
    
    show asteroid_small2:
        rotate 0
        anchor (0.5, 0.5)
        zoom 0.7
        around (330, 240)
        radius 320
        angle 0
        linear 30 clockwise circles 1 rotate 360*4
        repeat
        
    
    if module_in_orbit == True:
        show hyperspace_module:
            rotate 0
            zoom 0.3
            around (330, 240)
            radius 350
            angle 180
            linear 30 clockwise circles 1 rotate -360*4
            repeat
    else:
        show hyperspace_module:
            pos (-100, -100)
        
        
    if asteroid_cord_on_ground == True:
        show cord behind player:
            pos (450, 157)
            zoom 0.5
        
    
    
    #show warningfloor:
    #    anchor (0.5,0.5)
    #    pos (570,240)
    #    rotate 90
    
    #show light:
    #    pos (145,130)
        
    #show light as light2:
    #    pos (355,130)
        
    #show light as light3:
    #    pos (145,345)
        
    #show light as light4:
    #    pos (355,345)
        

    # check if spaceship is landing on this map or not
    # $ landing = False
    # $ landing = True
    call landing_anim from _call_landing_anim_8
    
    
    # set all variables for the map (nodes and path)
    $ nodeA = (360, 153)
    $ nodeB = (446, 186)
    $ nodeC = (560, 120)
    $ nodeD = (403, 287)
    
    $ nodeAA = (400,25)
    $ nodeBB = (670,240)
    $ nodeCC = (400,460)
    $ nodeDD = (315,240)
    
    $ pathA = (nodeA, nodeB, (0,0), nodeD, (0,0), (0,0), (0,0), nodeDD)
    $ pathB = (nodeA, nodeB, (0,0), nodeD, (0,0), (0,0), (0,0), nodeDD)
    $ pathC = (nodeA, nodeB, (0,0), nodeD, (0,0), (0,0), (0,0), nodeDD)
    $ pathD = (nodeA, nodeB, (0,0), nodeD, (0,0), (0,0), (0,0), nodeDD)
    
    $ pathAA = (nodeA, nodeB, (0,0), nodeD, (0,0), (0,0), (0,0), nodeDD)
    $ pathBB = (nodeA, nodeB, (0,0), nodeD, (0,0), (0,0), (0,0), nodeDD)
    $ pathCC = (nodeA, nodeB, (0,0), nodeD, (0,0), (0,0), (0,0), nodeDD)
    $ pathDD = (nodeA, nodeB, (0,0), nodeD, (0,0), (0,0), (0,0), nodeDD)
    
    
    if landing == True:
        $ inventory_select = "spacesuit"
        call inventory_notify from _call_inventory_notify_10
        
        





label loop_asteroid1:
    
    while True:
        # start "move through the map" loop
        call startpos from _call_startpos_83 


        # do something at node?
        if exitpos == 1:
            if startpos == 1:
                if inventory_select == "":
                    m "Nice place here. {w=2.5} {nw}"
                else:
                    call asteroid_dig(0) from _call_asteroid_dig_3
            $ startpos = 1   
            
            
            
            
            
        if exitpos == 2:
            if startpos == 2:
                call asteroid1_nodeB from _call_asteroid1_nodeB # do everything at node B
            $ startpos = 2
            
            
        if exitpos == 3:
            $ startpos = 3

            
        if exitpos == 4:
            if startpos == 4:
                if inventory_select == "":
                    m "This asteroid is really small. {w=2.5} {nw}"
                    m "But big enough for landing! {w=2.5} {nw}"
                else:
                    call asteroid_dig(0) from _call_asteroid_dig_4
            $ startpos = 4

            

        if exitpos == 11:     
            $ startpos = 11   

            
        if exitpos == 22:
            $ startpos = 22

            
        if exitpos == 33:
            $ startpos = 33

            
        # spaceship
        if exitpos == 44:
            $ startpos = 44
            #call sound_door
            call takeoff_anim("withmenu") from _call_takeoff_anim_10 # go to takeoff
            $ pnc_nodes_visible = True
            
            # straight to space
            if takeoftospace == True:
                $ takeoftospace = False
                $ space_anim = True
                $ pnc_nodes_visible = False
                hide screen asteroid1_orbitpos
                jump space

            
            # to surface
            if landing == True:
                $ shippos = (0,400) # set position in surface engine
                hide screen asteroid1_orbitpos
                jump surface
                



# node B
label asteroid1_nodeB:
    
    if inventory_select == "":
        if  module_orbit_pos_x > 580 and module_in_orbit == True:
            m "There is also a small metallic object in orbit! {w=4.5} {nw}"
            m "But what could it be? {w=3} {nw}"

        elif asteroid_cord_on_ground == True:
            m "It is nice to have this cord on the ground, but what to do with it now? {w=5} {nw}"
        
        else:
            m "Wow, some small asteroids are in orbit around us. {w=4.5} {nw}"
            if module_in_orbit == True:
                m "They are so close I could almost catch them! {w=4} {nw}"
            

    elif inventory_select == "cord" and asteroid_cord_on_ground == False:
        m "A cord alone is not enough for fishing! {w=3.5} {nw}"
        m "Let's try to attach the proper tool to it. {w=3.5} {nw}"
        
        call use_item from _call_use_item_7
        $ asteroid_cord_on_ground = True
        show cord behind player:
            pos (450, 157)
            zoom 0.5
            

    elif inventory_select == "hook" and asteroid_cord_on_ground == True:
        m "This is a nice idea if I want to catch some fish. {w=3.5} {nw}"
        m "Well... {w=1.5} {nw}"
        m "Actually, this is really not a good idea! {w=3.5} {nw}"
        m "I'd rather save myself instead of trying to catch some fish in space! {w=5} {nw}"
        $ inventory_select = ""
        

    elif inventory_select == "magnet" and asteroid_cord_on_ground == True:
        m "Let's try to tight this magnet to the cord. {w=3.5} {nw}"
        call use_item from _call_use_item_8
        call get_item("magnetcord") from _call_get_item
        
        if inventory_notify == "magnetcord":
            hide cord
            $ asteroid_cord_on_ground = False
            

    elif inventory_select not in ["magnet","hook"] and asteroid_cord_on_ground == True:
        m "This could be an interesting piece of art. {w=3.5} {nw}"
        m "But actually... {w=2.5} {nw}"
        m "It is not the right moment to be an artist! {w=3.5} {nw}"
        $ inventory_select = ""
         
    
    elif inventory_select == "hook" or inventory_select == "magnet":
        m "This is a nice idea but it is not long enough. {w=3.5} {nw}"
        


    # throw magnetcord
    elif inventory_select == "magnetcord" and module_in_orbit == True:
        call use_and_keep_item from _call_use_and_keep_item_38
        show cord_throw:
            pos nodeB
            xzoom 0.0
            ease 0.5 xzoom 1.0
        
        pause 0.5
        
        if module_orbit_pos_x > 580 and 50 < module_orbit_pos_y < 190:
            pause 0.5
            
            show hyperspace_module:
                pos (674, 187)
                linear 3 pos (900,580)
            show cord_throw2:
                pos (674, 187)
                linear 3 pos (900,580)
            $ inventory.remove("magnetcord")
            hide cord_throw
            call sound_collect from _call_sound_collect_12
            with flash
            $ module_in_orbit = False
            pause 3
            
            m "Oh no!{w=0.5} no!{w=0.5} no!{w=0.5} no!{w=0.5} no!...{w=2}{nw}"
            m "Now I lost everything. {w=3} {nw}"
            m "That was my last hope. {w=3} {nw}"
            m "I will never escape from this stupid asteroid field!{w=4} {nw}"
            
            
        
        else:
            show cord_throw:
                pos nodeB
                xzoom 1.0
                ease 0.5 xzoom 0.0
            pause 0.5
            #with hpunch

            

    elif inventory_select == "magnetcord" and module_in_orbit == False:
        m "I really have better things to do right now than fishing around!{w=4.5}{nw}"
    
    else:
        call asteroid_dig(0) from _call_asteroid_dig_5
    
    
    return




# asteroid dig with pick or with shovel
label asteroid_dig(found):
    if inventory_select == "":
        call dialog_nothing from _call_dialog_nothing_68
    
    elif inventory_select == "pick" or inventory_select == "shovel":
        call sound_dig from _call_sound_dig_7
        
        $ inventory_select2 = inventory_select
        
        call use_and_keep_item from _call_use_and_keep_item_39
         
        
        pause 1.5
        if found == 0:
            call dialog_nothing from _call_dialog_nothing_69
            
    elif inventory_select == "asteroid":
        m "I think, I really don't need this asteroid piece.{w=3.5}{nw}"
        m "I'll throw it away.{w=2.5}{nw}"
        m "Bye-bye!{w=2}{nw}"
        call use_item from _call_use_item_9
        show asteroid_small as astrobullet:
            pos position
            zoom 0.25
            rotate 0
            linear 4 pos (900, -100) rotate 360
    
    elif inventory_select != "pick" or inventory_select != "shovel":
        call dialog_nosense from _call_dialog_nosense_34
    
    else:
        pass

    return





