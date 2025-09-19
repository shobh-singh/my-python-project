class Engine:
    def start(self):
        print("Engine started")

class Music:
    def play(self):
        print("Playing music")

class Car(Engine, Music):
    pass

my_car = Car()
my_car.start()
my_car.play()
