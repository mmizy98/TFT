init -99 python:
    def getSprite(FilePath):
        return ConditionSwitch(
            "persistent.sprite_time=='day'", im.MatrixColor( FilePath, im.matrix.tint(0.83, 0.88, 0.92)),
            "persistent.sprite_time=='sunset'", im.MatrixColor(FilePath, im.matrix.tint(0.94, 0.82, 1.0)),
            "persistent.sprite_time=='night'", im.MatrixColor(FilePath, im.matrix.tint(0.63, 0.78, 0.82)))

    
    def TFTgetRandomItem(items):
        num = renpy.random.randint(0, len(items)-1)
        return items[num]  
    def TFTgetRandomButton():
        return TFTgetRandomItem(['W','A','D','E','R','F','C','G'])

init:
    define config.developer = True
    $ mods["tft_menu_main"]=u"Cудьбы Двух"

    $ day1_vzlom = False
    $ day0_drunk =  False
    $ tft_qte_loose = False
    $ tft_qte_count = 0

# Transforms:

    define flash_black = Fade(5, 0.0, 0.5, color="#000000")

    transform stepping:
        anchor (0.0, 0.0) pos (0.0, 0.0)
        linear 0.5 pos (-5, -5)
        linear 0.5 pos (0, 0)
        linear 0.5 pos (5, -5)
        linear 0.5 pos (0, 0)
        repeat

    transform headshaking:
        anchor (0.0, 0.0) pos (0.0, 0.0)
        linear 0.08 pos (-7, 0)
        linear 0.08 pos (0, 0)
        linear 0.08 pos (7, 0)
        linear 0.08 pos (0, 0)

    transform appdouble(imgn, z=1.1, zt=1.0, t=1.0):
        contains:
            ImageReference(imgn)
            truecenter
            linear zt zoom z
        contains:
            ImageReference(imgn)
            truecenter
            zoom z
            alpha 0.0
            pause zt
            linear t xpos 0.48 alpha 0.3 zoom (z + 0.05)
        contains:
            ImageReference(imgn)
            truecenter
            zoom z
            alpha 0.0
            pause zt
            linear t xpos 0.51 alpha 0.2 zoom (z + 0.05)
        
# Characters:

    # Denis:
    $ dns = Character (u'Денис', color = "#a7c575", what_color = "E2C778")
    # Arseniy:
    $ ars = Character (u'Арсений', color = "#de6868", what_color = "E2C778")
    # Фанат
    $ fan = Character (u'Поклонник', color = "#7e79b5", what_color = "E2C778")
    # Cook:
    $ pvr = Character (u'Повар', color = "#4170fd", what_color = "E2C778")
    $ mar = Character (u'Мария', color = "#4170fd", what_color = "E2C778")
    # Музыканты
    $ muz = Character (u'Музыкант', color = "#440475", what_color = "E2C778")
    $ muzs = Character (u'Музыканты', color = "#440475", what_color = "E2C778")
    
