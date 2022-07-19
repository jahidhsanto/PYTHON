def add(a, b):
    sum = a + b
    return sum


result = add(20, 30)
print("Result: ", result)


def large(a, b):
    if a > b:
        return a
    else:
        return b


print("Large: ", large(20, 30))

# Use valiable as funciton
maximum=large
print("Large: ", maximum(20, 30))
