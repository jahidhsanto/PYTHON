# A function without name (Anonymous Function)
# Not Powerful as Named Function
# It can work with single expression/single line of code


def calculate(a, b):
    return a * a + 2 * a * b + b * b
print(calculate(2, 3))

# Convert this to Lambda_Function

# SYNTAX
# lambda parameter : expression
L = (lambda a, b: a * a + 2 * a * b + b * b)(2, 3)
print(L)
