def oper(x,y):

    yield x + y
    yield x - y
    yield x * y
    yield x / y


obj = oper(4, 3)
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
# print(next(obj))  # Errror