"""
total_inches = int(input("Enter number of inches: "))

feet = total_inches // 12
inches = total_inches % 12

print(f"{total_inches} inches is {feet} feet and {inches} inches")


"""

total_inches = int(input("Enter number of inches: "))

feet = total_inches // 12
inches = total_inches - (feet * 12)

print(f"{total_inches} inches is {feet} feet and {inches} inches")

