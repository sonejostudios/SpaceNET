# games screens


    
    


init python:
    
    # copy mouse position to clipboard
    import pygame.scrap
    def copytext(t):
        pygame.scrap.put(pygame.scrap.SCRAP_TEXT, t.encode("utf-8"))




screen buttons():
    zorder 90
 
    if superdev == True:
        textbutton "restart" action [Jump("start")]:
            xpos 0.7
            ypos -10
    
    
    # menu icon and time
    imagebutton:
        idle "images/menuicon_idle.png"
        action ShowMenu("preferences")
        anchor (0.5, 0.5)
        pos (777, 025)

    
    # countdown
    if countdown == True and countdown_sec >= 0:
        text "[countdown_sec]" size 25  xpos 790  ypos 45 xanchor 1.0
        timer 1 repeat True action [SetVariable("countdown_sec", int(countdown_sec) -1)]
        
    
    # set to countdown=False if countdown <= 0
    if countdown_sec <= 0 and countdown == True:
        timer 1 repeat True action [SetVariable("countdown", False)]
        
        
        
    # inventory button
    if inventory_button == True:
        imagebutton:
            idle "images/inventory/inventory_button_idle.png"
            action Show("inventory"), Hide("selected_item")
            anchor (0.5,0.5)
            pos (775, 457)
                
        text (_("{color=#8dd35f}[coins]c")) size 16 xpos 0.94 ypos 0.94 xanchor 1.0
    
    

    
    # pre-version type
    text "{color=#8dd35f}[pre_version]" size 16 xpos 0.01 ypos 0.94 xanchor 0.0

    
    
    # mute all sounds
    key "m" action [Preference("all mute", "toggle"), Notify("Mute toggled")]
    
    
    # show inventory
    #key "i" action Show("inventory"), Hide("selected_item")
    if inventory_button == True:
        key "mousedown_3" action Show("inventory"), Hide("selected_item")

        # inventory select up
        key 'mousedown_5':
            if inventory_select_number < len(inventory)-1:
                action SetVariable("inventory_select_number", inventory_select_number+1), SetVariable("inventory_select", inventory[inventory_select_number+1]), Show("selected_item")

        # inventory select down
        key 'mousedown_4':
            if inventory_select_number > 0:
                action SetVariable("inventory_select_number", inventory_select_number-1), SetVariable("inventory_select", inventory[inventory_select_number-1]), Show("selected_item")
            else:
                action SetVariable("inventory_select_number", -1), SetVariable("inventory_select", ""), Hide("selected_item")
        




    # workaround to not crash from old saves (because in old version cash/lamp was added but not shown)
    # remove "cash" from inventory
    if "cash" in inventory:
        $ inventory.remove("cash")
    
    # replace "lamp" with "flashlight"
    if "lamp" in inventory:
        if "flashlight" not in inventory:
            $ inventory.append("flashlight")
        $ inventory.remove("lamp")
    
    
    
    
    
    if use_dev_keys == True:
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

        

    
    # if red glasses on / in fire
    #add "#FF0000" alpha 0.2
    
    #if underwater
    #add "#0000FF" alpha 0.2
    #add "#0000FF" alpha 0.1

    


    




screen superdev():
    zorder 2000
    
    if superdev == True:
        # show mouse position for devs
        text "[mousepos]" at left
        
        # move engine values
        text "exitpos: [exitpos]\nstartpos: [startpos]\ngotopos: [gotopos]\nmoving: [moving]\nshippos: [shippos]\n\n" at right
        
        # surface values
        #text "shippos [shippos]  - maplink [maplink] - ingame [ingame]" at center
        text "engine: [engine] - pnc_nodes_visible: [pnc_nodes_visible]\n\n" at center

        
        # inventory values
        text "         inv_select: [inventory_select] - inv_notify: [inventory_notify] - planet: [planet] \n         nodes: [spacenetnodes]\n         liftpos: [liftpos] - isc_spaceship_interchange: [isc_spaceship_interchange]" at topleft
        
        # mousepos
        timer 0.1 repeat True action [SetVariable("mousepos", renpy.get_mouse_pos())] # original for pc
        #$ mousepos = renpy.get_mouse_pos()
        
        
        # show click position
        if renpy.variant("touch"):
            add "images/target.png":
                anchor (0.5,0.5)
                pos mousepos
            
        
        # copy mouse position to clipboard
        key "c" action [Function(copytext, t=str(mousepos)), Notify("Mouse position copied to clipboard!")]
        
        
        #text "pnc_nodes_visible: [pnc_nodes_visible]\n\n\n" at center
        

        
    

init:
    $ nodeclicksize = 40
    
   

