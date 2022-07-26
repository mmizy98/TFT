init -99 python:
  def getSprite(FilePath):
    return ConditionSwitch(
      "persistent.sprite_time=='day'", im.MatrixColor( FilePath, im.matrix.tint(0.83, 0.88, 0.92)),
      "persistent.sprite_time=='sunset'", im.MatrixColor(FilePath, im.matrix.tint(0.94, 0.82, 1.0)),
      "persistent.sprite_time=='night'", im.MatrixColor(FilePath, im.matrix.tint(0.63, 0.78, 0.82)))

init:
    define config.developer = True
    $ mods["estr_TFOTprolog"]=u"Страх, Любовь и Слёзы"

    $ day1_vzlom = False
    $ day0_drunk =  False

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
        
# Characters:

    # Denis:
    $ dns = Character (u'Денис', color = "#a7c575", what_color = "E2C778")
  
    # Cook:
    $ pvr = Character (u'Повар', color = "#4170fd", what_color = "E2C778")
    $ mar = Character (u'Мария', color = "#4170fd", what_color = "E2C778")

    # Музыканты
    $ muz = Character (u'Музыкант', color = "#440475", what_color = "E2C778")
    $ muzs = Character (u'Музыканты', color = "#440475", what_color = "E2C778")

    # Фанат
    $ fan = Character (u'Поклонник', color = "#7e79b5", what_color = "E2C778")
    
# Sounds:

    # Music:
    $ greenday = "images/sound/music/greenday.mp3"

    $ hyperborea = "images/sound/music/hyperborea.mp3"

    $ sizor = "images/sound/music/sizor.mp3"

    $ kostr = "images/sound/music/vzveiteskostrami.mp3"

    $ plastinki = "images/sound/music/plastinki.ogg"

    $ unbroken = "images/sound/music/Unbroken.mp3"

    $ prologmusic = "images/sound/music/prologmusic.mp3"

    $ BLAD = "images/sound/music/BLAD.mp3"

    $ aprilrain = "images/sound/music/aprilrain.mp3"

    $ SP_city = "images/sound/music/SP_city.mp3"

    $ deepcosmo = "images/sound/music/deepcosmo.mp3"

    $ diapazon = "images/sound/music/diapazon.mp3"

    $ stressedoutminus = "images/sound/music/stressedoutminus.mp3"

    $ Omelchuk_Roads_Ahead = "images/sound/music/Omelchuk_Roads_Ahead.mp3"
    
    # SFX:
    $ heartbeat = "images/sound/sfx/heartbeat.mp3"

    $ avaria = "images/sound/sfx/avaria.mp3"

    $ claps = "images/sound/sfx/claps.mp3"

    $ oi = "images/sound/sfx/oi1.ogg"

    $ saray = "images/sound/sfx/saray_door1.mp3"

    $ storage = "images/sound/sfx/storage_noise.ogg"

    $ storagenoise = "images/sound/sfx/storage_noise.ogg"

    $ jimbeam = "images/sound/sfx/jimbeam.mp3"

    $ window_dining = "images/sound/sfx/window_dining.mp3"

    $ fall_bed = "images/sound/sfx/fall_onto_bed.ogg"

    $ train_honk = "images/sound/sfx/train_honk.mp3"
    
    $ clock_timeskip = "images/sound/sfx/clock_timeskip.mp3"

    $ ambience_city = "images/sound/sfx/ambience_city.mp3"

    $ clock_alert = "images/sound/sfx/clock_alert.mp3"

    $ light = "images/sound/sfx/light_on.mp3"

    $ shot = "images/sound/sfx/shot.mp3"

    $ rattle = "images/sound/sfx/rattle.mp3"

    $ resiever = "images/sound/sfx/resiever.mp3"

    $ okno = "images/sound/sfx/okno.mp3"

    $ fridge = "images/sound/sfx/fridge.mp3"

    $ liazdoor = "images/sound/sfx/liazdoor.mp3"

    $ coldsteps = "images/sound/sfx/coldsteps.mp3"

    $ train = "images/sound/sfx/train_inside.mp3"

    
