label tft_day2:

    $ backdrop = "day"
    $ new_chapter(4, u"Судьбы двух. День 4")
    $ day_time()
    $ persistent.sprite_time = "day"
    play ambience ambience_int_cabin_day fadein 4
    scene dom with Dissolve(5)

    "Проснулся я от того что кто-то пытался меня разбудить."

    show ars_smile with dissolve

    "Это был Арсений. Он стоял прямо надо мной."
    ars "Доброе утро-о-о-о! Просыпайся!"
    "Я в полусне поднялся и поставил ноги на пол."
    "Через пару секунд туман в голове развеялся и ко мне вернулось сознание."
    ars "Смотрю ты рано вставать не привыкший."
    dns "Что правда то правда."

    hide ars_smile
    show ars_smile2
    with dissolve


    ars "Ты где ночью то был?"
    dns "Да что-то есть захотелось, я же ужин проспал, ну и пошёл на улицу, думал столовая открыта. {w}Алису ещё встретил, а уже ночь была, короче голодный остался."
    "Постарался пересказать ему я, избегая подробностей про столовую."

    hide ars_smile2
    show ars_smile4
    with dissolve

    ars "Ну ты даёшь. {w}А в тумбе смотрел?"
    dns "Нет, а что там."

    play sound window_dining

    "Он открыл ящик тумбочки. {w}Внутри лежал большой пакет с едой."
    dns "Нихера себе. {w}Откуда у тебя столько?"
    ars "Повариху нашу знаешь?"
    dns "Ну допустим."
    ars "Это тётка моя."
    th "Ну тогда всё понятно."
    ars "Короче если есть захочешь - можешь взять. Я один всё-равно это не съем."

    hide ars_smile4
    show ars_smile3
    with dissolve

    ars "Ну давай короче иди умывайся, скоро линейка начнётся."
    dns "Ага."

    play sound sfx_open_cabinet_1
    hide ars_smile3 with dissolve

    "Арсений ушел, оставив меня одного."
    "Я достал из тумбы пакет с умывальными принадлежностями."
    "Внутри лежали советский зубной порошок и счётка."
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

    "На пути к умывальникам я проходил мимо музыкального клуба."
    "Внутри было тихо. Судя по всему Мику ещё не на месте."

    window hide
    pause (1)
    scene bg ext_washstand_day with dissolve2
    show mi normal pioneer far at left
    show un normal pioneer far at right
    with dissolve
    window show

    "Издалека я заметил двух девочек из своего отряда - Мику и Лену."
    "Первая видимо пыталась выяснить что-то у второй."
    "Подойдя ещё ближе стала различима тема разговора."
    mi "Лен, почему ты так редко в клуб заходишь? Ты же сама записалась!"
    un "Мику, ты же знаешь..."
    mi "Ты говорила что стесняешься, ну и что? Там же некого стесняться! Там все свои!"
    un "Я прихожу всегда как у меня появляется свободное время."

    window hide
    show mi normal pioneer at left
    show un normal pioneer at right
    with dissolve
    pause (1)
    hide mi
    hide un
    with dissolve
    pause (1)
    window show

    "Я прошёл мимо них к умывальнкиам."
    "После этого они судя по всему решили поменять место разговора."

    window hide
    scene bg ext_washstand2_day with dissolve2
    pause (1)
    play sound_loop sfx_water_sink_stream fadein 2
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

    "Вытащив сумку из под стола, расстегнул молнию и положил умывальные принадлежности внутрь."
    "Линейка начиналась в восемь. {w}Сейчас было без десяти."
    "Я посидел на кровати пару минут и пошёл на площадь."

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
    mt "И уже утром повара недосчитались целой дюжены булочек. {w}Из-за этого сегодня мы остаёмся без них, иначе на всех не хватит."
    "По рядам пронёсся огорчённый гул."

    window hide
    show mt angry pioneer with dissolve
    window show

    mt "Я не знаю кто это сделал, но хочу заставить этого человека задуматься, ведь повара тратят свои силы и лагерные продукты на то, чтобы накормить вас."

    window hide
    show mt normal pioneer with dissolve
    window show

    mt "Так же после завтрака особо не расходимся, ведь как вы помните сегодня четвертый четверг месяца!"
    th "Что ещё за четвёртый четверг?"
    mt "А сейчас, все желающие пойти на спорт площадку шаг вперёд."
    "Ульяна, и некотрые пионеры из других отрядом шагнули из строя."
    mt "На-пра-во! {w}Ша-гом марш!"
    mt "Остальные могут быть свободны до завтрака."

    window hide
    show mt normal pioneer:
        linear 1 xalign 1.7
    pause (1)
    hide mt
    window show

    "Ольга развернулась и пошла с остальными на площадку."

    window hide
    pause (1)
    scene bg ext_houses_day with dissolve
    play sound sfx_slavya_run
    window show

    "Я уже ушёл от площади, как вдруг сзади послышались шаги."

    window hide
    show sl smile2 sport with dissolve
    window show

    "Обернувшись я увидел Славю в спортивной одежде."
    sl "Денис, доброе утро."
    dns "Доброе."
    sl "Можно тебя кое о чём попросить?"
    dns "Ну... да."
    sl "Ольга Дмитриевна попросила книгу её любиммую получить в библиотеке, а меня щас физрук просит помочь в подсобке да и зарядку не хотелось бы пропускать. {w}Ты не мог был забрать книжку и в домик вожатой положить?"
    "Мне было лень этим заниматься, но и отмазки придувымать не хотелось."
    dns "Ну давай. {w}Какое название, кто автор?"
    sl "Называется ''Двенадцать стульев'', авторы Ильф и Петров."
    th "О, я такое знаю, читал."
    dns "Понял, щас схожу."
    "Сказал я, уже собираясь уходить."
    "Как вдруг Славя дёрнула меня к себе, но переусердствовала, из-за чего мы оказались вплотную друг к другу."
    "Затем она неловко отстранилась и продолжила:"

    show sl normal sport with dissolve

    sl "Только это... не испорти её, а то Ольга Дмитриевна тебе за неё устроит."
    dns "Хорошо. {w}Могу идти?"

    show sl smile sport

    sl "Да, всё."

    show sl smile sport:
        linear 1 xalign -0.8
    pause (1)
    hide sl

    "Славя побежала по делам, а я направился в библиотеку."

    window hide
    scene bg ext_aidpost_day with dissolve2
    pause (1)
    scene bg ext_library_day with dissolve2
    pause (1)
    play sound sfx_open_cabinet_2
    stop ambience fadeout 2
    scene bg int_library_day with dissolve2
    stop music fadeout 3
    play ambience ambience_library_day fadein 3
    window show

    th "Серп и молот, серп и молот, серп и молот... {w}Везде серп и молот!"

    window hide
    camera:
        perspective True
        zpos 0
        linear 2 xpos -250 zpos -600
    pause (2)
    window show

    th "Портреты Ильича, его же бюсты."
    "Чуть правее виднелись полки с книгами, кресла. На дальнем камоде стоял барабан, на котором лежала труба."
    "А слева у окна располагался столик, с лежащими на нём игральными картами."
    "Видимо пионеры собираются за игрой именно здесь."

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

    mz "Зачем пришёл?"
    "Спросила вдруг Женя, возникшая передомной из ниоткуда."
    dns "За книгой пришёл."
    mz "Да ну. Пацаны читают книги?"
    dns "Да, прикинь."
    mz "Ну и какая книга тебе нужна?"
    dns "Двенадцать стульев. Ильф, Петров."
    mz "Ты прям как наша вожатая."
    dns "Интересная книга потому что."
    mz "Ну стой тут тогда, щас принесу."

    window hide
    hide mz with dissolve
    window show

    "Библиотекарша растворилась среди стеллажей и полок."
    "На столе лежал неразгаданный кроссворд."
    "Вопрос был такой: ''Приносит детей. Слово из четырёх букв.''"

    window hide
    show mz normal glasses pioneer with dissolve
    window show

    mz "Что ты там смотришь?"
    dns "Аист."
    mz "Что?"
    dns "Слово в кроссворде - аист."
    
    window hide
    show mz smile glasses pioneer with dissolve
    window show

    mz "И правда. {w}Спасибо тебе, а то я голову сидела ломала."
    dns "Обращайся."
    "Женя дала мне книгу а после села за свой стол и вписала недостоющее слово."

    window hide
    show mz normal glasses pioneer with dissolve
    window show
    
    mz "Так, читательский билет заводить будешь?"
    dns "Зачем он нужен?"
    mz "Не поверишь, чтобы книги читать."
    dns "Нет, не надо."
    mz "А зря. {w}Вот тут и тут распишись и можешь идти."
    dns "Я поставил подписи где требовалось, поблагодарил Женю и вышел из библиотеки."

    window hide
    stop music fadeout 3
    pause (1)
    play sound sfx_open_cabinet_2
    scene bg ext_library_day with dissolve2
    play ambience ambience_day_countryside_ambience fadein 3
    window show

    th "Теперь к вожатой, и свободен."

    play sound sfx_dinner_jingle_speaker

    "В этот момент как раз прозвучал горн, призывающий пионеров на завтрак."

    window hide
    scene bg ext_aidpost_day with dissolve2
    pause (1)
    scene bg ext_houses_day with dissolve2
    pause (1)
    scene bg ext_house_of_mt_day with dissolve2
    window show

    "Я зашёл без стука."

    window hide
    scene bg int_house_of_mt_day with dissolve2
    play sound sfx_open_cabinet_2
    window show

    "Внутри помощения было прохладно."
    "Потоком ветра из открытого окна колыхало тюль."
    "Вокруг же царил ''творческий беспорядок'': на полу были разбросаны предметы гардероба, на столе стояла немытая чашка."
    "Я взял её в руки."
    "Внутри судя по всему были остатки кофе."
    "Внезапно с улицы донеслось, как кто-то быстрым шагом приблежался к домику."
    th "Не дай бог это вожатая."
    "Я поставил чашку на место."

    window hide
    play sound sfx_open_door_strong
    show ars_smile with dissolve
    window show

    "Дверь распахнулась и внутрь зашёл Арсений."
    "Он был запыхавшийся, на лбу у него выступал пот."
    ars "Ты то мне и нужен."
    dns "Что такое?"
    "Спросил я его, кладя книгу на стол."
    ars "Потом объясню, пойдём за вожатой."
    dns "Ну пойдем."
     
    window hide
    play sound sfx_open_cabinet_1
    scene bg ext_house_of_mt_day with dissolve2
    window show

    "Не объяснив что к чему он повёл меня в сторону столовой."

    window hide
    scene bg ext_houses_day with dissolve2
    pause(1)
    scene bg ext_square_day with dissolve2
    pause (1)
    scene bg ext_dining_hall_away_day with dissolve2
    pause (0.5)
    scene bg ext_dining_hall_near_day with dissolve2
    stop ambience fadeout 2
    play sound sfx_open_cabinet_1
    play ambience ambience_dining_hall_full fadein 3
    pause (0.5)
    scene stolovaya1 with dissolve2
    window show

    "Некоторые пионеры уже завтракали."
    dns "Ну и че мы здесь забыли?"
    ars "Да погодь. Подыграй мне щас."

    window hide
    show mt normal panama pioneer with dissolve
    window show

    ars "Ольга Дмитриевна, Ольга Дмитриевна!"

    show mt surprise panama pioneer with dissolve

    mt "Что случилось?"
    ars "Маша пропала! Мы с Денисом её ищем но никак найти не можем."
    dns "Нигде её нет."
    "Подключился я."
    "От неожиданности вожатая даже растерялась."
    mt "Как пропала? Куда она могла пропасть?"
    ars "Сам не знаю, но в лагере её вроде нет."
    ars "Можно мы вдвоём сбегаем до старого лагеря, может она там?"
    mt "А как же завтрак?"
    ars "Я в домикe возьму, у меня есть. {w}Да и это важнее чем еда."
    dns "Да и не голодные мы."
    mt "Ну тогда идите скорее, только сами аккуратнее там! {w}Чтоб мне не пришлось потом и за вами кого-то отправлять."
    ars "Да что с нами будет? {w}Мы два здоровых парня."
    dns "Мы вообще спортсмены!"
    mt "Тогда идите же скорее!"

    window hide
    stop ambience fadeout 2
    play ambience ambience_day_countryside_ambience fadein 3
    scene bg ext_dining_hall_near_day with dissolve2
    pause (1)
    scene bg ext_dining_hall_away_day with dissolve2
    show ars_smile with dissolve
    window show

    dns "И че это было?"
    "Выйдя из столовой спросил я Арсения."
    ars "Щас выйдем за территорию лагеря и всё тебе расскажу."
    dns "Уж постарайся."

    window hide
    scene bg ext_dining_hall_away_day with dissolve2
    pause (1)
    scene ext_storage_day2 with dissolve2
    pause (1)
    scene ext_backdoor_day_7dl with dissolve2
    pause (1)
    scene ext_backroad_day_7dl with dissolve2
    pause (1)
    scene bg ext_path2_day with dissolve2
    window show

    dns "Ну так что? Объяснишь что к чему?"

    window hide
    show ars_smile with dissolve
    window show

    ars "Ну смотри, мы щас идём в местную деревню."
    dns "А вся эта история с похищением?"
    ars "Маша - моя подруга, она помогает мне и щас сидит заперевшись в домике пока мы её ''ищем''."
    dns "А зачем нам в эту деревню?"
    ars "Ну там можно достать всякие ништяки."
    dns "Не за бесплатно же?"
    ars "Ну естественно."
    dns "У меня ничего нет с собой. {w}Получается я просто так туда щас иду?"
    ars "Нет. {w}Сегодня четвёрртый четверг месяца, а это значит что в лагере санитарный день, и после завтрака все пионеры будут убирать территорию лагеря. {w}Не думаю что ты больше предпочёл бы это."
    dns "Ладно, убедил."

    window hide
    hide ars_smile with dissolve
    scene ext_bush_day_7dl with dissolve2
    pause (1)
    scene black with Dissolve(4)
    pause (0.5)
    scene ext_village_day_ll with dissolve2
    window show

    "Спустя сорок минут ходьбы по степи мы оказались на просёлочной улице."
    
    window hide
    scene ext_village_back_day_ll with dissolve2
    window show

    "Мы зашли в чей-то двор."

    window hide
    show ars_smile at left with dissolve
    show petr_normal at right with dissolve
    window show

    "Там был какой-то открытый сарай, а рядом сидел дед."
    ars "Дядь Петь, здравствуй!"

    window hide
    hide petr_normal at right
    show petr_smile at right
    with dissolve
    window show

    ded "О! Арсюш, привет!"
    ars "Как поживаешь?"
    ded "Да потихоньку. {w}Давно тебя не видел. Ты с другом пришёл?"
    ars "Да, Денис зовут."
    dns "Здравствуйте."
    ded "Здравствуй сынок, меня Пётр звать."
    dns "Очень приятно!"
    ded "Ну что, Арсюш, как обычно?"
    ars "Ага."
    ded "Ну пойдём в сарай."

    window hide
    scene dct_ext_hangar_sunset with dissolve2
    window show

    "Мы втроём подошли к его дверям, дед зашёл внутрь и начал копошиться в различном хламе."

    window hide
    show ars_smile at left
    show petr_smile at right
    with dissolve
    window show

    ded "Так, вот есть три штуки, самые лучшие листы сушил."
    "Он что-то передал Арсению."
    "Я порядком удивился."
    ars "Спасибо дядь Петь, вот как ты и просил."
    ded "Ох, внучок, спасибо, выручил старика."
    "Поблагодарил Арсения Пётр, забирая из его рук свёрток."
    ded "Ну что, проходите в дом чтоли, чаем угощу."
    
    window hide
    hide petr_smile with dissolve
    scene black with Dissolve(4)
    play ambience ambience_int_cabin_day fadein 3
    pause (0.5)
    scene int_house_of_nuv_day with dissolve2
    window show

    "Следующие два часа мы провели за игрой в карты."
    "Дед был матёрым картёжником. {w}Оно и не удивительно, судя по всему это единственное развлечение в деревне."
    "За десять партий он ни разу не остался в дураках, в отличии от меня и Арсения."

    window hide 
    scene grib_draw with dissolve2
    window show

    "Потом мы помогали Петру поднять банки с соленьями из погреба."
    "Их было приличное количество, видимо год был урожайный."

    window hide
    scene int_attic_7dl with dissolve2
    window show

    "Затем вместе с Арсением вытаскивали с чердака какую-то тяжёлую коробку."
    "Я даже чуть не навернулся пока спускался по лестнице."

    window hide
    stop ambience fadeout 2
    play ambience ambience_rain_in_7dl fadein 3
    scene int_house_of_nuv_day with dissolve2
    window show

    "А потом пошёл дождь. {w}Как раз в тот момент как мы собирались уходить."
    "Мы решили что он пройдёт быстро, и остались у Петра еще на пол часа."
    "Но по прошествию этого времени погода не улучшилась."

    window hide
    show ars_surprise with dissolve
    window show
    
    ars "Уборка уже давно должна была закончиться."
    dns "Мы что в этот ливень пойдём?"
    ars "Не знаю даже. {w}Вожатая нас наверное уже ищет."

    window hide
    hide ars_surprise
    show ars_surprise:
        xalign 0.5
        linear 1 xalign 0.20
    pause (0.5)
    show petr_normal at right with Dissolve(1.3)
    window show

    ded "Ну раз ищет то лучше вам идти."
    ars "Тогда бежать придётся."
    dns "Ну ниче, пробежимся."
    ded "Постойте."
    "Пётр протянул руку в карман и вытащил пачку сигарет."
    ded "Мне тут соседка сигареты проиграла в карты, но я покрепче люблю, а эти бабские какие-то."
    ded "Нужны кому? А то у меня просто так валяются."
    "Мы с Арсением переглянулись."
    ars "Ну я не курю."
    dns "Да я вроде тоже..."

    window hide
    menu:
        "Взять сигареты":

            $ day4_cig =  True
            th "Хотя, думаю, я смогу найти им применение."
            dns "Ладно, давайте я возьму."

            window hide
            show petr_smile at right with dissolve
            hide petr_normal at right
            window show

            ded "Ну и отлично, чего им у меня валяться."
            "Я взял сиграеты и убрал себе в карман."
        "Не брать":

            $ day4_cig =  False
            ded "Ну раз никому не надо, то соседке верну."
    
    show petr_normal at right with dissolve
    hide petr_smile

    ars "Ну что, пошли?"
    dns "Ага."
    "Мы попрощались с Петром, вышли на крыльцо и под дождём побежали в лагерь."

    window hide
    hide ars_surprise
    hide petr_normal
    with dissolve2
    play sound sfx_open_cabinet_2
    play ambience ambience_rain_7dl fadein 3
    scene black
    show ext_village_rain_ll at running
    with dissolve2
    pause (1)
    scene black with Dissolve(3)
    show ext_warehouse_rain_day_7dl at running with Dissolve(3)
    pause (0.5)
    hide ext_warehouse_rain_day_7dl at running with dissolve2
    pause (0.5)
    show ext_square_rain_day_7dl at running with dissolve2
    pause (0.5)
    hide ext_square_rain_day_7dl at running with dissolve2
    pause (0.5)
    show ext_washstand_rain_7dl at running with dissolve2
    pause (0.5)
    hide ext_washstand_rain_7dl at running with dissolve2
    pause (0.5)
    show ext_musclub_rain_7dl at running with dissolve2
    pause (0.5)
    hide ext_musclub_rain_7dl at running with dissolve2
    pause (0.5)
    play sound sfx_open_cabinet_1
    play ambience ambience_rain_in_7dl fadein 3
    show int_musclub_rain_7dl with dissolve2
    hide ext_musclub_rain_7dl
    window show

    "Мы забежали в пустой муз-клуб."
    dns "Мику в домике чтоли?"

    window hide
    show ars_normal with dissolve
    window show

    ars "Да не, она дождь любит, ходит может где."
    dns "А что по поводу вожатой?"
    ars "Ну Маша должна была уже сама выйти."
    dns "Ну и хорошо."
    ars "Но давай зайдём на всякий случай, покажимся ей."
    dns "Как скажешь."

    window hide
    play sound sfx_open_cabinet_1
    show ars_normal:
        xalign 0.5
        linear 1 xalign 0.15
    pause (1.3)
    show ars_smile with dissolve:
        xalign 0.15
    hide ars_normal
    show mi_upset_wet_rain at right with dissolve
    window show

    "Вдруг в помещение зашла Мику."
    "Вся мокрая, и кажется, немного грустная."

    play sound oi

    "Увидев нас она ойкнула от неожиданности."
    mi "А вы что тут делаете?"
    dns "Дождь пережидаем."

    window hide
    show mi_smile_wet_rain at right
    hide mi_upset_wet_rain
    with dissolve
    window show

    mi "Понятно."
    "Она улыбнулась."
    mi "А где были?"
    ars "Машу искали, она потерялась."

    window hide
    show mi_grin_wet_rain at right with dissolve
    hide mi_smile_wet_rain
    window show

    mi "А я знаю что она в домике сидела."

    window hide
    show ars_surprise2:
        xalign 0.15
    hide ars_smile
    with dissolve
    window show

    ars "Серьёзно? {w}А зачем же мы тогда в старый лагерь пёрлись и по лесу её искали?"
    "Арсений судя по всему включил ''Режим дурочка''."

    window hide
    show mi_shocked_wet_rain at right
    hide mi_grin_wet_rain
    with dissolve
    window show

    mi "Вы в старый лагерь ходили?"
    "Мику сильно удивилась."
    ars "Ну да."
    dns "А что в этом такого?"
    mi "Там же темно! И страшно! И... {w=0.5}Призраки!"
    dns "Ну мы не встретили."

    window hide
    show mi_normal_wet_rain at right
    hide mi_shocked_wet_rain
    show ars_smile:
        xalign 0.15
    hide ars_surprise2
    with dissolve
    window show

    mi "Потому что вы были там днём, а они днём спят, а ночью просыпаются."
    dns "Спасибо, будем знать."

    window hide
    show mi_smile_wet_rain at right
    hide mi_normal_wet_rain
    with dissolve
    window show

    mi "Печенье хотите?"
    ars "Я не против."
    dns "Тоже не откажусь."
    mi "Сейчас!"

    window hide
    show mi_smile_wet_rain at right:
        linear 1 xalign -0.7
    pause (1)
    hide mi_smile_wet_rain
    show ars_smile:
        linear 1 xalign 0.5
    pause (0.5)
    window show

    dns "Что вожатой то скажем?"
    ars "Да что-нибудь придумаем."
    "Ответил Арсений."
    "Затем шопотом продолжил:"

    window hide
    show ars_smile3
    hide ars_smile
    with dissolve
    window show

    ars "Видел у Мику через рубашку соски просвечиваются?"
    dns "Не, не смотрел."
    ars "Ну глянь щас."

    window hide
    hide ars_smile3
    show ars_smile
    with dissolve
    show ars_smile:
        xalign 0.5
        linear 1 xalign 0.15
    play sound sfx_open_cabinet_1
    pause (1)
    show mi_shy_wet_rain at right with dissolve
    window show

    "Мику вернулась с печеньем."
    "На лице её было заметно смущение. {w}Видимо она всё слышала."
    mi "Это вам."
    dns "А сама не будешь?"
    mi "Ну я чуть-чуть у вас возьму."

    window hide
    stop ambience fadeout 4
    scene black with Dissolve(4)
    play ambience ambience_int_cabin_day fadein 4
    scene bg int_musclub_day with Dissolve(4)
    window show

    "Через час дождь закончился, через окна начали пробиваться солнечные лучи."

    window hide
    show mi smile pioneer at right
    show ars_smile:
        xalign 0.15
    with dissolve
    window show

    ars "Ну ладно, мы наверное пойдём."
    mi "Пока ребята, заходите ещё!"
    dns "Пока, Мику."

    window hide
    play sound sfx_open_cabinet_1
    play ambience ambience_day_countryside_ambience fadein 3
    scene bg ext_musclub_day with dissolve2
    window show

    "Выйдя из музыкального клуба мы направились к домику вожатой."

    window hide
    scene bg ext_washstand_day with dissolve2
    pause (1)
    scene bg ext_square_day with dissolve2
    pause (1)
    scene bg ext_houses_day with dissolve2
    pause (1)
    scene sov1 with dissolve2
    pause (1)
    scene bg ext_house_of_mt_day with dissolve2
    window show

    "На подходе к нему мы увидели Ольгу Дмириевну, выходящую на улицу."

    window hide
    show mt normal panama pioneer with dissolve
    window show

    mt "О, Денис, Арсений. {w}А Маша уже нашлась."
    dns "А где она была?"
    mt "В домике у себя сидела."

    window hide
    show mt normal panama pioneer:
        xalign 0.5
        linear 1 xalign 0.85
    pause (1)
    show ars_normal at left with dissolve
    window show

    ars "Значит я просто так панику развёл?"

    window hide
    show mt grin panama pioneer with dissolve:
        xalign 0.85
    window show

    mt "Получается что да."
    dns "Ну ты балда."
    mt "Ладно, проехали."
    dns "Мы пошли тогда."
    mt "Да, идите."
    
    window hide
    scene bg ext_house_of_mt_day with dissolve2
    pause (1)
    scene sov1 with dissolve2
    pause (1)
    scene bg ext_houses_day with dissolve2
    show ars_smile with dissolve
    window show

    ars "Ладно, я пойду Машу проведаю."
    dns "Ага, увидимся ещё."
    
    show ars_smile:
        linear 1.3 xalign 2.0
    pause (1.3)
    hide ars_smile

    "Арсений ушёл, а я направился дальше к домику."

    window hide
    scene bg ext_square_day with dissolve2
    pause (1)
    scene bg ext_house_of_dv_day with dissolve2
    show dv normal pioneer2 flt with dissolve
    window show

    "Вдруг мы пересеклись взглядами с Алисой, которая сидела на ступенях своего домика."
    dns "Привет."
    dv  "Здарова."
    dns "Чё как дела у тебя?"
    dv "Да не плохо. {w}Слышала вы с Сеней в деревню гоняли?"
    dns "Да, а откуда знаешь?"
    dv "Мику рассказала."
    dns "А сама где была?"
    dv "Да нигде. Дома сидела."
    dns "Нормально."
    dv "Какие планы на вечер?"
    dns "Никаких вроде. {w}А что?"
    dv "Да жарковато что-то, не хочешь на пляж сходить?."
    dns "Почему бы и нет?"
    dv "Тогда иди плавки одевай, а я тут подожду."
    dns "А тебе типо переодеваться не надо?"
    dv "Я уже в купальнике."

    window hide
    show dv grin pioneer2 flt with dissolve
    window show

    dv "Или тебе убедиться надо?"
    dns "Нет, не надо."
    dv "Тогда иди переодевайся уже, телóк."
    dns "Угу."

    window hide
    scene domext with dissolve2
    pause (1)
    play sound sfx_open_cabinet_1
    play ambience ambience_int_cabin_day fadein 3
    scene dom with dissolve2
    window show

    "Зайдя в домик я быстро скинул шорты, трусы, одел плавки и на них снова шорты."
    "Затем на всякий случай убрал всё в рюкзак и вышел на улицу."
    
    window hide
    stop ambience fadeout 2
    play sound sfx_open_cabinet_2
    scene domext with dissolve2
    play ambience ambience_day_countryside_ambience fadein 3
    pause (1)
    scene bg ext_house_of_dv_day
    show dv smile pioneer2 flt
    with dissolve2
    window show

    dv "Ну наконец-то."
    dns "Ой какие мы нетерпеливый."
    dv "Получишь щас."
    dns "Пошли уже."

    window hide
    hide dv with dissolve
    pause (1)
    scene bg ext_square_day with dissolve2
    pause (1)
    scene bg ext_dining_hall_away_day with dissolve2
    pause (1)
    scene ext_storage_day with dissolve2
    pause (1)
    play ambience ambience_lake_shore_day fadein 4
    scene bg ext_beach_day with Dissolve(3)
    show dv smile pioneer2 flt with dissolve
    window hide

    "Выйдя на берег мы начали раздеваться."

    $ persistent.sprite_time = "day"
    window hide
    show dv smile pioneershirt flt with dissolve2
    pause (1)
    show dv smile swim flt with dissolve2
    window show

    "Сначала сняли низ, потом верх."
    "У Алисы была очень красивая фигура."
    "Ровные изгибы талии, плоский живот уходящий ниже без единой складки, оголёные загорелые ключицы."

    window hide 
    show dv smile swimhair flt with dissolve2
    window show

    dv "Ну и что ты уставился?"
    "Спросила Алиса снимая заколки с волос."
    dns "Полюбоваться чтоль нельзя?"

    window hide 
    show dv grin swimhair flt with dissolve
    window show

    dv "Только с моего разрешения."
    dns "Ой да расскажешь."
    dns "Не хотела бы чтоб на тебя смотрели - не завязывала бы рубашку в узел под грудью."
    dv "Я может для себя завязываю, откуда ты знаешь?"
    dv "И вообще, пойдём уже купаться."
    "Cказала она и рванула в воду."
    
    window hide
    show dv grin swimhair flt:
        linear 1 xalign 1.8
    pause (1)
    hide dv
    scene ext_beach_water_sunset with dissolve2
    window show

    "Я ринулся за ней."

    window hide
    scene d4_dvswim_tft with dissolve2
    window show

    "Алиса прошла по мелководью с десяток шагов и развернулась, будто ожидая меня."
    dv "Дуй сюда."

    window hide
    scene ext_beach_water_sunset with dissolve2
    play sound sfx_water_splash
    pause (0.5)
    play sound sfx_water_splash
    window show

    "И стоило мне только подойти ближе, как она начала меня брызгать."

    window hide
    play sound sfx_water_splash
    pause (0.5)
    play sound sfx_water_splash
    pause (0.5)
    play sound sfx_water_splash
    window show

    "Я начал брызгать её в ответ."
    "Она отпрыгнула дальше, где уже могла нырнуть под воду."
    "Это Алиса и сделала, скрывшись тем самым у меня из виду."
    "Я прошёл вперёд, туда, где последний раз видел её."
    "Внезапно она вынырнула и напрыгнула на меня со спины."
    "И вместе мы повалились в воду."

    window hide
    scene black with Dissolve(5)
    play ambience ambience_lake_shore_evening fadein 4
    $ persistent.timeofday = "sunset"
    $ persistent.sprite_time = "sunset"
    scene bg ext_beach_sunset with Dissolve(5)
    window show

    dns "И куда после школы планируешь?"
    dv "Ну может на хирурга. {w}Уеду в Ленинград и буду там работать."
    dns "Почему именно в Ленинград?"
    dv "Ну там красиво очень, я там была в детстве, уже не помню толком ничего, но очень хочу еще раз побывать."
    dns "Я там... {w=0.4}бывал. {w}Впринципе неплохо."
    "Рассуждали мы с Алисой." 
    "Накупавшись, наплескавшись, лёжа на песке и встречая закат."
    
    window hide
    pause (0.5)
    play sound sfx_dinner_jingle_normal
    pause (4)
    window show

    "Вдруг со стороны столовой донёсся горн."
    dv "Пойдём?"
    dns "Ну пошли."

    window hide
    show dv smile swimhair flt with dissolve2
    window show

    "Мы поднялись с земли и начали одеваться."

    window hide
    show dv smile hairskirt flt with dissolve2
    pause (1)
    show dv smile hair flt with dissolve2
    window show

    dv "Ты сам то голодный?"

    window hide
    show dv smile pioneer2 flt with dissolve2
    window show

    "Спросила меня Алиса, собирая волосы заколкой."
    "Помимо чая Пётр угостил нас салатом и парой бутербродов с салом, так что есть мне не хотелось."
    dns "Да честно не особо."
    dv "Как хочешь."
    "Собрав свои вещи, мы направились обратно."

    window hide
    stop ambience fadeout 2
    play ambience ambience_forest_evening fadein 3
    hide dv with dissolve
    scene ext_warehouse_sunset_7dl with dissolve2
    pause (1)
    scene bg ext_dining_hall_away_sunset with dissolve2
    pause (1)
    show dv normal pioneer2 flt with dissolve
    window show

    dns "Ладно, ты иди сама, а я в домик пойду."
    dv "Хорошо, до встречи."    
    dns "Ещё увидимся."

    window hide
    hide dv with dissolve
    pause (1)
    scene bg ext_square_sunset with dissolve2
    pause (1)
    scene bg ext_houses_sunset with dissolve2
    pause (1)
    scene dvhousesunset with dissolve2
    pause (1)
    stop ambience fadeout 3
    scene domexteven with dissolve2
    play ambience ambience_int_cabin_evening fadein 3
    pause (1)
    play sound sfx_open_cabinet_1
    scene dom with dissolve2
    window show

    "Арсения дома не было."
    th "Наверное с этой своей Машей сидит."
    "Подумал я, переодеваясь из плавок в обычные трусы."
    "И хотя мы с Алисой на пляже больше лежали и отдыхали чем активничали, усталость была приличная."
    "Ненадеясь уснуть я закрыл глаза."

    window hide
    scene black with Dissolve(4)    
    pause (1)
    play ambience ambience_int_cabin_night fadein 4
    $ persistent.timeofday = "night"
    $ persistent.sprite_time = "night"
    scene domnight with Dissolve(3)
    window show

    "На лагерь опустилась ночь."
    "Я не знаю сколько валялся в раздумьях, но за это время успел порассуждать на многие темы."
    "Например про пионерские лагери в СССР."
    "Вспомнил причины развала союза."
    "О дружбе. {w}Почему сейчас мы не можем подойти к человеку и сказать ''Привет, давай дружить?'', как это делали в детстве."
    "О нашем с Арсением походе в деревню."
    "И конечно же о Алисе, с которой мы полтора часа валялись на песке и обсуждали всякую всячину."
    "А также ещё на огромное множество других тем."
    "Только щас я понял, что Арсения до сих пор нет."
    th "Надо бы пойти прогуляться. {w}Усну я, видимо, ещё не скоро"

    window hide
    play sound sfx_open_cabinet_1
    stop ambience fadeout 2
    play ambience ambience_forest_night fadein 4
    scene domextnight with dissolve2
    window show 
    
    "Я вышел из домика, и под стрекотание сверчков побрёл куда глаза глядят."

    window hide
    scene muznight3 with dissolve2
    pause (1)
    scene ext_washstand_night_7dl with dissolve2
    window show
    
    "Выйдя к умывальникам меня посетила идея умыться."

    window hide
    scene ext_washstand2_night with dissolve2
    play sound_loop sfx_water_sink_stream fadein 3
    window show

    "Из крана потекла вода."
    "Я набрал её в ладони и ополостнул лицо."

    window hide
    play sound sfx_water_splash
    pause (1)
    window show

    "Холодок пробежал по телу, стало свежо."

    window hide
    play sound sfx_close_water_sink
    pause (0.5)
    stop sound_loop fadeout 2
    window show

    "Выключив воду я побрёл дальше."

    window hide
    scene ext_washstand_night_7dl with dissolve2
    pause (1)
    scene muznight3 with dissolve2
    pause (1)
    scene ext_houses_night with dissolve2
    pause (1)
    scene bg ext_square_night with dissolve2
    window show

    "Выйдя на площадь я замер напротив памятника некому ''Генде''."

    camera:
        perspective True
        zpos 0
        linear 1 xpos 50 zpos -200
    
    "Где-то он уже покрылся мхом, где-то потрескался."
    "В одном месте видимо его даже подкрашивали."

    camera:
        perspective True
        linear 1 xpos 0 zpos 0

    "Ночью в лагере было тихо."
    "Эта тишина мне была даже непривычна после шумного города."
    "С площади со стороны реки виднелась небольшая лодочная станция. {w}Я направился туда."

    window hide
    stop ambience fadeout 2
    scene bg ext_boathouse_night with dissolve2
    play ambience ambience_lake_shore_night fadein 3
    window show

    "Она представляла из себя несколько деревянных плотов, с привязанными к ним лодками, и дебаркадер - дом, построенный на воде."

    play music vzveiteskostrami fadein 5 volume 0.3

    "Неожиданно для меня среди ночного гула и шума воды послышалась тихая музыка."
    "Я решил пойти в сторону источника звука, исходившего с дебаркадера."

    window hide
    scene ext_pier_night with dissolve2
    window show

    "Оказавшись на нём, чётко стало ясно что кто-то наигрывает мелодию на гитаре."
    th "Кто бы это мог быть?"
    "Я зашёл за угол. Как раз туда, откуда шёл звук."

    window hide
    scene ext_boathouse_alt_night_7dl with dissolve2
    show dv normal pioneer flt with dissolve2
    window show

    "Это была Алиса, сидевшая свесив ноги над водой и игравшая на гитаре."
    
    stop music fadeout 2
    
    "Когда я подошёл она перестала играть."
    dns "Ты чего тут в одиночестве сидишь?"
    dv "А ты чего не спишь?"
    dns "Не спится."
    dv "Ну вот и мне тоже."
    "Я немного замялся."
    dns "А...{w} с тобой можно?"
    pause (0.8)
    dv "Можно..."
    "С небольшой паузой ответила она."

    window hide
    show dv smile5 pioneer flt with dissolve
    window hide

    dv "Послушать не хочешь?"
    dns "Хочу конечно."

    window hide
    hide dv with dissolve
    scene d4_dv_stage_1_ll with Dissolve(3)
    window hide

    "Я подошёл к ней и сел рядом."
    dv "Ну слушай."

    window hide
    pause (0.5)
    play music vzveiteskostrami fadein 1.5
    pause (15)
    window show

    "{b}Нажми чтобы музыка закончилась"

    window hide
    stop music fadeout 5
    pause (3.5)
    window show

    dv "Ну как тебе?"
    dns "Ты отлично играешь. {w}Сама научилась или занималась где?"
    dv "Я самоучка."
    dns "Круто. {w}А можно я тоже сыграю?"
    dv "Давай."
    "Она протянула мне гитару."

    window hide
    scene d4_dv_stage_2_ll with dissolve2
    window hide

    dns "Начинаю?"
    dv "Ага."

    window hide
    pause (0.5)
    play music grob_oborona fadein 1.5
    pause (15)
    window show

    "{b}Нажми чтобы музыка закончилась"

    window hide
    stop music fadeout 5
    pause (3.5)
    window show

    dv "Ну неплохо. Мог лучше конечно."
    dns "Ага, как же."
    
    window hide
    scene d4_dv_stage_1_ll with dissolve2
    window hide

    "Она забрала у меня гитару."
    dv "У меня тут песня есть, хочешь сыграю?"
    dns "Что, прям песня?"
    dv "Прям песня."
    dns "Ну давай."

    window hide
    play music d4_dv_song fadein 3
    pause (3)
    scene d4_dv_stage_5_ll with dspr
    window show

    "Алиса начала играть и запела."

    window hide
    pause (15)
    window show

    "{b}Нажми чтобы музыка закончилась."

    window hide
    stop music fadeout 5
    pause (3.5)
    scene d4_dv_stage_1_ll with dissolve
    pause (0.5)
    window show 

    "Хотя голос у неё и грубоват, как для девушки, но получилалось у неё великолепно."
    dns "Алис, это очень круто, правда."
    "Её вокальные данные произвели на меня впечатление."
    dv "Ой да не льсти."
    dns "А можно я тоже сыграю кое-что?"
    dv "Ну на, удивляй."
    "Она отдала мне гитару."
    
    window hide
    scene d4_dv_stage_4_ll with dissolve
    window show

    "Я взял её поудобнее."
    dns "Начинать?"
    dv "Давай уже."

    window hide
    play music sos_pro_kota fadein 2
    pause (15)
    window show

    "{b}Нажмите чтобы музыка закончилась."

    window hide
    stop music fadeout 5
    pause (3.5)
    window show 

    dv "Классная песня, смысловая."
    "Я вернул гитару Алисе."
    dns "Мне тоже нравится."

    window hide
    scene ext_boathouse_alt_night_7dl with dissolve2
    show dv smile pioneer flt with dissolve
    window show

    dv "А почему ты в муз-клуб не записался? Играть умеешь, поёшь даже."
    dns "Не знаю, может запишусь как-нибудь."
    dv "Давай."
    if day4_cig:
        "Я вспомнил о пачке сигарет, лежащей в кармане."
        dns "Кстати, Алис, у тебя сигареты ещё есть?"

        window hide
        show dv surprise pioneer with dissolve
        window show

        dv "Ты же говорил что не куришь..."
        dns "Да не в этом дело. {w}Есть или нет?"
        dv "Нет, закончились."
        "Я вытащил из кармана пачку и протянул ей."
        dns "Вот, держи."
        
        window hide 
        show dv pioneer grin flt with dissolve
        window hide

        dv "Спасибо! {w}Я уж думала у физрука пойти стрелять."
        "Она взяла её и убрала в карман."
        dns "Да не за что."

        window hide
        show dv smile pioneer flt with dissolve
        window show

    dv "Ладно, пойдём наверное, а то небось эта мымра белобрысая опять весь лагерей проверяет."
    dns "Ну после вчерашнего то да."
    dv "Вот интересно что ей вожатая сделала за то что не уследила за столовой."
    dns "Не знаю. {w}Пошли?"
    dv "Да, погнали."

    window hide
    scene ext_pier_night with dissolve2
    pause (1)
    stop ambience fadeout 1.5
    play ambience ambience_forest_night fadein 4
    scene bg ext_boathouse_night with dissolve2
    pause (1)
    scene bg ext_square_night with dissolve2
    pause (1)
    scene ext_houses_night with dissolve2
    pause (1)
    scene bg ext_house_of_dv_night with dissolve2
    window show


    "Я проводил Алису до домика."
    "Она даже хлопнула меня по плечу на прощание."
    
    window hide
    scene domextnight with dissolve2
    play sound sfx_open_cabinet_1
    stop ambience fadeout 1.5
    play ambience ambience_int_cabin_night fadein 2
    scene domnight with dissolve2
    window show

    "Арсений к этому моменту, видимо, уже вернулся домой, и валялся на своей кровати."
    "Я тоже разделся, и лёг в свою постель."
    "Меня сразу потянуло в сон."
    th "Оказывается достаточно всего лишь прогуляться на свежем воздухе чтобы нормально уснуть."
    
    window hide
    stop ambience fadeout 5
    scene black with Dissolve(5)
    pause (1)
    jump tft_day3


        

    
