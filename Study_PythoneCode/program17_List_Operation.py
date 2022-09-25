subjects = ["C", "C++", "Java", "Python", "Android", "OS", "TOC"]
print(len(subjects))

subjects.append("JAHID")
print(subjects)

subjects.insert(2, "INSERT")
print(subjects)

subjects.remove("INSERT")
print(subjects)

subjects.sort()
print(subjects)

subjects.reverse()
print(subjects)

subjects.pop()
print(subjects)

subjects2 = subjects.copy()
print("Subjects2", subjects2)

subjects2.clear()
print(subjects2)

print(subjects.index("Java"))

print(subjects.count("Java"))
