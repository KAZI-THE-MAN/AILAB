"""
1.
def percentage_to_decimal(percentage):
    return percentage / 100


percentage = float(input("Enter a percentage: "))
decimal = percentage_to_decimal(percentage)
print("Decimal equivalent:", decimal)

2.
percentage = float(input("Enter a percentage: "))
decimal = "{:.2f}".format(percentage / 100)
print("Decimal equivalent:", decimal)
"""
percentage = float(input("Enter a percentage: "))
decimal = f"{percentage / 100:.2f}"
print("Decimal equivalent:", decimal)
