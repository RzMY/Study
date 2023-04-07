food = 'bacon'
print("Is food == 'bacon'? I predict True.")
print(food == 'bacon')
print("Is food == 'chicken'? I predict False.")
print(food == 'chicken')
number = 10
print("Is number == 10? I predict True.")
print(number == 10)
print("Is number == 20? I predict False.")
print(number == 20)
print("Is number != 20? I predict True.")
print(number != 20)
a = 10
b = 20
print("Is a>b? I predict False.")
print(a>b)
print("Is a<b? I predict True.")
print(a<b)
print("Is a>=b? I predict False.")
print(a>=b)
print("Is b<=20? I predict True.")
print(b<=20)
print("Is a==10 and b==20? I predict True.")
print(a==10 and b==20)#用and连接的两个条件都为True时，结果才为True
print("Is a>=15 or b>=15? I predict True.")
print(a>=15 or b>=15)#用or连接的两个条件只要有一个为True，结果就为True
number_list = list(range(1,21,3))
print(number_list)
print("Is 1 in number_list? I predict True.")
print(1 in number_list)
print("Is 2 in number_list? I predict False.")
print(2 in number_list)#in判断某个值是否在列表中
print("Is 2 not in number_list? I predict True.")
print(2 not in number_list)#not in判断某个值是否不在列表中