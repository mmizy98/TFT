#ЭКРРАНЫ QTE
screen tft_qte_start(pressed_key, time):
    add "tft_qte_button" xalign 0.5 yalign 0.5
    key pressed_key action [ Hide("tft_qte_start"), Return() ] 
    text "{font=[furore]}[pressed_key]" pos (907, 390) size 150 color "#ffffff"
    timer time action [ Hide("tft_qte_start"), SetVariable("tft_qte_loose", True), Return() ]
    add "tft_qte_bar" xalign 0.5 yalign 0.3

screen tft_qte2_start(pressed_key, time):
    add "tft_qte_button" xalign 0.5 yalign 0.5
    key pressed_key action [ Hide("tft_qte2_start"), Return() ] 
    text "{font=[furore]}[pressed_key]" pos (907, 390) size 150 color "#ffffff"
    timer time action [ Hide("tft_qte2_start"), SetVariable("tft_qte2_loose", True), Return() ]
    add "tft_qte_bar" xalign 0.5 yalign 0.3

#ЛЭЙБЛЫ QTE
label tft_qte_label(count=1, time=2):
    $ tft_qte_count = count
    while tft_qte_count > 0:
        if tft_qte_loose:
            pass
        else:
            call screen tft_qte_start(TFTgetRandomButton(),time)
        $ tft_qte_count -= 1
    return

label tft_qte2_label(count=1, time=2):
    $ tft_qte2_count = count
    while tft_qte2_count > 0:
        if tft_qte2_loose:
            pass
        else:
            call screen tft_qte2_start(TFTgetRandomButton(),time)
        $ tft_qte2_count -= 1
    return

#ПРЕДУПРЕЖДЕНИЕ О QTE
    image qte_alert:
        getFile("gui/qte/qte_alert_4.png")
        0.3
        getFile("gui/qte/qte_alert_3.png")
        0.3
        getFile("gui/qte/qte_alert_2.png")
        0.3
        getFile("gui/qte/qte_alert_1.png")
        0.3
        getFile("gui/qte/qte_alert_2.png")
        0.3
        getFile("gui/qte/qte_alert_3.png")
        0.3
        getFile("gui/qte/qte_alert_4.png")
        repeat

#КНОПКА QTE
    image tft_qte_button:
        getFile("gui/qte/tft_qte_button.png")

