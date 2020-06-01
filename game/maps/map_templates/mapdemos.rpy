
label mapdemos:
    scene bgcolor
    
    show text "special demo scenes" at truecenter
    
    menu:
        
        "moving walls":
            menu:
                "moving walls A":
                    $ startpos = 1
                    jump movingwalls
                
                "moving walls CC":
                    $ startpos = 33
                    jump movingwalls
            
        "crossroom":
            $ startpos = 1
            jump crossroom
            
        
        "exit":
            $ landing = False
            jump map6
