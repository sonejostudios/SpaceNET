# MAPS

############################################

init:
    $ tutorial_propeller = False



# bunker map

label tutorial_room1:
    
    stop music
    call atmo_spaceship_hum from _call_atmo_spaceship_hum_7
    
    $ startpos = 2
    
    #$ inventory = ["accesscard"]
    $ inventory = []
    
    $ tutorial_propeller = False
    
    
    show screen setpos
    show screen buttons
    show screen selected_item
    show screen termfx
    show screen superdev
    window hide
    
    
    image totorial_room1 = imagemapsdir + "crossroom.png"
    
    scene bgcolor
    show totorial_room1 at truecenter

    #show screen notify("spacenet tutorial")
    
    
    
    show box:
        pos (270, 110)
        
    #show box as box2:
    #    pos (470, 330)
        
    show box as box3:
        pos (530, 325)
    
    
    show circle:
        pos (290,350)
            

    
    
    #doors (comment to disable)
    show doorh as doorA:
        pos (500, 53)
    #show doorv as doorB:
    #    pos (587, 240)
    #show doorh as doorC:
    #    pos (400, 427)
    show doorv as doorD:
        pos (213, 240)
    
   
    
    show buttonscreen: #right
        pos (586, 240)
        rotate 90
        
    show buttonscreen as buttonscreen2: # down
        pos (400,426)
        
    

    # set all variables for the map (nodes and path)
    $ nodeA = (500, 73)
    $ nodeB = (560, 240)
    $ nodeC = (400, 402)
    $ nodeD = (235, 240)
    

    $ nodeAA = (400, 240)
    $ nodeBB = (550, 402)
    $ nodeCC = (-100, -100)
    $ nodeDD = (-100, -100)

    $ pathA = (nodeA, nodeB, nodeC, nodeD, nodeAA, (0, 0), nodeCC, (0, 0))
    $ pathB = (nodeA, nodeB, (0, 0), nodeD, nodeAA, (0, 0), nodeCC, (0, 0))
    $ pathC = (nodeA, (0, 0), nodeC, (0, 0), nodeAA, nodeBB, nodeCC, (0, 0))
    $ pathD = (nodeA, nodeB, (0, 0), nodeD, nodeAA, (0, 0), nodeCC, (0, 0))
     
    $ pathAA = (nodeA, nodeB, nodeC, nodeD, nodeAA, (0, 0), nodeCC, (0, 0))
    $ pathBB = ((0, 0), (0, 0), nodeC, (0, 0), (0, 0), nodeBB, (0, 0), (0, 0))
    $ pathCC = (nodeA, nodeB, nodeC, nodeD, nodeAA, (0, 0), nodeCC, (0, 0))
    $ pathDD = (nodeA, nodeB, (0, 0), nodeD, nodeAA, nodeBB, nodeCC, nodeDD)
    
    
    # show info panel first
    call tutorial_info from _call_tutorial_info
    
    



label loop_tutorial_room1:
    
    if tutorial_propeller == True:
        hide propeller2
        if renpy.showing("propeller") != True:
            show propeller behind shadow:
                pos (290,350)
                linear 10 rotate 180.0
                rotate 0
                repeat
    else:
        hide propeller
        show propeller as propeller2 behind shadow:
                pos (290,350)

    
    
    while True:

        # start "move through the map" loop
        call startpos from _call_startpos_81 

        # do something at node?
        if exitpos == 1:
            if startpos == 1:
                if inventory_select != "accesscard":
                    call dialog_closed from _call_dialog_closed_47
                else:
                    call sound_electroshock from _call_sound_electroshock_26
                    with hpunch
                    m "This access card doesn't work on this door.{w=3.0} {nw}"
                    $ inventory_select = ""
            
            $ startpos = 1
            
        
        if exitpos == 2:
            if startpos == 2:
                call tutorial_info from _call_tutorial_info_1
            $ startpos = 2

            
        if exitpos == 3:
            if startpos == 3:
                show screen tutorial_button_panel
            $ startpos = 3

            
        if exitpos == 4:
            if startpos == 4:
                if inventory_select != "accesscard":
                    call dialog_closed from _call_dialog_closed_48
                else:
                    m "Let's try to use the access card on the door.{w=3.0} {nw}"
                    call sound_door from _call_sound_door_175
                    $ inventory_select = ""
                    m "The door is now open!{w=3.0} {nw}"
                    m "Now I'm ready... Let's go!{w=3.0} {nw}"
                    #with pixellate
                    $ inventory = []
                    $ coins = 0
                    stop atmo
                    $ renpy.music.play("music/space-amb.ogg", channel="music", fadein=1, fadeout=0, tight=True, if_changed=True)
                    
                    $ tutorial_done = True
                    
                    jump _invoke_main_menu
                    
                
            $ startpos = 4



        if exitpos == 11:  
            #jump tutorial_room1
            if startpos == 11:
                m "This is the tutorial room.{w=2.5} {nw}"
                m "On the right, there is an information panel.{w=3.5} {nw}"
                m "Close to the aeration, there is a button panel.{w=3.5} {nw}"
            $ startpos = 11     
 
            
        if exitpos == 22:
            if startpos == 22:
                if "accesscard" not in inventory:
                    m "There is something on the floor.{w=2.5} {nw}"
                    m "It is an access card!{w=2} {nw}"
                    call take_item("accesscard") from _call_take_item_18 
                else:
                    m "This is a big metal box.{w=2.5} {nw}"
                    call dialog_nothing from _call_dialog_nothing_35
                    if coins == 0:
                        m "Wait...{w=1.5} {nw}"
                        m "I think there are some coins!{w=2.5} {nw}"
                        call io_cash(tutorial_cash) from _call_io_cash_24
                        #$ tutorial_cash = 0
                        m "I found 5c... I'm rich!{w=2.5} {nw}"
                
            $ startpos = 22

            
        if exitpos == 33:
            $ startpos = 33

            
        if exitpos == 44:
            $ startpos = 44




label tutorial_info:
    
    $ info_panel_symbol = "node"
    $ showtext = """
SpaceNET          Tutorial


The dashed circles are action points. Just click on one
to move to it. When you are on an action point, click on it
again to perform an action (look, talk, take, etc.). 
If an item of the inventory is selected (click it twice), 
you will then perform an action with this item (use, give, etc.).

Your inventory is in the bottom-right corner of the screen.
The game menu is in the top-right corner.
To exit this panel, or any other, just click somewhere on it.


The exit door is locked.
To open it, you'll need to find its access card.

Good luck!
    """
    
    call info_panel from _call_info_panel_20 # in animations

    return



#button screen
screen tutorial_button_panel() zorder -999:
    #add "#112119"
    
    on "show" action SetVariable("pnc_nodes_visible", False)
    on "hide" action SetVariable("pnc_nodes_visible", True)
    
    imagebutton: 
        idle "images/maps/bg.png" 
        action [Hide("tutorial_button_panel"), Jump("loop_tutorial_room1")]
            
    add "inventory/inventory.png"

    hbox xalign 0.5 yalign 0.5:
        vbox xalign 0.5:
            
            label "Aeration" at center
            null height 10
            imagebutton at center:
                auto "images/buttonbig_%s.png" 
                action [ToggleVariable("tutorial_propeller"), Play("sound", "sounds/beep.ogg")]
            null height 10
            label "Start/Stop " at center
            
        
            
    if shadow_enable == 1:
        add "images/shadow.png" align (0.5,0.5)
    


