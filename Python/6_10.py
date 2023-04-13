favorite_number = {
    'qzs': [1,2,3],
    'zmj': [2,3,4],
    'wyh': [3,4,5],
    'zhs': [4,5,6],
    'cwj': [5,6,7],
}
for k,v in favorite_number.items():
    print(f"{k.title()}'s favorite number is:",end="")
    for i in v:
        print(i,end=" ")
    print("\n")

        