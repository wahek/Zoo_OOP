class Counter:
    def __init__(self):
        self.data = self.read_with_file()

    def get_count(self):
        return self.data

    def read_with_file(self):
        try:
            with open("count.txt", "r") as file:
                value = int(file.read())
        except FileNotFoundError:
            value = 0
        return value

    def add(self):
        self.data += 1
        with open("count.txt", "w") as file:
            file.write(str(self.data))
