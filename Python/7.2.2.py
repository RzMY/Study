prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to quit the program."

message = ""

while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(f"\n{message}")
    else:
        print("You have quit the program.")