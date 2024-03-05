numbers = [23, 45, 12, 67, 8, 34]
numbers.sort()
total = numbers[0] + numbers[-1]
print("Sum of smallest and largest number:", total)


numbers = [23, 45, 12, 67, 8, 34]
total = min(numbers) + max(numbers)
print("Sum of smallest and largest number:", total)


numbers = [23, 45, 12, 67, 8, 34]
total = sum([min(numbers), max(numbers)])
print("Sum of smallest and largest number:", total)


numbers = [23, 45, 12, 67, 8, 34]
smallest = largest = numbers[0]

for num in numbers:
    if num < smallest:
        smallest = num
    elif num > largest:
        largest = num

total = smallest + largest
print("Sum of smallest and largest number:", total)



import numpy as np

numbers = [23, 45, 12, 67, 8, 34]
total = np.min(numbers) + np.max(numbers)
print("Sum of smallest and largest number:", total)
