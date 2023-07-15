from homeAnimal import HomeAnimal


class Hamster(HomeAnimal):
    def __init__(self, name: str, data_of_birth: str, function: []):
        HomeAnimal.__init__(self, data_of_birth, name)
        self.function = function

    def __str__(self):
        return f'(Имя: {self.name}, Дата рождения: {self.data_of_birth}, Функции: {self.function})'

    def get_function(self):
        return self.function

    def is_hamster(self):
        return True

    def add_function(self, function: str):
        self.function.append(function)
