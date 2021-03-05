from itertools import takewhile

nums = [1, 2, 3, 4, 5, 4, 3, 2, 1]
print(list(takewhile(lambda x: x <= 3, nums)))  # [1, 2, 3]
print(list(filter(lambda x: x <= 3, nums)))  # [1, 2, 3, 3, 2, 1]