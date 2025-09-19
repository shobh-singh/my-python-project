class vahicle:
    def A(self):
        pass
    def B(self):
        print("ooh ")

class Car(vahicle):
    def A(self):
        print("hii")

class bike(vahicle):
    def A(self):
        print("hello")

c1=Car()
c1.A()
c1.B()