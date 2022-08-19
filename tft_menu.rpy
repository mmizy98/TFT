label tft_menu_main:
    $ day_time()
    scene menu_fone with dissolve
    show tft_menu_background with dissolve:
        pos (0, 0)
    call screen tft_menu with dissolve
    play ambience ambience_forest_evening

label tft_car:
    scene black with Dissolve(4)
    "Здесь был Mantgxe6."

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