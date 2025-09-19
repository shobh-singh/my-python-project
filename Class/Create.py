class Car:
    # constructor: object create होते समय attributes initialize करता है
    def __init__(self, name, color):
        self.name = name
        self.color = color
    
    # method: object की जानकारी print करता है
    def show(self):
        print(f"Car: {self.name}, Color: {self.color}")

# Object creation (class के बाहर)
c1 = Car("BMW", "Black")
c1.show()
