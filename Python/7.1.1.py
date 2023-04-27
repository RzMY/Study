message = input("Tell me something, and I will repeat it back to you:")
print(message)

name = input("Please enter your name:")
print (f"\nHello, {name}!")

prompt = "If you tell us who you are, we can personalize the message you see."
prompt += "\nWhat is your first name?"
message = input(prompt)
print (f"\nHello, {message}")