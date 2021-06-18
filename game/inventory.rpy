#$ items.append("apple")
#$ items.remove("apple")
#$ apples = items.count("apple")


init:
    $ item_info = ""
    
    $ inventory_dir = "images/inventory/"
    
    default notebook_notes = []
    $ notebook_text = ""
    $ notebook_count = 0
    
    $ spacenet_copied = False
    
    $ inventory_visible = False
    
    
    $ item_name_dict = {"":"",
    "newspaper": "newspaper",
    "screwdriver": "screwdriver",
    "spacesuit": "spacesuit",
    "flashlight": "flashlight",
    "cable": "electric cable",
    "bulb": "light bulb",
    "mirror": "mirror",

    "spacenet": "computer disk",
    
    "accesscard": "access card",
    "rope": "rope",
    "pick": "pick",
    "shovel": "shovel",
    "dynamite": "dynamite",
    "minidroid": "minidroid",
    
    "gem": "gems",
    
    "star": "star",
    "notebook": "notebook",
    "laser": "laser tool",
    "key": "old key",
    "letter": "letter",
    "hook": "safety hook",
    "magnet": "magnet",
    "robotcard": "robot ID card",
    "knife": "knife",
    "cards": "card game",
    "module": "hyperspace module",
    "cord": "cord",
    "magnetcord": "cord with a magnet",
    "asteroid": "asteroid piece" }
    
    
    
    

