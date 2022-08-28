label tft_day1:
    window hide
    $ backdrop = "days"
    $ new_chapter(3, u"Судьбы двух. День 3")
    scene black with dissolve2
    $ day_time()
    play ambience ambience_ext_road_day fadein 2
    play music BLAD fadein 2
    scene bg ext_path2_day with dissolve2
    $ renpy.pause(2)
    $ persistent.sprite_time = "day"
    window show
    "Вот уже третий день я бесцельно брожу по лагерю."
    "За всё время у меня не появилось ни одной нормальной догадки о том, что это за место."
    "Чистилище? {w=0.5}Сон? {w=0.5}Скорее всего я просто сошёл с ума."
    window hide
    scene bg ext_playground_day with dissolve2
    window show
    "В любом случае - я сейчас где-то очень далеко, в другом времени, пространстве..."
    "Совковый лагерь, смена времени года, пионерия... {w}Это всё точно не соответствует месту в котором я жил раньше."
    window hide
    scene ext_storage_day with dissolve2
    stop music fadeout 4
    window show
    "Спустя какое-то время передомной вырос небольшой амбар."
    "Рядом в воздухе веял сигаретный дым, разносимый ветром из-за угла здания."
    th "Впрочем, неудивительно, что в лагере кто-то курит."
    window hide
    scene ext_storage_day2 with dissolve2
    pause (0.5)
    window show
    "Зайдя в импровизированную курилку, я ожидал увидеть там физрука или вожатого."
    play music music_list['that_s_our_madhouse'] fadein 4
    "Но на деле всё оказалось куда интереснее."
    window hide
    show dv guilty pioneer2 flt with dissolve
    window show
    "За углом стояла рыжеволосая пионерка."
    "Кажется остальные пионеры звали её Алисой."
    window hide
    hide dv guilty pioneer2 flt with dissolve
    show dv angry pioneer2 flt with dissolve
    window show
    "Увидев меня, выражение лица девушки изменилось."
    dv "Ты что тут забыл?!"
    dns "Да гуляю просто."
    dv "Расскажешь кому о том что видел - пеняй на себя."
    "Я порядком удивился её наглости, но внутри заиграло самолюбие."
    window hide
    menu:
        "Дерзить Алисе":
            dns "Нифига, а если расскажу?"
            dv "Только попробуй."
            dns "И что ты сделаешь?"
            show dv rage pioneer2 flt with dissolve
            "Глаза пионерки вспыхнули."
            dv "В нос получишь!"
            "Нежелание нажить себе врагов ещё в одном мире победило, так что я не стал накалять обстановку дальше."
        "Уступить Алисе":
            "Нежелание нажить себе врагом ещё в одном мире победило, так что я не стал накалять обстановку дальше."
    dns "Ладно, не боись, я не стукач."
    show dv angry pioneer2 flt with dissolve
    "В ответ Алиса лишь фыркнула."
    "Девушка и правда была довольно симпатичной. {w}Янтарного цвета глаза, блестящие рыжие волосы, заплетённые в два хвоста, аккуратное лицо."
    "Рубашку она завязала ''На свой стиль'', подчеркивая грудь и оголив плоский загорелый живот."
    th "Внешними данными природа её точно не обделила."
    dns "Какие куришь то?"
    "Спросил я чтобы вывести диалог из тупика."
    show dv normal pioneer2 with dissolve
    dv "Мор."
    dv "Не проси, не дам, у меня и так мало осталось."
    th "По рассказам родственников, в СССР ''More'' был не менее желанным чем ''Malboro'', но курили его в основном девушки."
    th "Впринципе неудивительно что Алиса курит именно их."
    dns "Да я не курю."
    dv "А зачем тогда спрашивал?"
    dns "Просто так."
    show dv angry pioneer2 flt with dissolve
    dv "И вот только не надо сейчас мне говорить что я девочка, и не должна курить."
    dns "Мне без разницы. {w}Хочешь - кури."
    show dv surprise2 pioneer2 flt with dissolve
    "На её лице появилось удивление."
    stop music fadeout 6
    "Видимо я первый от кого она такое слышит."
    window hide
    pause (1)
    play sound sfx_dinner_jingle_speaker
    pause (2.5)
    window show
    "Вдруг по лагерю разнёсся горн, призывающий всех на обед."
    "Я бродил по лагерю в раздумьях с момента как проснулся, и даже пропустил завтрак, так что есть хотелось прилично."
    dns "Ладно, я пошёл."
    show dv normal pioneer2 with dissolve
    dv "Ещё увидимся."
    "Оставив Алису в курилке я направился в сторону столовой."
    window hide
    scene bg ext_dining_hall_away_day with dissolve2
    window show
    th "Девушка «не влезай - убьёт»."
    "Наверное в лагере она пользуется авторитетом."
    window hide
    scene bg ext_dining_hall_away_day with dissolve2
    stop ambience fadeout 4
    pause (0.5)
    scene bg ext_dining_hall_near_day with dissolve2
    pause (0.5)
    play ambience ambience_dining_hall_full fadein 4
    scene stolovaya1 with dissolve2
    window show
    "Некоторые пионеры уже трапездничали."
    "Все остальные стояли в очереди. {w}Я поспешил занять в ней место."
    window hide
    pause (3.5)
    scene bg int_dining_hall_people_day with dissolve2
    window show
    "Пришло моё время брать еду."
    window hide
    show cook_normal with dissolve
    window show
    "На выдаче стояла женщина лет тридцати."
    pvr "Первое - суп с фрикадельками, второе - пюре с котлетой. {w}Всё возьмёшь или что-то одно?"
    dns "Можно только пюре?"
    window hide
    pause (1.5)
    window show
    "Накладывая мне картошки, повариха вдруг спросила:"
    pvr "А это ты новенький? {w}Я слышала что к нам приехал один."
    dns "Да, я тут всего пару дней."
    pvr "Ну вот, значит я была права. {w}Меня кстати Марией зовут, но все зовут тётей Машей."
    dns "Очень приятно, а я Денис."
    hide cook_normal with dspr
    show cook_smile with dissolve
    "Она положила мне две котлеты и отдала тарелку."
    mar "Приятного аппетита!"
    dns "Спасибо, тёть Маш."
    window hide
    hide cook_smile with dissolve2
    pause (0.5)
    window show
    "Оставалось найти себе место."
    "Так оказалось, что ближайшие свободное стулья были у окна, где никого не было, и в центре столовой."
    "Сел я в итоге у окна, там мне показалось тише."
    window hide
    pause (0.5)
    scene cg d1_food_normal with dissolve2
    pause (0.5)
    window show
    "Пюре на удивление оказалось очень даже вкусным."
    "Хотя наверное так ощущалось из-за голода."
    th "Можно сказать что в моём попадании сюда есть свои плюсы."
    th "Бесплатная одежда, еда."
    th "Солнце, свежий воздух."
    th "Гуляя по площади я даже узнал из диалога пионеров о том, что лагерь находится на берегу реки и здесь есть пляж."
    th "Интересно только что это за река."
    th "Зная это, можно было бы предположить о моём местоположении в данный момент."
    th "Вопрос только в том нужно ли мне это знать и что мне это даст."
    window hide
    pause (2)
    scene black with dissolve2
    pause (1)
    scene stolovaya1 with dissolve2
    pause (1)
    window show
    "Пока я неспеша ел, столовая пустела."
    "Конечно, пионеры не хотят тратить своё ценное время на еду, здесь им важнее побыстрее найти развлечение."
    play music music_list['i_want_to_play'] fadein 3
    "Вдруг ко мне кто-то подсел."
    window hide
    show chair with dissolve
    show us smile sport close:
        xalign -1.0
    show us smile sport close:
        linear 0.7 xalign 0.5
    pause (1)
    window show
    us "Привет, ты Денис?"
    dns "Привет, да. {w}А ты кто?"
    us "А я Ульяна."
    dns "Круто, а меня откуда знаешь?"
    us "От верблюда!"
    dns "Ясно. Чего хочешь то?"
    us "Познакомиться!"
    dns "Эм..."
    show us laugh sport close with dissolve
    us "Да шучу я!"
    window hide
    pause (0.5)
    show us smile sport close with dissolve
    pause (0.5)
    window show
    us "Пойдешь с нами на воллейболл?"
    th "Я здесь уже третий день, а за всё время ещё ни с кем нормально не контактировал."
    th "Хоть Ульяна и выглядет младше той же Алисы, но думаю стоит попробовать."
    dns "Да, давай."
    dns "Только с кем с вами? Я тут никого не знаю."
    us "Я, Алиса, Витька и Машка, еще какой-то мальчик... {w=0.7}Ну и ты."
    us "У тебя же форма спортивная есть?"
    dns "Нету..."
    show us surp1 sport close with dissolve
    us "Ну ты даёшь! В детский лагерь и без формы приехал!"
    dns "Ну так получилось. {w}А её можно где-то здесь взять?"
    show us normal sport close with dissolve
    us "А я откуда знаю?"
    us "Ну попробуй у Оль Дмитревны спросить, может у неё есть."
    dns "Хорошо, попробую."
    us "Как найдешь - приходи на спорт площадку, там дальше есть воллейбольная сетка."
    show us smile sport close with dissolve
    us "Только не опаздывай!"
    dns "Постараюсь."
    window hide
    show us smile sport close:
        linear 1 xalign 2.0
    hide chair with dissolve2
    "Ульяна соскачила со стула и вылетела из столовой."
    th "Если Алиса - ''Девушка пожар'', то эта - ''Ракета''."
    stop music fadeout 3
    "Сдав грязную посуду, я покинул столовую."
    stop ambience fadeout 4
    window hide
    scene black with dissolve2
    play ambience ambience_ext_road_day fadein 3
    pause (1)
    scene bg ext_square_day with dissolve2
    play music music_list['silhouette_in_sunset'] fadein 4
    pause (1)
    window show
    "Возле Генды дети играли в догонялки."
    "Минуя их, я шёл к вожатой."
    window hide
    scene bg ext_houses_day with dissolve2
    window show
    "Мир вокруг казался красочным и ярким."
    "Пышные кроны деревьев, голубое небо, пение птиц..."
    th "Вот бы так же было в моём... прошлом мире."
    th "Выходишь утром во двор, а там зелень, всё цветёт, свежо..."
    window hide
    pause (1)
    scene sov1 with dissolve2
    pause (1)
    window show
    th "Только вот мест рядом, где такое можно было бы увидеть, я не знаю."
    th "Вокруг только серые многоэтажки, серые дороги, люди... машины..."
    th "Хотя в городе жить всё-равно удобнее."
    th "Вся инфраструктура в пешей доступности, куча торговых центров и прочего."
    window hide
    scene bg ext_house_of_mt_day with dissolve2
    window show
    "Дверь в домик вожатой была приоткрыта. Оно и не удивительно, на улице было градусов под тридцать."
    "Я постучал и зашёл."
    window hide
    play sound sfx_knock_door7_polite
    play sound sfx_open_cabinet_1
    stop ambience fadeout 2
    play ambience ambience_int_cabin_day fadein 4
    scene bg int_house_of_mt_day with dissolve2
    window show
    "Вожатая пила чай сидя за столом."
    dns "Ольга Дмитриевна добрый день!"
    show mt smile panama pioneer with dissolve
    mt "Привет Денис, да уже вечер почти."
    mt "Ты просто так или по делу?"
    dns "По делу. {w}У вас случаем нету лишней спортивной формы?"
    mt "А твоя где?"
    dns "Не взял..."
    show mt normal panama pioneer with dissolve
    mt "Ну может и есть. {w}Посмотри в том шкафу."
    "Вожатая указала пальцем на большой гардероб позади меня."
    mt "Во втором ящике снизу."
    mt "Да, да, в этом."
    mt "Я туда кладу вещи которые ребята с предыдущих смен забывают."
    "Немного порывшись в вещах пионеров, среди них оказались невзрачные серые спортивные шорты."
    "С виду они были маловаты, но выбирать не приходилось."
    "Затем на дне нашлась салатовая футболка. {w}Приложив её к груди стало ясно что она тоже немного маловата."
    dns "Ну вроде нашел но это всё мне наверное будет не по размеру."
    show mt smile panama pioneer with dissolve
    mt "Ну другого нет, бери это."
    mt "А покажи ка. {w}Да нормально впринципе, разносишь."
    dns "Ну ладно."
    mt "А плавки у тебя есть?"
    dns "Тоже нет."
    mt "В ящике повыше возьми, там на самом верху лежат."
    "Я открыл указанный ящик."
    "Внутри лежала стопка нижнего белья, мужского и женского. Сверху и правда лежали черные плавки."
    dns "Спасибо!"
    mt "Да не за что."
    window hide
    stop ambience fadeout 3
    scene bg ext_house_of_mt_day with dissolve2
    play sound sfx_open_cabinet_1
    play ambience ambience_day_countryside_ambience fadein 2
    window show
    th "Вопрос с одеждой решён, осталось только переодеться."
    "Жилище вожатой было местом проходным, да ещё и плавки надо занести."
    "Исходя из этого я направился в домик где меня разместили ''по приезде''."
    window hide
    pause (0.5)
    scene bg ext_houses_day with dissolve2
    pause (0.5)
    window show
    th "Интересно где там мой сосед?"
    th "Живём вместе третий день, а я даже не запомнил как его зовут."
    th "Андрей...{w} Артём...{w} Артур..."
    th "Не-не-не, как-то по другому"
    window hide
    pause (0.5)
    scene bg ext_square_day with dissolve2
    pause (0.5)
    window show
    th "Александр? {w}Саша..."
    th "Санька... {w}Сенька..."
    window hide
    pause (0.5)
    scene domext with dissolve2
    pause (0.5)
    window show
    th "Сеня... {w}Арсений! Точно, Арсений!"
    "Вспоминая имя я чуть не уткнулся носом в дверь своего домика."
    window hide
    stop ambience fadeout 2
    play sound sfx_open_cabinet_2
    play ambience ambience_int_cabin_day fadein 2
    scene dom with dissolve2
    window show 
    "Внутри было пусто."
    "Лишь только пахло чем-то не совсем приятным, будто кто-то жёг сухие листья или ставил благовонию."
    "Я открыл окно чтобы развеять это всё."
    "Затем бросил шорты в свою сумку, быстро скинул с себя пионерскую форму и переоделся в добытую спортивную."
    "Шорты немного жали в талии, а вот футболка пришлась по размеру."
    th "Ну надеюсь растянутся."
    "После пионерской формы с галстуками и ремнями переодевание в нормальную одежду ощущалось каким-то облегчением."
    "Я ещё с детства терпеть не мог все эти формальности, или как это называла наша директриса ''Деловой стиль одежды''."
    "Во первых этот стиль подразумевает многослойность: рубашечка, жилетик, пиджачок.{w} В школах и так душно, а надев всё это становилось просто невыносимо."
    th "Про галстуки вообще молчу - адская удавка."
    "Закончив с переодеванием я бросил вещи на кровать и собрался уходить."
    "К этому времени запах в комнате немного развеялся и был не таким резким и не так давал в голову."
    window hide
    stop ambience fadeout 2
    play sound sfx_open_cabinet_1
    play ambience ambience_forest_evening fadein 2
    scene domext with dissolve2
    pause (1)
    scene bg ext_square_day with dissolve2
    pause (1)
    scene bg ext_dining_hall_away_day with dissolve2
    pause (1)
    scene ext_storage_day with dissolve2
    pause (1)
    scene bg ext_playground_day with dissolve2
    pause (1)
    window show
    "Вскоре я вышел к спортивной площадке, где с краю находился воллейбольный корт."
    window hide
    scene ext_volley_court_7dl with dissolve2
    pause (0.5)
    show dv normal sport flt at left
    show us smile sport at right
    with dissolve
    window show
    "Там меня уже ждали."
    us "Алиска, вон он!"
    dv "Ну наконец-то! Почему так долго?"
    dns "Спешил как мог."
    dv "Ладно, проехали."
    us "Ты играть то хоть умеешь?"
    dns "Конечно умею! Если б не умел не пришел бы."
    us "Хорошо. Как делиться будем? Чур я с Алиской!"
    dv "А зачем делиться? {w}Мы втроём против тех ребят."
    "Она показала на пионеров, стоявших на другой стороне поля."
    us "Ура!"
    dns "Отлично."
    stop music fadeout 5
    dv "Значит начинаем."
    window hide
    pause (1)
    play music music_list['always_ready'] fadein 6
    hide dv normal sport flt at left
    hide us smile sport at right
    with dissolve
    pause (1)
    scene volleyball with dissolve2
    window show
    "Первыми подавали наши противники."
    window hide
    play sound sfx_soccer_ball_kick
    window show
    "Удар. {w}Мяч летит Ульяне. {w}Она отбивает его, Алиса запускает назад."
    "Наша команда зарабатывает очко."
    dns "Так держать!"
    "Следующим на подаче был я."
    us "Смотри не профукай!"
    dns "Не боись."
    window hide
    pause (0.5)
    play sound sfx_soccer_ball_kick
    window show
    "Я подкинул мяч и сильно ударил."
    "Произошло всё так как я и хотел - мяч коснулся земли почти у края поля."
    "Противники вернули мяч."
    "Теперь они ожидали сильную подачу и отошли к концу."
    "Я же наоборот подавал снизу."
    window hide
    pause (0.5)
    play sound sfx_soccer_ball_kick
    window show
    "Мяч приземлился сразу за сеткой."
    "Наша команда зарабатывает третье очко."
    window hide
    pause (0.5)
    play sound sfx_soccer_ball_kick
    window show
    show qte_alert with dissolve:
        xpos 0 ypos 0
    "Ещё удар, мяч летит в центр."
    "Противники легко отбивают его обратно."
    window hide
    pause (0.5)
    call tft_qte_label(1,2.6)
    if tft_qte_loose:
        $ tft_qte_loose = False
        "Я попытался сделать рывок в сторону мяча, но не успел."
        "А Алиса с Ульянкой были далеко."
        "Команда противников зарабатывает своё первое очко."
        "От них на подачу встаёт..."
        th "...Арсений!"
        th "Как это я его сразу не заметил."
        "Он сильным ударом запускает мяч в конец нашей половины поля."
        window hide
        pause (0.5)
        call tft_qte2_label(1,2.6)
        if tft_qte2_loose:
            $ tft_achievment_3 = True 
            $ tft_qte2_loose = False
            $ day3_valleyball_nicepunch = False
            "И снова наша команда не успевает среагировать."
            "Мяч коснулся земли буквально в миллиметрах от аута."
            "Ульяна попросилась на подачу. Никто не был против и я уступил ей."
            play sound sfx_soccer_ball_kick
            "Она ударяет по мячу со всей силы, он летит в левый угол вражеской половины."
            "Арсений прыгает в его сторону и успевает отбить."
            play sound sfx_soccer_ball_kick
            "Туда же подбегает тёмно-синеволосая девочка, и накидывает ему."
            play sound sfx_soccer_ball_kick
            "Он запускает мяч назад."
            "Но не расчитав силу, ударяет слишком сильно. {w}Так, что мяч летит точно Ульянку."
            play sound sfx_punch_washstand
            window hide
            scene ext_volley_court_7dl
            show qte_alert with dissolve:
                xpos 0 ypos 0
            pause (1)
            show dv laugh sport flt:
                xalign 0.99
            show ars_smile3:
                xalign 0.4
            show msh_laugh_sport:
                xalign 0.01
            with dissolve2
            pause (1)
            window show
            "Девочка даже ничего не поняла и застыла в недоумении после удара мяча об её голову."
            "Но хохот, поднявшийся на корте вывел её из ступора, и она тоже начала смеяться."
            window hide
            if tft_achievment_3:
                $ tft_achievment_3_count = 1
                play sound sfx_achievement
                call screen Get_Achieve_3
        else:
            $ day3_valleyball_nicepunch = True
            $ tft_achievment_2 = True
            pause (0.5)
            play sound sfx_soccer_ball_kick
            window show
            "Я успеваю среагировать и отбиваю его. {w}Алиса накидывает Ульяне, та ударяет в прыжке и мяч ложится за сеткой."
            "Девочки ударили кулачками."
            "Ульяна попросилась на подачу. Никто не был против и я уступил ей."
            play sound sfx_soccer_ball_kick
            "Она ударяет по мячу со всей силы, он летит в левый угол вражеской половины."
            "Арсений прыгает в его сторону и успевает отбить."
            play sound sfx_soccer_ball_kick
            "Туда же подбегает тёмно-синеволосая девочка, и накидывает ему."
            play sound sfx_soccer_ball_kick
            "Он запускает мяч назад."
            "Но не расчитав силу, ударяет слишком сильно. {w}Так, что мяч летит точно Ульянку."
            play sound sfx_punch_washstand
            window hide
            scene ext_volley_court_7dl
            pause (1)
            show dv laugh sport flt:
                xalign 0.99
            show ars_smile3:
                xalign 0.4
            show msh_laugh_sport:
                xalign 0.01
            with dissolve2
            pause (1)
            window show
            "Девочка даже ничего не поняла и застыла в недоумении после удара мяча об её голову."
            "Но хохот, поднявшийся на корте вывел её из ступора, и она тоже начала смеяться."
            window hide
            if tft_achievment_2:
                $ tft_achievment_2_count = 1
                play sound sfx_achievement
                call screen Get_Achieve_2
    else:
        $ day3_valleyball_nicepunch = True
        play sound sfx_soccer_ball_kick
        "Я быстро сделал три шага в сторону и отбил мяч."
        "Ульяна принимает его и накидывает Алисе."
        play sound sfx_soccer_ball_kick
        "Та сильным ударом посылает его обратно."
        "Противники не успевают отбить мяч и наша команда зарабатывает ещё одно очко."
        "Вместе с рыжими играть было легко, все понимали цели игры, и знали как добиться результата."
        "Ульяна попросилась на подачу. Никто не был против и я уступил ей."
        play sound sfx_soccer_ball_kick
        "Она ударяет по мячу со всей силы, он летит в левый угол вражеской половины."
        "Арсений прыгает в его сторону и успевает отбить."
        play sound sfx_soccer_ball_kick
        "Туда же подбегает тёмно-синеволосая девочка, и накидывает ему."
        play sound sfx_soccer_ball_kick
        "Он запускает мяч назад."
        "Но не расчитав силу, ударяет слишком сильно. {w}Так, что мяч летит точно Ульянку."
        play sound sfx_punch_washstand
        window hide
        pause (1)
        scene ext_volley_court_7dl
        show dv laugh sport flt:
            xalign 0.99
        show ars_smile3:
            xalign 0.4
        show msh_laugh_sport:
            xalign 0.01
        with dissolve2
        pause (1)
        window show
        "Девочка даже ничего не поняла и застыла в недоумении после удара мяча об её голову."
        "Но хохот, поднявшийся на корте вывел её из ступора, и она тоже начала смеяться."
        window hide
        scene ext_volley_court_7dl
        show qte_alert with dissolve:
            xpos 0 ypos 0
        with dissolve
        "Теперь на подачу встаёт Алиса."
        play sound sfx_soccer_ball_kick
        "Она сильным ударом запускает мяч в конец вражеской половины поля."
        "Девочка из команды противников отбивает мяч обратно на нашу сторону."
        window hide
        pause (0.5)
        call tft_qte2_label(1,2.6)
        if tft_qte2_loose:
            $ tft_achievment_2 = True
            $ tft_qte2_loose = False
            "Мяч коснулся земли буквально в миллиметрах от аута."
            "Ульяна попросилась на подачу. Никто не был против и я уступил ей."
            play sound sfx_soccer_ball_kick
            "Она ударяет по мячу со всей силы, он летит в левый угол вражеской половины."
            "Арсений прыгает в его сторону и успевает отбить."
            play sound sfx_soccer_ball_kick
            "Туда же подбегает тёмно-синеволосая девочка, и накидывает ему."
            play sound sfx_soccer_ball_kick
            "Он запускает мяч назад."
            "Но не расчитав силу, ударяет слишком сильно. {w}Так, что мяч летит точно Ульянку."
            play sound sfx_punch_washstand
            window hide
            scene ext_volley_court_7dl
            pause (1)
            show dv laugh sport flt:
                xalign 0.99
            show ars_smile3:
                xalign 0.4
            show msh_laugh_sport:
                xalign 0.01
            with dissolve2
            pause (1)
            window show
            "Девочка даже ничего не поняла и застыла в недоумении после удара мяча об её голову."
            "Но хохот, поднявшийся на корте вывел её из ступора, и она тоже начала смеяться."
            window hide
            if tft_achievment_2:
                $ tft_achievment_2_count = 1
                play sound sfx_achievement
                call screen Get_Achieve_2
        else:
            $ tft_achievment_1 = True
            $ day3_valleyball_nicepunch = True
            pause (0.5)
            play sound sfx_soccer_ball_kick
            window show
            "Я успеваю среагировать и отбиваю его. {w}Алиса накидывает Ульяне, та ударяет в прыжке и мяч ложится за сеткой."
            window hide
            scene ext_volley_court_7dl
            show dv laugh sport flt at left
            show us grin sport at right
            with dissolve2
            window show
            "Девочки ударили кулачками."
            "Ульяна попросилась на подачу. Никто не был против и я уступил ей."
            window hide
            scene ext_volley_court_7dl with dissolve2
            window show
            play sound sfx_soccer_ball_kick
            "Она ударяет по мячу со всей силы, он летит в левый угол вражеской половины."
            "Арсений прыгает в его сторону и успевает отбить."
            play sound sfx_soccer_ball_kick
            "Туда же подбегает тёмно-синеволосая девочка, и накидывает ему."
            play sound sfx_soccer_ball_kick
            "Он запускает мяч назад."
            "Но не расчитав силу, ударяет слишком сильно. {w}Так, что мяч летит точно Ульянку."
            play sound sfx_punch_washstand
            window hide
            pause (1)
            scene ext_volley_court_7dl
            show dv laugh sport flt:
                xalign 0.01
            show ars_smile3:
                xalign 0.5
            show msh_laugh_sport:
                xalign 0.99
            with dissolve2
            pause (1)
            window show
            "Девочка даже ничего не поняла и застыла в недоумении после удара мяча об её голову."
            "Но хохот, поднявшийся на корте вывел её из ступора, и она тоже начала смеяться."
            window hide
            if tft_achievment_1:
                $ tft_achievment_1_count = 1
                play sound sfx_achievement
                call screen Get_Achieve_1