# Pictures:
    
    # Alisa pics:
    image dvfire = "images/cg/dvfire.jpg"

    image dv_polyana2 = "images/cg/dv_polyana2.jpeg"

    image night_event = "images/cg/night_event.jpg"

    image d3_dv_kiss_7dl = "images/cg/d3_dv_kiss_7dl.jpg"

    image d3_dv_kiss_7dl_rev = "images/cg/d3_dv_kiss_7dl_rev.jpg"

    image dvpodnos = "images/cg/dvpodnos.jpg"

    image dvuneat = "images/cg/dvuneat.jpg"

    image dveda = "images/cg/dveda.jpg"

    image dvmushug = "images/cg/dvmushug.jpg"

    image dvcryhug = "images/cg/dvcryhug.jpg"

    image dvlovenight = "images/cg/dvlovenight.jpg"

    image hittendv = "images/cg/dv_hit.png"

    image dv_beach_sunset = "images/cg/dv_beach_sunset.jpg"

    image dv_shore = "images/cg/dv_kiss_st.png"

    image dvkissforest = "images/cg/dvkissforest.jpg"

    image dvdance = "images/cg/ss_dv_dance.jpg"

    image dvsleep = "images/cg/dvsleep.jpg"

    image dvfallangry = "images/cg/dvfallangry.jpg"

    image sexdv1 = "images/cg/sexdv1.jpg"

    image sexdv2 = "images/cg/sexdv2.jpg"

    image lovedv1 = "images/cg/lovedv1.jpg"

    image lovedv2 = "images/cg/lovedv2.jpg"

    image dvnight = "images/cg/dvnight.png"

    image sondv = "images/cg/MoV1IAs8Ufc.jpg"

    image dvhug2 = "images/cg/XrQy7tlzzFE.jpg"

    image dvmibus = "images/cg/d1_mi_dv_bus_7dl.jpg"

    image dv_thinking_close = "images/cg/dv_thinking_close.jpg"

    image dv_sleep_window = "images/cg/dv_sleep_window.jpg"

    image dv_sleep_bed = "images/cg/dv_sleep_bed.jpg"
    
    # Other:
    image food_breakfast = "images/cg/food_breakfast.png"

    image white_screen = "images/sprites/misc/white_screen.png"

    image flt_timeskip_logo1 = "images/sprites/misc/flt_timeskip_logo1.png"

    image flt_timeskip_logo2 = "images/sprites/misc/flt_timeskip_logo2.png"
    
    image volleyball = "images/cg/volleyball.png"

    image semsquore = "images/cg/semsquore.jpg"

    image slexit = "images/cg/d1_sl_exit.jpg"

    image mikufort = "images/cg/mikufort.jpg"

    image d2_wertuska_wse = "images/cg/d2_wertuska_wse.jpg"

    image mikuboat = "images/cg/mikuboat.jpg"

    image fag_room = "images/cg/d3_fag_room.jpg"

    image mi_guitar = "images/cg/mi_guitar.jpg"

    image navrat2 = "images/cg/navrat2.jpg"

    image morning_line = "images/cg/morning_line.jpg"

    image son = "images/cg/wtf_end_of_day.jpg"

    image mirror = "images/cg/semyon_mirror.jpg"

    image navrat = "images/cg/navrat.jpg"

    image sportsunset = "images/cg/ext_playground_sunset.jpg"

    image jerry = "images/cg/jerry.jpg"

    image mirror2 = "images/cg/semyon_mirror2.jpg"

