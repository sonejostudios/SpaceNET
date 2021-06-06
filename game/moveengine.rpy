
# SpaceNET MOVE ENGINE
# Call it from a map


init:
    $ moving_speed = 0.5




label startpos:

    show player

    
    if startpos == 1:
        jump positionA
        
    if startpos == 2:
        jump positionB
        
    if startpos == 3:
        jump positionC
        
    if startpos == 4:
        jump positionD   
    


    if startpos == 11:
        jump positionAA
        
    if startpos == 22:
        jump positionBB
        
    if startpos == 33:
        jump positionCC
        
    if startpos == 44:
        jump positionDD
        
    
    return


    
label positionA:
    
    $ position = nodeA
    
    show player:
        pos nodeA
    
    $ path = pathA
    call place from _call_place
    call hidepaths from _call_hidepaths_1
    
    jump clickngo      
    jump positionA
            
            
label positionB:

    $ position = nodeB

    show player:
        pos nodeB
    
    $ path = pathB
    call place from _call_place_1
    call hidepaths from _call_hidepaths_2
    
    
    jump clickngo
    jump positionB    
    

label positionC:

    $ position = nodeC
    
    show player:
        pos nodeC
    
    $ path = pathC
    call place from _call_place_2
    call hidepaths from _call_hidepaths_3
    
    
    jump clickngo
    jump positionC 
    
    
label positionD:

    $ position = nodeD
    
    show player:
        pos nodeD
    
    $ path = pathD
    call place from _call_place_3
    call hidepaths from _call_hidepaths_4
    
    
    jump clickngo
    jump positionD 
    
    
########

label positionAA:

    $ position = nodeAA
    
    show player:
        pos nodeAA
    
    $ path = pathAA
    call place from _call_place_4
    call hidepaths from _call_hidepaths_5
    
    
    jump clickngo      
    jump positionAA
            
            
label positionBB:

    $ position = nodeBB

    show player:
        pos nodeBB
    
    $ path = pathBB
    call place from _call_place_5
    call hidepaths from _call_hidepaths_6
    
    
    jump clickngo
    jump positionBB 
    

label positionCC:

    $ position = nodeCC
    
    show player:
        pos nodeCC
    
    $ path = pathCC
    call place from _call_place_6
    call hidepaths from _call_hidepaths_7
    
    
    jump clickngo
    jump positionCC
    
    
label positionDD:

    $ position = nodeDD
    
    show player:
        pos nodeDD
    
    $ path = pathDD
    call place from _call_place_7
    call hidepaths from _call_hidepaths_8
    
    
    jump clickngo
    jump positionDD
    

########


label hidepaths:

    if path[0] == (0,0):
        hide textA
    if path[1] == (0,0):
        hide textB
    if path[2] == (0,0):
        hide textC
    if path[3] == (0,0):
        hide textD
    if path[4] == (0,0):
        hide textAA
    if path[5] == (0,0):
        hide textBB
    if path[6] == (0,0):
        hide textCC
    if path[7] == (0,0):
        hide textDD
    
    
    if path[0] == (0,0):
        hide pathnodeA
    if path[1] == (0,0):
        hide pathnodeB
    if path[2] == (0,0):
        hide pathnodeC
    if path[3] == (0,0):
        hide pathnodeD
    if path[4] == (0,0):
        hide pathnodeAA
    if path[5] == (0,0):
        hide pathnodeBB
    if path[6] == (0,0):
        hide pathnodeCC
    if path[7] == (0,0):
        hide pathnodeDD
    

    return


