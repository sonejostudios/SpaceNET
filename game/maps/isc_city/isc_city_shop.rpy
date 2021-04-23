# MAPS

############################################
label isc_city_shop:
    
    stop atmo
    call music_shop from _call_music_shop
    
    
    #$ inventory = ["newspaper", "screwdriver", "spacesuit", "flashlight", "bulb", "mirror", "spacenet", "accesscard", "rope", 
    #                    "cable", "pick", "dynamite", "minidroid", "gem", "star", "notebook", "laser", "key", "letter", "hook"]
    
    image isc_city_shop = imagemapsdir + "crossroom.png"
    
    scene bgcolor
    show isc_city_shop at truecenter
    
    if startpos != 11:
        show screen notify("ISC City Shop")
    

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
        
    
    image item_cards = "images/inventory/cards_idle.png"
    show item_cards:
        anchor (0.5,0.5)
        zoom 0.7
        pos (0.4,175)
        
    image item_bulb = "images/inventory/bulb_idle.png"
    show item_bulb:
        anchor (0.5,0.5)
        zoom 0.7
        pos (0.5,175)
        
    image item_hook = "images/inventory/hook_idle.png"
    show item_hook:
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
    $ nodeD = (240, 340)
    

    $ nodeAA = (400, 240)
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


label loop_isc_city_shop:
    
    
    while True:
        # start "move through the map" loop
        call startpos from _call_startpos_58

        # do something at node?
        if exitpos == 1:
            $ startpos = 1 
            
        if exitpos == 2:
            $ startpos = 2
            
        if exitpos == 3:
            $ startpos = 2
            call sound_door from _call_sound_door_127
            jump isc_city_center # out
            
        if exitpos == 4:
            if startpos == 4:
                call isc_city_shop_info from _call_isc_city_shop_info
                
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
                                jump loop_isc_city_shop 
                
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
            call isc_city_shop_vendor from _call_isc_city_shop_vendor
            
            
        if exitpos == 22:
            $ startpos = 22
            
        if exitpos == 33:
            $ startpos = 33
            
        if exitpos == 44:
            $ startpos = 44



    

label isc_city_shop_info:
    
    $ info_panel_symbol = ""
    $ showtext = """
- Industrial Space City Shop -


Today's special prices:

Card game = 15c
Light bulb = 10c
Safety hook = 99c

"""
    call info_panel from _call_info_panel_11 # in animations
    return
    
    




label isc_city_shop_vendor:
    if inventory_select != "":
        call npc_dont_need_item(vendor) from _call_npc_dont_need_item_1
        return
    
    
    vendor "Hello, what do you want to buy?{w=3.0} {nw}"

    menu:
        "Card game\n15c":
            call buy_item("cards", 15) from _call_buy_item
        
        "Light bulb\n10c":
            if isc_crane_repared == True:
                m "This is a stupid idea...{w=2.0} {nw}"
                m "I already bought one and gave it to the system administrator.{w=4} {nw}"
                m "I don't think I will need another one!{w=3.0} {nw}"
            else:    
                call buy_item("bulb", 10) from _call_buy_item_1
        
        "Safety hook\n99c":
            call buy_item("hook", 99) from _call_buy_item_2
        
        "Nothing, thanks.":
            m "Nothing, thanks.{w=2.0} {nw}"
            vendor "Okay!{w=2.0} {nw}"
            vendor "Come back if you need anything.{w=3.0} {nw}"
            
    #show npc:
    #    linear 1 rotate 90
    #pause 1
    
    return
    
    
    
