# MAPS

############################################

label map_tester_start:
    
    show screen map_editor_screen
    
    show screen map_tester_exit
    
    show screen setpos
    #show screen buttons
    $ landing = False
    
    show screen notify("Select a Start Position.")
    
    menu:
        "Start A":
            $ startpos = 1
        "Start B":
            $ startpos = 2
        "Start C":
            $ startpos = 3
        "Start D":
            $ startpos = 4
        "Start AA":
            $ startpos = 11
        "Start BB":
            $ startpos = 22
        "Start CC":
            $ startpos = 33
        "Start DD":
            $ startpos = 44
        
    

   
    jump map_tester



label map_tester:
    
    scene mapeditor
    show screen notify("MAP TEST")
    
    show bgcolor behind mapeditor
    
    
    # dirty hack replace strings with node coords in path""
    #pathA
    if pathA2[0] == "nodeA":
        $ pathA[0] = nodeA
    if pathA2[1] == "nodeB":
        $ pathA[1] = nodeB
    if pathA2[2] == "nodeC":
        $ pathA[2] = nodeC
    if pathA2[3] == "nodeD":
        $ pathA[3] = nodeD
        
    if pathA2[4] == "nodeAA":
        $ pathA[4] = nodeAA
    if pathA2[5] == "nodeBB":
        $ pathA[5] = nodeBB
    if pathA2[6] == "nodeCC":
        $ pathA[6] = nodeCC
    if pathA2[7] == "nodeDD":
        $ pathA[7] = nodeDD
        
    #pathB
    if pathB2[0] == "nodeA":
        $ pathB[0] = nodeA
    if pathB2[1] == "nodeB":
        $ pathB[1] = nodeB
    if pathB2[2] == "nodeC":
        $ pathB[2] = nodeC
    if pathB2[3] == "nodeD":
        $ pathB[3] = nodeD
                     
    if pathB2[4] == "nodeAA":
        $ pathB[4] = nodeAA
    if pathB2[5] == "nodeBB":
        $ pathB[5] = nodeBB
    if pathB2[6] == "nodeCC":
        $ pathB[6] = nodeCC
    if pathB2[7] == "nodeDD":
        $ pathB[7] = nodeDD
        
        
    #pathC
    if pathC2[0] == "nodeA":
        $ pathC[0] = nodeA
    if pathC2[1] == "nodeB":
        $ pathC[1] = nodeB
    if pathC2[2] == "nodeC":
        $ pathC[2] = nodeC
    if pathC2[3] == "nodeD":
        $ pathC[3] = nodeD
                     
    if pathC2[4] == "nodeAA":
        $ pathC[4] = nodeAA
    if pathC2[5] == "nodeBB":
        $ pathC[5] = nodeBB
    if pathC2[6] == "nodeCC":
        $ pathC[6] = nodeCC
    if pathC2[7] == "nodeDD":
        $ pathC[7] = nodeDD
        
        
    #pathD
    if pathD2[0] == "nodeA":
        $ pathD[0] = nodeA
    if pathD2[1] == "nodeB":
        $ pathD[1] = nodeB
    if pathD2[2] == "nodeC":
        $ pathD[2] = nodeC
    if pathD2[3] == "nodeD":
        $ pathD[3] = nodeD
                     
    if pathD2[4] == "nodeAA":
        $ pathD[4] = nodeAA
    if pathD2[5] == "nodeBB":
        $ pathD[5] = nodeBB
    if pathD2[6] == "nodeCC":
        $ pathD[6] = nodeCC
    if pathD2[7] == "nodeDD":
        $ pathD[7] = nodeDD
        
  
    #pathAA
    if pathAA2[0] == "nodeA":
        $ pathAA[0] = nodeA
    if pathAA2[1] == "nodeB":
        $ pathAA[1] = nodeB
    if pathAA2[2] == "nodeC":
        $ pathAA[2] = nodeC
    if pathAA2[3] == "nodeD":
        $ pathAA[3] = nodeD
                      
    if pathAA2[4] == "nodeAA":
        $ pathAA[4] = nodeAA
    if pathAA2[5] == "nodeBB":
        $ pathAA[5] = nodeBB
    if pathAA2[6] == "nodeCC":
        $ pathAA[6] = nodeCC
    if pathAA2[7] == "nodeDD":
        $ pathAA[7] = nodeDD
        
        
    #pathBB
    if pathBB2[0] == "nodeA":
        $ pathBB[0] = nodeA
    if pathBB2[1] == "nodeB":
        $ pathBB[1] = nodeB
    if pathBB2[2] == "nodeC":
        $ pathBB[2] = nodeC
    if pathBB2[3] == "nodeD":
        $ pathBB[3] = nodeD
                      
    if pathBB2[4] == "nodeAA":
        $ pathBB[4] = nodeAA
    if pathBB2[5] == "nodeBB":
        $ pathBB[5] = nodeBB
    if pathBB2[6] == "nodeCC":
        $ pathBB[6] = nodeCC
    if pathBB2[7] == "nodeDD":
        $ pathBB[7] = nodeDD
        
        
    #pathCC
    if pathCC2[0] == "nodeA":
        $ pathCC[0] = nodeA
    if pathCC2[1] == "nodeB":
        $ pathCC[1] = nodeB
    if pathCC2[2] == "nodeC":
        $ pathCC[2] = nodeC
    if pathCC2[3] == "nodeD":
        $ pathCC[3] = nodeD
                      
    if pathCC2[4] == "nodeAA":
        $ pathCC[4] = nodeAA
    if pathCC2[5] == "nodeBB":
        $ pathCC[5] = nodeBB
    if pathCC2[6] == "nodeCC":
        $ pathCC[6] = nodeCC
    if pathCC2[7] == "nodeDD":
        $ pathCC[7] = nodeDD
        
    
    #pathDD
    if pathDD2[0] == "nodeA":
        $ pathDD[0] = nodeA
    if pathDD2[1] == "nodeB":
        $ pathDD[1] = nodeB
    if pathDD2[2] == "nodeC":
        $ pathDD[2] = nodeC
    if pathDD2[3] == "nodeD":
        $ pathDD[3] = nodeD
                      
    if pathDD2[4] == "nodeAA":
        $ pathDD[4] = nodeAA
    if pathDD2[5] == "nodeBB":
        $ pathDD[5] = nodeBB
    if pathDD2[6] == "nodeCC":
        $ pathDD[6] = nodeCC
    if pathDD2[7] == "nodeDD":
        $ pathDD[7] = nodeDD
        
    
    

label loop_mapeditor:

    # start "move through the map" loop
    call startpos from _call_startpos_33

    # do something at node?
    if exitpos == 1:       #if at node A
        $ startpos = 1     # stay in A
        jump map_tester         # map loop to jump to
        
    if exitpos == 2:
        $ startpos = 2
        jump map_tester
        
    if exitpos == 3: # switch board
        $ startpos = 3
        jump map_tester
        
    if exitpos == 4:
        $ startpos = 4
        jump map_tester 
        

    #exits routing "got to map and set position for next map"
    if exitpos == 11:       #if going out at AA
        $ startpos = 11     #go to CC
        jump map_tester          # map to jump to
        
    if exitpos == 22:
        $ startpos = 22
        jump map_tester 
        
    if exitpos == 33:
        $ startpos = 33
        jump map_tester
        
    if exitpos == 44:
        $ startpos = 44
        jump map_tester

    jump map_tester
#END



screen map_tester_exit:
    
    textbutton "exit" action [Jump("map_editor")] at topright
