current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue#continue语句让Python忽略余下的代码，并返回到循环开头
    print (current_number)