label volleyball_end:
    window hide
    scene ext_volley_court_7dl with dissolve2
    window hide
    pause (1)
    play sound_loop clock_timeskip fadein 2
    show white_screen
    show aftertwohour
    with dissolve2
    pause (2)
    stop sound_loop fadeout 2
    hide white_screen
    hide aftertwohour
    with dissolve2
    play ambience ambience_forest_evening fadein 4
    $ persistent.timeofday = "sunset"
    pause (1)
    window show
    "Но всё хорошее имеет свойство кончаться."
    "Игра по итогу закончилась ничьей."
    "Все начали расходиться."
    stop music fadeout 3
    window hide
    show us smile sport:
        xalign 0.60
    show dv smile sport flt behind us:
        xalign 0.2
    show msh_smile_sport behind dv:
        xalign -0.25
    show ars_smile:
        xalign 1.15
    with dissolve
    window show
    "Ульяна сказала что пропустит ужин и убежала играть в футбол."
    window hide
    show us smile sport at right:
        linear 1.5 xalign -1.0
    pause (1.5)
    show dv smile sport flt with dissolve
    window show
    "Алиса пошла по своим делам."
    window hide
    show dv smile sport flt:
        linear 1.5 xalign -1.0
    pause (1.5)
    window show
    "Девочка из другой команды тоже незаметно исчезла."
    window hide
    show msh_smile_sport:
        xalign -0.25
        linear 1.5 xalign -1.0
    pause (1.5)
    show ars_smile:
        linear 1 xalign 0.5
        pause (1 )
    window show
    "А мы с Арсением пошли в домик."
    "Попутно обсуждая только что окончившийся матч."
    window hide
    hide ars_smile with dissolve2
    scene bg ext_dining_hall_away_sunset with dissolve2
    pause (1)
    scene bg ext_square_sunset with dissolve2
    pause (0.5)
    show ars_smile with dissolve
    window show
    jump arseniy_after_vallyball
    if day3_valleyball_nicepunch:
        $ tft_achievment_4 = True
        ars "Круто ты кстати ту мою первую подачу отбил."
        dns "Да оно случайно вышло, а так спасибо."
        window hide
        if tft_achievment_4:
                $ tft_achievment_4_count = 1
                play sound sfx_achievement
                call screen Get_Achieve_4
