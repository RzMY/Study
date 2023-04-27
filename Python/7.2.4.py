prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\nEnter 'quit' when you are finished."

while True:
    city = input(prompt)
    
    if city == 'quit':
        print("You have quit the program.")
        break
    else:
        print(f"I'd love to go to {city.title()}")