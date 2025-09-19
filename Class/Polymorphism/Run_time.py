class A:
    def Add(self):
        print("Hii")

class B(A):
    def Add(self):
        print("Hello")

class C(A):
    def Add(self):
        print("Hello")

c1=[B(),C(),A()]

for D in c1:
    D.Add()