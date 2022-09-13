init 2:
#ЭФФЕКТЫ
#КАРТИНКИ СНЕГА И ЭФФЕКТ
    image Snf snf1 = getFile("sprites/misc/SnowLarge.png")
    image Snf snf2 = getFile("sprites/misc/SnowNormal.png")
    image Snf snf3 = getFile("sprites/misc/SnowLittle.png")
    image SnowL:
        truecenter
        xzoom 1.4 yzoom 1.4
        contains:
            SnowBlossom("Snf snf1", 30, 50, (50,150), (250,400), 10)
        contains:
            SnowBlossom("Snf snf2", 120, 50, (50,150), (250,400), 10)
        contains:
            SnowBlossom("Snf snf3", 150, 50, (50,150), (250,400), 10)

#КАРТИНКИ ПЫЛИ И ЭФФЕКТ
    image Dst dst1 = getFile("sprites/misc/Dust1.png")
    image Dst dst2 = getFile("sprites/misc/Dust2.png")
    image DustB:
        truecenter
        zoom 1.5
        contains:
            SnowBlossom("Dst dst1", 20, 50, (-30,-25), (-30,30), 25, False, True)
        contains:
            SnowBlossom("Dst dst1", 20, 50, (25,30), (-30,30), 25, False, True)
        contains:
            SnowBlossom("Dst dst2", 20, 50, (-30,-25), (-30,30), 25, False, True)
        contains:
            SnowBlossom("Dst dst2", 20, 50, (25,30), (-30,30), 25, False, True)

#СВЕТЛЯЧКИ И ЭФФЕКТ
    image Flf flf1:
        getFile("sprites/misc/FireFly1.png")
        alpha 0.0
        ease 1 alpha 1.0
    image FireFlies:
        truecenter
        contains:
            SnowBlossom("Flf flf1", 20, 80, (-30,25), (-30,30), 25, False, True)

#ИКОНКИ ДОСТИЖЕНИЙ:
    image achieve_locked = getFile("gui/achievements/achieve_locked.png")
    image achieve_menu_easter_egg = getFile("gui/achievements/achieve_menu_easter_egg.png")
    image achieve_day3_qte_win = getFile("gui/achievements/achieve_day3_qte_win.png")
    image achieve_day3_qte_almost = getFile("gui/achievements/achieve_day3_qte_almost.png")
    image achieve_day3_qte_loose = getFile("gui/achievements/achieve_day3_qte_loose.png")
    image achieve_day3_nice_punch = getFile("gui/achievements/achieve_day3_nice_punch.png")

#ЗВУКИ:
#ОКРУЖЕНИЕ:
    $ ambience_rain_7dl = getFile("sound/ambience/ambience_rain_7dl.ogg")
    $ ambience_rain_in_7dl = getFile("sound/ambience/ambience_rain_in_7dl.ogg")

#МУЗЫКА:
    $ letov_u_okna = getFile("sound/music/letov_u_okna.mp3")
    $ roxette = getFile("sound/music/roxette.mp3")
    $ your_nobility = getFile("sound/music/your_nobility.mp3")
    $ GS_Chasing_a_Rumor = getFile("sound/music/GS_Chasing_a_Rumor.mp3")
    $ greenday = getFile("sound/music/greenday.mp3")
    $ hyperborea = getFile("sound/music/hyperborea.mp3")
    $ sizor = getFile("sound/music/sizor.mp3")
    $ kostr = getFile("sound/music/vzveiteskostrami.mp3")
    $ plastinki = getFile("sound/music/plastinki.ogg")
    $ unbroken = getFile("sound/music/Unbroken.mp3")
    $ prologmusic = getFile("sound/music/prologmusic.mp3")
    $ BLAD = getFile("sound/music/BLAD.mp3")
    $ aprilrain = getFile("sound/music/aprilrain.mp3")
    $ SP_city = getFile("sound/music/SP_city.mp3")
    $ deepcosmo = getFile("sound/music/deepcosmo.mp3")
    $ porn_diapazon = getFile("sound/music/diapazon.mp3")
    $ stressedoutminus = getFile("sound/music/stressedoutminus.mp3")
    $ Omelchuk_Roads_Ahead = getFile("sound/music/Omelchuk_Roads_Ahead.mp3")
    $ vzveiteskostrami = getFile("sound/music/vzveiteskostrami.mp3")
    $ d4_dv_song = getFile("sound/music/d4_dv_song.mp3")
    $ grob_oborona = getFile("sound/music/grob_oborona.mp3")
    $ sos_pro_kota = getFile("sound/music/sos_pro_kota.mp3")

#ПОСТОРОННИЕ ЗВУКИ:
    $ heartbeat = getFile("sound/sfx/heartbeat.mp3")
    $ avaria = getFile("sound/sfx/avaria.mp3")
    $ claps = getFile("sound/sfx/claps.mp3")
    $ oi = getFile("sound/sfx/oi1.ogg")
    $ saray = getFile("sound/sfx/saray_door1.mp3")
    $ storage = getFile("sound/sfx/storage_noise.ogg")
    $ storagenoise = getFile("sound/sfx/storage_noise.ogg")
    $ jimbeam = getFile("sound/sfx/jimbeam.mp3")
    $ window_dining = getFile("sound/sfx/window_dining.mp3")
    $ fall_bed = getFile("sound/sfx/fall_onto_bed.ogg")
    $ train_honk = getFile("sound/sfx/train_honk.mp3")
    $ clock_timeskip = getFile("sound/sfx/clock_timeskip.mp3")
    $ ambience_city = getFile("sound/sfx/ambience_city.mp3")
    $ clock_alert = getFile("sound/sfx/clock_alert.mp3")
    $ light = getFile("sound/sfx/light_on.mp3")
    $ shot = getFile("sound/sfx/shot.mp3")
    $ rattle = getFile("sound/sfx/rattle.mp3")
    $ resiever = getFile("sound/sfx/resiever.mp3")
    $ okno = getFile("sound/sfx/okno.mp3")
    $ fridge = getFile("sound/sfx/fridge.mp3")
    $ liazdoor = getFile("sound/sfx/liazdoor.mp3")
    $ coldsteps = getFile("sound/sfx/coldsteps.mp3")
    $ train = getFile("sound/sfx/train_inside.mp3")
    $ sfx_menu_selected = getFile("sound/sfx/sfx_menu_selected.mp3")
    $ sfx_menu_select = getFile("sound/sfx/sfx_menu_select.mp3")
    $ sfx_door_ding = getFile("sound/sfx/sfx_door_ding.mp3")

