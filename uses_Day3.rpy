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