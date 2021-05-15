class Information:
    def __init__(self, name, family_name, age, national_code):
        self.name = name
        self.family_name = family_name
        self.age = age
        self.national_code = national_code




p1 = Information("Niloufar", "Rahimizade", "27", "273012587")
p2 = Information("Amir", "Rahimizadeh", "15", "2738520912")
print(p1.national_code)