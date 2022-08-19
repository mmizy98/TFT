screen tft_qte_green_start(pressed_key, time):
    add "tft_qte_anim_button_green" xalign 0.5 yalign 0.5
    key pressed_key action [ Hide("tft_qte_green_start"), Return() ] 
    text "[pressed_key]" xalign 0.5 yalign 0.5 size 150 color "#288520"
    timer time action [ Hide("tft_qte_green_start"), SetVariable("tft_qte_loose", True), Return() ]

label tft_qte_green_start(count=1, time=2):
    $ tft_qte_count = count
    while tft_qte_count > 0:
        if tft_qte_loose:
            pass
        else:
            call screen tft_qte_green_start(TFTgetRandomButton(),time)
        $ tft_qte_count -= 1
    return

screen tft_qte_blue_start(pressed_key, time):
    add "tft_qte_anim_button_blue" xalign 0.5 yalign 0.5
    key pressed_key action [ Hide("tft_qte_blue_label"), Return() ] 
    text "[pressed_key]" xalign 0.5 yalign 0.5 size 150 color "#6256a6"
    timer time action [ Hide("tft_qte_blue_label"), SetVariable("tft_qte_loose", True), Return() ]

label tft_qte_blue_label(count=1, time=2):
    $ tft_qte_count = count
    while tft_qte_count > 0:
        if tft_qte_loose:
            pass
        else:
            call screen tft_qte_blue_start(TFTgetRandomButton(),time)
        $ tft_qte_count -= 1
    return