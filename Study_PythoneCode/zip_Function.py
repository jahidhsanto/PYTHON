roll = [101, 102, 103, 104, 105, 106, 107]
name = ["Badhon", "Jahid", "Joy", "Bibek", "Sabrina", "Aliz", "Emon"]

# We want to combine these two list into one list
# Our expected:
# [(101, "Badhon"), (102,"Jahid"),  ........]

print(list(zip(roll, name)))
print(list(zip(roll, name, "ABABAB")))
