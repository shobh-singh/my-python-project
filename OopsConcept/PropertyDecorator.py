class marks:
    def __init__(self, phy,math,his):
        self.phy=phy
        self.math=math
        self.his=his
    
    @property
    def percentage(self):
        return str((self.phy+self.math+self.his)/3)+"%"
    
s1=marks(98,87,99)
print(s1.percentage)

s1.math=85

print(s1.math)

print(s1.percentage)

