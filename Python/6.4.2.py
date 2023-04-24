pizza = {'crust':'think',
         'toppings':['mushrooms','extra cheese'],
         }

print(f"You ordered a {pizza['crust']}-crust pizza")

for topping in pizza['toppings']:
    print("\t" + topping)
    
favorite_languages = {'jen':['python','ruby'],
                      'sarsh':['c'],
                      'edward':['ruby','go'],
                      'phil':['python','haskell'],
                      }

for name,languages in favorite_languages.items():
    print(f"{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")