class car:
    @staticmethod
    def start():
        print("car started:: ")
    @staticmethod
    def stop():
        print("car stoped")


class car1(car):
    def A(self,a):
        print(a)

class car2(car1):
    def __init__(self):
        print("Hiii")

s1=car2()
s1.start()
s1.A(10)