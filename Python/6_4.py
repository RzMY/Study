key_words = {
    'if':'if语句',
    'while':'while语句',
    'for':'for语句',
}
print(f"if:\n{key_words['if']}")
print(f"while:\n{key_words['while']}")
print(f"for:\n{key_words['for']}\n")

for key,value in key_words.items():
    print(f"{key}:\n{value}")
print("\n")
key_words['print'] = 'print语句'
key_words['input'] = 'input语句'
key_words['del'] = 'del语句'

for key,value in key_words.items():
    print(f"{key}:\n{value}")