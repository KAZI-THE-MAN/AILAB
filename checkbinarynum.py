"""input_string = input("Enter a string: ")
if all(char in '01' for char in input_string):
    print("Binary Number")
else:
    print("Not a Binary Number")
"""
def is_binary(string):
    for char in string:
        if char not in '01':
            return False
    return True

input_string = input("Enter a string: ")
if is_binary(input_string):
    print("Binary Number")
else:
    print("Not a Binary Number")


