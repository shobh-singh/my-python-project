class car:
    def __init__(self, type):
        self.type=type

    @staticmethod
    def start():
        print("Car Started")

class fortuner(car):
    def __init__(self, type,name):
        super().__init__(type)
        self.name=name

        super().start()

c1=fortuner("2024","scorpio")
print(c1.type)