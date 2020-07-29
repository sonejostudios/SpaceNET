# MAPS

init:
    $ cargo_remote_control = "disabled"
    $ cargo_reactor_state = "working"
    


############################################
label cargo_reactor:
    
    $ pnc_nodes_visible = True
    
            
    call atmo_reactor from _call_atmo_reactor
    
    
    scene bgcolor
    show screen notify("cargo reactor")
    
    image cargo_reactor = imagemapsdir + "cargo_reactor.png"
    show cargo_reactor
    
    image reactor:
        "images/reactor.png"
        anchor (0.5,0.5)
        



    if cargo_reactor_state == "working":
        show reactor:
            pos (560, 240)
            rotate 0
            linear 2 rotate 180
            repeat
        $ alarm_on = False
        $ countdown = False
        $ countdown_sec = 0
            

            
    if cargo_reactor_state == "stopped":
        show reactor:
            pos (560, 240)
            rotate 160
    
    
    if cargo_reactor_state == "stopping":
        show reactor:
            pos (560, 240)
            rotate 0
            easein 2 rotate 160
        $ cargo_reactor_state = "stopped"
        
        # set countdown
        $ countdown = True
        $ countdown_sec = 180
        
        $ alarm_on = True
        
        
        
        

            
    if countdown_sec <= 0:
        $ alarm_on = False
        $ cargo_reactor_state = "working"
   





    # set all variables for the map (nodes and path)
    $ nodeA = (200, 420)
    $ nodeB = (55, 284)
    $ nodeC = (175, 120)
    $ nodeD = (329, 240)

    $ nodeAA = (744, 425)
    $ nodeBB = (704, 427)
    $ nodeCC = (661, 427)
    $ nodeDD = (614, 429)

    $ pathA = (nodeA, nodeB, nodeC, nodeD, (0, 0), (0, 0), (0, 0), (0, 0))
    $ pathB = (nodeA, nodeB, nodeC, nodeD, (0, 0), (0, 0), (0, 0), (0, 0))
    $ pathC = (nodeA, nodeB, nodeC, nodeD, (0, 0), (0, 0), (0, 0), (0, 0))
    $ pathD = (nodeA, nodeB, nodeC, nodeD, (0, 0), (0, 0), (0, 0), (0, 0))
     
    $ pathAA = ((0, 0), (0, 0), (0, 0), nodeD, nodeAA, (0, 0), (0, 0), (0, 0))
    $ pathBB = ((0, 0), nodeB, nodeC, (0, 0), (0, 0), nodeBB, nodeCC, (0, 0))
    $ pathCC = (nodeA, nodeB, nodeC, nodeD, (0, 0), nodeBB, nodeCC, (0, 0))
    $ pathDD = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)
    
    


label loop_cargo_reactor:

    while True:
        
        # alarm
        call alarm_check from _call_alarm_check_9
        
        # start "move through the map" loop
        call startpos from _call_startpos_30

        # do something at node?
        if exitpos == 1:
            $ startpos = 33
            call sound_door from _call_sound_door_77
            
            # stop reactor sound
            stop atmo
                    
            jump cargo_conveyor2

            
        if exitpos == 2:
            if startpos == 2:
                
                call dialog_closed from _call_dialog_closed_15
                
                #if superdev == 1:
                    #jump cargo_explosion_anim
                #    call terminal
                
            $ startpos = 2
            
        if exitpos == 3:
            if startpos == 3:
                m "This is the control computer of the reactor.{w=3}{nw}"
                jump cargo_reactor_computer
            $ startpos = 3
            
        if exitpos == 4:
            if startpos == 4:
                m "This is the reactor of the cargo spaceship.{w=3}{nw}"
                m "It is huge and it looks really dangerous!{w=3}{nw}"
            $ startpos = 4
            

        #conveyor animation out
        if exitpos == 11:
            $ startpos = 11
              
            
            
        if exitpos == 22:
            $ startpos = 22
            
            
        if exitpos == 33:
            $ startpos = 33

            
        if exitpos == 44:
            $ startpos = 44




label cargo_reactor_computer:
    
    $ pnc_nodes_visible = False
    
    
    scene terminal at topleft
    call sound_beep from _call_sound_beep_27
    
    $ showtext = """
    Cargo Reactor Control
    [ascii_line]
    
    Reactor state: [cargo_reactor_state]
    
    Remote Control is : [cargo_remote_control]

    """
    
    show text Text(showtext,text_align=termtext_align) at termtextpos
    
    
    menu:            
        
        "Stop Reactor" if cargo_reactor_state == "working":
            $ cargo_reactor_state = "stopping"
            
            m "Okay, the reactor will stop now...{w=2.5}{nw}"
            m "Now I need to hurry up before the guards are coming to restart it!{w=3.5}{nw}"
            m "Let's go!{w=2}{nw}"
            
            jump cargo_reactor
            
        "Start Reactor" if cargo_reactor_state == "stopped":
            $ cargo_reactor_state = "working"
            jump cargo_reactor
            
        
        "Enable Remote Control" if cargo_remote_control == "disabled":
            call server_progressbar from _call_server_progressbar_8
            $ showtext ="""
    Remote Control enabled!
    
    Terminal Command : ssh cargo
    Password : convoy"""
            show text Text(showtext,text_align=termtext_align) at termtextpos
            
            $ cargo_remote_control = "enabled"
            call add_note("Cargo remote control: ssh cargo. Pass: convoy") from _call_add_note_4
            pause 4

        "Disable Remote Control" if cargo_remote_control == "enabled":
            call server_progressbar from _call_server_progressbar_9
            $ showtext ="""
    Remote Control disabled!
            
    No external access allowed."""
            show text Text(showtext,text_align=termtext_align) at termtextpos
            
            $ cargo_remote_control = "disabled" 
            pause 4
            
   
            
        "Exit":
            jump cargo_reactor
            
    
            
    jump cargo_reactor_computer



