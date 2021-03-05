
from itertools import takewhile

nums = range(10)

print(list(nums))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(takewhile(lambda x: x <= 5, nums)))  # [0, 1, 2, 3, 4, 5]