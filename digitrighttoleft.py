num = int(input("Enter a number: "))
num_str = str(num)
for digit in num_str[::-1]:
    print(digit)


num = int(input("Enter a number: "))
while num > 0:
    digit = num % 10
    print(digit)
    num //= 10
