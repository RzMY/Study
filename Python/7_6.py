#使用active变量来控制while循环，这样循环就可以在任何时候退出。
prompt = ("\nPlease enter the age of your family member:")
prompt += ("\nEnter 'quit' when you are finished.")

active = True

while active:
    age = input(prompt)
    if age == 'quit':
        active = False
        print("\nHope you enjoyed the movie.")
    else:
        age = int(age)
        if age < 3:
            print("\nThe ticket is free.")
        elif age >= 3 and age <= 12:
            print("\nThe ticket is $10.")
        elif age > 12:
            print("\nThe ticket is $15.")
            
prompt = ("\nPlease enter the age of your family member:")
prompt += ("\nEnter 'quit' when you are finished.")

#使用break语句来退出循环
while True:
    age = input(prompt)
    if age == 'quit':
        print("\nHope you enjoyed the movie.")
        break
    else:
        age = int(age)
        if age < 3:
            print("\nThe ticket is free.")
        elif age >= 3 and age <= 12:
            print("\nThe ticket is $10.")
        elif age > 12:
            print("\nThe ticket is $15.")

#使用while条件测试来退出循环
prompt = ("\nPlease enter the age of your family member:")
prompt += ("\nEnter 'quit' when you are finished.")

age = ''
while age != 'quit':
    age = input(prompt)
    if age == 'quit':
        print("\nHope you enjoyed the movie.")
    else:
        age = int(age)
        if age < 3:
            print("\nThe ticket is free.")
        elif age >= 3 and age <= 12:
            print("\nThe ticket is $10.")
        elif age > 12:
            print("\nThe ticket is $15.")