favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
for name,language in favorite_language.items():
    print(f"{name.title()}'s favorite language is {language}")
    
print("\n")

investigate_list = ['jen','qzs','sarah','edward','phil','zmj','wyh','zhs','cwj']
for people in investigate_list:
    if people in favorite_language.keys():
        print(f"{people.title()},thank you for your response.")
    else:
        print(f"{people.title()},please take the investigate.")
