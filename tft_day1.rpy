label tft_1:

    window hide
    $ backdrop = "days"
    $ new_chapter(1, u"Искра. День 3")
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

    show dv normal pioneer2 flt with dissolve

    dv "Мор. {w=0.5}Не проси, не дам, у меня и так мало осталось."
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

    show dv normal pioneer2 flt with dissolve

    dv "Ещё увидимся."
    "Оставив Алису в курилке я направился в сторону столовой."

    window hide
    scene bg ext_dining_hall_away_day with dissolve2
    window show
    
    th "Девушка «не влезай - убьёт» , девушка «пожар»."
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
    hide cook_smile
    show cook_laugh with dissolve
    pause (0.5)
    hide cook_laugh with dissolve2
    window show
    
    "Оставалось найти себе место."
    "Так оказалось, что ближайшие свободное стулья были у окна, где никого не было, и в центре столовой."
    "Сел я в итоге у окна так как там было тише."

    window hide
    pause (0.5)
    scene cg d1_food_normal with dissolve2
    pause (0.5)
    window show

    "Пюре на удивление оказалось очень даже вкусным."
    "Хотя наверное так ощущалось из-за голода."
    th "Можно скказать что в моём попадании сюда есть свои плюсы."
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
    stop ambience fadeout 1.5
    play ambience ambience_dining_hall_full fadein 2
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
        linear 1 xalign 0.5
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
    us "Я, Алиса, Витька и Машка. {w=0.7}Ну и ты."
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
    stop music fadeout 4

    "Ульяна соскачила со стула и вылетела из столовой."
    th "Если Алиса - ''Девушка пожар'', то эта - ''Ракета''."
   
    stop ambience fadeout 4
   
    "Сдав грязную посуду, я покинул столовую."

    window hide
    play ambience ambience_ext_road_day fadein 3
    scene bg ext_square_day with dissolve2
    play music music_list["my_daily_life"] fadein 4
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
    th "Только вот мест рядом, где такое можно было бы увидеть, я не знаю."
    th "Вокруг только серые многоэтажки, серые дороги, люди... машины..."
    th "Хотя в городе жить всё-равно удобнее."
    th "Вся инфраструктура в пешей доступности, куча торговых центров и прочего."

    window hide
    scene bg ext_house_of_mt_day with dissolve2
    window show

    "Дверь в домик вожатой была приоткрыта."
    "Скорее всего вожатой стало жарко."

    window hide
    play sound sfx_knock_door7_polite
    play sound sfx_open_cabinet_1
    window show

    "Я постучал и зашёл."

    window hide
    stop ambience fadeout 2
    play ambience ambience_int_cabin_day fadein 4
    scene bg ext_house_of_mt_day with dissolve2
    window show

    "Вожатая пила чай сидя за столом."
    dns "Ольга Дмитриевна добрый день!"
    mt "Привет Денис, да уже вечер почти."
    mt "Ты просто так или по делу?"
    dns "По делу. {w}У вас случаем нету лишней спортивной формы?"
    mt "А твоя где?"
    dns "Не взял..."
    mt "Может и есть. {w}Посмотри в том шкафу."
    "Вожатая указала пальцем на большой гардероб позади меня."
    mt "Там во втором ящике снизу лежат вещи забытые с предыдущих смен, в них посмотри."
    ""

    
   

