screen inventory():
    zorder 91
    modal True
    
    # hide inventory shortcut
    #key "i" action Show("selected_item"), Hide("inventory")#i, SetVariable("inventory_select", "")
    key "mousedown_3" action Show("selected_item"), Hide("inventory")
    
    
    # inventory select up
    key 'mousedown_5':
        if inventory_select_number < len(inventory)-1:
            action SetVariable("inventory_select_number", inventory_select_number+1), SetVariable("inventory_select", inventory[inventory_select_number+1]), Hide("selected_item")

    # inventory select down
    key 'mousedown_4':
        if inventory_select_number > 0:
            action SetVariable("inventory_select_number", inventory_select_number-1), SetVariable("inventory_select", inventory[inventory_select_number-1]), Hide("selected_item")
        else:
            action SetVariable("inventory_select_number", -1), SetVariable("inventory_select", ""), Hide("selected_item")
    
    
    #timer 1:
    #    action Hide("selected_item")
    

    
    imagebutton: 
        idle "images/inventory/inventory.png"
        action Show("selected_item"), Hide("inventory"), SetVariable("inventory_select", "")
            
    
    
    
    if superdev == True:
        text "\n[inventory]":
            ypos 280
            


    hbox:
        pos (60,65)
        xmaximum 720
        box_wrap True
        
        for i in range(len(inventory)):
            $ inventory_item = inventory[i]
            
            if inventory_item == "newspaper":
                imagebutton idle inventory_dir + "newspaper_idle.png" selected_idle inventory_dir + "newspaper_selected_idle.png" selected_hover inventory_dir + "newspaper_selected_idle.png":
                    if inventory_select != "newspaper":
                        action SelectedIf(inventory_select == "newspaper"), SetVariable("inventory_select", "newspaper")
                    else:
                        action SelectedIf(inventory_select == "newspaper"), Hide("selected_item"), Show("selected_item"), Hide("inventory")
                        
                    
            if inventory_item == "screwdriver":
                imagebutton idle inventory_dir + "screwdriver_idle.png" selected_idle inventory_dir + "screwdriver_selected_idle.png" selected_hover inventory_dir + "screwdriver_selected_idle.png":
                    if inventory_select != "screwdriver":
                        action SelectedIf(inventory_select == "screwdriver"), SetVariable("inventory_select", "screwdriver")
                    else:
                        action SelectedIf(inventory_select == "screwdriver"), Hide("selected_item"), Show("selected_item"), Hide("inventory")

            
            if inventory_item == "spacesuit":
                imagebutton idle inventory_dir + "spacesuit_idle.png" selected_idle inventory_dir + "spacesuit_selected_idle.png" selected_hover inventory_dir + "spacesuit_selected_idle.png":
                    if inventory_select != "spacesuit":
                        action SelectedIf(inventory_select == "spacesuit"), SetVariable("inventory_select", "spacesuit")
                    else:
                        action SelectedIf(inventory_select == "spacesuit"), Hide("selected_item"), Show("selected_item"), Hide("inventory")


            if inventory_item == "flashlight":
                imagebutton idle inventory_dir + "flashlight_idle.png" selected_idle inventory_dir + "flashlight_selected_idle.png" selected_hover inventory_dir + "flashlight_selected_idle.png":
                    if inventory_select != "flashlight":
                        action SelectedIf(inventory_select == "flashlight"), SetVariable("inventory_select", "flashlight")
                    else:
                        action SelectedIf(inventory_select == "flashlight"), Hide("selected_item"), Show("selected_item"), Hide("inventory")
 
 
            if inventory_item == "cable":
                imagebutton idle inventory_dir + "cable_idle.png" selected_idle inventory_dir + "cable_selected_idle.png" selected_hover inventory_dir + "cable_selected_idle.png":
                    if inventory_select != "cable":
                        action SelectedIf(inventory_select == "cable"), SetVariable("inventory_select", "cable")
                    else:
                        action SelectedIf(inventory_select == "cable"), Hide("selected_item"), Show("selected_item"), Hide("inventory")
      
      
            if inventory_item == "bulb":
                imagebutton idle inventory_dir + "bulb_idle.png" selected_idle inventory_dir + "bulb_selected_idle.png" selected_hover inventory_dir + "bulb_selected_idle.png":
                    if inventory_select != "bulb":
                        action SelectedIf(inventory_select == "bulb"), SetVariable("inventory_select", "bulb")
                    else:
                        action SelectedIf(inventory_select == "bulb"), Hide("selected_item"), Show("selected_item"), Hide("inventory")
      
      
            if inventory_item == "mirror":
                imagebutton idle inventory_dir + "mirror_idle.png" selected_idle inventory_dir + "mirror_selected_idle.png" selected_hover inventory_dir + "mirror_selected_idle.png":
                    if inventory_select != "mirror":
                        action SelectedIf(inventory_select == "mirror"), SetVariable("inventory_select", "mirror")
                    else:
                        action SelectedIf(inventory_select == "mirror"), Hide("selected_item"), Show("selected_item"), Hide("inventory")
      
      
            if inventory_item == "spacenet":
                imagebutton idle inventory_dir + "spacenet_idle.png" selected_idle inventory_dir + "spacenet_selected_idle.png" selected_hover inventory_dir + "spacenet_selected_idle.png":
                    if inventory_select != "spacenet":
                        if spacenet_copied == True:
                            action SelectedIf(inventory_select == "spacenet"), SetVariable("inventory_select", "spacenet")
                        else:
                            action SelectedIf(inventory_select == "spacenet"), SetVariable("inventory_select", "spacenet")
                    else:
                        action SelectedIf(inventory_select == "spacenet"), Hide("selected_item"), Show("selected_item"), Hide("inventory")
       
       
            if inventory_item == "accesscard":
                imagebutton idle inventory_dir + "accesscard_idle.png" selected_idle inventory_dir + "accesscard_selected_idle.png" selected_hover inventory_dir + "accesscard_selected_idle.png":
                    if inventory_select != "accesscard":
                        action SelectedIf(inventory_select == "accesscard"), SetVariable("inventory_select", "accesscard")
                    else:
                        action SelectedIf(inventory_select == "accesscard"), Hide("selected_item"), Show("selected_item"), Hide("inventory")
      
      
            if inventory_item == "rope":
                imagebutton idle inventory_dir + "rope_idle.png" selected_idle inventory_dir + "rope_selected_idle.png" selected_hover inventory_dir + "rope_selected_idle.png":
                    if inventory_select != "rope":
                        action SelectedIf(inventory_select == "rope"), SetVariable("inventory_select", "rope")
                    else:
                        action SelectedIf(inventory_select == "rope"), Hide("selected_item"), Show("selected_item"), Hide("inventory")
                   
                    
            if inventory_item == "pick":
                imagebutton idle inventory_dir + "pick_idle.png" selected_idle inventory_dir + "pick_selected_idle.png" selected_hover inventory_dir + "pick_selected_idle.png":
                    if inventory_select != "pick":
                        action SelectedIf(inventory_select == "pick"), SetVariable("inventory_select", "pick")
                    else:
                        action SelectedIf(inventory_select == "pick"), Hide("selected_item"), Show("selected_item"), Hide("inventory")
                  
            if inventory_item == "shovel":
                imagebutton idle inventory_dir + "shovel_idle.png" selected_idle inventory_dir + "shovel_selected_idle.png" selected_hover inventory_dir + "shovel_selected_idle.png":
                    if inventory_select != "shovel":
                        action SelectedIf(inventory_select == "shovel"), SetVariable("inventory_select", "shovel")
                    else:
                        action SelectedIf(inventory_select == "shovel"), Hide("selected_item"), Show("selected_item"), Hide("inventory")        
            
            
            if inventory_item == "dynamite":
                imagebutton idle inventory_dir + "dynamite_idle.png" selected_idle inventory_dir + "dynamite_selected_idle.png" selected_hover inventory_dir + "dynamite_selected_idle.png":
                    if inventory_select != "dynamite":
                        action SelectedIf(inventory_select == "dynamite"), SetVariable("inventory_select", "dynamite")
                    else:
                        action SelectedIf(inventory_select == "dynamite"), Hide("selected_item"), Show("selected_item"), Hide("inventory")
     
     
            if inventory_item == "minidroid":
                imagebutton idle inventory_dir + "minidroid_idle.png" selected_idle inventory_dir + "minidroid_selected_idle.png" selected_hover inventory_dir + "minidroid_selected_idle.png":
                    if inventory_select != "minidroid":
                        action SelectedIf(inventory_select == "minidroid"), SetVariable("inventory_select", "minidroid")
                    else:
                        action SelectedIf(inventory_select == "minidroid"), Hide("selected_item"), Show("selected_item"), Hide("inventory")
                    
                    
            if inventory_item == "gem" and gems > 0:
                fixed:
                    xmaximum 75
                    ymaximum 75
                    imagebutton idle inventory_dir + "gem_idle.png" selected_idle inventory_dir + "gem_selected_idle.png" selected_hover inventory_dir + "gem_selected_idle.png":
                        if inventory_select != "gem":
                            action SelectedIf(inventory_select == "gem"), SetVariable("inventory_select", "gem")
                        else:
                            action SelectedIf(inventory_select == "gem"), Hide("selected_item"), Show("selected_item"), Hide("inventory")
                    text "{color=#8dd35f}{size=11}[gems]/[maxgems]":
                        anchor (1.0,1.0)
                        pos (0.95,0.95)
                        
            
            
                        
                        
                        
       
            if inventory_item == "star":
                imagebutton idle inventory_dir + "star_idle.png" selected_idle inventory_dir + "star_selected_idle.png" selected_hover inventory_dir + "star_selected_idle.png":
                    if inventory_select != "star":
                        action SelectedIf(inventory_select == "star"), SetVariable("inventory_select", "star")
                    else:
                        action SelectedIf(inventory_select == "star"), Hide("selected_item"), Show("selected_item"), Hide("inventory")
                
            
            if inventory_item == "notebook":
                imagebutton idle inventory_dir + "notebook_idle.png" selected_idle inventory_dir + "notebook_selected_idle.png" selected_hover inventory_dir + "notebook_selected_idle.png":
                    if inventory_select != "notebook":
                        action SelectedIf(inventory_select == "notebook"), SetVariable("inventory_select", "notebook")
                    else:
                        #action SelectedIf(inventory_select == "notebook"), Hide("selected_item"), Show("selected_item"), Hide("inventory")
                        action SelectedIf(inventory_select == "notebook"), Show("notebook_screen"), Hide("inventory") 
                        
            
            if inventory_item == "laser":
                imagebutton idle inventory_dir + "laser_idle.png" selected_idle inventory_dir + "laser_selected_idle.png" selected_hover inventory_dir + "laser_selected_idle.png":
                    if inventory_select != "laser":
                        action SelectedIf(inventory_select == "laser"), SetVariable("inventory_select", "laser")
                    else:
                        action SelectedIf(inventory_select == "laser"), Hide("selected_item"), Show("selected_item"), Hide("inventory")
                        
            
            if inventory_item == "key":
                imagebutton idle inventory_dir + "key_idle.png" selected_idle inventory_dir + "key_selected_idle.png" selected_hover inventory_dir + "key_selected_idle.png":
                    if inventory_select != "key":
                        action SelectedIf(inventory_select == "key"), SetVariable("inventory_select", "key")
                    else:
                        action SelectedIf(inventory_select == "key"), Hide("selected_item"), Show("selected_item"), Hide("inventory")
            
            
            if inventory_item == "letter":
                imagebutton idle inventory_dir + "letter_idle.png" selected_idle inventory_dir + "letter_selected_idle.png" selected_hover inventory_dir + "letter_selected_idle.png":
                    if inventory_select != "letter":
                        action SelectedIf(inventory_select == "letter"), SetVariable("inventory_select", "letter")
                    else:
                        action SelectedIf(inventory_select == "letter"), Hide("selected_item"), Show("selected_item"), Hide("inventory")
                        #action SelectedIf(inventory_select == "letter"), Show("letter_screen"), Hide("selected_item"), Show("selected_item"), Hide("inventory")
                     
                     
                        
            if inventory_item == "hook":
                imagebutton idle inventory_dir + "hook_idle.png" selected_idle inventory_dir + "hook_selected_idle.png" selected_hover inventory_dir + "hook_selected_idle.png":
                    if inventory_select != "hook":
                        action SelectedIf(inventory_select == "hook"), SetVariable("inventory_select", "hook")
                    else:
                        action SelectedIf(inventory_select == "hook"), Hide("selected_item"), Show("selected_item"), Hide("inventory")
                        
            if inventory_item == "magnet":
                imagebutton idle inventory_dir + "magnet_idle.png" selected_idle inventory_dir + "magnet_selected_idle.png" selected_hover inventory_dir + "magnet_selected_idle.png":
                    if inventory_select != "magnet":
                        action SelectedIf(inventory_select == "magnet"), SetVariable("inventory_select", "magnet")
                    else:
                        action SelectedIf(inventory_select == "magnet"), Hide("selected_item"), Show("selected_item"), Hide("inventory")
                        
                        
            if inventory_item == "robotcard":
                imagebutton idle inventory_dir + "robotcard_idle.png" selected_idle inventory_dir + "robotcard_selected_idle.png" selected_hover inventory_dir + "robotcard_selected_idle.png":
                    if inventory_select != "robotcard":
                        action SelectedIf(inventory_select == "robotcard"), SetVariable("inventory_select", "robotcard")
                    else:
                        action SelectedIf(inventory_select == "robotcard"), Hide("selected_item"), Show("selected_item"), Hide("inventory")
                        
            if inventory_item == "knife":
                imagebutton idle inventory_dir + "knife_idle.png" selected_idle inventory_dir + "knife_selected_idle.png" selected_hover inventory_dir + "knife_selected_idle.png":
                    if inventory_select != "knife":
                        action SelectedIf(inventory_select == "knife"), SetVariable("inventory_select", "knife")
                    else:
                        action SelectedIf(inventory_select == "knife"), Hide("selected_item"), Show("selected_item"), Hide("inventory")
                        
            if inventory_item == "cards":
                imagebutton idle inventory_dir + "cards_idle.png" selected_idle inventory_dir + "cards_selected_idle.png" selected_hover inventory_dir + "cards_selected_idle.png":
                    if inventory_select != "cards":
                        action SelectedIf(inventory_select == "cards"), SetVariable("inventory_select", "cards")
                    else:
                        action SelectedIf(inventory_select == "cards"), Hide("selected_item"), Show("selected_item"), Hide("inventory")
                        
                        
                        
            if inventory_item == "module":
                imagebutton idle inventory_dir + "module_idle.png" selected_idle inventory_dir + "module_selected_idle.png" selected_hover inventory_dir + "module_selected_idle.png":
                    if inventory_select != "module":
                        action SelectedIf(inventory_select == "module"), SetVariable("inventory_select", "module")
                    else:
                        action SelectedIf(inventory_select == "module"), Hide("selected_item"), Show("selected_item"), Hide("inventory")
                        
                        
            if inventory_item == "cord":
                imagebutton idle inventory_dir + "cord_idle.png" selected_idle inventory_dir + "cord_selected_idle.png" selected_hover inventory_dir + "cord_selected_idle.png":
                    if inventory_select != "cord":
                        action SelectedIf(inventory_select == "cord"), SetVariable("inventory_select", "cord")
                    else:
                        action SelectedIf(inventory_select == "cord"), Hide("selected_item"), Show("selected_item"), Hide("inventory")
                        
                        
            if inventory_item == "magnetcord":
                imagebutton idle inventory_dir + "magnetcord_idle.png" selected_idle inventory_dir + "magnetcord_selected_idle.png" selected_hover inventory_dir + "magnetcord_selected_idle.png":
                    if inventory_select != "magnetcord":
                        action SelectedIf(inventory_select == "magnetcord"), SetVariable("inventory_select", "magnetcord")
                    else:
                        action SelectedIf(inventory_select == "magnetcord"), Hide("selected_item"), Show("selected_item"), Hide("inventory")
                        
                        
            if inventory_item == "asteroid":
                imagebutton idle inventory_dir + "asteroid_idle.png" selected_idle inventory_dir + "asteroid_selected_idle.png" selected_hover inventory_dir + "asteroid_selected_idle.png":
                    if inventory_select != "asteroid":
                        action SelectedIf(inventory_select == "asteroid"), SetVariable("inventory_select", "asteroid")
                    else:
                        action SelectedIf(inventory_select == "asteroid"), Hide("selected_item"), Show("selected_item"), Hide("inventory")
                
            
    
    
    
    #item info
    $ item_info_dict = {"":"",
    "newspaper": "This is an old newspaper.\nNothing interesting inside.",
    "screwdriver": "This is a very good screwdriver.\nI stole it from a robot.",
    "spacesuit": "This is a space suit.\nI'll need it to breathe in space.",
    "flashlight": "This is a flashlight.\nIt could be useful in dark rooms.",
    "cable": "This is a piece of electric cable.\nIt could be useful.",
    "bulb": "This is a light bulb.\nWhy do I need it?",
    "mirror": "This is a small mirror.\nI look good!",

    "spacenet": "This is a computer disk.\nIt seems to be empty.",
    
    "accesscard": "This is an access card.\nIt has A.R.K. Corporation written on it.",
    "rope": "This is a big rope.\nI'm sure I'll need it soon.",
    "pick": "This is a pick.\nHandy to break big stones.",
    "shovel": "This is a shovel.\nGood for digging.",
    "dynamite": "This is a stick of dynamite!\nI should be careful with it.",
    "minidroid": "This is a remote-controlled minidroid.\nIt is great to explore dangerous or narrow places.",
    
    "gem": "These are some precious gems.\nI've got [gems] out of [maxgems] gems.",
    
    "star": "This is the star of the Rebel Alliance.\nI need it to identify myself.",
    "notebook": "This is a notebook.\nI can write notes and reminders in it.",
    "laser": "This is a small but powerful laser tool.\nPerfect for cutting hard materials.",
    "key": "This is an old key.\nI don't think it is for a regular door.",
    "letter": "This is a simple old-school letter.\nIt is sealed.",
    "hook": "This is a safety hook.\nI'll need it if I want to climb somewhere.",
    "magnet": "This is a pretty strong magnet.\nIt could be useful.",
    "robotcard": "This is an ID card of a crew robot.\nIt has holes in it.",
    "knife": "This is a knife.\nIt is really sharp!",
    "cards": "This is a card game.\nNice to have it!",
    "module": "This is the hyperspace module of a spaceship.\nI guess it is from the spaceship wreck.",
    "cord": "This is a thin cord.\nI'm sure it will be useful.",
    "magnetcord": "This is a thin cord with a magnet.\nGreat tool for fishing metal things.",
    "asteroid": "This is a tiny piece of an asteroid.\nNice souvenir." }
    

    # change spacenet item info if copied to disk
    if spacenet_copied == True:
        $ item_info_dict["spacenet"] = "This is the spaceNET software.\nI should install it on the computer nodes."
    
    # change gem to singular if only one
    if gems == 1:
        $ item_info_dict["gem"] = "It is a precious gem.\nI've got [gems] out of [maxgems] gems."
    
    
    
    # set info
    #timer 0.1 repeat True action SetVariable("item_info", item_info_dict[inventory_select])
    
    
    # show info
    #if inventory_select != "":
    #text item_info:
    #    pos (80,380)
        

    
    #set and show item info
    if len(inventory) == 0:
        $ item_info = "My inventory is empty..."
    else:
        $ item_info = item_info_dict[inventory_select]
    
    text item_info:
        pos (80,380)
        
        
    # set pnc_nodes_visible for pnc mode and highlights
    on "show" action SetVariable("inventory_visible", True)
    on "hide" action SetVariable("inventory_visible", False)
    
    
    if engine == "move":
        on "show" action SetVariable("pnc_nodes_visible", False)
        on "hide" action SetVariable("pnc_nodes_visible", True)
        
        on "replace" action SetVariable("pnc_nodes_visible", False)
        on "replaced" action SetVariable("pnc_nodes_visible", False)

        




