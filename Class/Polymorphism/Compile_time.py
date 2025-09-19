class Add:
    def Sum1(self, a,b,c=0):
        return a+b+c
    
c1=Add()
print(c1.Sum1(2,3))
print(c1.Sum1(2,5,7))