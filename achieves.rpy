
#ЛЭЙБЛ ЭКРАНА ДОСТИЖЕНИЙ
label achs:
    scene ach_bg
    call screen ach

#ЭКРРАН ДОСТИЖЕНИЙ (НЕДОПИЛ)
screen ach:
    tag menu
    imagebutton:
        xpos 300 ypos 150
        idle getFile("gui/achievements/achieve_locked.png")
        hover getFile("gui/achievements/achieve_locked_hover.png")
        hovered Play("sfx_2", sfx_menu_selected)
        action [ ShowMenu ("achs_inwork") ]
    imagebutton:
        xpos 810 ypos 150
        idle getFile("gui/achievements/achieve_locked.png")
        hover getFile("gui/achievements/achieve_locked_hover.png")
        hovered Play("sfx_2", sfx_menu_selected)
        action [ ShowMenu ("achs_inwork") ]
    imagebutton:
        xpos 1320 ypos 150
        idle getFile("gui/achievements/achieve_locked.png")
        hover getFile("gui/achievements/achieve_locked_hover.png")
        hovered Play("sfx_2", sfx_menu_selected)
        action [ ShowMenu ("achs_inwork") ]
    imagebutton:
        xpos 300 ypos 250
        idle getFile("gui/achievements/achieve_locked.png")
        hover getFile("gui/achievements/achieve_locked_hover.png")
        hovered Play("sfx_2", sfx_menu_selected)
        action [ ShowMenu ("achs_inwork") ]
    imagebutton:
        xpos 810 ypos 250
        idle getFile("gui/achievements/achieve_locked.png")
        hover getFile("gui/achievements/achieve_locked_hover.png")
        hovered Play("sfx_2", sfx_menu_selected)
        action [ ShowMenu ("achs_inwork") ]
    imagebutton:
        xpos 1320 ypos 250
        idle getFile("gui/achievements/achieve_locked.png")
        hover getFile("gui/achievements/achieve_locked_hover.png")
        hovered Play("sfx_2", sfx_menu_selected)
        action [ ShowMenu ("achs_inwork") ]
    imagebutton:
        xpos 300 ypos 350
        idle getFile("gui/achievements/achieve_locked.png")
        hover getFile("gui/achievements/achieve_locked_hover.png")
        hovered Play("sfx_2", sfx_menu_selected)
        action [ ShowMenu ("achs_inwork") ]
    imagebutton:
        xpos 810 ypos 350
        idle getFile("gui/achievements/achieve_locked.png")
        hover getFile("gui/achievements/achieve_locked_hover.png")
        hovered Play("sfx_2", sfx_menu_selected)
        action [ ShowMenu ("achs_inwork") ]
    imagebutton:
        xpos 1320 ypos 350
        idle getFile("gui/achievements/achieve_locked.png")
        hover getFile("gui/achievements/achieve_locked_hover.png")
        hovered Play("sfx_2", sfx_menu_selected)
        action [ ShowMenu ("achs_inwork") ]
    imagebutton:
        xalign 0.98 yalign 0.98
        auto getFile("gui/button_back_%s.png")
        action [ ShowMenu ("tft_menu_main") ]

#ДОСТИЖЕНИЯ В РАЗРАБОТКЕ
screen achs_inwork:
    tag menu
    text "{font=[cinzel_bold]}ПРОСТИ, ДРУГ, ДОСТИЖЕНИЯ ЕЩЁ В РАЗРАБОТКЕ :(" xalign 0.5 yalign 0.45 size 50 color "#ffffff"
    text "{font=[cinzel_bold]}А ПОКА ПОПРОБУЙ НАЙТИ ПАСХАЛКУ В МЕНЮ!" xalign 0.5 yalign 0.55 size 50 color "#ffffff"
    imagebutton:
        xalign 0.98 yalign 0.98
        auto getFile("gui/button_back_%s.png")
        action [ ShowMenu ("ach") ]

#ЭКРАН ДОСТИЖЕНИЙ
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

#ПЕРЕМЕННЫЕ ДОСТИЖЕНИЙ:
    $ persistent.achievment_1 = False
    $ tft_achievment_1_count = 0

    $ persistent.achievment_2 = False
    $ tft_achievment_2_count = 0

    $ persistent.achievment_3 = False
    $ tft_achievment_3_count = 0

    $ persistent.achievment_4 = False
    $ tft_achievment_4_count = 0

    $ persistent.achievment_5 = False
    $ tft_achievment_5_count = 0