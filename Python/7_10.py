active = True
user = {}
while active:
    name = input("What is your name?")
    place = input("If you could visit one place in the world, where would you go?")
    
    user[name] = place
    
    another_people = input("Would you like to let another person respond? (yes/no)")
    if another_people == 'no':
        active = False
for name,place in user.items():
    print(f"{name.title()} would like to go to {place.title()}")