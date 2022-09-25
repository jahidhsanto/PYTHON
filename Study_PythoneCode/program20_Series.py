# 1 + 2 + 3 + ... + n
n = int(input("Enter the last number: "))
sum = 0
for x in range(1, n + 1, 1):
    sum += x
print("Sum of", n, "numbers: ", sum)

# 2 + 4 + 6 + ... + n (sum of even numbers from 1-n)
sum = 0
for x in range(2, n + 1, 2):
    sum += x
print("Sum of even numbers: ", sum)

# 1 + 3 + 5 + ... + n (sum of odd numbers from 1-n)
sum = 0
for x in range(1, n + 1, 2):
    sum += x
print("Sum of odd numbers: ", sum)

# 1^2 + 2^2 + 3^2 + ... + n^2
sum = 0
for x in range(1, n + 1, 1):
    sum += pow(x, 2)
print("Sum of odd numbers: ", sum)