#ЦГ:
    image d4_dv_beach1 = getFile("cg/d4_dv_beach1.jpg")
    image aliceroof = getFile("cg/aliceroof.jpg")
    image dvfire = getFile("cg/dvfire.jpg")
    image dv_polyana2 = getFile("cg/dv_polyana2.jpg")
    image night_event = getFile("cg/night_event.jpg")
    image d3_dv_kiss_7dl = getFile("cg/d3_dv_kiss_7dl.jpg")
    image d3_dv_kiss_7dl_rev = getFile("cg/d3_dv_kiss_7dl_rev.jpg")
    image dvpodnos = getFile("cg/dvpodnos.jpg")
    image dvuneat = getFile("cg/dvuneat.jpg")
    image dveda = getFile("cg/dveda.jpg")
    image dvmushug = getFile("cg/dvmushug.jpg")
    image dvcryhug = getFile("cg/dvcryhug.jpg")
    image dvlovenight = getFile("cg/dvlovenight.jpg")
    image hittendv = getFile("cg/dv_hit.png")
    image dv_beach_sunset = getFile("cg/dv_beach_sunset.jpg")
    image dv_shore = getFile("cg/dv_kiss_st.png")
    image dvkissforest = getFile("cg/dvkissforest.jpg")
    image dvdance = getFile("cg/ss_dv_dance.jpg")
    image dvsleep = getFile("cg/dvsleep.jpg")
    image dvfallangry = getFile("cg/dvfallangry.jpg")
    image sexdv1 = getFile("cg/sexdv1.jpg")
    image sexdv2 = getFile("cg/sexdv2.jpg")
    image lovedv1 = getFile("cg/lovedv1.jpg")
    image lovedv2 = getFile("cg/lovedv2.jpg")
    image dvnight = getFile("cg/dvnight.png")
    image sondv = getFile("cg/MoV1IAs8Ufc.jpg")
    image dvhug2 = getFile("cg/XrQy7tlzzFE.jpg")
    image dvmibus = getFile("cg/d1_mi_dv_bus_7dl.jpg")
    image dv_thinking_close = getFile("cg/dv_thinking_close.jpg")
    image dv_sleep_window = getFile("cg/dv_sleep_window.jpg")
    image dv_sleep_bed = getFile("cg/dv_sleep_bed.jpg")
    image d4_dvswim_tft = getFile("cg/d4_dvswim_tft.jpg")
    image d4_dv_stage_1_ll = getFile("cg/d4_dv_stage_1_ll.jpg")
    image d4_dv_stage_2_ll = getFile("cg/d4_dv_stage_2_ll.jpg")
    image d4_dv_stage_3_ll = getFile("cg/d4_dv_stage_3_ll.jpg")
    image d4_dv_stage_4_ll = getFile("cg/d4_dv_stage_4_ll.jpg")
    image d4_dv_stage_5_ll = getFile("cg/d4_dv_stage_5_ll.jpg")
    image d4_dv_stage_6_ll = getFile("cg/d4_dv_stage_6_ll.jpg")
    image food_breakfast = getFile("cg/food_breakfast.png")
    image volleyball = getFile("cg/volleyball.png")
    image semsquore = getFile("cg/semsquore.jpg")
    image slexit = getFile("cg/d1_sl_exit.jpg")
    image mikufort = getFile("cg/mikufort.jpg")
    image d2_wertuska_wse = getFile("cg/d2_wertuska_wse.jpg")
    image mikuboat = getFile("cg/mikuboat.jpg")
    image fag_room = getFile("cg/d3_fag_room.jpg")
    image mi_guitar = getFile("cg/mi_guitar.jpg")
    image navrat2 = getFile("cg/navrat2.jpg")
    image morning_line = getFile("cg/morning_line.jpg")
    image son = getFile("cg/wtf_end_of_day.jpg")
    image mirror = getFile("cg/semyon_mirror.jpg")
    image navrat = getFile("cg/navrat.jpg")
    image sportsunset = getFile("cg/ext_playground_sunset.jpg")
    image jerry = getFile("cg/jerry.jpg")
    image mirror2 = getFile("cg/semyon_mirror2.jpg")
    image grib_draw = getFile("cg/grib_draw.jpg")

#БГ:
#ГОРОД:
    image ach_bg = getFile("gui/ach_bg.jpg")
    image int_staircase_7dl = getFile("bg/int_staircase_7dl.jpg")
    image night_bar = getFile("bg/night_bar.jpg")
    image int_prolog_nightclub = getFile("bg/int_bar_7dl.jpg")
    image ext_city_night_7dl = getFile("bg/ext_city_night_7dl.jpg")
    image ext_mv2_7dl = getFile("bg/ext_mv2_7dl.jpg")
    image cityhouse = getFile("bg/cityhouse.jpg")
    image windowsun = getFile("bg/windowsun.jpg")
    image roommorning = getFile("bg/roommorning.png")
    image roomwindowsun = getFile("bg/int_semen_room_window_day_7dl.jpg")
    image ulica2 = getFile("bg/ulica2.jpg")
    image ostanovka2 = getFile("bg/ostanovka2.jpg")
    image vavtday = getFile("bg/vavtday.jpg")
    image busepilogue = getFile("bg/busepilogue.png")
    image roomreal = getFile("bg/roomreal.jpg")
    image city1 = getFile("bg/dct_landscape_city1.jpg")
    image city2 = getFile("bg/ext_IRL_night.png")
    image ulica2 = getFile("bg/ulica2.jpg")
    image ext_winterpark_7dl = getFile("bg/ext_winterpark_7dl.jpg")
    image bath = getFile("bg/bath.png")
    image vavt = getFile("bg/vavt.jpg")
    image ulica_day = getFile("bg/ulica_day.jpg")
    image ext_bus_city = getFile("bg/ext_bus_city.jpg")
    image podzd = getFile("bg/podzd.jpg")

