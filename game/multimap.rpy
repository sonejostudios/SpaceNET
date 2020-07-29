init:
    # set all variables for the map (nodes and path)
    $ nodeA = (400,240)
    $ nodeB = (-100,000)
    $ nodeC = (-100,000)
    $ nodeD = (-100,000)
    
    $ nodeAA = (400,50)
    $ nodeBB = (750,240)
    $ nodeCC = (400,430)
    $ nodeDD = (50,240)
    
    $ pathA = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)
    $ pathB = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)
    $ pathC = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)
    $ pathD = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)
    
    $ pathAA = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)
    $ pathBB = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)
    $ pathCC = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)
    $ pathDD = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)

    $ pathviewall = (nodeA, nodeB, nodeC, nodeD, nodeAA, nodeBB, nodeCC, nodeDD)
    
    $ multiposx = 0
    $ multiposy = 0
    $ multipos = (0, 0)
    
    # positions for special objects (doors, item)
    $ multiobjectposN = (400,147)
    $ multiobjectposE = (493,240)
    $ multiobjectposS = (400,333)
    $ multiobjectposW = (307,240)
    
    # nodes position for special objects (doors, item)
    $ multinodeposN = (400,170)
    $ multinodeposE = (470,240)
    $ multinodeposS = (400,310)
    $ multinodeposW = (330,240)
    
    $ maplink = "0"
    
    $ multiarray = [["3E","2E","7S", "1S"],
                    ["7N","3S","7W", "2N"],
                    ["1E","4N","2E", "7W"],
                    ["1E","3N","2E", "1W"]]
                    
                    
    
    
    image M1:
        imagemapsdir + "/multimap/1.png"
        anchor (0.5, 0.5)
        pos (0.5,0.5)

    image M2:
        imagemapsdir + "/multimap/2.png"
        anchor (0.5, 0.5)
        pos (0.5,0.5)

    image M7:
        imagemapsdir + "/multimap/7.png"
        anchor (0.5, 0.5)
        pos (0.5,0.5)

    image M3:
        imagemapsdir + "/multimap/3.png"
        anchor (0.5, 0.5)
        pos (0.5,0.5)
        
    image M4:
        imagemapsdir + "/multimap/4.png"
        anchor (0.5, 0.5)
        pos (0.5,0.5)
        
     


label multimap_startanim:
    
    # set all variables for the map (nodes and path)
    $ nodeA = (400,240)
    
    $ nodeB = (-100,000)
    $ nodeC = (-100,000)
    $ nodeD = (-100,000)
    
    $ nodeAA = (400,50)
    $ nodeBB = (750,240)
    $ nodeCC = (400,430)
    $ nodeDD = (50,240)
    
    
    call draw_multimap from _call_draw_multimap
    return

     
        
    # draw multimap
label draw_multimap:
    hide M1 
    hide M2 
    hide M7 
    hide M3 
    hide M4

    $ maplink = multiarray[multiposy][multiposx]
    
    

# North      
    if maplink == "1N":
        show M1 zorder -99
        $ pathA = (nodeA, (0,0), (0,0), (0,0), nodeAA, (0,0), (0,0), (0,0))
        $ pathAA = (nodeA, (0,0), (0,0), (0,0), nodeAA, (0,0), (0,0), (0,0))
        
    if maplink == "2N":
        show M2 zorder -99
        $ pathA = (nodeA, (0,0), (0,0), (0,0), nodeAA, (0,0), nodeCC, (0,0))
        $ pathAA = (nodeA, (0,0), (0,0), (0,0), nodeAA, (0,0), nodeCC, (0,0))
        $ pathCC = (nodeA, (0,0), (0,0), (0,0), nodeAA, (0,0), nodeCC, (0,0))
        
    if maplink == "7N":
        show M7 zorder -99
        $ pathA = (nodeA, (0,0), (0,0), (0,0), nodeAA, nodeBB, (0,0), (0,0))
        $ pathAA = (nodeA, (0,0), (0,0), (0,0), nodeAA, (0,0), (0,0), (0,0))
        $ pathBB = (nodeA, (0,0), (0,0), (0,0), (0,0), nodeBB, (0,0), (0,0))
        
    if maplink == "3N":
        show M3 zorder -99
        $ pathA = (nodeA, (0,0), (0,0), (0,0), nodeAA, nodeBB, (0,0), nodeDD)
        $ pathAA = (nodeA, (0,0), (0,0), (0,0), nodeAA, (0,0), (0,0), (0,0))
        $ pathBB = (nodeA, (0,0), (0,0), (0,0), (0,0), nodeBB, (0,0), nodeDD)
        $ pathDD = (nodeA, (0,0), (0,0), (0,0), (0,0), nodeBB, (0,0), nodeDD)
        
    
    if maplink == "4N":
        show M4 zorder -99
        $ pathA = (nodeA, (0,0), (0,0), (0,0), nodeAA, nodeBB, nodeCC, nodeDD)
        $ pathAA = (nodeA, (0,0), (0,0), (0,0), nodeAA, (0,0), nodeCC, (0,0))
        $ pathBB = (nodeA, (0,0), (0,0), (0,0), (0,0), nodeBB, (0,0), nodeDD)
        $ pathCC = (nodeA, (0,0), (0,0), (0,0), nodeAA, (0,0), nodeCC, (0,0))
        $ pathDD = (nodeA, (0,0), (0,0), (0,0), (0,0), nodeBB, (0,0), nodeDD)
        

