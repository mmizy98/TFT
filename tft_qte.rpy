#qte
screen tft_qte_start(pressed_key, time):
    add "tft_qte_button" xalign 0.5 yalign 0.5
    key pressed_key action [ Hide("tft_qte_start"), Return() ] 
    text "{font=[furore]}[pressed_key]" pos (907, 390) size 150 color "#ffffff"
    timer time action [ Hide("tft_qte_start"), SetVariable("tft_qte_loose", True), Return() ]
    add "tft_qte_bar" xalign 0.5 yalign 0.3

label tft_qte_label(count=1, time=2):
    $ tft_qte_count = count
    while tft_qte_count > 0:
        if tft_qte_loose:
            pass
        else:
            call screen tft_qte_start(TFTgetRandomButton(),time)
        $ tft_qte_count -= 1
    return



screen tft_qte2_start(pressed_key, time):
    add "tft_qte_button" xalign 0.5 yalign 0.5
    key pressed_key action [ Hide("tft_qte2_start"), Return() ] 
    text "{font=[furore]}[pressed_key]" pos (907, 390) size 150 color "#ffffff"
    timer time action [ Hide("tft_qte2_start"), SetVariable("tft_qte2_loose", True), Return() ]
    add "tft_qte_bar" xalign 0.5 yalign 0.3

label tft_qte2_label(count=1, time=2):
    $ tft_qte2_count = count
    while tft_qte2_count > 0:
        if tft_qte2_loose:
            pass
        else:
            call screen tft_qte2_start(TFTgetRandomButton(),time)
        $ tft_qte2_count -= 1
    return

screen tft_qte3_start(pressed_key, time):
    add "tft_qte_button" xalign 0.5 yalign 0.5
    key pressed_key action [ Hide("tft_qte3_start"), Return() ] 
    text "{font=[furore]}[pressed_key]" pos (907, 390) size 150 color "#ffffff"
    timer time action [ Hide("tft_qte3_start"), SetVariable("tft_qte3_loose", True), Return() ]
    add "tft_qte_bar" xalign 0.5 yalign 0.3

label tft_qte3_label(count=1, time=2):
    $ tft_qte3_count = count
    while tft_qte3_count > 0:
        if tft_qte3_loose:
            pass
        else:
            call screen tft_qte3_start(TFTgetRandomButton(),time)
        $ tft_qte3_count -= 1
    return