#НИЖЕ ПРЕДЫДУЩАЯ ВЕРСИЯ МОДА, ОТТУДА БЕРУ ОТРЫВКИ
    window hide
    play sound sfx_open_cabinet_1
    play ambience ambience_day_countryside_ambience fadein 3
    scene domext with dissolve2
    pause (1)
    play music music_list['everyday_theme'] fadein 3
    scene bg ext_house_of_dv_day with dissolve2
    window show
    
    
    window hide
    pause (1)
    scene bg ext_square_day with dissolve2
    pause (1)
    scene bg ext_dining_hall_away_day with dissolve2
    pause (1)
    scene ext_storage_day with dissolve2
    pause (1)
    play ambience ambience_forest_evening fadein 5
    scene bg ext_playground_day with dissolve2
    pause (1)
    window show
    
    "Вскоре я вышел к спортивной площадке."
    "С краю находился воллейбольный корт, где меня уже ждали."
    
    window hide
    scene ext_volley_court_7dl with dissolve2
    pause (0.5)
    show dv normal sport flt  at left
    show us smile sport at right
    with dissolve
    window show
    
    usp "Алиска, это он?"
    dv "Да, Ульян."
    us "Ну наконец-то! Почему так долго?"
    dns "Извиняйте."
    us "Ладно, проехали."
    us "Ты играть хоть умеешь?"
    dns "В волейбол то?"
    us "Ага."
    dns "Конечно умею!"
    us "Ну тогда ладно."
    dns "Как делиться будем?"
    us "А зачем делиться? {w}Мы втроём против тех ребят."
    "Она показала на пионеров, стоявших на другой стороне поля."
    dns "Хорошо."
    
    stop music fadeout 5
    
    dv "Значит начинаем."
    
    window hide
    pause (1)
    play music music_list['always_ready'] fadein 6
    hide dv normal sport flt  at left
    hide us smile sport at right
    with dissolve
    pause (1)
    window show
    
    "Игра началась."
    "Первыми подавали наши противники."
    
    play sound sfx_soccer_ball_kick
    
    "Удар. {w}Мяч летит Ульяне. {w}Она отбивает его, а Алиса запускает назад."
    "Нам удаётся заработать очко."
    dns "Так держать!"
    
    show dv smile sport flt  at left
    show us grin sport at right
    with dissolve
    
    us "Смотри не профукай подачу."
    dns "Наблюдай."
    "Гордо сказал я."
    
    window hide
    hide dv smile sport flt  at left
    hide us grin sport at right
    with dissolve
    pause (1)
    window show
    play sound sfx_soccer_ball_kick
    
    "Затем взял мяч, отошёл назад, подкинул его и ударил сверху."
    "Было бы комично, если бы сейчас ничего не получилось, но удача была на моей стороне."
    "Мяч коснулся земли почти у края поля."
    "Счёт стал {b}2:0."
    "Противники вернули мяч."
    "Я снова попытался дать подачу сверху."
    
    play sound sfx_soccer_ball_kick
    
    "Получилось криво. {w}Мяч даже не перелетел сетку."
    
    window hide
    show dv normal sport flt  at left
    show us dontlike sport at right
    with dissolve
    window show
    
    us "И что это было?"
    "Недовольно произнесла Ульяна."
    dv "Да чё ты, нормально же всё пока."
    us "Это пока. {w}Противникам нельзя отдавать ни очка! Мне так Иван Анатольевич говорил!"
    th "Надо исправлять положение."

    show us normal sport at right with dissolve

    "Алиса отдала мяч противникам, и те приготовились подавать."
    
    window hide
    pause (1)
    hide dv normal sport flt  at left
    hide us dontlike sport at right
    with dissolve
    pause (1)
    play sound sfx_soccer_ball_kick
    
    "Удар. Мяч летит в центр."
    "Я отбиваю его, Алиса накидывает Ульяне."
    "Та ударяет, и мяч ложится на вражеской половине."
    "Счёт становится {b}3:1."
    
    show dv grin sport flt at left
    show us grin sport at right
    with dissolve

    dns "Классно сработали."
    dv "Да, все молодцы."
    
    window hide
    pause (1)
    hide dv grin sport flt at left
    hide us grin sport at right
    with dissolve
    scene volleyball with dissolve2
    pause (1)
    window show
    
    "Следующие полтора часа мы провели за игрой."
    "Наша команда работала быстро и слаженно. Будто мы играем не первый раз. Хотя на деле едва знакомы."
    
    window hide
    pause (1)
    play sound_loop clock_timeskip fadein 2
    show white_screen with dissolve2
    show flt_timeskip_logo1 with dissolve
    pause (1)
    show flt_timeskip_logo2
    with dissolve
    hide flt_timeskip_logo2
    show flt_timeskip_logo1
    with dspr
    show ext_volley_court_7dl
    show white_screen
    with dissolve2
    pause (1)
    stop sound_loop fadeout 2
    hide flt_timeskip_logo1
    hide white_screen
    with dissolve2
    play ambience ambience_forest_evening fadein 4
    $ persistent.timeofday = "sunset"
    pause (1)
    window show
    
    "Но всё хорошее имеет свойство кончаться."
    
    window hide
    show dv smile sport flt at left
    show us smile sport at right
    with dissolve
    window show
    
    "Спустя час игра закончилась. Все начали расходиться."
    "Ульяна сказала что пропустит ужин и убежала играть в футбол."
    
    window hide
    hide us smile sport at right
    hide dv smile sport flt at left
    with dissolve
    show dv smile sport flt with dissolve
    stop music fadeout 3
    window show
    
    "Ребята, против которых мы играли, пошли по своим делам."
    "А {i}мы{/i} с Алисой пошли в домики."
    "Попутно обсуждая только что окончившийся матч."
    
    window hide
    hide dv smile sport flt  with dissolve
    pause (0.3)
    scene bg ext_dining_hall_away_sunset with dissolve2
    pause (1)
    scene bg ext_square_sunset with dissolve2
    pause (0.5)
    show dv smile sport flt  with dissolve
    window show
    
    dv "Классно поиграли."
    dns "Да, мне тоже понравилось."
    
    hide dv smile sport flt 
    show dv grin sport flt with dissolve
    
    dv "Знаешь, я сначала думала ты откажешься или скажешь, что играть не умеешь."
    dv "А оказалось что ты даже неплохо играешь."
    dns "Вот видишь, не прогадала ты с тем, кого звать."
    dv "Ага."
    dns "Приглашай ещё. От игры на свежем воздухе грех отказываться."
    th "Тем более в компании красивой девушки."
    dv "Буду знать что ты не против поиграть."
    
    hide dv grin sport flt dspr
    show dv smile sport flt  with dissolve
    
    "Хоть она и девочка, разговор с ней шёл легко."
    "Возможно это окружающая среда и смена обстановки так повлияли на моё поведение. {w}А возможно {i}что-то другое."
    
    window hide
    hide dv smile sport flt  with dissolve
    pause (0.5)
    scene bg ext_houses_sunset with dissolve2
    pause (1)
    scene dvhousesunset with dissolve2
    window show
     
    "Проходя мимо домика с флагом на стекле, Алиса вдруг остановилась."
    
    show dv normal sport flt  with dissolve
    
    dv "Пришли. Я тут живу."
    dns "Прикольно окно украсили. Я оценил когда мимо шёл."
    
    hide dv normal sport flt 
    show dv grin sport flt with dissolve
    
    dv "Мы с Ульяной старались."
    dns "Выглядит и правда круто. {w}А вы вместе живёте?"
    dv "Да, а что?"
    dns "А сколько ей лет? Выглядит она младше тебя."
    dv "Четырнадцать."
    dv "Ей скучно с ровесниками, поэтому её в старший отряд перевели."
    dns "Понял."
    
    hide dv grin sport flt
    show dv smile sport flt with dissolve
    
    dv "Ладно, ещё увидимся."
    dns "Давай."
    
    window hide
    play sound sfx_open_cabinet_2 
    pause (1)
    hide dv smile sport flt with dissolve
    window show
    
    "Она скрылась за дверью."
    "Я проводил её взглядом и пошёл к себе."
    
    window hide
    scene domexteven with dissolve2
    pause (0.8)
    play sound sfx_open_cabinet_1
    pause (0.3)
    play ambience ambience_int_cabin_day fadein 4
    scene dom with dissolve2
    pause (0.3)
    window show
    
    "Зайдя в домик, плюхнулся на кровать."
    play sound fall_bed
    "Затем по привычке достал телефон."
    "Остановил меня значёк отсутствия сети в правом верхнем углу экрана."
    th "Ах, совсем забыл! Я же хер пойми где, и не знаю как сюда попал."
    "Зато мне удалось узнать время - {b}18:22"
    "После игры я довольно вымотался. {w}Поэтому решил передохнуть, и закрыл глаза."
    
    window hide
    scene anim prolog_1 with dissolve2
    window show
    
    "Впервые за день я наконец остался один на один с самим собой."
    "Мысли о попадании в лагерь ударили в голову."
    th "Что же это за место такое?"
    th "Неужели я и правда как герой какого-нибудь романа перенёсся в прошлое?"
    th "Но ведь в любых событиях есть какой-то смысл."
    th "Тогда в чём смысл моего попадания сюда?"
    th "Да и куда это «сюда»?"
    th "Какой-то пионер лагерь в совке, на дворе лето."
    th "Причём люди в лагере знают о том, что я должен был приехать."
    th "Можно предположить что я, к примеру, поменялся с кем-то местами."
    th "И сейчас по современному Петербургу гуляет какой-то Вася из восьмедесятых. А может и девяностых."
    th "Хах, интересно какого ему там."
    th "Насколько я понял, я тут ещё и помолодел."
    th "Если в лагере присутствует система отрядов, то дети в них должны делиться по возрасту."
    th "Значит если Ульяне четырнадцать, то Алисе примерно семнадцать, как и всем остальным пионерам, включая меня."
    th "Но не слишком ли поздно - пионерия в семнадцать?"
    th "Из курса истории я помню, что в 1987 году в результате новой реформы ввели 11-летнее образование со сдвигом всех классов, начиная с четвёртого, на год вперёд."
    th "В тупую спрашивать: «А какой сейчас год?» будет странно, так что через вопросы о классе, думаю, можно будет это выяснить." 
    
    window hide
    pause (1.5)
    window show

    th "Интересная ситуация конечно."
    th "Попал в прошлое. И как я до такого дошёл?"
    th "Жаль только не рассказать никому - не поверят."
    "Представляя как друзья, которым я повествую о своём путешествии во времени и пространстве, крутят палец у виска и говорят что-то на подобии: «Чем это тебя таким тяжелым в питере накачали?» я не заметил как окончательно погрузился в сон."
    
    window hide
    scene black with dissolve2
    pause (2)
    play ambience ambience_int_cabin_night fadein 5
    window hide
    pause (1)
    $ persistent.sprite_time = "night"
    $ persistent.timeofday = "night"
    scene domnight with dissolve2
    window show
    pause (1)
    
    "Судя по тому, что проснулся я в темноте, на лагерь опустилась ночь."
    
    play sound sfx_stomach_growl
    
    "В животе сильно урчало."
    th "Понятное дело, ужин то я проспал."
    "Быстро переодевшись в пионерскую форму я вышел из домика."
    
    window hide
    play sound sfx_open_cabinet_1
    scene domextnight with dissolve2
    window show
    
    th "Надеюсь столовая ещё открыта или Мария сделает мне одолжение и накормит."
    
    window hide
    pause (1)
    scene bg ext_house_of_dv_night with dissolve2
    pause (1)
    scene ext_houses_night with dissolve2
    pause (1)
    scene bg ext_square_night with dissolve2
    pause (1)
    window show
    
    "В лагере было пусто."
    "Вокруг царила тишина и спокойствие, сопровождаемые стрекотанием сверчков."
    
    window hide
    pause (0.75)
    scene bg ext_dining_hall_away_night with dissolve2
    pause (0.75)
    window show
    
    "В окнах столовой была лишь темнота."
    "Но в потёмках мне удалось разглядеть какую-то фигуру у двери."
    th "Может это повариха?"
    
    window hide
    scene bg ext_dining_hall_near_night with dissolve2
    play sound_loop sfx_alisa_picklock fadein 2
    window show
    
    "Подойдя ближе, я услышал звук, похожий на то, будто кто-то ковырял замок."
    
    pause (0.6)
    show dv normal pioneer with dissolve

    "Взломщиком оказалась Алиса."
    "Она усердно чем-то пыталась открыть дверь, склонившись над замочной скважиной."
    dns "Алис!"
    
    pause (0.7)
    stop sound_loop
    hide dv normal pioneer with dissolve
    show dv scared1 pioneer flt with dissolve
    
    dv "..."
    
    pause (1)
    hide dv scared1 pioneer flt
    show dv angry pioneer with dissolve
    
    dv "Напугал блин."
    dns "Ты чего тут делаешь?"
    
    show dv normal pioneer with dissolve
    
    dv "А что, не заметно?"
    dns "Да пока не особо."
    dv "Столовую пытаюсь открыть, не наелась."
    dns "А я ужин проспал..."
    dv "Ну так помоги открыть, и вместе поедим."
    th "Конечно можно попытаться вскрыть столовую, и провести ужин в компании девушки, но и подставлять под удар лояльность поварихи тоже не хочется."
    th "Точно! Я же с собой еду в дорогу брал."
    th "Если Алиса согласится, то можно вдвоём поесть у меня в домике."
    
    menu:
        "Согласиться на взлом":
            
            $ day1_vzlom = True
            $ persistent.sprite_time = "night"
            th "Нет, одними бутербродами не наешься."
            dns "Ну показывай."
            "Она отошла от двери на шаг и продемонстрировала мне отмычку, торчавшую из замочной скважины."
            dv "Вот."
            "Я вытащил её и осмотрел."
            th "Похоже, когда-то это была заколка для волос."
            dns "Сама сделала?"
            dv "Ну да."
            th "Пытаться открыть этим что-то - равносильно тому, что пытаться разобрать автомобиль одним лишь гаячным ключом."
            "Двери столовой были сделаны из дерева и имели небольшие окошки. {w}Появилась идея."
            "Я вернул Алисе отмычку."
            
            show dv surprise pioneer with dissolve
            
            dv "И как ты её голыми руками собрался открыть?"
            "Недоумевающе спросила она."
            dns "Где-то я раньше видел, что у таких дверей двигались стёкла."
            dv "Ну да, только тут их не подцепить. {w}Ульяна уже пробовала."
            dns "Ну я всё-равно попробую."
            
            pause (0.7)
            show dv normal pioneer with dissolve
            
            "Я приложил ладонь к стеклу и надавил."
            
            window hide
            pause (2)
            window show
            
            "Через пару секунд оно двинулось, образовав сантиметровую щель."
            
            play sound window_dining
            
            "Я отодвинул его чуть больше, чтобы туда пролезла рука."
            
            play sound sfx_lock_open
            
            "Затем дотянулся до ручки и открыл замок с внутренней стороны."
            
            hide dv surprise pioneer with dspr
            show dv grin pioneer flt with dissolve
            play sound sfx_open_cupboard
            
            "Открыл дверь, и жестом пригласил Алису внутрь."
            dns "Дамы вперёд."
            dv "Неплохо."
            
            window hide
            scene bg int_dining_hall_night with dissolve2
            play ambience ambience_int_cabin_night fadein 3
            pause (1)
            play sound sfx_close_cabinet
            pause (1)
            window show
            
            dns "Что у нас сегодня на ужин?"
            "Сказал я, cадясь за стол, пока Алиса шарилась на кухне."
            dv "Булки!"
            dns "Музыки бы!"
            
            show dv smile pioneer with dissolve
            
            dv "Это да, но боюсь нас услышат."
            "Она поставила еду на стол и села рядом."
            dv "Угощайся."
            dns "Благодарю."
            
            window hide
            scene dveda with dissolve2
            pause (1.5)
            window show
            
            "Спустя какое-то время стало скучно."
            th "Чего молча сидеть? {w}Да и девочку стоит по-ближе узнать."
            "Я начал диалог."
            dns "Слушай, Алис, а как тебе вообще в этом лагере? {w}Нравится?"
            dv "Ну да, я уже не первый раз сюда езжу и пока не надоедает."
            dns "Есть что-то конкретное?"
            dv "Природа наверное... Она здесь шикарная."
            dns "А вы с Ульяной здесь познакомились?"
            dv "Да. А потом оказалось что мы из одного города."
            dns "Мир тесен, как говорится."
            dv "Это точно."
            
            window hide
            scene bg int_dining_hall_night with dissolve2
            show chair with dissolve
            show dv smile pioneer close with dissolve
            window show
            
            "Как продолжать диалог я не знал, но за меня это сделала Алиса."
            dv "Расскажи тоже что-нибудь."
            dns "А что тебя интересует?"
            "Произнёс я, поддерживая с ней зрительный контакт. {w}Она улыбнулась, и ответила:"
            dv "Ну о себе. Что дома делаешь, чем занимаешься впринципе."
            dns "Хм... {w}Ничего особенного, общаюсь с друзьями, гуляем иногда."
            dns "Увлекаюсь путешествиями, люблю музыку."
            dv "Что слушаешь?"
            dns "Да что душе понравится. {w}Но чаще всего что-то из рока, панк-рока."
            dv "У нас похожие вкусы. {w}А сам играешь на чём-нибудь?"
            dns "Нет, а ты?"
            dv "На гитаре."
            dns "Классно."
            dns "Знаешь, я люблю когда в песне есть смысл или лирика, как считаешь?"
            
            hide dv smile pioneer with dspr
            show dv thinking2 pioneer close flt with dissolve
            
            "Она задумалась."
            
            hide dv thinking2 pioneer close flt with dspr
            show dv smile pioneer close with dissolve
            
            dv "Да, согласна. {w}Музыка это большое искусство."
            dns "Поддерживаю."
            "Я бы хотел продолжить беседу, но не тут то было."
            voice "Кто окно открыл?"
            "Донеслось вдруг со стороны входа."
            
            hide dv smile pioneer close with dissolve
            show dv surprise2 pioneer close flt  with dissolve
            
            dv "Это Славя! Она обход ночной за вожатую делает."
            dns "Прячемся!"
            
            window hide
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
            th "Всё испортила!"
            
            show dv normal pioneer with dissolve
            
            "Мы выбрались из своих укрытий."
            dv "Вот же коза белобрысая!"
            dns "Есть такое. А вы не в ладах?"
            dv "Я с ней не общаюсь. Слишком уж правильная она, да ещё и стукачит."
            dns "Мы толком не разговаривали, но раз уж ты так говоришь, то буду иметь ввиду."
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
            
            show dv smile4 pioneer flt with dissolve
            
            "Через минуту подошла Алиса, державшая в одной руке бумажный пакет, куда положила еду, а другой протягивала мне булочку."
            dv "Держи."
            "Выглядело это очень мило."
            dns "Ой, спасибо большое."
            
            hide dv smile4 pioneer flt with dspr
            show dv smile5 pioneer flt
            with dissolve
            
            dv "Да не за что."
            "Я спрятал её маленький презент в карман."
            dns "Всё, пойдем."
            dv "Угу."

            hide dv with dissolve

            "Я забрался на подоконник и спрыгнул вниз, на траву."
            "Затем помог Алисе аккуратно спуститься."
            
            window hide
            scene black with dissolve2
            scene bg ext_square_night with dissolve
            window show
            
            "Вскоре мы вдвоём уже шли вдоль площади, по направлению своих домиков."
            
            window hide
            scene bg ext_house_of_dv_night with dissolve2
            window show
            
            show dv smile pioneer with dissolve
            
            dv "Ну всё, я пошла."
            dns "Спасибо за вечер."
            
            hide dv smile pioneer with dspr
            show dv grin pioneer flt with dissolve
            
            dv "И тебе."
            
            play sound sfx_open_cabinet_1
            hide dv grin pioneer flt with dissolve
            
            "Она помахала мне рукой и скрылась в дверях."
            "А я пошёл к себе."
            
            window hide
            scene domextnight with dissolve2
            play ambience ambience_int_cabin_night fadein 4
            pause (1)
            scene domnight with dissolve2
            window show
            
            "Сняв с себя одежду, оставил её на полу."
            "Затем плюхнулся на кровать."
            th "Боже, завтра же ещё на эту линейку идти ни свет ни заря."
            "Пришлось встать ещё раз."
            "Я поставил будильник в телефоне на {b}7:40{/b} и наконец лёг в кровать."
            
            window hide
            stop ambience fadeout 4
            pause (4)
            scene anim prolog_1 with dissolve2
            window show
            
            "Спать совершненно не хотелось."
            play music aprilrain fadein 6
            "Пока я лежал с закрытыми глазами, в моей голове было лишь одно - мысли о том, что было в столовой, а конкретно о девочке Алисе, с которой я там находился."
            th "Людей сближает общение и вместе пережитые моменты."
            th "Как же так вышло, что когда я попал сюда, то контактировал больше всего с ней, а не с кем-то другим?"
            th "Раньше я так много с девушками не общался."
            th "Было не с кем..."
            
            pause (2)
            
            th "Мда."
            th "Это ведь какой-то паррадокс!"
            th "До этого в моём окружении было множество красивых парней и девушек, но ни у кого не было пары."
            th "И ведь с этим ничего не поделать."
            th "Людей нельзя просто взять, и заставить любить."
            th "Та же любовь с первого взгляда на деле она оказывается лишь симпатией."
            th "Ведь любовь - высшее чувство, которое появляется между двумя людьми разного пола."
            th "Любовь выше дружбы, и ничто не сближает людей так, как она."
            th "Это - длительный процесс, который начинается с взаимной симпатии, и постепенно, из-за тесного общения, превращается в маленький огонёк души, который легко потухнет, если пропадёт взаимность."
            th "А в реальности люди пытаются найти любовь в интернете, через сайты и группы для знакомств."
            th "Но общение в сети и общение в жизни - это совершенно разные несвязные вещи."
            th "Отношения должны быть консервативными, и {/i}{b}общество{/b}{i} в них должно играть наименьшую роль."

            window hide
            pause (2)
            window show

            th "Боже, завтра же ещё на эту линейку идти ни свет ни заря."
            "Пришлось встать ещё раз."
            "Я поставил будильник в телефоне на {b}7:40{/b} и лёг обратно."
            "Сил продолжать думать больше не осталось, поэтому я медленно начал погружаться в сон."

            window hide
            stop music fadeout 5
            scene black with flash_black
            pause (1)
            jump estr_TFOT2
            
        "Предложить бутерброды":
            
            $ persistent.sprite_time = "night"
            dns "И чем ты собралась её открывать?"
            "Она отошла от двери на шаг и продемонстрировала мне отмычку, торчавшую из замка."
            dv "Вот."
            "Я вытащил её и осмотрел. {w}Сделана она была из заколки."
            dns "Мда, с таким инструментом мы тут до утра провозимся."
            
            show dv angry pioneer with dissolve
            
            dv "У тебя есть другие идеи?"
            dns "Есть. {w}Я с собой бутербродов привёз, можем ко мне пойти, я тебя угощу."
            
            show dv normal pioneer with dissolve
            
            "Она немного подумала, и согласилась."
            dv "Ладно, пойдём."
            
            window hide
            pause (1)
            scene bg ext_dining_hall_away_night with dissolve2
            pause (1)
            scene bg ext_square_night with dissolve2
            pause (1)
            scene bg ext_house_of_dv_night with dissolve2
            pause (1)
            show dv normal pioneer with dissolve
            
            dns "Ульяна уже спит?"
            "Поинтересовался я у Алисы, когда мы проходили мимо её домика."
            dv "Она книжку читала когда я уходила."
            dns "Она что, в темноте читает?"
            
            show dv smile pioneer with dissolve
            
            dv "Не, у нас лампа есть, мы её включаем чтоб вожатая не заходила во время обхода."
            dns "И как? Спасает от визита?"
            dv "Не всегда."
            dns "И что же вы делаете?"
            dv "Она когда приходит, по лестнице на цыпочках поднимается, но мы всё-равно слышим, и притворяемся будто спим."
            dns "А если спалит?"
            dv "Ну нас ещё ни разу не палила. Но одних ребят заставила из-за этого целый день в столовой дежурить."
            dns "Это серьёзное наказание?"
            dv "Ну считай весь день торчишь там. Ни погулять, ни на пляж сходить."
            dns "Тут пляж есть?"
            dv "Да. Лагерь же на берегу реки находится."
            dns "Прикольно. Надо будет сходить."
            dv "А ты не знал?"
            dns "Да как-то не рассказывали."
            dv "Ну приходи завтра, мы с Ульянкой купаться утром собирались."
            dns "Плавки бы где найти..."
            dv "У вожатой попроси, у неё точно есть."
            
            show dv laugh pioneer with dissolve
            
            dv "Ну если не найдешь, я тебе труселя розовые дам."
            dns "Боюсь спросить зачем они тебе."
            dv "Ты не подумай, не мои. Просто кто-то с прошлой смены в домике оставил."
            dns "Вот так находка."

            show dv smile pioneer with dissolve

            dv "Да уж."
            
            window hide
            hide dv with dissolve
            scene domextnight with dissolve2
            window show
            
            $ persistent.sprite_time = "night"
            "Разговаривая, мы подошли к моему домику."
            "Я открыл дверь и пригласил Алису внутрь."
            
            window hide
            play ambience ambience_int_cabin_night fadein 4
            play sound sfx_open_cabinet_2
            scene domnight with dissolve2
            window show
            
            "Она мельком осмотрела комнату, отодвинула себе стул и села."
            
            show chair with dissolve
            show dv smile pioneer close with dissolve
            
            dv "Доставай что у тебя там есть."
            dns "Сейчас только..."
            
            play sound light
            $ persistent.sprite_time = "day"
            scene domintnight2
            show chair
            show dv smile pioneer close
            with dspr
            pause (0.3)
            show dv surprise2 pioneer close flt with dissolve
            
            "Лунный свет и так освещал комнату, но как по мне, его было не достаточно."
            dv "Ты чего!"
            "Всполошилась вдруг Алиса."
            dns "А что такого?"
            dv "Отбой уже был! Щас вожатая блин придёт."
            
            play sound light
            $ persistent.sprite_time = "night"
            hide dv surprise2 pioneer close flt 
            scene domnight
            show chair
            show dv surprise2 pioneer close flt
            with dspr
            
            dns "Ладно-ладно, не переживай ты так."
            
            hide dv surprise2 pioneer close flt with dspr
            show dv normal pioneer close with dissolve
            play sound jimbeam
            
            "Я достал из под кровати сумку. {w}Послышался звон коньяка."
            dv "Что это у тебя там звинит?"
            dns "Да так, воды взял в дорогу."
            "Нащупав пакет с бутербродами, я вытащил его наружу и положил перед ней."
            dns "У меня ещё пироженное есть. Будешь?"
            
            show dv smile pioneer close with dissolve
            
            dv "Всё на стол!"
            "Я усмехнулся, вытащил пачку пироженного и поставил её рядом с бутербродами."
            dns "Вот, угощайся."
            dv "Спасибо."
            
            window hide
            pause (2.5)
            show dveda with dissolve2
            pause (1.5)
            window show
            
            "Алиса, кажется, задумалась о чём-то, пока жевала."
            "А я молча наблюдал за тем, как девочка ест, и за тем, как мило это выглядело в свете луны."
            
            window hide
            pause (2)
            window show
            
            "Наконец мне стало скучно, и я заговорил:"
            
            window hide
            scene domnight
            show chair
            show dv normal pioneer close
            with dissolve2
            window show
            
            dns "Слушай, Алис, а как тебе вообще в этом лагере? {w}Нравится?"
            "Она взглянула на меня."
            dv "Ну да, я уже не первый раз сюда езжу и пока не надоедает."
            dns "Есть что-то конкретное?"
            dv "Природа наверное... Она здесь шикарная."
            dns "Соглашусь."
            dns "А вы с Ульяной здесь познакомились?"
            dv "Да. А потом оказалось что мы из одного города."
            dns "Мир тесен, как говорится."

            show dv smile pioneer close with dissolve

            "Как продолжать диалог я не знал, но за меня это сделала Алиса."
            dv "Расскажи тоже что-нибудь."
            dns "А что тебя интересует?"
            "Произнёс я, поддерживая с ней зрительный контакт. {w}Она улыбнулась, и ответила:"
            dv "Ну о себе. Что дома делаешь, чем занимаешься впринципе."
            dns "Хм... {w}Ничего особенного, общаюсь с друзьями, гуляем иногда."
            dns "Увлекаюсь путешествиями, люблю музыку."
            dv "Что слушаешь?"
            dns "Да что душе понравится. {w}Но чаще всего что-то из рока, панк-рока."
            dv "У нас похожие вкусы. {w}А сам играешь на чём-нибудь?"
            dns "Пробовал на гитаре научиться, но как-то не срослось."
            dv "А у меня срослось."
            dns "Хорошо играешь?"
            dv "Слушатели не жалуются."
            dns "Видимо хорошо, раз слушатели есть."
            
            window hide
            pause (0.5)
            show dv laugh pioneer close with dissolve
            pause (0.5)
            show dv smile pioneer close with dissolve
            window show

            dns "Знаешь, я люблю когда в песне есть смысл или лирика, как считаешь?"
            
            hide dv smile pioneer with dspr
            show dv thinking2 pioneer close flt with dissolve
            
            "Она задумалась."
            
            hide dv thinking2 pioneer close flt with dspr
            show dv smile pioneer close with dissolve
            
            dv "Да, согласна. {w}Музыка это большое искусство."
            dns "Поддерживаю."
            "Я бы с радостью продолжил разговаривать с ней на разные темы, но мне приспичило."
            "Да так, что терпеть долго я не смог бы."
            dns "Алис, я на минуту.{w} Будь тут, ладно?"

            show dv surprise pioneer close with dissolve

            "И не дожидаясь ответа встал, и попятился к дверям."
            dv "Хорошо..."

            window hide
            scene domextnight with dissolve2
            play sound sfx_open_cabinet_1
            stop ambience fadeout 2
            play ambience ambience_forest_night fadein 3
            window show

            "Не зная где находится туалет, я как можно быстрее зашагал в сторону площади в надежде найти его самому."

            window hide
            pause (1)
            scene bg ext_house_of_dv_night with dissolve2
            pause (1)
            scene bg ext_square_night with dissolve2
            pause (1)
            show sl serious pioneer with dissolve
            window show

            "Моим спасением оказалась Славя, направляющаяся в ту сторону, откуда я пришёл."
            sl "Денис, ты чего не в домике? Отбой уже был."
            dns "Да-да привет. {w=0.25}Где здесь туалет?"

            show sl normal pioneer with dissolve

            sl "А тебе зачем?"
            dns "Угадай."

            show sl smile2 pioneer with dissolve

            sl "Ой, прости."
            sl "А я вот обход ночной делаю. Проверяю все ли спят."
            th "Она прикалывается?"
            dns "Славя!"

            show sl laugh pioneer with dissolve

            sl "Ладно, прости, не смогла удержаться."

            show sl smile2 pioneer with dissolve

            sl "Вон там медпункт, а за ним туалет."
            "Она показала куда-то в сторону. {w}Я быстро зашагал в указанном направлении."

            hide sl with dissolve

            "Славя осталась на месте."
            sl "Спокойной ночи!"
            "Послышалось из-за спины."
            dns "Угу."
            "Хмыкнул я себе под нос."

            window hide
            pause (1)
            scene bg ext_houses_night with dissolve2
            pause (1)
            scene bg ext_aidpost_night with dissolve2
            window show
            
            "Медпунктом оказалось небольшое одноэтажное здание с повисшим белым флагом. Предположительно на нём был красный крест."
            "Свет внутри не горел. Собственно, мне туда и не надо было."
            "Пройдя чуть дальше, я увидел небольшие кабинки, которые и представлял из себя туалет."

            window hide
            pause (1)
            play sound_loop clock_timeskip fadein 2
            show white_screen with dissolve2
            show flt_timeskip_logo1 with dissolve
            pause (1)
            show flt_timeskip_logo2
            with dissolve
            hide flt_timeskip_logo2
            show flt_timeskip_logo1
            with dspr
            show bg ext_square_night
            show white_screen
            with dissolve2
            pause (1)
            stop sound_loop fadeout 2
            hide flt_timeskip_logo1
            hide white_screen
            with dissolve2
            pause (1)
            window show

            "Когда я возвращался домой, Слави на площади уже не было."
            th "Проверила всё походу, и спать пошла."
            th "Летом всегда ложишься спать раньше, так как световой день больше, активность больше, да и вцелом время медленнее летит."

            window hide
            scene bg ext_house_of_dv_night with dissolve2
            window show

            th "Так подумать, незачем было в столовую идти, ведь голод пропал после первого бутерброда."
            th "Хотя нет, не пошёл бы я туда - не встретил бы Алису."
            th "Приятно всё-таки с девушкой общаться. Особенно когда не надо из себя что-то выдавливать из-за того, что человек не может поддержать диалог."
            th "А с Алисой как-то легко получается вести разговор. Хотя мы едва знакомы."

            window hide
            scene domextnight with dissolve2
            pause (1)
            play ambience ambience_int_cabin_night fadein 1
            play sound sfx_open_cabinet_2
            scene domnight with dissolve2
            window show

            dns "Ну как ты тут? Всё пирожное уже схомячила?"
            "Открывая дверь, ещё с порога проговорил я."

            window hide
            play music aprilrain fadein 4
            show dv_sleep_window with dissolve2
            window show

            "Алиса мирно спала, облакотившись на подоконник."
            dns "А. {w=0.4}Вот оно что..."
            "Я сделал пару шагов к ней - она никак не отреагировала."
            "Отодвинув стул, я аккуратно сел рядом. {w}Девочка тихо посапывала."
            "Лунный свет красиво ложился на её щёку, веки были закрыты, а губы едва поблёскивали."
            "Определённо, внешние данные у неё были впечатляющие."
            "Когда её бёдра и торс обтягивали спортивные шорты с заправленной в них футболкой, я разглядел, что она очень стройная, и видно, что следит за своей фигурой."
            "Лицо - отдельный разговор. {w}Острый подбородок, аккуратный нос, большие глаза, про цвет которых вообще бессмысленно говорить, тонкие брови."
            "Всё это в купе с короткой стрижкой и необычным цветом волос образует потрясающую картину."
            "Из всех встреченных девочек, она была самой привлекательной. {w}Не то чтобы я гнался исключительно за красотой, нет. Мне важен человек как личность, не как сущность."
            th "Интересно, какой длинны у неё волосы без заколок."
            "Алиса едва заметно дёрнулась."
            th "Вот на сколько она крепко спит? {w}Надо бы проверить."
            "Я аккуратно тыкнул её в бок."
            "Она лишь немного поёжилась."
            th "Нужна более действенная мера."
            "Я положил руку ей на плечо и немного потолкал."
            "В ответ получил лишь недовольное мычание."
            th "И что же мне с тобой делать, спящая красавица?"
            "Переложить на кровать и спать с ней в одной комнате? Не, херня затея, потом по шапке получу от неё же, мол чего не разбудил."
            "А будить мне её совершенно не хотелось - уж слишком мило она спала."
            "Значит остаётся лишь один вариант - донести её до дома самому, благо до него не далеко."
            
            window hide
            stop music fadeout 4
            hide dv_sleep_window with dissolve2
            window show

            "Я поднялся со стула и тихо поставил его на место."
            "Затем встал позади Алисы и потянул её к себе за плечи."
            "Теперь она сидела, облакотившись на спинку стула и склонив голову вперёд."
            "Я подошёл к ней сбоку, чуть присел, одной рукой обхватил спину, а другой взял под колени."
            "Затем встал, и Алиса уже лежала у меня на руках."
            "Весила она, считай, ничего. Девочка всё-таки."

            window hide
            play ambience ambience_forest_night fadein 4
            play sound sfx_open_cabinet_1
            scene domextnight with dissolve2
            window show

            "Конечно, было не очень удобно её так нести, ведь сама она никак за меня не держалась."
            "Но это было терпимо, так как её домик буквально через пятдесят метров от моего."
            "Пока я её нёс, она успела уткнуться лицом мне в плечо, отчего я чувствовал её теплое дыхание."
            
            window hide
            scene bg ext_house_of_dv_night with dissolve2
            pause (1)
            play sound sfx_open_door_squeak_2
            play ambience ambience_int_cabin_night
            scene int_house_of_dv_night2 with dissolve2
            window show

            "Поддев носком край двери, я тихонько открыл её и занёс прижавшуюся ко мне Алису внутрь."
            "В темноте небыло видно, спит ли мелкая, но судя по тому, что она никак не отреагировала на наше появление - спит."

            play sound sfx_bed_squeak2

            "Я подошёл к соседней кровати, и положил Алису на неё."

            window hide
            show dv_sleep_bed with dissolve2
            window show

            th "Как она в верхней одежде то спать будет."
            th "И чё делать? Не раздевать же её тут."
            th "Хотя вроде темно, и ничего не видно..."
            th "Нет. Не хватало ещё ей, или Ульяне проснуться, пока я буду стягивать с неё юбку. {w}Сандали сниму, а спать так будет."
            "Я аккуратно расстегнул застёжки, снял обувь с её ступней и поставил рядом с кроватью."

            window hide
            hide dv_sleep_bed with dissolve2
            window show

            th "Вроде всё."
            "Я поспешил покинуть их с Ульяной жилище."
            
            window hide
            play sound sfx_open_cabinet_1
            play ambience ambience_forest_night fadein 2
            scene bg ext_house_of_dv_night with dissolve2
            window show

            "Беготня по лагерю в поисках туалета и тоскание спящей девочки на руках отняло у меня приличное количество сил, потому я не задумываясь ни о чём, на автомате побрёл к своему домику."

            window hide
            pause (1)
            scene domextnight with dissolve2
            pause (1)
            play sound sfx_open_cabinet_2
            play ambience ambience_int_cabin_night fadein 2.0
            scene domnight with dissolve2
            window show

            "Скинув с себя одежду я обессиленно плюхнулся на кровать."

            window hide
            pause (1)
            play music deepcosmo fadein 7
            scene anim prolog_1 with dissolve2
            window show

            "Сознание заполонила куча мыслей, как это и бывает, когда в конце дня наконец остаёшься наедине с самим собой."
            "В их число входили мысли и о девочке Алисе, с которой я сегодня провёл столько времени."
            th "Как же так вышло, что когда я попал сюда, то контактировал больше всего именно с ней, а не с кем-то другим?"
            "Определённо, внешние данные у неё были впечатляющие."
            "Когда её бёдра и торс обтягивали спортивные шорты с заправленной в них футболкой, я разглядел, что она очень стройная, и видно, что следит за своей фигурой."
            "Лицо - отдельный разговор. {w}Острый подбородок, аккуратный нос, большие глаза, про цвет которых вообще бессмысленно говорить, тонкие брови."
            "Всё это в купе с короткой стрижкой и необычным цветом волос образует потрясающую картину."
            "Из всех встреченных девочек, она была самой привлекательной. {w}Не то чтобы я гнался исключительно за красотой, нет. Мне важен человек как личность, не как сущность."
            th "Интересно, какой длинны у неё волосы без заколок."
            th "Раньше я так много с девушками не общался. {w}Было не с кем..."
            
            pause (2)
            
            th "Мда."
            th "Это ведь какой-то паррадокс!"
            th "До этого в моём окружении было множество красивых парней и девушек, но ни у кого не было пары."
            th "И ведь с этим ничего не поделать."
            th "Людей нельзя просто взять, и заставить любить."
            th "Та же любовь с первого взгляда на деле она оказывается лишь симпатией."
            th "Ведь любовь - высшее чувство, которое появляется между двумя людьми разного пола."
            th "Любовь выше дружбы, и ничто не сближает людей так, как она."
            th "Это - длительный процесс, который начинается с взаимной симпатии, и постепенно, из-за тесного общения, превращается в маленький огонёк души, который легко потухнет, если пропадёт взаимность."
            th "А в реальности люди пытаются найти любовь в интернете, через сайты и группы для знакомств."
            th "Но общение в сети и общение в жизни - это совершенно разные несвязные вещи."
            th "Отношения должны быть консервативными, и {i}{b}общество{/b}{/i} в них должно играть наименьшую роль."

            window hide
            pause (2)
            window show

            th "Боже, завтра же ещё на эту линейку идти ни свет ни заря."
            "Пришлось встать ещё раз."
            "Я поставил будильник в телефоне на {b}7:40{/b} и лёг обратно."
            "Сил продолжать думать больше не осталось, поэтому я медленно начал погружаться в сон."

            window hide
            stop music fadeout 5
            stop ambience fadeout 5
            scene black with flash_black
            pause (1)
            jump estr_TFOT2





            







            
            
            
            
            