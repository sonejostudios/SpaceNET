# games screens


    
    


init python:
    
    # copy mouse position to clipboard
    import pygame.scrap
    def copytext(t):
        pygame.scrap.put(pygame.scrap.SCRAP_TEXT, t.encode("utf-8"))




screen buttons():
    zorder 90
    
    # up right, time, coins, exit
    #timer 3600.0 repeat True action [SetVariable("minutes", 0), SetVariable("seconds", 0),SetVariable("hours", int(hours) + 1)]
    #timer 60.0 repeat True action [SetVariable("seconds", 0),SetVariable("minutes", int(minutes) + 1)]
    #timer 1.0 repeat True action [SetVariable("seconds", int(seconds) +1)]
    
    #$ runtime = int(renpy.get_game_runtime())


    if superdev == True:
        textbutton "restart" action [Jump("start")]:
            xpos 0.7
            ypos -10
    
    
    # menu icon and time
    frame:
        style "menu"
        xpos 795
        ypos 005
        xanchor 1.0
        button:
            #action ShowMenu("save")
            action ShowMenu("preferences")
            #style "menu_choice_button"
            activate_sound "sounds/beep.ogg"
            
            add "/images/menuicon.png"
            #text "save" #style "menu_choice"
            xpos 1.0
            xanchor 1.0

        # timer
        #text "[hours]:[minutes]:[seconds]" size 16  xpos 0.95  ypos 0.0 xanchor 1.0

    
    # countdown
    if countdown == True and countdown_sec >= 0:
        text "[countdown_sec]" size 25  xpos 790  ypos 45 xanchor 1.0
        timer 1 repeat True action [SetVariable("countdown_sec", int(countdown_sec) -1)]
        
    
    # set to countdown=False if countdown <= 0
    if countdown_sec <= 0 and countdown == True:
        timer 1 repeat True action [SetVariable("countdown", False)]
        
        
        
    # inventory button
    if inventory_button == True:
        imagebutton auto "images/inventory/inventory_button_%s.png": 
                #action SetVariable("inventory_select", ""), Show("inventory")
                action Show("inventory"), Hide("selected_item")
                #pos (8,440)
                pos (758, 442)
                
        text (_("{color=#8dd35f}[coins]c")) size 16 xpos 0.94 ypos 0.94 xanchor 1.0
    
    

    
    # pre-version type
    text "{color=#8dd35f}[pre_version]" size 16 xpos 0.01 ypos 0.94 xanchor 0.0

    
    

    
    if use_dev_keys == True:
        # mute all sounds
        key "m" action Preference("all mute", "toggle")
        
        # TOGGLE SUPERDEV
        key "d" action ToggleVariable("superdev")
    
    
    


    
    
screen termfx():
    zorder 1000
    if termfx_enable == 1:
        add "images/termfx.png"
        
    
    # get drunk in bar (drunktime 2xsec)
    if drunktime > 0:
        timer 0.5 repeat True action SetVariable("drunktime", drunktime - 1)
        if superdev == 1:
            text "[drunktime]" pos (0.1, 0.5)

        #if drunktime >= 7 or drunktime == 5 or drunktime == 3 or drunktime == 1:
        #    # blue (beer)
        #    add "#0000FF" alpha 0.2
        
        if drunktime > 10:
            # blue (beer)
            add "#0000FF" alpha 0.2
        else:
            add "#0000FF" alpha (0.2/10)*drunktime
            
            
    
    # alien shot trip (trip 2xsec)
    if triptime == True:
        add "#ffffff"

        
    
    # shadow points
    # maybe better  not as screen, but in moveengine, and show shadowpoints behind the nodes
    # or through the idea, and implement path finding instead
    
    #if path[0] == (0,0):
    #    add "images/shadowpoint.png" anchor (0.5,0.5) pos nodeA
    #if path[1] == (0,0):
    #    add "images/shadowpoint.png" anchor (0.5,0.5) pos nodeB
    #if path[2] == (0,0):
    #    add "images/shadowpoint.png" anchor (0.5,0.5) pos nodeC
    #if path[3] == (0,0):
    #    add "images/shadowpoint.png" anchor (0.5,0.5) pos nodeD
        
    #if path[4] == (0,0):
    #    add "images/shadowpoint.png" anchor (0.5,0.5) pos nodeAA
    #if path[5] == (0,0):
    #    add "images/shadowpoint.png" anchor (0.5,0.5) pos nodeBB
    #if path[6] == (0,0):
    #    add "images/shadowpoint.png" anchor (0.5,0.5) pos nodeCC
    #if path[7] == (0,0):
    #    add "images/shadowpoint.png" anchor (0.5,0.5) pos nodeDD
        
        
        

    
    # if red glasses on / in fire
    #add "#FF0000" alpha 0.2
    
    #if underwater
    #add "#0000FF" alpha 0.2
    #add "#0000FF" alpha 0.1

    


    




