from animals import Animals


class HomeAnimal(Animals):
    def __init__(self, data_of_birth: str, name: str):
        Animals.__init__(self, data_of_birth)
        self.name = name

    def is_home(self):
        return True

    def get_name(self):
        return self.name

