file = open("student.txt", "r")  # Open file in read mode
# file = open("student.txt", "r+")  # Open file in read & write mode

print(file.readable())  # Check file readable or not

text = file.read()  # Read file data
print(text)

size = len(text)
print("Length:", size)

# this will work when previous code is commented
text = file.readlines()     # assign in a list
print(text)
text = file.readlines()[1]  # print index/line wise
print(text)

# Print all data using loop
for line in file:
    print(line)

file.close()
