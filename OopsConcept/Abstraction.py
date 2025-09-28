class car:
    def __init__(self):
        self.acc=False
        self.brk=False
        self.cultch=False
    
    def start(self):
        self.acc=True
        self.cultch=True
        print("car started :")

s1=car()
s1.start()