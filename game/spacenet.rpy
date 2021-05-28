#SpaceNET

######################################################

label spacenet_comp(snetnode):
    $ engine = "terminal"
    $ pnc_nodes_visible = False
    
    show terminal at topleft
    
    hide spacenetsender
    
    if shadow_enable == 1:
        show shadow:
            pos (270, 240)
    


    while True:    
        
        # update current node state
        if snetnode in spacenetnodes:
            $ node_state = "active"
        else:
            $ node_state = "inactive"
    
        
        call sound_beep from _call_sound_beep_39
        call nodes_list_update from _call_nodes_list_update_1
        
        $ showtext = """
    SpaceNET
    [ascii_line]
    
    Node name: [snetnode]
    
    State: [node_state]
    """
        
        show text Text(showtext,text_align=termtext_align) at termtextpos
        
        
        menu:
            "Insert" if inventory_select != "spacenet":
                if inventory_select != "spacenet":
                    if inventory_select == "":
                        m "I have nothing to insert into this computer! {w=3.5} {nw}"
                    else:
                        $ inventory_select = ""
                        call dialog_nosense from _call_dialog_nosense_19
                            
            "Install Software" if inventory_select == "spacenet" and spacenet_copied == False:
                call use_and_keep_item from _call_use_and_keep_item_27
                call sound_electroshock from _call_sound_electroshock_20
                with hpunch
                m "The disk is empty, there is nothing to install! {w=3} {nw}"
                                
            
            "Install SpaceNET Software" if inventory_select == "spacenet" and spacenet_copied == True:
                if snetnode in spacenetnodes:
                    m "The SpaceNET software is already installed on this computer! {w=3.5} {nw}"
                    m "I should better do something else. {w=2.5} {nw}"
                    $ inventory_select = ""
                    return
                    
                call use_and_keep_item from _call_use_and_keep_item_28
                call sound_collect from _call_sound_collect_2
                $ inventory_select = ""
                call server_progressbar from _call_server_progressbar_12
                with flash
                
                $ showtext ="""
    SpaceNET
    [ascii_line]
    
    Install successfull.
    
    The SpaceNET software is now installed
    and ready to use.
    
    Please wait until it connects itself 
    to the network.
    
    """
                show text Text(showtext,text_align=termtext_align) at termtextpos
                
                pause 7
                    
                call sound_modem from _call_sound_modem_1
                call server_progressbar from _call_server_progressbar_13
                
                if snetnode not in spacenetnodes:
                    $ spacenetnodes.append(snetnode)
                    
                    
        
                call sound_connected from _call_sound_connected_37
                with flash
                
                $ showtext ="""
    SpaceNET
    [ascii_line]
    
    The node connection was successful!
    
    This SpaceNET node is now connected
    and ready to use.

    
    """
                show text Text(showtext,text_align=termtext_align) at termtextpos
                
                pause 5

                
            "Active Nodes":
                $ showtext = """
    SpaceNET
    [ascii_line]
    
    The following nodes are active ([active_nodes_amount]):
    
    [spacenetnodes_text]
    """
        
                show text Text(showtext,text_align=termtext_align) at termtextpos
                menu:
                    "Back":
                        pass

            "Info":
                $ showtext = """
    SpaceNET
    [ascii_line]
    
    To install or update software, 
    please insert the medium.
    
    For more information about the 
    SpaceNET network, please type 'spacenet' 
    in the terminal.
    """
        
                show text Text(showtext,text_align=termtext_align) at termtextpos
                menu:
                    "Back":
                        pass
            
            
                
            "Exit":
                $ pnc_nodes_visible = True
                return
        #return
        
        
    
    
label nodes_list_update:
    #$ spacenetnodes.append("xylo_village2")
    
    # update node list text
    $ spacenetnodes_text = ""
    python:
        for x in range(len(spacenetnodes)):
            spacenetnodes_text += str(x+1) + " - " + spacenetnodes[x] + "\n    "
    
    
    # update node amount
    $ active_nodes_amount = len(spacenetnodes)
    
    return
    
    

