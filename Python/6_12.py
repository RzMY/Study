#字典的嵌套
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

#添加一个城市
cities['Moscow'] = {
    'Country': 'Russia',
    'Population': '12 million',
    'Fact': 'The capital of Russia',
}

for k_1,v_1 in cities.items():
    print(f"{k_1}:")
    for k_2,v_2 in v_1.items():
        print(f"{k_2}:{v_2}")
    print("\n")
    
#删除一个城市
del cities['New York']

for k_1,v_1 in cities.items():
    print(f"{k_1}:")
    for k_2,v_2 in v_1.items():
        print(f"{k_2}:{v_2}")
    print("\n")

#访问一个城市的信息
print(cities['Chengdu'])
print(cities['Chengdu']['Population'])


#修改一个城市的信息
cities['Chengdu']['Population'] = '15 million'

print(cities.get('Chengdu', 'No such city.'))
#get到成都的人口
print(cities.get('Chengdu', 'No such city.').get('Population', 'No such information.'))