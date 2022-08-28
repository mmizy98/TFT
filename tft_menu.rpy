label tft_menu_main:
    $ day_time()
    scene int_staircase_7dl with dissolve
    call screen tft_menu with dissolve

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

screen Get_Achieve_1:
    add "achieve_day3_qte_win":
        at transform:
            xpos 1921 ypos 1015
            ease_back 1.5 xpos 1600
            pause 1.5
            ease_back 1.5 xpos 1930
    timer 4.0 action [ Hide("Get_Achieve_1"), Jump("volleyball_end") ]

screen Get_Achieve_2:
    add "achieve_day3_qte_almost":
        at transform:
            xpos 1921 ypos 1015
            ease_back 1.5 xpos 1600
            pause 1.5
            ease_back 1.5 xpos 1930
    timer 4.0 action [ Hide("Get_Achieve_2"), Jump("volleyball_end") ]

screen Get_Achieve_3:
    add "achieve_day3_qte_loose":
        at transform:
            xpos 1921 ypos 1015
            ease_back 1.5 xpos 1600
            pause 1.5
            ease_back 1.5 xpos 1930
    timer 4.0 action [ Hide("Get_Achieve_3"), Jump("volleyball_end") ]

screen Get_Achieve_4:
    add "achieve_day3_nice_punch":
        at transform:
            xpos 1921 ypos 1015
            ease_back 1.5 xpos 1600
            pause 1.5
            ease_back 1.5 xpos 1930
    timer 4.0 action [ Hide("Get_Achieve_3"), Jump("arseniy_after_vallyball") ]

screen Get_Achieve_5:
    add "achieve_menu_easter_egg":
        at transform:
            xpos 1921 ypos 1015
            ease_back 1.5 xpos 1600
            pause 1.5
            ease_back 1.5 xpos 1930
    timer 4.0 action [ Hide("Get_Achieve_5"), Jump("tft_menu_main") ]

label tft_menu_easter_egg:
    $ tft_achievment_5 = True
    scene black with Dissolve(1.5)
    scene pirat_prewiew with dspr
    $ renpy.movie_cutscene(getFile("pirat_video.webm"))
    if tft_achievment_5:
        $ tft_achievment_5_count = 1
        play sound sfx_achievement
        call screen Get_Achieve_5
        