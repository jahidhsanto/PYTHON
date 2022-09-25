# Can't store duplicate values
num1 = {1, 2, 3, 4, 5, 5}  # This is a set
num2 = set([4, 5, 6, 7])  # List convert to Set
num2.add(8)
print(num2)
num2.remove(8)
print(num2)
print(4 in num2)

# Operation for set
print(num1 | num2)  # UNION
print(num1 & num2)  # INTERSECTION
print(num1 - num2)  # DIFFERENCE
