# MAPS

############################################

label isc_bar_lift_room:
    
    image crossroomsmall = imagemapsdir + "crossroomsmall.png"
    
    scene bgcolor
    show crossroomsmall at truecenter
    show screen notify("Lift room")
    
    show doorv:
        pos (305,240)
        
    show doorv as doorv2:
        pos (495,240)
    
    show buttonscreen:
        pos (400, 148)
    
    
    # set all variables for the map (nodes and path)
    $ nodeA = (400, 170)
    $ nodeB = (475, 240)
    $ nodeC = (400, 315)
    $ nodeD = (325, 240)
    

    $ nodeAA = (400, 240)
    $ nodeBB = (-100, -100)
    $ nodeCC = (-100, -100)
    $ nodeDD = (-100, -100)

    $ pathA = (nodeA, nodeB, (0, 0), nodeD, (0, 0), (0, 0), (0, 0), (0, 0))
    $ pathB = (nodeA, nodeB, (0, 0), nodeD, (0, 0), (0, 0), (0, 0), (0, 0))
    $ pathC = (nodeA, nodeB, nodeC, nodeD, (0, 0), (0, 0), (0, 0), (0, 0))
    $ pathD = (nodeA, nodeB, (0, 0), nodeD, (0, 0), (0, 0), (0, 0), (0, 0))
     
    $ pathAA = (nodeA, nodeB, nodeC, nodeD, (0, 0), (0, 0), (0, 0), (0, 0))
    $ pathBB = (nodeA, nodeB, nodeC, nodeD, (0, 0), (0, 0), (0, 0), (0, 0))
    $ pathCC = (nodeA, nodeB, nodeC, nodeD, (0, 0), (0, 0), (0, 0), (0, 0))
    $ pathDD = (nodeA, nodeB, nodeC, nodeD, (0, 0), (0, 0), (0, 0), (0, 0))
    
    



label loop_isc_bar_lift_room:

    while True:

        # start "move through the map" loop
        call startpos from _call_startpos_27
        

        # do something at node?
        if exitpos == 1:
            if startpos ==1 :
                call isc_bar_lift_info from _call_isc_bar_lift_info 
            $ startpos = 1 

            
        if exitpos == 2:
            $ liftpos = 3
            call sound_door from _call_sound_door_65
            jump isc_city_bar_lift2
            $ startpos = 2
            

        if exitpos == 3:
            $ startpos = 3

            
            
        if exitpos == 4:
            $ liftpos = 0
            call sound_door from _call_sound_door_66
            jump isc_city_bar_lift1
            $ startpos = 4


        #######
        
        if exitpos == 11:
            $ startpos = 11
 
            
        if exitpos == 22:
            $ startpos = 22

            
        if exitpos == 33:
            $ startpos = 33

            
        if exitpos == 44:
            $ startpos = 44






label isc_bar_lift_info:
    
    $ info_panel_symbol = "noentry"

    $ showtext = """
    
    
- Restricted Area -


This area is strictly prohibided. 
Entering without a special authorisation
will be punished by law.

    """
    
    # {font=marvosym.ttf}{size=70}haj{/size}{/font}
    # {font=symbolx.ttf}{size=70}bpr{/size}{/font}
    
    call info_panel from _call_info_panel_4 # in animations
    
    
    return