# East      
    if maplink == "1E":
        show M1 zorder -99:
            rotate 90
        $ pathA = (nodeA, (0,0), (0,0), (0,0), (0,0), nodeBB, (0,0), (0,0))
        $ pathBB = (nodeA, (0,0), (0,0), (0,0), (0,0), nodeBB, (0,0), (0,0))
        
    if maplink == "2E":
        show M2 zorder -99:
            rotate 90
        $ pathA = (nodeA, (0,0), (0,0), (0,0), (0,0), nodeBB, (0,0), nodeDD)
        $ pathBB = (nodeA, (0,0), (0,0), (0,0), (0,0), nodeBB, (0,0), nodeDD)
        $ pathDD = (nodeA, (0,0), (0,0), (0,0), (0,0), nodeBB, (0,0), nodeDD)
        
    if maplink == "7E":
        show M7 zorder -99:
            rotate 90
        $ pathA = (nodeA, (0,0), (0,0), (0,0), (0,0), nodeBB, nodeCC, (0,0))
        $ pathBB = (nodeA, (0,0), (0,0), (0,0), (0,0), nodeBB, (0,0), (0,0))
        $ pathCC = (nodeA, (0,0), (0,0), (0,0), (0,0), (0,0), nodeCC, (0,0))
        
    if maplink == "3E":
        show M3 zorder -99:
            rotate 90
        $ pathA = (nodeA, (0,0), (0,0), (0,0), nodeAA, nodeBB, nodeCC, (0,0))
        $ pathAA = (nodeA, (0,0), (0,0), (0,0), nodeAA, (0,0), nodeCC, (0,0))
        $ pathBB = (nodeA, (0,0), (0,0), (0,0), (0,0), nodeBB, (0,0), (0,0))
        $ pathCC = (nodeA, (0,0), (0,0), (0,0), nodeAA, (0,0), nodeCC, (0,0))
        
    if maplink == "4E":
        show M4 zorder -99
        $ pathA = (nodeA, (0,0), (0,0), (0,0), nodeAA, nodeBB, nodeCC, nodeDD)
        $ pathAA = (nodeA, (0,0), (0,0), (0,0), nodeAA, (0,0), nodeCC, (0,0))
        $ pathBB = (nodeA, (0,0), (0,0), (0,0), (0,0), nodeBB, (0,0), nodeDD)
        $ pathCC = (nodeA, (0,0), (0,0), (0,0), nodeAA, (0,0), nodeCC, (0,0))
        $ pathDD = (nodeA, (0,0), (0,0), (0,0), (0,0), nodeBB, (0,0), nodeDD)
  
        
