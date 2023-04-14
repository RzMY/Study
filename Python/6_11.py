cities = {
    'Chengdu': {
        'Country': 'China',
        'Population': '14 million',
        'Fact': 'The capital of Sichuan Province',
    },
    'Tokyo': {
        'Country': 'Japan',
        'Population': '13 million',
        'Fact': 'The capital of Japan',
    },
    'New York': {
        'Country': 'United States',
        'Population': '8 million',
        'Fact': 'The capital of New York State',
    },
}

for k_1,v_1 in cities.items():
    print(f"{k_1}:")
    for k_2,v_2 in v_1.items():
        print(f"{k_2}:{v_2}")
    print("\n")