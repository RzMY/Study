def describe_city(city_name,country='China'):
    print(f"{city_name.title()} is in {country.title()}.")
    
describe_city('beijing')
describe_city(city_name='shanghai')
describe_city('tokyo','japan')
describe_city(city_name='new york',country='america')