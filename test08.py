class Calculator:
    def __init__(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2
    def add_numbers(self):
        return self.num_1 + self.num_2

    def sub_numbers(self):
        return self.num_1 - self.num_2

    def mul_numbers(self):
        return self.num_1 * self.num_2

    def div_numbers(self):
        return self.num_1/self.num_2

    def rem_numbers(self):
        return self.num_1%self.num_2

    def pow_numbers(self):
        return self.num_1 ** self.num_2
