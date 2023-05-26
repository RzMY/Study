# def describe_pet(animal_type='cat',pet_name):
# 有问题，非默认值形参必须在默认值形参前面
animal = 'cat'
#函数默认值只在定义函数时初始化一次，如果默认值是列表或字典，可以使用函数来修改
def describe_pet(pet_name,animal_type=animal):
    print(f"I have a {animal_type}, it's name is {pet_name.title()}.")
    animal = 'dog'
animal = 'dog'

describe_pet('kiko')
describe_pet(pet_name='kiko')
#animal_type='cat'是默认值，如果调用函数时给animal_type提供了实参，python将忽略这个形参的默认值
describe_pet('dabai','dog')