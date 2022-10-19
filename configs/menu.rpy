#ЛЭЙБЛ МЕНЮ
label tft_menu_main:
    stop sound_loop
    stop music
    play music letov_u_okna fadein 10 volume 0.4
    stop ambience
    $ updVisual()
    $ day_time()
    scene int_staircase_7dl with dissolve
    call screen tft_menu with dissolve

#ЭКРАН МЕНЮ
screen tft_menu:
    tag menu
    imagebutton:
        xpos 460 ypos 140
        auto getFile("gui/menu/tft_start_%s.png")
        hovered Play("sfx_2", sfx_menu_selected)
        action [ Play("sfx_3", sfx_menu_select), Jump ("tft_disclaimer") ]
    imagebutton:
        xpos 417 ypos 190
        auto getFile("gui/menu/tft_load_%s.png")
        hovered Play("sfx_2", sfx_menu_selected)
        action [ Play("sfx_3", sfx_menu_select), ShowMenu('load') ]
    imagebutton:
        xpos 437 ypos 240
        auto getFile("gui/menu/tft_settings_%s.png")
        hovered Play("sfx_2", sfx_menu_selected)
        action [ Play("sfx_3", sfx_menu_select), ShowMenu('preferences') ]
    imagebutton:
        xpos 476 ypos 300
        auto getFile("gui/menu/tft_exit_%s.png")
        hovered Play("sfx_2", sfx_menu_selected)
        action [ Play("sfx_3", sfx_menu_select), MainMenu() ]
    imagebutton:
        xpos 701 ypos 390
        auto getFile("gui/menu/tft_door_ding_%s.png")
        action [ Play("sfx_3", sfx_door_ding), Jump ("tft_menu_easter_egg")  ]

#ПАСХАЛКА
label tft_menu_easter_egg:
    $ tft_achievment_5 = True
    scene black with Dissolve(1.5)
    scene pirat_prewiew with dspr
    $ renpy.movie_cutscene(getFile("gui/pirat_video.webm"))
    if tft_achievment_5:
        $ tft_achievment_5_count = 1
        play sound sfx_achievement
        call screen Get_Achieve_5

#ДИСКЛЕЙМЕР
label tft_disclaimer:
    stop music fadeout 3
    scene black with Dissolve(3)
    call screen disclaimer_screen

#ЭКРАН ДИСКЛЕЙМЕРА
screen disclaimer_screen:
    tag menu
    add "qte_alert" pos (0,0)
    timer 15.0 action [ Jump("tft_prolog") ]
    text "{font=[cinzel_bold]}ДИСКЛЕЙМЕР" xalign 0.5 yalign 0.1 size 100 color "#ff0000"
    text "{font=[cinzel_bold]}В МОДЕ ПРИСУТСТВУЕТ QTE, О НЁМ ВАС УВЕДОМИТ ЗНАЧОК В ЛЕВОМ ВЕРХНЕМ УГЛУ" pos (20, 360) size 40 color "#fff"
    text "{font=[cinzel_bold]}ПЕРЕД ПРОЧТЕНИЕМ УБЕДИТЕСЬ ЧТО У ВАС СТОИТ АНГЛИЙСКАЯ РАСКЛАДКА И ВЫКЛЮЧЕН CAPS LOCK" pos (20, 460) size 40 color "#fff"
    text "{font=[cinzel_bold]}ЕСЛИ ПОСЛЕ ПРОХОЖДЕНИЯ У ВАС ОСТАЛИСЬ ВОПРОСЫ ПО СЮЖЕТУ ИЛИ ВЫ НАШЛИ БАГ, ОБЯЗАТЕЛЬНО ОСТАВЬТЕ ФИДБЕК В STEAM" pos (20, 600) size 40 color "#fff"


