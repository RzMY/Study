num = 5

if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")


age = 25
if age >= 18 and age <= 60:
    print("You are an adult.")


# 多个条件的组合示例

# 条件1：x > 0 且 y > 0
x = 5
y = 10
if x > 0 and y > 0:
    print("Both x and y are positive.")

# 条件2：x > 0 或 y > 0
x = 5
y = -2
if x > 0 or y > 0:
    print("Either x or y is positive.")

# 条件3：x 不是正数
x = 5
if not x > 0:
    print("x is not positive.")


age = 20
message = "You are an adult." if age >= 18 else "You are not an adult."
print(message)


num = 5
assert num > 0, "The number must be positive."
