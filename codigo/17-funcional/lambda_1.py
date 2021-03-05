def func(f, arg):
    return f(arg)

y = func(lambda x: 2*x*x, 5)
print(y)  # 50