# show which item is selected on main screen
screen selected_item():
    zorder 100
    
    if inventory_select != "":
        add "images/inventory/[inventory_select]_idle.png": 
            pos (0,0)
        


label get_item(i):
    if i not in inventory:
        $ inventory_select = i
        $ inventory.append(i)
        call sound_collect from _call_sound_collect_4
        call inventory_notify from _call_inventory_notify_1
        with flash
    return
   
        
label take_item(i):
    menu:
        "Take it":
            call get_item(i) from _call_get_item_1
        "Leave it":
            return
    return
    

    
label take_gem:
    m "There is a gem! {w=2} {nw}"

    if "gem" not in inventory:
        $ inventory.append("gem")
    
    $ gems += 1
    $ inventory_select = "gem"
    call sound_collect from _call_sound_collect_5
    call inventory_notify from _call_inventory_notify_2
    with flash
    m "Gem(s): [gems]/[maxgems] {w=2} {nw}"
    
    if gems == maxgems:
        m "...{w=1.5}{nw}"
        m "Now I've got all [maxgems] gems...{w=2.5} Nice one!{w=2}{nw}"
        m "Maybe I should go back to the Zen Master...{w=4.5}{nw}"

    
    return
    



label use_item:
    if inventory_select in inventory:
        $ inventory.remove(inventory_select)
        call sound_connected from _call_sound_connected_33
        #with flash
        call inventory_notify from _call_inventory_notify_3
    
    return
    
    
