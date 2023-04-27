prompt = "\nPlease enter the ingredients you want to add to your pizza:"
prompt += "\nEnter 'quit' when you are finished."

active = True

while active:
    ingredient = input(prompt)
    if ingredient == 'quit':
        active = False
        print("Your pizza is being prepared.")
    else:
        print(f"We will add {ingredient} in your pizza.")