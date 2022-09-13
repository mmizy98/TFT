#======================================#
#ДОСТИЖЕНИЕ - QTE ВЫИГРЫШ
screen Get_Achieve_1:
    add "achieve_day3_qte_win":
        at transform:
            xpos 1921 ypos 1015
            ease_back 1.5 xpos 1600
            pause 1.5
            ease_back 1.5 xpos 1930
    timer 4.0 action [ Hide("Get_Achieve_1"), Jump("volleyball_end") ]
#======================================#
#ДОСТИЖЕНИЕ - QTE ПОЛОВИНА
screen Get_Achieve_2:
    add "achieve_day3_qte_almost":
        at transform:
            xpos 1921 ypos 1015
            ease_back 1.5 xpos 1600
            pause 1.5
            ease_back 1.5 xpos 1930
    timer 4.0 action [ Hide("Get_Achieve_2"), Jump("volleyball_end") ]
#======================================#
#ДОСТИЖЕНИЕ - QTE ПРОИГРЫШ
screen Get_Achieve_3:
    add "achieve_day3_qte_loose":
        at transform:
            xpos 1921 ypos 1015
            ease_back 1.5 xpos 1600
            pause 1.5
            ease_back 1.5 xpos 1930
    timer 4.0 action [ Hide("Get_Achieve_3"), Jump("volleyball_end") ]
#======================================#
#ДОСТИЖЕНИЕ - ВЕЛИКИЙ XI НЕФРИТОВЫЙ СТЕРЖЕНЬ УДАР 
screen Get_Achieve_4:
    add "achieve_day3_nice_punch":
        at transform:
            xpos 1921 ypos 1015
            ease_back 1.5 xpos 1600
            pause 1.5
            ease_back 1.5 xpos 1930
    timer 4.0 action [ Hide("Get_Achieve_3"), Jump("arseniy_after_vallyball") ]
#======================================#
#ДОСТИЖЕНИЕ - ПАСХАЛКА
screen Get_Achieve_5:
    add "achieve_menu_easter_egg":
        at transform:
            xpos 1921 ypos 1015
            ease_back 1.5 xpos 1600
            pause 1.5
            ease_back 1.5 xpos 1930
    timer 4.0 action [ Hide("Get_Achieve_5"), Jump("tft_menu_main") ]
#======================================#
#ПЕРЕМЕННЫЕ ДОСТИЖЕНИЙ:
#ДОСТИЖЕНИЕ - QTE ВЫИГРЫШ
    $ tft_achievment_1 = False
    $ tft_achievment_1_count = 0
#======================================#
#ДОСТИЖЕНИЕ - QTE ПОЛОВИНА
    $ tft_achievment_2 = False
    $ tft_achievment_2_count = 0
#======================================#
#ДОСТИЖЕНИЕ - QTE ПРОИГРЫШ
    $ tft_achievment_3 = False
    $ tft_achievment_3_count = 0
#======================================#
#ДОСТИЖЕНИЕ - ВЕЛИКИЙ XI НЕФРИТОВЫЙ СТЕРЖЕНЬ УДАР 
    $ tft_achievment_4 = False
    $ tft_achievment_4_count = 0
#======================================#
#ДОСТИЖЕНИЕ - ПАСХАЛКА
    $ tft_achievment_5 = False
    $ tft_achievment_5_count = 0
#======================================#