# Sounds:

    # Music:

    $ roxette = "mods/TFT/image/sound/music/roxette.mp3"

    $ your_nobility = "mods/TFT/image/sound/music/your_nobility.mp3"

    $ GS_Chasing_a_Rumor = "mods/TFT/image/sound/music/GS_Chasing_a_Rumor.mp3"

    $ greenday = "mods/TFT/image/sound/music/greenday.mp3"

    $ hyperborea = "mods/TFT/image/sound/music/hyperborea.mp3"

    $ sizor = "mods/TFT/image/sound/music/sizor.mp3"

    $ kostr = "mods/TFT/image/sound/music/vzveiteskostrami.mp3"

    $ plastinki = "mods/TFT/image/sound/music/plastinki.ogg"

    $ unbroken = "mods/TFT/image/sound/music/Unbroken.mp3"

    $ prologmusic = "mods/TFT/image/sound/music/prologmusic.mp3"

    $ BLAD = "mods/TFT/image/sound/music/BLAD.mp3"

    $ aprilrain = "mods/TFT/image/sound/music/aprilrain.mp3"

    $ SP_city = "mods/TFT/image/sound/music/SP_city.mp3"

    $ deepcosmo = "mods/TFT/image/sound/music/deepcosmo.mp3"

    $ porn_diapazon = "mods/TFT/image/sound/music/diapazon.mp3"

    $ stressedoutminus = "mods/TFT/image/sound/music/stressedoutminus.mp3"

    $ Omelchuk_Roads_Ahead = "mods/TFT/image/sound/music/Omelchuk_Roads_Ahead.mp3"
    
    # SFX:
    $ heartbeat = "mods/TFT/image/sound/sfx/heartbeat.mp3"

    $ avaria = "mods/TFT/image/sound/sfx/avaria.mp3"

    $ claps = "mods/TFT/image/sound/sfx/claps.mp3"

    $ oi = "mods/TFT/image/sound/sfx/oi1.ogg"

    $ saray = "mods/TFT/image/sound/sfx/saray_door1.mp3"

    $ storage = "mods/TFT/image/sound/sfx/storage_noise.ogg"

    $ storagenoise = "mods/TFT/image/sound/sfx/storage_noise.ogg"

    $ jimbeam = "mods/TFT/image/sound/sfx/jimbeam.mp3"

    $ window_dining = "mods/TFT/image/sound/sfx/window_dining.mp3"

    $ fall_bed = "mods/TFT/image/sound/sfx/fall_onto_bed.ogg"

    $ train_honk = "mods/TFT/image/sound/sfx/train_honk.mp3"
    
    $ clock_timeskip = "mods/TFT/image/sound/sfx/clock_timeskip.mp3"

    $ ambience_city = "mods/TFT/image/sound/sfx/ambience_city.mp3"

    $ clock_alert = "mods/TFT/image/sound/sfx/clock_alert.mp3"

    $ light = "mods/TFT/image/sound/sfx/light_on.mp3"

    $ shot = "mods/TFT/image/sound/sfx/shot.mp3"

    $ rattle = "mods/TFT/image/sound/sfx/rattle.mp3"

    $ resiever = "mods/TFT/image/sound/sfx/resiever.mp3"

    $ okno = "mods/TFT/image/sound/sfx/okno.mp3"

    $ fridge = "mods/TFT/image/sound/sfx/fridge.mp3"

    $ liazdoor = "mods/TFT/image/sound/sfx/liazdoor.mp3"

    $ coldsteps = "mods/TFT/image/sound/sfx/coldsteps.mp3"

    $ train = "mods/TFT/image/sound/sfx/train_inside.mp3"

    
