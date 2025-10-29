def add(x) :
    return x + 3

def func(*args) :
    result = map(add, args)
    return result


result = func(1,2,3,4)
print(list(result))