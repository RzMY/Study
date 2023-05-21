sandwich_orders = ['pastrami', 'tuna', 'pastrami', 'chicken', 'pastrami', 'pastrami' , 'beef' ,'pastrami']
print("There is no pastrami.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
finished_sandwiches = []
for sandwich in sandwich_orders:
    print(f"I made your {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)
print("\nAll sandwich orders have been made.")
print(finished_sandwiches)