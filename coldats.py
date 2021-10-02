import wrap



def remove(coldat):

    wrap.sprite.remove(coldat["id"])
    wrap.sprite.remove(coldat["hp_bar"])




def add_coldat():

    coldat = wrap.sprite.add("coldat", 755, 550)

    green_bar = wrap.sprite.add("DECORATORS", 755, 550, "green_bar")
    wrap.sprite.set_angle(coldat, 28)
    c = {"id": coldat, "hp_bar": green_bar}

    return c

def move_angle_dir(dict_coldat,distance):
    wrap.sprite.move_at_angle_dir(dict_coldat["id"], distance)
    wrap.sprite.move_at_angle_dir(dict_coldat["hp_bar"], distance)