class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} barks: {sound}"

class JackRussellTerrier(Dog):
    def speak(self, sound="Arf"):
        return super().speak(sound)

class Bulldog(Dog):
    pass
jim = Bulldog("Jim", 5)
print(jim.speak("Woof"))
miles = JackRussellTerrier("Miles", 4)
print(miles.speak())