#ТАЙМЕР
    image tft_qte_bar:
        getFile("gui/qte/tft_qte_bar1.png")
        0.025
        getFile("gui/qte/tft_qte_bar2.png")
        0.025
        getFile("gui/qte/tft_qte_bar3.png")
        0.025
        getFile("gui/qte/tft_qte_bar4.png")
        0.025
        getFile("gui/qte/tft_qte_bar5.png")
        0.025
        getFile("gui/qte/tft_qte_bar6.png")
        0.025
        getFile("gui/qte/tft_qte_bar7.png")
        0.025
        getFile("gui/qte/tft_qte_bar8.png")
        0.025
        getFile("gui/qte/tft_qte_bar9.png")
        0.025
        getFile("gui/qte/tft_qte_bar10.png")
        0.025
        getFile("gui/qte/tft_qte_bar11.png")
        0.025
        getFile("gui/qte/tft_qte_bar12.png")
        0.025
        getFile("gui/qte/tft_qte_bar13.png")
        0.025
        getFile("gui/qte/tft_qte_bar14.png")
        0.025
        getFile("gui/qte/tft_qte_bar15.png")
        0.025
        getFile("gui/qte/tft_qte_bar16.png")
        0.025
        getFile("gui/qte/tft_qte_bar17.png")
        0.025
        getFile("gui/qte/tft_qte_bar18.png")
        0.025
        getFile("gui/qte/tft_qte_bar19.png")
        0.025
        getFile("gui/qte/tft_qte_bar20.png")
        0.025
        getFile("gui/qte/tft_qte_bar21.png")
        0.025
        getFile("gui/qte/tft_qte_bar22.png")
        0.025
        getFile("gui/qte/tft_qte_bar23.png")
        0.025
        getFile("gui/qte/tft_qte_bar24.png")
        0.025
        getFile("gui/qte/tft_qte_bar25.png")
        0.025
        getFile("gui/qte/tft_qte_bar26.png")
        0.025
        getFile("gui/qte/tft_qte_bar27.png")
        0.025
        getFile("gui/qte/tft_qte_bar28.png")
        0.025
        getFile("gui/qte/tft_qte_bar29.png")
        0.025
        getFile("gui/qte/tft_qte_bar30.png")
        0.025
        getFile("gui/qte/tft_qte_bar31.png")
        0.025
        getFile("gui/qte/tft_qte_bar32.png")
        0.025
        getFile("gui/qte/tft_qte_bar33.png")
        0.025
        getFile("gui/qte/tft_qte_bar34.png")
        0.025
        getFile("gui/qte/tft_qte_bar35.png")
        0.025
        getFile("gui/qte/tft_qte_bar36.png")
        0.025
        getFile("gui/qte/tft_qte_bar37.png")
        0.025
        getFile("gui/qte/tft_qte_bar38.png")
        0.025
        getFile("gui/qte/tft_qte_bar39.png")
        0.025
        getFile("gui/qte/tft_qte_bar40.png")
        0.025
        getFile("gui/qte/tft_qte_bar41.png")
        0.025
        getFile("gui/qte/tft_qte_bar42.png")
        0.025
        getFile("gui/qte/tft_qte_bar43.png")
        0.025
        getFile("gui/qte/tft_qte_bar44.png")
        0.025
        getFile("gui/qte/tft_qte_bar45.png")
        0.025
        getFile("gui/qte/tft_qte_bar46.png")
        0.025
        getFile("gui/qte/tft_qte_bar47.png")
        0.025
        getFile("gui/qte/tft_qte_bar48.png")
        0.025
        getFile("gui/qte/tft_qte_bar49.png")
        0.025
        getFile("gui/qte/tft_qte_bar50.png")
        0.025
        getFile("gui/qte/tft_qte_bar51.png")
        0.025
        getFile("gui/qte/tft_qte_bar52.png")
        0.025
        getFile("gui/qte/tft_qte_bar53.png")
        0.025
        getFile("gui/qte/tft_qte_bar54.png")
        0.025
        getFile("gui/qte/tft_qte_bar55.png")
        0.025
        getFile("gui/qte/tft_qte_bar56.png")
        0.025
        getFile("gui/qte/tft_qte_bar57.png")
        0.025
        getFile("gui/qte/tft_qte_bar58.png")
        0.025
        getFile("gui/qte/tft_qte_bar59.png")
        0.025
        getFile("gui/qte/tft_qte_bar60.png")
        0.025
        getFile("gui/qte/tft_qte_bar61.png")
        0.025
        getFile("gui/qte/tft_qte_bar62.png")
        0.025
        getFile("gui/qte/tft_qte_bar63.png")
        0.025
        getFile("gui/qte/tft_qte_bar64.png")
        0.025
        getFile("gui/qte/tft_qte_bar65.png")
        0.025
        getFile("gui/qte/tft_qte_bar66.png")
        0.025
        getFile("gui/qte/tft_qte_bar67.png")
        0.025
        getFile("gui/qte/tft_qte_bar68.png")
        0.025
        getFile("gui/qte/tft_qte_bar69.png")
        0.025
        getFile("gui/qte/tft_qte_bar70.png")
        0.025
        getFile("gui/qte/tft_qte_bar71.png")
        0.025
        getFile("gui/qte/tft_qte_bar72.png")
        0.025
        getFile("gui/qte/tft_qte_bar73.png")
        0.025
        getFile("gui/qte/tft_qte_bar74.png")
        0.025
        getFile("gui/qte/tft_qte_bar75.png")
        0.025
        getFile("gui/qte/tft_qte_bar76.png")
        0.025
        getFile("gui/qte/tft_qte_bar77.png")
        0.025
        getFile("gui/qte/tft_qte_bar78.png")
        0.025
        getFile("gui/qte/tft_qte_bar79.png")
        0.025
        getFile("gui/qte/tft_qte_bar80.png")
        0.025
        getFile("gui/qte/tft_qte_bar81.png")
        0.025
        getFile("gui/qte/tft_qte_bar82.png")
        0.025
        getFile("gui/qte/tft_qte_bar83.png")
        0.025
        getFile("gui/qte/tft_qte_bar84.png")
        0.025
        getFile("gui/qte/tft_qte_bar85.png")
        0.025
        getFile("gui/qte/tft_qte_bar86.png")
        0.025
        getFile("gui/qte/tft_qte_bar87.png")
        0.025
        getFile("gui/qte/tft_qte_bar88.png")
        0.025
        getFile("gui/qte/tft_qte_bar89.png")
        0.025
        getFile("gui/qte/tft_qte_bar90.png")
        0.025
        getFile("gui/qte/tft_qte_bar91.png")
        0.025
        getFile("gui/qte/tft_qte_bar92.png")
        0.025
        getFile("gui/qte/tft_qte_bar93.png")
        0.025
        getFile("gui/qte/tft_qte_bar94.png")
        0.025
        getFile("gui/qte/tft_qte_bar95.png")
        0.025
        getFile("gui/qte/tft_qte_bar96.png")
        0.025
        getFile("gui/qte/tft_qte_bar97.png")
        0.025
        getFile("gui/qte/tft_qte_bar98.png")
        0.025
        getFile("gui/qte/tft_qte_bar99.png")
        0.025
        getFile("gui/qte/tft_qte_bar100.png")
        0.025
        getFile("gui/qte/tft_qte_bar0.png")