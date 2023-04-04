#classTest.py

# class test(object):
#     int i
#     int j
#     str k

class Person:
    def __init__(self):
        self.age = "30"
        self.name = "default name"
    def print(self):
        print("My name is {0}, age is {1}".format(self.name, self.age))
p1 = Person()
p1.print()

