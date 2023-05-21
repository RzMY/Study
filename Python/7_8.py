sandwich_orders = ['pastrami', 'tuna', 'pastrami', 'chicken', 'pastrami', 'beef']
finished_sandwiches = []
for sandwich in sandwich_orders:
    print(f"I made your {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)
print("\nAll sandwich orders have been made.")
print(finished_sandwiches)