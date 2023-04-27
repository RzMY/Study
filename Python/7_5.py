prompt = ("\nPlease enter the age of your family member:")
prompt += ("\nEnter 'quit' when you are finished.")

active = True

while active:
    age = input(prompt)
    if age == 'quit':
        active = False
        print("\nHope you enjoyed the movie.")
    else:
        age = int(age)
        if age < 3:
            print("\nThe ticket is free.")
        elif age >= 3 and age <= 12:
            print("\nThe ticket is $10.")
        elif age > 12:
            print("\nThe ticket is $15.")