def A(func):

    def wrapper():
        print("Hii")

        func()
        print("hello")

    return wrapper

@A
def sayhello():
    print("hii sayhello")

sayhello()
