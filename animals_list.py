__list_of_animals = []


def get_list():
    return __list_of_animals


def get_obj_of_index(index):
    return __list_of_animals[index]


def add_to_list(who: object):
    return get_list().append(who)


def print_list():
    for i in get_list():
        print(i)
