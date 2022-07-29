    #ЭТО ТЕ ОТРЫВКИ ПППРЕДЫДУЩЕЙ ВЕРСИИ КОТОРЫЕ 100% НАДО ЮЗАТЬ
    
    
    "Я открыл дверь и зашёл внутрь."
    "Алиса зашла следом."
    
    window hide
    scene int_warehouse_day2 with dissolve2
    window show 

    "Внутри оказалось много стеллажей с одеждой."
    "Посреди комнаты стояла гладильная доска, а в углу швейная машинка."
    th "Довольно цивильно."

    show dv smile pioneer2 with dissolve

    dv "Ты размер то свой знаешь?"
    th "Благодаря консультантке из магазина одежды - знаю."
    dns "Да, конечно."
    dns "А что мне конкретно нужно?"

    hide dv smile pioneer2 with dissolve
    show dv surprise pioneer2 with dissolve

    dv "Рубашка, шорты... {w}ремень и галстук наверное..."
    dns "Спасибо."

    window hide
    hide dv surprise pioneer2 with dissolve
    show dv normal pioneer2 with dissolve
    play sound storagenoise
    pause (3)
    window show

    "Искать долго не пришлось."
    dns "Вроде всё."
    dv "Угу."

    window hide
    play sound saray
    scene ext_storage_day with dissolve2
    play ambience ambience_day_countryside_ambience fadein 3
    play sound sfx_keys_rattle
    window show

    "Я вернул Алисе ключи."

    show dv smile pioneer2 with dissolve

    dv "Ладно, я пошла."

    th "Ладно, как говорил один мой знакомый: «Если тебя уже насилуют, то тебе остается только стонать.»."

    "Оторвавшись от зеркала, я начал разбирать свою сумку."
    th "Смысла перекладывать вещи в шкаф нет, их у меня не так уж и много."
    th "Только вот бутылку надо на дно засунуть. {w}Не знаю зачем... {w}На всякий случай."
    
    play sound jimbeam
    
    "Переложив бутылку в самый низ и прикрыв её одеждой я довольно отряхнул руки."
    th "Отлично, чем бы теперь заняться?"
    
    window hide
    play sound sfx_open_cabinet_1
    scene domext with dissolve2
    play ambience ambience_day_countryside_ambience
    pause (1.5)
    play sound sfx_dinner_jingle_normal
    window show
    
    th "Интересно тут конечно."
    th "Хотя кому не было бы интересно в другой реальности или осознанном сне, где можно почувствовать и потрогать окружение."
    
    show mz normal glasses pioneer far with dissolve
    
    "Лавочки перед входом были заняты какой-то пионеркой в очках."
    "Выглядела она не добро, поэтому я не решил садиться рядом. Вместо этого отправился на площадь, где тоже можно было посидеть."

    "По пути назад моё внимание привлекло окно одного из домиков."
    "Оно было занавешено флагом, с изображённым на нём весёлым роджером."
    th "Прикольно."

    $ persistent.sprite_time = "night"
    dns "И чем ты собралась её открывать?"
    "Она отошла от двери на шаг и продемонстрировала мне отмычку, торчавшую из замка."
    dv "Вот."
    "Я вытащил её и осмотрел. {w}Сделана она была из заколки."
    dns "Мда, с таким инструментом мы тут до утра провозимся."
    
    show dv angry pioneer with dissolve
    
    dv "У тебя есть другие идеи?"
    dns "Есть. {w}Я с собой булочки привёз, можем ко мне пойти, я тебя угощу."
    
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
    show sl normal pioneer with dissolv
    sl "А тебе зачем?"
    dns "Угадай."
    show sl smile2 pioneer with dissolv
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

    play sound sfx_bed_squeak

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
    "Сил продолжать думать больше не осталось, поэтому я медленно начал погружаться в сон."
