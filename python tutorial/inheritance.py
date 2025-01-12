#single inheritance

'''class Car:
    color = "black"
    @staticmethod
    def start():
        print("car started ")

    @staticmethod 
    def stop():
        print("car stopped ")

class  ToyotaCar(Car):
        def __init__(self , name):
            self.name = name

car1 = ToyotaCar("fortuner")
car2 = ToyotaCar("skoda")

print(car1.start())
print(car1.color)

'''

#multi-level inheritance 
'''
class Car():
    @staticmethod 
    def start():
        print("car started")

    @staticmethod 
    def stop():
        print("car stopped ")

class ToyotaCar(Car):
    def __init__(self , brand):
        self.brand = brand

class Fortuner(ToyotaCar):
    def __init__(self , Type):
        self.type = type 

car1 = Fortuner("diesel") 
car1.start()
car1.type()
'''
#multiple inheritance 
class A:
    varA = "welcome to class A "

class B:
    varB = "welcome to class B "


class C(A,B):
    varC = "welcome to class C"

c1 = C()

print(c1.varC)
print(c1.varB)
print(c1.varA)
















        
