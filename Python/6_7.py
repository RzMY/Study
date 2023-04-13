friend_1 = {
    'name':'qzs',
    'first_name':'q',
    'last_name':'zs',
    'age':19,
    'city':'nanchong',
}
friend_2 = {
    'name':'zmj',
    'first_name':'z',
    'last_name':'mj',
    'age':18,
    'city':'chengdu',
}
friend_3 = {
    'name':'wyh',
    'first_name':'w',
    'last_name':'yh',
    'age':18,
    'city':'nanchong',
}
people = []
people.append(friend_1)
people.append(friend_2)
people.append(friend_3)
print(people)
for friend in people:
    for k,v in friend.items():
        print(f"{k}:{v}")
    print("\n")