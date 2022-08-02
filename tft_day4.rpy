label tft_day2:

    $ backdrop = "day"
    $ new_chapter(2, u"Судьбы двух. День 4")
    $ day_time()
    $ persistent.sprite_time = "day"
    play ambience ambience_int_cabin_day fadein 4
    scene dom with dissolve2

    "Проснулся я от того что кто-то пытался меня разбудить."

    show ars_smile with dissolve

    "Это был Арсений. Он стоял прямо надо мной."
    ars "Доброе утро-о-о-о! Просыпайся!"
    "Я в полусне поднялся и поставил ноги на пол."
    "Через пару секунд туман в голове развеялся и ко мне вернулось сознание."
    ars "Смотрю ты рано вставать не привыкший."
    dns "Что правда то правда."

    hide ars_smile
    show ars_smile2 with dissolve


    ars "Ты где кстати ночью то был?"
    "Я постарался пересказать ему то, что было вчера вечером, избегая подробностей про столовую."
    dns "Да что-то есть захотелось, я же ужин проспал, ну и пошёл на улицу, думал столовая открыта. {w}Алису ещё встретил, а уже ночь была, короче голодный остался."

    hide ars_smile2
    show ars_smile4 with dissolve

    ars "Ну ты даёшь. {w}А в тумбе смотрел?"
    dns "Нет, а что там."

    play sound window_dining

    "Он открыл ящик тумбочки. {w}Внутри лежал большой пакет с едой."
    dns "Нихера себе. {w}Откуда у тебя столько?"
    ars "Повариху нашу знаешь?"
    dns "Ну допустим."
    ars "Это тётка моя."
    "Ну тогда всё понятно."
    ars "Если есть захочешь и до столовой идти лень будет - можешь взять. Я один всё это не съем."

    hide ars_smile4
    show ars_smile3 with dissolve

    ars "Ну давай короче иди умывайся, скоро линейка начнётся."
    dns "Ага."

    play sound sfx_open_cabinet_1
    hide ars_smile3 with dissolve

    "Арсений ушел, оставив меня одного."
    "Я достал из тумбы пакет с умывальными принадлежностями."
    "Внутри лежали советский зубной порошок и счётка."
    th "В моём времени его использует, наверное, только тот самый десятый стоматолог."
    "Одев ботинки я вышел на улицу."

    window hide
    play sound sfx_open_cabinet_2
    play ambience ambience_day_countryside_ambience fadein 3
    play music music_list["sweet_darkness"] fadein 4
    scene domext with dissolve2
    window show
    
    "Снаружи дул прохладный утренний ветер, было свежо, на траве блестела роса."

    window hide
    scene bg ext_house_of_dv_day with dissolve2
    pause (1)
    scene bg ext_square_day with dissolve2
    window show

    "На площади вожатая гоняла младших пионеров, чтобы те быстрее собирались на линейку."

    window hide
    scene ext_admins_day_7dl with dissolve2
    pause (1)
    scene bg ext_musclub_day with dissolve2
    pause (1)
    window show

    "В первый раз проходя мимо музыкального клуба, мне так понравилась музыка, доносящаяся изнутри, что все последующие разы проходя мимо него, я сбавлял шаг."
    "Сейчас внутри было тихо. Судя по всему Мику нет внутри."
    "За зданием кружка виднелись умывальники."

    window hide
    pause (1)
    scene bg ext_washstand_day with dissolve2
    show mi normal pioneer far at left
    show un normal pioneer far at right
    with dissolve
    window show

    "Издалека я заметил двух девочек из своего отряда - Мику и Лену."
    "Первая видимо пыталась выяснить что-то у второй."

    window hide
    show mi normal pioneer at left
    show un normal pioneer at right
    with dissolve
    window show

    "Подойдя ещё ближе стала различима тема разговора."
    mi "Лена, почему ты так редко в клуб заходишь? Ты же сама записалась! У тебя же такой красивый голос!"
    un "Мику, ты же знаешь..."
    mi "Ты говорила что стесняешься, ну и что? Там же некого стесняться! Там все свои! Я, ты, Арсений, Алиса!"
    un "Я прихожу всегда как у меня появляется свободное время."
    "Пока я проходил рядом девочки молча провожали меня взглядом, а потом снова продолжили."

    window hide
    scene bg ext_washstand2_day with dissolve2
    pause (1)
    play sound sfx_close_water_sink
    pause (1)
    play sound_loop sfx_water_sink_stream
    window show

    "Прежде чем начать чистить зубы, я включил кран и набрал воды в ладоши."

    play sound sfx_water_splash
    
    th "Ух, бодрит."
    "После сна в горле было сухо, и непобрезговав, я даже отпил немного."
    "Помочив счётку, нанёс на неё горсть порошка и принялся чистить зубы."

    window hide
    pause (2)
    window show

    "Закончив, сплюнул и снова набрал воды."
    "Тщательно прополоскав ротовую полость, я убрал умывальные принадлежности обратно в пакет, и направился в домик."

    window hide
    play sound sfx_close_water_sink
    stop sound_loop fadeout 3
    pause (1)
    scene bg ext_musclub_day with dissolve2
    pause (0.5)
    scene bg ext_square_day with dissolve2
    pause (0.5)
    scene bg ext_house_of_dv_day with dissolve2
    pause (0.5)
    scene domext with dissolve2
    pause (0.5)
    play sound sfx_open_cabinet_1
    play ambience ambience_int_cabin_day fadein 3
    scene dom with dissolve2
    window show

    "Вытащив сумку из под стола, я расстегнул молнию и положил умывальные принадлежности сверху."
    "Линейка начиналась в восемь. {w}Сейчас было без десяти."
    "Я полежал на кровати пару минут и пошёл на площадь."

    window hide
    play sound sfx_open_cabinet_2
    play ambience ambience_day_countryside_ambience fadein 3
    scene domext with dissolve2
    pause (0.5)
    scene bg ext_house_of_dv_day with dissolve2
    pause (0.5)
    scene bg ext_square_day with dissolve2
    pause (0.5)
    window show

    "Когда я пришёл, пионеры уже выстраивались в шeренги."
    "Ближе всего к памятнику стояли знакомые мне лица."
    "Славя с табличкой «{b}ПЕРВЫЙ ОТРЯД{/b}», Хихикающие Алиса с Ульяной, что-то вечно обсуждающие Электроник с Шуриком, Лена и Мику."
    "Как только я встал в строй, вожатая объявила:"

    window hide
    show mt normal pioneer with dissolve
    window show

    mt "Доброе утро ребята, сегодня линейка начнётся с плохих новостей."
    mt "Ведь вчера вечером повара испекли вкусных сдобных булок, а ночью, после отбоя, какие-то несознательные и безответственные пионеры проникли в столовую через окно."
    mt "И уже утром повара недосчитались целой дюжены булочек. {w}Из-за этого сегодня все остаются без них."
    "По рядам пронёсся огорчённый гул."

    window hide
    show mt angry pioneer with dissolve
    window show

    mt "Я не знаю кто это сделал, но хочу заставить этого человека задуматься, ведь повара тратят свои силы и лагерные продукты на то, чтобы накормить вас."
    "Произнесла Ольга, глядя на Алису с Ульяной."

    window hide
    show mt normal pioneer with dissolve
    window show

    mt "А сейчас, все желающие пойти на спорт площадку шаг вперёд."
    "Ульяна, Славя и некотрые пионеры из других отрядом шагнули из строя."
    mt "На{w=0.2}-пра-{w=0.2}во! {w}Ша{w=0.2}-гом марш!"
    mt "Остальные могут быть свободны до завтрака."

    window hide
    show mt normal pioneer:
        linear 1 xalign 1.7
    pause (1)
    hide mt
    window show

    "Ольга развернулась и пошла с остальными на площадку."
    "Мы начали расходиться, но вдруг кто-то из толпы сказал:"

    window hide
    show pi normal at left with dissolve
    window show

    pi "Сто процентов Двачевская опять."

    window hide
    show dv angry pioneer at right with dissolve
    window show

    dv "Слышь! Щас договоришься!"








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