# Pictures:

    # Alisa pics:
    image aliceroof = "mods/TFT/image/cg/aliceroof.jpg"

    image dvfire = "mods/TFT/image/cg/dvfire.jpg"

    image dv_polyana2 = "mods/TFT/image/cg/dv_polyana2.jpeg"

    image night_event = "mods/TFT/image/cg/night_event.jpg"

    image d3_dv_kiss_7dl = "mods/TFT/image/cg/d3_dv_kiss_7dl.jpg"

    image d3_dv_kiss_7dl_rev = "mods/TFT/image/cg/d3_dv_kiss_7dl_rev.jpg"

    image dvpodnos = "mods/TFT/image/cg/dvpodnos.jpg"

    image dvuneat = "mods/TFT/image/cg/dvuneat.jpg"

    image dveda = "mods/TFT/image/cg/dveda.jpg"

    image dvmushug = "mods/TFT/image/cg/dvmushug.jpg"

    image dvcryhug = "mods/TFT/image/cg/dvcryhug.jpg"

    image dvlovenight = "mods/TFT/image/cg/dvlovenight.jpg"

    image hittendv = "mods/TFT/image/cg/dv_hit.png"

    image dv_beach_sunset = "mods/TFT/image/cg/dv_beach_sunset.jpg"

    image dv_shore = "mods/TFT/image/cg/dv_kiss_st.png"

    image dvkissforest = "mods/TFT/image/cg/dvkissforest.jpg"

    image dvdance = "mods/TFT/image/cg/ss_dv_dance.jpg"

    image dvsleep = "mods/TFT/image/cg/dvsleep.jpg"

    image dvfallangry = "mods/TFT/image/cg/dvfallangry.jpg"

    image sexdv1 = "mods/TFT/image/cg/sexdv1.jpg"

    image sexdv2 = "mods/TFT/image/cg/sexdv2.jpg"

    image lovedv1 = "mods/TFT/image/cg/lovedv1.jpg"

    image lovedv2 = "mods/TFT/image/cg/lovedv2.jpg"

    image dvnight = "mods/TFT/image/cg/dvnight.png"

    image sondv = "mods/TFT/image/cg/MoV1IAs8Ufc.jpg"

    image dvhug2 = "mods/TFT/image/cg/XrQy7tlzzFE.jpg"

    image dvmibus = "mods/TFT/image/cg/d1_mi_dv_bus_7dl.jpg"

    image dv_thinking_close = "mods/TFT/image/cg/dv_thinking_close.jpg"

    image dv_sleep_window = "mods/TFT/image/cg/dv_sleep_window.jpg"

    image dv_sleep_bed = "mods/TFT/image/cg/dv_sleep_bed.jpg"
    
    # Other:
    image food_breakfast = "mods/TFT/image/cg/food_breakfast.png"

    image volleyball = "mods/TFT/image/cg/volleyball.png"

    image semsquore = "mods/TFT/image/cg/semsquore.jpg"

    image slexit = "mods/TFT/image/cg/d1_sl_exit.jpg"

    image mikufort = "mods/TFT/image/cg/mikufort.jpg"

    image d2_wertuska_wse = "mods/TFT/image/cg/d2_wertuska_wse.jpg"

    image mikuboat = "mods/TFT/image/cg/mikuboat.jpg"

    image fag_room = "mods/TFT/image/cg/d3_fag_room.jpg"

    image mi_guitar = "mods/TFT/image/cg/mi_guitar.jpg"

    image navrat2 = "mods/TFT/image/cg/navrat2.jpg"

    image morning_line = "mods/TFT/image/cg/morning_line.jpg"

    image son = "mods/TFT/image/cg/wtf_end_of_day.jpg"

    image mirror = "mods/TFT/image/cg/semyon_mirror.jpg"

    image navrat = "mods/TFT/image/cg/navrat.jpg"

    image sportsunset = "mods/TFT/image/cg/ext_playground_sunset.jpg"

    image jerry = "mods/TFT/image/cg/jerry.jpg"

    image mirror2 = "mods/TFT/image/cg/semyon_mirror2.jpg"

