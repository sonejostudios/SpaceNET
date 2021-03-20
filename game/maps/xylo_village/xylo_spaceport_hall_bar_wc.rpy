# MAPS

############################################



    

label xylo_spaceport_hall_bar_wcs:
    
    stop atmo
    
    if xylo_village_bar_music == 1:
        call music_bar_village_deep from _call_music_bar_village_deep_1
    
    if xylo_village_bar_music == 2:
        call music_bar_chill_deep from _call_music_bar_chill_deep_1
        
    if xylo_village_bar_music == 3:
        call music_outro_deep from _call_music_outro_deep_1
    
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
    $ nodeB = (433, 240)
    $ nodeC = (400, 320)
    $ nodeD = (325, 240)
    

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
        call startpos from _call_startpos_80
        

        # do something at node?
        if exitpos == 1:
            if startpos == 1:
                if startpos == 1:
                    #m "This is an advertisement panel. {w=2} {nw}"
                    call xylo_spaceport_hall_bar_wcs_info from _call_xylo_spaceport_hall_bar_wcs_info    
            $ startpos = 1 

            
        if exitpos == 2:
            if startpos == 2:
                m "This is the toilet... {w=1}it is really dirty! {w=2} {nw}"
                menu:
                    "Flush":
                        call sound_flush from _call_sound_flush_3
                        pause 5
                        m "It looks better now. {w=2} {nw}"
                        if xylo_spaceport_hall_wc_cash_wc > 0:
                            m "There is some money! {w=2} {nw}"
                            call io_cash(xylo_spaceport_hall_wc_cash_wc) from _call_io_cash_22
                            $ xylo_spaceport_hall_wc_cash_wc = 0
                    
                    "Do nothing":
                        pass
            $ startpos = 2
            

        # cash
        if exitpos == 3:
            if startpos == 3:
                if xylo_spaceport_hall_wc_cash > 0:
                    m "Oh, there are some coins... {w=2} {nw}"
                    call io_cash(xylo_spaceport_hall_wc_cash) from _call_io_cash_23
                    $ xylo_spaceport_hall_wc_cash = 0
                else:
                    call dialog_nothing from _call_dialog_nothing_60
            $ startpos = 3

            
        if exitpos == 4:
            call sound_door from _call_sound_door_174
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
Spend some time at the Xylo sea. 

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
don't forget to flush the toilet
when you are done!


"""

    
    call info_panel from _call_info_panel_19 # in animations
    
    
    return



