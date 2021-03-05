a = ['x', 'y']
b = a.copy()
b[0] = 'z'
print(b)  # ['z', 'y']
print(a)  # ['x', 'y']