# Backgrounds:
    
    # City:
    image night_bar = "mods/TFT/image/bg/night_bar.jpg"

    image int_prolog_nightclub = "mods/TFT/image/bg/int_prolog_nightclub.jpg"

    image ext_city_night_7dl = "mods/TFT/image/bg/ext_city_night_7dl.jpg"

    image ext_mv2_7dl = "mods/TFT/image/bg/ext_mv2_7dl.jpg"

    image cityhouse = "mods/TFT/image/bg/cityhouse.jpg"

    image ext_bus_city = "mods/TFT/image/bg/ext_bus_city.jpg"

    image windowsun = "mods/TFT/image/bg/windowsun.jpg"

    image roommorning = "mods/TFT/image/bg/roommorning.png"

    image kitchen2 = "mods/TFT/image/bg/kitchen2.jpg"

    image roomwindowsun = "mods/TFT/image/bg/int_semen_room_window_day_7dl.jpg"

    image podzd2 = "mods/TFT/image/bg/podzd2.jpg"

    image ulica2 = "mods/TFT/image/bg/ulica2.jpg"

    image market = "mods/TFT/image/bg/market.png"

    image market2 = "mods/TFT/image/bg/market2.png"

    image train = "mods/TFT/image/bg/train.jpg"

    image vokzal = "mods/TFT/image/bg/vokzal.jpg"

    image train2 = "mods/TFT/image/bg/train2.jpg"

    image starbucks = "mods/TFT/image/bg/starbucks.jpg"

    image ostanovka2 = "mods/TFT/image/bg/ostanovka2.jpg"

    image vavtday = "mods/TFT/image/bg/vavtday.jpg"

    image busepilogue = "mods/TFT/image/bg/busepilogue.png"

    image roomreal = "mods/TFT/image/bg/roomreal.jpg"

    image lift = "mods/TFT/image/bg/lift_normal.jpg"

    image city1 = "mods/TFT/image/bg/dct_landscape_city1.jpg"

    image city2 = "mods/TFT/image/bg/ext_IRL_night.png"

    image ulica2 = "mods/TFT/image/bg/ulica2.jpg"

    image ext_winterpark_7dl = "mods/TFT/image/bg/ext_winterpark_7dl.jpg"

    image bath = "mods/TFT/image/bg/bath.png"

    image vavt = "mods/TFT/image/bg/vavt.jpg"

    image ulica_day = "mods/TFT/image/bg/ulica_day.jpg"

    image ext_bus_city = "mods/TFT/image/bg/ext_bus_city.jpg"

    image kitchen = "mods/TFT/image/bg/kitchen.jpg"

    image podzd = "mods/TFT/image/bg/podzd.jpg"
    
    # Camp:

    image menu_fone = "mods/TFT/image/bg/menu_fone.jpg"

    image ext_music_club_verandah_day = "mods/TFT/image/bg/ext_music_club_verandah_day.jpg"

    image ext_admins_night_7dl = "mods/TFT/image/bg/ext_admins_night_7dl.jpg"

    image ext_admins_day_7dl = "mods/TFT/image/bg/ext_admins_day_7dl.jpg"

    image int_house_of_dv_night2 = "mods/TFT/image/bg/int_house_of_dv_night2.jpg"

    image int_staircase_7dl = "mods/TFT/image/bg/int_staircase_7dl.jpg"

    image int_store_7dl = "mods/TFT/image/bg/int_store_7dl.jpg"

    image ext_volley_court_7dl = "mods/TFT/image/bg/ext_volley_court_7dl.jpg"

    image ext_houses_night = "mods/TFT/image/bg/ext_houses_night.jpg"

    image dvhousesunset = "mods/TFT/image/bg/dvhousesunset.jpg"

    image cssunset = "mods/TFT/image/bg/cssunset.jpg"

    image domnight = "mods/TFT/image/bg/domnight.jpg"

    image muznight = "mods/TFT/image/bg/muznight.jpg"

    image dark_room = "mods/TFT/image/bg/dark_room.jpg"

    image ss_datroom_day = "mods/TFT/image/bg/ss_datroom_day.jpg"

    image ext_old_house_day = "mods/TFT/image/bg/ext_old_house_day.jpg"

    image int_old_house_day = "mods/TFT/image/bg/int_old_house_day.jpg"

    image vorota = "mods/TFT/image/bg/vorota.png"

    image ext_beach_water_sunset = "mods/TFT/image/bg/ext_beach_water_sunset.jpg"

    image oldrainy = "mods/TFT/image/bg/int_old_building_day_rainy.jpg"

    image forest = "mods/TFT/image/bg/ext_forest_day_rainy.jpg"

    image forest2 = "mods/TFT/image/bg/ext_forest2_day_rainy.jpg"

    image int_banya_clear = "mods/TFT/image/bg/int_banya_clear.jpg"

    image int_banya_smoke = "mods/TFT/image/bg/int_banya_smoke.jpg"

    image stolovaya1 = "mods/TFT/image/bg/int_stolovaya_notfull.jpg"

    image muznight2 = "mods/TFT/image/bg/muznight2.jpg"

    image dom = "mods/TFT/image/bg/domsemday.jpg"

    image clubsevening = "mods/TFT/image/bg/ext_clubs_sunset.jpg"

    image domext = "mods/TFT/image/bg/ext_hata_nru_day.jpg"

    image domextnight = "mods/TFT/image/bg/ext_hata_nru_night.jpg"

    image domexteven = "mods/TFT/image/bg/ext_house_of_max_sunset.jpg"

    image domeven = "mods/TFT/image/bg/ggroomnl.png"

    image muznight3 = "mods/TFT/image/bg/muznight3.jpg"

    image domnight = "mods/TFT/image/bg/domnight.jpg"

    image ext_house_of_un_night = "mods/TFT/image/bg/ext_house_of_un_night.jpg"

    image muznightinside = "mods/TFT/image/bg/muznightinside.jpg"

    image ext_playground_sunset = "mods/TFT/image/bg/ext_playground_sunset.jpg"

    image mikunight = "mods/TFT/image/bg/mikunight.jpg"

    image muznightnear = "mods/TFT/image/bg/muzhightnear.jpg"

    image buswindow = "mods/TFT/image/bg/int_bus_window.png"

    image sov2 = "mods/TFT/image/bg/sov2.jpg"

    image sov1 = "mods/TFT/image/bg/sov1.jpg"

    image sov3 = "mods/TFT/image/bg/sov3.jpg"

    image sklad_day = "mods/TFT/image/bg/sklad_day.jpg"

    image muzinnight = "mods/TFT/image/bg/muzinnight.jpg"

    image domintnight2 = "mods/TFT/image/bg/domintnight2.png"

    image windowsun = "mods/TFT/image/bg/windowsun.jpg"

    image ext_storage_day = "mods/TFT/image/bg/ext_storage_day2.jpg"

    image ext_storage_night = "mods/TFT/image/bg/ext_storage_night2.jpg"

    image ext_storage_day2 = "mods/TFT/image/bg/ext_storage_day.png"

    image ext_storage_night2 = "mods/TFT/image/bg/ext_storage_night.jpg"

    image int_warehouse_day = "mods/TFT/image/bg/int_warehouse_day_7dl.jpg"

    image int_warehouse_day2 = "mods/TFT/image/bg/int_warehouse_day2_7dl.jpg"

