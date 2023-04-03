tourist_places = ['Iceland','Norway','Switzerland','American','Canada']
print(tourist_places[0])#索引从0开始
print(tourist_places[-1])#索引倒数从-1开始
tourist_places.append('japan')#在末尾添加元素
print(tourist_places)
message_0 = f"I heard that {tourist_places[-1].title()} is a beautiful place."#title()首字母大写
print(message_0)
tourist_places.insert(0,'China')#在指定位置添加元素
print(tourist_places)
message_1 = f"I am in {tourist_places.pop(0)}"#删除指定位置元素
print(message_1)
print(tourist_places)
tourist_places.remove('American')#删除指定元素
print(tourist_places)
del tourist_places[-1]#删除指定位置元素
print(tourist_places)
message_2 = ""
for i in tourist_places:
    message_2 = message_2 + i + "、"#打印列表的时候去掉中括号,并且用、隔开
print(f"I want to go to {message_2}, these {len(tourist_places)} places")#打印列表的时候去掉中括号