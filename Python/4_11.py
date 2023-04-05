pizza = ['pepperoni', 'sausage', 'cheese', 'mushroom', 'pineapple']
for i in pizza:
    message = f"I like {i} pizza."
    print(message)
print("I really love pizza!")
friend_pizzas = pizza[:]#复制列表
#friend_pizzas = pizza#直接赋值，friend_pizzas和pizza指向同一个列表
