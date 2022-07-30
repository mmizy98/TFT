screen qte_start(pressed_key, time):
    add "qte_anim_button" xalign 0.5 yalign 0.5
    key pressed_key action [ Hide("qte_start"), Return() ] 
    text "[pressed_key]" xalign 0.5 yalign 0.5 size 380 color "#c51d1d"
    text "Жми!" align(0.5, 0.85) size 60
    timer time action [ Hide("qte_start"), SetVariable("qte_loose", True), Return() ]

label qte_label(count=1, time=2):
    $ qte_count = count
    while qte_count > 0:
        if qte_loose:
            pass
        else:
            call screen qte_start(getRandomButton(),time)
        $ qte_count -= 1
    return