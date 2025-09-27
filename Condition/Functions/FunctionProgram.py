print("Function Without Parameter")

def greet():
    print("Hello, Vikaram")

greet()




print("Parameter Function")

def animal(name):
    print(f"Hello,{name}")

animal("Lion")
animal("Tiger")




print("Function with Return value")

def A(a,b):
    return a+b

result=A(12,2.3)
print(result)




print("Function With Default Parameter")

def B(name="Vikram"):
    print(f"Hello,{name}")

B()
B("Amit")




print("Function With KeyWord Argument")

def describe(name, age):
    print(f"{name} is {age} years old.")

describe(age=25, name="Bob")



print("Function with arbitrary number of arguments")

def add_numbers(*args):
    return sum(args)

print(add_numbers(1, 2, 3, 4))



def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25, city="London")


