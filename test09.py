from test08 import Calculator


inp1 = int(input("Please enter your first number: "))
inp2 = int(input("Please enter your second number: "))

app = Calculator(inp1, inp2)

output1 = app.add_numbers()
print("Summation:", output1)

output2 = app.sub_numbers()
print("Subtraction:",output2)

output3 = app.mul_numbers()
print("Multiplication:",output3)

output4 = app.div_numbers()
print("Division:", output4)

output5 = app.rem_numbers()
print("Remainder:", output5)

output6 = app.pow_numbers()
print("Power:", output6)
