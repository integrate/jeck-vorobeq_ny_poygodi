import wrap, guns, coldats as mod_coldats, time, ochered, place

wrap.add_sprite_dir("sprites")
wrap.world.create_world(1930, 1000)
wrap.world.set_back_image("pytrwqHL/нет.jpg")

# солдаты
coldats = []

score = 100
take = False

row = []
row.append(ochered.add_row(1900, 100, "mario-scenery", "cloud2"))
row.append(ochered.add_row(6000, 70, "mario-scenery", "cloud2"))
row.append(ochered.add_row(900, 50, "mario-scenery", "cloud2"))
row.append(ochered.add_row(600, 50, "mario-scenery", "cloud2"))
ime = time.time()
place_gun = place.create(950, 204)
castle = wrap.sprite.add("DECORATORS", 1125, 80)
gun, radius = guns.add_gun(120, 20, 145, True)

gun_war1, radius_war_1 = guns.add_gun(96, 0, 213, False)
gun_war2, radius_war_2 = guns.add_gun(98, 1, 213, False)

scorecastle = wrap.sprite.add_text(str(score), 50, 20, text_color=[255, 207, 0], font_size=40)


@wrap.on_mouse_down
def took(pos_x, pos_y):
    global take
    magazin = wrap.sprite.is_collide_point(gun, pos_x, pos_y)

    if magazin:
        take = True


@wrap.on_key_down(wrap.K_q)
def Q():
    global take
    take = False
    wrap.sprite.move_to(gun, 500, 110)
    wrap.sprite.hide(radius)


# радиус и установка пушки
@wrap.on_mouse_move
def mouse(pos_x, pos_y):
    wrap.world.set_title("X: " + str(pos_x) + " Y: " + str(pos_y))

    if take:
        guns.move_gun(gun, radius, pos_x, pos_y)
        wrap.sprite.hide(radius)

        if place.mogu_postavit_gun(place_gun, gun):
            place.premerka(gun, radius, place_gun)


@wrap.on_mouse_down(wrap.BUTTON_LEFT)
def install(keys, pos_x, pos_y):
    global take

    if take and place.mogu_postavit_gun(place_gun, gun):
        place.install_gun_on_place(place_gun,gun_war1,radius_war_1)
        guns.move_gun(gun, radius, 500, 110)
        wrap.sprite.hide(radius)
        take = False

    # возращение раб.пушки в магазин
    two = wrap.sprite.is_collide_point(gun_war2, pos_x, pos_y)
    if wrap.K_q in keys and two:
        wrap.sprite.hide(gun_war2)
        guns.move_gun(gun_war2, radius_war_2, 500, 110)

    one = wrap.sprite.is_collide_point(gun_war1, pos_x, pos_y)
    if wrap.K_q in keys and one:
        wrap.sprite.hide(gun_war1)
        guns.move_gun(gun_war1, radius_war_1, 500, 110)


@wrap.always(100)
def coldatss():
    qtime = int((time.time() - ime) * 1000)
    for g in row:
        if g["time"] <= qtime:
            c = ochered.add_coldat(g)
            coldats.append(c)
            row.remove(g)


@wrap.always(40)
def move():
    global scorecastle, score
    for a in coldats:
        if a["hp"] <= 0:
            mod_coldats.remove(a)
            coldats.remove(a)
            continue
        mod_coldats.move_angle_dir(a, 5)

        point = wrap.sprite.is_collide_point(a["id"], 1002, 502)
        if point:
            wrap.sprite.set_angle(a["id"], 40)
        point = wrap.sprite.is_collide_point(a["id"], 1102, 335)
        if point:
            wrap.sprite.set_angle(a["id"], 0)

        castlecollide = wrap.sprite.is_collide_sprite(a["id"], castle)
        if castlecollide:
            score -= 1
            if score <= 0:
                game = wrap.sprite.add_text(str("WASTED"), 900, 400, text_color=[255, 207, 0], font_size=400)
                exit()
            wrap.sprite_text.set_text(scorecastle, str(score))
            mod_coldats.remove(a)
            coldats.remove(a)

    b = []
    for s in coldats:
        b.append(s["id"])
    guns.set_angle_gun(radius_war_1, gun_war1, coldats)

    guns.set_angle_gun(radius_war_2, gun_war2, coldats)