screen superdev() zorder 2000:
    if superdev == True:
        # show mouse position for devs
        text "[mousepos]" at left
        
        # move engine values
        text "exitpos: [exitpos]\nstartpos: [startpos]\ngotopos: [gotopos]\nmoving: [moving]\n\n" at right
        
        # surface values
        text "shippos [shippos]  - maplink [maplink] - ingame [ingame]" at center
        
        # inventory values
        text "            inv_select : [inventory_select] - inv_notify : [inventory_notify] - planet : [planet] \n           nodes : [spacenetnodes]\n             liftpos - [liftpos]" at topleft
        
        # mousepos
        timer 0.1 repeat True action [SetVariable("mousepos", renpy.get_mouse_pos())]
        
        
        
        # copy mouse position to clipboard
        key "c" action [Function(copytext, t=str(mousepos)), Notify("Mouse Position copied to Clipboard !")]
        
        
        #text "pnc_nodes_visible: [pnc_nodes_visible]\n\n\n" at center
        

        
    

init:
    $ nodeclicksize = 40

screen setpos():
    zorder 100
    # get every 0.1 sec mouse position
    timer 0.1 repeat True action [SetVariable("mousepos", renpy.get_mouse_pos())]

    
    if (nodeA[0]-nodeclicksize ) < (mousepos[0]) < (nodeA[0]+nodeclicksize) and (nodeA[1]-nodeclicksize ) < (mousepos[1]) < (nodeA[1]+nodeclicksize):
        timer 0.1 repeat True action [SetVariable("gotopos", 1)]
        if superdev == True:
            text "A"

        if pnc_mode == True and pnc_nodes_visible == True and nodeA in path:
            add "images/node.png":
                anchor (0.5,0.5)
                pos nodeA

        
    elif (nodeB[0]-nodeclicksize ) < (mousepos[0]) < (nodeB[0]+nodeclicksize) and (nodeB[1]-nodeclicksize ) < (mousepos[1]) < (nodeB[1]+nodeclicksize):
        timer 0.1 repeat True action [SetVariable("gotopos", 2)]
        if superdev == True:
            text "B"
            
        if pnc_mode == True and pnc_nodes_visible == True and nodeB in path:
            add "images/node.png":
                anchor (0.5,0.5)
                pos nodeB
        
    elif (nodeC[0]-nodeclicksize ) < (mousepos[0]) < (nodeC[0]+nodeclicksize) and (nodeC[1]-nodeclicksize ) < (mousepos[1]) < (nodeC[1]+nodeclicksize):
        timer 0.1 repeat True action [SetVariable("gotopos", 3)]
        if superdev == True:
            text "C"
            
        if pnc_mode == True and pnc_nodes_visible == True and nodeC in path:
            add "images/node.png":
                anchor (0.5,0.5)
                pos nodeC
             
    elif (nodeD[0]-nodeclicksize ) < (mousepos[0]) < (nodeD[0]+nodeclicksize) and (nodeD[1]-nodeclicksize ) < (mousepos[1]) < (nodeD[1]+nodeclicksize):
        timer 0.1 repeat True action [SetVariable("gotopos", 4)]
        if superdev == True:
            text "D"
            
        if pnc_mode == True and pnc_nodes_visible == True and nodeD in path:
            add "images/node.png":
                anchor (0.5,0.5)
                pos nodeD
               
    ###    

    elif (nodeAA[0]-nodeclicksize ) < (mousepos[0]) < (nodeAA[0]+nodeclicksize) and (nodeAA[1]-nodeclicksize) < (mousepos[1]) < (nodeAA[1]+nodeclicksize):
        timer 0.1 repeat True action [SetVariable("gotopos", 11)]
        if superdev == True:
            text "AA"
            
        if pnc_mode == True and pnc_nodes_visible == True and nodeAA in path:
            add "images/node.png":
                anchor (0.5,0.5)
                pos nodeAA
        
    elif (nodeBB[0]-nodeclicksize ) < (mousepos[0]) < (nodeBB[0]+nodeclicksize) and (nodeBB[1]-nodeclicksize ) < (mousepos[1]) < (nodeBB[1]+nodeclicksize):
        timer 0.1 repeat True action [SetVariable("gotopos", 22)]
        if superdev == True:
            text "BB"
        
        if pnc_mode == True and pnc_nodes_visible == True and nodeBB in path:
            add "images/node.png":
                anchor (0.5,0.5)
                pos nodeBB
                
            
    elif (nodeCC[0]-nodeclicksize ) < (mousepos[0]) < (nodeCC[0]+nodeclicksize) and (nodeCC[1]-nodeclicksize ) < (mousepos[1]) < (nodeCC[1]+nodeclicksize):
        timer 0.1 repeat True action [SetVariable("gotopos", 33)]
        if superdev == True:
            text "CC"
            
        if pnc_mode == True and pnc_nodes_visible == True and nodeCC in path:
            add "images/node.png":
                anchor (0.5,0.5)
                pos nodeCC
        
    elif (nodeDD[0]-nodeclicksize ) < (mousepos[0]) < (nodeDD[0]+nodeclicksize) and (nodeDD[1]-nodeclicksize ) < (mousepos[1]) < (nodeDD[1]+nodeclicksize):
        timer 0.1 repeat True action [SetVariable("gotopos", 44)]
        if superdev == True:
            text "DD"
            
        if pnc_mode == True and pnc_nodes_visible == True and nodeDD in path:
            add "images/node.png":
                anchor (0.5,0.5)
                pos nodeDD
            
    ###
            
    else:
        timer 0.1 repeat True action [SetVariable("gotopos", 0)]
        if superdev == True:
            text "NoMove"
            
        
        
        
        
        
        