# Backgrounds:
    
    # City:
    image night_bar = "images/bg/night_bar.jpg"

    image int_prolog_nightclub = "images/bg/int_prolog_nightclub.jpg"

    image ext_city_night_7dl = "images/bg/ext_city_night_7dl.jpg"

    image ext_mv2_7dl = "images/bg/ext_mv2_7dl.jpg"

    image cityhouse = "images/bg/cityhouse.jpg"

    image ext_bus_city = "images/bg/ext_bus_city.jpg"

    image windowsun = "images/bg/windowsun.jpg"

    image roommorning = "images/bg/roommorning.png"

    image kitchen2 = "images/bg/kitchen2.jpg"

    image roomwindowsun = "images/bg/int_semen_room_window_day_7dl.jpg"

    image podzd2 = "images/bg/podzd2.jpg"

    image ulica2 = "images/bg/ulica2.jpg"

    image market = "images/bg/market.png"

    image market2 = "images/bg/market2.png"

    image train = "images/bg/train.jpg"

    image vokzal = "images/bg/vokzal.jpg"

    image train2 = "images/bg/train2.jpg"

    image starbucks = "images/bg/starbucks.jpg"

    image ostanovka2 = "images/bg/ostanovka2.jpg"

    image vavtday = "images/bg/vavtday.jpg"

    image busepilogue = "images/bg/busepilogue.png"

    image roomreal = "images/bg/roomreal.jpg"

    image lift = "images/bg/lift_normal.jpg"

    image city1 = "images/bg/dct_landscape_city1.jpg"

    image city2 = "images/bg/ext_IRL_night.png"

    image ulica2 = "images/bg/ulica2.jpg"

    image park7dl = "images/bg/ext_winterpark_7dl.jpg"

    image bath = "images/bg/bath.png"

    image vavt = "images/bg/vavt.jpg"

    image ulica_day = "images/bg/ulica_day.jpg"

    image ext_bus_city = "images/bg/ext_bus_city.jpg"

    image kitchen = "images/bg/kitchen.jpg"

    image podzd = "images/bg/podzd.jpg"
    
    # Camp:
    image ext_music_club_verandah_day = "images/bg/ext_music_club_verandah_day.jpg"

    image ext_admins_night_7dl = "images/bg/ext_admins_night_7dl.jpg"

    image ext_admins_day_7dl = "images/bg/ext_admins_day_7dl.jpg"

    image int_house_of_dv_night2 = "images/bg/int_house_of_dv_night2.jpg"

    image int_staircase_7dl = "images/bg/int_staircase_7dl.jpg"

    image int_store_7dl = "images/bg/int_store_7dl.jpg"

    image ext_volley_court_7dl = "images/bg/ext_volley_court_7dl.jpg"

    image ext_houses_night = "images/bg/ext_houses_night.jpg"

    image dvhousesunset = "images/bg/dvhousesunset.jpg"

    image cssunset = "images/bg/cssunset.jpg"

    image domnight = "images/bg/domnight.jpg"

    image muznight = "images/bg/muznight.jpg"

    image dark_room = "images/bg/dark_room.jpg"

    image ss_datroom_day = "images/bg/ss_datroom_day.jpg"

    image ext_old_house_day = "images/bg/ext_old_house_day.jpg"

    image int_old_house_day = "images/bg/int_old_house_day.jpg"

    image vorota = "images/bg/vorota.png"

    image ext_beach_water_sunset = "images/bg/ext_beach_water_sunset.jpg"

    image oldrainy = "images/bg/int_old_building_day_rainy.jpg"

    image forest = "images/bg/ext_forest_day_rainy.jpg"

    image forest2 = "images/bg/ext_forest2_day_rainy.jpg"

    image int_banya_clear = "images/bg/int_banya_clear.jpg"

    image int_banya_smoke = "images/bg/int_banya_smoke.jpg"

    image stolovaya1 = "images/bg/int_stolovaya_notfull.jpg"

    image muznight2 = "images/bg/muznight2.jpg"

    image dom = "images/bg/domsemday.jpg"

    image clubsevening = "images/bg/ext_clubs_sunset.jpg"

    image domext = "images/bg/ext_hata_nru_day.jpg"

    image domextnight = "images/bg/ext_hata_nru_night.jpg"

    image domexteven = "images/bg/ext_house_of_max_sunset.jpg"

    image domeven = "images/bg/ggroomnl.png"

    image muznight3 = "images/bg/muznight3.jpg"

    image domnight = "images/bg/domnight.jpg"

    image ext_house_of_un_night = "images/bg/ext_house_of_un_night.jpg"

    image muznightinside = "images/bg/muznightinside.jpg"

    image ext_playground_sunset = "images/bg/ext_playground_sunset.jpg"

    image mikunight = "images/bg/mikunight.jpg"

    image muznightnear = "images/bg/muzhightnear.jpg"

    image buswindow = "images/bg/int_bus_window.png"

    image sov2 = "images/bg/sov2.jpg"

    image sov1 = "images/bg/sov1.jpg"

    image sov3 = "images/bg/sov3.jpg"

    image sklad_day = "images/bg/sklad_day.jpg"

    image muzinnight = "images/bg/muzinnight.jpg"

    image domintnight2 = "images/bg/domintnight2.png"

    image windowsun = "images/bg/windowsun.jpg"

    image ext_storage_day = "images/bg/ext_storage_day2.jpg"

    image ext_storage_night = "images/bg/ext_storage_night2.jpg"

    image ext_storage_day2 = "images/bg/ext_storage_day.png"

    image ext_storage_night2 = "images/bg/ext_storage_night.jpg"

    image int_warehouse_day = "images/bg/int_warehouse_day_7dl.jpg"

    image int_warehouse_day2 = "images/bg/int_warehouse_day2_7dl.jpg"

