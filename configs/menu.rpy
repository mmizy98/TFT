#======================================#
#ЛЭЙБЛ МЕНЮ
label tft_menu_main:
    $ day_time()
    scene int_staircase_7dl with dissolve
    call screen tft_menu with dissolve
#======================================#
#САМО МЕНЮ
screen tft_menu:
    imagebutton:
        xpos 459 ypos 136
        auto getFile("gui/menu/tft_start_%s.png")
        hovered Play("sfx_2", sfx_menu_selected)
        action [ Play("sfx_3", sfx_menu_select), Jump ("tft_prolog") ]
    imagebutton:
        xpos 417 ypos 187
        auto getFile("gui/menu/tft_load_%s.png")
        hovered Play("sfx_2", sfx_menu_selected)
        action [ Play("sfx_3", sfx_menu_select), ShowMenu('load') ]
    imagebutton:
        xpos 417 ypos 104
        auto getFile("gui/menu/tft_achieves_%s.png")
        hovered Play("sfx_2", sfx_menu_selected)
        action [ Play("sfx_3", sfx_menu_select), ShowMenu('load') ]
    imagebutton:
        xpos 437 ypos 235
        auto getFile("gui/menu/tft_settings_%s.png")
        hovered Play("sfx_2", sfx_menu_selected)
        action [ Play("sfx_3", sfx_menu_select), ShowMenu('preferences') ]
    imagebutton:
        xpos 476 ypos 293
        auto getFile("gui/menu/tft_exit_%s.png")
        hovered Play("sfx_2", sfx_menu_selected)
        action [ Play("sfx_3", sfx_menu_select), MainMenu() ]
    imagebutton:
        xpos 701 ypos 390
        auto getFile("gui/menu/tft_door_ding_%s.png")
        action [ Play("sfx_3", sfx_door_ding), Jump ("tft_menu_easter_egg")  ]
#======================================#
#ПАСХАЛКА
label tft_menu_easter_egg:
    $ tft_achievment_5 = True
    scene black with Dissolve(1.5)
    scene pirat_prewiew with dspr
    $ renpy.movie_cutscene(getFile("pirat_video.webm"))
    if tft_achievment_5:
        $ tft_achievment_5_count = 1
        play sound sfx_achievement
        call screen Get_Achieve_5
#======================================#
        