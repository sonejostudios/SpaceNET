# map editor

init:
    $ mapeditor_newpaths = ""
    
    
label map_editor:
    
    # set image background for the map
    image mapeditor = imagemapsdir + "cargo_reactor.png"
    
    show bgcolor behind mapeditor
    show mapeditor:
        align (0.0,0.0)
    

    
    show screen map_editor_screen
    
    hide screen setpos
    hide screen map_tester_exit
    hide screen map_editor_summary
    
    
    

    show screen notify("Welcome to the Map Editor.")

    menu:
        "Set Nodes":
            jump node_editor
        
        "Set Paths":
            jump path_editor
            
        "Test Map":
            jump map_tester_start
            
        "Export":
            jump save_to_file
            
        "Exit":
            $ mapeditor_newpaths = ""
            hide screen map_editor_screen
            jump _invoke_main_menu


label node_editor:
    
    hide screen map_editor_summary
    show screen map_tester_exit
    
    show bgcolor behind mapeditor
    
    show screen notify("Set Positions of the Nodes.")
    
    hide text
    
    # start wizard
    
    centered "A?"
    $ nodeA = mousepos
    show nodeanime as pathnodeA:
        pos nodeA
    show text "A" as textA:
        pos nodeA

    centered "B?"
    $ nodeB = mousepos
    show nodeanime as pathnodeB:
        pos nodeB
    show text "B" as textB:
        pos nodeB
        
    centered "C?"
    $ nodeC = mousepos
    show nodeanime as pathnodeC:
        pos nodeC
    show text "C" as textC:
        pos nodeC

    centered "D?"
    $ nodeD = mousepos
    show nodeanime as pathnodeD:
        pos nodeD
    show text "D" as textD:
        pos nodeD
        

    centered "AA?"
    $ nodeAA = mousepos
    show nodeanime as pathnodeAA:
        pos nodeAA
    show text "AA" as textAA:
        pos nodeAA

    centered "BB?"
    $ nodeBB = mousepos
    show nodeanime as pathnodeBB:
        pos nodeBB
    show text "BB" as textBB:
        pos nodeBB
        
    centered "CC?"
    $ nodeCC = mousepos
    show nodeanime as pathnodeCC:
        pos nodeCC
    show text "CC" as textCC:
        pos nodeCC

    centered "DD?"
    $ nodeDD = mousepos
    show nodeanime as pathnodeDD:
        pos nodeDD
    show text "DD" as textDD:
        pos nodeDD

    
    window hide
    pause 1
    show screen map_editor_summary
    pause
    hide screen map_editor_summary
    
    menu:
            
        "Set Paths":
            jump path_editor
            
        "Exit":
            jump map_editor
    
    # This ends the game.

    return
    
  

# show nodes

label show_nodes:
        # show nodes
    show nodeanime as pathnodeA:
        pos nodeA
    show text "A" as textA:
        pos nodeA

    show nodeanime as pathnodeB:
        pos nodeB
    show text "B" as textB:
        pos nodeB
        
    show nodeanime as pathnodeC:
        pos nodeC
    show text "C" as textC:
        pos nodeC

    show nodeanime as pathnodeD:
        pos nodeD
    show text "D" as textD:
        pos nodeD

    show nodeanime as pathnodeAA:
        pos nodeAA
    show text "AA" as textAA:
        pos nodeAA

    show nodeanime as pathnodeBB:
        pos nodeBB
    show text "BB" as textBB:
        pos nodeBB

    show nodeanime as pathnodeCC:
        pos nodeCC
    show text "CC" as textCC:
        pos nodeCC

    show nodeanime as pathnodeDD:
        pos nodeDD
    show text "DD" as textDD:
        pos nodeDD
    
    return



# path editor

label path_editor:
    
    $ path = [(0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0)]
    
    show screen notify("Choose the Node to set up its Paths.")
    
    
    call show_nodes
    
    
    menu:
        "Node A":
            $ pathedit = "A"
            $ mapeditor_newpaths += "A, "
        "Node B":
            $ pathedit = "B"
            $ mapeditor_newpaths += "B, "
        "Node C":
            $ pathedit = "C"
            $ mapeditor_newpaths += "C, "
        "Node D":
            $ pathedit = "D"
            $ mapeditor_newpaths += "D, "
            
        "Node AA":
            $ pathedit = "AA"
            $ mapeditor_newpaths += "AA, "
        "Node BB":
            $ pathedit = "BB"
            $ mapeditor_newpaths += "BB, "
        "Node CC":
            $ pathedit = "CC"
            $ mapeditor_newpaths += "CC, "
        "Node DD":
            $ pathedit = "DD"
            $ mapeditor_newpaths += "DD, "
            
        "Exit":
            jump map_editor

    
    call path_chooser
    
    
    #copy path to pathA, pathB etc
    if pathedit == "A":
        $ pathA2 = path

    if pathedit == "B":
        $ pathB2 = path

    if pathedit == "C":
        $ pathC2 = path

    if pathedit == "D":
        $ pathD2 = path


    if pathedit == "AA":
        $ pathAA2 = path

    if pathedit == "BB":
        $ pathBB2 = path

    if pathedit == "CC":
        $ pathCC2 = path

    if pathedit == "DD":
        $ pathDD2 = path

    
    
    
    window hide
    pause 1    
    show screen map_editor_summary
    window hide
    pause
    hide screen map_editor_summary

    
    jump path_editor
    
    
