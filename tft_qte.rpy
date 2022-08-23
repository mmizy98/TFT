#qte
screen tft_qte_start(pressed_key, time):
    add "tft_qte_button" xalign 0.5 yalign 0.5
    key pressed_key action [ Hide("tft_qte_start"), Return() ] 
    text "{font=[furore]}[pressed_key]" pos (907, 390) size 150 color "#ffffff"
    timer time action [ Hide("tft_qte_start"), SetVariable("qte_loose", True), Return() ]
    add "tft_qte_bar" xalign 0.5 yalign 0.3

label tft_qte_label(count=1, time=2):
    $ qte_count = count
    while qte_count > 0:
        if qte_loose:
            pass
        else:
            call screen tft_qte_start(TFTgetRandomButton(),time)
        $ qte_count -= 1
    return