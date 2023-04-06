pizza = ['pepperoni', 'sausage', 'cheese', 'mushroom', 'pineapple']
for pizza_0 in pizza:
    message = f"I like {pizza_0} pizza."
    print(message)
print("I really love pizza!")
friend_pizzas = pizza[:]#复制列表
#friend_pizzas = pizza#直接赋值，friend_pizzas和pizza指向同一个列表
pizza.append('bacon')
friend_pizzas.append('chicken') 
print(f"My favorite pizzas are:")
for pizza_1 in pizza:
    print(pizza_1)
print(f"My friend's favorite pizzas are:")
for pizza_2 in friend_pizzas:
    print(pizza_2)