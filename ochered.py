import coldats


def add_row(time, hp, sprite, costym):
    t = {"time": time, "hp": hp, "sprite": sprite, "costum": costym}

    return t


def add_coldat(row_el):
    c = coldats.add_coldat(row_el["hp"], row_el["costum"], row_el["sprite"])

    return c