screen setpos():
    zorder 100
    # get every 0.1 sec mouse position
    timer 0.1 repeat True action [SetVariable("mousepos", renpy.get_mouse_pos())] # original for pc
    #$ mousepos = renpy.get_mouse_pos()
    

    
    
    if (nodeA[0]-nodeclicksize ) < (mousepos[0]) < (nodeA[0]+nodeclicksize) and (nodeA[1]-nodeclicksize ) < (mousepos[1]) < (nodeA[1]+nodeclicksize):
        timer 0.1 repeat True action [SetVariable("gotopos", 1)]
        if superdev == True:
            text "A"
                
        if pnc_nodes_visible == True and renpy.showing("pathnodeA") == True and not renpy.variant("touch"):
            add "images/node_hover.png":
                alpha 0.5
                anchor (0.5,0.5)
                pos nodeA
                
                

        
    elif (nodeB[0]-nodeclicksize ) < (mousepos[0]) < (nodeB[0]+nodeclicksize) and (nodeB[1]-nodeclicksize ) < (mousepos[1]) < (nodeB[1]+nodeclicksize):
        timer 0.1 repeat True action [SetVariable("gotopos", 2)]
        if superdev == True:
            text "B"
                
        if pnc_nodes_visible == True and renpy.showing("pathnodeB") == True and not renpy.variant("touch"):
            add "images/node_hover.png":
                alpha 0.5
                anchor (0.5,0.5)
                pos nodeB
                
       
                      
        
    elif (nodeC[0]-nodeclicksize ) < (mousepos[0]) < (nodeC[0]+nodeclicksize) and (nodeC[1]-nodeclicksize ) < (mousepos[1]) < (nodeC[1]+nodeclicksize):
        timer 0.1 repeat True action [SetVariable("gotopos", 3)]
        if superdev == True:
            text "C"
                
        if pnc_nodes_visible == True and renpy.showing("pathnodeC") == True and not renpy.variant("touch"):
            add "images/node_hover.png":
                alpha 0.5
                anchor (0.5,0.5)
                pos nodeC
                
        
                
             
    elif (nodeD[0]-nodeclicksize ) < (mousepos[0]) < (nodeD[0]+nodeclicksize) and (nodeD[1]-nodeclicksize ) < (mousepos[1]) < (nodeD[1]+nodeclicksize):
        timer 0.1 repeat True action [SetVariable("gotopos", 4)]
        if superdev == True:
            text "D"
                
        if pnc_nodes_visible == True and renpy.showing("pathnodeD") == True and not renpy.variant("touch"):
            add "images/node_hover.png":
                alpha 0.5
                anchor (0.5,0.5)
                pos nodeD
                
        
       
    ###    

    elif (nodeAA[0]-nodeclicksize ) < (mousepos[0]) < (nodeAA[0]+nodeclicksize) and (nodeAA[1]-nodeclicksize) < (mousepos[1]) < (nodeAA[1]+nodeclicksize):
        timer 0.1 repeat True action [SetVariable("gotopos", 11)]
        if superdev == True:
            text "AA"
                
        if pnc_nodes_visible == True and renpy.showing("pathnodeAA") == True and not renpy.variant("touch"):
            add "images/node_hover.png":
                alpha 0.5
                anchor (0.5,0.5)
                pos nodeAA
                
        

        
    elif (nodeBB[0]-nodeclicksize ) < (mousepos[0]) < (nodeBB[0]+nodeclicksize) and (nodeBB[1]-nodeclicksize ) < (mousepos[1]) < (nodeBB[1]+nodeclicksize):
        timer 0.1 repeat True action [SetVariable("gotopos", 22)]
        if superdev == True:
            text "BB"
                
        if pnc_nodes_visible == True and renpy.showing("pathnodeBB") == True and not renpy.variant("touch"):
            add "images/node_hover.png":
                alpha 0.5
                anchor (0.5,0.5)
                pos nodeBB
                
        
                
            
    elif (nodeCC[0]-nodeclicksize ) < (mousepos[0]) < (nodeCC[0]+nodeclicksize) and (nodeCC[1]-nodeclicksize ) < (mousepos[1]) < (nodeCC[1]+nodeclicksize):
        timer 0.1 repeat True action [SetVariable("gotopos", 33)]
        if superdev == True:
            text "CC"
                
        if pnc_nodes_visible == True and renpy.showing("pathnodeCC") == True and not renpy.variant("touch"):
            add "images/node_hover.png":
                alpha 0.5
                anchor (0.5,0.5)
                pos nodeCC
                
        
        
    elif (nodeDD[0]-nodeclicksize ) < (mousepos[0]) < (nodeDD[0]+nodeclicksize) and (nodeDD[1]-nodeclicksize ) < (mousepos[1]) < (nodeDD[1]+nodeclicksize):
        timer 0.1 repeat True action [SetVariable("gotopos", 44)]
        if superdev == True:
            text "DD"
                
        if pnc_nodes_visible == True and renpy.showing("pathnodeDD") == True and not renpy.variant("touch"):
            add "images/node_hover.png":
                alpha 0.5
                anchor (0.5,0.5)
                pos nodeDD
                
      
            
    ###
            
    else:
        timer 0.1 repeat True action [SetVariable("gotopos", 0)]
        if superdev == True:
            text "NoMove"
            

            

        
        
        
        
