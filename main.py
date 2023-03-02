import wrap, guns, coldats as mod_coldats, time, ochered, place

wrap.add_sprite_dir("sprites")
wrap.world.create_world(int(1900/1.5), int(1000/1.5))
wrap.world.set_back_image("pytrwqHL/нет.jpg")

# солдаты
coldats = []

score = 1
take = False

row = []
row.append(ochered.add_row(1900, 60, "coldat", "coldat"))
row.append(ochered.add_row(6000, 200, "coldat", "tank"))
row.append(ochered.add_row(900, 50, "coldat", "coldat"))
row.append(ochered.add_row(600, 50, "coldat", "coldat"))

row.append(ochered.add_row(11900, 60, "coldat", "coldat"))
row.append(ochered.add_row(16000, 200, "coldat", "tank"))
row.append(ochered.add_row(10900, 50, "coldat", "coldat"))
row.append(ochered.add_row(10600, 50, "coldat", "coldat"))

row.append(ochered.add_row(21900, 60, "coldat", "coldat"))
row.append(ochered.add_row(26000, 200, "coldat", "tank"))
row.append(ochered.add_row(20900, 50, "coldat", "coldat"))
row.append(ochered.add_row(20600, 50, "coldat", "coldat"))
ime = time.time()
place_gun = place.create(int(950/1.5), int(204/1.5))
place_gun2 = place.create(int(1034/1.5), int(675/1.5))
castle = wrap.sprite.add("DECORATORS", int(1125/1.5), int(80/1.5))
gun, radius = guns.add_gun(int(500/1.5), int(110/1.5), 145, True)

gun_war1, radius_war_1 = guns.add_gun(int(96/1.5), 0, 213, False)
gun_war2, radius_war_2 = guns.add_gun(int(98/1.5), 1, 213, False)

scorecastle = wrap.sprite.add_text(str(score), int(50/1.5), int(20/1.5), text_color=[255, 207, 0], font_size=int(40/1.5))


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
    wrap.sprite.move_to(gun, int(500/1.5), int(110/1.5))
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
        if place.mogu_postavit_gun(place_gun2, gun):
            place.premerka(gun, radius, place_gun2)


@wrap.on_mouse_down(wrap.BUTTON_LEFT)
def install(keys, pos_x, pos_y):
    global take

    if take and place.mogu_postavit_gun(place_gun, gun):
        place.install_gun_on_place(place_gun, gun_war1, radius_war_1)
        guns.move_gun(gun, radius, int(500/1.5), int(110/1.5))
        wrap.sprite.hide(radius)
        take = False

    if take and place.mogu_postavit_gun(place_gun2, gun):
        place.install_gun_on_place(place_gun2, gun_war2, radius_war_2)
        guns.move_gun(gun, radius, int(500/1.5), int(110/1.5))
        wrap.sprite.hide(radius)
        take = False
    # возращение раб.пушки в магазин

    one = wrap.sprite.is_collide_point(gun_war1, pos_x, pos_y)
    if wrap.K_q in keys and one:
        place.delete_gun(place_gun)

        wrap.sprite.hide(gun_war1)
        guns.move_gun(gun_war1, radius_war_1, int(500/1.5), int(110/1.5))
    one = wrap.sprite.is_collide_point(gun_war2, pos_x, pos_y)
    if wrap.K_q in keys and one:
        place.delete_gun(place_gun2)
        wrap.sprite.hide(gun_war2)
        guns.move_gun(gun_war2, radius_war_2, int(500/1.5), int(110/1.5))


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

        point = wrap.sprite.is_collide_point(a["id"], int(1002/1.5), int(502/1.5))
        if point:
            wrap.sprite.set_angle(a["id"], 40)
        point = wrap.sprite.is_collide_point(a["id"], int(1102/1.5), int(335/1.5))
        if point:
            wrap.sprite.set_angle(a["id"], 0)

        castlecollide = wrap.sprite.is_collide_sprite(a["id"], castle)
        if castlecollide:
            score -= 1
            if score <= 0:
                game = wrap.sprite.add_text(str("WASTED"), int(900/1.5), int(400/1.5), text_color=[255, 207, 0], font_size=int(400/1.5))
                exit()
            wrap.sprite_text.set_text(scorecastle, str(score))
            mod_coldats.remove(a)
            coldats.remove(a)

    b = []
    for s in coldats:
        b.append(s["id"])
    guns.set_angle_gun(radius_war_1, gun_war1, coldats)

    guns.set_angle_gun(radius_war_2, gun_war2, coldats)
