
# sounds



init:
    $ steps_sound = "concrete"
    
    
    $ renpy.music.register_channel("alarm_channel", mixer=None, loop=None, stop_on_mute=True, tight=False, file_prefix='', file_suffix='', buffer_queue=True, movie=False, framedrop=False)
    
    $ renpy.music.set_volume(0.5, delay=0, channel='music')
    
    
    
    # atmo channel
    $ renpy.music.register_channel("atmo", mixer="atmo", loop=True, stop_on_mute=True, tight=True, file_prefix='', file_suffix='', buffer_queue=True, movie=False, framedrop=False)
    #$ renpy.music.set_volume(0.5, delay=0, channel='atmo')
    
    
    # register atmo and alarm to sound instead of music???


label sound_door:
    play sound "sounds/door-open.ogg"
    return
    
label sound_door_locked:
    play sound "sounds/door-locked.ogg"
    #call dialog_closed
    #with hpunch
    return
    
    
label sound_connected:
    play sound "sounds/connected.ogg"
    return
    
label sound_beep:
    play sound "sounds/beep.ogg"
    return
    
    
label sound_collect:
    play sound "sounds/collect.ogg"
    return
    
    
label sound_take_off:
    play sound "sounds/takeoff.ogg"
    return
    

label sound_lift:
    play sound "sounds/lift.ogg" 
    return
    
label sound_electroshock:
    play sound "sounds/bzz.ogg"
    return
    

label sound_scan:
    play sound "sounds/scan.ogg" 
    return
    
    
label sound_hyperspace:
    play sound "sounds/hyperspace.ogg" 
    return
    
    
label sound_movingwall:
    play sound "sounds/movingwall.ogg" 
    return
    
    
label sound_tap:
    play sound "sounds/tap.ogg" 
    return
    
label sound_flush:
    play sound "sounds/flush.ogg" 
    return
    
    
label sound_paper:
    play sound "sounds/paper.ogg" 
    return
    
    
label sound_screw:
    play sound "sounds/screw.ogg" 
    return
    
label sound_search:
    #play sound "sounds/search.ogg" 
    return
    
    
label sound_modem:
    play sound "sounds/modem.ogg" 
    return
    
    
label sound_alarm:
    play alarm_channel "sounds/alarm.ogg" loop
    return


label sound_ignition:
    play sound "sounds/ignition.ogg"
    return

label sound_explosion:
    play audio "sounds/boom.ogg"
    return
    
label sound_earthquake:
    play sound "sounds/earthquake.ogg"
    return
    
label sound_dig:
    play sound "sounds/dig.ogg"
    return
    
label sound_crane:
    play audio "sounds/crane.ogg"
    return
    
label sound_crane_sound:
    play sound "sounds/crane.ogg"
    return
    
label sound_train:
    play sound "sounds/train.ogg"
    
    return
    
label sound_minitrain_loop:
    #play audio "sounds/train.ogg"
    $ renpy.music.play("sounds/conveyor.ogg", channel="sound", fadein=1, fadeout=1, tight=True, if_changed=True, loop=True)
    return
    
label sound_propulsion:
    play audio "sounds/propulsion.ogg"
    return
    
label sound_small_propulsion:
    play audio "sounds/small-propulsion.ogg"
    return
    
    
    
#label sound_steps:
    #if steps_sound == "concrete":
    #    play sound "sounds/steps_concrete.ogg"
    
    #if steps_sound == "metal":
    #    play sound "sounds/steps_metal.ogg"
    
    #return
    
    
    
    
label atmo_conveyor:
    #play atmo "sounds/conveyor.ogg"
    $ renpy.music.play("sounds/conveyor.ogg", channel="atmo", fadein=0, fadeout=0, tight=True, if_changed=True)
    return

label atmo_reactor:
    #play atmo "sounds/reactor.ogg"
    $ renpy.music.play("sounds/reactor.ogg", channel="atmo", fadein=0, fadeout=0, tight=True, if_changed=True)
    return
    
    
label sound_title:
    play sound "sounds/title.ogg"
    return
    
    
    
label atmo_spaceship:
    #play atmo "sounds/spaceship.ogg"
    
    $ renpy.music.play("sounds/spaceship.ogg", channel="atmo", fadein=0, fadeout=0, tight=True, if_changed=True)
    return

label atmo_spaceship_hum:
    $ renpy.music.play("sounds/spaceship-hum.ogg", channel="atmo", fadein=0.5, fadeout=0.5, tight=True, if_changed=True)
    return
    
label atmo_spaceport:
    $ renpy.music.play("sounds/spaceport.ogg", channel="atmo", fadein=0, fadeout=0, tight=True, if_changed=True)
    return
    
label atmo_village:
    $ renpy.music.play("sounds/village.ogg", channel="atmo", fadein=0.5, fadeout=0.5, tight=True, if_changed=True)
    return
    
label atmo_sea:
    $ renpy.music.play("sounds/sea.ogg", channel="atmo", fadein=1, fadeout=1, tight=True, if_changed=True)
    return
    
    