# image/sprites:

    # Alisa sport wear:
    image dv angry sport flt  = getSprite("mods/TFT/image/sprites/dv/normal/sport/sport_dv_normal_angry.png")
    image dv laugh sport flt  = getSprite("mods/TFT/image/sprites/dv/normal/sport/sport_dv_normal_laugh.png")
    image dv smile sport flt  = getSprite("mods/TFT/image/sprites/dv/normal/sport/sport_dv_normal_smile.png")
    image dv normal sport flt  = getSprite("mods/TFT/image/sprites/dv/normal/sport/sport_dv_normal_normal.png")
    image dv shoked sport flt  = getSprite("mods/TFT/image/sprites/dv/normal/sport/sport_dv_normal_shoked.png")
    image dv scared sport flt  = getSprite("mods/TFT/image/sprites/dv/normal/sport/sport_dv_normal_scared.png")
    image dv cry sport flt  = getSprite("mods/TFT/image/sprites/dv/normal/sport/sport_dv_normal_cry.png")
    image dv surprise sport flt  = getSprite("mods/TFT/image/sprites/dv/normal/sport/sport_dv_normal_surprise.png")
    image dv surprise2 sport flt = getSprite("mods/TFT/image/sprites/dv/normal/sport/sport_dv_normal_surprise2.png")
    image dv grin sport flt = getSprite("mods/TFT/image/sprites/dv/normal/sport/sport_dv_normal_grin.png")
    image dv guilty sport flt = getSprite("mods/TFT/image/sprites/dv/normal/sport/sport_dv_normal_guilty.png")
    image dv sad sport flt = getSprite("mods/TFT/image/sprites/dv/normal/sport/sport_dv_normal_sad.png")
    image dv shy sport flt = getSprite("mods/TFT/image/sprites/dv/normal/sport/sport_dv_normal_shy.png")
    
    # Alisa sport wear far:
    image dv angry sport far flt = getSprite("mods/TFT/image/sprites/dv/far/sport/sport_dv_angry.png")
    image dv rage sport far flt = getSprite("mods/TFT/image/sprites/dv/far/sport/sport_dv_rage.png")
    image dv surprise sport far flt = getSprite("mods/TFT/image/sprites/dv/far/sport/sport_dv_surprise.png")
    image sport_dv_far_grin flt = getSprite("mods/TFT/image/sprites/dv/far/sport/sport_dv_grin.png")
    
    # Alisa underwear:
    image dv shy swim flt = getSprite("mods/TFT/image/sprites/dv/normal/swim/swim_dv_shy.png")
    image dv sadsmile swim flt = getSprite("mods/TFT/image/sprites/dv/normal/swim/swim_dv_sadsmile.png")
    image dv sad swim flt = getSprite("mods/TFT/image/sprites/dv/normal/swim/swim_dv_sad.png")
    image dv shy swim far flt = getSprite("mods/TFT/image/sprites/dv/normal/swim/swim_dv_laugh_far.png")
    image dv shy skirt flt = getSprite("mods/TFT/image/sprites/dv/normal/swim/skirt_dv_shy.png")
    
    # Alisa wet pioneer:
    image dv angry wet flt = getSprite("mods/TFT/image/sprites/dv/normal/wet/wet_dv_angry_rain.png")
    image dv cry wet flt = getSprite("mods/TFT/image/sprites/dv/normal/wet/wet_dv_cry_rain.png")
    image dv laugh wet flt = getSprite("mods/TFT/image/sprites/dv/normal/wet/wet_dv_laugh_rain.png")
    image dv normal wet flt = getSprite("mods/TFT/image/sprites/dv/normal/wet/wet_dv_normal_rain.png")
    image dv rage wet flt = getSprite("mods/TFT/image/sprites/dv/normal/wet/wet_dv_rage_rain.png")
    image dv sad wet flt = getSprite("mods/TFT/image/sprites/dv/normal/wet/wet_dv_sad_rain.png")
    image dv shy wet flt = getSprite("mods/TFT/image/sprites/dv/normal/wet/wet_dv_shy_rain.png")
    image dv surprise wet flt = getSprite("mods/TFT/image/sprites/dv/normal/wet/wet_dv_surprise_rain.png")
    
    # Аlisa pioneer:
    image dv smile pioneer close flt = getSprite("mods/TFT/image/sprites/dv/close/pioneer/pioneer_dv_smile3.png")
    image dv smile2 pioneer close flt = getSprite("mods/TFT/image/sprites/dv/close/pioneer/pioneer_dv_smile4.png")
    image dv smile3 pioneer close flt = getSprite("mods/TFT/image/sprites/dv/close/pioneer/pioneer_dv_smile5.png")
    image dv smile4 pioneer flt = getSprite("mods/TFT/image/sprites/dv/normal/pioneer/pioneer_dv_smile6.png")
    image dv smile5 pioneer flt = getSprite("mods/TFT/image/sprites/dv/normal/pioneer/pioneer_dv_smile7.png")
    image dv grin pioneer flt = getSprite("mods/TFT/image/sprites/dv/normal/pioneer/pioneer_dv_grin.png")
    image dv surprise2 pioneer close flt  = getSprite("mods/TFT/image/sprites/dv/close/pioneer/pioneer_dv_surprise2.png")
    image dv surprise pioneer2 flt = getSprite("mods/TFT/image/sprites/dv/normal/pioneer/pioneer_dv_surprise.png")
    image dv thinking pioneer flt = getSprite("mods/TFT/image/sprites/dv/normal/pioneer/pioneer_dv_thinking.png")
    image dv thinking2 pioneer close flt = getSprite("mods/TFT/image/sprites/dv/close/pioneer/pioneer_dv_think.png")
    image dv shy2 pioneer close flt = getSprite("mods/TFT/image/sprites/dv/close/pioneer/pioneer_dv_shy2.png")
    image dv scared1 pioneer flt = getSprite("mods/TFT/image/sprites/dv/normal/pioneer/pioneer_dv_scared1.png")
    
    # Alisa pioneer style:
    image dv heart pioneer2 far flt = getSprite("mods/TFT/image/sprites/dv/far/pioneer2/pioneer2_dv_heart.png")
    image dv sad2 pioneer2 flt = getSprite("mods/TFT/image/sprites/dv/normal/pioneer2/pioneer2_dv_sad2.png")
    image dv guilty pioneer2 flt = getSprite("mods/TFT/image/sprites/dv/normal/pioneer2/pioneer2_dv_guilty.png")
    image dv scared pioneer2 flt = getSprite("mods/TFT/image/sprites/dv/normal/pioneer2/pioneer2_dv_scared.png")
    image dv smile pioneer2 flt = getSprite("mods/TFT/image/sprites/dv/normal/pioneer2/pioneer2_dv_smile.png")
    image dv smile2 pioneer2 flt = getSprite("mods/TFT/image/sprites/dv/normal/pioneer2/pioneer2_dv_smile2.png")
    image dv surprise pioneer2 flt = getSprite("mods/TFT/image/sprites/dv/normal/pioneer2/pioneer2_dv_surprise.png")
    image dv surprise2 pioneer2 flt = getSprite("mods/TFT/image/sprites/dv/normal/pioneer2/pioneer2_dv_surprise2.png")
    image dv shoked pioneer2 flt = getSprite("mods/TFT/image/sprites/dv/normal/pioneer2/pioneer2_dv_shoked.png")
    image dv shoked2 pioneer2 flt = getSprite("mods/TFT/image/sprites/dv/normal/pioneer2/pioneer2_dv_shoked2.png")
    image dv shy pioneer2 flt = getSprite("mods/TFT/image/sprites/dv/normal/pioneer2/pioneer2_dv_shy.png")
    image dv grin pioneer2 flt = getSprite("mods/TFT/image/sprites/dv/normal/pioneer2/pioneer2_dv_grin.png")
    image dv angry pioneer2 flt = getSprite("mods/TFT/image/sprites/dv/normal/pioneer2/pioneer2_dv_angry.png")
    image dv rage pioneer2 flt = getSprite("mods/TFT/image/sprites/dv/normal/pioneer2/pioneer2_dv_rage.png")
    image dv normal pioneer2 flt = getSprite("mods/TFT/image/sprites/dv/normal/pioneer2/pioneer2_dv_normal.png")

    # Arseniy pioneer:
    image ars_angry = getSprite("mods/TFT/image/sprites/ars/pioneer/ars_angry.png")
    image ars_angry2 = getSprite("mods/TFT/image/sprites/ars/pioneer/ars_angry2.png")
    image ars_normal = getSprite("mods/TFT/image/sprites/ars/pioneer/ars_normal.png")
    image ars_normal2 = getSprite("mods/TFT/image/sprites/ars/pioneer/ars_normal2.png")
    image ars_smile = getSprite("mods/TFT/image/sprites/ars/pioneer/ars_smile.png")
    image ars_smile2 = getSprite("mods/TFT/image/sprites/ars/pioneer/ars_smile2.png")
    image ars_smile3 = getSprite("mods/TFT/image/sprites/ars/pioneer/ars_smile3.png")
    image ars_smile4 = getSprite("mods/TFT/image/sprites/ars/pioneer/ars_smile4.png")
    image ars_surprise = getSprite("mods/TFT/image/sprites/ars/pioneer/ars_surprise.png")
    image ars_surprise2 = getSprite("mods/TFT/image/sprites/ars/pioneer/ars_surprise2.png")
    image ars_think = getSprite("mods/TFT/image/sprites/ars/pioneer/ars_think.png")
    image ars_think2 = getSprite("mods/TFT/image/sprites/ars/pioneer/ars_think2.png")
    
    # Arseniy coat:
    image coat_ars_angry = getSprite("mods/TFT/image/sprites/ars/coat/coat_ars_angry.png")
    image coat_ars_normal = getSprite("mods/TFT/image/sprites/ars/coat/coat_ars_normal.png")
    image coat_ars_smile = getSprite("mods/TFT/image/sprites/ars/coat/coat_ars_smile.png")
    
    # Alisa coat:
    image coat_dv_normal = getSprite("mods/TFT/image/sprites/dv/normal/coat/coat_dv_normal.png")
    image coat_dv_surprise = getSprite("mods/TFT/image/sprites/dv/normal/coat/coat_dv_surprise.png")
    
    # Alisa sleep wear:
    image sleep_dv_shy = getSprite("mods/TFT/image/sprites/dv/far/sleep/sleep_dv_shy.png")
    
    # Uliana pioneer:
    image spina_us = getSprite("mods/TFT/image/sprites/us/spina_us.png")
    
    # Miku pioneer:
    image spina_mi = getSprite("mods/TFT/image/sprites/mi/spina_mi.png")
    image miku_ruki = getSprite("mods/TFT/image/sprites/mi/miku_ruki.png")
    
    # Cook:
    image cook_laugh = getSprite("mods/TFT/image/sprites/nt/nt_1_cook.png")
    image cook_smile = getSprite("mods/TFT/image/sprites/nt/nt_2_cook.png")
    image cook_normal = getSprite("mods/TFT/image/sprites/nt/nt_3_cook.png")
    image cook_sad = getSprite("mods/TFT/image/sprites/nt/nt_4_cook.png")
    
    # Pioneer coat:
    image coat_pi = getSprite("mods/TFT/image/sprites/pi/coat_pi.png")
    
    # Chairs:
    image chair = getSprite("mods/TFT/image/sprites/misc/chair.png")
    image chair2 = getSprite("mods/TFT/image/sprites/misc/chair2.png")

    # other
    image aftertwohour = getSprite("mods/TFT/image/screens/other/aftertwohour.png")
    image day3 = getSprite("mods/TFT/image/screens/other/day3.png")
    image white_screen = getSprite("mods/TFT/image/screens/white_screen.png")

    #qte:
    image tft_qte_anim_button:
        "mods/TFT/image/screens/qte_buttons/qte_button1.png"
        0.2
        "mods/TFT/image/screens/qte_buttons/qte_button2.png"
        0.2
        repeat

    screen tft_menu: 
        imagebutton:
            xalign 0.95 yalign 0.90
            auto "mods/TFT/image/screens/menu/tft_start_%s.png"
            action Jump ("tft_prolog")

        imagebutton:
            xalign 0.50 yalign 0.90
            auto "mods/TFT/image/screens/menu/tft_tracklist_%s.png"
            action Jump ("tft_menu_tracklist")

        imagebutton:
            xalign 0.05 yalign 0.90
            auto "mods/TFT/image/screens/menu/tft_exit_%s.png"
            action Jump ("tft_menu_exit")

    screen tft_tracklist:
        imagebutton:
            xalign 0.05 yalign 0.90
            auto "mods/TFT/image/screens/menu/tft_back_%s.png"
            action Jump ("tft_menu_plus")

