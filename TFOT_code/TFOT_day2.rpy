label estr_TFOT2:

    $ backdrop = "day"
    $ new_chapter(2, u"Судьбы двух. День 2")
    $ day_time()
    $ persistent.sprite_time = "day"
    play ambience ambience_int_cabin_day fadein 4
    play sound clock_alert
    scene dom with dissolve2

    "Проснулся я от сигнала будильника."
    "К моему удивлению - в кровати в которой и уснул, а не в автобусе."
    "В голову нахлынули воспоминания о вчерашнем вечере."
    
    if day1_vzlom:
        "хуй"
    
    else: 
        window hide
        scene dv_sleep_window
        show prologue_dream
        with dissolve2
        pause (2)
        scene dv_sleep_bed
        show prologue_dream
        with dissolve2
        pause (2)
        scene dom with dissolve2
        pause (2)
        window show

        "От воспоминаний того, как Алиса сопела уткнувшись мне в плечо, на лице появилась непрозвольная улыбка."

    "Я поднялся с кровати и начал одевать форму, часть которой валялась на полу."

    play music music_list["forest_maiden"] fadein 4
    play sound sfx_open_door_strong
    show sl smile sport with dissolve

    "Дверь вдруг распахнулась, и в помещение зашла Славя, одетая в спортивный костюм."
    "К счастью, к тому моменту я уже одел шорты."
    sl "Доброе утро!"
    th "Стучаться не учили?"
    dns "Привет. Ты чего так?"
    sl "Вожатая попросила тебе передать умывальные принадлежности. {w}Держи."
    "Я взял пакет из её рук и поставил на стол."
    "В нём оказалась ничем не примечательная счётка и зубной порошок."
    th "Давно я его не видел. {w}Последний раз, наверное, в деревне, ещё будучи ребёнком."
    th "Не стоило ей конечно так врываться, но за это спасибо."
    dns "Благодарю."
    sl "Не опаздывай на линейку!"
    "Сказала Славя, уходя."
    
    hide sl with dissolve
    play sound sfx_open_cabinet_2

    "Я завязал галстук на шее, взял пакет с умывальными принадлежностями и вышел на улицу."

    window hide
    play sound sfx_open_cabinet_2
    play ambience ambience_day_countryside_ambience fadein 3
    play music music_list["sweet_darkness"] fadein 4
    scene domext with dissolve2
    window show
    
    "Снаружи дул прохладный утренний ветер, пахло свежестью, на траве была раса."

    window hide
    scene bg ext_house_of_dv_day with dissolve2
    pause (1)
    scene bg ext_square_day with dissolve2
    pause (1)
    show mt normal pioneer far with dissolve
    window show

    "В поисках умывальников я вышел на площадь, где меня окликнула вожатая."
    mt "Денис! {w}Постой."

    show mt normal pioneer with dissolve
    
    "Она подошла ко мне и протянула какой-то листок."
    mt "Вот, держи."
    dns "Что это?"
    mt "Это - обходной лист. Тебе нужно до обеда посетить всё, что тут указано."
    th "Не плохое начало дня. Как раз лагерь этот по-ближе узнаю."
    dns "Хорошо. {w}А чего через Славю не передали?"
    mt "Забыла ей отдать. {w}Всё, бегом к умывальникам! Пионер должен быть чист и опрятен."
    "Скомандовала вожатая."
    dns "А где они находятся?"
    mt "Рядом с музыкальным клубом есть. Он вон там."
    "Она указала в сторону."
    dns "Спасибо."
    mt "Про обходной не забудь!"
    dns "Да, конечно."

    window hide
    hide mt with dissolve
    pause (1)
    scene ext_admins_day_7dl with dissolve2
    pause (1)
    scene bg ext_musclub_day with dissolve2
    pause (1)
    window show

    "Здание музыкального клуба выглядело, скажем так, необычно."
    "С одной стороны была веранда, а с другой огромноe панарамное стекло, занимающее весь периметр стены."
    "Дальше виднелись умывальники."

    window hide
    pause (1)
    scene bg ext_washstand_day with dissolve2
    show mi normal pioneer far with dissolve
    window show

    "Когда я подошёл, от них уходила какая-то девушка необычной внешности."

    window hide
    show mi normal pioneer with dissolve
    pause (1)
    hide mi with dissolve
    window show

    "Проходя мимо меня, она подмигнула."
    "У неё были два огромных циановых хвоста, азиатская внешность и небольшой  рост."

    window hide
    scene bg ext_washstand2_day with dissolve2
    pause (1)
    play sound sfx_close_water_sink
    play sound sfx_water_sink_stream
    window show

    "Прежде чем начать чистить зубы, я включил кран и набрал воды в ладоши. {w}Ледяной воды."

    play sound sfx_water_splash
    
    th "Уф, бодрит."
    "Помочив счётку, я нанёс на неё горсть порошка и принялся чистить зубы."
    "Закончив, сплюнул и снова набрал воды."
    "Тщательно прополоскав ротовую полость, убрал умывальные принадлежности обратно в пакет, и направился в домик."

    window hide
    pause (1)
    scene bg ext_musclub_day with dissolve2
    window show

    "По пути я достал из кармана листок, который дала мне вожатая."
    "Развернув его, моим глазам предстал немаленький список:"
    "В нём были перечислены места, которые требовалось посетить новым жителям лагеря."
    "В число мест входили: Спортивные секции..."
    th "Заочно посетил."
    "Кружок кибернетики..."
    th "Тоже."
    "Музыкальный клуб..."
    th "Вот он как раз."
    "Библиотека..."
    th "Не самое интересное место."
    "Медпункт."
    th "Неужели у лагеря есть подозрения на то, что к ним приедет больной?{w} Не думаю что много ребят, не здор{b}о{/b}во себя чувствующих, ездят в пионер лагеря."
    "Пользуясь моментом, я решил получить подпись в муз-клубе."

    window hide
    scene ext_music_club_verandah_day with dissolve2
    window show
    
    "Оказавшись на его пороге, я не стучась зашёл зашёл внутрь."

    window hide
    play sound sfx_open_door_strong
    scene bg int_musclub_day with dissolve2
    play ambience ambience_music_club_day fadein 3
    pause (1)
    show spina_mi with dissolve
    window show

    "Посреди комнаты стояла девушка, спиной ко мне.{w} Та самая, что подмигнула мне возле умывальников."
    "Она развернулась на шум двери."

    hide spina_mi with dspr
    show mi smile pioneer far with dissolve

    mi "Ой, привет!"
    mi "Денис, да? Мне говорили что ты новенький."
    dns "Привет, да."
    "Коротко ответил я. {w}Она, в отличии от меня, так делать не собиралась."
    mi "А меня Мику зовут! Никто не верит, но у меня такое имя. Моя мама - японка, а папа - русский."
    dns "Классно. {w}Слушай, мне тут обходной выдали, и там сказано что муз-клуб надо посетить. Можешь как-то отметить то, что я пришёл?"
    "Японка закивала."
    mi "Сейчас-сейчас, только ручку возьму!"

    window hide
    hide mi with dissolve
    play sound storagenoise
    pause (3)
    show mi smile pioneer with dissolve
    window show

    mi "Давай сюда."
    "Я протянул ей листок. {w}Она быстро расписалась в нём и вернула мне назад."
    dns "Спасибо!"
    mi "Незачто! А ты случаем музыкой не увлекаешься? Не хотел бы записаться в музыкальный кружок?"
    th "С одной стороны музыка мне близка, и я даже кое-как научился играть на гитаре."
    th "Но с другой стороны -  я уже давно ни на чём не играл, и больше предпочитаю слушать музыку, а не создавать её."
    "Придя к выводу, что записываться я не очень то и хочу, я решил вежлово отказаться:"
    dns "Мику, прости, но нет."
    
    show mi sad pioneer with dissolve

    mi "Почему?"
    dns "Понимаешь, я когда-то умел на гитаре играть, но это очень давно было, да и не хочется заного начинать."

    show mi grin pioneer with dissolve

    "Её глаза блестнули."
    mi "Так я тебе помогу вспомнить как играть!"
    "Кажется, она не услышала конец моей фразы."
    dns "Не хочу, говорю, заново учиться играть."

    show mi sad pioneer with dissolve
    
    mi "Ну ладно..."
    "Грустно протянула она."
    dns "Ещё раз спасибо за обходной. {w}Хорошего дня!"

    show mi smile pioneer with dissolve

    mi "И тебе!"
    "Всю её грусть на лице будто ветром сдуло. Девочка снова заулыбалась и больше не выглядела расстроенной."

    window hide
    pause (1)
    play sound sfx_open_cabinet_2
    play ambience ambience_day_countryside_ambience fadein 4
    scene ext_music_club_verandah_day with dissolve2
    window hide

    "Я вышел на улицу и направился в сторону домика."

    window hide
    scene bg ext_musclub_day with dissolve2
    pause (1)
    scene vorota with dissolve2
    pause (1)
    window hide

    "Но на развилке, вместо того чтобы пойти прямо, повернул направо, дабы получить подпись кибернетиков."

    window hide
    scene bg ext_clubs_day with dissolve2
    play sound sfx_open_door_strong
    pause (1)
    show el normal pioneer far at left
    show sh normal pioneer far 
    show sl normal sport far at right
    with dissolve
    show sl smile sport far at right with dissolve
    window show

    "Я было хотел постучаться, но дверь вдруг открылась, и оттуда вышли Электроник, Шурик и Славя."
    dns "Привет парни, привет Славя."
    all "Привет!"
    sl "Денис, сейчас линейка начнётся, ты не забыл?"
    dns "Не забыл. {w}Электроник, можешь задержаться? Помощь твоя нужна."
    el "Да, конечно. Ребят, я позже подойду."
    sl "Не опаздывай."

    window hide
    hide sl
    hide sh 
    with dissolve2
    hide el with dissolve
    show el normal pioneer with dissolve

    el "А в чём собственно проблема?"
    dns "Да ничего сверх сложного. {w}Вожатая обходной выдала, ты не мог бы подпись поставить?"
    el "Конечно могу, только тогда нужно зайти в клуб."
    dns "Ну давай."

    window hide
    scene bg int_clubs_male_day with dissolve2
    play sound sfx_open_door_clubs
    play ambience ambience_int_cabin_day fadein 3
    window show
    show el normal pioneer with dissolve

    "Электроник взял со стола ручку."
    el "Давай свой обходной."
    "Я протянул ему листок. {w}Он быстро расписался в нём."
    dns "Благодарю. {w}Как кстати к тебе можно обращаться помимо «Электроника»."
    "Спросил я, взяв бегунок и убирав его в карман."
    el "Ну можешь называть Элом, или накрайняк Серёжей. {w}Только не Сыроежкой, как Ульяна, пожалуйста."
    dns "Без проблем."
    el "Ладно, пойдем."
    dns "Угу."

    window hide
    scene bg ext_clubs_day with dissolve2
    play sound sfx_open_door_clubs
    play ambience ambience_day_countryside_ambience fadein 3
    show el normal pioneer with dissolve
    window show

    dns "Я пошёл. Мне в домик умывальные принадлежности надо занести."
    el "Поторопись, щас линейка уже начнется, а Ольга не любит когда на неё опаздывают."
    dns "Постараюсь."
    
    window hide
    scene vorota with dissolve2
    window show
    
    "На развилке я повернул на улицу с домами, оставляя клубы позади."

    window hide
    pause (1)
    scene domext with dissolve2
    pause (1)
    play sound sfx_open_cabinet_1
    play ambience ambience_int_cabin_day fadein 3
    scene dom with dissolve2
    window show

    "Стараясь всё делать быстро, я вытащил сумку из под стола, расстегнул молнию и положил умывальные принадлежности сверху."
    "Закрывать сумку я не стал, лишь толкнул её обратно под кровать, совсем позабыв что помимо одежды ещё находится внутри."
    "На всякий случай проверив наличие в кармане обходного, вышел из домика и направился на площадь."

    window hide
    play sound sfx_open_cabinet_2
    play ambience ambience_day_countryside_ambience fadein 3
    scene domext with dissolve2
    pause (1)
    scene bg ext_house_of_dv_day with dissolve2
    pause (1)
    scene bg ext_square_day with dissolve2
    pause (1)
    window show

    "Когда я пришёл, пионеры уже выстраивались в шeренги."
    "Ближе всего к памятнику стояли мои все мои знакомые."
    "Славя стояла с табличкой «{b}ПЕРВЫЙ ОТРЯД». {w}Алиса с Ульяной хихикали.{w} Электроник с Шуриком что-то обсуждали.{w}Лена общалась с Мику."

    show mt normal pioneer with dissolve

    "Как только я встал в строй, Ольга объявила:"
    if day1_vzlom:
        mt "Доброе утро ребята, сегодня линейка начнётся с не очень приятных новостей, ведь вчера вечером повара испекли вкусныъ сдобных булок, а ночью, после отбоя кто-то проник в столовую через окно, и сегодня утром наш повар Мария не досчиталась целого пакета."
        mt "Я не знаю кто это сделал, но хочу заставить этого человека задуматься, ведь повара тратят свои силы и продукты на то, чтобы накормить вас."
        mt "А из-за того, кто украл пакет, сегодня на завтраке кто-то останется без булки."
        "По рядам пронёсся огорчённый гул."
    else:
        mt "Ребята, сегодняшний день начинается с хороших новостей! Вчера вечером наши повара испекли для вас сдобных булочек!"
        "По рядам пронёсся радостный гул."
        mt "Так же в конце дня пройдёт футбольный матч между младшими отрядами, всех желающих приглашаю посмотреть."
        "Судя по отсутствию реакции, никому небыло дела до того, как малышня будет гонять мяч."
        "Я решил убедиться в своей теории, и когда вожатая отвернулась, тихонько подошёл к Ульяне."

        show us smile sport with dissolve

        dns "Ты будешь в этом матче учавствовать?"
        us "Нет конечно! Там только мелкие, а они играть не умеют!"

        show us laugh sport with dissolve

        us "А ты чего, записаться хочешь?"
        dns "Нет, просто было интересно твоё мнение."

        hide us with dissolve

        "Я вернулся на своё место."

    show mt normal pioneer with dissolve

    mt "А сейчас, все желающие пойти на спорт площадку шаг вперёд."
    "Ульяна, Славя и некотрые пионеры из других отрядом шагнули из строя."
    mt "На{w=0.2}-пра-{w=0.2}во! {w}Ша{w=0.2}-гом марш!"
    mt "Остальные могут быть свободны до завтрака."
    "Все начали расходиться, я пошёл в сторону медпункта, дабы получить подпись медсестры."

    window hide
    pause (1)
    scene bg ext_houses_day with dissolve
    window show
    
    "Но по пути кто-то легонько толкнул меня в плечо."
    "Я обернулся."

    show dv normal sport flt with dissolve
    
    "Передомной стояла Алиса."
    "Она была одета в спортивную форму, и по всей видимости шла на зарядку."
    "Тут подтвердилась моя догадка о том, что она следит за фигурой."
    dns "Привет, Алис."
    if day1_vzlom:
        dv "Привет. {w}Помнишь наш разговор?"
        dns "Насчёт?"
        dv "Про пляж. Пойдешь сегодня с нами купаться после завтрака?"
        dns "Да, пойду."
        dv "Ты плавки нашёл?"
        dns "Нет."

        show dv laugh sport flt with dissolve

        dv "Моё предложение о розовых труселях ещё в силе!"
        dns "Оставь себе, я у вожатой попрошу."
        dv "Её купальник на тебя не налезет."
        "Мы оба рассмеялись."
        dv "Короче, жду после завтрака."
        dns "Хорошо. {w}Ты щас куда кстати?"

        show dv smile sport flt 

        dv "На спорт площадку. А что?"
        dns "Да просто интересно."

        show dv normal sport flt with dissolve

        "Алиса с интересом изогнула бровь."
        dns "Ладно, увидимся после завтрака."
        dv "Давай."
        hide dv normal sport flt with dissolve
    else:
        dv "Привет, можешь рассказать что произошло вчера?"
        dns "А что последнее ты помнишь?"
        dv "Ну ты ушёл, я была уставшей, потому облакотилась на подоконник, прикрыла глаза, а проснулась уже утром у себя в постели."
        dv "Ульяна ничего не знает, говорит что спала, но по глазам вижу, что что-то знает, и не рассказывает."
        dns "Когда я вернулся, ты спала на подоконнике, я попытался тебя разбудить, но ты не просывалась."

        show dv shy sport flt with dissolve

        dns "Потом я тебя на руках донёс до домика, снял сандали и уложил на кровать."
        "Алиса выглядела смущённой."
        "Меня это позабавило, и я продолжил:"
        dns "Затем поцеловал в губы, пожелал спокойной ночи и ушёл."

        show dv shoked sport flt with dissolve

        dv "..."
        dns "Да шучу я!"

        show dv angry sport flt with dissolve

        dv "Дурак!"
        "Обидно назвала меня она."
        dns "Понравилось на руках кататься?"
        "Съязвил я в ответ."

        show dv shy sport flt with dissolve

        dv "Иди ты..."
        dns "Это кстати было не бесплатно. {w}Взамен скажи мне где находится библиотека."

        show dv normal sport flt with dissolve

        dv "Идешь вон туда, там проходишь медпункт, за ним туалет а дальше библиотека."
        dns "Спасибо."
        dv "Помнишь наш разговор?"
        dns "Насчёт?"
        dv "Про пляж. Пойдешь сегодня с нами купаться после завтрака?"
        dns "Да, пойду."
        dv "Ты плавки нашёл?"
        dns "Нет."

        show dv laugh sport flt with dissolve

        dv "Моё предложение о розовых труселях ещё в силе!"
        dns "Оставь себе, я у вожатой попрошу."
        dv "Её купальник на тебя не налезет."
        "Мы оба рассмеялись."
        dv "Короче, жду после завтрака."
        dns "Хорошо. {w}Ты щас куда кстати?"

        show dv smile sport flt with dissolve

        dv "На спорт площадку. А что?"
        dns "Да просто интересно."

        show dv normal sport flt with dissolve

        "Алиса с интересом изогнула бровь."
        dns "Ладно, увидимся после завтрака."
        dv "Давай."

        hide dv normal sport flt with dissolve

    "Алиса ушла в сторону площади догонять колонну вожатой. {w} я же направился в медпункт."
    
    window hide
    pause (1)
    scene bg ext_aidpost_day with dissolve2
    window show

    "Ночью я не ошибся - на флаге, что висел на крыше, был изображён красный крест."

    play sound sfx_knock_door7_polite

    "Оказавшись на крыльце, я постучал, дабы убедиться что там не занято."
    csp "Войдите!"
    "Послышалось изнутри."

    window hide
    play sound sfx_open_cabinet_2
    pause (1)
    scene int_aidpost_day with dissolve2
    play ambience ambience_medstation_inside_day fadein 3
    window show

    "Внутри медпункта оказалось довольно прохладно."
    "В помещении было всё необходимое для осмотра: весы для взвешивания, таблица Снеллена для проверки глаз. {w}Множество разных медицинских приборов на столе. Даже некое подобие компьютера."

    play music music_list["eternal_longing"] fadein 3
    show cs normal glasses far with dissolve

    "Изучая комнату, я совсем не обратил внимания на медсестру. {w}Она сидела на стуле и выжидиюще смотрела на меня."
    dns "Здравствуйте."
    csp "Привет пионер, рассказывай с чем пришёл."
    "Медсестра выглядела молодо. У неё были тёмные волосы, собрраные сзади в хвост, а также разного цвета глаза."
    th "Наверное линзы носит... хотя были ли они в СССР? {w}Не уж то и правда гетерохромия?"
    "Я хотел посмотреть на бэйджик, но сразу отвёл взгляд."
    "Верхние пуговицы халата медсестры были расстегнуты, и если бы я попытался прочитать надпись, то со стороны это бы выглядело так, будто я пялюсь на её грудь."
    dns "А... Извините, а как к вам обращаться?"
    cs "Меня зовут Виолетта Церновна, но можешь называть Виолой."
    dns "Очень приятно... Виола. Меня к вам вожатая отправила с обходным."
    cs "А, ты новенький? Денис, да?"
    dns "Да, это я."
    "Она говорила так, что складывалось ощущение, будто все слова она произносит на выдохе."
    cs "А ты почему на утреннюю зарядку не пошёл? Минздрав рекомендует между прочим!"
    dns "Да я бы с радостью, только у меня же обходной."
    cs "Ладно, давай свой листок, только перед подписью мне нужно тебя осмотреть."
    "Она встала со стула и начала приближаться ко мне."
    "Осмотр в мои планы не входил."
    dns "А можно как-то без этого обойтись?"
    "Сказал я, пятясь назад."
    "Виола вдруг остановилась."
    cs "Можно, если ты пообещаешь мне впредь ходит на утренниe занятия."
    dns "Конечно обещаю!"

    show cs smile glasses far with dissolve

    cs "Точно?"
    dns "Точно! {w}Не будь у меня обходного, я бы непременно туда пошёл!"
    cs "Вот и хорошо. Давай его сюда."
    "Я протянул ей бегунок. {w}Она вытащила из кармана ручку, расписалась в нём и вернула мне назад."
    dns "Благодарю. {w}Хорошего дня!"
    "Сказал я, уходя."
    cs "Не болей, пионер."

    window hide
    play sound sfx_open_cabinet_2
    scene bg ext_aidpost_day with dissolve2
    stop music fadeout 3
    play ambience ambience_day_countryside_ambience fadein 3
    window show

    th "Интересно, а в этом лагере вообще работают мужчины? Ну или хотя-бы пожилые люди."
    th "А то это не пионер лагерь из совка, а царство амазонок, которое мне снится."
    th "Может библиотекарша окажется ворчливой бабкой? Никогда бы не подумал, что буду рад такому."
    "Закончив монолог, я отправился в сторону библиотеки."

    window hide
    pause (1)
    scene bg ext_library_day with dissolve2
    window show

    "Здание библиотеки ничего особенным не выделялось. Лишь слева от входа располагалась пристройка с пожарным щитом."

    window hide
    play sound sfx_open_cabinet_2
    scene bg int_library_day with dissolve2
    play ambience ambience_library_day fadein 3
    window show

    "Внутри меня встретило множество гербов и плакатов с советской символикой."
    th "Серп и молот, серп и молот, серп и молот... {w}Везде серп и молот!"

    window hide
    camera:
        perspective True
        zpos 0
        linear 2 xpos -250 zpos -600
    pause (2)
    window show

    th "А, нет. Ещё портреты Владимира Ильича, и его же бюсты."
    th "Я не антикоммунист, но в современном мире не вооружённым взглядом видно, что капитализм победил."
    th "Господство товарно-денежных отношений, превращение рабочей силы в товар, эксплуатация наёмных рабочих - перечислять можно долго, но факт остаётся фактом."
    "Чуть дальше виднелись полки с книгами, столики, кресла. На дальнем камоде стоял барабан, а на нём лежала труба."

    window hide
    camera:
        perspective True
        linear 2 xpos 0 zpos 0
    pause (2)
    window show

    th "Так, ну и где же следящий за всем этим марксистским безобразинем?"
    
    window hide
    show mz normal glasses pioneer with dissolve
    play music music_list['your_bright_side'] fadein 4
    pause (1)
    window show

    mzp "Зачем пришёл?"
    "Спросила вдруг девушка, возникшая передомной из ниоткуда."
    dns "Обходной. {w}А как тебя..."
    mz "Женя."
    dns "Денис."
    "Она была маленького роста, носила очки и имела каре темно-синего цвета."
    "При моих ста восьмидесяти с хвостиком, она была мне по плечо."

    show mz bukal glasses pioneer with dissolve

    mz "Ну чё ты встал, давай свой обходной."
    "Грубо потребовала библиотекарша."
    dns "Да не кипятись, я тебе ещё ничего не сделал."
    "Сказал я, протягивая ей вынутый из кармана листок."
    mz "Да постоянно приходите и стоите как истуканы. Будто книг ни разу не видели!"
    th "Ну с тем, как ты встречаешь людей, неудевительно что тебе сл{b}о{/b}ва боятся сказать."
    dns "Ну бывает."
    "Женя поставила подпись и отдала мне листок со словами:"
    mz "Бывает... Да ну вас!"
    dns "Пока."

    window show
    pause (1)
    play sound sfx_open_cabinet_2
    scene bg ext_library_day with dissolve2
    stop music fadeout 3
    play ambience ambience_day_countryside_ambience fadein 3
    window show

    "Ответа не последовало."
    th "Мда... Хотел старух увидеть - вот тебе старуха, правда в молодом теле."
    th "Так, что там следующее?"
    "Я посмотрел на бегунок."
    th "Всё что ли?!"

    play sound sfx_dinner_horn_processed

    th "Вовремя уложился. {w}Можно и на завтрак."

    window hide
    pause (1)
    scene bg ext_aidpost_day with dissolve2
    pause (1)
    scene bg ext_square_day with dissolve2
    pause (1)
    scene bg ext_dining_hall_away_day with dissolve2
    pause (1)
    window show

    "На подходе к столовой я увидел Ольгу Дмитриевну, которая вместе с той частью людей, что пошли на зарядку, маршировала завтракать."
    "Я прибавил ходу, дабы встать в очередь первее."

    window hide
    pause (1)
    scene bg ext_dining_hall_near_day with dissolve2
    pause (1)
    play sound sfx_open_cabinet_2
    scene bg int_dining_hall_empty with dissolve2
    window show

    "Не смотря на отсутствие немалой части людей, в столовой все-равно выстроилась приличная очередь."

    window hide
    scene bg int_dining_hall_notfull with dissolve2
    window show

    "Я занял место, и через какое-то время настал мой черёд брать еду."
    if day1_vzlom:
        show cook_sad with dissolve
        dns "Здравствуйте тёть Маш."
        mar "Привет, Денис. {w}Компот будешь?"
        dns "Буду."
        "В этот раз Мария выглядела расстроенной."
        "Пока она наливала мне компот и поливала сырники сгущёнкой, я спросил её:"
        dns "Тёть Маш, а что вы грустная такая?"
        mar "Да представляешь, сегодня ночью кто-то в столовую через окошко пробрался, и пакет булок стащил! Форточники прям!"
        dns "Я слышал, нам на линейке рассказывали."
        dns "Не переживайте вы так, чего из-за хлеба расстраиваться."
        mar "Да я не из-за хлеба, а от того, что среди пионеров есть такие нечестные люди. {w}Тут ведь все считай свои, все друг-друга знают, и вот так подло поступают."
        dns "Ну да, согласен, неприятно. {w}Но уже ничего не поделать. Разве что надеяться, что у человека проснётся совесть, и он так больше не будет делать."
        mar "Ну да. {w}Ты сам булку то будешь?"
        menu:
            "Взять булку":
                "А почему бы и нет?"
                dns "Да, давайте."
                show cook_normal with dissolve
                mar "Вот, держи свою тарелку, и вот тебе булка. {w}Приятного аппетита!"
                dns "Спасибо тёть Маш!"
            "Отказаться":
                "Не, я и так ночью их ел. Правильнее будет отказаться."
                dns "Не, пусть другим достанется, я не голодный."
                show cook_smile with dissolve
                mar "Какой ты молодец! Настоящий пионер!"
                dns "Чего уж там..."
                mar "Вот, держи свою тарелку. {w}Приятного аппетита!"
                dns "Спасибо тёть Маш!"
                hide cook_smile with dissolve
    else:
        show cook_smile with dissolve
        dns "Здравствуйте тёть Маш."
        mar "Привет, Денис. {w}Компот будешь?"
        dns "Буду."
        mar "Погода сегодня хорошая, не правда?"
        "Поливая сырники сгущёнкой, спросила Мария."
        dns "Да, суперская просто. {w}Я вот на пляж пойду сегодня."
        mar "Я бы тоже с удовольствием сходила, да вот работаю."
        dns "Тогда не смею вас отвлекать!"
        "Проговорил я, взяв тарелку, которую мне протянула повар."
        show cook_laugh with dissolve
        mar "Приятного аппетита!"
        dns "Спасибо тёть Маш!"
        hide cook_laugh with dissolve

    "Я взял еду и пошёл искать столик."
    "Какая-то часть пионеров ещё стояла в очереди, так что ещё оставались свободные столы."
    "Уселся я за крайний, что находился и окна."

    window hide
    show food_breakfast with dissolve2
    pause (2)
    window show

    "Сырники настолько вкусными, что я упллетал их, не поднимая голову."

    window hide
    scene bg int_dining_hall_people_day
    show us laugh pioneer close
    show chair
    with dissolve2
    window show

    us "Как кот за сметаной!"
    dns "А ты попробуй, сама потому потом за уши не оттянешь."

    show us smile pioneer close with dissolve

    us "Алиса кстати говорила, что ты с нами купаться пойдёшь."
    dns "Да, пойду. А где она сама кстати?"
    us "Она булками, которые вы вчера стащили, наелась."
    dns "Ну ты по тише про это."
    us "Ну так ты на пляж идёшь?"
    dns "Иду, я же уже ответил."
    us "Ну тогда как доешь, сразу иди на пляж."
    dns "Договорились."
    "К этому моменту я уже доел, и оставив Ульяну одну, пошёл сдавать посуду."
    "Затем подошёл к Ольге Дмитриевне, следящей за порядком в столовой."

    show mt normal pioneer with dissolve

    dns "Ольга Дмитриевна, я закончил с обходным."

    show mt surprise pioneer with dissolve

    mt "Так быстро? {w}Я думала до обеда провозишься!"
    "Я отдал удивлённой вожатой бегунок."
    dns "Так получилось. {w}Кстати, у вас случаем плавок мужских нет? Я просто свои дома оставил."

    show mt normal pioneer with dissolve

    mt "У меня то есть. Но ты видишь чем я сейчас занимаюсь?"
    dns "Ну Ольга Дмитриевна, мне очень нужно!"
    mt "Ладно... Я домик не закрывала, зайди, там в шкафу на нижней полке слева лежат."
    dns "Спасибо!"
    mt "Но смотри! Если что-то пропадёт - пеняй на себя!"
    dns "Да чего мне у вас там брать."
    "Радостный, я вышел из столовой."

    window hide
    play music music_list['she_is_kind'] fadein 6
    play sound sfx_open_cabinet_2
    play ambience ambience_day_countryside_ambience fadein 3
    scene bg ext_dining_hall_near_day with dissolve2
    pause (1)
    scene bg ext_dining_hall_away_day with dissolve2
    window show

    "Так, сейчас к вожатой, потом к себе, там переоденусь и можно идти на пляж."

    window show
    scene bg ext_square_day with dissolve2
    pause (1)
    scene bg ext_houses_day with dissolve2
    pause (1)
    scene sov1 with dissolve2
    pause (1)
    scene bg ext_house_of_mt_day with dissolve2
    pause (1)
    play sound sfx_open_cabinet_2
    play ambience ambience_int_cabin_day fadein 3
    scene bg int_house_of_mt_day with dissolve2
    window show

    "Домик Ольги, как и предполагалось, оказался незапертым."
    "Оказавшись внутри, я сразу открыл шкаф и начал рыться в куче вещей на нижних полках."
    "Среди них были и футболки, и майки, даже шорты какие-то нашись, правда они были совсем детские."
    th "Судя по всему, здесь у неё хранятся забытые или потерянные вещи."
    "Наконец в куче одежды я нащупал материал, из которого обычно делают купальники."
    "Ухватившись за ткань, потянул её, и моему обозрению предстали однотонные мужские плавки чёрного цвета."
    th "Строго, спортивно, ничего лишнего. Вроде даже мой размер."
    "Раздобыв необхадимое для купания, я поспешил закрыть шкаф и покинуть жилище вожатой."

    window hide
    scene bg ext_house_of_mt_day with dissolve2
    play sound sfx_open_cabinet_2
    play ambience ambience_day_countryside_ambience fadein 3
    window show

    "Выйдя на улицу, направился в сторону своего домика, дабы переодеться."

    window hide
    scene sov1 with dissolve2
    pause (1)
    scene bg ext_houses_day with dissolve2
    pause (1)
    scene bg ext_square_day with dissolve2
    pause (1)
    scene bg ext_house_of_dv_day with dissolve2
    pause (1)
    scene domext with dissolve2
    pause (1)
    play sound sfx_open_cabinet_1
    play ambience ambience_int_cabin_day fadein 3
    scene dom with dissolve2
    window show

    "В своём домике я примерил плавки. {w}Они и вправду оказались впору."
    th "Так, с плавками разобрались."
    th "Ульяна говорила сразу идти на пляж, но есть у меня подозрение, что приду я сильно раньше них."
    th "Ладно, делать всё-равно больше нечего."
    
    window hide
    play sound sfx_open_cabinet_2
    scene domext with dissolve2
    play ambience ambience_day_countryside_ambience fadein 3
    window show

    "С этими мыслями я вышел на улицу и направился на пляж."

    window hide
    scene bg ext_house_of_dv_day with dissolve2
    pause (1)
    scene bg ext_square_day with dissolve2
    pause (1)
    scene bg ext_dining_hall_away_day with dissolve2
    pause (1)
    scene ext_storage_day2 with dissolve2
    scene black with flash_black
    window show