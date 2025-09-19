class A:
    def info_a(self):
        print("Class A")

class B(A):
    def info_b(self):
        print("Class B")

class C(A):
    def info_c(self):
        print("Class C")

class D(B, C):
    def info_d(self):
        print("Class D")

d = D()
d.info_a()  # from A
d.info_b()  # from B
d.info_c()  # from C
d.info_d()  # from D
