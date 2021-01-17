###############
# SpaceNet



define m = Character("[playername]", image="player", color="#ffffff")
define md = Character("[playername]", image="minidroid", color="#ffffff")

define guard = Character("Guard", image="guardian", color="#ffffff")
define guardxylo = Character("Guard", image="guardxylo", color="#ffffff")
define robotguard = Character("Guard", image="robotguard", color="#ffffff")

define radio = Character(" ", image="radio", color="#ffffff")
define robot = Character("Robot", image="robotguard", color="#ffffff")

define barman_xvil = Character("Barman", image="barman2", color="#ffffff")
define barman_xsea = Character("Barman", image="barman3", color="#ffffff")
define barman_isc = Character("Barman", image="barman", color="#ffffff")

define vendor = Character("Vendor", image="vendor", color="#ffffff")

define oldman = Character("Man", image="oldman", color="#ffffff")
define fisher = Character("Fisher", image="fisher", color="#ffffff")

define worker = Character("Worker", image="person", color="#ffffff")
define worker1 = Character("Worker", image="worker1", color="#ffffff")
define worker2 = Character("Worker", image="worker2", color="#ffffff")
define worker3 = Character("Worker", image="worker3", color="#ffffff")

define officer = Character("Officer", image="person", color="#ffffff")

define client = Character("Client", image="person", color="#ffffff")
define client1 = Character("Client", image="client1", color="#ffffff")
define client2gem = Character("Client", image="client2gem", color="#ffffff")

define clientsea = Character("Client", image="clientsea", color="#ffffff")

define clientsysadmin = Character("Client", image="sysadmin", color="#ffffff")
define clientplayer = Character("Client", image="clientplayer", color="#ffffff")
define clientisc3 = Character("Client", image="clientisc3", color="#ffffff")

define sam = Character("Sam", image="sam", color="#ffffff")
define samclient = Character("Client", image="sam", color="#ffffff")


define hacker = Character("4n0nym0u5", image="hacker", color="#ffffff")
define hackerradio = Character("4n0nym0u5", image="radio", color="#ffffff")


define sysadmin = Character("Sys Admin", image="sysadmin", color="#ffffff")

#side images
#image side person = "sides/person.png"
image side radio = "sides/radio.png"


image side cross = "sides/cross.png"
image side minidroid = "sides/minidroid.png"


image side player = ConditionSwitch(
        "playertype=='player'", "sides/cross.png",
        "playertype=='minidroid'", "sides/minidroid.png")


# avatar choose test
#image side player = ConditionSwitch(
#        "planet=='xylo'", "sides/sam.png",
#        "planet=='demo'", "sides/hacker.png",
#        "planet=='cargo'", "sides/barman.png",
#        "planet=='isc'", "sides/barman2.png")




image side sam = "sides/sam.png"
image side hacker = "sides/hacker.png"

image side barman = "sides/barman.png"
image side barman2 = "sides/barman2.png"
image side barman3 = "sides/barman3.png"

#image side vendor = "sides/vendor.png"
#image side vendor2 = "sides/vendor2.png"

image side vendor = ConditionSwitch(
        "planet=='xylo'", "sides/vendor.png",
        "planet=='isc'", "sides/vendor2.png")
        

image side oldman = "sides/oldman.png"
image side client1 = "sides/client1.png"
image side client2gem = "sides/client2gem.png"
image side guardxylo = "sides/guardxylo.png"
image side worker1 = "sides/worker1.png"
image side worker2 = "sides/worker2.png"
image side worker3 = "sides/worker3.png"
image side fisher = "sides/fisher.png"
image side clientsea = "sides/clientsea.png"
image side robotguard = "sides/robotguard.png"
image side sysadmin = "sides/sysadmin.png"
image side clientplayer = "sides/clientplayer.png"
image side clientisc3 = "sides/clientisc3.png"




#music fade
define config.fade_music = 1.0



# main colors
image bgcolor = "#112119"
image black = "#000000"
image white = "#ffffff"
image green = "#8dd35f"



image shadow:
    "images/shadow.png"
    anchor (0.5,0.5)
    
    
    

image player:
    #"images/position.png"
    ConditionSwitch(
        "playertype=='player'", "images/position.png",
        "playertype=='minidroid'", "images/minidroid.png")
    anchor (0.5,0.5)
    linear 1 alpha 0.2
    linear 1 alpha 1.0
    repeat
    
image playercross:
    "images/position.png"
    anchor (0.5,0.5)
    #linear 1 alpha 0.2
    #linear 1 alpha 1.0
    #repeat
    
image minidroid:
    "images/minidroid.png"
    anchor (0.5,0.5)


image nodeanime:
    "images/node.png"
    anchor (0.5,0.5)
    linear 10 rotate 180.0
    rotate 0
    repeat
    
    
    
