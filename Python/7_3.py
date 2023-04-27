num = input("Please enter a number, and I'll tell you if it's multiple of 10:")

num = int(num)

if num % 10 == 0:
    print(f"The number {num} is multiple of 10.")
else:
    print(f"The number {num} is not multiple of 10.")