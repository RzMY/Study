print(4 % 3)#%是求余数的运算符，4除以3的余数是1

number = input("Enter a number, and I'll tell you if it's even or odd:")
number = int(number)
if number % 2 == 0:
    print(f"The number {number} is even.")
else:
    print(f"The number {number} is odd.")