#image pathnodeA = At("images/node.png", nodeanime) # create image and apply transform on it


image propeller:
    anchor (0.5,0.5)
    "images/propeller.png"


image light:
    anchor (0.5,0.5)
    "images/light.png"
    alpha 0.0
    pause 1
    alpha 1.0
    pause 1
    repeat


# spaceship up    
image spaceship:
    anchor (0.5,0.5) 
    ConditionSwitch(
        "spaceshiptype=='1'", "images/spaceship/spaceship1u.png",
        "spaceshiptype=='2'", "images/spaceship/spaceship2u.png",
        "spaceshiptype=='3'", "images/spaceship/spaceship3u.png")

# spaceship side 
image spaceshipside:
    anchor (0.5,0.5) 
    ConditionSwitch(
        "spaceshiptype=='1'", "images/spaceship/spaceship1s.png",
        "spaceshiptype=='2'", "images/spaceship/spaceship2s.png",
        "spaceshiptype=='3'", "images/spaceship/spaceship3s.png")


# spaceship up
image spaceship1u:
    "images/spaceship/spaceship1u.png"
    anchor (0.5,0.5)

image spaceship2u:
    "images/spaceship/spaceship2u.png"
    anchor (0.5,0.5)
    
image spaceship3u:
    "images/spaceship/spaceship3u.png"
    anchor (0.5,0.5)
    
    
# spaceship side
image spaceship1s:
    "images/spaceship/spaceship1s.png"
    anchor (0.5,0.5)

image spaceship2s:
    "images/spaceship/spaceship2s.png"
    anchor (0.5,0.5)
    
image spaceship3s:
    "images/spaceship/spaceship3s.png"
    anchor (0.5,0.5)


        
        
image doorh:
    "images/door.png"
    anchor (0.5,0.5)
    
image doorv:
    "images/door.png"
    anchor (0.5,0.5)
    rotate 90
    
image circle:
    "images/circle.png"
    anchor (0.5,0.5)
    
image screw:
    "images/screw.png"
    anchor (0.5,0.5)
    
image buttonscreen:
    "images/buttonscreen.png"
    anchor (0.5,0.5)
    
image hexagon:
    "images/hexagon.png"
    anchor (0.5,0.5)
    
image warningfloor = "/images/warningfloor.png"

image spacenetsender:
    anchor (0.5,0.5)
    "/images/senderc.png"
    pause 0.5
    "/images/senderb.png"
    pause 0.5
    "/images/sender.png"
    pause 0.5
    repeat
    
    
image guard:
    anchor (0.5, 0.9)
    rotate_pad True
    "images/guard.png"
    pause 0.1
    "images/guard2.png"
    pause 0.1
    repeat
    
image npc:
    "/images/npc.png"
    anchor (0.5,0.5)
    rotate_pad True
    
    
    
image tube:
    "/images/tube.png"
    anchor (0.5,0.5)
    
    
image rails2:
    "/images/rails2.png"
    anchor (0.5,0.5)
    
image infopanel = "/images/infopanel.png"


image brokenwall closed:
    "/images/brokenwall1.png"
    anchor (0.5,0.5)

image brokenwall open:
    "/images/brokenwall2.png"
    anchor (0.5,0.5)
    
image table: 
    "images/table.png"
    anchor (0.5,0.5)
    
image box:
    "box.png"
    anchor (0.5,0.5)
    
    

image galaxy_intro:
    "images/galaxy.png"
    alpha 0.1
    anchor (0.5, 0.5)
    pos (0.5, 0.5)
    pause 1
    linear 400 rotate 360.0
    rotate 0
    repeat
    


# main menu music
define config.main_menu_music = "music/space-amb.ogg"

#mouse cursor
#define config.mouse = {"default" : [("images/cursor_default.png", 30, 30)]}
define config.mouse = None 


# see also in option.py
        

