
numbers = []


for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)


for i in range(1, 6):
    subset_sum = sum(numbers[:i])
    print(f"Sum of the first {i} numbers:", subset_sum)
