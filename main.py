import Menu
import animals_list
from Cat import Cat
from Dog import Dog
from Horse import Horse
from Hamster import Hamster
from Donkey import Donkey
from Camel import Camel
from counter import Counter

dog1 = Dog('qsad', '11232', ['gow', 'sleep'])

cat1 = Cat('wser', '42', 'meow')

horse1 = Horse('werher', '15', 'rabbit')

hamster1 = Hamster('wweg', '123', ['eat', 'sleep', 'wolk'])

donkey1 = Donkey('awdw', '154', 'grap baggage')

camel1 = Camel('wwef', '124', ['drink', 'eat'])

animals_list.add_to_list(dog1)
animals_list.add_to_list(cat1)
animals_list.add_to_list(horse1)
animals_list.add_to_list(hamster1)
animals_list.add_to_list(donkey1)
animals_list.add_to_list(camel1)
Menu.upgrade_command(dog1, 'meowmeeew')

while True:
    Menu.get_menu()
    choice = input()
    match choice:
        case '1':
            animals_list.print_list()
            print(counter.get_count())
        case '2':
            try:
                who = input('Введите индекс объекта в списке чтобы добавить команд: ')
                Menu.upgrade_command(animals_list.get_obj_of_index(int(who)), input('Какой команде обучим?: '))
            except IndexError:
                print('Такого элемента нет')
        case '3':
            try:
                who = input('Введите индекс объекта в списке чтобы посмотреть к кому относится: ')
                print(type(animals_list.get_obj_of_index(int(who))))
            except IndexError:
                print('Такого элемента нет')
        case '4':
            try:
                who = input('Введите индекс объекта в списке чтобы посмотреть что он умеет: ')
                print(Menu.get_command(animals_list.get_obj_of_index(int(who))))
            except IndexError:
                print('Такого элемента нет')
        case '5':
            stop = True
            count = 0
            counter = Counter()
            while stop:
                if count > 2:
                    print('Слишком много попыток')
                    break
                which_class = input('Какой класс животного хотите добавить: ')
                match which_class.lower():
                    case 'horse':
                        horse = Horse(input('Имя: '), input('Дата рождения: '), input('Функция: '))
                        print('Успешно')
                        counter.add()
                        counter.read_with_file()
                        stop = False
                    case 'donkey':
                        donkey = Donkey(input('Имя: '), input('Дата рождения: '), input('Функция: '))
                        print('Успешно')
                        counter.add()
                        counter.read_with_file()
                        stop = False
                    case 'camel':
                        camel = Camel(input('Имя: '), input('Дата рождения: '), input('Функция: '))
                        print('Успешно')
                        counter.add()
                        counter.read_with_file()
                        stop = False
                    case 'dog':
                        dog = Dog(input('Имя: '), input('Дата рождения: '), input('Функция: '))
                        print('Успешно')
                        counter.add()
                        counter.read_with_file()
                        stop = False
                    case 'cat':
                        cat = Cat(input('Имя: '), input('Дата рождения: '), input('Функция: '))
                        print('Успешно')
                        counter.add()
                        counter.read_with_file()
                        stop = False
                    case 'hamster':
                        hamster = Hamster(input('Имя: '), input('Дата рождения: '), input('Функция: '))
                        print('Успешно')
                        counter.add()
                        counter.read_with_file()
                        stop = False
                    case _:
                        count += 1

                    # print('Можно добавить только: horse, camel, donkey, dog, cat, hamster')

        case '0':
            print('Пока')
            exit()
