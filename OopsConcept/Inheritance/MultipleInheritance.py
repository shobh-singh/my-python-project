class A:
    var1="Welcome A"

class B:
    var2="Welcome B"

class C(A,B):
    var3="Welcome C"

s1=C()
print(s1.var1)
print(s1.var2)
print(s1.var3)