label atmo_ground:
    $ renpy.music.play("sounds/spaceport-ground.ogg", channel="atmo", fadein=0, fadeout=0, tight=True, if_changed=True)
    return
    
label atmo_wind:
    $ renpy.music.play("sounds/wind.ogg", channel="atmo", fadein=0, fadeout=0, tight=True, if_changed=True)
    return
    
label atmo_cave:
    $ renpy.music.play("sounds/cave.ogg", channel="atmo", fadein=0, fadeout=0, tight=True, if_changed=True)
    return
    
label atmo_deep_ambiance:
    $ renpy.music.play("sounds/spaceship-amb.ogg", channel="atmo", fadein=0, fadeout=0, tight=True, if_changed=True)
    return
    
label atmo_base:
    $ renpy.music.play("sounds/base.ogg", channel="atmo", fadein=0, fadeout=0, tight=True, if_changed=True)
    return
    
#label atmo_polarbase:
#    $ renpy.music.play("sounds/polarbase.ogg", channel="atmo", fadein=0, fadeout=0, tight=True, if_changed=True)
#    return
    
label atmo_spaceship_station:
    $ renpy.music.play("sounds/spaceship-station.ogg", channel="atmo", fadein=0, fadeout=0, tight=True, if_changed=True)
    return
    
    
#label atmo_nature:
#    $ renpy.music.play("sounds/nature.ogg", channel="atmo", fadein=0, fadeout=0, tight=True, if_changed=True)
#    return










    
#################################
#music


label music_space:
    #$ renpy.music.set_volume(0.7, delay=0, channel='music')
    #play music "music/Sci-Fi-Open_Looping.mp3" fadein 1.0 fadeout 1.0
    
    # atmo
    #$ renpy.music.play("sounds/spaceship.ogg", channel='music', loop=True, fadeout=0, synchro_start=False, fadein=0, tight=None, if_changed=True)
    
    
    $ renpy.music.play("music/space.ogg", channel="music", fadein=0, fadeout=0, tight=True, if_changed=True)
    return
    
    
    
label music_intro:
    $ renpy.music.play("music/intro.ogg", channel="music", fadein=1, fadeout=1, tight=True, if_changed=True)
    return


label music_drops:
    $ renpy.music.play("music/drops.ogg", channel="music", fadein=1, fadeout=1, tight=True, if_changed=True)
    return
    
label music_shop:
    $ renpy.music.play("music/shop.ogg", channel="music", fadein=0, fadeout=0, tight=True, if_changed=True)
    return
    
    
    
    
# bars    
label music_bar_village:
    $ renpy.music.play("music/bar-village.ogg", channel="music", fadein=0, fadeout=0, tight=True, if_changed=True)
    return
    
label music_bar_village_deep:
    $ renpy.music.play("music/bar-village-deep.ogg", channel="music", fadein=0, fadeout=0, tight=True, if_changed=True)
    return
   
#    
label music_bar_sea:
    $ renpy.music.play("music/bar.ogg", channel="music", fadein=0, fadeout=0, tight=True, if_changed=True)
    return
#    
label music_bar_sea_deep:
    $ renpy.music.play("music/bar-deep.ogg", channel="music", fadein=0, fadeout=0, tight=True, if_changed=True)
    return
   
   
label music_bar_chill:
    $ renpy.music.play("music/bar-chill.ogg", channel="music", fadein=0, fadeout=0, tight=True, if_changed=True)
    return


label music_bar_chill_deep:
    $ renpy.music.play("music/bar-chill-deep.ogg", channel="music", fadein=0, fadeout=0, tight=True, if_changed=True)
    return
   
   
   
label music_outro:
    $ renpy.music.play("music/outro.ogg", channel="music", fadein=0, fadeout=0, tight=True, if_changed=True)
    return
    
label music_outro_bar:
    $ renpy.music.play("<from 19.83>music/outro.ogg", channel="music", fadein=0, fadeout=0, tight=True, if_changed=True)
    return
    
label music_outro_deep:
    $ renpy.music.play("music/outro-deep.ogg", channel="music", fadein=0, fadeout=0, tight=True, if_changed=True)
    return
   
   
   
   
label music_surface:
    $ renpy.music.play("music/surface.ogg", channel="music", fadein=1, fadeout=1, tight=True, if_changed=True)
    return   


# village building
label music_xylo_building: 
    $ renpy.music.play("music/xylo-building.ogg", channel="music", fadein=0, fadeout=0, tight=True, if_changed=True)
    return
    
    

    
label music_satellite:
    $ renpy.music.play("<from 54.70>music/space-amb.ogg", channel="music", fadein=0, fadeout=0, tight=True, if_changed=True)
    return
    


    
label music_cargo:
    $ renpy.music.play("music/cargo.ogg", channel="music", fadein=0, fadeout=0, tight=True, if_changed=True)
    return
    
label music_isc:
    $ renpy.music.play("music/isc.ogg", channel="music", fadein=0, fadeout=0, tight=True, if_changed=True)
    return
    

    