label path_chooser:
        
    #start wizard
    show text "From [pathedit]"
    
    
    #while True:
    
    menu:
        "Show A":
            $ path[0] = "nodeA"
        
        "Hide A":
            $ path[0] = (0,0)
            hide pathnodeA
            hide textA
        
    menu:
        "Show B":
            $ path[1] = "nodeB"
        
        "Hide B":
            $ path[1] = (0,0)
            hide pathnodeB
            hide textB
        
    menu:
        "Show C" :
            $ path[2] = "nodeC"
        
        "Hide C":
            $ path[2] = (0,0)
            hide pathnodeC
            hide textC
        
    menu:
        "Show D" :
            $ path[3] = "nodeD"
        
        "Hide D" :
            $ path[3] = (0,0)
            hide pathnodeD
            hide textD

    menu:
        "Show AA" :
            $ path[4] = "nodeAA"
        
        "Hide AA" :
            $ path[4] = (0,0)
            hide pathnodeAA
            hide textAA
        
    menu:
        "Show BB" :
            $ path[5] = "nodeBB"
        
        "Hide BB" :
            $ path[5] = (0,0)
            hide pathnodeBB
            hide textBB
        
    menu:
        "Show CC" :
            $ path[6] = "nodeCC"
        
        "Hide CC" :
            $ path[6] = (0,0)
            hide pathnodeCC
            hide textCC
        
    menu:
        "Show DD" :
            $ path[7] = "nodeDD"
        
        "Hide DD" :
            $ path[7] = (0,0)
            hide pathnodeDD
            hide textDD
        
        

    hide text
    return
            
            

    
label save_to_file:
    
    show screen map_editor_summary
    
    menu:
        "Export":
            pass
        "Back":
            jump map_editor
    
     
    python:
        gamedir = config.gamedir + '/'
        gamedir = gamedir.replace('\\', '/') # to avoid problems on windows
        
        import codecs
        
        target = codecs.open(gamedir + "mapeditor/" + 'NEWMAP.txt', 'w+', 'utf-8')
        
        
        # write nodes
        target.write("$ nodeA = " + str(nodeA) + '\n' +
            "$ nodeB = " + str(nodeB) + '\n' +
            "$ nodeC = " + str(nodeC) + '\n' +
            "$ nodeD = " + str(nodeD) + '\n\n' +
            
            "$ nodeAA = " + str(nodeAA) + '\n' +
            "$ nodeBB = " + str(nodeBB) + '\n' +
            "$ nodeCC = " + str(nodeCC) + '\n' +
            "$ nodeDD = " + str(nodeDD) + '\n\n'
            )

        # write paths
        target.write("$ pathA = (" + str(pathA2[0]) + ", " + str(pathA2[1]) + ", " + str(pathA2[2]) + ", " + str(pathA2[3]) + ", " + str(pathA2[4]) + ", " + str(pathA2[5]) + ", " + str(pathA2[6]) + ", " + str(pathA2[7]) + ")" + "\n")
        target.write("$ pathB = (" + str(pathB2[0]) + ", " + str(pathB2[1]) + ", " + str(pathB2[2]) + ", " + str(pathB2[3]) + ", " + str(pathB2[4]) + ", " + str(pathB2[5]) + ", " + str(pathB2[6]) + ", " + str(pathB2[7]) + ")"+ "\n")
        target.write("$ pathC = (" + str(pathC2[0]) + ", " + str(pathC2[1]) + ", " + str(pathC2[2]) + ", " + str(pathC2[3]) + ", " + str(pathC2[4]) + ", " + str(pathC2[5]) + ", " + str(pathC2[6]) + ", " + str(pathC2[7]) + ")"+ "\n")
        target.write("$ pathD = (" + str(pathD2[0]) + ", " + str(pathD2[1]) + ", " + str(pathD2[2]) + ", " + str(pathD2[3]) + ", " + str(pathD2[4]) + ", " + str(pathD2[5]) + ", " + str(pathD2[6]) + ", " + str(pathD2[7]) + ")"+ "\n \n")

        target.write("$ pathAA = (" + str(pathAA2[0]) + ", " + str(pathAA2[1]) + ", " + str(pathAA2[2]) + ", " + str(pathAA2[3]) + ", " + str(pathAA2[4]) + ", " + str(pathAA2[5]) + ", " + str(pathAA2[6]) + ", " + str(pathAA2[7]) + ")" + "\n")
        target.write("$ pathBB = (" + str(pathBB2[0]) + ", " + str(pathBB2[1]) + ", " + str(pathBB2[2]) + ", " + str(pathBB2[3]) + ", " + str(pathBB2[4]) + ", " + str(pathBB2[5]) + ", " + str(pathBB2[6]) + ", " + str(pathBB2[7]) + ")"+ "\n")
        target.write("$ pathCC = (" + str(pathCC2[0]) + ", " + str(pathCC2[1]) + ", " + str(pathCC2[2]) + ", " + str(pathCC2[3]) + ", " + str(pathCC2[4]) + ", " + str(pathCC2[5]) + ", " + str(pathCC2[6]) + ", " + str(pathCC2[7]) + ")"+ "\n")
        target.write("$ pathDD = (" + str(pathDD2[0]) + ", " + str(pathDD2[1]) + ", " + str(pathDD2[2]) + ", " + str(pathDD2[3]) + ", " + str(pathDD2[4]) + ", " + str(pathDD2[5]) + ", " + str(pathDD2[6]) + ", " + str(pathDD2[7]) + ")"+ "\n \n")

        
        target.close() # don't forget to close the file !!
        
        
    hide screen map_editor_summary
    "Export done!\n\nHave a look at /mapeditor/NEWMAP.txt"
        
    jump map_editor
    
    


