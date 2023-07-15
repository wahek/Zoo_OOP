class Animals(object):
    def __init__(self, data_of_birth: str):
        self.data_of_birth = data_of_birth

    def get_alive(self):
        return True

    def get_data_of_birth(self):
        return self.data_of_birth
