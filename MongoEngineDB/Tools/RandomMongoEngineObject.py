from random import choice


def get_random(object_type, quantity=1):
    rand_list = []
    id_list = object_type.objects.only('id')
    for _ in range(quantity):
        dish_id = choice(id_list)['id']
        rand_list.append(object_type.objects(id=dish_id).next())
    return rand_list