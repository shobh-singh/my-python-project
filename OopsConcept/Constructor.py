class car:
    def __init__(self , fullname,marks):
        self.name= fullname
        self.marks=marks
        print("My Car")

s1=car("vikram",98)
print(s1.name,s1.marks)

s2=car("pk",99)
print(s2.name,s2.marks)