#ЛАГЕРЬ:
    image int_attic_7dl = getFile("bg/int_attic_7dl.jpg")
    image dct_ext_hangar_sunset = getFile("bg/dct_ext_hangar_sunset.jpg")
    image int_house_of_nuv_day = getFile("bg/int_house_of_nuv_day.jpg")
    image menu_fone = getFile("bg/menu_fone.jpg")
    image ext_music_club_verandah_day = getFile("bg/ext_music_club_verandah_day.jpg")
    image ext_admins_night_7dl = getFile("bg/ext_admins_night_7dl.jpg")
    image ext_admins_day_7dl = getFile("bg/ext_admins_day_7dl.jpg")
    image int_house_of_dv_night2 = getFile("bg/int_house_of_dv_night2.jpg")
    image int_store_7dl = getFile("bg/int_store_7dl.jpg")
    image ext_volley_court_7dl = getFile("bg/ext_volley_court_7dl.jpg")
    image ext_houses_night = getFile("bg/ext_houses_night.jpg")
    image dvhousesunset = getFile("bg/dvhousesunset.jpg")
    image cssunset = getFile("bg/cssunset.jpg")
    image domnight = getFile("bg/domnight.jpg")
    image muznight = getFile("bg/muznight.jpg")
    image dark_room = getFile("bg/dark_room.jpg")
    image ss_datroom_day = getFile("bg/ss_datroom_day.jpg")
    image ext_old_house_day = getFile("bg/ext_old_house_day.jpg")
    image int_old_house_day = getFile("bg/int_old_house_day.jpg")
    image vorota = getFile("bg/vorota.png")
    image ext_beach_water_sunset = getFile("bg/ext_beach_water_sunset.jpg")
    image oldrainy = getFile("bg/int_old_building_day_rainy.jpg")
    image forest = getFile("bg/ext_forest_day_rainy.jpg")
    image forest2 = getFile("bg/ext_forest2_day_rainy.jpg")
    image int_banya_clear = getFile("bg/int_banya_clear.jpg")
    image int_banya_smoke = getFile("bg/int_banya_smoke.jpg")
    image stolovaya1 = getFile("bg/int_stolovaya_notfull.jpg")
    image muznight2 = getFile("bg/muznight2.jpg")
    image dom = getFile("bg/san_int_house_male_day.jpg")
    image clubsevening = getFile("bg/ext_clubs_sunset.jpg")
    image domext = getFile("bg/ext_hata_nru_day.jpg")
    image domextnight = getFile("bg/ext_hata_nru_night.jpg")
    image domexteven = getFile("bg/ext_house_of_max_sunset.jpg")
    image domeven = getFile("bg/san_int_house_male_evening.png")
    image muznight3 = getFile("bg/muznight3.jpg")
    image domnight = getFile("bg/san_int_house_male_night.jpg")
    image ext_house_of_un_night = getFile("bg/ext_house_of_un_night.jpg")
    image muznightinside = getFile("bg/muznightinside.jpg")
    image ext_playground_sunset = getFile("bg/ext_playground_sunset.jpg")
    image mikunight = getFile("bg/mikunight.jpg")
    image muznightnear = getFile("bg/muzhightnear.jpg")
    image buswindow = getFile("bg/int_bus_window.png")
    image sov2 = getFile("bg/sov2.jpg")
    image sov1 = getFile("bg/sov1.jpg")
    image sov3 = getFile("bg/sov3.jpg")
    image sklad_day = getFile("bg/sklad_day.jpg")
    image muzinnight = getFile("bg/muzinnight.jpg")
    image domintnight2 = getFile("bg/domintnight2.png")
    image windowsun = getFile("bg/windowsun.jpg")
    image ext_storage_day = getFile("bg/ext_storage_day2.jpg")
    image ext_warehouse_sunset_7dl = getFile("bg/ext_warehouse_sunset_7dl.jpg")
    image ext_storage_night = getFile("bg/ext_storage_night2.jpg")
    image ext_storage_day2 = getFile("bg/ext_storage_day.png")
    image ext_storage_night2 = getFile("bg/ext_storage_night.jpg")
    image int_warehouse_day = getFile("bg/int_warehouse_day_7dl.jpg")
    image int_warehouse_day2 = getFile("bg/int_warehouse_day2_7dl.jpg")
    image ext_bush_day_7dl = getFile("bg/ext_bush_day_7dl.jpg")
    image ext_bush_sunset_7dl = getFile("bg/ext_bush_sunset_7dl.jpg")
    image ext_backroad_day_7dl = getFile("bg/ext_backroad_day_7dl.jpg")
    image ext_backroad_sunset_7dl = getFile("bg/ext_backroad_sunset_7dl.jpg")
    image ext_backdoor_day_7dl = getFile("bg/ext_backdoor_day_7dl.jpg")
    image ext_backdoor_sunset_7dl = getFile("bg/ext_backdoor_sunset_7dl.jpg")
    image ext_forest_road_day_ll = getFile("bg/ext_forest_road_day_ll.jpg")
    image ext_forest_road_night_ll = getFile("bg/ext_forest_road_night_ll.jpg")
    image ext_forest_road_rain_ll = getFile("bg/ext_forest_road_rain_ll.jpg")
    image ext_village_back_day_ll = getFile("bg/ext_village_back_day_ll.jpg")
    image ext_village_day_ll = getFile("bg/ext_village_day_ll.jpg")
    image ext_village_rain_ll = getFile("bg/ext_village_rain_ll.jpg")
    image ext_washstand_night_7dl = getFile("bg/ext_washstand_night_7dl.jpg")
    image ext_washstand2_night = getFile("bg/ext_washstand2_night.jpg")
    image ext_pier_night = getFile("bg/ext_pier_night.jpg")
    image ext_boathouse_alt_night_7dl = getFile("bg/ext_boathouse_alt_night_7dl.jpg")

#ДОЖДЛИВЫЕ:
    image int_musclub_rain_7dl = getFile("bg/int_musclub_rain_7dl.jpg")
    image ext_washstand_rain_7dl = getFile("bg/ext_washstand_rain_7dl.jpg")
    image ext_warehouse_rain_day_7dl = getFile("bg/ext_warehouse_rain_day_7dl.jpg")
    image ext_musclub_rain_7dl = getFile("bg/ext_musclub_rain_7dl.jpg")
    image ext_forest_camp_sunset = getFile("bg/ext_forest_camp_sunset.jpg")
    image ext_forest_camp_night = getFile("bg/ext_forest_camp_night.jpg")
    image ext_square_rain_day_7dl = getFile("bg/ext_square_rain_day_7dl.jpg")

