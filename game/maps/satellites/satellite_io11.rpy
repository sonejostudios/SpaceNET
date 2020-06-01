# MAPS
############################################

init:
    
    $ io11_remote_control = "disabled" 
    $ io11_pass = "none"
    


label satellite_io11:
    
    $ pnc_nodes_visible = True
    
    stop music fadeout 10.0
    call atmo_spaceship
    
    image satellite_io11 = imagemapsdir + "satellite_map1.png"
    
    scene bgcolor
    call show_space
    show satellite_io11 at inspace_idle
    
    show screen notify("satellite io11")
    
    $ inventory_button = True
    
    #show bgcolor behind satellite_map1
    
    
    # set all variables for the map (nodes and path)
    $ nodeA = (400, 388)
    $ nodeB = (292, 260)
    $ nodeC = (292, 155)
    $ nodeD = (400, 115)

    $ nodeAA = (507, 240)
    $ nodeBB = (41, 436)
    $ nodeCC = (90, 436)
    $ nodeDD = (136, 436)

    $ pathA = (nodeA, nodeB, nodeC, nodeD, nodeAA, (0, 0), (0, 0), (0, 0))
    $ pathB = (nodeA, nodeB, nodeC, nodeD, nodeAA, (0, 0), (0, 0), (0, 0))
    $ pathC = (nodeA, nodeB, nodeC, nodeD, nodeAA, (0, 0), (0, 0), (0, 0))
    $ pathD = (nodeA, nodeB, nodeC, nodeD, nodeAA, (0, 0), (0, 0), (0, 0))
     
    $ pathAA = (nodeA, nodeB, nodeC, nodeD, nodeAA, (0, 0), (0, 0), (0, 0))
    $ pathBB = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)
    $ pathCC = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)
    $ pathDD = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)


label loop_satellite_io11:
    
    while True:

        # start "move through the map" loop
        call startpos

        # do something at node?
        if exitpos == 1:
            call sound_door
            $ startpos = 1
            
            call show_space
            jump leave_docking 
            
        if exitpos == 2:
            if startpos == 2:
                m "There are some machines... {w=2.0} {nw}"
            $ startpos = 2
            
        if exitpos == 3:
            if startpos == 3:
                call sound_electroshock
                with hpunch
                m "No! The terminal is broken... {w=2.0} {nw}"
                #call terminal
                #call show_space
                #show satellite_io11 at inspace_idle
            $ startpos = 3
            
        if exitpos == 4:
            if startpos == 4:
                m "There are some computers and screens... {w=2.0} {nw}"
                jump satellite_io11_computer
                
            $ startpos = 4
            

        #exits routing "got to map and set position for next map"
        if exitpos == 11:
            if startpos == 11:
                call dialog_idontknow
      
            $ startpos = 11     

            
        if exitpos == 22:
            $ startpos = 22
            call dialog_closed

            
        if exitpos == 33:
            $ startpos = 33

            
        if exitpos == 44:
            $ startpos = 44




label satellite_io11_computer:
    $ pnc_nodes_visible = False
    
    scene terminal at topleft
    call sound_beep
    
    $ showtext = """
    Welcome to 
    Satellite Io-11 Direct Control
    [ascii_line]
    
    Enable/disable Remote Control?
    
    Remote Control is: [io11_remote_control]
    
    [ascii_line]
    
    To access it remotely, type in the terminal:
    
    Command: ssh io11
    Password: [io11_pass]

    """
    
    show text Text(showtext,text_align=termtext_align) at termtextpos
    
    menu:            
        
        "Enable Remote Control" if io11_remote_control == "disabled":
            call server_progressbar
            $ showtext ="""
    Remote Control enabled!
    
    Terminal Command: ssh io11"""
            show text Text(showtext,text_align=termtext_align) at termtextpos
            
            $ io11_remote_control = "enabled"
            call add_note("io11 remote command: ssh io11")
            pause 4

        "Disable Remote Control" if io11_remote_control == "enabled":
            call server_progressbar
            $ showtext ="""
    Remote Control disabled!
            
    No external access allowed."""
            show text Text(showtext,text_align=termtext_align) at termtextpos
            
            $ io11_remote_control = "disabled" 
            pause 4
            
        "Reset password" if io11_pass == "none":
            python:
                io11_pass = renpy.input(_("Enter a new password:"))
                io11_pass = io11_pass.strip()
                if not io11_pass:
                    io11_pass = "none"
            
            if io11_pass != "none":
                $ io11_pass_text = "io11 remote password: " + io11_pass
                call add_note(io11_pass_text)
            
            jump satellite_io11_computer
            
        "Exit":
            jump satellite_io11
            
    
            
    jump satellite_io11_computer

