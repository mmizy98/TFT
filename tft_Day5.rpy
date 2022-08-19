label tft_day3:

    $ backdrop = "day"
    $ new_chapter(5, u"Судьбы двух. День 5")
    $ day_time()
    $ persistent.sprite_time = "day"
    play ambience ambience_int_cabin_day fadein 4
    scene dom with Dissolve(5)

    "ап"