label clickngo:
    
    $ engine = "move"
    
    window hide # hide say window while pausing
    
    if shadow_enable == 1:
        show shadow behind pathnodeA, pathnodeB, pathnodeC, pathnodeD, pathnodeAA, pathnodeBB, pathnodeCC, pathnodeDD, player:
            pos position
    else:
        hide shadow
    
    
    if gotopos != 0:
        $ inventory_select = ""
    


    # unflag moving
    $ moving = False
    
    
    
    
    
    
    
    
    # wait for click to move player to next node
    pause
    
    
    
    



    # flag moving
    if startpos != gotopos:
        $ moving = True    
    
    
    
    if gotopos == 1 and nodeA in path:
        show player:
            ease moving_speed pos path[0]
        if shadow_enable == 1:
            show shadow zorder 1000:
                easein moving_speed pos path[0]
        else:
            hide shadow
        if position != nodeA:
            pause moving_speed
        $ exitpos = 1
        return
            
    if gotopos == 2 and nodeB in path:
        show player:
            ease moving_speed pos path[1]
        if shadow_enable == 1:
            show shadow zorder 1000:
                easein moving_speed pos path[1]
        else:
            hide shadow
        if position != nodeB:
            pause moving_speed
        $ exitpos = 2
        return
            
    if gotopos == 3 and nodeC in path:
        show player:
            easein moving_speed pos path[2]
        if shadow_enable == 1:
            show shadow zorder 1000:
                easein moving_speed pos path[2]
        else:
            hide shadow
        if position != nodeC:
            pause moving_speed
        $ exitpos = 3
        return
            
    if gotopos == 4 and nodeD in path:
        show player:
            easein moving_speed pos path[3]
        if shadow_enable == 1:
            show shadow zorder 1000:
                easein moving_speed pos path[3]
        else:
            hide shadow
        if position != nodeD:
            pause moving_speed
        $ exitpos = 4
        return
        
  #############     
    if gotopos == 11 and nodeAA in path:
        show player:
            easein moving_speed pos path[4]
        if shadow_enable == 1:
            show shadow zorder 1000:
                easein moving_speed pos path[4]
        else:
            hide shadow
        if position != nodeAA:
            pause moving_speed
        $ exitpos = 11
        return
            
    if gotopos == 22 and nodeBB in path:
        show player:
            easein moving_speed pos path[5]
        if shadow_enable == 1:
            show shadow zorder 1000:
                easein moving_speed pos path[5]
        else:
            hide shadow
        if position != nodeBB:
            pause moving_speed
        $ exitpos = 22
        return
            
    if gotopos == 33 and nodeCC in path:
        show player:
            easein moving_speed pos path[6]    
        if shadow_enable == 1:
            show shadow zorder 1000:
                easein moving_speed pos path[6]
        else:
            hide shadow
        if position != nodeCC:
            pause moving_speed
        $ exitpos = 33
        return
            
    if gotopos == 44 and nodeDD in path:
        show player:
            easein moving_speed pos path[7]      
        if shadow_enable == 1:
            show shadow zorder 1000:
                easein moving_speed pos path[7]
        else:
            hide shadow
        if position != nodeDD:
            pause moving_speed
        $ exitpos = 44
        return 

    #"end of clickngo"
    #return
    jump clickngo





label place:
    
    if pnc_mode == False:

        if nodeA in path and renpy.showing("pathnodeA") != True:
            show nodeanime as pathnodeA:
                pos path[0]
            if superdev == True:
                show text "A" as textA:
                    pos path[0]
                
        if nodeB in path and renpy.showing("pathnodeB") != True:
            show nodeanime as pathnodeB:
                pos path[1]
            if superdev == True:
                show text "B" as textB:
                    pos path[1]
        
        if nodeC in path and renpy.showing("pathnodeC") != True:            
            show nodeanime as pathnodeC:
                pos path[2]
            if superdev == True:        
                show text "C" as textC:
                    pos path[2]
        
        if nodeD in path and renpy.showing("pathnodeD") != True:        
            show nodeanime as pathnodeD:
                pos path[3]
            if superdev == True:        
                show text "D" as textD:
                    pos path[3]
                
     ###########           
        if nodeAA in path and renpy.showing("pathnodeAA") != True:
            show nodeanime as pathnodeAA:
                pos nodeAA
            if superdev == True:
                show text "AA" as textAA:
                    pos nodeAA
                
        if nodeBB in path and renpy.showing("pathnodeBB") != True:
            show nodeanime as pathnodeBB:
                pos nodeBB
            if superdev == True:        
                show text "BB" as textBB:
                    pos nodeBB
        
        if nodeCC in path and renpy.showing("pathnodeCC") != True:
            show nodeanime as pathnodeCC:
                pos nodeCC
            if superdev == True: 
                show text "CC" as textCC:
                    pos nodeCC
        
        if nodeDD in path and renpy.showing("pathnodeDD") != True:
            show nodeanime as pathnodeDD:
                pos nodeDD
            if superdev == True: 
                show text "DD" as textDD:
                    pos nodeDD
        
    
    return
    

######################################################


# dark room
# i.e. used in xylo_mine_crossroom1
label darkroom:

    if startpos == 1:
        $ pathA = (nodeA, (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0))
    if startpos == 2:
        $ pathB = ((0, 0), nodeB, (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0))
    if startpos == 3:
        $ pathC = ((0, 0), (0, 0), nodeC, (0, 0), (0, 0), (0, 0), (0, 0), (0, 0))
    if startpos == 4:
        $ pathD = ((0, 0), (0, 0), (0, 0), nodeD, (0, 0), (0, 0), (0, 0), (0, 0))
        
    if startpos == 11:
        $ pathAA = ((0, 0), (0, 0), (0, 0), (0, 0), nodeAA, (0, 0), (0, 0), (0, 0))
    if startpos == 22:
        $ pathBB = ((0, 0), (0, 0), (0, 0), (0, 0), (0, 0), nodeBB, (0, 0), (0, 0))
    if startpos == 33:
        $ pathCC = ((0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), nodeCC, (0, 0))
    if startpos == 44:
        $ pathDD = ((0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), nodeDD)
        
        
    
    show black as darkroombg behind player
    m "There is no light, it is too dark to see anything.{w=3} {nw}"
    
    return






#######################################################

# call centered_text("aaa",2.0)    
label centered_text(centered_text, centered_text_time):
    
    scene bgcolor
    with pixellate
    show shadow at truecenter
    centered "[centered_text] {w=[centered_text_time]} {nw}"
    
    window hide
    
    return



    
