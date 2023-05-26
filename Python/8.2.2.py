#关键字实参，关键字实参是传递给函数的名称-值对

def describe_pet(animal_type,pet_name):
    """Display information about a pet"""
    print(f"I have a {animal_type}, it's name is {pet_name.title()}.")
    
describe_pet(pet_name='kiko',animal_type='cat')
describe_pet(animal_type='dog',pet_name='dabai')