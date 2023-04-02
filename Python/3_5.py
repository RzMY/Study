friends = ['QZS','ZHS','ZMJ']
#message_1 = f"Hello {friends[0]},would you like to eat dinner with me?"
#message_2 = f"Hello {friends[1]},would you like to eat dinner with me?"
#message_3 = f"Hello {friends[2]},would you like to eat dinner with me?"
#print(message_1)
#print(message_2)
#print(message_3)
for i in friends:
    print(f"Hello {i},would you like to eat dinner with me?")
busy_friend = friends.pop(0)
print(f"{busy_friend} can't come to dinner.")
friends.insert(2,'WYH')
for i in friends:
    print(f"Hello {i},would you like to eat dinner with me?")
print("I found a bigger table.")
friends.insert(0, 'XYJ')
friends.insert(2, 'AHY')
friends.append('YZY')
for i in friends:
    print(f"Hello {i},would you like to eat dinner with me?")
print("I can only invite two people to dinner.")
for i in range(0,4):
    print(f"Sorry {friends.pop(0)},I can't invite you to dinner.")
for i in friends:
    print(f"hello{i},you are still invited to dinner.")
#for i in friends:
#    friends.remove(i)#用for循环删除列表中的元素会报错，因为列表长度在变化，所以要用while循环
#friends.clear()#清空列表
#用while循环删除列表中的元素
while friends:#列表不为空时，循环
    friends.pop()
if friends == []:
    print("The list is empty.")
else:
    print("The list is not empty.")
print (friends)