# xargs
def student(id, name):
    print(id, name)


student(101, "Badhon")


# Number of parameter constant but any number of argument can pass
def student(*details):  # This is works like tuples
    print(details)
    print(details[1])


student(101, "Badhon")
student(101, "Badhon", 3.75)


def add(*numbers):
    sum = 0
    for x in numbers:
        sum = sum + x
    print(sum)


add(10, 20)
add(10, 20, 30)
add(10, 20, 30, 40)


########################################
# xxargs
def student(**love):
    print(love)
    print(love["name"])


student(id=101, name="Asma")