screen map_editor_screen:
    zorder 1
         
    # get every 0.1 sec mouse position
    timer 0.1 repeat True action [SetVariable("mousepos", renpy.get_mouse_pos())]
    
    # show mouse position for devs
    text "mouse [mousepos]" at topright
    
    text "changed paths: [mapeditor_newpaths]" at topleft

    
    

screen map_editor_summary:
    
    add color("#112119")
    
    text "{size=12}\n\n nodeA = [nodeA]\n nodeB = [nodeB]\n nodeC = [nodeC]\n nodeD = [nodeD]\n\n nodeAA = [nodeAA]\n nodeBB = [nodeBB]\n nodeCC = [nodeCC]\n nodeDD = [nodeDD]"

    text "{size=12}\n\n\n\n\n\n\n\n\n\n\n\n\n\n pathA = [pathA2]\n pathB = [pathB2]\n pathC = [pathC2]\n pathD = [pathD2]\n\n pathAA = [pathAA2]\n pathBB = [pathBB2]\n pathCC = [pathCC2]\n pathDD = [pathDD2]"
    
  


label map_editor_init:
    $ pathedit = "A"
    
    $ path = ["nodeA", "nodeB", "nodeC", "nodeD", "nodeAA", "nodeBB", "nodeCC", "nodeDD"]
    
    
    $ pathA = ["nodeA", "nodeB", "nodeC", "nodeD", "nodeAA", "nodeBB", "nodeCC", "nodeDD"]
    $ pathB = ["nodeA", "nodeB", "nodeC", "nodeD", "nodeAA", "nodeBB", "nodeCC", "nodeDD"]
    $ pathC = ["nodeA", "nodeB", "nodeC", "nodeD", "nodeAA", "nodeBB", "nodeCC", "nodeDD"]
    $ pathD = ["nodeA", "nodeB", "nodeC", "nodeD", "nodeAA", "nodeBB", "nodeCC", "nodeDD"]
    
    $ pathAA = ["nodeA", "nodeB", "nodeC", "nodeD", "nodeAA", "nodeBB", "nodeCC", "nodeDD"]
    $ pathBB = ["nodeA", "nodeB", "nodeC", "nodeD", "nodeAA", "nodeBB", "nodeCC", "nodeDD"]
    $ pathCC = ["nodeA", "nodeB", "nodeC", "nodeD", "nodeAA", "nodeBB", "nodeCC", "nodeDD"]
    $ pathDD = ["nodeA", "nodeB", "nodeC", "nodeD", "nodeAA", "nodeBB", "nodeCC", "nodeDD"]
    
    
    # path"2" is written and exported, path"" is used for testing
    $ pathA2 = ["nodeA", "nodeB", "nodeC", "nodeD", "nodeAA", "nodeBB", "nodeCC", "nodeDD"]
    $ pathB2 = ["nodeA", "nodeB", "nodeC", "nodeD", "nodeAA", "nodeBB", "nodeCC", "nodeDD"]
    $ pathC2 = ["nodeA", "nodeB", "nodeC", "nodeD", "nodeAA", "nodeBB", "nodeCC", "nodeDD"]
    $ pathD2 = ["nodeA", "nodeB", "nodeC", "nodeD", "nodeAA", "nodeBB", "nodeCC", "nodeDD"]
    
    $ pathAA2 = ["nodeA", "nodeB", "nodeC", "nodeD", "nodeAA", "nodeBB", "nodeCC", "nodeDD"]
    $ pathBB2 = ["nodeA", "nodeB", "nodeC", "nodeD", "nodeAA", "nodeBB", "nodeCC", "nodeDD"]
    $ pathCC2 = ["nodeA", "nodeB", "nodeC", "nodeD", "nodeAA", "nodeBB", "nodeCC", "nodeDD"]
    $ pathDD2 = ["nodeA", "nodeB", "nodeC", "nodeD", "nodeAA", "nodeBB", "nodeCC", "nodeDD"]
    

    
    jump map_editor

