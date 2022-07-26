label estr_TFOT3:
    $ backdrop = "day"
    $ new_chapter(3, u"Судьбы двух. День 3")
    $ day_time()
    $ persistent.sprite_time = "day"
    
    window show
    "Я проснулся от того, что кто-то меня трёс."
    scene dom with dissolve2
    "Я открыл глаза, и недоумевающе посмотрел на Дениса."
    show dns_normal2 with dissolve
    dns "Доброе утро."
    "Я перевёл своё положение на кровати из лежачего в сидячие."
    vld "Доброе..."
    "Наудивление мне опять ничего не снилось."
    window hide
    pause (1)
    window show
    "Всё вокруг казалось бесцветным."
    scene black with dissolve2
    scene dom with dissolve2
    "Я закрыл лицо руками, протёр глаза и снова посмотрел вокруг."
    "Мир принял краски."
    "В голову решительно ничего не приходило."
    vld "А сколько время?"
    dns "Пол восьмого."
    "В ответ я лишь промычал."
    dns "Собирайся, нам щас на линейку, а потом ещё в старый лагерь за монтировкой."
    th "А, надо же Денису рассказать."
    vld "Не надо уже... Я вчера сходил."
    hide dns_normal2
    show dns_smile3 with dissolve
    dns "Серьезно?"
    vld "Ага..."
    dns "А где она?"
    vld "Вон стоит..."
    "Я показал на фомку, стоящую в углу."
    dns "Красава! {w} Освободил нас от половины работы."
    vld "Спасибо конечно, но это не всё..."
    dns "А что ещё?"
    "Я поднялся с кровати, открыл шкаф, нащупал среди простыней металическую раму ТТ и вытащил его наружу."
    "Не показывая его, я повернулся к Денису."
    vld "А ещё, я нашёл вот что."
    "Я продемонстрировал пистолет Денису."
    hide dns_smile3
    show dns_surprise2 with dissolve
    dns "Ох*еть."
    dns "Ты где его достал?"
    "Я заулыбался."
    vld "В бомбоубежище нашёл, как и фомку."
    hide dns_surprise2
    show dns_smile2 with dissolve
    dns "Ну ты даёшь!"
    vld "Ага."
    dns "Ну... Это решает целый ряд проблем."
    vld "Например?"
    dns "Ну... есть чем прикончить эту мразь."
    "Его ответу я не удивился."
    "Что нам ещё делать с Семёном, как не убить его?"
    vld "Можно тогда я его убью?"
    dns "Без проблем."
    vld "Ура."
    dns "Ладно, спрячь его пока куда-нибудь, и пойдем на линейку."
    vld "Угу."
    "Я спрятал пистолет в шкаф."
    vld "Пойдём."
    dns "Пошли."
    scene domext with dissolve2
    play sound sfx_open_cabinet_2
    stop ambience
    play sound_loop ambience_camp_entrance_day
    "Мы вышли на улицу."
    play music music_list["everyday_theme"] fadein 5
    "Снаружи дул легкий ветерок, разносящий по лагерю приятный запах из столовой."
    show dns_smile4 with dissolve
    dns "Вкусно пахнет."
    vld "Ага, интересно что там сегодня."
    window hide
    hide dns_smile4 with dissolve
    pause (2)
    window show
    "Мы направились на площадь."
    scene bg ext_house_of_dv_day with dissolve2
    "Проходя мимо домика Алисы, Денис вдруг спросил меня:"
    show dns_smile2 with dissolve
    dns "Как у вас с Мику то?"
    vld "Как-как, всё отлично, мы уже друзья."
    vld "Я к ней вот записался, сегодня собираюсь зайти."
    "Больше мне рассказывать было нечего, поэтому я задал ему встречный вопрос."
    vld "А у вас с Алисой как?"
    dns "У нас тоже всё хорошо. Вчера весь день вместе провели. В футбол играли, купались... Она меня яблоком угостила."
    dns "Я ещё заметил кое-что... Когда на пляже сидели - я на воду смотрел, думал она тоже... А потом повернулся - а она на меня смотрит... загадочно ещё так. А как увидела что я её взгляд уловил, сразу отвернулась и покраснела."
    th "Ну тут всё очевидно."
    vld "Радуйся, братан, понравился ты ей походу."
    hide dns_smile2
    show dns_smile3 with dissolve
    dns "Хах, очень на это надеюсь."
    window hide
    pause (1)
    scene bg ext_square_day with dissolve2
    pause (1)
    window show
    "Мы вышли к площади."
    "Там уже выстраивались пионеры."
    "Наш отряд был в сборе."
    "Денис встал к Алисе, а я к Мику."
    show mi smile pioneer with dissolve
    vld "Привет Мику!"
    mi "Ой, привет Владик!"
    vld "Рад тебя видеть."
    show mi grin pioneer with dissolve
    mi "И я тебя..."
    hide mi grin pioneer with dissolve
    window hide
    pause (1)
    window show
    "Все пионеры выстроились в аккуратные линейки."
    "Перед всеми отрядами уже стояли вожатые, но только не перед нашим."
    "Ольги Дмитриевны почему-то нигде не было."
    window hide
    pause (1)
    window show
    "Через несколько минут она наконец пришла."
    scene d2_wertuska_wse with dissolve2
    th "Ээээ, не хорошо опаздывать, Ольга Дмитриевна."
    "Она быстро встала перед нашим отрядом и начала рассказывать о планах на день."
    "Я естественно её не слушал."
    "В голове было только одно - моя Мику."
    "Хотелось провести с ней весь сегодняшний день."
    window hide
    pause (1)
    window show
    play sound sfx_dinner_jingle_normal
    "Под конец линейки как по заказу прозвучал горн, призывающий всех в столовую."
    "Линейка закончилась, и все направились на завтрак."
    window hide
    scene bg ext_dining_hall_away_day with dissolve2
    stop music fadeout 3
    scene bg ext_dining_hall_near_day with dissolve2
    play ambience ambience_dining_hall_full fadein 3
    scene bg int_dining_hall_people_day with dissolve2
    "Мы зашли в столовую, и мне вдруг захотелось поухаживать за Мику."
    show mi smile pioneer with dissolve
    vld "Мику, садись за стол, я тебе возьму еду."
    show mi shy pioneer with dissolve
    "Мику на секунду засмушалась, но потом вдруг улыбнулась."
    show mi smile pioneer with dissolve
    mi "Хорошо."
    hide mi smile pioneer with dissolve
    "Я отстоял небольшую очередь и подошёл к выдаче."
    show shadow2 with dissolve
    pvr "Здравствуй, пионер."
    vld "Здравствуйте, можно 2 порции? Пионерке отнесу."
    pvr "Ещё один пионерке несёт... Что же вас ухажёров развелось так много? Ты уже третий кто за последнии три дня берет порцию девушки."
    vld "Просто пионерок много красивых вокруг, вот и ухаживаем."
    pvr "Хах, ну ладно. {w} Меня Клим звать."
    "Сказал он и протянул мне руку."
    vld "Влад, будем знакомы."
    window hide
    pause (1)
    window show
    "Он передал мне 2 подноса с едой."
    vld "Спасибо."
    klm "Удачи."
    hide shadow2 with dissolve
    "Я направился к столику, за которым уже сидела и ждала меня Мику."
    "Подходя к нему, меня вдруг окликнули."
    dv "Влад!"
    "Я повернулся в сторону голоса."
    scene dvpodnos with dissolve
    "Им оказалась Алиса."
    "Рубашка на ней была повязана её любимым способом."
    "В руках она тоже держала еду."
    dv "Привет Влад, а зачем тебе два подноса?"
    vld "Привет, Алис, да вот..."
    "Я замялся и кивнул в сторону Мику."
    "Алиса посмотрела на неё, затем на меня, и вдруг широко заулыбалась."
    dv "Ну удачи."
    vld "Спасибо."
    scene bg int_dining_hall_people_day with dissolve
    "Она подмигнула мне и скрылась из виду."
    "Я таки дошёл до столика, который заняла нам Мику."
    "Поставил подносы и сел на стул."
    show mi smile pioneer with dissolve
    mi "Спасибо!"
    vld "Да не за что.{w} Приятного аппетита."
    mi "И тебе!"
    hide mi smile pioneer with dissolve
    "Я принялся за еду."
    window hide
    pause (1)
    window show
    "Мику рассказывала о том, как училась играть на разных инструментах, о том что она поёт, и о многом другом."
    "Я особо не слушал, а лишь любовался её прекрасным личиком."
    "Затем Мику попросила меня тоже рассказать что-то."
    "Я рассказал ей о том, что рисую."
    "На что она ответила мне, что ей было бы интересно взглнуть на мои рисунки."
    "Но к сожалению ничего такого я с собой не брал, когда ехал в автобусе."
    window hide
    pause (1)
    window show
    "Умяв тарелку каши, я принялся за компот."
    "На удивление всё, что я ел в лагере за эти три дня, было вкусным и сытным."
    "Может и правда ''Раньше было лучше?''"
    "Мои раздумья прервало девичие хихиканье."
    "Скорее даже смешок."
    "Я повернулся в сторону звука."
    scene dvuneat with dissolve
    "В паре столиков от нас сидели Лена, Денис и Алиса."
    th "Странно что Лена с Алисой сидят вместе за одним столиком, а тем более странно, что Алиса подпустила её к Денису."
    "А он, по всей видимости что-то им рассказывал."
    "Обе девочки улыбались."
    th "Кто-кто, а Денис говорить умеет."
    scene bg int_dining_hall_people_day with dissolve
    "Я повернулся назад к Мику."
    show mi grin pioneer with dissolve
    "К этому моменту она уже доела, и кажется смотрела на меня."
    "Наши взгляды пересеклись."
    "Её большие голубые глаза..."
    "Я был готов любоваться ими вечно."
    window hide
    pause (1)
    window show
    show mi smile pioneer with dissolve
    mi "Пойдем?"
    vld "Куда?"
    show mi sad pioneer with dissolve
    mi "Не знаю..."
    vld "Может к тебе?"
    show mi surprise pioneer with dissolve
    mi "Там же Лена..."
    vld "Да не в домик... я про муз-клуб!"
    show mi laugh pioneer with dissolve
    mi "Ааааа, а я подумала что ты в домик ко мне хочешь."
    vld "Хаха."
    show mi smile pioneer with dissolve
    mi "Ну пошли."
    vld "Пойдем."
    window hide
    pause (1)
    scene bg ext_dining_hall_near_day with dissolve2
    scene bg ext_dining_hall_away_day with dissolve2
    scene bg ext_square_day with dissolve2
    scene bg ext_musclub_day with dissolve2
    scene veranda_muz with dissolve2
    scene bg int_musclub_day with dissolve2
    play sound sfx_open_cabinet_2
    stop ambience
    play sound_loop ambience_music_club_day fadein 2
    window show
    "Мы зашли в муз-клуб."
    show mi smile pioneer with dissolve
    mi "Давай я тебе на фортепиано сыграю?"
    vld "Я был бы рад."
    "Мику быстро села за фортепиано, и начала листать ноты."
    window hide
    pause (1)
    window show
    "Выбрав мелодию, она заиграла."
    scene mikufort with dissolve
    play music music_list["memories_piano_outdoors"] fadein 2
    window hide
    pause (5)
    window show
    "Музыка была упоительно приятна."
    "Я сидел и наслаждался её игрой."
    window hide
    pause (12)
    window show
    stop music fadeout 3
    scene bg int_musclub_day with dissolve
    "Мику закончила, и я стоя поаплодирвоал ей."
    show mi shy pioneer with dissolve
    "Она засмущалась."
    mi "Ну не стоит..."
    vld "Нет, что ты! {w} Ты прекрасно играешь."
    mi "Спасибо..."
    show mi smile pioneer with dissolve
    mi "Я ещё на флейте умею."
    vld "Я не сомневаюсь, можно послушать?"
    mi "Конечно!"
    "Мику взяла музыкальный инструмент и начала играть."
    hide mi smile pioneer with dissolve
    play music music_list["miku_song_flute"] fadein 2
    window hide
    pause (12)
    window show
    stop music fadeout 5
    th "Красивая мелодия."
    vld "Мику, это было великолепно."
    show mi grin pioneer with dissolve
    mi "Мне приятно, спасибо."
    hide mi grin pioneer with dissolve
    window hide
    pause (2)
    window show
    "Так мы сидели порядка пары часов."
    window hide
    pause (2)
    window show
    show mi smile pioneer with dissolve
    "Тут в муз-клуб вдруг зашёл Денис."
    play sound sfx_open_cabinet_2
    hide mi smile
    show mi smile pioneer at right with dissolve
    show dns_normal at left with dissolve
    "Увидев Мику он улыбнулся."
    hide dns_normal
    show dns_smile at left with dissolve
    dns "Привет, Мику."
    show mi smile pioneer with dissolve
    mi "Привет, Денис."
    "Он повернулся ко мне."
    dns "Влад, ты не забыл?"
    th "И правда забыл."
    vld "Точно! А что, уже пол первого?"
    dns "Да."
    "Я обратился к Мику."
    vld "Мику, прости, мне идти надо. Дела."
    mi "Да, конечно, иди, я тебя не держу."
    hide dns_smile
    play sound sfx_open_cabinet_2
    stop ambience fadeout 2
    play sound_loop ambience_camp_entrance_day fadein 2
    scene veranda_muz with dissolve2
    "Вдвоем мы вышли из кружка."
    vld "Напомни план."
    show dns_normal2 with dissolve
    dns "Ты идешь к воротам, встречаешь его, ведешь примерно к нашему домику."
    vld "А потом?"
    dns "Потом я сзади подойду и ударю его монтировкой по голове."
    vld "Отлично, потом в старый лагерь его дотащим?"
    dns "Думаю да. До вечера подержим, а там решим что с ним делать."
    vld "Хорошо, пойдем тогда за фомкой."
    scene bg ext_clubs_day with dissolve2
    scene domext with dissolve2
    play sound sfx_open_cabinet_2
    stop ambience fadeout 2
    play sound ambience_int_cabin_day fadein 2
    scene dom with dissolve2
    show dns_normal with dissolve
    "Мы зашли в наш домик."
    dns "Щас перекушу немного и пойдем."
    "Денис взял булку со стола, сел на кровать и принялся есть."
    "Я взял монтировку, стоящую в углу и положил её на стол."
    "Затем тоже присел."
    window hide
    pause (3)
    window show
    "Денис доел булку."
    vld "Погнали."
    "Денис взял мантировку и мы вышли на улицу."
    stop ambience fadeout 2
    play sound sfx_open_cabinet_2
    play sound_loop ambience_camp_entrance_day fadein 2
    scene domext with dissolve2
    show dns_normal
    dns "Я тут где-нибудь спрячусь."
    vld "Хорошо, я к воротам."
    dns "Давай."
    hide dns_normal with dissolve
    "Денис ушёл, а я направился к главным воротам."
    scene bg ext_clubs_day with dissolve
    scene vorota with dissolve2
    "Подойдя к ним, я сел на ступеньки обители кибернетиков, и принялся ждать."
    window hide
    pause (5)
    window show
    "Вскоре за воротами послышалось какое-то движение."
    "Я поднялся со ступенек и подошёл к воротам."
    "Мысленно натянув на себя маску пионера, я выдохнул и выглянул из-за ворот."
    scene bg ext_bus with dissolve2
    show art with dissolve
    "Передо мной пердстала картина:."
    "Испкуганный Семён на фоне икаруса."
    "Увидев меня, он немного успокоился."
    "Я вышел и поприветствовал его."
    vld "Привет, ты наверное новенький?"
    "Он стоял молча пару секунд, а затем ответил."
    me "П-Привет... Да, новенький."
    vld "Добро пожаловать. Меня Влад зовут."
    "Я протянул ему руку."
    me "С-Семён."
    "Мы пожали руки."
    vld "Пойдем, я тебя к вожатой отведу, она тебе все расскажет."
    me "Ну... Пойдем..."
    scene vorota with dissolve2
    scene bg ext_clubs_day with dissolve2
    "Я медленно вёл Семёна к месту, где его должен был встретить Денис."
    scene domext with dissolve2
    "Я не смотрел по сторонам, хотя было интересно, откуда выйдет Денис."
    play sound sfx_body_bump
    "Тут сзади послышался замах, затем удар."
    play sound sfx_bodyfall_1
    "Что-то свалилось на землю."
    "Я обернулся."
    show dns_normal with dissolve
    "Передо мной стоял Денис с монтировкой в руках, а на земле лежал Семён без сознания."
    vld "Молодец, а теперь потащили его."
    "Денис бросил монтировку в кусты."
    dns "Ты за руки я за ноги."
    "Мы взяли тело Семёна и побрели в старый лагерь."
    play sound_loop ambience_forest_day
    scene bg ext_path_day with dissolve2
    scene bg ext_path2_day with dissolve2
    stop ambience
    play sound_loop ambience_old_camp_outside
    scene ext_old_house_day with dissolve2
    stop ambience
    play sound_loop ambience_int_cabin_day fadein 2
    scene int_old_house_day with dissolve2
    "Мы затащили его в старый лагерь."
    show dns_normal2 with dissolve
    dns "Куда его денем?"
    vld "Давай в ту комнату."
    "Я указал на соседнюю дверь."
    dns "Окей."
    scene ss_datroom_day with dissolve2
    play sound sfx_bodyfall_1 
    "Мы бросили тело на пол."
    vld "Есть чем связать его?"
    dns "Об этом я не подумал."
    vld "Пойду поищу."
    scene int_old_house_day with dissolve2
    "Я вышел в коридор и начал его осматривать."
    "Над потолком я заметил длинный провод."
    th "Возможно подойдет."
    play sound sfx_bodyfall_1
    "Я прыгнул оттолкнувшись от стены, и рукой сорвал провод с потолка."
    scene ss_datroom_day with dissolve2
    show dns_normal2 with dissolve
    "Вернулся в комнату к Денису и продемонстрировал ему добытый кусок провода."
    hide dns_normal2
    show dns_smile2 with dissolve
    dns "Оооо, молодец."
    hide dns_smile2
    show dns_normal with dissolve
    "Он взял его, и связал руки и ноги Семёну."
    window hide
    pause (3)
    window show
    "Закончив, он встал, и отряхнулся."
    vld "Готово?"
    dns "Да, можно назад идти."
    scene int_old_house_day with dissolve2
    window hide
    pause (1)
    window show
    scene ext_old_house_day with dissolve2
    window hide
    pause (1)
    window show
    "Мы вышли из старого здания и направились обратно в лагерь."
    window hide
    pause (1)
    scene bg ext_path2_day with dissolve2
    pause (1)
    scene bg ext_path_day with dissolve2
    pause (1)
    scene domext with dissovle2
    window show
    "Через какое-то время мы наконец вернулись в лагерь."
    "Было решено пойти посмотреть что происходит на площади."
    window hide
    pause (1)
    scene bg ext_house_of_dv_day with dissolve2
    pause (1)
    scene bg ext_square_day with dissolve2
    window show
    "По ней уже разгуливали пионеры, только пришедшшие с обеда."
    "Не знаю насчёт Дениса, но мне есть не хотелось."
    "Хотя у меня был только завтрак."
    "По итогу, не найдя ничего интересного, мы направились в домик."
    window hide
    scene bg ext_house_of_dv_day with dissolve2
    pause (1)
    scene domext with dissolve2
    pause (1)
    stop ambience
    play sound sfx_open_cabinet_2
    play sound_loop ambience_int_cabin_day fadein 2
    scene dom
    window show
    "Зайдя в него, мы распластались на своих кроватях."
jump estr_TFOT4