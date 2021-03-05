from itertools import accumulate

nums = list(accumulate(range(8)))

print(list(range(8)))  # [0, 1, 2, 3, 4, 5, 6, 7]
print(nums)  # [0, 1, 3, 6, 10, 15, 21, 28]