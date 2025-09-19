class Grandparent:
    def info_grandparent(self):
        print("Grandparent class")

class Parent(Grandparent):
    def info_parent(self):
        print("Parent class")

class Child(Parent):
    def info_child(self):
        print("Child class")

c = Child()
c.info_grandparent()
c.info_parent()
c.info_child()
