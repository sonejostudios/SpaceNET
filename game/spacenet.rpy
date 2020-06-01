#SpaceNET

######################################################

label spacenet_comp(snetnode):
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
    
        
        call sound_beep
        call nodes_list_update
        
        $ showtext = """
    SpaceNET
    [ascii_line]
    
    Node Name : [snetnode]
    
    State : [node_state]
    """
        
        show text Text(showtext,text_align=termtext_align) at termtextpos
        
        
        menu:
            "Insert" if inventory_select != "spacenet":
                if inventory_select != "spacenet":
                        if inventory_select == "":
                            m "I have nothing to insert into this computer! {w=2.5} {nw}"
                        else:
                            $ inventory_select = ""
                            call dialog_nosense
                            
            "Install Software" if inventory_select == "spacenet" and spacenet_copied == False:
                call use_and_keep_item
                call sound_electroshock
                with hpunch
                m "The disk is empty, there is nothing to install! {w=3} {nw}"
                                
            
            "Install SpaceNET Software" if inventory_select == "spacenet" and spacenet_copied == True:
                call use_and_keep_item
                $ inventory_select = ""
                call server_progressbar
                with flash
                #$ inventory_select = ""
                
                $ showtext ="""
    SpaceNET
    [ascii_line]
    
    Install sucessfull.
    
    The SpaceNET software is now installed
    and ready to use.
    
    Please wait until it connects itself 
    to the network.
    
    """
                show text Text(showtext,text_align=termtext_align) at termtextpos
                
                pause 7
                    
                call sound_modem
                call server_progressbar
                
                if snetnode not in spacenetnodes:
                    $ spacenetnodes.append(snetnode)
                    
                    
        
                call sound_connected
                with flash
                
                $ showtext ="""
    SpaceNET
    [ascii_line]
    
    Node connection successful!
    
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
                    "back":
                        pass

            "Info":
                $ showtext = """
    SpaceNET
    [ascii_line]
    
    To install or update a software, 
    please insert the medium.
    
    For more information about the 
    SpaceNET network, please type "spacenet" 
    in the terminal.
    """
        
                show text Text(showtext,text_align=termtext_align) at termtextpos
                menu:
                    "back":
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
    
    

