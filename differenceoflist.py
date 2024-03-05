numbers = [23, 45, 12, 67, 8, 34, 55, 19, 30, 42]
smallest = largest = numbers[0]
total = 0

for num in numbers:
    total += num
    if num < smallest:
        smallest = num
    elif num > largest:
        largest = num

average = total / len(numbers)
difference_smallest = average - smallest
difference_largest = largest - average
print("Difference between average and smallest number:", difference_smallest)
print("Difference between average and largest number:", difference_largest)


numbers = [23, 45, 12, 67, 8, 34, 55, 19, 30, 42]
average = sum(numbers) / len(numbers)
difference_smallest = average - min(numbers)
difference_largest = max(numbers) - average
print("Difference between average and smallest number:", difference_smallest)
print("Difference between average and largest number:", difference_largest)


numbers = [23, 45, 12, 67, 8, 34, 55, 19, 30, 42]
numbers.sort()
average = sum(numbers) / len(numbers)
difference_smallest = average - numbers[0]
difference_largest = numbers[-1] - average
print("Difference between average and smallest number:", difference_smallest)
print("Difference between average and largest number:", difference_largest)