label use_and_keep_item:
    #call sound_connected
    if inventory_select != "":
        call inventory_notify from _call_inventory_notify_4
    
    return



label inventory_notify:
    $ inventory_notify = inventory_select
    show screen notify("{image=images/inventory/[inventory_notify]_idle.png}")
    $ inventory_select = ""
    return
    


# buy item
label buy_item(i, y):
    if i not in inventory:
            if coins >= y:
                m "I take the [i] for [y]c. {w=2.0} {nw}"
                $ inventory_select = i
                $ inventory.append(i)
                #call sound_collect
                call inventory_notify from _call_inventory_notify_5
                #with flash
                
                #$ coins -= y
                
                call io_cash(-y) from _call_io_cash_14
            
            else:
                m "Here, [coins]c, that's all I have. {w=2.5} {nw}"
                vendor "Sorry, but that's not enough... {w=2.5} {nw}"
                m "Okay, bye! {w=2} {nw}"
                vendor "See you soon! {w=2.5} {nw}"
    
    else:
        m "I have already one. {w=1.5} {nw}"
        

    return
    
    

# cash
label io_cash(x):
    
    call sound_collect from _call_sound_collect_6
    with flash
    
    $ coins += x
    
    
    if x < 0:
        show text "{size=18}[x]{/size}" as textcoins:
            pos position
            linear 2 pos (position[0],position[1]-100) alpha 0.0
        
    else:    
        show text "{size=18}+[x]{/size}" as textcoins:
            pos position
            linear 2 pos (position[0],position[1]-100) alpha 0.0
    
    #m "I found [x] cash !"
    pause 2
    hide textcoins
    
    return




