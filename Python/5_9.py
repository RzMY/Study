user = ['admin','jack','mike','lucy','tom']
for user_0 in user:
    if user_0 == 'admin':
        print("Hello admin,would you like to see a status report?")
    else:
        print("Hello "+user_0+",thank you for logging in again.")
if user == []:
    print("We need to find some users!")
else:
    print(f"We have {len(user)} users.")
user.clear()
if user == []:
    print("We need to find some users!")