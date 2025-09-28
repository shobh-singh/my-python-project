# class student:
#     def __init__(self, name):
#         self.name=name
    
#     def hello(self):
#         print("Hello Method")

# s1=student("sodha")
# print("Welcome : ",s1.name)

# s1.hello()



class students:
    def __init__(self , name,marks):
        self.name=name
        self.marks=marks
    
    def Average(self):
        sum=0
        for val in self.marks:
            sum+=val
        print("hii",self.name,"marks score is",sum/3)

s1=students("Vikran",[89,99,98])
s1.Average()

#Update name

s1.name="Shobh"
s1.Average()

        
