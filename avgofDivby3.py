total = 0
count = 0

for num in range(3, 100, 3):
    total += num
    count += 1

average = total / count
print("Average:", average)

"""
import numpy as np

average = np.mean([num for num in range(3, 100, 3)])
print("Average:", average)
"""

