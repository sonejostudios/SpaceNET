# MAPS

############################################

init:
    $ isc_spaceship_interchange = False
    

    
    

label isc_interchange:
    
    stop music fadeout 1.0
    call atmo_spaceport from _call_atmo_spaceport_5 
    
    image isc_interchange = imagemapsdir + "spaceport.png"
    
    scene bgcolor
    show screen notify("Spaceship Interchange")
    
    show isc_interchange
    
    show crane:
        pos (62, 240)
    
    show doorh:
        pos (650,35)
    
    show warningfloor:
        anchor (0.5,0.5)
        pos (570,240)
        rotate 90
        
    show warningfloor as warningfloor2:
        anchor (0.5,0.5)
        pos (730,240)
        rotate 90
    
    
    show light:
        pos (145,130)
        
    show light as light2:
        pos (355,130)
        
    show light as light3:
        pos (145,345)
        
    show light as light4:
        pos (355,345)
        
      
        
    show tube:
        pos (1200,346)
        
    show tube as tube2:
        pos (1200,413)
    
    show rails2:
        pos (950,380)
        
        

   
    
    
    if landing == True:
        show isctrain:
            anchor (0.35,0.5)
            pos (650,380)
    

    # check if spaceship is landing on this map or not
    # $ landing = False
    # $ landing = True
    
    #"[isc_spaceship_interchange]"
    
    if landing == True:
         $ isc_spaceship_interchange = True
         call landing_anim from _call_landing_anim_7
    
    if isc_spaceship_interchange == True:
        #call landing_anim
        show spaceship:
            anchor (0.5,0.5)
            pos (250, 240) 
            zoom 0.75  
            rotate 0
        
    
    
    # set all variables for the map (nodes and path)
    $ nodeA = (650,55) #(467,47)
    $ nodeB = (470,240)
    $ nodeC = (650,340) #(470,420)
    $ nodeD = (249,240)
    
    $ nodeAA = (400,25)
    $ nodeBB = (650,240)
    $ nodeCC = (400,460)
    $ nodeDD = (320,240)
    
    $ pathA = (nodeA, nodeB, nodeC, (0,0), (0,0), nodeBB, (0,0), nodeDD)
    $ pathB = (nodeA, nodeB, nodeC, (0,0), (0,0), nodeBB, (0,0), nodeDD)
    $ pathC = (nodeA, nodeB, nodeC, (0,0), (0,0), nodeBB, (0,0), nodeDD)
    $ pathD = ((0,0), nodeB, nodeC, (0,0), (0,0), (0,0), (0,0), nodeDD)
    
    $ pathAA = (nodeA, (0,0), (0,0), (0,0), nodeAA, (0,0), (0,0), (0,0))
    $ pathBB = (nodeA, nodeB, nodeC, (0,0), (0,0), nodeBB, (0,0), nodeDD)
    $ pathCC = ((0,0), (0,0), nodeC, (0,0), (0,0), (0,0), nodeCC, (0,0))
    $ pathDD = (nodeA, nodeB, nodeC, (0,0), (0,0), nodeBB, (0,0), nodeDD)
    
    if isc_spaceship_interchange == False:
        $ pathBB = (nodeA, nodeB, nodeC, nodeD, (0,0), nodeBB, (0,0), nodeDD)
        $ pathDD = (nodeA, nodeB, nodeC, nodeD, (0,0), nodeBB, (0,0), nodeDD)
        $ pathA = (nodeA, nodeB, nodeC, nodeD, (0,0), nodeBB, (0,0), nodeDD)
        $ pathB = (nodeA, nodeB, nodeC, nodeD, (0,0), nodeBB, (0,0), nodeDD)
        $ pathC = (nodeA, nodeB, nodeC, nodeD, (0,0), nodeBB, (0,0), nodeDD)
        $ pathD = (nodeA, nodeB, nodeC, nodeD, (0,0), nodeBB, (0,0), nodeDD)


    if shadow_enable == 1:
        show shadow zorder 800:
            pos nodeC
    
    image isctrain = "/images/isctrain.png"
        
    
    # train entry anim
    if isctrain_anim == True:
        show isctrain:
            transform_anchor True
            rotate 180
            pos (900,380)
            anchor (0.35,0.5)
            easein 2 pos (650,380)
        pause 2
        show isctrain:
            transform_anchor True
            rotate 180
            anchor (0.35,0.5)
            pos (650,380)
        $ startpos = 3
        $ isctrain_anim = False
        call sound_door from _call_sound_door_169
        
    else:
        show isctrain:
            anchor (0.35,0.5)
            pos (650,380)



    # coming from trip
    #if triptime == True:
    #    $ triptime = False
    #    $ startpos = 22
    #    call sound_scan
    #    #with Dissolve(0.5)
    #    with pixellate



label loop_isc_interchange:
    
    while True:

        # start "move through the map" loop
        call startpos from _call_startpos_78

        # do something at node?
        if exitpos == 1:       #if at node A

            if isc_spaceship_interchange == True:
                call sound_door from _call_sound_door_170
                $ startpos = 1  
                jump isc_spaceshipport
            else:
                call dialog_closed from _call_dialog_closed_45
                
            $ startpos = 1   

            
        if exitpos == 2:
            if startpos == 2:
                m "This is the spaceship interchange station of the Industrial Space City.{w=5.0} {nw}"
            $ startpos = 2

            
        if exitpos == 3:
            if startpos == 3:
                #call dialog_closed
                call sound_door from _call_sound_door_171
                #pause 0.2
                hide player
                
                show isctrain:
                    rotate 0
                    easeout 2 xpos 850
                pause 0.5
                call sound_train from _call_sound_train_1
                pause 1.5
                jump isc_wagon_anim_toright
                
            $ startpos = 3
            
            
        if exitpos == 4:
            if startpos == 4:
                if isc_interchange_gem == True:
                    call take_gem from _call_take_gem_9
                    $ isc_interchange_gem = False
                else:
                    call dialog_nothing from _call_dialog_nothing_58
            $ startpos = 4

            

        #exits routing "got to map and set position for next map"
        if exitpos == 11:       #if going out at AA
            $ startpos = 11    #go to CC

            
        if exitpos == 22:
            if startpos == 22:
                call dialog_nothing from _call_dialog_nothing_59
            $ startpos = 22

            
        if exitpos == 33:
            $ startpos = 33

            
        if exitpos == 44:
            $ startpos = 44
            if isc_spaceship_interchange == True:
                call sound_door from _call_sound_door_172
                call takeoff_anim("withmenu") from _call_takeoff_anim_9 # go to takeoff
                
                $ isc_spaceship_interchange = False
                
                
                # straight to space
                if takeoftospace == True:
                    $ takeoftospace = False
                    $ space_anim = True
                    jump space

                
                # to surface
                if landing == True:
                    $ shippos = (0,1000) # set position in surface engine
                    jump surface_isc
            else:
                pass
                