label arseniy_after_vallyball:
    hide ars_smile
    show ars_smile3
    with dissolve
    ars "Слушай, а как ты в команду к Двачевской то попал?"
    dns "А что в этом такого?"
    show ars_normal2
    hide ars_smile3
    with dissolve
    ars "Да она же фиг кого подпустит к себе."
    dns "Ну вообще меня Ульяна позвала когда я в столовой сидел..."
    ars "А... {w}Ну тогда не знаю даже. {w}Может им реально больше некого было взять."
    dns "Возможно."
    show ars_smile3
    hide ars_normal2
    with dissolve
    ars "А ты чего кстати такой тучный первые пару дней был?"
    dns "Да так, ситуация в жизни неприятная случилась."
    show ars_normal2
    hide ars_smile3
    with dissolve
    ars "Ну тогда ладно."
    window hide
    pause (1)
    scene bg ext_houses_sunset with dissolve2
    pause (1)
    window show
    "На очередном повороте Арсений отделился от меня, сообщив что обещал помочь поварихе Марие."
    window hide
    scene domexteven with dissolve2
    pause (0.8)
    play sound sfx_open_cabinet_1
    pause (0.3)
    play ambience ambience_int_cabin_day fadein 4
    scene dom with dissolve2
    pause (0.3)
    window show
    "Зайдя в домик, я плюхнулись на свою кровать."
    play sound fall_bed
    "Но затем сразу же пришлось вставать - стало интересно сравнить время на настенных часах и в телефоне."
    play sound sfx_unzip_sleepbag
    "Шарясь по рюкзаку рукой, я почти сразу нащупал телефон, лежащий в боковом кармане вместе с наушниками."
    "В главном отсеке находилось моё пальто и та самая подаренная фанатом бутылка."
    play sound jimbeam
    th "Судя по всему я тут ещё на долго, так что можно будет её когда-нибудь выпить."
    "Время на экране смартфона застыло на цифре {b}00:32."
    th "Судя по всему в это время я и переходил ту злополучную дорогу..."
    "Висящие же на стене часы показывали правильное ''местное'' время - {b}19:17."
    "После игры я довольно вымотался. {w}Положил телефон обратно в рюкзак и плюхнуля на кровать."
    window hide
    stop ambience fadeout 4
    scene black with Dissolve(3)
    scene anim prolog_1 with Dissolve(3)
    play music aprilrain fadein 10
    window show
    "Впервые за день я наконец остался один на один с самим собой."
    "Мысли о попадании в лагерь ударили в голову."
    th "Что же это за место такое?"
    th "Неужели я и правда как герой какого-нибудь романа перенёсся в прошлое?"
    th "Но ведь в любых событиях есть какой-то смысл."
    th "Тогда в чём смысл моего попадания сюда?"
    th "Да и куда это «сюда»?"
    th "Очнулся в автобусе, все вещи при себе."
    th "Какой-то лагерь в совке, на дворе лето."
    th "Вокруг бегают дети в пионерской форме. {w}Да и сам подросток."
    th "Если в лагере присутствует система отрядов, то дети в них должны делиться по возрасту."
    th "Допустим Ульяне лет четырнадцать, тогда Алисе примерно шестнадцать, мне примерно столько же."
    th "Но не слишком ли поздно - пионерия в шестнадцать?"
    th "Можно предположить что я, к примеру, поменялся с кем-то местами."
    th "И сейчас по современному Петербургу гуляет какой-то Вася из восьмедесятых. А может и девяностых."
    th "Хах, интересно какого ему там."
    window hide
    stop music fadeout 6
    show black with Dissolve(4)
    pause (2)
    play ambience ambience_int_cabin_night fadein 5
    window hide
    pause (1)
    $ persistent.sprite_time = "night"
    $ persistent.timeofday = "night"
    show domnight with dissolve2
    window show
    pause (1)
    "Проснулся я в темноте."
    "На лагерь опустилась ночь."
    play sound sfx_stomach_growl
    "В животе сильно урчало."
    th "Всё-таки не надо было отказываться от супа."
    th "Понятное дело, ужин я уже проспал. {w}Может столовая ещё открыта и я смогу поесть?"
    "Арсений спал на своей кровати."
    "Тихо переодевшись, пионерскую форму дабы не нарушить его сон, я вышел из домика."
    window hide
    show FireFlies
    stop ambience fadeout 3
    play sound sfx_open_cabinet_1
    pause (1)
    play ambience ambience_forest_night fadein 3
    show domextnight behind FireFlies with dissolve2
    pause (1)
    show bg ext_house_of_dv_night behind FireFlies with dissolve2
    pause (1)
    show ext_houses_night behind FireFlies with dissolve2
    hide bg ext_house_of_dv_night
    hide domextnight
    hide black
    window show
    "В лагере было пусто."
    "Вокруг царила тишина и спокойствие, сопровождаемые стрекотанием сверчков."
    "Звёзды и луна освещали верхушки елей, красиво отбрасывающих тень на вымощенные камнем дорожку, образовывая невероятные узоры."
    "Атмосфера ночи, когда в округе нет никого кроме тебя самого - одно из самых завораживающих явлений, которое может увидеть человек в простых условиях."
    window hide
    show bg ext_square_night behind FireFlies with dissolve2
    pause (1)
    show bg ext_dining_hall_away_night behind FireFlies with dissolve2
    pause (1)
    window show
    "В окнах столовой была лишь темнота."
    "Но в потёмках мне удалось разглядеть фигуру у двери."
    th "Может это Мария?"
    window hide
    show bg ext_dining_hall_near_night behind FireFlies with dissolve2
    play sound_loop sfx_alisa_picklock fadein 2
    window show
    "Подойдя ближе, я услышал звук, похожий на то, будто кто-то ковырял замок."
    window hide
    pause (0.6)
    $ persistent.sprite_time = "night"
    show dv normal pioneer with dissolve
    window show
    "Взломщиком оказалась Алиса."
    "Она усердно чем-то пыталась открыть дверь, склонившись над замочной скважиной."
    dns "Бу!"
    stop sound_loop
    window hide
    hide dv normal pioneer with dissolve
    show dv scared1 pioneer flt with dissolve
    window show
    "От испуга девочка вскрикнула."
    window hide
    hide dv scared1 pioneer flt
    show dv angry pioneer flt with dissolve
    window show
    dv "Опять ты?!"
    "Но потом вернулась в своё обычное состояние."
    dns "Ты чего тут делаешь?"
    show dv normal pioneer with dissolve
    dv "А что, не понятно?"
    dns "Да не особо."
    dv "Столовую пытаюсь открыть, ужин пропустила."
    dns "Я тоже..."
    dv "Ну так помоги открыть, чего стоишь."
    th "Конечно можно попытаться вскрыть столовую, и провести ужин в компании девушки, но и подставлять под удар лояльность поварихи тоже не хочется."
    "Голод оказался сильней, и я согласился."
    dns "Ну показывай."
    window hide
    show dv normal pioneer:
        linear 0.5 xalign 0.75
    pause (0.6)
    window show
    "Она отошла от двери на шаг и продемонстрировала мне отмычку, торчавшую из замочной скважины."
    dv "Вот."
    "Я вытащил её и осмотрел."
    th "Похоже, когда-то это была заколка для волос."
    dns "Сама сделала?"
    dv "Ну да."
    th "Пытаться открыть этим что-то - равносильно тому, что пытаться разобрать автомобиль одним лишь гаячным ключом."
    "Двери столовой были сделаны из дерева и имели небольшие окошки. {w}Появилась идея."
    "Я вернул Алисе отмычку."
    show dv surprise pioneer flt with dissolve
    dv "И как ты её голыми руками собрался открыть?"
    "Недоумевающе спросила она."
    dns "Где-то я раньше видел, что у таких дверей двигались стёкла."
    dv "Ну да, только тут их не подцепить. {w}Ульяна уже пробовала."
    dns "Ну я всё-равно попробую."
    pause (0.7)
    show dv normal pioneer with dissolve
    "Я приложил ладонь к стеклу и начал давить в сторону."
    window hide
    pause (2)
    window show
    "Через пару секунд оно двинулось, образовав сантиметровую щель."
    play sound window_dining
    "Затем отодвинул его чуть больше, так, чтобы туда пролезла рука."
    play sound sfx_lock_open
    "Дотянувшись до ручки открыл замок с внутренней стороны."
    play sound sfx_open_cupboard
    "Открыл дверь, и жестом пригласил Алису внутрь."
    dns "Дамы вперёд."
    window hide
    show dv grin pioneer flt with dissolve:
        xalign 0.75
    pause (0.5)
    window show
    dv "Неплохо."
    window hide
    show dv grin pioneer flt:
        linear 1.3 xalign -0.75
    pause (2)
    stop ambience fadeout 3
    play sound sfx_close_cabinet
    scene bg int_dining_hall_night with dissolve2
    play ambience ambience_int_cabin_night fadein 3
    pause (1)
    play music roxette fadein 3 volume 0.5
    window show
    dns "Что у нас сегодня на ужин?"
    "Сказал я, cадясь за стол, пока Алиса шарилась на кухне."
    dv "Булки!"
    "Послышалось с кухни."
    window hide
    show chair with dissolve
    show dv smile pioneer close with dissolve
    window show
    "Алиса поставила еду на стол и села рядом."
    dv "Угощайся."
    dns "Спасибо. {w}С чем булки то?"
    dv "Да фиг его знает, с чем нашла с тем взяла."
    window hide
    scene dveda with dissolve2
    pause (1.5)
    window show
    "Ели мы молча."
    "Спустя какое-то время стало скучно."
    th "Чего просто так сидеть? {w}Да и девочку стоит по-ближе узнать."
    "Я начал диалог."
    dns "Слушай, Алис, а как тебе вообще в этом лагере? {w}Нравится?"
    dv "Ну да, я уже не первый раз сюда езжу и пока не надоедает."
    dns "Есть что-то конкретное?"
    dv "Природа наверное... Она здесь шикарная."
    dns "А вы с Ульяной здесь познакомились?"
    dv "Да. А потом оказалось что мы из одного города."
    dns "Мир тесен."
    dv "Это точно."
    window hide
    scene bg int_dining_hall_night with dissolve2
    show chair with dissolve
    show dv smile pioneer close with dissolve
    window show
    "Как продолжать диалог я не знал, но за меня это сделала Алиса."
    dv "Расскажи тоже что-нибудь."
    dns "А что тебя интересует?"
    "Произнёс я, поддерживая с ней зрительный контакт."
    dv "Ну о себе. Что дома делаешь, чем занимаешься впринципе."
    "Не стоит, думаю, ей знать о группе."
    dns "Хм... {w}Ничего особенного, общаюсь с друзьями, гуляем иногда."
    dns "Увлекаюсь путешествиями, люблю музыку."
    dv "Что слушаешь?"
    dns "Рок, Альтернативу, что-то в этом духе."
    dv "Я тоже."
    dns "Прикинь как совпало."
    dns "А сама играешь на чем-нибудь?"
    dv "На гитаре."
    dns "Круто."
    dv "А ты?"
    stop music fadeout 3
    dns "Неа."
    "Я бы хотел продолжить беседу, но не тут то было."
    play music music_list['doomed_to_be_defeated'] fadein 3
    voice "Почему окно открыто?"
    window hide
    hide dv smile pioneer close with dissolve
    show dv surprise2 pioneer close flt with dissolve
    window show
    "Донеслось вдруг со стороны входа."
    dv "Прячься! Это Славя! Она обход ночной за вожатую делает."
    window hide
    hide dv surprise2 pioneer close flt with dissolve
    hide chair with dissolve
    scene night_event with dissolve2
    window show
    "Алиса быстро залезла под стол, а я встал за колонну."
    "Из-за неё мне было видно, как в окно заглядывает Славяна."
    th "Как я мог забыть его задвинуть то?"
    sl "Если там кто-то есть, то лучше выходите, иначе я закрою, и будете сидеть до утра!"
    th "Так мы к тебе и выйдем."
    "Ненамеренные выдавать себя, мы с Алисой остались на свои местах."
    window hide
    pause (0.75)
    play sound window_dining
    pause (0.75)
    scene bg int_dining_hall_night with dissolve2
    window show
    "Славя подождала ещё немного, и не получив ответа, закрыла окно и ушла."
    window show
    stop music fadeout 4
    show dv normal pioneer with dissolve
    window show
    "Мы выбрались из своих укрытий."
    dv "Вот же коза белобрысая!"
    dns "Есть такое."
    dv "И вот чё ей не спится..."
    dns "А вы не в ладах?"
    dv "Я с ней не общаюсь. Слишком уж правильная она, да ещё и стукачит."
    dns "Буду иметь ввиду."
    dv "Короче, я щас ещё булок прихвачу, а ты пока иди окно открывай."
    dns "А чего просто через дверь не выйдем?"
    dv "А вдруг она там караулит?"
    dns "Ладно, убедила."
    window hide
    pause (0.5)
    hide dv with dissolve
    pause (1)
    play sound sfx_open_window
    play ambience ambience_forest_night
    pause (0.5)
    window show
    "Она ушла на кухню, а я подошёл к окну, повернул ручку и открыл его."
    "Меня окутал приятный ночной бриз."
    "В столовой было довольно душно. Облакотившись на окно, я принялся полной грудью вдыхать свежий воздух."
    show dv smile pioneer with dissolve
    "Через минуту подошла Алиса, державшая в одной руке бумажный пакет, куда положила еду, а другой протягивала мне булочку."
    dv "Держи, в домике съешь."
    dns "Спасибо большое."
    show dv smile5 pioneer flt with dissolve
    dv "Да не за что."
    "Я спрятал её маленький презент в карман."
    dns "Всё, пойдем."
    dv "Угу."
    window hide
    hide dv with dissolve
    window show
    "Я забрался на подоконник и спрыгнул вниз, на траву."
    "Затем помог Алисе аккуратно спуститься."
    window hide
    show FireFlies
    show black behind FireFlies with dissolve2
    hide black
    show bg ext_square_night behind FireFlies
    with dissolve2
    pause (1)
    hide bg ext_square_night
    show bg ext_house_of_dv_night behind FireFlies
    with dissolve2
    pause (1)
    show dv smile pioneer behind FireFlies with dissolve
    window show
    "Мы остановились возле домика, находящегося неподалёку от моего."
    "Одно из окон было зановешено чёрным флагом с изображённым на нём весёлым роджером."
    dns "Спокойной ночи."
    window hide
    hide dv smile pioneer
    show dv grin pioneer flt
    with dissolve
    window show
    dv "И тебе."
    window hide
    play sound sfx_open_cabinet_1
    hide dv grin pioneer flt with dissolve
    window show
    "Она помахала мне рукой и скрылась в дверях."
    "А я пошёл к себе."
    window hide
    show domextnight behind FireFlies with dissolve2
    play ambience ambience_int_cabin_night fadein 4
    pause (1)
    show domnight with dissolve2

    "Соседняя кровать была пуста. {w}Арсения дома не было."
    th "В туалет может пошел?"
    "Сняв с себя одежду, положил её на кровати у ног."
    "Затем лёг, укрылся одеялом, больше похожим на простынь."
    th "Ух ё, завтра же ещё на эту линейку идти ни свет ни заря."
    th "Сегодня был слишком активный день для меня."
    th "Надеюсь Арсений меня разбудит."
    window hide
    show anim prolog_1 with Dissolve(3)
    stop ambience fadeout 4
    pause (4)
    window show
    "Спать совершненно не хотелось."
    "Пока я лежал с закрытыми глазами, в моей голове было лишь одно - мысли о том, что было в столовой, а конкретно о девочке Алисе, с которой я там сидел."
    th "Людей сближает общение и вместе пережитые моменты."
    th "Как же так вышло, что когда я попал сюда, то контактировал больше всего с ней, а не с кем-то другим?"
    th "Определённо, внешние данные у неё были впечатляющие."
    "Когда она была одета в спортивные шорты с заправленной в них футболкой, можно было увидеть что она стройная, и следит за своей фигурой."
    "Все её внешние данные вкупе образуют потрясающую картину."
    window hide
    stop music fadeout 5
    stop ambience fadeout 5
    show black with Dissolve(5)
    pause (1)
    jump tft_day2





            







            
            
            
            
            