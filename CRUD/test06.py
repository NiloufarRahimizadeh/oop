class Information:
    def __init__(self, name, family_name, age, national_code):
        self.name = name
        self.family_name = family_name
        self.age = age
        self.national_code = national_code
    
    def display_info(self):
        print("My name is " + self.name+ ".")
        print("I'm "+ self.age +" years old.")
p1 = Information("amir", "rahimizadeh", "15", "2730548752")
del p1.age

p1.display_info()