#СПРАЙТЫ:
#АЛИСА СПОРТИВКИ:
    image dv angry sport flt = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( tft_sprite_path + "dv/normal/sport/sport_dv_normal_angry.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'",im.MatrixColor( tft_sprite_path + "dv/normal/sport/sport_dv_normal_angry.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, tft_sprite_path + "dv/normal/sport/sport_dv_normal_angry.png")

    image dv laugh sport flt = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( tft_sprite_path + "dv/normal/sport/sport_dv_normal_laugh.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'",im.MatrixColor( tft_sprite_path + "dv/normal/sport/sport_dv_normal_laugh.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, tft_sprite_path + "dv/normal/sport/sport_dv_normal_laugh.png")

    image dv smile sport flt = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( tft_sprite_path + "dv/normal/sport/sport_dv_normal_smile.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'",im.MatrixColor( tft_sprite_path + "dv/normal/sport/sport_dv_normal_smile.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, tft_sprite_path + "dv/normal/sport/sport_dv_normal_smile.png")

    image dv normal sport flt = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( tft_sprite_path + "dv/normal/sport/sport_dv_normal_normal.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'",im.MatrixColor( tft_sprite_path + "dv/normal/sport/sport_dv_normal_normal.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, tft_sprite_path + "dv/normal/sport/sport_dv_normal_normal.png")

    image dv shoked sport flt = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( tft_sprite_path + "dv/normal/sport/sport_dv_normal_shoked.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'",im.MatrixColor( tft_sprite_path + "dv/normal/sport/sport_dv_normal_shoked.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, tft_sprite_path + "dv/normal/sport/sport_dv_normal_shoked.png")

    image dv scared sport flt = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( tft_sprite_path + "dv/normal/sport/sport_dv_normal_scared.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'",im.MatrixColor( tft_sprite_path + "dv/normal/sport/sport_dv_normal_scared.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, tft_sprite_path + "dv/normal/sport/sport_dv_normal_scared.png")

    image dv cry sport flt = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( tft_sprite_path + "dv/normal/sport/sport_dv_normal_cry.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'",im.MatrixColor( tft_sprite_path + "dv/normal/sport/sport_dv_normal_cry.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, tft_sprite_path + "dv/normal/sport/sport_dv_normal_cry.png")

    image dv surprise sport flt = ConditionSwitch( 
        "persistent.sprite_time=='sunset'",im.MatrixColor( tft_sprite_path + "dv/normal/sport/sport_dv_normal_surprise.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'",im.MatrixColor( tft_sprite_path + "dv/normal/sport/sport_dv_normal_surprise.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, tft_sprite_path + "dv/normal/sport/sport_dv_normal_surprise.png")

    image dv surprise2 sport flt = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( tft_sprite_path + "dv/normal/sport/sport_dv_normal_surprise2.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'",im.MatrixColor( tft_sprite_path + "dv/normal/sport/sport_dv_normal_surprise2.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, tft_sprite_path + "dv/normal/sport/sport_dv_normal_surprise2.png")

    image dv grin sport flt = ConditionSwitch( 
        "persistent.sprite_time=='sunset'",im.MatrixColor( tft_sprite_path + "dv/normal/sport/sport_dv_normal_grin.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'",im.MatrixColor( tft_sprite_path + "dv/normal/sport/sport_dv_normal_grin.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, tft_sprite_path + "dv/normal/sport/sport_dv_normal_grin.png")

    image dv guilty sport flt = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( tft_sprite_path + "dv/normal/sport/sport_dv_normal_guilty.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'",im.MatrixColor( tft_sprite_path + "dv/normal/sport/sport_dv_normal_guilty.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, tft_sprite_path + "dv/normal/sport/sport_dv_normal_guilty.png")

    image dv sad sport flt = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( tft_sprite_path + "dv/normal/sport/sport_dv_normal_sad.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'",im.MatrixColor( tft_sprite_path + "dv/normal/sport/sport_dv_normal_sad.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, tft_sprite_path + "dv/normal/sport/sport_dv_normal_sad.png")

    image dv shy sport flt = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( tft_sprite_path + "dv/normal/sport/sport_dv_normal_shy.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'",im.MatrixColor( tft_sprite_path + "dv/normal/sport/sport_dv_normal_shy.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, tft_sprite_path + "dv/normal/sport/sport_dv_normal_shy.png")

#АЛИСА СПОРТИВКИ ДАЛЕКО:
    image dv angry sport far flt = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( tft_sprite_path + "dv/far/sport/sport_dv_angry.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'",im.MatrixColor( tft_sprite_path + "dv/far/sport/sport_dv_angry.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, tft_sprite_path + "dv/far/sport/sport_dv_angry.png")

    image dv rage sport far flt = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( tft_sprite_path + "dv/far/sport/sport_dv_rage.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'",im.MatrixColor( tft_sprite_path + "dv/far/sport/sport_dv_rage.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, tft_sprite_path + "dv/far/sport/sport_dv_rage.png")

    image dv surprise sport far flt = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( tft_sprite_path + "dv/far/sport/sport_dv_surprise.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'",im.MatrixColor( tft_sprite_path + "dv/far/sport/sport_dv_surprise.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, tft_sprite_path + "")

    image sport_dv_far_grin flt = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( tft_sprite_path + "dv/far/sport/sport_dv_grin.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'",im.MatrixColor( tft_sprite_path + "dv/far/sport/sport_dv_grin.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, tft_sprite_path + "dv/far/sport/sport_dv_grin.png")

#АЛИСА КУПАЛЬНИК:
    image dv shy swim flt = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( tft_sprite_path + "dv/normal/swim/swim_dv_shy.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'",im.MatrixColor( tft_sprite_path + "dv/normal/swim/swim_dv_shy.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, tft_sprite_path + "dv/normal/swim/swim_dv_shy.png")

    image dv sadsmile swim flt = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( tft_sprite_path + "dv/normal/swim/swim_dv_sadsmile.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'",im.MatrixColor( tft_sprite_path + "dv/normal/swim/swim_dv_sadsmile.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, tft_sprite_path + "dv/normal/swim/swim_dv_sadsmile.png")

    image dv sad swim flt = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( tft_sprite_path + "dv/normal/swim/swim_dv_sad.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'",im.MatrixColor( tft_sprite_path + "dv/normal/swim/swim_dv_sad.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, tft_sprite_path + "dv/normal/swim/swim_dv_sad.png")

    image dv shy skirt flt = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( tft_sprite_path + "dv/normal/swim/skirt_dv_shy.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'",im.MatrixColor( tft_sprite_path + "dv/normal/swim/skirt_dv_shy.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, tft_sprite_path + "dv/normal/swim/skirt_dv_shy.png")

    image dv smile pioneerskirt flt = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( tft_sprite_path + "dv/normal/swim/dv_smile_pioneerskirt.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'",im.MatrixColor( tft_sprite_path + "dv/normal/swim/dv_smile_pioneerskirt.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, tft_sprite_path + "dv/normal/swim/dv_smile_pioneerskirt.png")

    image dv smile pioneershirt flt = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( tft_sprite_path + "dv/normal/swim/dv_smile_pioneershirt.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'",im.MatrixColor( tft_sprite_path + "dv/normal/swim/dv_smile_pioneershirt.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, tft_sprite_path + "dv/normal/swim/dv_smile_pioneershirt.png")

    image dv smile swimhair flt = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( tft_sprite_path + "dv/normal/swim/dv_smile_swimhair.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'",im.MatrixColor( tft_sprite_path + "dv/normal/swim/dv_smile_swimhair.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, tft_sprite_path + "dv/normal/swim/dv_smile_swimhair.png")

    image dv grin swimhair flt = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( tft_sprite_path + "dv/normal/swim/dv_grin_swimhair.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'",im.MatrixColor( tft_sprite_path + "dv/normal/swim/dv_grin_swimhair.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, tft_sprite_path + "dv/normal/swim/dv_grin_swimhair.png")
        
    image dv smile hair flt = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( tft_sprite_path + "dv/normal/swim/dv_smile_hair.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'",im.MatrixColor( tft_sprite_path + "dv/normal/swim/dv_smile_hair.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, tft_sprite_path + "dv/normal/swim/dv_smile_hair.png")

    image dv smile hairskirt flt = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( tft_sprite_path + "dv/normal/swim/dv_smile_hairskirt.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'",im.MatrixColor( tft_sprite_path + "dv/normal/swim/dv_smile_hairskirt.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, tft_sprite_path + "dv/normal/swim/dv_smile_hairskirt.png")
        
    image dv smile swim flt = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( tft_sprite_path + "dv/normal/swim/dv_smile_swim.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'",im.MatrixColor( tft_sprite_path + "dv/normal/swim/dv_smile_swim.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, tft_sprite_path + "dv/normal/swim/dv_smile_swim.png")

#АЛИСА МОКРАЯ:
    image dv angry wet flt = ConditionSwitch( 
        "persistent.sprite_time=='sunset'",im.MatrixColor( tft_sprite_path + "dv/normal/wet/wet_dv_angry_rain.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'",im.MatrixColor( tft_sprite_path + "dv/normal/wet/wet_dv_angry_rain.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, tft_sprite_path + "dv/normal/wet/wet_dv_angry_rain.png")

    image dv cry wet flt = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( tft_sprite_path + "dv/normal/wet/wet_dv_cry_rain.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'",im.MatrixColor( tft_sprite_path + "dv/normal/wet/wet_dv_cry_rain.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, tft_sprite_path + "dv/normal/wet/wet_dv_cry_rain.png")

    image dv laugh wet flt = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( tft_sprite_path + "dv/normal/wet/wet_dv_laugh_rain.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'",im.MatrixColor( tft_sprite_path + "dv/normal/wet/wet_dv_laugh_rain.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, tft_sprite_path + "dv/normal/wet/wet_dv_laugh_rain.png")

    image dv normal wet flt = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( tft_sprite_path + "dv/normal/wet/wet_dv_normal_rain.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'",im.MatrixColor( tft_sprite_path + "dv/normal/wet/wet_dv_normal_rain.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, tft_sprite_path + "dv/normal/wet/wet_dv_normal_rain.png")

    image dv rage wet flt = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( tft_sprite_path + "dv/normal/wet/wet_dv_rage_rain.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'",im.MatrixColor( tft_sprite_path + "dv/normal/wet/wet_dv_rage_rain.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, tft_sprite_path + "dv/normal/wet/wet_dv_rage_rain.png")

    image dv sad wet flt = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( tft_sprite_path + "dv/normal/wet/wet_dv_sad_rain.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'",im.MatrixColor( tft_sprite_path + "dv/normal/wet/wet_dv_sad_rain.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, tft_sprite_path + "dv/normal/wet/wet_dv_sad_rain.png")

    image dv shy wet flt = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( tft_sprite_path + "dv/normal/wet/wet_dv_shy_rain.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'",im.MatrixColor( tft_sprite_path + "dv/normal/wet/wet_dv_shy_rain.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, tft_sprite_path + "dv/normal/wet/wet_dv_shy_rain.png")

    image dv surprise wet flt = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( tft_sprite_path + "dv/normal/wet/wet_dv_surprise_rain.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'",im.MatrixColor( tft_sprite_path + "dv/normal/wet/wet_dv_surprise_rain.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, tft_sprite_path + "dv/normal/wet/wet_dv_surprise_rain.png")

#АЛИСА ПИОНЕРСКАЯ:
    image dv smile4 pioneer flt = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( tft_sprite_path + "dv/normal/pioneer/pioneer_dv_smile6.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'",im.MatrixColor( tft_sprite_path + "dv/normal/pioneer/pioneer_dv_smile6.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, tft_sprite_path + "dv/normal/pioneer/pioneer_dv_smile6.png")

    image dv smile5 pioneer flt = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( tft_sprite_path + "dv/normal/pioneer/pioneer_dv_smile7.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'",im.MatrixColor( tft_sprite_path + "dv/normal/pioneer/pioneer_dv_smile7.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, tft_sprite_path + "dv/normal/pioneer/pioneer_dv_smile7.png")

    image dv grin pioneer flt = ConditionSwitch( 
        "persistent.sprite_time=='sunset'",im.MatrixColor( tft_sprite_path + "dv/normal/pioneer/pioneer_dv_grin.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'",im.MatrixColor( tft_sprite_path + "dv/normal/pioneer/pioneer_dv_grin.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, tft_sprite_path + "dv/normal/pioneer/pioneer_dv_grin.png")

    image dv surprise2 pioneer close flt = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( tft_sprite_path + "dv/close/pioneer/pioneer_dv_surprise2.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'",im.MatrixColor( tft_sprite_path + "dv/close/pioneer/pioneer_dv_surprise2.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, tft_sprite_path + "dv/close/pioneer/pioneer_dv_surprise2.png")

    image dv surprise pioneer flt = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( tft_sprite_path + "dv/normal/pioneer/dv_surprise_pioneer.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'",im.MatrixColor( tft_sprite_path + "dv/normal/pioneer/dv_surprise_pioneer.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, tft_sprite_path + "dv/normal/pioneer/dv_surprise_pioneer.png")

    image dv thinking pioneer flt = ConditionSwitch( 
        "persistent.sprite_time=='sunset'",im.MatrixColor( tft_sprite_path + "dv/normal/pioneer/pioneer_dv_thinking.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'",im.MatrixColor( tft_sprite_path + "dv/normal/pioneer/pioneer_dv_thinking.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, tft_sprite_path + "dv/normal/pioneer/pioneer_dv_thinking.png")

    image dv thinking2 pioneer close flt = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( tft_sprite_path + "dv/close/pioneer/pioneer_dv_think.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'",im.MatrixColor( tft_sprite_path + "dv/close/pioneer/pioneer_dv_think.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, tft_sprite_path + "dv/close/pioneer/pioneer_dv_think.png")

    image dv shy2 pioneer close flt = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( tft_sprite_path + "dv/close/pioneer/pioneer_dv_shy2.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'",im.MatrixColor( tft_sprite_path + "dv/close/pioneer/pioneer_dv_shy2.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, tft_sprite_path + "dv/close/pioneer/pioneer_dv_shy2.png")

    image dv scared1 pioneer flt = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( tft_sprite_path + "dv/normal/pioneer/pioneer_dv_scared1.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'",im.MatrixColor( tft_sprite_path + "dv/normal/pioneer/pioneer_dv_scared1.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, tft_sprite_path + "dv/normal/pioneer/pioneer_dv_scared1.png.png")

    image dv guilty pioneer flt = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( tft_sprite_path + "dv/normal/pioneer/dv_pioneer_guilty_flt.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'",im.MatrixColor( tft_sprite_path + "dv/normal/pioneer/dv_pioneer_guilty_flt.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, tft_sprite_path + "dv/normal/pioneer/dv_pioneer_guilty_flt.png.png")

    image dv sad pioneer flt = ConditionSwitch( 
        "persistent.sprite_time=='sunset'",im.MatrixColor( tft_sprite_path + "dv/normal/pioneer/dv_pioneer_sad_flt.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'",im.MatrixColor( tft_sprite_path + "dv/normal/pioneer/dv_pioneer_sad_flt.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, tft_sprite_path + "dv/normal/pioneer/dv_pioneer_sad_flt.png")

    image dv angry pioneer flt = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( tft_sprite_path + "dv/normal/pioneer/dv_angry_pioneer.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'",im.MatrixColor( tft_sprite_path + "dv/normal/pioneer/dv_angry_pioneer.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, tft_sprite_path + "dv/normal/pioneer/dv_angry_pioneer.png.png")

    image dv scared1 pioneer flt = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( tft_sprite_path + "dv/normal/pioneer/pioneer_dv_scared1.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'",im.MatrixColor( tft_sprite_path + "dv/normal/pioneer/pioneer_dv_scared1.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, tft_sprite_path + "dv/normal/pioneer/pioneer_dv_scared1.png")

#АЛИСА ПИОНЕРСКАЯ С УЗЛОМ:
    image dv heart pioneer2 far flt = ConditionSwitch( 
        "persistent.sprite_time=='sunset'",im.MatrixColor( tft_sprite_path + "dv/far/pioneer2/pioneer2_dv_heart.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'",im.MatrixColor( tft_sprite_path + "dv/far/pioneer2/pioneer2_dv_heart.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, tft_sprite_path + "dv/far/pioneer2/pioneer2_dv_heart.png")

    image dv sad2 pioneer2 flt = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( tft_sprite_path + "dv/normal/pioneer2/pioneer2_dv_sad2", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'",im.MatrixColor( tft_sprite_path + "dv/normal/pioneer2/pioneer2_dv_sad2", im.matrix.tint(0.63, 0.78, 0.82)),
        True, tft_sprite_path + "dv/normal/pioneer2/pioneer2_dv_sad2")

    image dv guilty pioneer2 flt = ConditionSwitch( 
        "persistent.sprite_time=='sunset'",im.MatrixColor( tft_sprite_path + "dv/normal/pioneer2/pioneer2_dv_guilty.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'",im.MatrixColor( tft_sprite_path + "dv/normal/pioneer2/pioneer2_dv_guilty.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, tft_sprite_path + "dv/normal/pioneer2/pioneer2_dv_guilty.png")

    image dv scared pioneer2 flt = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( tft_sprite_path + "dv/normal/pioneer2/pioneer2_dv_scared.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'",im.MatrixColor( tft_sprite_path + "dv/normal/pioneer2/pioneer2_dv_scared.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, tft_sprite_path + "dv/normal/pioneer2/pioneer2_dv_scared.png")

    image dv smile2 pioneer2 flt = ConditionSwitch( 
        "persistent.sprite_time=='sunset'",im.MatrixColor( tft_sprite_path + "dv/normal/pioneer2/pioneer2_dv_smile2.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'",im.MatrixColor( tft_sprite_path + "dv/normal/pioneer2/pioneer2_dv_smile2.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, tft_sprite_path + "dv/normal/pioneer2/pioneer2_dv_smile2.png")

    image dv surprise pioneer2 flt = ConditionSwitch( 
        "persistent.sprite_time=='sunset'",im.MatrixColor( tft_sprite_path + "dv/normal/pioneer2/pioneer2_dv_surprise.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'",im.MatrixColor( tft_sprite_path + "dv/normal/pioneer2/pioneer2_dv_surprise.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, tft_sprite_path + "dv/normal/pioneer2/pioneer2_dv_surprise.png")

    image dv surprise2 pioneer2 flt = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( tft_sprite_path + "dv/normal/pioneer2/pioneer2_dv_surprise2.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'",im.MatrixColor( tft_sprite_path + "dv/normal/pioneer2/pioneer2_dv_surprise2.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, tft_sprite_path + "dv/normal/pioneer2/pioneer2_dv_surprise2.png")

    image dv shoked pioneer2 flt = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( tft_sprite_path + "dv/normal/pioneer2/pioneer2_dv_shoked.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'",im.MatrixColor( tft_sprite_path + "dv/normal/pioneer2/pioneer2_dv_shoked.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, tft_sprite_path + "dv/normal/pioneer2/pioneer2_dv_shoked.png")

    image dv shoked2 pioneer2 flt = ConditionSwitch( 
        "persistent.sprite_time=='sunset'",im.MatrixColor( tft_sprite_path + "dv/normal/pioneer2/pioneer2_dv_shoked2.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'",im.MatrixColor( tft_sprite_path + "dv/normal/pioneer2/pioneer2_dv_shoked2.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, tft_sprite_path + "dv/normal/pioneer2/pioneer2_dv_shoked2.png")

    image dv shy pioneer2 flt = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( tft_sprite_path + "dv/normal/pioneer2/pioneer2_dv_shy.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'",im.MatrixColor( tft_sprite_path + "dv/normal/pioneer2/pioneer2_dv_shy.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, tft_sprite_path + "dv/normal/pioneer2/pioneer2_dv_shy.png")

    image dv grin pioneer2 flt = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( tft_sprite_path + "dv/normal/pioneer2/pioneer2_dv_grin.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'",im.MatrixColor( tft_sprite_path + "dv/normal/pioneer2/pioneer2_dv_grin.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, tft_sprite_path + "dv/normal/pioneer2/pioneer2_dv_grin.png")

    image dv angry pioneer2 flt = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( tft_sprite_path + "dv/normal/pioneer2/pioneer2_dv_angry.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'",im.MatrixColor( tft_sprite_path + "dv/normal/pioneer2/pioneer2_dv_angry.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, tft_sprite_path + "dv/normal/pioneer2/pioneer2_dv_angry.png")

    image dv rage pioneer2 flt = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( tft_sprite_path + "dv/normal/pioneer2/pioneer2_dv_rage.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'",im.MatrixColor( tft_sprite_path + "dv/normal/pioneer2/pioneer2_dv_rage.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, tft_sprite_path + "dv/normal/pioneer2/pioneer2_dv_rage.png")

    image dv normal pioneer2 flt = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( tft_sprite_path + "dv/normal/pioneer2/dv_normal_pioneer2.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'",im.MatrixColor( tft_sprite_path + "dv/normal/pioneer2/dv_normal_pioneer2.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, tft_sprite_path + "dv/normal/pioneer2/dv_normal_pioneer2.png")

#АРСЕНИЙ:
    image ars_angry = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( tft_sprite_path + "ars/pioneer/ars_angry.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'",im.MatrixColor( tft_sprite_path + "ars/pioneer/ars_angry.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, tft_sprite_path + "ars/pioneer/ars_angry.png")

    image ars_angry2 = ConditionSwitch( 
        "persistent.sprite_time=='sunset'",im.MatrixColor( tft_sprite_path + "ars/pioneer/ars_angry2.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'",im.MatrixColor( tft_sprite_path + "ars/pioneer/ars_angry2.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, tft_sprite_path + "ars/pioneer/ars_angry2.png")

    image ars_normal = ConditionSwitch( 
        "persistent.sprite_time=='sunset'",im.MatrixColor( tft_sprite_path + "ars/pioneer/ars_normal.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'",im.MatrixColor( tft_sprite_path + "ars/pioneer/ars_normal.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, tft_sprite_path + "ars/pioneer/ars_normal.png")

    image ars_normal2  = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( tft_sprite_path + "ars/pioneer/ars_normal2.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'",im.MatrixColor( tft_sprite_path + "ars/pioneer/ars_normal2.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, tft_sprite_path + "ars/pioneer/ars_normal2.png")
        
    image ars_smile = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( tft_sprite_path + "ars/pioneer/ars_smile.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'",im.MatrixColor( tft_sprite_path + "ars/pioneer/ars_smile.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, tft_sprite_path + "ars/pioneer/ars_smile.png")

    image ars_smile2 = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( tft_sprite_path + "ars/pioneer/ars_smile2.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'",im.MatrixColor( tft_sprite_path + "ars/pioneer/ars_smile2.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, tft_sprite_path + "ars/pioneer/ars_smile2.png")

    image ars_smile3 = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( tft_sprite_path + "ars/pioneer/ars_smile3.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'",im.MatrixColor( tft_sprite_path + "ars/pioneer/ars_smile3.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, tft_sprite_path + "ars/pioneer/ars_smile3.png")

    image ars_smile4 = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( tft_sprite_path + "ars/pioneer/ars_smile4.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'",im.MatrixColor( tft_sprite_path + "ars/pioneer/ars_smile4.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, tft_sprite_path + "ars/pioneer/ars_smile4.png")

    image ars_surprise = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( tft_sprite_path + "ars/pioneer/ars_surprise.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'",im.MatrixColor( tft_sprite_path + "ars/pioneer/ars_surprise.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, tft_sprite_path + "ars/pioneer/ars_surprise.png")

    image ars_surprise2 = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( tft_sprite_path + "ars/pioneer/ars_surprise2.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'",im.MatrixColor( tft_sprite_path + "ars/pioneer/ars_surprise2.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, tft_sprite_path + "ars/pioneer/ars_surprise2.png")

    image ars_think = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( tft_sprite_path + "ars/pioneer/ars_think.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'",im.MatrixColor( tft_sprite_path + "ars/pioneer/ars_think.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, tft_sprite_path + "ars/pioneer/ars_think.png")

    image ars_think2 = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( tft_sprite_path + "ars/pioneer/ars_think2.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'",im.MatrixColor( tft_sprite_path + "ars/pioneer/ars_think2.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, tft_sprite_path + "ars/pioneer/ars_think2.png")

#МИКУ МОКРАЯ:
    image mi_grin_wet_rain = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( tft_sprite_path + "mi/wet/mi_grin_wet_rain.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'",im.MatrixColor( tft_sprite_path + "mi/wet/mi_grin_wet_rain.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, tft_sprite_path + "mi/wet/mi_grin_wet_rain.png")

    image mi_normal_wet_rain = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( tft_sprite_path + "mi/wet/mi_normal_wet_rain.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'",im.MatrixColor( tft_sprite_path + "mi/wet/mi_normal_wet_rain.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, tft_sprite_path + "mi/wet/mi_normal_wet_rain.png")

    image mi_shy_wet_rain = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( tft_sprite_path + "mi/wet/mi_shy_wet_rain.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'",im.MatrixColor( tft_sprite_path + "mi/wet/mi_shy_wet_rain.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, tft_sprite_path + "mi/wet/mi_shy_wet_rain.png")

    image mi_smile_wet_rain = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( tft_sprite_path + "mi/wet/mi_smile_wet_rain.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'",im.MatrixColor( tft_sprite_path + "mi/wet/mi_smile_wet_rain.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, tft_sprite_path + "mi/wet/mi_smile_wet_rain.png")

    image mi_surprise_wet_rain = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( tft_sprite_path + "mi/wet/mi_surprise_wet_rain.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'",im.MatrixColor( tft_sprite_path + "mi/wet/mi_surprise_wet_rain.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, tft_sprite_path + "mi/wet/mi_surprise_wet_rain.png")

    image mi_upset_wet_rain = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( tft_sprite_path + "mi/wet/mi_upset_wet_rain.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'",im.MatrixColor( tft_sprite_path + "mi/wet/mi_upset_wet_rain.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, tft_sprite_path + "mi/wet/mi_upset_wet_rain.png")

    image mi_scared_wet_rain = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( tft_sprite_path + "mi/wet/mi_scared_wet_rain.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'",im.MatrixColor( tft_sprite_path + "mi/wet/mi_scared_wet_rain.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, tft_sprite_path + "mi/wet/mi_scared_wet_rain.png")

    image mi_shocked_wet_rain = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( tft_sprite_path + "mi/wet/mi_shocked_wet_rain.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'",im.MatrixColor( tft_sprite_path + "mi/wet/mi_shocked_wet_rain.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, tft_sprite_path + "mi/wet/mi_shocked_wet_rain.png")

#АЛИСА ПИЖАМА:
    image sleep_dv_shy = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( tft_sprite_path + "dv/far/sleep/sleep_dv_shy.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'",im.MatrixColor( tft_sprite_path + "dv/far/sleep/sleep_dv_shy.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, tft_sprite_path + "dv/far/sleep/sleep_dv_shy.png")

#УЛЬЯНА СПИНОЙ:
    image spina_us = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( tft_sprite_path + "us/spina_us.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'",im.MatrixColor( tft_sprite_path + "us/spina_us.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, tft_sprite_path + "us/spina_us.png")

#МИКУ СПИНА И РУКИ:
    image spina_mi = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( tft_sprite_path + "mi/spina_mi.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'",im.MatrixColor( tft_sprite_path + "mi/spina_mi.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, tft_sprite_path + "mi/spina_mi.png")

    image miku_ruki = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( tft_sprite_path + "mi/miku_ruki.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'",im.MatrixColor( tft_sprite_path + "mi/miku_ruki.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, tft_sprite_path + "mi/miku_ruki.png")

#ПОВАР МАРИЯ:
    image cook_laugh = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( tft_sprite_path + "nt/nt_1_cook.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'",im.MatrixColor( tft_sprite_path + "nt/nt_1_cook.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, tft_sprite_path + "nt/nt_1_cook.png")

    image cook_smile = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( tft_sprite_path + "nt/nt_2_cook.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'",im.MatrixColor( tft_sprite_path + "nt/nt_2_cook.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, tft_sprite_path + "nt/nt_2_cook.png")

    image cook_normal = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( tft_sprite_path + "nt/nt_3_cook.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'",im.MatrixColor( tft_sprite_path + "nt/nt_3_cook.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, tft_sprite_path + "nt/nt_3_cook.png")

    image cook_sad = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( tft_sprite_path + "nt/nt_4_cook.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'",im.MatrixColor( tft_sprite_path + "nt/nt_4_cook.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, tft_sprite_path + "nt/nt_4_cook.png")

#ПЕТЯ s1pepega:
    image petr_smile = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( tft_sprite_path + "ded/petr_smile.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'",im.MatrixColor( tft_sprite_path + "ded/petr_smile.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, tft_sprite_path + "ded/petr_smile.png")

    image petr_grin = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( tft_sprite_path + "ded/petr_grin.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'",im.MatrixColor( tft_sprite_path + "ded/petr_grin.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, tft_sprite_path + "ded/petr_grin.png")

    image petr_normal = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( tft_sprite_path + "ded/petr_normal.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'",im.MatrixColor( tft_sprite_path + "ded/petr_normal.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, tft_sprite_path + "ded/petr_normal.png")

#МАША:
    image msh_laugh_sport = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( tft_sprite_path + "msh/msh_laugh_sport.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'",im.MatrixColor( tft_sprite_path + "msh/msh_laugh_sport.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, tft_sprite_path + "msh/msh_laugh_sport.png")
        
    image msh_smile_sport = ConditionSwitch(
        "persistent.sprite_time=='sunset'",im.MatrixColor( tft_sprite_path + "msh/msh_smile_backhands_sport.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'",im.MatrixColor( tft_sprite_path + "msh/msh_smile_backhands_sport.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, tft_sprite_path + "msh/msh_smile_backhands_sport.png")
        
#ПРОЧЕЕ:
    image chair = getFile("sprites/misc/chair.png")
    image chair2 = getFile("sprites/misc/chair2.png")
    image aftertwohour = getFile("gui/aftertwohour.png")
    image day3 = getFile("gui/day3.png")
    image white_screen = getFile("gui/white_screen.png")
    image tft_menu_background = getFile("screens/menu/tft_menu_background.png")
    image pirat_prewiew = getFile("gui/pirat_prewiew.jpg")

    # = ConditionSwitch(
    #    "persistent.sprite_time=='sunset'",im.MatrixColor( tft_sprite_path + "", im.matrix.tint(0.94, 0.82, 1.0)),
    #    "persistent.sprite_time=='night'",im.MatrixColor( tft_sprite_path + "", im.matrix.tint(0.63, 0.78, 0.82)),
    #    True, tft_sprite_path + "")