# notebook
screen notebook_screen() zorder 100:
    
    if notebook_count < len(notebook_notes):
        for i in notebook_notes:
            $ notebook_text += i + "\n"
            $ notebook_count += 1
    
    add "#112119"
    
    imagebutton: 
        idle "images/maps/bg.png" 
        action Hide("notebook_screen")
            
    #add "images/infopanel.png"
    add "images/terminal.png" xpos 120
    
    text "notebook\n[ascii_line]\n\n[notebook_text]" xanchor 0.5 pos (400,60) text_align 0.5
    
    if shadow_enable == 1:
        add "images/shadow.png" align (0.5,0.5)
                
      
      
      
      
# notes      
label add_note(i):
    if "notebook" in inventory:
        if i not in notebook_notes:
            $ notebook_notes.append(i)
            m "This is an interesting information... {w=2}{nw}"
            m "I'll write it down!{w=2}{nw}"
            
            $ inventory_select = "notebook"
            call inventory_notify from _call_inventory_notify_6
            
            call sound_collect from _call_sound_collect_7
            with flash
    else:
        m "This is an interesting information, but unfortunately, I have nothing to write it down...{w=5}{nw}"
    
    return

    
label remove_note(i):
    if i in notebook_notes:
            $ notebook_notes.remove(i)
    return




# removable notes
init:
    $ sam_hacker_meeting_text_workaround = "Meet 4n0nym0u5 in space around " + str(hacker_pos)
    $ note_locate_asteroids = "Terminal: locate asteroids"
    $ note_locate_isc = "Terminal: locate isc"
    $ note_locate_cargo = "Terminal: locate cargo"
    

 
 
 
 
 
 
 
 

