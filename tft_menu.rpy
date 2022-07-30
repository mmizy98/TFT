label tft_menu_plus:
    $ day_time()
    play ambience ambience_ext_road_day
    scene vorota with dspr
    call screen tft_menu with dissolve
            
label tft_menu_main:
    $ day_time()
    play ambience ambience_ext_road_day
    scene vorota with dissolve2
    call screen tft_menu with dissolve

label tft_menu_tracklist:
    call screen tft_tracklist with dissolve

label tft_menu_exit:
    return