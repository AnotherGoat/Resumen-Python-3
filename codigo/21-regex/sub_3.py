import re

for i in range(1, 8):
    print(re.sub(r"10", "*", "10101010101010", count=i))