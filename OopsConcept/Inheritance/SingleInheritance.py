class car:
    @staticmethod
    def start():
        print("car started:: ")
    @staticmethod
    def stop():
        print("car stoped")

class car1(car):
    def __init__(self):
        print("Hiii")

s1=car1()
s1.start()
