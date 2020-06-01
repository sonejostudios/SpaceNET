# MAPS

############################################



    

label xylo_spaceport_hall_bar_wcs:
    
    stop atmo
    
    if xylo_village_bar_music == 1:
        call music_bar_village_deep
    
    if xylo_village_bar_music == 2:
        call music_bar_chill_deep
        
    if xylo_village_bar_music == 3:
        call music_outro_deep
    
    if xylo_village_bar_music == 4:
        stop music fadeout 1.0
    
    
    image crossroomsmall = imagemapsdir + "crossroomsmall.png"
    
    scene bgcolor
    show crossroomsmall at truecenter
    show screen notify("Bathroom")
        
    show wc:
        anchor (0.5,0.5)
        pos (475, 240)
        rotate 90
        
    show doorv:
        pos (305,240)
        
    show buttonscreen:
        pos (400,147)
        

    # set all variables for the map (nodes and path)
    $ nodeA = (400, 170)
    $ nodeB = (435, 240)
    $ nodeC = (400, 320)
    $ nodeD = (320, 240)
    

    $ nodeAA = (400, 240)
    $ nodeBB = (-100, -100)
    $ nodeCC = (-100, -100)
    $ nodeDD = (-100, -100)

    $ pathA = (nodeA, nodeB, nodeC, nodeD, (0, 0), (0, 0), (0, 0), (0, 0))
    $ pathB = (nodeA, nodeB, nodeC, nodeD, (0, 0), (0, 0), (0, 0), (0, 0))
    $ pathC = (nodeA, nodeB, nodeC, nodeD, (0, 0), (0, 0), (0, 0), (0, 0))
    $ pathD = (nodeA, nodeB, nodeC, nodeD, (0, 0), (0, 0), (0, 0), (0, 0))
     
    $ pathAA = (nodeA, nodeB, nodeC, nodeD, (0, 0), (0, 0), (0, 0), (0, 0))
    $ pathBB = (nodeA, nodeB, nodeC, nodeD, (0, 0), (0, 0), (0, 0), (0, 0))
    $ pathCC = (nodeA, nodeB, nodeC, nodeD, (0, 0), (0, 0), (0, 0), (0, 0))
    $ pathDD = (nodeA, nodeB, nodeC, nodeD, (0, 0), (0, 0), (0, 0), (0, 0))
    
  
  
label loop_xylo_spaceport_hall_bar_wcs:

    while True:

        # start "move through the map" loop
        call startpos
        

        # do something at node?
        if exitpos == 1:
            if startpos == 1:
                if startpos == 1:
                    #m "This is an advertisement panel. {w=2} {nw}"
                    call xylo_spaceport_hall_bar_wcs_info    
            $ startpos = 1 

            
        if exitpos == 2:
            if startpos == 2:
                m "This is the wc... {w=1}it is really dirty! {w=2} {nw}"
                menu:
                    "flush":
                        call sound_flush
                        pause 5
                        m "It looks better now. {w=2} {nw}"
                        if xylo_spaceport_hall_wc_cash_wc > 0:
                            m "There is some money! {w=2} {nw}"
                            call io_cash(xylo_spaceport_hall_wc_cash_wc)
                            $ xylo_spaceport_hall_wc_cash_wc = 0
                    
                    "do nothing":
                        pass
            $ startpos = 2
            

        # cash
        if exitpos == 3:
            if startpos == 3:
                if xylo_spaceport_hall_wc_cash > 0:
                    m "Oh, there are some coins... {w=2} {nw}"
                    call io_cash(xylo_spaceport_hall_wc_cash)
                    $ xylo_spaceport_hall_wc_cash = 0
                else:
                    call dialog_nothing
            $ startpos = 3

            
        if exitpos == 4:
            call sound_door
            $ startpos = 33
            jump xylo_spaceport_hall_bar
            #$ startpos = 4


        #######
        
        if exitpos == 11:
            $ startpos = 11
 
            
        if exitpos == 22:
            $ startpos = 22

            
        if exitpos == 33:
            $ startpos = 33

            
        if exitpos == 44:
            $ startpos = 44





label xylo_spaceport_hall_bar_wcs_info:
    
    $ info_panel_symbol = "" #"exit"

    $ showtext = """
- THE BEAUTIFUL XYLO SEA -


Do you need some holidays?

Spend some time at the xylo sea. 

Enjoy its beautiful coast, the sunsets, 

the beach and the boat trips.

"""

    if drunktime > 0:
        $ showtext = """
- Hey! -

Hi hi hi...
It looks like you had 
too many galactic beers!

Please, 
don't forget to flush the wc 
when you are done!


"""




    
    call info_panel # in animations
    
    
    return



