label tft_menu_main:
    $ day_time()
    scene int_staircase_7dl with dissolve
    call screen tft_menu with dissolve
    play ambience ambience_forest_evening

screen tft_menu_selector:
    tag menu
    modal True
    $ timeofday = persistent.timeofday
    $ time_of_day = persistent.timeofday
    button:
        style "blank_button"
        xalign 0 yalign 0
        xfill True
        yfill True
        action Return()
    
    add "image/screens/menu/lil_menu.png":
        xalign 0.5 yalign 0.5

    imagebutton:
        xalign 0.5 yalign 0.30
        auto "image/screens/menu/tft_lil_exit_button_%s.png"
        style "button_none"
        action [ Function(toDefaultSettings), MainMenu() ]
    imagebutton:
        xalign 0.5 yalign 0.40
        auto "image/screens/menu/tft_lil_save_button_%s.png"
        style "button_none"
        action ShowMenu('dpa_Save')
    imagebutton:
        xalign 0.5 yalign 0.50
        auto "image/screens/menu/tft_lil_load_button_%s.png"
        style "button_none"
        action ShowMenu('tft_Load')

screen tft_menu:
        imagebutton:
            xpos 459 ypos 136
            auto "mods/TFT/image/screens/menu/tft_start_%s.png"
            hovered Play("sfx_2", sfx_menu_selected)
            action [ Play("sfx_3", sfx_menu_select), Jump ("tft_prolog") ]
        imagebutton:
            xpos 417 ypos 187
            auto "mods/TFT/image/screens/menu/tft_load_%s.png"
            hovered Play("sfx_2", sfx_menu_selected)
            action [ Play("sfx_3", sfx_menu_select), ShowMenu('load') ]
        imagebutton:
            xpos 437 ypos 235
            auto "mods/TFT/image/screens/menu/tft_settings_%s.png"
            hovered Play("sfx_2", sfx_menu_selected)
            action [ Play("sfx_3", sfx_menu_select), ShowMenu('preferences') ]
        imagebutton:
            xpos 476 ypos 293
            auto "mods/TFT/image/screens/menu/tft_exit_%s.png"
            hovered Play("sfx_2", sfx_menu_selected)
            action [ Play("sfx_3", sfx_menu_select), Function(toDefaultSettings), MainMenu() ]
        imagebutton:
            xpos 701 ypos 390
            auto "mods/TFT/image/screens/menu/tft_door_ding_%s.png"
            action [ Play("sfx_3", sfx_door_ding) ]
init -97:
    image tft_qte_anim_button_green:
        "mods/TFT/image/screens/qte_buttons/qte_button_green1.png"
        0.2
        "mods/TFT/image/screens/qte_buttons/qte_button_green.png"
        0.2
        repeat
    image tft_qte_anim_button_blue:
        "mods/TFT/image/screens/qte_buttons/qte_button_blue1.png"
        0.2
        "mods/TFT/image/screens/qte_buttons/qte_button_blue.png"
        0.2
        repeat
    image tft_qte_anim_button_red:
        "mods/TFT/image/screens/qte_buttons/qte_button_blue1.png"
        0.2
        "mods/TFT/image/screens/qte_buttons/qte_button_blue.png"
        0.2
        repeat