def get_menu():
    print('1: Показать список всех животных\n'
          '2: Обучить животное новым функциям\n'
          '3: Показать к какому классу относится животное\n'
          '4: Список команд у животного\n'
          '5: Добавить животное'
          '0: Выход')


def upgrade_command(who: object, command: str):
    who.add_function(command)


def get_class(who: object):
    return type(who)


def get_command(who: object):
    return who.function
