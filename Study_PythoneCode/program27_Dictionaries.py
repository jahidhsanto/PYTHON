studentID = {
    "201002032" : "Asma Ul Husna",
    "201002081" : "Sayed Emon Alom",
    "201002143" : "Joy Munshi",
    "201002152" : "Sabrina Akter",
    "201002214" : "Raknat Jahan Aliz",
    "201002352" : "Bibek Chandra Dey",
    "201002463" : "Jahid Hassan"
}
print(studentID["201002032"])
print(studentID.get("201002081"))
print(studentID.get("20100208", "Not a valid key"))


student = {
    201002032 : "Asma Ul Husna",
    201002081 : "Sayed Emon Alom",
    201002143 : "Joy Munshi",
    201002152 : "Sabrina Akter",
    201002214 : "Raknat Jahan Aliz",
    201002352 : "Bibek Chandra Dey",
    201002463 : "Jahid Hassan"
}
print(studentID["201002032"])
print(studentID.get(201002081))
print(studentID.get(20100208, "Not a valid key"))