# Sprites:

    # Alisa sport wear:
    image dv angry sport flt  = getSprite("images/sprites/dv/normal/sport/sport_dv_normal_angry.png")
    image dv laugh sport flt  = getSprite("images/sprites/dv/normal/sport/sport_dv_normal_laugh.png")
    image dv smile sport flt  = getSprite("images/sprites/dv/normal/sport/sport_dv_normal_smile.png")
    image dv normal sport flt  = getSprite("images/sprites/dv/normal/sport/sport_dv_normal_normal.png")
    image dv shoked sport flt  = getSprite("images/sprites/dv/normal/sport/sport_dv_normal_shoked.png")
    image dv scared sport flt  = getSprite("images/sprites/dv/normal/sport/sport_dv_normal_scared.png")
    image dv cry sport flt  = getSprite("images/sprites/dv/normal/sport/sport_dv_normal_cry.png")
    image dv surprise sport flt  = getSprite("images/sprites/dv/normal/sport/sport_dv_normal_surprise.png")
    image dv surprise2 sport flt = getSprite("images/sprites/dv/normal/sport/sport_dv_normal_surprise2.png")
    image dv grin sport flt = getSprite("images/sprites/dv/normal/sport/sport_dv_normal_grin.png")
    image dv guilty sport flt = getSprite("images/sprites/dv/normal/sport/sport_dv_normal_guilty.png")
    image dv sad sport flt = getSprite("images/sprites/dv/normal/sport/sport_dv_normal_sad.png")
    image dv shy sport flt = getSprite("images/sprites/dv/normal/sport/sport_dv_normal_shy.png")
    
    # Alisa sport wear far:
    image dv angry sport far flt = getSprite("images/sprites/dv/far/sport/sport_dv_angry.png")
    image dv rage sport far flt = getSprite("images/sprites/dv/far/sport/sport_dv_rage.png")
    image dv surprise sport far flt = getSprite("images/sprites/dv/far/sport/sport_dv_surprise.png")
    image sport_dv_far_grin flt = getSprite("images/sprites/dv/far/sport/sport_dv_grin.png")
    
    # Alisa underwear:
    image dv shy swim flt = getSprite("images/sprites/dv/normal/swim/swim_dv_shy.png")
    image dv sadsmile swim flt = getSprite("images/sprites/dv/normal/swim/swim_dv_sadsmile.png")
    image dv sad swim flt = getSprite("images/sprites/dv/normal/swim/swim_dv_sad.png")
    image dv shy swim far flt = getSprite("images/sprites/dv/normal/swim/swim_dv_laugh_far.png")
    image dv shy skirt flt = getSprite("images/sprites/dv/normal/swim/skirt_dv_shy.png")
    
    # Alisa wet pioneer:
    image dv angry wet flt = getSprite("images/sprites/dv/normal/wet/wet_dv_angry_rain.png")
    image dv cry wet flt = getSprite("images/sprites/dv/normal/wet/wet_dv_cry_rain.png")
    image dv laugh wet flt = getSprite("images/sprites/dv/normal/wet/wet_dv_laugh_rain.png")
    image dv normal wet flt = getSprite("images/sprites/dv/normal/wet/wet_dv_normal_rain.png")
    image dv rage wet flt = getSprite("images/sprites/dv/normal/wet/wet_dv_rage_rain.png")
    image dv sad wet flt = getSprite("images/sprites/dv/normal/wet/wet_dv_sad_rain.png")
    image dv shy wet flt = getSprite("images/sprites/dv/normal/wet/wet_dv_shy_rain.png")
    image dv surprise wet flt = getSprite("images/sprites/dv/normal/wet/wet_dv_surprise_rain.png")
    
    # Аlisa pioneer:
    image dv smile pioneer close flt = getSprite("images/sprites/dv/close/pioneer/pioneer_dv_smile3.png")
    image dv smile2 pioneer close flt = getSprite("images/sprites/dv/close/pioneer/pioneer_dv_smile4.png")
    image dv smile3 pioneer close flt = getSprite("images/sprites/dv/close/pioneer/pioneer_dv_smile5.png")
    image dv smile4 pioneer flt = getSprite("images/sprites/dv/normal/pioneer/pioneer_dv_smile6.png")
    image dv smile5 pioneer flt = getSprite("images/sprites/dv/normal/pioneer/pioneer_dv_smile7.png")
    image dv grin pioneer flt = getSprite("images/sprites/dv/normal/pioneer/pioneer_dv_grin.png")
    image dv surprise2 pioneer close flt  = getSprite("images/sprites/dv/close/pioneer/pioneer_dv_surprise2.png")
    image dv surprise pioneer2 flt = getSprite("images/sprites/dv/normal/pioneer/pioneer_dv_surprise.png")
    image dv thinking pioneer flt = getSprite("images/sprites/dv/normal/pioneer/pioneer_dv_thinking.png")
    image dv thinking2 pioneer close flt = getSprite("images/sprites/dv/close/pioneer/pioneer_dv_think.png")
    image dv shy2 pioneer close flt = getSprite("images/sprites/dv/close/pioneer/pioneer_dv_shy2.png")
    image dv scared1 pioneer flt = getSprite("images/sprites/dv/normal/pioneer/pioneer_dv_scared1.png")
    
    # Alisa pioneer style:
    image dv heart pioneer2 far flt = getSprite("images/sprites/dv/far/pioneer2/pioneer2_dv_heart.png")
    image dv sad2 pioneer2 flt = getSprite("images/sprites/dv/normal/pioneer2/pioneer2_dv_sad2.png")
    image dv guilty pioneer2 flt = getSprite("images/sprites/dv/normal/pioneer2/pioneer2_dv_guilty.png")
    image dv scared pioneer2 flt = getSprite("images/sprites/dv/normal/pioneer2/pioneer2_dv_scared.png")
    image dv smile pioneer2 flt = getSprite("images/sprites/dv/normal/pioneer2/pioneer2_dv_smile.png")
    image dv smile2 pioneer2 flt = getSprite("images/sprites/dv/normal/pioneer2/pioneer2_dv_smile2.png")
    image dv surprise pioneer2 flt = getSprite("images/sprites/dv/normal/pioneer2/pioneer2_dv_surprise.png")
    image dv surprise2 pioneer2 flt = getSprite("images/sprites/dv/normal/pioneer2/pioneer2_dv_surprise2.png")
    image dv shoked pioneer2 flt = getSprite("images/sprites/dv/normal/pioneer2/pioneer2_dv_shoked.png")
    image dv shoked2 pioneer2 flt = getSprite("images/sprites/dv/normal/pioneer2/pioneer2_dv_shoked2.png")
    image dv shy pioneer2 flt = getSprite("images/sprites/dv/normal/pioneer2/pioneer2_dv_shy.png")
    image dv grin pioneer2 flt = getSprite("images/sprites/dv/normal/pioneer2/pioneer2_dv_grin.png")
    image dv angry pioneer2 flt = getSprite("images/sprites/dv/normal/pioneer2/pioneer2_dv_angry.png")
    image dv rage pioneer2 flt = getSprite("images/sprites/dv/normal/pioneer2/pioneer2_dv_rage.png")
    image dv normal pioneer2 flt = getSprite("images/sprites/dv/normal/pioneer2/pioneer2_dv_normal.png")

    # Denis pioneer:
    image dns_angry = getSprite("images/sprites/dns/pioneer/dns_angry.png")
    image dns_angry2 = getSprite("images/sprites/dns/pioneer/dns_angry2.png")
    image dns_normal = getSprite("images/sprites/dns/pioneer/dns_normal.png")
    image dns_normal2 = getSprite("images/sprites/dns/pioneer/dns_normal2.png")
    image dns_smile = getSprite("images/sprites/dns/pioneer/dns_smile.png")
    image dns_smile2 = getSprite("images/sprites/dns/pioneer/dns_smile2.png")
    image dns_smile3 = getSprite("images/sprites/dns/pioneer/dns_smile3.png")
    image dns_smile4 = getSprite("images/sprites/dns/pioneer/dns_smile4.png")
    image dns_surprise = getSprite("images/sprites/dns/pioneer/dns_surprise.png")
    image dns_surprise2 = getSprite("images/sprites/dns/pioneer/dns_surprise2.png")
    image dns_think = getSprite("images/sprites/dns/pioneer/dns_think.png")
    image dns_think2 = getSprite("images/sprites/dns/pioneer/dns_think2.png")
    
    # Denis coat:
    image coat_dns_angry = getSprite("images/sprites/dns/coat/coat_dns_angry.png")
    image coat_dns_normal = getSprite("images/sprites/dns/coat/coat_dns_normal.png")
    image coat_dns_smile = getSprite("images/sprites/dns/coat/coat_dns_smile.png")
    
    # Alisa coat:
    image coat_dv_normal = getSprite("images/sprites/dv/normal/coat/coat_dv_normal.png")
    image coat_dv_surprise = getSprite("images/sprites/dv/normal/coat/coat_dv_surprise.png")
    
    # Alisa sleep wear:
    image sleep_dv_shy = getSprite("images/sprites/dv/far/sleep/sleep_dv_shy.png")
    
    # Uliana pioneer:
    image spina_us = getSprite("images/sprites/us/spina_us.png")
    
    # Miku pioneer:
    image spina_mi = getSprite("images/sprites/mi/spina_mi.png")
    image miku_ruki = getSprite("images/sprites/mi/miku_ruki.png")
    
    # Cook:
    image cook_laugh = getSprite("images/sprites/nt/nt_1_cook.png")
    image cook_smile = getSprite("images/sprites/nt/nt_2_cook.png")
    image cook_normal = getSprite("images/sprites/nt/nt_3_cook.png")
    image cook_sad = getSprite("images/sprites/nt/nt_4_cook.png")
    
    # Pioneer coat:
    image coat_pi = getSprite("images/sprites/pi/coat_pi.png")
    
    # Chairs:
    image chair = getSprite("images/sprites/misc/chair.png")
    image chair2 = getSprite("images/sprites/misc/chair2.png")

    # 2 hours
    image aftertwohour = getSprite("images/sprites/misc/aftertwohour.png")
    
    # days
    image day3 = getSprite("images/sprites/misc/day3.png")