# South      
    if maplink == "1S":
        show M1 zorder -99:
            rotate 180
        $ pathA = (nodeA, (0,0), (0,0), (0,0), (0,0), (0,0), nodeCC, (0,0))
        $ pathCC = (nodeA, (0,0), (0,0), (0,0), (0,0), (0,0), nodeCC, (0,0))
        
    if maplink == "2S":
        show M2 zorder -99:
            rotate 180
        $ pathA = (nodeA, (0,0), (0,0), (0,0), nodeAA, (0,0), nodeCC, (0,0))
        $ pathAA = (nodeA, (0,0), (0,0), (0,0), nodeAA, (0,0), nodeCC, (0,0))
        $ pathCC = (nodeA, (0,0), (0,0), (0,0), nodeAA, (0,0), nodeCC, (0,0))
        
    if maplink == "7S":
        show M7 zorder -99:
            rotate 180
        $ pathA = (nodeA, (0,0), (0,0), (0,0), (0,0), (0,0), nodeCC, nodeDD)
        $ pathCC = (nodeA, (0,0), (0,0), (0,0), (0,0), (0,0), nodeCC, (0,0))
        $ pathDD = (nodeA, (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), nodeDD)
        
    if maplink == "3S":
        show M3 zorder -99:
            rotate 180
        $ pathA = (nodeA, (0,0), (0,0), (0,0), (0,0), nodeBB, nodeCC, nodeDD)
        $ pathBB = (nodeA, (0,0), (0,0), (0,0), (0,0), nodeBB, (0,0), nodeDD)
        $ pathCC = (nodeA, (0,0), (0,0), (0,0), (0,0), (0,0), nodeCC, (0,0))
        $ pathDD = (nodeA, (0,0), (0,0), (0,0), (0,0), nodeBB, (0,0), nodeDD)
        
    if maplink == "4S":
        show M4 zorder -99
        $ pathA = (nodeA, (0,0), (0,0), (0,0), nodeAA, nodeBB, nodeCC, nodeDD)
        $ pathAA = (nodeA, (0,0), (0,0), (0,0), nodeAA, (0,0), nodeCC, (0,0))
        $ pathBB = (nodeA, (0,0), (0,0), (0,0), (0,0), nodeBB, (0,0), nodeDD)
        $ pathCC = (nodeA, (0,0), (0,0), (0,0), nodeAA, (0,0), nodeCC, (0,0))
        $ pathDD = (nodeA, (0,0), (0,0), (0,0), (0,0), nodeBB, (0,0), nodeDD)
    
            
# West     
    if maplink == "1W":
        show M1 zorder -99:
            rotate 270
        $ pathA = (nodeA, (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), nodeDD)
        $ pathDD = (nodeA, (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), nodeDD)
        
    if maplink == "2W":
        show M2 zorder -99:
            rotate 270
        $ pathA = (nodeA, (0,0), (0,0), (0,0), (0,0), nodeBB, (0,0), nodeDD)
        $ pathBB = (nodeA, (0,0), (0,0), (0,0), (0,0), nodeBB, (0,0), nodeDD)
        $ pathDD = (nodeA, (0,0), (0,0), (0,0), (0,0), nodeBB, (0,0), nodeDD)
        
    if maplink == "7W":
        show M7 zorder -99:
            rotate 270
        $ pathA = (nodeA, (0,0), (0,0), (0,0), nodeAA, (0,0), (0,0), nodeDD)
        $ pathAA = (nodeA, (0,0), (0,0), (0,0), nodeAA, (0,0), (0,0), (0,0))
        $ pathDD = (nodeA, (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), nodeDD)
        
    if maplink == "3W":
        show M3 zorder -99:
            rotate 270
        $ pathA = (nodeA, (0,0), (0,0), (0,0), nodeAA, (0,0), nodeCC, nodeDD)
        $ pathAA = (nodeA, (0,0), (0,0), (0,0), nodeAA, (0,0), nodeCC, (0,0))
        $ pathCC = (nodeA, (0,0), (0,0), (0,0), nodeAA, (0,0), nodeCC, (0,0))
        $ pathDD = (nodeA, (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), nodeDD)
        
    if maplink == "4W":
        show M4 zorder -99
        $ pathA = (nodeA, (0,0), (0,0), (0,0), nodeAA, nodeBB, nodeCC, nodeDD)
        $ pathAA = (nodeA, (0,0), (0,0), (0,0), nodeAA, (0,0), nodeCC, (0,0))
        $ pathBB = (nodeA, (0,0), (0,0), (0,0), (0,0), nodeBB, (0,0), nodeDD)
        $ pathCC = (nodeA, (0,0), (0,0), (0,0), nodeAA, (0,0), nodeCC, (0,0))
        $ pathDD = (nodeA, (0,0), (0,0), (0,0), (0,0), nodeBB, (0,0), nodeDD)
    
    
    return


    
