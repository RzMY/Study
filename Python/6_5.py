rivers = {
    'Yangtze': 'China',
    'Nile': 'Egypt',
    'Amazon': 'Brazil',
    'Mississippi': 'United States',
}

for river,country in rivers.items():
    print(f"The {river} runs through {country}.")
print("\n")

for river in rivers.keys():
    print(river)

print("\n")

for country in rivers.values():
    print(country)