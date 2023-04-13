pet_1 = {
    'name':'nanci',
    'type':'dog',
    'color':'white',
}
pet_2 = {
    'name':'nangua',
    'type':'cat',
    'color':'black',
}
pet_3 = {
    'name':'xigua',
    'type':'dog',
    'color':'yellow',
}
pets = [pet_1,pet_2,pet_3]

for pet in pets:
    for k,v in pet.items():
        print(f"{k}:{v}")
    print("\n")