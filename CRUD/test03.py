class Myclass2:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myFunction(self):
        print("Hello! My name is " + self.name)
        print("I'm " + self.age + " years old")


p1 = Myclass2("niloufar", "27")
p1.myFunction()