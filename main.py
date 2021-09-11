import wrap

wrap.add_sprite_dir("sprites")
wrap.world.create_world(1930, 1000)
wrap.world.set_back_image("pytrwqHL/нет.jpg")

# солдаты
coldats = []

score = 100
take = False

green_bar = wrap.sprite.add("DECORATORS", 755, 1050, "green_bar")
radius_war_1 = wrap.sprite.add("DECORATORS", 960, 840, "radius", False)
radius_war_2 = wrap.sprite.add("DECORATORS", 985, 274, "radius", False)
radius = wrap.sprite.add("DECORATORS", 345, 123, "radius", False)
place_gun = wrap.sprite.add("DECORATORS", 960, 840, "place_gun")
place_gun2 = wrap.sprite.add("DECORATORS", 985, 274, "place_gun")
castle = wrap.sprite.add("DECORATORS", 1125, 80)
gun = wrap.sprite.add("gun", 500, 110)
wrap.sprite.set_angle(gun, 139)
gun_war1 = wrap.sprite.add("gun", 500, 110, visible=False)
wrap.sprite.set_angle(gun_war1, 139)
gun_war2 = wrap.sprite.add("gun", 500, 110, visible=False)
wrap.sprite.set_angle(gun_war2, 139)

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


@wrap.on_mouse_move
def mouse(pos_x, pos_y):
    wrap.world.set_title("X: " + str(pos_x) + " Y: " + str(pos_y))

    if take:
        wrap.sprite.move_to(gun, pos_x, pos_y)
        wrap.sprite.hide(radius)
        one = wrap.sprite.is_collide_sprite(gun, place_gun)
        pos1place = wrap.sprite.get_pos(place_gun)
        if one:
            wrap.sprite.move_to(radius, pos1place[0], pos1place[1])
            wrap.sprite.move_to(gun, pos1place[0], pos1place[1])
            wrap.sprite.show(radius)

        one = wrap.sprite.is_collide_sprite(gun, place_gun2)
        pos2place = wrap.sprite.get_pos(place_gun2)
        if one:
            wrap.sprite.move_to(radius, pos2place[0], pos2place[1])
            wrap.sprite.move_to(gun, pos2place[0], pos2place[1])
            wrap.sprite.show(radius)


@wrap.on_mouse_down(wrap.BUTTON_LEFT)
def install(keys, pos_x, pos_y):
    global take

    one = wrap.sprite.is_collide_sprite(gun, place_gun)
    if take and one:
        pos1place = wrap.sprite.get_pos(place_gun)
        wrap.sprite.move_to(gun, 500, 110)
        wrap.sprite.show(gun_war1)
        wrap.sprite.hide(radius)
        wrap.sprite.move_to(gun_war1, pos1place[0], pos1place[1])
        take = False

    one = wrap.sprite.is_collide_sprite(gun, place_gun2)
    if take and one:
        pos2place = wrap.sprite.get_pos(place_gun2)
        wrap.sprite.move_to(gun, 500, 110)
        wrap.sprite.show(gun_war2)
        wrap.sprite.hide(radius)
        wrap.sprite.move_to(gun_war2, pos2place[0], pos2place[1])
        take = False

    # возращение раб.пушки в магазин
    two = wrap.sprite.is_collide_point(gun_war2, pos_x, pos_y)
    if wrap.K_q in keys and two:
        wrap.sprite.hide(gun_war2)
        wrap.sprite.move_to(gun_war2, 500, 110)

    one = wrap.sprite.is_collide_point(gun_war1, pos_x, pos_y)
    if wrap.K_q in keys and one:
        wrap.sprite.hide(gun_war1)
        wrap.sprite.move_to(gun_war1, 500, 110)


@wrap.always(5000)
def coldatss():
    global green_bar
    coldat = wrap.sprite.add("coldat", 755, 1050)
    green_bar = wrap.sprite.add("DECORATORS", 755, 1050, "green_bar")
    wrap.sprite.set_angle(coldat, 28)
    c = {"id": coldat, "hp_bar": green_bar}
    coldats.append(c)


@wrap.always(40)
def move():
    global scorecastle, score
    for a in coldats:
        wrap.sprite.move_at_angle_dir(a["id"], 5)
        point = wrap.sprite.is_collide_point(a["id"], 1002, 502)
        if point:
            wrap.sprite.set_angle(a["id"], 40)
        point = wrap.sprite.is_collide_point(a["id"], 1102, 335)
        if point:
            wrap.sprite.set_angle(a["id"], 0)
        xcoldat=wrap.sprite.get_x(a["id"])
        ycoldat = wrap.sprite.get_top(a["id"])
        wrap.sprite.move_to(a["hp_bar"],xcoldat,ycoldat)
        castlecollide = wrap.sprite.is_collide_sprite(a["id"], castle)
        if castlecollide:
            score -= 1
            if score <= 0:
                game = wrap.sprite.add_text(str("WASTED"), 900, 400, text_color=[255, 207, 0], font_size=400)
                exit()
            wrap.sprite_text.set_text(scorecastle, str(score))
            wrap.sprite.remove(a["id"])
            wrap.sprite.remove(a["hp_bar"])
            coldats.remove(a)

    # radius_true = wrap.sprite.is_collide_any_sprite(radius_war_1, coldats)
    # if radius_true != None:
    #     pos_coldat = wrap.sprite.get_pos(radius_true)
    #     wrap.sprite.set_angle_to_point(gun_war1, pos_coldat[0], pos_coldat[1])
    #
    # radius_true = wrap.sprite.is_collide_any_sprite(radius_war_2, coldats)
    # if radius_true != None:
    #     pos_coldat = wrap.sprite.get_pos(radius_true)
    #     wrap.sprite.set_angle_to_point(gun_war2, pos_coldat[0], pos_coldat[1])


a = []
b = {"name": "boris", "age": 21, "age2": 2000}
a.append(b)
b = {"name": "boris", "age": 22, "age2": 2000}
a.append(b)
b = {"name": "boris", "age": 23, "age2": 2000}
a.append(b)

print(b["name"])
c = 7
c += 1

for q in a:
    q["age2"] = 2000 - q["age"]

for c in a:
    print(c["age"])
    c["age"] += 1
