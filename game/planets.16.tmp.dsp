#planet information

# screen shown in orbital view
screen planet_info:
    vbox:
        pos (50,100)
        text "{color=#8dd35f}DATA"
        null height 10
        text "{color=#8dd35f}Name: [planet_name]"
        text "{color=#8dd35f}Type: [planet_type]"
        text "{color=#8dd35f}Size: [planet_size]"
        text "{color=#8dd35f}Moon(s): [planet_moons]"
        text "{color=#8dd35f}Atmosphere: [planet_atmosphere]"
        text "{color=#8dd35f}Temperature: [planet_temperature]"
        text "{color=#8dd35f}Radiations: [planet_radiations]"  
        text "{color=#8dd35f}Habitable: [planet_habitable]"
        text "{color=#8dd35f}Inhabited: [planet_inhabited]"
        text "{color=#8dd35f}Auth. needed: [planet_auth_needed]"
        text "{color=#8dd35f}Required ship: [planet_required_ship]"




init:
    
    # set orbit of planet
    $ planet = "none"
    
    #planet variables
    $ planet_name = "-"
    $ planet_type = "-"
    $ planet_size = "-"
    $ planet_moons = "-"
    $ planet_atmosphere = "-"
    $ planet_temperature = "-"
    $ planet_radiations = "-"
    $ planet_habitable = "-"
    $ planet_inhabited = "-"
    $ planet_auth_needed = "-"
    $ planet_required_ship = "-"
    
    #specific planet variables
    $ planetxy_auth = False


# planet info called by orbital view
label planet_info:
    
    #for testing only
    #$ planet = "planet1"
    
    
    if planet == "none":
        $ planet_name = "-"
        $ planet_type = "-"
        $ planet_size = "-"
        $ planet_moons = "-"
        $ planet_atmosphere = "-"
        $ planet_temperature = "-"
        $ planet_radiations = "-"
        $ planet_habitable = "-"
        $ planet_inhabited = "-"
        $ planet_auth_needed = "-"
        $ planet_required_ship = "-"
        
    if planet == "megaship":
        $ planet_name = "megaship"
        $ planet_type = "spaceship"
        $ planet_size = "2 km^3"
        $ planet_moons = "none"
        $ planet_atmosphere = "Yes"
        $ planet_temperature = "24"
        $ planet_radiations = "No"
        $ planet_habitable = "Yes"
        $ planet_inhabited = "Yes"
        $ planet_auth_needed = "No"
        $ planet_required_ship = "SD2+"
        
    
    if planet == "xylo":
        $ planet_name = "xylo"
        $ planet_type = "Planet"
        $ planet_size = "10000 km^3"
        $ planet_moons = "2"
        $ planet_atmosphere = "Yes"
        $ planet_temperature = "22"
        $ planet_radiations = "No"
        $ planet_habitable = "Yes"
        $ planet_inhabited = "Yes"
        $ planet_auth_needed = "Yes"
        $ planet_required_ship = "SD2+"
        
        
    if planet == "demo":
        $ planet_name = "Demo"
        $ planet_type = "Planet"
        $ planet_size = "12 km^3"
        $ planet_moons = "3"
        $ planet_atmosphere = "Yes"
        $ planet_temperature = "26"
        $ planet_radiations = "No"
        $ planet_habitable = "Yes"
        $ planet_inhabited = "Yes"
        $ planet_auth_needed = "No"
        $ planet_required_ship = "SD2+"
        
        
    if planet == "sat-io11":
        $ planet_name = "Io-11"
        $ planet_type = "Satellite"
        $ planet_size = "10 m^3"
        $ planet_moons = "none"
        $ planet_atmosphere = "No"
        $ planet_temperature = "-60"
        $ planet_radiations = "No"
        $ planet_habitable = "No"
        $ planet_inhabited = "No"
        $ planet_auth_needed = "No"
        $ planet_required_ship = "SD2+"
    
    
    return
