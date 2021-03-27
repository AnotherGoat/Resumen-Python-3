
from itertools import takewhile

nums = range(10)

print(list(nums))
print(list(takewhile(lambda x: x <= 5, nums)))