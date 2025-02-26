import wrap


def remove(coldat):
    wrap.sprite.remove(coldat["id"])
    wrap.sprite.remove(coldat["hp_bar"])
    wrap.sprite.remove(coldat["red_bar"])


def add_coldat(hp=50, costum="coldat", sprite="coldat"):
    coldat = wrap.sprite.add(sprite, int(755/1.5), int(1050/1.5), costum)
    red_bar = wrap.sprite.add("DECORATORS", int(755/1.5), int(1050/1.5), "red_bar")
    green_bar = wrap.sprite.add("DECORATORS", int(755/1.5), int(1050/1.5), "green_bar")
    wrap.sprite.set_angle(coldat, 28)

    c = {"id": coldat, "hp_bar": green_bar, "red_bar": red_bar, "hp": hp, "full_hp": hp}

    return c


def move_angle_dir(dict_coldat, distance):
    wrap.sprite.move_at_angle_dir(dict_coldat["id"], distance)

    xcoldat = wrap.sprite.get_x(dict_coldat["id"])
    ycoldat = wrap.sprite.get_top(dict_coldat["id"])
    wrap.sprite.move_to(dict_coldat["red_bar"], xcoldat, ycoldat)
    xleftred = wrap.sprite.get_left(dict_coldat["red_bar"])
    centre = wrap.sprite.get_centery(dict_coldat["red_bar"])

    wrap.sprite.move_left_to(dict_coldat["hp_bar"], xleftred)
    wrap.sprite.move_centery_to(dict_coldat["hp_bar"], centre)


def kick(dict_coldat):
    dict_coldat["hp"] -= 1
    proc1 = dict_coldat["full_hp"] / 100
    currentproc = dict_coldat["hp"] / proc1
    wrap.sprite.set_width(dict_coldat["hp_bar"], int(currentproc/1.5))
