#БЫСТРЫЕ ПУТИ
init -100 python:
    default_tft_path = "mods/tft/materials/"
    tft_sprite_path = "mods/tft/materials/sprites/"

#КОМАНДА ДЛЯ БЫСТРЫХ ПУТЕЙ
init -99 python:
    def getFile(file):
        return default_tft_path + file

#РАНДОМ
init -98 python:
    def TFTgetRandomItem(items):
        num = renpy.random.randint(0, len(items)-1)
        return items[num]  
    def TFTgetRandomButton():
        return TFTgetRandomItem(['a','x','f','h','y','r','t','e'])

#ШРИФТЫ
init -97 python:
    furore = getFile("fonts/furore.ttf")
    montserrat = getFile("fonts/montserrat_extralight.ttf")
    cinzel_bold = getFile("fonts/cinzel_bold.ttf")

#МУЗЫКАЛЬНЫЕ КАНАЛЫ
init python:
    renpy.music.register_channel("sfx_2",loop=False)
    renpy.music.register_channel("sfx_3",loop=False)

#ПЕРЕМЕННЫЕ
init:
    define config.developer = True
    $ mods["tft_menu_main"]=u"{font=[montserrat]}Пионерия"
    $ day0_drunk =  False
    $ day3_valleyball_nicepunch = False
    $ day4_cig = False
    $ tft_qte_loose = False
    $ tft_qte2_loose = False
    $ tft_qte_count = 0
    $ tft_qte2_count = 0

#ПЕРСОНАЖИ:
    $ dns = Character (u'Семён', color = "#a7c575", what_color = "E2C778")
    $ ars = Character (u'Арсений', color = "#de6868", what_color = "E2C778")
    $ fan = Character (u'Поклонник', color = "#7e79b5", what_color = "E2C778")
    $ pvr = Character (u'Повар', color = "#4170fd", what_color = "E2C778")
    $ mar = Character (u'Мария', color = "#4170fd", what_color = "E2C778")
    $ muz = Character (u'Музыкант', color = "#440475", what_color = "E2C778")
    $ muzs = Character (u'Музыканты', color = "#440475", what_color = "E2C778")
    $ ded = Character (u'Дядя Петя', color = "#fbff00", what_color = "E2C778")
    $ msh = Character (u'Маша', color = "#4d06bf", what_color = "E2C778")

#ШАГИ
    transform stepping_tft:
        anchor (0.0, 0.0) pos (0.0, 0.0)
        linear 0.5 pos (-5, -5)
        linear 0.5 pos (0, 0)
        linear 0.5 pos (5, -5)
        linear 0.5 pos (0, 0)
        repeat

#БЕГ
    transform running_tft:
        anchor (0.0, 0.0) pos (0.0, 0.0)
        linear 0.2 pos (-5, -5)
        linear 0.2 pos (0, 0)
        linear 0.2 pos (5, -5)
        linear 0.2 pos (0, 0)
        repeat

#ВСТРЯСКА
    transform headshaking_tft:
        anchor (0.0, 0.0) pos (0.0, 0.0)
        linear 0.08 pos (-7, 0)
        linear 0.08 pos (0, 0)
        linear 0.08 pos (7, 0)
        linear 0.08 pos (0, 0)