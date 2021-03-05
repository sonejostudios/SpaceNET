# MAPS

############################################
label xylo_spaceport_hall_store:
    
    stop atmo
    call music_shop from _call_music_shop_1
    
    
    image xylo_spaceport_hall_store = imagemapsdir + "crossroom.png"
    
    scene bgcolor
    show xylo_spaceport_hall_store at truecenter
    
    if startpos != 11:
        show screen notify("xylo's spaceport shop")
    
    show bgcolor behind xylo_spaceport_hall_store
    
    image store_table = "images/storetable.png"
    show store_table:
        anchor (0.5,0.5)
        pos (400, 178)
        
    show npc:
        pos (400, 85)
        rotate 90
        linear 2 pos (500, 85)
        linear 1 rotate 270
        linear 4 pos (300, 85)
        linear 1 rotate 90
        linear 2 pos (400, 85)
        repeat
        
    
    image item_lamp = "images/inventory/lamp_idle.png"
    show item_lamp:
        anchor (0.5,0.5)
        zoom 0.7
        pos (0.4,175)
        
    image item_knife = "images/inventory/knife_idle.png"
    show item_knife:
        anchor (0.5,0.5)
        zoom 0.7
        pos (0.5,175)
        
    image item_mirror = "images/inventory/mirror_idle.png"
    show item_mirror:
        anchor (0.5,0.5)
        zoom 0.7
        pos (0.6,175)
    
    #doors (comment to disable)
    #show doorh as doorA:
    #    pos (400, 55)
    #show doorv as doorB:
    #    pos (587, 240)
    show doorh as doorC:
        pos (400, 427)
    #show doorv as doorD:
    #    pos (215, 240)
    
    
    show buttonscreen:
        anchor (0.5,0.5)
        rotate 90
        pos (218, 340)
    
    
    # set all variables for the map (nodes and path)
    $ nodeA = (400, 75)
    $ nodeB = (570, 240)
    $ nodeC = (400, 405)
    $ nodeD = (242, 340)
    

    $ nodeAA = (400, 242)
    $ nodeBB = (-100, -100)
    $ nodeCC = (-100, -100)
    $ nodeDD = (-100, -100)

    $ pathA = ((0, 0), (0, 0), nodeC, (0, 0), nodeAA, (0, 0), (0, 0), (0, 0))
    $ pathB = ((0, 0), (0, 0), nodeC, (0, 0), nodeAA, (0, 0), (0, 0), (0, 0))
    $ pathC = ((0, 0), (0, 0), nodeC, nodeD, nodeAA, (0, 0), (0, 0), (0, 0))
    $ pathD = ((0, 0), (0, 0), nodeC, nodeD, nodeAA, (0, 0), (0, 0), (0, 0))
     
    $ pathAA = ((0, 0), (0, 0), nodeC, nodeD, nodeAA, (0, 0), (0, 0), (0, 0))
    $ pathBB = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)
    $ pathCC = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)
    $ pathDD = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)


label loop_xylo_spaceport_hall_store:
    
    while True:

        # start "move through the map" loop
        call startpos from _call_startpos_66

        # do something at node?
        if exitpos == 1:
            $ startpos = 1 

            
        if exitpos == 2:
            $ startpos = 2

            
        if exitpos == 3:
            $ startpos = 4
            call sound_door from _call_sound_door_142
            jump xylo_spaceport_hall # out
            
        if exitpos == 4:
            if startpos == 4:
                call xylo_spaceport_shop_info from _call_xylo_spaceport_shop_info
                
                if superdev == 1:
                    while True:
                        menu:
                            "coins + 10":
                                $ coins += 10
                            "coins - 10":
                                $ coins -= 10
                            "coins = 0":
                                $ coins = 0
                            "delete all items":
                                $ inventory = []
                            "exit":
                                jump loop_xylo_spaceport_hall_store 
                
            $ startpos = 4

            

        #exits routing "got to map and set position for next map"
        if exitpos == 11:
            show npc:
                linear 1 rotate 180
                linear 1 pos (400,85)
            
            #if startpos == 11: # vendor
                #call xylo_spaceport_hall_vendor
            #    jump loop_xylo_spaceport_hall_store 
            
            $ startpos = 11
            $ position = nodeAA
            call xylo_spaceport_hall_vendor from _call_xylo_spaceport_hall_vendor
            

            
        if exitpos == 22:
            $ startpos = 22

            
        if exitpos == 33:
            $ startpos = 33

            
        if exitpos == 44:
            $ startpos = 44




    

label xylo_spaceport_shop_info:
    
    $ info_panel_symbol = ""
    $ showtext = """
- Xylo's Spaceport Shop -


Today's special prices:

lamp = 100c
knife = 70c
mirror = 50c

"""
    call info_panel from _call_info_panel_14 # in animations
    return
    
    




label xylo_spaceport_hall_vendor:
    if inventory_select != "":
        $ inventory_select = ""
        vendor "[text_i_dont_need_anything]"
        return
        
    
    if demo_version == True:
        vendor "I'm really sorry, but I'm not allowed to sell you anything in the demo version!{w=6.0} {nw}"
        return
    
    vendor "Hello, what do you want to buy?{w=3.0} {nw}"

    menu:
        #"{image=images/inventory/lamp_idle.png}":
        #    pass
        "lamp\n100c":
            call buy_item("lamp", 100) from _call_buy_item_3
        
        "knife\n70c":
            call buy_item("knife", 70) from _call_buy_item_4
        
        "mirror\n50c":
            if xylo_village_mirror_state == 1:
                m "This is a stupid idea...{w=2.0} {nw}"
                m "I already bought one and used it at the laser fence.{w=3.5} {nw}"
                m "I could just get it back!{w=2.0} {nw}"
            else:
                call buy_item("mirror", 50) from _call_buy_item_5
        
        "nothing, thanks.":
            m "Nothing, thanks.{w=2.0} {nw}"
            vendor "Okay!{w=2.0} {nw}"
            vendor "Come back if you need anything.{w=3.0} {nw}"
            
    #show npc:
    #    linear 1 rotate 90
    #pause 1
    
    return
    
    
    
