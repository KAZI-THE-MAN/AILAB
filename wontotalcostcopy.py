"""
def calculate_copy_cost(num_copies):
    base_cost = 50  
    additional_cost = 30  

    if num_copies <= 100:
        total_cost = num_copies * base_cost
    else:
        total_cost = 100 * base_cost + (num_copies - 100) * additional_cost

    return total_cost

num_copies = int(input("Enter the number of copies: "))

total_cost = calculate_copy_cost(num_copies)


print("Total cost:", total_cost, "won")
"""

num_copies = int(input("Enter the number of copies: "))

if num_copies <= 100:
        total_cost = num_copies * 50
else:
        total_cost = 100 * 50 + (num_copies - 100) * 30
print("Total cost:", total_cost, "won")