init :
    
    # demo version
    $ demo_version = False
    
    # pre version. For release = ""
    $ pre_version = ""
    
    ## The version of the game.
    define config.version = "1.0"
    
    # build date. Set date for release.
    $ build_date = "2021-01-17"
    
    # developer mode (True/False). For release = False
    $ superdev = False
    
    # use dev-keys and show superdev prefs button. For release = False
    $ use_dev_keys = False
    



    # DEFAULT VARS
    $ imagemapsdir = "images/maps/"

    # spaceship type, as string, so it is possible to add 1b, 1c etc.
    $ spaceshiptype = "1"
    
    
    # player types: "player", "minidroid"
    $ playertype = "player"
    
    $ playername = "hero"
    
    $ tutorial_done = False
    
    
    $ planet = "megaship"
    
    
    $ flash = Fade(.10,0,.75,color="fff")
 
    $ nodeA = (400,100)
    $ nodeB = (600,240)
    $ nodeC = (400,400)
    $ nodeD = (100,240)
    
    $ nodeAA = (400,25)
    $ nodeBB = (780,240)
    $ nodeCC = (400,460)
    $ nodeDD = (30,240)
    
    
    $ mousepos = (0,0)
    $ position = (0,0)
    $ gotopos =  0
 
    $ startpos = 11
    $ exitpos = 33
    
    $ path = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)
    
    $ pathA = ()
    $ pathB = ()
    $ pathC = ()
    $ pathD = ()
    
    $ pathAA = ()
    $ pathBB = ()
    $ pathCC = ()
    $ pathDD = ()
    
    #default inventory = []
    #default inventory = ["cable", "lamp", "mirror", "bulb", "spacenet", "screwdriver", "gem"]
    default inventory = ["newspaper", "screwdriver", "spacesuit", "lamp", "bulb", "mirror", "spacenet", "accesscard", "rope", 
                        "cable", "pick", "dynamite", "minidroid", "gem", "star", "notebook", "laser", "key", "letter", "hook", "magnet", "robotcard", "knife", "cards"]
    
    $ inventory_select = ""
    $ inventory_notify = ""
    
    default planetlist = ["sun", "megaship", "xylo", "isc", "cargo", "io11"]
    #default planetlist = ["megaship", "xylo"]
    
    $ gems = 0
    $ maxgems = 12
    
    $ active_nodes_amount = 0
    $ max_nodes_amount = 4
    
    
    $ inventory_button = True
    
    $ coins = 0
    
    
    # using "default" make this list saveable
    default spacenetnodes = []
    
    $ hours = 0
    $ minutes = 0
    $ seconds = 0
    
    $ alarm_on = False
    
    $ liftlevel = ("00", "01", "02", "03")
    
    $ countdown = False
    $ countdown_sec = 0
    
    
    $ drunktime = 0
    $ drunk_level = 0
    
    $ triptime = False
    
    
    
## settings
    # point'n'click mode
    $ pnc_mode = False
    $ pnc_nodes_visible = True
    
    
    # cursor style
    $ pnc_cursor = False

    # display
    $ termfx_enable = 1
    $ shadow_enable = 1
    $ galaxy_enable = 1
    
    # multiplicator for stars amount. for android = 1, for pc = 4
    # this as to set at compile time
    #$ starsamount = 1 this is set in animations.rpy

    $ in_intro = True
 

## others

    $ liftpos = 0
    $ guardpos = 6 # 6 = no pos
    

    $ buttons = False
    $ button_house = False
    $ button_chase = False
    $ button_multimap1 = False
    
    $ darkroom = True
    
    $ spacenetmenu = False
    $ loginmenu = False
    
    $ info_panel_symbol = ""
    
    $ showtext = ""
    

    
    
    


# The game starts here.

label start:
    #jump space
    
    show screen setpos
    show screen buttons
    
    show screen selected_item
    
    
    #if termfx_enable == 1:
    show screen termfx
    
    show screen superdev
    
    $ startpos = 1
    window hide
    #show map6
    #centered "start the engine at position node [startpos] (DD) "
    
    
    
   
    
    
    $ ingame = False
    $ landing = False
    $ space_anim = False
    
    $ in_intro = False
    
    
    # empty inventory
    #$ inventory = []
    
    # reset coins
    $ coins = 0

    
    #$ xylo_mine_used_dynamite = False
    #$ xylo_mine_minitrain_room_pick = False
    
    
    # for final end only
    #$ active_nodes_amount = 4
    #$ cargo_exploded = 2
    #$ intercom_sat = True 
    #$ sat_connected_to = "SpaceNET"
    
    #$ game_end = True
    
    $ spacenet_copied = True


    $ isc_spaceport_auth = True


    #jump to first map
    #$ liftpos = 3
    $ startpos = 1
    

            
    #jump xylo_village1
    
    
    #jump megaship_spaceport
    #jump map4
    #$ startpos = 2
    #jump xylo_mountain2
    
    #$ planet = "megaship"
    #jump megaship_spaceport
    #jump xylo_map1
    #$ shippos = (400,0) # set position in surface engine
    #jump map6
    #jump mapdemos
    
    $ planetxy_register = True
    $ planetxy_auth = True
    #$ hacker_in_prison = 1
    
    menu:
        "megaship":
            $ planet = "megaship"
        "xylo":
            $ planet = "xylo"
        "isc":
            $ planet = "isc"
        "io11":
            $ planet = "io11"
        "sun":
            $ planet = "sun"
        "cargo":
            $ planet = "cargo"
            
    jump space
    #jump xylo_map5house
    #jump docking
    #jump cargo_spaceport
    
    
    # This ends the game.
    return
    
    



