guest_number = input("Please enter the number of guests:")

num = int(guest_number)

if num > 8:
    print("Sorry, you have to wait for a table.")
else:
    print("Your table is ready.")