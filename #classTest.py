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

p2 = Person()
p2.name = "전우치"
p2.test="test"
p2.print() 

#런타임 변수 추가

Person.title = "new title"
print(p1.title)
print(p2.title)
print(Person.title)