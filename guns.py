import wrap,coldats as mod_coldats


def add_gun(pos_x, pos_y, angle_gun, visible):
    radius = wrap.sprite.add("DECORATORS", pos_x, pos_y, "radius", False)
    gun = wrap.sprite.add("gun", pos_x, pos_y, visible=visible)
    wrap.sprite.set_angle(gun, angle_gun)

    return [gun, radius]


def move_gun(gun_id, radius_id, pos_x, pos_y):
    """
    двигает пушку на указаные координаты

    :param gun_id:
    :param radius_id:
    :param pos_x:
    :param pos_y:
    :return:
    """
    wrap.sprite.move_to(gun_id, pos_x, pos_y)
    wrap.sprite.move_to(radius_id, pos_x, pos_y)


def set_angle_gun(radius_war, gun_war,dict_coldats):
    b = []
    for s in dict_coldats:
        b.append(s["id"])
    coldat_id = wrap.sprite.is_collide_any_sprite(radius_war, b)
    if coldat_id == None:
        return
    pos_coldat = wrap.sprite.get_pos(coldat_id)
    wrap.sprite.set_angle_to_point(gun_war, pos_coldat[0], pos_coldat[1])
    for s in dict_coldats:
        if s["id"] == coldat_id:
            mod_coldats.kick(s)