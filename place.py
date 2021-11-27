import wrap,guns






def create(x,y):
    place_gun = wrap.sprite.add("DECORATORS",x,y,"place_gun")

    lol={"id":place_gun,"zanat":False}

    return lol


def mogu_postavit_gun(place,gun):
    if place["zanat"]:
        return False
    one = wrap.sprite.is_collide_sprite(gun, place["id"])

    return one


def premerka(gun,radius,place_gun):
    pos1place = wrap.sprite.get_pos(place_gun["id"])
    guns.move_gun(gun, radius, pos1place[0], pos1place[1])
    wrap.sprite.show(radius)


def place_gun_id(place_gun):
    place_gun_id=place_gun["id"]

    return place_gun_id


def install_gun_on_place(place_gun,gun_war1,radius_war_1):
    pos1place = wrap.sprite.get_pos(place_gun["id"])
    wrap.sprite.show(gun_war1)
    guns.move_gun(gun_war1, radius_war_1, pos1place[0], pos1place[1])
    place_gun["zanat"]=True







