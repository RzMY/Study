#位置实参，基于实参的顺序，调用函数时，python将每个实参关联到函数定义中的形参

def describe_pet(animal_type,pet_name):
    """Display information about a pet"""
    print(f"I have a {animal_type}, it's name is {pet_name.title()}.")
    
describe_pet('cat','kiko')

describe_pet('dog','dabai')